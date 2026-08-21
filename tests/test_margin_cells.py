import re
import unittest

from bs4 import BeautifulSoup

from sds.sds import (_apply_margin_cells, _enclosing_directive_start,
                     _lift_code_cells_from_margin)

CELL = """```{{code-cell}} python
:tags: [hide-input]

print({n})
```"""


def margin(*body, fence='````'):
    return fence + '{margin}\n' + '\n\n'.join(body) + '\n' + fence + '\n'


def cell_positions(text):
    """(kind, order) of every marker and code cell, in document order."""
    out = []
    for m in re.finditer(r'sds-margin-cell-(src|slot)" data-margin-cell="(\d+)"'
                         r'|^`{3,}\{code-cell\}', text, re.M):
        out.append(m.group(1) + m.group(2) if m.group(1) else 'cell')
    return out


class TestLiftCodeCellsFromMargin(unittest.TestCase):

    def test_cell_is_lifted_before_a_top_level_margin(self):
        src = 'Prima.\n\n' + margin(CELL.format(n=1)) + '\nDopo.\n'
        out = _lift_code_cells_from_margin(src)
        self.assertEqual(cell_positions(out), ['src1', 'cell', 'slot1'])
        # The cell leaves the margin body and lands outside the fence.
        self.assertLess(out.index('print(1)'), out.index('{margin}'))

    def test_cell_is_lifted_out_of_the_enclosing_box(self):
        src = ('`````{prf:example}\n:label: ex-uno\n\nTesto.\n\n'
               + margin(CELL.format(n=1))
               + '\nResto.\n`````\n')
        out = _lift_code_cells_from_margin(src)
        # Top level means outside every directive, box included.
        self.assertLess(out.index('print(1)'), out.index('{prf:example}'))
        self.assertEqual(cell_positions(out), ['src1', 'cell', 'slot1'])

    def test_text_and_graphics_keep_their_order(self):
        src = margin('Testo prima.', CELL.format(n=1), 'Testo in mezzo.',
                     CELL.format(n=2), 'Testo dopo.')
        out = _lift_code_cells_from_margin(src)
        self.assertEqual(cell_positions(out),
                         ['src1', 'cell', 'src2', 'cell', 'slot1', 'slot2'])
        def slot(n):
            return f'sds-margin-cell-slot" data-margin-cell="{n}"'

        body = out[out.index('{margin}'):]
        self.assertLess(body.index('Testo prima.'), body.index(slot(1)))
        self.assertLess(body.index(slot(1)), body.index('Testo in mezzo.'))
        self.assertLess(body.index('Testo in mezzo.'), body.index(slot(2)))
        self.assertLess(body.index(slot(2)), body.index('Testo dopo.'))

    def test_margins_of_several_boxes_are_numbered_across_the_document(self):
        src = (margin(CELL.format(n=1)) + '\nTesto.\n\n'
               + margin(CELL.format(n=2)))
        out = _lift_code_cells_from_margin(src)
        self.assertEqual(cell_positions(out),
                         ['src1', 'cell', 'slot1', 'src2', 'cell', 'slot2'])

    def test_margin_without_cells_is_untouched(self):
        src = margin('Solo testo.')
        self.assertEqual(_lift_code_cells_from_margin(src), src)

    def test_cell_fence_not_shorter_than_the_margin_is_not_nested(self):
        # ```{margin} … ```{code-cell}: the cell fence closes the margin, so the
        # cell is already at top level and must be left alone.
        src = '```{margin}\nTesto.\n```\n\n```{code-cell} python\nx = 1\n```\n'
        self.assertEqual(_lift_code_cells_from_margin(src), src)

    def test_is_idempotent(self):
        once = _lift_code_cells_from_margin(margin(CELL.format(n=1)))
        self.assertEqual(_lift_code_cells_from_margin(once), once)

    def test_cell_tags_survive(self):
        out = _lift_code_cells_from_margin(margin(CELL.format(n=1)))
        self.assertIn(':tags: [hide-input]', out)


class TestEnclosingDirectiveStart(unittest.TestCase):

    def test_outermost_directive_wins(self):
        src = ('Testo.\n\n`````{prf:example}\n\n````{margin}\nX\n````\n'
               '`````\n')
        pos = src.index('{margin}')
        self.assertEqual(_enclosing_directive_start(src, pos),
                         src.index('`````{prf:example}'))

    def test_none_at_top_level(self):
        src = 'Testo.\n\n````{margin}\nX\n````\n'
        self.assertIsNone(
            _enclosing_directive_start(src, src.index('Testo')))


class TestApplyMarginCells(unittest.TestCase):

    def page(self, slot=True, src=True):
        marker_src = ('<span class="sds-margin-cell-src" '
                      'data-margin-cell="1"></span>') if src else ''
        marker_slot = ('<span class="sds-margin-cell-slot" '
                       'data-margin-cell="1"></span>') if slot else ''
        return BeautifulSoup(
            '<html><body><section>'
            f'{marker_src}'
            '<div class="cell docutils container"><img src="plot.png"/></div>'
            '<div class="proof example">'
            '<aside class="margin sidebar"><p>Prima.</p>'
            f'{marker_slot}'
            '<p>Dopo.</p></aside>'
            '</div></section></body></html>', 'html.parser')

    def aside_layout(self, soup):
        out = []
        for child in soup.select_one('aside.margin').children:
            if getattr(child, 'name', None) is None:
                continue
            if child.name == 'div' and 'cell' in (child.get('class') or []):
                out.append('cell')
            else:
                out.append(child.get_text().strip())
        return out

    def test_cell_lands_in_the_slot_between_the_paragraphs(self):
        soup = self.page()
        self.assertTrue(_apply_margin_cells(soup, False))
        self.assertEqual(self.aside_layout(soup), ['Prima.', 'cell', 'Dopo.'])
        self.assertEqual(len(soup.select('aside.margin img')), 1)

    def test_markers_are_removed(self):
        soup = self.page()
        _apply_margin_cells(soup, False)
        self.assertEqual(soup.select('[data-margin-cell]'), [])

    def test_second_run_is_a_no_op(self):
        soup = self.page()
        _apply_margin_cells(soup, False)
        self.assertFalse(_apply_margin_cells(soup, False))

    def test_slot_without_its_cell_is_left_alone(self):
        soup = self.page(src=False)
        self.assertFalse(_apply_margin_cells(soup, False))
        self.assertEqual(len(soup.select('span.sds-margin-cell-slot')), 1)


if __name__ == '__main__':
    unittest.main()
