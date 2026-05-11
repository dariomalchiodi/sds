import unittest
from sds.toc import TOC


class TestTOCLocalization(unittest.TestCase):

    LOCALES = [
        ('en', 'Chapter',  'Section',    'Appendix'),
        ('it', 'Capitolo', 'Paragrafo',  'Appendice'),
        ('fr', 'Chapitre', 'Paragraphe', 'Annexe'),
        ('es', 'Capítulo', 'Párrafo',    'Apéndice'),
    ]

    def test_localization_all_languages(self):
        for lang, chapter, section, appendix in self.LOCALES:
            with self.subTest(lang=lang):
                toc = TOC(language=lang)
                toc.add_chapter('c1.md', 'c1', 'Intro')
                toc.add_section('s1.md', 's1', 'Background')
                toc.start_appendix()
                toc.add_chapter('a1.md', 'a1', 'App A')
                toc.add_section('as1.md', 'as1', 'App Section')

                toc_str = toc.get_toc()
                self.assertIn(f'{chapter} 1: Intro',          toc_str)
                self.assertIn(f'{section} 1.1: Background',   toc_str)
                self.assertIn(f'{appendix} A: App A',         toc_str)
                self.assertIn(f'{section} A.1: App Section',  toc_str)

                self.assertEqual(toc.get_caption_by_label('c1'),  f'{chapter} 1')
                self.assertEqual(toc.get_caption_by_label('s1'),  f'{section} 1.1')
                self.assertEqual(toc.get_caption_by_label('a1'),  f'{appendix} A')
                self.assertEqual(toc.get_caption_by_label('as1'), f'{section} A.1')

                self.assertEqual(toc.get_caption_by_file('c1.md'),  '1')
                self.assertEqual(toc.get_caption_by_file('s1.md'),  '1.1')
                self.assertEqual(toc.get_caption_by_file('a1.md'),  'A')
                self.assertEqual(toc.get_caption_by_file('as1.md'), 'A.1')


class TestTOCEnglish(unittest.TestCase):

    def setUp(self):
        self.toc = TOC(language='en')

    def test_chapter_and_sections(self):
        self.toc.add_chapter('chapter1.md', 'ch1', 'Introduction')
        self.toc.add_section('section1.md', 'sec1', 'Background')
        self.toc.add_section('section2.md', 'sec2', 'Motivation')

        toc_str = self.toc.get_toc()
        self.assertIn('Chapter 1: Introduction', toc_str)
        self.assertIn('Section 1.1: Background', toc_str)
        self.assertIn('Section 1.2: Motivation', toc_str)

        self.assertEqual(self.toc.get_caption_by_label('ch1'),  'Chapter 1')
        self.assertEqual(self.toc.get_caption_by_label('sec1'), 'Section 1.1')
        self.assertEqual(self.toc.get_caption_by_file('chapter1.md'), '1')
        self.assertEqual(self.toc.get_caption_by_file('section2.md'), '1.2')

    def test_appendix_and_section(self):
        self.toc.add_chapter('chapter1.md', 'ch1', 'Intro')
        self.toc.start_appendix()
        self.toc.add_chapter('appendixA.md', 'appA', 'Appendix A')
        self.toc.add_section('appAsec1.md', 'appAsec1', 'App Section 1')

        toc_str = self.toc.get_toc()
        self.assertIn('Appendix A: Appendix A',    toc_str)
        self.assertIn('Section A.1: App Section 1', toc_str)

        self.assertEqual(self.toc.get_caption_by_label('appA'),    'Appendix A')
        self.assertEqual(self.toc.get_caption_by_label('appAsec1'), 'Section A.1')
        self.assertEqual(self.toc.get_caption_by_file('appendixA.md'), 'A')
        self.assertEqual(self.toc.get_caption_by_file('appAsec1.md'),  'A.1')

    def test_duplicate_label_raises(self):
        self.toc.add_chapter('chapter1.md', 'ch1', 'Intro')
        with self.assertRaises(ValueError):
            self.toc.add_chapter('chapter2.md', 'ch1', 'Another')

    def test_duplicate_file_raises(self):
        self.toc.add_chapter('chapter1.md', 'ch1', 'Intro')
        with self.assertRaises(ValueError):
            self.toc.add_chapter('chapter1.md', 'ch2', 'Another')

    def test_empty_label_raises(self):
        with self.assertRaises(ValueError):
            self.toc.add_chapter('chapter1.md', '', 'Intro')

    def test_empty_file_raises(self):
        with self.assertRaises(ValueError):
            self.toc.add_chapter('', 'ch1', 'Intro')

    def test_empty_title_raises(self):
        with self.assertRaises(ValueError):
            self.toc.add_chapter('chapter1.md', 'ch1', '')

    def test_section_before_chapter_raises(self):
        with self.assertRaises(ValueError):
            self.toc.add_section('section1.md', 'sec1', 'Should fail')


class TestTOCItalian(unittest.TestCase):

    def test_localization(self):
        toc = TOC(language='it')
        toc.add_chapter('cap1.md', 'cap1', 'Introduzione')
        toc.add_section('par1.md', 'par1', 'Contesto')

        toc_str = toc.get_toc()
        self.assertIn('Capitolo 1: Introduzione', toc_str)
        self.assertIn('Paragrafo 1.1: Contesto',  toc_str)


class TestTOCUnsupportedLanguage(unittest.TestCase):

    def test_unsupported_language_raises(self):
        with self.assertRaises(ValueError):
            TOC(language='de')


if __name__ == '__main__':
    unittest.main()
