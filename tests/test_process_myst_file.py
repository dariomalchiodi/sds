import unittest
import tempfile
import os
from pathlib import Path
import sys

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from sds.sds import process_myst_file

class TestProcessMystFile(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = Path(self.temp_dir) / "test.md"
        
    def tearDown(self):
        """Clean up after each test method."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_process_file_with_python_block(self):
        """Test processing a file with a Python code block."""
        content = '''# Test Document

Some text before the code.

```python
x = 5
x * 2
```

Some text after the code.
'''
        
        # Write test content to file
        self.test_file.write_text(content, encoding='utf-8')
        
        # Process the file
        backup_path = process_myst_file(str(self.test_file))
        
        # Check that backup was created
        self.assertTrue(Path(backup_path).exists())
        
        # Check that backup contains original content
        backup_content = Path(backup_path).read_text(encoding='utf-8')
        self.assertEqual(backup_content, content)
        
        # Check that original file was modified
        processed_content = self.test_file.read_text(encoding='utf-8')
        self.assertNotEqual(processed_content, content)
        
        # Check that processed content contains expected elements
        self.assertIn('# Test Document', processed_content)
        self.assertIn('```python', processed_content)
        self.assertIn('<div id="out-1"', processed_content)
        self.assertIn('<py-script>', processed_content)
        
    def test_process_file_no_python_blocks(self):
        """Test processing a file with no Python blocks."""
        content = '''# Simple Document

This is just text with no Python code.

Some more text.
'''
        
        # Write test content to file
        self.test_file.write_text(content, encoding='utf-8')
        
        # Process the file
        backup_path = process_myst_file(str(self.test_file))
        
        # Check that backup was created
        self.assertTrue(Path(backup_path).exists())
        
        # Check that content is unchanged (no Python blocks to process)
        processed_content = self.test_file.read_text(encoding='utf-8')
        self.assertEqual(processed_content, content)
        
    def test_process_file_with_setup_disabled(self):
        """Test processing a file with setup disabled."""
        content = '''```python
print("Hello, World!")
```'''
        
        # Write test content to file
        self.test_file.write_text(content, encoding='utf-8')
        
        # Process the file with setup disabled
        backup_path = process_myst_file(str(self.test_file), include_setup=False)
        
        # Check that backup was created
        self.assertTrue(Path(backup_path).exists())
        
        # Check that processed content doesn't contain setup
        processed_content = self.test_file.read_text(encoding='utf-8')
        self.assertNotIn('def display(', processed_content)
        self.assertNotIn('def Element(', processed_content)
        
    def test_file_not_found(self):
        """Test error handling when file doesn't exist."""
        non_existent_file = Path(self.temp_dir) / "nonexistent.md"
        
        with self.assertRaises(FileNotFoundError):
            process_myst_file(str(non_existent_file))
    
    def test_backup_file_path(self):
        """Test that backup file path is correct."""
        content = "# Test"
        self.test_file.write_text(content, encoding='utf-8')
        
        backup_path = process_myst_file(str(self.test_file))
        
        expected_backup = str(self.test_file) + '.backup'
        self.assertEqual(backup_path, expected_backup)
        
    def test_multiple_python_blocks(self):
        """Test processing a file with multiple Python blocks."""
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
        
        # Write test content to file
        self.test_file.write_text(content, encoding='utf-8')
        
        # Process the file
        backup_path = process_myst_file(str(self.test_file))
        
        # Check that processed content contains multiple cells
        processed_content = self.test_file.read_text(encoding='utf-8')
        self.assertIn('<div id="out-1"', processed_content)
        self.assertIn('<div id="out-2"', processed_content)

if __name__ == '__main__':
    unittest.main()
