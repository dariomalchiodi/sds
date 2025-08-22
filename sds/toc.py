import re

LABELS = {'it': {'chapter': 'Capitolo',
                 'section': 'Paragrafo',
                 'appendix': 'Appendice'},
          'en': {'chapter': 'Chapter',
                 'section': 'Section',
                 'appendix': 'Appendix'},
          'fr': {'chapter': 'Chapitre',
                 'section': 'Paragraphe',
                 'appendix': 'Annexe'},
          'es': {'chapter': 'Capítulo',
                 'section': 'Párrafo',
                 'appendix': 'Apéndice'}}

class TOC:
    """
    Table of Contents (TOC) manager for documents with chapters, sections,
    and appendices.

    Supports localization, cross-referencing, and validation of entries.
    Each entry is a dictionary with keys: 'title', 'label', 'file',
    'caption', and 'number'.
    """
    def __init__(self, language='en'):
        """
        Initialize a TOC object for a given language.

        Args:
            language (str): Language code for localization (e.g., 'en', 'it',
                'fr', 'es').
        Raises:
            ValueError: If the language is not supported.
        """
        if language not in LABELS:
            raise ValueError(f"Unsupported language: {language}")
        self.language = language
        self.toc = []
        self.label_to_caption = {}
        self.file_to_number = {}
        self.current_chapter_num = 0
        self.current_section_num = 0
        self.is_appendix_part = False

    def _validate_entry(self, file, label, title):
        """
        Validate a TOC entry for uniqueness and non-empty fields.

        Args:
            file (str): Path to the markdown file.
            label (str): Unique label for cross-referencing.
            title (str): Title of the entry.
        Raises:
            ValueError: If any field is empty or not a string, or if label or
                file is duplicated.
        """
        if not label or not isinstance(label, str):
            raise ValueError("Label must be a non-empty string.")
        if not file or not isinstance(file, str):
            raise ValueError("File must be a non-empty string.")
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        if label in self.label_to_caption:
            raise ValueError(f"Duplicate label: {label}")
        if file in self.file_to_number:
            raise ValueError(f"Duplicate file: {file}")

    def add_chapter(self, file, label, title):
        """
        Add a chapter or appendix entry to the TOC.

        Args:
            file (str): Path to the markdown file.
            label (str): Unique label for the chapter/appendix.
            title (str): Title of the chapter/appendix.
        Raises:
            ValueError: If validation fails.
        """
        self._validate_entry(file, label, title)
        label = re.sub(r'[:_]', '-', label)
        self.current_chapter_num += 1
        self.current_section_num = 0
        key = 'appendix' if self.is_appendix_part else 'chapter'
        caption = LABELS[self.language][key]
        if self.is_appendix_part:
            appendix_counter = ord('A') + self.current_chapter_num - 1
            number = chr(appendix_counter)
        else:
            number = f'{self.current_chapter_num}'
        entry = {'title': title, 'label': label,
                   'file': file, 'caption': caption,
                   'number': number}
        self.toc.append(entry)
        self.label_to_caption[label] = f'{caption} {number}'
        self.file_to_number[file] = number

    def start_appendix(self):
        """
        Switch TOC to appendix mode and reset chapter numbering.
        """
        self.is_appendix_part = True
        self.current_chapter_num = 0
    
    def add_section(self, file, label, title):
        """
        Add a section entry to the TOC, under the current chapter or appendix.

        Args:
            file (str): Path to the markdown file.
            label (str): Unique label for the section.
            title (str): Title of the section.
        Raises:
            ValueError: If no chapter or appendix exists, or validation fails.
        """
        if self.current_chapter_num == 0 and not self.is_appendix_part:
            raise ValueError("Cannot add a section before a chapter.")
        self._validate_entry(file, label, title)
        label = re.sub(r'[:_]', '-', label)
        self.current_section_num += 1
        caption = LABELS[self.language]['section']
        if self.is_appendix_part:
            section_num = chr(ord('A') + self.current_chapter_num - 1) + f'.{self.current_section_num}'
        else:
            section_num = f'{self.current_chapter_num}.{self.current_section_num}'
        section = {'title': title, 'label': label,
                   'file': file, 'caption': caption,
                   'number': section_num}
        self.toc.append(section)
        self.label_to_caption[label] = f'{caption} {section_num}'
        self.file_to_number[file] = section_num
    
    def get_caption_by_label(self, label):
        """
        Get the caption and number for a given label.

        Args:
            label (str): The label to look up.
        Returns:
            str or None: Caption and number if found, else None.
        """
        return self.label_to_caption.get(label, None)
    
    def get_caption_by_file(self, file):
        """
        Get the number for a given file.

        Args:
            file (str): The file path to look up.
        Returns:
            str or None: Number if found, else None.
        """
        return self.file_to_number.get(file, None)
    
    def get_toc(self):
        """
        Get a formatted string representation of the entire TOC.

        Returns:
            str: The formatted TOC.
        """
        out = ''
        for entry in self.toc:
            out += f'{entry["caption"]} {entry["number"]}: {entry["title"]}\n'
        return out
