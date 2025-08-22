import pytest
from sds.sds import generate_toc

def make_mock_toc():
    return {
        'parts': [
            {
                'caption': 'Presentation',
                'chapters': [
                    {
                        'file': 'P0/introduction',
                        'sections': [
                            {'file': 'P0/approach'},
                            {'file': 'P0/acknowledgments'},
                        ]
                    },
                    {'file': 'P0/overview'}
                ]
            },
            {
                'caption': "Programming for data analysis",
                'chapters': [
                    {'file': 'P1-PAD/presentation'},
                    {
                        'file': 'P1-PAD/c1-intro-python/intro-python',
                        'sections': [
                            {'file': 'P1-PAD/c1-intro-python/installing'},
                            {'file': 'P1-PAD/c1-intro-python/data-types'}
                        ]
                    },
                    {'file': 'P1-PAD/c2-pandas/pandas',}
                ]
            },
            {
                'caption': 'Appendices',
                'chapters': [
                    {'file': 'references',
                     'sections': [
                            {'file': 'app/python'},
                            {'file': 'app/pandas'}]}
                ]
            }
        ]
    }

def test_generate_toc_with_mock():
    toc_data = make_mock_toc()
    toc = generate_toc(language='en', toc_data=toc_data)
    toc_str = toc.get_toc()
    # Check chapters
    assert 'Chapter 1: Introduction' in toc_str
    assert 'Chapter 2: Overview' in toc_str
    # Check sections
    assert 'Section 1.1: Approach' in toc_str
    assert 'Section 1.2: Acknowledgments' in toc_str
    # Check appendix
    assert 'Appendix A: References' in toc_str
    assert 'Section A.1: Python' in toc_str
    # Check label lookups
    assert toc.get_caption_by_label('source-en-P0-introduction.md') == 'Chapter 1'
    assert toc.get_caption_by_label('source-en-P0-approach.md') == 'Section 1.1'
    assert toc.get_caption_by_label('source-en-references.md') == 'Appendix A'
    assert toc.get_caption_by_label('source-en-app-python.md') == 'Section A.1'
    # Check file lookups
    assert toc.get_caption_by_file('P0/introduction') == '1'
    assert toc.get_caption_by_file('P0/approach') == '1.1'
    assert toc.get_caption_by_file('references') == 'A'
    assert toc.get_caption_by_file('app/python') == 'A.1'

