import pytest
from sds.toc import TOC

# --- Fixtures ---
@pytest.fixture(params=[
    ('en', 'Chapter', 'Section', 'Appendix'),
    ('it', 'Capitolo', 'Paragrafo', 'Appendice'),
    ('fr', 'Chapitre', 'Paragraphe', 'Annexe'),
    ('es', 'Capítulo', 'Párrafo', 'Apéndice'),
])
def toc_locale(request):
    lang, chapter, section, appendix = request.param
    toc = TOC(language=lang)
    return toc, chapter, section, appendix

@pytest.fixture
def toc_en():
    return TOC(language='en')

@pytest.fixture
def toc_it():
    return TOC(language='it')

# --- Tests ---

def test_localization_chapter_section_appendix(toc_locale):
    toc, chapter_label, section_label, appendix_label = toc_locale
    toc.add_chapter('c1.md', 'c1', 'Intro')
    toc.add_section('s1.md', 's1', 'Background')
    toc.start_appendix()
    toc.add_chapter('a1.md', 'a1', 'App A')
    toc.add_section('as1.md', 'as1', 'App Section')
    toc_str = toc.get_toc()
    assert f'{chapter_label} 1: Intro' in toc_str
    assert f'{section_label} 1.1: Background' in toc_str
    assert f'{appendix_label} A: App A' in toc_str
    assert f'{section_label} A.1: App Section' in toc_str
    # Check label lookups
    assert toc.get_caption_by_label('c1') == f'{chapter_label} 1'
    assert toc.get_caption_by_label('s1') == f'{section_label} 1.1'
    assert toc.get_caption_by_label('a1') == f'{appendix_label} A'
    assert toc.get_caption_by_label('as1') == f'{section_label} A.1'
    # Check file lookups
    assert toc.get_caption_by_file('c1.md') == '1'
    assert toc.get_caption_by_file('s1.md') == '1.1'
    assert toc.get_caption_by_file('a1.md') == 'A'
    assert toc.get_caption_by_file('as1.md') == 'A.1'

def test_add_chapter_and_section(toc_en):
    toc_en.add_chapter('chapter1.md', 'ch1', 'Introduction')
    toc_en.add_section('section1.md', 'sec1', 'Background')
    toc_en.add_section('section2.md', 'sec2', 'Motivation')
    toc_str = toc_en.get_toc()
    assert 'Chapter 1: Introduction' in toc_str
    assert 'Section 1.1: Background' in toc_str
    assert 'Section 1.2: Motivation' in toc_str
    assert toc_en.get_caption_by_label('ch1') == 'Chapter 1'
    assert toc_en.get_caption_by_label('sec1') == 'Section 1.1'
    assert toc_en.get_caption_by_file('chapter1.md') == '1'
    assert toc_en.get_caption_by_file('section2.md') == '1.2'

def test_add_appendix_and_section(toc_en):
    toc_en.add_chapter('chapter1.md', 'ch1', 'Intro')
    toc_en.start_appendix()
    toc_en.add_chapter('appendixA.md', 'appA', 'Appendix A')
    toc_en.add_section('appAsec1.md', 'appAsec1', 'App Section 1')
    toc_str = toc_en.get_toc()
    assert 'Appendix A: Appendix A' in toc_str
    assert 'Section A.1: App Section 1' in toc_str
    assert toc_en.get_caption_by_label('appA') == 'Appendix A'
    assert toc_en.get_caption_by_label('appAsec1') == 'Section A.1'
    assert toc_en.get_caption_by_file('appendixA.md') == 'A'
    assert toc_en.get_caption_by_file('appAsec1.md') == 'A.1'

def test_localization_italian(toc_it):
    toc_it.add_chapter('cap1.md', 'cap1', 'Introduzione')
    toc_it.add_section('par1.md', 'par1', 'Contesto')
    toc_str = toc_it.get_toc()
    assert 'Capitolo 1: Introduzione' in toc_str
    assert 'Paragrafo 1.1: Contesto' in toc_str

def test_duplicate_label_raises(toc_en):
    toc_en.add_chapter('chapter1.md', 'ch1', 'Intro')
    with pytest.raises(ValueError):
        toc_en.add_chapter('chapter2.md', 'ch1', 'Another')

def test_duplicate_file_raises(toc_en):
    toc_en.add_chapter('chapter1.md', 'ch1', 'Intro')
    with pytest.raises(ValueError):
        toc_en.add_chapter('chapter1.md', 'ch2', 'Another')

def test_empty_label_raises(toc_en):
    with pytest.raises(ValueError):
        toc_en.add_chapter('chapter1.md', '', 'Intro')

def test_empty_file_raises(toc_en):
    with pytest.raises(ValueError):
        toc_en.add_chapter('', 'ch1', 'Intro')

def test_empty_title_raises(toc_en):
    with pytest.raises(ValueError):
        toc_en.add_chapter('chapter1.md', 'ch1', '')

def test_section_before_chapter_raises(toc_en):
    with pytest.raises(ValueError):
        toc_en.add_section('section1.md', 'sec1', 'Should fail')

def test_unsupported_language():
    with pytest.raises(ValueError):
        TOC(language='de')
