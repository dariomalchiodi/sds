import unittest
import tempfile
from pathlib import Path

from sds.sds import process_html_py_roles, generate_inline_python


class TestGenerateInlinePython(unittest.TestCase):

    def test_english(self):
        result = generate_inline_python('2 + 3', 1, 'en')
        self.assertEqual(result,
            '<span id="inline-1" class="py-inline-splash">Loading...</span>')

    def test_italian(self):
        result = generate_inline_python('x = 42', 2, 'it')
        self.assertEqual(result,
            '<span id="inline-2" class="py-inline-splash">Caricamento...</span>')

    def test_french(self):
        result = generate_inline_python("len('test')", 3, 'fr')
        self.assertEqual(result,
            '<span id="inline-3" class="py-inline-splash">Chargement...</span>')

    def test_spanish(self):
        result = generate_inline_python('3 * 4', 4, 'es')
        self.assertEqual(result,
            '<span id="inline-4" class="py-inline-splash">Cargando...</span>')


SAMPLE_HTML = '''<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
    <script type="module" src="https://pyscript.net/releases/2025.5.1/core.js"></script>
</head>
<body>
    <p>Test inline: {py}`2 + 3`</p>
    <p>Another: {py}`len("hello")`</p>
</body>
</html>'''


class TestProcessHtmlPyRoles(unittest.TestCase):

    def _write_html(self, directory, filename='test.html'):
        path = Path(directory) / filename
        path.write_text(SAMPLE_HTML, encoding='utf-8')
        return path

    def test_dry_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._write_html(tmp)
            summary = process_html_py_roles(tmp, dry_run=True, language='en')

            self.assertEqual(summary['files_processed'], 1)
            self.assertEqual(summary['files_modified'], 1)
            self.assertEqual(summary['total_replacements'], 2)
            self.assertEqual(len(summary['errors']), 0)

            # File must not be touched in dry-run mode
            content = (Path(tmp) / 'test.html').read_text(encoding='utf-8')
            self.assertEqual(content, SAMPLE_HTML)

    def test_actual_processing(self):
        with tempfile.TemporaryDirectory() as tmp:
            test_file = self._write_html(tmp)
            summary = process_html_py_roles(tmp, dry_run=False, language='en')

            self.assertEqual(summary['files_processed'], 1)
            self.assertEqual(summary['files_modified'], 1)
            self.assertEqual(summary['total_replacements'], 2)
            self.assertEqual(len(summary['errors']), 0)

            content = test_file.read_text(encoding='utf-8')

            # Original roles replaced with span placeholders
            self.assertNotIn('{py}`2 + 3`', content)
            self.assertNotIn('{py}`len("hello")`', content)
            self.assertIn('<span id="inline-', content)
            self.assertIn('class="py-inline-splash"', content)

            # PyScript execution block injected before </body>
            self.assertIn('<script type="py">', content)
            self.assertIn('inline_expressions =', content)

            # Backup created with original content
            backup = test_file.with_suffix('.html.backup')
            self.assertTrue(backup.exists())
            self.assertEqual(backup.read_text(encoding='utf-8'), SAMPLE_HTML)

    def test_skip_static_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            static_dir = Path(tmp) / '_static'
            static_dir.mkdir()
            (static_dir / 'test.html').write_text(SAMPLE_HTML, encoding='utf-8')

            summary = process_html_py_roles(tmp, dry_run=False, language='en')

            self.assertEqual(summary['files_processed'], 0)
            self.assertEqual(summary['files_modified'], 0)
            self.assertEqual(summary['total_replacements'], 0)

    def test_no_py_roles(self):
        html = '<!DOCTYPE html><html><body><p>No Python here.</p></body></html>'
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / 'test.html').write_text(html, encoding='utf-8')
            summary = process_html_py_roles(tmp, dry_run=False, language='en')

            self.assertEqual(summary['files_processed'], 1)
            self.assertEqual(summary['files_modified'], 0)
            self.assertEqual(summary['total_replacements'], 0)


if __name__ == '__main__':
    unittest.main()
