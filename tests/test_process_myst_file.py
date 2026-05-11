import unittest
import tempfile
import shutil
from pathlib import Path

from sds.sds import process_myst_file


class TestProcessMystFile(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = Path(self.temp_dir) / 'test.md'

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_process_file_with_python_block(self):
        content = '''# Test Document

Some text before the code.

```python
x = 5
x * 2
```

Some text after the code.
'''
        self.test_file.write_text(content, encoding='utf-8')
        backup_path = process_myst_file(str(self.test_file))

        self.assertTrue(Path(backup_path).exists())
        self.assertEqual(Path(backup_path).read_text(encoding='utf-8'), content)

        processed = self.test_file.read_text(encoding='utf-8')
        self.assertNotEqual(processed, content)
        self.assertIn('# Test Document', processed)
        self.assertIn('```python', processed)
        self.assertIn('<script type="py">', processed)

    def test_process_file_no_python_blocks(self):
        content = '''# Simple Document

This is just text with no Python code.

Some more text.
'''
        self.test_file.write_text(content, encoding='utf-8')
        backup_path = process_myst_file(str(self.test_file))

        self.assertTrue(Path(backup_path).exists())
        self.assertEqual(self.test_file.read_text(encoding='utf-8'), content)

    def test_process_file_with_setup_disabled(self):
        content = '```python\nprint("Hello, World!")\n```'
        self.test_file.write_text(content, encoding='utf-8')
        backup_path = process_myst_file(str(self.test_file), include_setup=False)

        self.assertTrue(Path(backup_path).exists())
        processed = self.test_file.read_text(encoding='utf-8')
        self.assertNotIn('PyScript utilities loaded successfully', processed)
        self.assertNotIn('_ensure_localfs', processed)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            process_myst_file(str(Path(self.temp_dir) / 'nonexistent.md'))

    def test_backup_file_path(self):
        self.test_file.write_text('# Test', encoding='utf-8')
        backup_path = process_myst_file(str(self.test_file))
        self.assertEqual(backup_path, str(self.test_file) + '.backup')

    def test_multiple_python_blocks(self):
        content = '''# Multiple Blocks

First block:
```python
a = 1
```

Second block:
```python
b = 2
b + 1
```

The end.
'''
        self.test_file.write_text(content, encoding='utf-8')
        process_myst_file(str(self.test_file))

        processed = self.test_file.read_text(encoding='utf-8')
        # Both cells' code appear in the single combined PyScript block
        self.assertIn('a = 1', processed)
        self.assertIn('result = b + 1', processed)
        self.assertEqual(processed.count('<script type="py">'), 1)


if __name__ == '__main__':
    unittest.main()
