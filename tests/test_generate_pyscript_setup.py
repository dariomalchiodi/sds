import unittest
from sds.sds import generate_pyscript_setup


class TestGeneratePyscriptSetup(unittest.TestCase):
    def setUp(self):
        self.result = generate_pyscript_setup()

    def test_returns_string(self):
        self.assertIsInstance(self.result, str)
        self.assertGreater(len(self.result), 0)

    def test_contains_matplotlib_setup(self):
        self.assertIn('#BEGIN# import matplotlib', self.result)
        self.assertIn('import matplotlib', self.result)
        self.assertIn('#END#', self.result)

    def test_contains_pyscript_imports(self):
        self.assertIn('from pyscript import display', self.result)
        self.assertIn('from pyodide.http import open_url', self.result)

    def test_contains_localfs_setup(self):
        self.assertIn('async def _ensure_localfs()', self.result)
        self.assertIn('await _ensure_localfs()', self.result)

    def test_contains_success_log(self):
        self.assertIn('PyScript utilities loaded successfully', self.result)

    def test_no_html_wrappers(self):
        self.assertNotIn('<py-script>', self.result)
        self.assertNotIn('</py-script>', self.result)
        self.assertNotIn('<script type="py">', self.result)
        self.assertNotIn('```{raw} html', self.result)


if __name__ == '__main__':
    unittest.main()
