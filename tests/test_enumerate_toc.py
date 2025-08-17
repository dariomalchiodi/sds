import unittest
from collections import OrderedDict
from sds.sds import enumerate_toc


class TestEnumerateToc(unittest.TestCase):
    """Test suite for the enumerate_toc function."""
    
    def setUp(self):
        """Set up test fixtures with various TOC structures."""
        
        # Simple TOC with just chapters (no sections)
        self.simple_toc = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {
                    'caption': 'Main Content',
                    'chapters': [
                        {'file': 'chapter1', 'title': 'Introduction'},
                        {'file': 'chapter2', 'title': 'Methods'},
                        {'file': 'chapter3', 'title': 'Results'}
                    ]
                }
            ]
        }
        
        # TOC with chapters and sections
        self.toc_with_sections = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {
                    'caption': 'Part One',
                    'chapters': [
                        {
                            'file': 'chapter1',
                            'title': 'Introduction',
                            'sections': [
                                {'file': 'section1-1', 'title': 'Background'},
                                {'file': 'section1-2', 'title': 'Objectives'}
                            ]
                        },
                        {
                            'file': 'chapter2',
                            'title': 'Methods',
                            'sections': [
                                {'file': 'section2-1', 'title': 'Data Collection'},
                                {'file': 'section2-2', 'title': 'Data Analysis'},
                                {'file': 'section2-3', 'title': 'Validation'}
                            ]
                        }
                    ]
                }
            ]
        }
        
        # TOC with appendices (Italian)
        self.toc_with_appendices_it = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {
                    'caption': 'Contenuto Principale',
                    'chapters': [
                        {'file': 'chapter1', 'title': 'Introduzione'},
                        {
                            'file': 'chapter2',
                            'title': 'Metodi',
                            'sections': [
                                {'file': 'section2-1', 'title': 'Raccolta Dati'}
                            ]
                        }
                    ]
                },
                {
                    'caption': 'Appendici',
                    'chapters': [
                        {'file': 'references', 'title': 'Bibliografia'},
                        {
                            'file': 'appendix-b',
                            'title': 'Dati Supplementari',
                            'sections': [
                                {'file': 'app-b-1', 'title': 'Tabelle'},
                                {'file': 'app-b-2', 'title': 'Grafici'}
                            ]
                        }
                    ]
                }
            ]
        }
        
        # TOC with appendices (English)
        self.toc_with_appendices_en = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {
                    'caption': 'Main Content',
                    'chapters': [
                        {'file': 'chapter1', 'title': 'Introduction'},
                        {'file': 'chapter2', 'title': 'Analysis'}
                    ]
                },
                {
                    'caption': 'Appendices',
                    'chapters': [
                        {'file': 'references', 'title': 'References'},
                        {'file': 'appendix-data', 'title': 'Additional Data'}
                    ]
                }
            ]
        }
        
        # TOC with appendices (French)
        self.toc_with_appendices_fr = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {
                    'caption': 'Contenu Principal',
                    'chapters': [
                        {'file': 'chapter1', 'title': 'Introduction'}
                    ]
                },
                {
                    'caption': 'Annexes',
                    'chapters': [
                        {'file': 'references', 'title': 'Références'}
                    ]
                }
            ]
        }
        
        # TOC with appendices (Spanish)
        self.toc_with_appendices_es = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {
                    'caption': 'Contenido Principal',
                    'chapters': [
                        {'file': 'chapter1', 'title': 'Introducción'}
                    ]
                },
                {
                    'caption': 'Apéndices',
                    'chapters': [
                        {'file': 'references', 'title': 'Referencias'}
                    ]
                }
            ]
        }
        
        # TOC with presentation files (should be skipped)
        self.toc_with_presentation = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {
                    'caption': 'Presentazione',
                    'chapters': [
                        {'file': 'presentazione', 'title': 'Presentazione del Libro'},
                        {'file': 'introduction', 'title': 'Introduction to the Topic'}
                    ]
                },
                {
                    'caption': 'Main Content',
                    'chapters': [
                        {'file': 'chapter1', 'title': 'First Chapter'},
                        {'file': 'chapter2', 'title': 'Second Chapter'}
                    ]
                }
            ]
        }
        
        # Complex TOC with multiple parts, chapters, sections, and subsections
        self.complex_toc = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {
                    'caption': 'Introduction',
                    'chapters': [
                        {
                            'file': 'chapter1',
                            'title': 'Getting Started',
                            'sections': [
                                {'file': 'section1-1', 'title': 'Prerequisites'},
                                {
                                    'file': 'section1-2',
                                    'title': 'Installation',
                                    'sections': [
                                        {'file': 'subsection1-2-1', 'title': 'Windows'},
                                        {'file': 'subsection1-2-2', 'title': 'MacOS'},
                                        {'file': 'subsection1-2-3', 'title': 'Linux'}
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    'caption': 'Advanced Topics',
                    'chapters': [
                        {
                            'file': 'chapter2',
                            'title': 'Advanced Features',
                            'sections': [
                                {'file': 'section2-1', 'title': 'Configuration'},
                                {'file': 'section2-2', 'title': 'Optimization'}
                            ]
                        }
                    ]
                },
                {
                    'caption': 'Appendices',
                    'chapters': [
                        {'file': 'references', 'title': 'References'},
                        {
                            'file': 'appendix-troubleshooting',
                            'title': 'Troubleshooting',
                            'sections': [
                                {'file': 'app-trouble-1', 'title': 'Common Issues'},
                                {'file': 'app-trouble-2', 'title': 'FAQ'}
                            ]
                        }
                    ]
                }
            ]
        }
    
    def test_simple_toc_chapters_only(self):
        """Test TOC with only chapters, no sections."""
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('en', self.simple_toc)
        expected = OrderedDict([
            ('Introduction', '1'),
            ('Methods', '2'),
            ('Results', '3')
        ])
        self.assertEqual(toc, expected)
    
    def test_toc_with_sections(self):
        """Test TOC with chapters and sections."""
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('en', self.toc_with_sections)
        expected = OrderedDict([
            ('Introduction', '1'),
            ('Background', '1.1'),
            ('Objectives', '1.2'),
            ('Methods', '2'),
            ('Data Collection', '2.1'),
            ('Data Analysis', '2.2'),
            ('Validation', '2.3')
        ])
        self.assertEqual(toc, expected)
    
    def test_appendices_italian(self):
        """Test Italian TOC with appendices."""
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('it', self.toc_with_appendices_it)
        expected = OrderedDict([
            ('Introduzione', '1'),
            ('Metodi', '2'),
            ('Raccolta Dati', '2.1'),
            ('Bibliografia', 'A'),
            ('Dati Supplementari', 'B'),
            ('Tabelle', 'B.1'),
            ('Grafici', 'B.2')
        ])
        self.assertEqual(toc, expected)
    
    def test_appendices_english(self):
        """Test English TOC with appendices."""
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('en', self.toc_with_appendices_en)
        expected = OrderedDict([
            ('Introduction', '1'),
            ('Analysis', '2'),
            ('References', 'A'),
            ('Additional Data', 'B')
        ])
        self.assertEqual(toc, expected)
    
    def test_appendices_french(self):
        """Test French TOC with appendices."""
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('fr', self.toc_with_appendices_fr)
        expected = OrderedDict([
            ('Introduction', '1'),
            ('Références', 'A')
        ])
        self.assertEqual(toc, expected)
    
    def test_appendices_spanish(self):
        """Test Spanish TOC with appendices."""
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('es', self.toc_with_appendices_es)
        expected = OrderedDict([
            ('Introducción', '1'),
            ('Referencias', 'A')
        ])
        self.assertEqual(toc, expected)
    
    def test_skip_presentation_files(self):
        """Test that presentation/introduction files are skipped."""
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('it', self.toc_with_presentation)
        expected = OrderedDict([
            ('First Chapter', '1'),
            ('Second Chapter', '2')
        ])
        self.assertEqual(toc, expected)
    
    def test_complex_toc_with_subsections(self):
        """Test complex TOC with multiple levels and appendices."""
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('en', self.complex_toc)
        expected = OrderedDict([
            ('Getting Started', '1'),
            ('Prerequisites', '1.1'),
            ('Installation', '1.2'),
            ('Windows', '1.2.1'),
            ('MacOS', '1.2.2'),
            ('Linux', '1.2.3'),
            ('Advanced Features', '2'),
            ('Configuration', '2.1'),
            ('Optimization', '2.2'),
            ('References', 'A'),
            ('Troubleshooting', 'B'),
            ('Common Issues', 'B.1'),
            ('FAQ', 'B.2')
        ])
        self.assertEqual(toc, expected)
    
    def test_empty_toc(self):
        """Test behavior with empty TOC."""
        empty_toc = {'format': 'jb-book', 'root': 'index', 'parts': []}
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('en', empty_toc)
        self.assertEqual(toc, OrderedDict())
    
    def test_toc_without_parts(self):
        """Test behavior with TOC that has no parts key."""
        no_parts_toc = {'format': 'jb-book', 'root': 'index'}
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('en', no_parts_toc)
        self.assertEqual(toc, OrderedDict())
    
    def test_part_without_chapters(self):
        """Test part that has no chapters."""
        toc_no_chapters = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {'caption': 'Empty Part'},
                {
                    'caption': 'Content',
                    'chapters': [
                        {'file': 'chapter1', 'title': 'Chapter One'}
                    ]
                }
            ]
        }
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('en', toc_no_chapters)
        expected = OrderedDict([
            ('Chapter One', '1')
        ])
        self.assertEqual(toc, expected)
    
    def test_chapter_without_title_or_file(self):
        """Test chapter entries without title or file: should raise if title but no file, skip if neither."""
        toc_incomplete = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {
                    'caption': 'Content',
                    'chapters': [
                        {'file': 'chapter1'},  # No title
                        {'title': 'Chapter Two'},  # No file, but has title
                        {'file': 'chapter3', 'title': 'Chapter Three'}
                    ]
                }
            ]
        }
        with self._mock_label_extraction():
            with self.assertRaises(ValueError) as cm:
                enumerate_toc('en', toc_incomplete)
            self.assertIn("Chapter 'Chapter Two' has a title but no file", str(cm.exception))
    
    def test_multiple_appendix_parts(self):
        """Test TOC with multiple appendix parts."""
        toc_multiple_appendices = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {
                    'caption': 'Main Content',
                    'chapters': [
                        {'file': 'chapter1', 'title': 'Introduction'}
                    ]
                },
                {
                    'caption': 'Appendici',
                    'chapters': [
                        {'file': 'references', 'title': 'References'}
                    ]
                },
                {
                    'caption': 'Additional Appendices',
                    'chapters': [
                        {'file': 'data', 'title': 'Data Tables'}
                    ]
                }
            ]
        }
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('it', toc_multiple_appendices)
        # Second part should continue appendix numbering
        expected = OrderedDict([
            ('Introduction', '1'),
            ('References', 'A'),
            ('Data Tables', 'B')
        ])
        self.assertEqual(toc, expected)
    
    def test_case_insensitive_appendix_detection(self):
        """Test that appendix detection is case insensitive."""
        toc_mixed_case = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {
                    'caption': 'Main Content',
                    'chapters': [
                        {'file': 'chapter1', 'title': 'Introduction'}
                    ]
                },
                {
                    'caption': 'APPENDICI',  # Uppercase
                    'chapters': [
                        {'file': 'references', 'title': 'References'}
                    ]
                }
            ]
        }
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('it', toc_mixed_case)
        expected = OrderedDict([
            ('Introduction', '1'),
            ('References', 'A')
        ])
        self.assertEqual(toc, expected)
    
    def test_return_type_is_ordered_dict(self):
        """Test that the function returns an OrderedDict."""
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('en', self.simple_toc)
        self.assertIsInstance(toc, OrderedDict)
    
    def test_numbering_consistency_across_parts(self):
        """Test that chapter numbering continues across non-appendix parts."""
        toc_multiple_parts = {
            'format': 'jb-book',
            'root': 'index',
            'parts': [
                {
                    'caption': 'Part One',
                    'chapters': [
                        {'file': 'chapter1', 'title': 'Chapter One'}
                    ]
                },
                {
                    'caption': 'Part Two',
                    'chapters': [
                        {'file': 'chapter2', 'title': 'Chapter Two'},
                        {'file': 'chapter3', 'title': 'Chapter Three'}
                    ]
                }
            ]
        }
        with self._mock_label_extraction():
            toc, _ = enumerate_toc('en', toc_multiple_parts)
        expected = OrderedDict([
            ('Chapter One', '1'),
            ('Chapter Two', '2'),
            ('Chapter Three', '3')
        ])
        self.assertEqual(toc, expected)

    from contextlib import contextmanager
    import sys
    @contextmanager
    def _mock_label_extraction(self):
        """Mock extract_title_and_label_from_file to always return (title, unique_label) for tests."""
        import sds.sds as sds_mod
        orig_func = sds_mod.enumerate_toc.__globals__['extract_title_and_label_from_file'] if 'extract_title_and_label_from_file' in sds_mod.enumerate_toc.__globals__ else None
        def fake_extract_title_and_label_from_file(file_path):
            # Use file_path to generate a unique label
            import os
            base = os.path.basename(file_path)
            label = os.path.splitext(base)[0].replace('-', '_').replace('.', '_')
            return None, label
        sds_mod.enumerate_toc.__globals__['extract_title_and_label_from_file'] = fake_extract_title_and_label_from_file
        try:
            yield
        finally:
            if orig_func:
                sds_mod.enumerate_toc.__globals__['extract_title_and_label_from_file'] = orig_func
            else:
                del sds_mod.enumerate_toc.__globals__['extract_title_and_label_from_file']


if __name__ == '__main__':
    unittest.main()
