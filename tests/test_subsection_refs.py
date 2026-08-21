import contextlib
import io
import os
import shutil
import tempfile
import unittest
from unittest import mock

from bs4 import BeautifulSoup

from sds.sds import (_apply_numbering, _apply_reference_captions,
                     _collect_subsection_numbers, _h2_labels)
from sds.toc import TOC


def section_html(*headings):
    """Build a page in the shape Sphinx gives second-level headings.

    Each heading is a (slug, labels, title) triple; docutils writes the labels
    declared with '(label)=' as empty <span> targets before the <h2>.
    """
    out = ['<html><body><article>']
    for slug, labels, title in headings:
        targets = ''.join(f'<span id="{lab}"></span>' for lab in labels)
        out.append(f'<section id="{slug}">\n{targets}<h2>{title}</h2>\n'
                   f'<p>text</p>\n</section>')
    out.append('</article></body></html>')
    return '\n'.join(out)


def ref(href, text, classes='reference internal'):
    return f'<a class="{classes}" href="{href}">' \
           f'<span class="std std-ref">{text}</span></a>'


class TestCollectSubsectionNumbers(unittest.TestCase):

    def setUp(self):
        self.build = tempfile.mkdtemp()
        self.toc = TOC(language='it')
        self.toc.add_chapter('c1/intro', 'chap_intro', 'Intro')
        self.toc.add_section('c1/dati', 'sec_dati', 'Dati')
        self.toc.add_section('c1/liste', 'sec_liste-page', 'Liste')

    def tearDown(self):
        shutil.rmtree(self.build)

    def write(self, rel_path, content):
        path = os.path.join(self.build, rel_path + '.html')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    def test_numbers_follow_heading_order(self):
        self.write('c1/dati', section_html(
            ('prima', [], 'Prima'),
            ('seconda', ['sec-seconda'], 'Seconda'),
            ('terza', ['sec-terza'], 'Terza')))
        numbers = _collect_subsection_numbers(self.build, self.toc)
        # Unlabelled headings still take their turn in the numbering.
        self.assertEqual(numbers['sec-seconda'], '1.1.2')
        self.assertEqual(numbers['sec-terza'], '1.1.3')

    def test_chapter_pages_get_two_level_numbers(self):
        self.write('c1/intro', section_html(('sola', ['sec-sola'], 'Sola')))
        numbers = _collect_subsection_numbers(self.build, self.toc)
        self.assertEqual(numbers['sec-sola'], '1.1')

    def test_slugs_are_not_collected(self):
        # Slugs repeat across pages ('esercizi', …), so they cannot identify a
        # heading and must stay out of the map.
        self.write('c1/dati', section_html(('esercizi', [], 'Esercizi')))
        self.write('c1/liste', section_html(('esercizi', [], 'Esercizi')))
        numbers = _collect_subsection_numbers(self.build, self.toc)
        self.assertEqual(numbers, {})

    def test_several_labels_on_one_heading(self):
        self.write('c1/dati', section_html(
            ('unica', ['sec-uno', 'sec-due'], 'Unica')))
        numbers = _collect_subsection_numbers(self.build, self.toc)
        self.assertEqual(numbers['sec-uno'], '1.1.1')
        self.assertEqual(numbers['sec-due'], '1.1.1')

    def test_labels_are_lowercased(self):
        self.write('c1/dati', section_html(('unica', ['Sec-Mixed'], 'Unica')))
        numbers = _collect_subsection_numbers(self.build, self.toc)
        self.assertIn('sec-mixed', numbers)

    def test_missing_page_is_skipped(self):
        self.assertEqual(_collect_subsection_numbers(self.build, self.toc), {})


class TestApplyNumberingOnStalePage(unittest.TestCase):
    """A page Sphinx left behind for a renamed/deleted source file has no number
    in the TOC; numbering must report it, not fail on it."""

    def setUp(self):
        self.toc = TOC(language='it')
        self.toc.add_chapter('P3/c4/variabili-aleatorie', 'chap_va', 'Variabili')
        self.toc.add_section('P3/c4/misure-di-centralita', 'sec_centralita',
                             'Misure di centralità')

    def page(self, title):
        return BeautifulSoup(
            '<html><body>'
            '<nav class="bd-links"><ul><li><a href="#">root</a></li>'
            '<li><a href="#">Variabili</a></li></ul></nav>'
            f'<article><section><h1>{title}</h1></section></article>'
            '</body></html>', 'html.parser')

    def apply(self, soup, rel_path):
        with mock.patch('sds.sds.get_root_doc', return_value='landing'), \
                contextlib.redirect_stdout(io.StringIO()) as out:
            changed = _apply_numbering(
                soup, f'build/sds/it/{rel_path}.html', 'it', self.toc,
                number_subsections=True)
        return changed, out.getvalue()

    def test_stale_page_is_reported_and_left_alone(self):
        soup = self.page('Misure di centralità')
        changed, output = self.apply(soup, 'P3/c4/valore-atteso')
        self.assertFalse(changed)
        self.assertIn('P3/c4/valore-atteso', output)
        self.assertIn('_toc.yml', output)
        self.assertEqual(soup.find('h1').get_text(), 'Misure di centralità')

    def test_page_in_the_toc_is_still_numbered(self):
        soup = self.page('Misure di centralità')
        changed, _ = self.apply(soup, 'P3/c4/misure-di-centralita')
        self.assertTrue(changed)
        self.assertEqual(soup.find('h1').get_text(),
                         '1.1. Misure di centralità')

    def test_root_doc_is_not_numbered(self):
        soup = self.page('Superhero Data Science')
        changed, output = self.apply(soup, 'landing')
        self.assertTrue(changed)
        self.assertEqual(output, '')
        self.assertEqual(soup.find('h1').get_text(),
                         'Superhero Data Science')


class TestH2Labels(unittest.TestCase):

    def test_labels_are_read_from_target_spans(self):
        soup = BeautifulSoup(section_html(
            ('le-liste', ['sec-liste', 'sec-elenchi'], 'Le liste')),
            'html.parser')
        self.assertEqual(_h2_labels(soup.find('h2')),
                         ['sec-elenchi', 'sec-liste'])

    def test_no_labels(self):
        soup = BeautifulSoup(section_html(('esercizi', [], 'Esercizi')),
                             'html.parser')
        self.assertEqual(_h2_labels(soup.find('h2')), [])


class TestApplyReferenceCaptions(unittest.TestCase):

    def setUp(self):
        self.toc = TOC(language='it')
        self.toc.add_chapter('c1/intro', 'chap_intro', 'Intro')
        self.toc.add_section('c1/dati', 'sec_dati', 'Dati')
        self.subsection_numbers = {'sec-liste': '1.1.3'}

    def captions(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        _apply_reference_captions(soup, self.toc, self.subsection_numbers)
        return [a.get_text() for a in soup.select('a')]

    def test_implicit_ref_to_subsection(self):
        html = ref('dati#sec-liste', 'Le liste',
                   'sds-secref reference internal')
        self.assertEqual(self.captions(html), ['Paragrafo 1.1.3'])

    def test_numref_to_subsection_keeps_only_the_number(self):
        html = ref('dati#sec-liste', 'Le liste',
                   'only-number reference internal')
        self.assertEqual(self.captions(html), ['1.1.3'])

    def test_ref_with_its_own_caption_is_left_alone(self):
        # {ref}`lista <sec_liste>` and [lista](sec_liste) reach post-processing
        # without the sds-secref class.
        html = ref('dati#sec-liste', 'lista')
        self.assertEqual(self.captions(html), ['lista'])

    def test_page_reference_still_resolved(self):
        html = ref('dati#sec-dati', 'Dati', 'sds-secref reference internal')
        self.assertEqual(self.captions(html), ['Paragrafo 1.1'])

    def test_page_numref_still_resolved(self):
        html = ref('dati#sec-dati', 'Dati', 'only-number reference internal')
        self.assertEqual(self.captions(html), ['1.1'])

    def test_unknown_label_is_left_alone(self):
        html = ref('dati#sec-ignoto', 'Ignoto',
                   'sds-secref reference internal')
        self.assertEqual(self.captions(html), ['Ignoto'])

    def test_on_page_toc_entry_is_left_alone(self):
        # The "On this page" index links slugs, which never carry sds-secref.
        html = ('<a class="reference internal nav-link" href="#le-liste">'
                '1.1.3. Le liste</a>')
        self.assertEqual(self.captions(html), ['1.1.3. Le liste'])


class TestSubsectionCaption(unittest.TestCase):

    LOCALES = [('it', 'Paragrafo 4.4.3'), ('en', 'Section 4.4.3'),
               ('fr', 'Paragraphe 4.4.3'), ('es', 'Párrafo 4.4.3')]

    def test_localization_all_languages(self):
        for lang, expected in self.LOCALES:
            with self.subTest(lang=lang):
                self.assertEqual(
                    TOC(language=lang).subsection_caption('4.4.3'), expected)


if __name__ == '__main__':
    unittest.main()
