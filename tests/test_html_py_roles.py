#!/usr/bin/env python3
"""
Unit tests for the HTML {py} role processing functionality.
"""

import unittest
import tempfile
import os
from pathlib import Path

# Add the code directory to the path
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from sds.sds import process_html_py_roles, generate_inline_python


class TestProcessHtmlPyRoles(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
    <script type="module" src="https://pyscript.net/releases/2025.5.1/core.js"></script>
</head>
<body>
    <p>Test inline: `2 + 3`{py}</p>
    <p>Another: `len("hello")`{py}</p>
</body>
</html>'''
    
    def test_generate_inline_python_english(self):
        """Test generate_inline_python function with English language."""
        result = generate_inline_python("2 + 3", 1, "en")
        expected = '<span id="inline-1" class="py-inline-result">Loading...</span>'
        self.assertEqual(result, expected)
    
    def test_generate_inline_python_italian(self):
        """Test generate_inline_python function with Italian language."""
        result = generate_inline_python("x = 42", 2, "it")
        expected = '<span id="inline-2" class="py-inline-result">Caricamento...</span>'
        self.assertEqual(result, expected)
    
    def test_generate_inline_python_french(self):
        """Test generate_inline_python function with French language."""
        result = generate_inline_python("len('test')", 3, "fr")
        expected = '<span id="inline-3" class="py-inline-result">Chargement...</span>'
        self.assertEqual(result, expected)
    
    def test_generate_inline_python_spanish(self):
        """Test generate_inline_python function with Spanish language."""
        result = generate_inline_python("3 * 4", 4, "es")
        expected = '<span id="inline-4" class="py-inline-result">Cargando...</span>'
        self.assertEqual(result, expected)
    
    def test_process_html_py_roles_dry_run(self):
        """Test process_html_py_roles in dry run mode."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test HTML file
            test_file = Path(temp_dir) / "test.html"
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(self.test_html)
            
            # Process in dry run mode
            summary = process_html_py_roles(temp_dir, dry_run=True, language="en")
            
            # Check results
            self.assertEqual(summary['files_processed'], 1)
            self.assertEqual(summary['files_modified'], 1)
            self.assertEqual(summary['total_replacements'], 2)
            self.assertEqual(len(summary['errors']), 0)
            
            # File should not be modified in dry run
            with open(test_file, 'r', encoding='utf-8') as f:
                content = f.read()
            self.assertEqual(content, self.test_html)
    
    def test_process_html_py_roles_actual_processing(self):
        """Test process_html_py_roles with actual file modification."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test HTML file
            test_file = Path(temp_dir) / "test.html"
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(self.test_html)
            
            # Process the file
            summary = process_html_py_roles(temp_dir, dry_run=False, language="en")
            
            # Check results
            self.assertEqual(summary['files_processed'], 1)
            self.assertEqual(summary['files_modified'], 1)
            self.assertEqual(summary['total_replacements'], 2)
            self.assertEqual(len(summary['errors']), 0)
            
            # File should be modified
            with open(test_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Should not contain original {py} roles
            self.assertNotIn('`2 + 3`{py}', content)
            self.assertNotIn('`len("hello")`{py}', content)
            
            # Should contain inline spans
            self.assertIn('<span id="inline-', content)
            self.assertIn('class="py-inline-result"', content)
            
            # Should contain PyScript execution
            self.assertIn('<py-script>', content)
            self.assertIn('inline_expressions =', content)
            
            # Backup should be created
            backup_file = test_file.with_suffix('.html.backup')
            self.assertTrue(backup_file.exists())
            
            # Backup should contain original content
            with open(backup_file, 'r', encoding='utf-8') as f:
                backup_content = f.read()
            self.assertEqual(backup_content, self.test_html)
    
    def test_process_html_py_roles_skip_static_files(self):
        """Test that _static files are skipped."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create _static directory with HTML file
            static_dir = Path(temp_dir) / "_static"
            static_dir.mkdir()
            static_file = static_dir / "test.html"
            with open(static_file, 'w', encoding='utf-8') as f:
                f.write(self.test_html)
            
            # Process the directory
            summary = process_html_py_roles(temp_dir, dry_run=False, language="en")
            
            # Should not process _static files
            self.assertEqual(summary['files_processed'], 0)
            self.assertEqual(summary['files_modified'], 0)
            self.assertEqual(summary['total_replacements'], 0)
    
    def test_process_html_py_roles_no_py_roles(self):
        """Test processing HTML file with no {py} roles."""
        html_without_py = '''<!DOCTYPE html>
<html>
<head><title>Test</title></head>
<body><p>No Python code here.</p></body>
</html>'''
        
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "test.html"
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(html_without_py)
            
            # Process the file
            summary = process_html_py_roles(temp_dir, dry_run=False, language="en")
            
            # Should process but not modify
            self.assertEqual(summary['files_processed'], 1)
            self.assertEqual(summary['files_modified'], 0)
            self.assertEqual(summary['total_replacements'], 0)


if __name__ == '__main__':
    unittest.main()
