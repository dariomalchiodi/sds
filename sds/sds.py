import argparse
import glob
import importlib
import json
import os
from pathlib import Path
import re
import shutil
import yaml

import ast
import astor
from bs4 import BeautifulSoup
from bs4 import NavigableString
from tqdm import tqdm

from sds.toc import TOC

LABELS = {'Theorem': {'it': 'Teorema', 'en': 'Theorem',
                      'fr': 'Théorème', 'es': 'Teorema'},
          'Corollary': {'it': 'Corollario', 'en': 'Corollary',  
                        'fr': 'Corollaire', 'es': 'Corolario'},
          'Lemma': {'it': 'Lemma', 'en': 'Lemma',
                    'fr': 'Lemme', 'es': 'Lema'},
          'Proof': {'it': 'Dimostrazione', 'en': 'Proof',
                    'fr': 'Démonstration', 'es': 'Demostración'},
          'Definition': {'it': 'Definizione', 'en': 'Definition',
                        'fr': 'Définition', 'es': 'Definición'},
          'Example': {'it': 'Esempio', 'en': 'Example',
                      'fr': 'Exemple', 'es': 'Ejemplo'},
          'Exercise': {'it': 'Esercizio', 'en': 'Exercise',
                       'fr': 'Exercice', 'es': 'Ejercicio'}}

SNIPPETS = 'source/snippets/'

def get_root_doc(language):
    # Build the module path as a string
    module_path = f"source.{language}.conf"
    conf = importlib.import_module(module_path)
    return getattr(conf, "root_doc", None)

def extract_python_roles(source):
    '''Extracts Python code blocks and inline roles from MyST Markdown source.
    
    Args:
        source (str): The MyST Markdown source as a string.
    Returns:
        list: A list of tuples (code_content, class_attr, is_inline) where:
              - code_content is the Python code
              - class_attr is the CSS class from :class: directive or None
              - is_inline is True for inline roles ({py}, {eval-python}), False
                for code blocks
    '''
    
    # Comprehensive pattern to match different Python code block formats
    # Matches: ```python...``` or ```{python}...``` or ```{interactive-code}
    # python...``` or {eval-python}`...` or {py}`...` For interactive-code format,
    # capture the full block including options
    pattern = r"(?:```\{interactive-code\}\s+python\s*([\s\S]*?)```)|" \
              r"(?:```(?:\{?python\}?)\s*([\s\S]*?)```)|" \
              r"(?:\{eval-python\}`([^`]+)`)|(?:\{py\}`([^`]+)`)"
    matches = re.finditer(pattern, source)
    
    result = []
    for match in matches:
        # Group 1 is interactive-code content, group 2 is python content, group 3 is
        # inline eval-python role, group 4 is inline py role
        if match.group(1) is not None:
            # This is a {interactive-code} python block
            content = match.group(1)
            # Check for :class: directive in the content
            class_attr = None
            if content and ':class:' in content:
                # Extract class and remove it from content
                class_match = re.search(r':class:\s*([^\n]+)', content)
                if class_match:
                    class_attr = class_match.group(1).strip()
                    # Remove the :class: line from the content
                    content = re.sub(r':class:\s*[^\n]+\n?', '', content)
            result.append((content.strip(), class_attr, False))
        elif match.group(2) is not None:
            # This is a regular python block
            content = match.group(2)
            result.append((content.strip(), None, False))
        elif match.group(3) is not None:
            # This is an inline eval-python role
            content = match.group(3)
            result.append((content.strip(), None, True))
        else:
            # This is an inline py role
            content = match.group(4)
            result.append((content.strip(), None, True))
    
    return result

def split_code(source):
    '''Splits Python source code into setup code and final statement.
    
    Args:
        source (str): The Python source code as a string.
    Returns:
        tuple: A pair (setup, final) where:
               - setup: string containing all code except the last statement
                 (or all code if final doesn't produce output)
               - final: string containing only the last statement if it
                 produces output, empty string otherwise
               If the source is empty, returns ('', '')
    '''
    
    try:
        # Parse the source code into an AST
        tree = ast.parse(source)
        
        # If there's no code, return empty
        if len(tree.body) == 0:
            return ('', '')
        
        # If only one statement, check if it produces output
        if len(tree.body) == 1:
            final_node = tree.body[0]
            if _produces_output(final_node):
                final_module = ast.Module(body=[final_node], type_ignores=[])
                final_code = astor.to_source(final_module).strip()
                return ('', final_code)
            else:
                # All code goes to setup if final doesn't produce output
                setup_module = ast.Module(body=tree.body, type_ignores=[])
                setup_code = astor.to_source(setup_module).strip()
                return (setup_code, '')
        
        # Multiple statements: check if final produces output
        setup_nodes = tree.body[:-1]
        final_node = tree.body[-1]
        
        if _produces_output(final_node):
            # Split normally
            setup_module = ast.Module(body=setup_nodes, type_ignores=[])
            final_module = ast.Module(body=[final_node], type_ignores=[])
            
            setup_code = astor.to_source(setup_module).strip()
            final_code = astor.to_source(final_module).strip()
            
            return (setup_code, final_code)
        else:
            # All code goes to setup if final doesn't produce output
            setup_module = ast.Module(body=tree.body, type_ignores=[])
            setup_code = astor.to_source(setup_module).strip()
            return (setup_code, '')
        
    except (SyntaxError, ValueError) as e:
        # If the code can't be parsed, return it as is in the setup part
        return (source.strip(), '')

def _produces_output(node):
    '''Check if an AST node would produce output in a Jupyter notebook.
    
    Args:
        node: An AST node
    Returns:
        bool: True if the node would produce output, False otherwise
    '''
    
    # Expressions that are not assignments produce output
    if isinstance(node, ast.Expr):
        return True
    
    # These statement types don't produce output
    if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign,
                        ast.Import, ast.ImportFrom, ast.FunctionDef,
                        ast.ClassDef, ast.For, ast.While, ast.If,
                        ast.With, ast.Try, ast.Pass, ast.Break,
                        ast.Continue, ast.Global, ast.Nonlocal,
                        ast.Delete, ast.Assert, ast.Raise, ast.Return)):
        return False
    
    # Default to False for safety
    return False

# def generate_myst_interactive(setup_code, final_code, cell_number):
#     '''Generates MyST Markdown code for interactive Python execution.
    
#     Args:
#         setup_code (str): The setup code (from split_code output)
#         final_code (str): The final expression code (from split_code output)
#         cell_number (int): Progressive number for the cell
#     Returns:
#         str: MyST Markdown code with Python role and HTML divs with PyScript
#     '''

#     # Combine all code for the Python role
#     if setup_code and final_code:
#         all_code = f"{setup_code}\n{final_code}"
#     elif setup_code:
#         all_code = setup_code
#     elif final_code:
#         all_code = final_code
#     else:
#         all_code = ""
    
#     # Create the Python code block
#     python_block = f"```python\n{all_code}\n```"
    
#     # Create the HTML raw block with divs and PyScript

#     html = f'<div id="splash-{cell_number}" class="splash"></div>\n'
#     html += f'<div id="out-{cell_number}" class="cell-out"></div>\n'
#     html += f'<div id="stdout-{cell_number}" class="cell-stdout"></div>\n'
#     html += f'<div id="stderr-{cell_number}" class="cell-stderr"></div>\n\n'
#     html += f'<py-script>\n{setup_code}\n'
    
#     # Add display call if there's a final expression
#     if final_code:
#         html += f'display({final_code}, target="out-{cell_number}")\n'
    
#     html += '</py-script>'
    
#     html_block = f'```{{raw}} html\n{html}\n```'
    
#     # Combine both blocks

#     return f"{python_block}\n\n{html_block}"

def generate_inline_python(python_code, cell_number, language='en'):
    '''Generates inline PyScript execution with span element for Python
    expressions.

    Args:
        python_code (str): The Python expression to evaluate
        cell_number (int): Progressive number for the cell
        language (str): The language code for localization (default: 'en')
    Returns:
        str: Direct HTML content for inline execution (not wrapped in raw block)
    '''

    # Get localized labels
    labels = get_toggle_labels(language)
    
    # Create direct HTML content without raw block wrapper
    # The span will show loading text initially, then get updated by PyScript
    return f'<span id="inline-{cell_number}" ' \
           f'class="py-inline-splash">{labels["wait"]}</span>'

def generate_pyscript_setup():
    '''Generates the initial PyScript setup with common imports and utilities.
    
    Returns:
        str: HTML block with PyScript setup that should be included once per
        document
    '''

    with open(SNIPPETS + 'pyscript-setup.pysnippet',
              'r', encoding='utf-8') as f:
        snippet = f.read()
    return snippet

def get_toggle_labels(language='en'):
    '''Get localized labels for toggle buttons and loading indicators.
    
    Args:
        language (str): The language code (default: 'en')
    Returns:
        dict: Dictionary with 'show', 'hide', and 'wait' keys for the labels
    '''

    labels = {
        'en': {
            'show': 'Show code',
            'hide': 'Hide code',
            'wait': 'Loading...'
        },
        'it': {
            'show': 'Mostra codice',
            'hide': 'Nascondi codice',
            'wait': 'Caricamento...'
        },
        'fr': {
            'show': 'Afficher le code',
            'hide': 'Masquer le code',
            'wait': 'Chargement...'
        },
        'es': {
            'show': 'Mostrar código',
            'hide': 'Ocultar código',
            'wait': 'Cargando...'
        }
    }
    
    return labels.get(language, labels['en'])

def _get_div_classes(base_class, class_attr):
    '''Generate CSS classes for output divs based on original code block
    classes.'''

    classes = [base_class]
    if class_attr and 'full-width' in class_attr:
        classes.append('full-width')
    return ' '.join(classes)

def process_myst_document(myst_content, source_file,
                          include_setup=True, language='en'):

    '''Processes a MyST Markdown document and adds interactive HTML blocks
    after each Python code block.
    
    Args:
        myst_content (str): The MyST Markdown document content as a string
        include_setup (bool): Whether to include the initial PyScript setup
            (default: True)
        language (str): The language code for localization (default: 'en')
    Returns:
        str: The processed document with interactive HTML blocks added after
            Python code blocks
    '''
    
    # Extract all Python code blocks from the document
    python_codes = extract_python_roles(myst_content)
    
    if not python_codes:
        return myst_content
    
    # Split the document by Python code blocks to reconstruct it
    result_parts = []
    pyscript_blocks = []  # Collect all PyScript blocks to add at the end
    inline_expressions = []  # Collect inline Python expressions
    all_imports = set()  # Collect all imported packages
    current_pos = 0
    cell_number = 1
    
    # Pattern to find Python code blocks and their positions Matches:
    # ```python...``` or ```{python}...``` or ```{interactive-code} python...``` or
    # {eval-python}`...` or {py}`...` For interactive-code format, capture the full
    # block including options
    pattern = r"(?:```\{interactive-code\}\s+python\s*([\s\S]*?)```)|" \
              r"(?:```(?:\{?python\}?)\s*([\s\S]*?)```)|" \
              r"(?:\{eval-python\}`([^`]+)`)|(?:\{py\}`([^`]+)`)"
    
    python_code_index = 0
    for match in re.finditer(pattern, myst_content):
        # Check if this code block is already inside a toggle wrapper
        context_before = myst_content[max(0, match.start() - 500):match.start()]
        context_after = myst_content[match.end():min(len(myst_content),
                                                     match.end() + 500)]
        
        # Skip if this code block is already inside a toggle wrapper
        if ('toggle-code-wrapper' in context_before and 
            'toggle-code-content' in context_before and 
            '</div>' in context_after):
            # This code block is already wrapped, skip it
            # Update current_pos to after this match
            current_pos = match.end()
            cell_number += 1
            python_code_index += 1
            continue
        
        # Add content before this Python block
        result_parts.append(myst_content[current_pos:match.start()])
        
        # Get the Python code content, class, and whether it's inline from our
        # extracted data
        is_inline = False
        height_attr = None
        if python_code_index < len(python_codes):
            python_code, class_attr, is_inline = python_codes[python_code_index]
            if python_code and ':height:' in python_code:
                    height_match = re.search(r':height:\s*([^\n]+)', python_code)
                    if height_match:
                        height_attr = height_match.group(1).strip()
                        python_code = re.sub(r':height:\s*[^\n]+\n?', '',
                                             python_code)
        else:
            # Fallback to regex extraction if index is out of bounds
            if match.group(1) is not None:
                # This is a {interactive-code} python block
                python_code = match.group(1)
                class_attr = None
                is_inline = False
                # Handle :class: directive extraction
                if python_code and ':class:' in python_code:
                    class_match = re.search(r':class:\s*([^\n]+)', python_code)
                    if class_match:
                        class_attr = class_match.group(1).strip()
                        python_code = re.sub(r':class:\s*[^\n]+\n?', '',
                                             python_code)
                if python_code and ':height:' in python_code:
                    height_match = re.search(r':height:\s*([^\n]+)', python_code)
                    if height_match:
                        height_attr = height_match.group(1).strip()
                        python_code = re.sub(r':height:\s*[^\n]+\n?', '',
                                             python_code)
            elif match.group(2) is not None:
                # This is a regular python block
                python_code = match.group(2)
                class_attr = None
                is_inline = False
            elif match.group(3) is not None:
                # This is an inline eval-python role
                python_code = match.group(3)
                class_attr = None
                is_inline = True
            else:
                # This is an inline py role
                python_code = match.group(4)
                class_attr = None
                is_inline = True
        
        # Handle inline roles differently
        if is_inline:
            # For inline roles, replace the original role with our generated
            # HTML
            inline_html = generate_inline_python(python_code.strip(),
                                                 cell_number, language)
            result_parts.append(inline_html)
            
            # Collect the inline expression to add PyScript code later
            inline_expressions.append((cell_number, python_code.strip()))
            
            current_pos = match.end()
            cell_number += 1
            python_code_index += 1
            continue
        
        # For code blocks, add the original Python block, with toggle wrapper
        # if needed
        original_block = match.group(0)
        
        if class_attr and 'toggle-code' in class_attr:
            # Remove the toggle-code class from the original block to prevent
            # double wrapping
            #cleaned_block = original_block.replace(':class: toggle-code', '')
            cleaned_block = original_block
            # Remove any empty class attributes that might be left
            cleaned_block = re.sub(r':class:\s*\[toggle-code\]', '', cleaned_block)
            cleaned_block = re.sub(r':class:\s*\n', '', cleaned_block)
            cleaned_block = re.sub(r':class:\s*$', '', cleaned_block,
                                   flags=re.MULTILINE)
            
            # Get localized labels
            labels = get_toggle_labels(language)
            
            # Wrap the code block in a toggle wrapper
            with open(SNIPPETS + 'toggle-code-block.md',
                      'r', encoding='utf-8') as f:
                toggle_snippet = f.read()
            
            content = toggle_snippet.format(show=labels['show'],
                                            cleaned_block=cleaned_block)
            result_parts.append(content)

        else:
            result_parts.append(original_block.replace('%this%', str(cell_number)))
        
        python_code_index += 1
        python_code = python_code.strip()
        
        # Extract imports from this code block
        imports = _extract_imports(python_code)
        all_imports.update(imports)
        
        # Split the Python code into setup and final parts
        setup_code, final_code = split_code(python_code)
        setup_code = setup_code.replace('%this%', str(cell_number))
        final_code = final_code.replace('%this%', str(cell_number))
        
        # Create only the HTML divs (no PyScript yet)
        # DELETED BECAUSE OF DOUBLE DIV CREATION
        # with open(SNIPPETS + 'cell-divs.md',
        #           'r', encoding='utf-8') as f:
        #     snippet = f.read()

        # html_divs = snippet.format(cell_number=cell_number, \
        #     splash_class=_get_div_classes('splash', class_attr),
        #     out_class=_get_div_classes('cell-out', class_attr),
        #     stdout_class=_get_div_classes('cell-stdout', class_attr),
        #     stderr_class=_get_div_classes('cell-stderr', class_attr),
        #     graph_class=_get_div_classes('cell-graph no-mathjax', class_attr))
        
        # if height_attr is not None:
        #     html_divs = html_divs.replace('class="splash"', 
        #                     f'class="splash" style="height: {height_attr};"')
            
        # result_parts.append(html_divs)
        
        # Check if matplotlib is used in this cell
        uses_matplotlib = _uses_matplotlib(python_code)
        
        # Create the PyScript block to be added later Add class attribute if
        # present, but NOT for toggle-code (that should only affect visible
        # code)
        py_script_class = ""
        if class_attr and 'toggle-code' not in class_attr:
            pass
        py_script_class = f' class="{class_attr}"'

        with open(SNIPPETS + 'pyscript-initial-content.pysnippet',
                  'r', encoding='utf-8') as f:
            snippet = f.read()
        pyscript_content = snippet.format(cell_number=cell_number,
                                          setup_code=_indent_code(setup_code,
                                                                 "    "))

        if final_code:
            final_code = final_code.replace('%this%', str(cell_number))
            pyscript_content += f'    # Execute final code and capture result'
            pyscript_content += '\n    result = None\n'
            
            # Only include matplotlib handling if matplotlib is actually used
            if uses_matplotlib:
                with open(SNIPPETS + 'pyscript-final-matplotlib.pysnippet',
                  'r', encoding='utf-8') as f:
                    snippet = f.read()
                pyscript_content += snippet.format(cell_number=cell_number,
                                                   final_code=final_code)
            else: # final-nomatplotlib
                with open(SNIPPETS + 'pyscript-final-nomatplotlib.pysnippet',
                  'r', encoding='utf-8') as f:
                    snippet = f.read()
                pyscript_content += snippet.format(final_code=final_code)
        else:
            # Only include matplotlib handling if matplotlib is actually used
            # (setup-only case)
            if uses_matplotlib:
                with open(SNIPPETS + 'pyscript-nofinal-matplotlib.pysnippet',
                  'r', encoding='utf-8') as f:
                    snippet = f.read()
                pyscript_content += snippet.format(cell_number=cell_number)

        with open(SNIPPETS + 'pyscript-middle.pysnippet',
                  'r', encoding='utf-8') as f:
            snippet = f.read()
        pyscript_content += snippet.format(cell_number=cell_number)
        
        if final_code:
            with open(SNIPPETS + 'pyscript-final.pysnippet',
                      'r', encoding='utf-8') as f:
                snippet = f.read()
            pyscript_content += snippet.format(cell_number=cell_number)

        if ':tags:' in pyscript_content:
            pyscript_content = pyscript_content.replace(':tags:', '#')
        
        pyscript_blocks.append(pyscript_content)
        
        current_pos = match.end()
        cell_number += 1
    
    # Add any remaining content after the last Python block
    result_parts.append(myst_content[current_pos:])
    
    # Add all PyScript blocks at the end
    if pyscript_blocks or inline_expressions:
        
        # Write the companion .py file for this page
        # source_path = Path(source_file)
        # script_name = source_path.stem + '.py'
        # script_dir = source_path.parent
        # script_path = script_dir / script_name

        all_pyscript_content = []

        # Add setup first if requested
        if include_setup:
            setup_content = generate_pyscript_setup()
            all_pyscript_content.append(f'{setup_content}\n')

        # Add PyScript code for inline expressions
        if inline_expressions:
            with open(SNIPPETS + 'inline-python-expressions.pysnippet',
                      'r', encoding='utf-8') as f:
                snippet = f.read()
            
            inline_pyscript_content = \
                snippet.format(inline_expressions=inline_expressions)

            all_pyscript_content.append(inline_pyscript_content)
            all_pyscript_content.append('\n\n')
            
        for block in pyscript_blocks:
            all_pyscript_content.append(block)
            all_pyscript_content.append('\n\n')

        all_pyscript_content = '\n\n'.join(all_pyscript_content)

        # with open(script_path, 'w', encoding='utf-8') as f:
        #     f.write(all_pyscript_content)

        result_parts.append('\n\n```{raw} html\n')
        # result_parts.append(f'<script type="py" '
        #                     f'src="{script_name}"></script>\n')
        result_parts.append(f'<script type="py">\n')
        result_parts.append(all_pyscript_content)
        result_parts.append('\n</script>\n')

        
        # Add toggle initialization script at the end if any toggle-code blocks
        # exist
        has_toggle_code = any('class="toggle-code"' in block
                              for block in pyscript_blocks)
        if has_toggle_code:
            with open(SNIPPETS + 'toggle-code-script.js',
                      'r', encoding='utf-8') as f:
                snippet = f.read()
            
            result_parts.append(f'<script>\n{snippet}\n</script>\n')
        
        result_parts.append('```')
    
    return ''.join(result_parts)

def _indent_code(code, indent):
    '''Helper function to indent code lines.
    
    Args:
        code (str): The code to indent
        indent (str): The indentation string to use
    Returns:
        str: The indented code
    '''
    if not code:
        return ''
    
    lines = code.split('\n')
    indented_lines = [indent + line if line.strip() else line for line in lines]
    return '\n'.join(indented_lines)

def process_myst_file(file_path, include_setup=True):
    '''Processes a MyST Markdown file and replaces its contents with
    interactive HTML blocks.
    
    Creates a backup of the original file before processing.
    
    Args:
        file_path (str): Path to the MyST Markdown file to process
        include_setup (bool): Whether to include the initial PyScript setup
            (default: True)
    Returns:
        str: Path to the backup file that was created
    Raises:
        FileNotFoundError: If the input file doesn't exist
        IOError: If there are issues reading/writing files
    '''
    
    # Convert to Path object for easier manipulation
    file_path = Path(file_path)
    
    # Check if the file exists
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Create backup file path
    backup_path = file_path.with_suffix(file_path.suffix + '.backup')
    
    # Create backup
    try:
        shutil.copy2(file_path, backup_path)
    except IOError as e:
        raise IOError(f"Failed to create backup: {e}")
    
    # Read the original file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except IOError as e:
        # If we can't read the file, remove the backup and re-raise
        backup_path.unlink(missing_ok=True)
        raise IOError(f"Failed to read file: {e}")
    
    # Determine language from file path
    language = 'en'  # default
    path_parts = file_path.parts
    if 'it' in path_parts:
        language = 'it'
    elif 'en' in path_parts:
        language = 'en'
    elif 'fr' in path_parts:
        language = 'fr'
    elif 'es' in path_parts:
        language = 'es'
    
    # Process the content
    try:
        processed_content = process_myst_document(original_content,
                                                  source_file=file_path,
                                                  include_setup=include_setup,
                                                  language=language)
    except Exception as e:
        # If processing fails, remove the backup and re-raise
        backup_path.unlink(missing_ok=True)
        raise RuntimeError(f"Failed to process MyST content: {e}")
    
    # Write the processed content back to the original file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(processed_content)
    except IOError as e:
        # If we can't write, try to restore from backup
        try:
            shutil.copy2(backup_path, file_path)
        except IOError:
            pass  # Best effort to restore
        raise IOError(f"Failed to write processed file: {e}")
    
    return str(backup_path)

def _extract_imports(code):
    '''Extract imported package names from Python code.
    
    Args:
        code (str): Python source code
    Returns:
        set: Set of imported package names
    '''
    
    if not code.strip():
        return set()
    
    packages = set()
    
    try:
        # Parse the code to extract imports
        tree = ast.parse(code)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    # Get the top-level package name
                    package = alias.name.split('.')[0]
                    packages.add(package)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    # Get the top-level package name
                    package = node.module.split('.')[0]
                    packages.add(package)
    except (SyntaxError, ValueError):
        # If AST parsing fails, try regex-based extraction as fallback
        import_patterns = [
            r'^\s*import\s+([a-zA-Z_][a-zA-Z0-9_.]*)',
            r'^\s*from\s+([a-zA-Z_][a-zA-Z0-9_.]*)\s+import'
        ]
        
        for line in code.split('\n'):
            line = line.strip()
            for pattern in import_patterns:
                match = re.match(pattern, line)
                if match:
                    package = match.group(1).split('.')[0]
                    packages.add(package)
    
    # Filter out built-in modules and common standard library modules that
    # don't need to be declared
    builtin_modules = {
        'sys', 'os', 'io', 'json', 're', 'math', 'random', 'datetime',
        'collections', 'itertools', 'functools', 'operator', 'copy',
        'typing', 'pathlib', 'urllib', 'html', 'xml', 'csv', 'sqlite3',
        'threading', 'multiprocessing', 'subprocess', 'shutil', 'glob',
        'tempfile', 'gzip', 'zipfile', 'tarfile', 'pickle', 'struct',
        'codecs', 'unicodedata', 'string', 'textwrap', 'difflib',
        'hashlib', 'hmac', 'secrets', 'uuid', 'time', 'calendar',
        'zoneinfo', 'locale', 'gettext', 'argparse', 'logging',
        'getpass', 'curses', 'platform', 'errno', 'ctypes', 'mmap',
        'winreg', 'msvcrt', 'winsound', 'posix', 'pwd', 'grp', 'crypt',
        'spwd', 'pty', 'fcntl', 'resource', 'nis', 'syslog', 'signal',
        'socket', 'ssl', 'select', 'selectors', 'asyncio', 'queue',
        'email', 'mailbox', 'mimetypes', 'base64', 'binhex', 'binascii',
        'quopri', 'uu', 'encodings', 'stringprep', 'readline', 'rlcompleter',
        'pdb', 'profile', 'pstats', 'timeit', 'trace', 'tracemalloc',
        'faulthandler', 'gc', 'inspect', 'site', 'fpectl', 'dis',
        'pickletools', 'distutils', 'unittest', 'doctest', 'test',
        'lib2to3', 'venv', 'ensurepip', 'zipapp', 'runpy', 'importlib',
        'pkgutil', 'modulefinder', 'compileall', 'py_compile', 'zipimport',
        'ast', 'symtable', 'symbol', 'token', 'keyword', 'tokenize',
        'tabnanny', 'pyclbr', 'py_compile', 'compileall', 'dis',
        'pickletools', 'formatter', 'warnings', 'contextlib', 'abc',
        'atexit', 'traceback', 'gc', 'weakref', 'builtins', 'decimal'
    }

    # fix Pillow package name
    if 'PIL' in packages:
        packages.remove('PIL')
        packages.add('Pillow')
    
    # Return only packages that are not built-in
    return packages - builtin_modules

def _uses_matplotlib(code):
    '''Check if code uses matplotlib or pyplot functionality.
    
    Args:
        code (str): Python source code
        
    Returns:
        bool: True if matplotlib is used, False otherwise
    '''

    if not code:
        return False
    
    # Check for matplotlib imports
    matplotlib_import_patterns = [
        r'import\s+matplotlib',
        r'from\s+matplotlib',
        r'import\s+matplotlib\.pyplot',
        r'from\s+matplotlib\.pyplot',
        r'import\s+pylab',
        r'from\s+pylab'
    ]
    
    for pattern in matplotlib_import_patterns:
        if re.search(pattern, code, re.MULTILINE):
            return True
    
    # Check for pyplot usage patterns
    pyplot_patterns = [
        r'plt\.',
        r'pyplot\.',
        r'pylab\.',
        r'matplotlib\.pyplot\.',
        r'plt\.show\(',
        r'plt\.plot\(',
        r'plt\.scatter\(',
        r'plt\.bar\(',
        r'plt\.hist\(',
        r'plt\.figure\(',
        r'plt\.subplot\(',
        r'plt\.savefig\(',
        r'plt\.close\(',
        r'plt\.clf\(',
        r'plt\.cla\(',
        r'plt\.legend\(',
        r'plt\.xlabel\(',
        r'plt\.ylabel\(',
        r'plt\.title\(',
        r'plt\.grid\(',
        r'plt\.axis\(',
        r'plt\.xlim\(',
        r'plt\.ylim\(',
        r'plt\.tight_layout\(',
        r'plt\.subplots\(',
        r'plt\.pie\(',
        r'plt\.boxplot\(',
        r'plt\.violinplot\(',
        r'plt\.heatmap\(',
        r'plt\.imshow\(',
        r'plt\.contour\(',
        r'plt\.contourf\(',
        r'plt\.quiver\(',
        r'plt\.streamplot\(',
        r'plt\.colorbar\(',
        r'plt\.clim\(',
        r'plt\.gca\(',
        r'plt\.gcf\(',
        r'plt\.get_fignums\(',
        r'plt\.switch_backend\(',
        r'plt\.ioff\(',
        r'plt\.ion\(',
        r'plt\.isinteractive\(',
        r'plt\.pause\(',
        r'plt\.draw\(',
        r'plt\.show\(',
        r'plt\.waitforbuttonpress\(',
    ]
    
    for pattern in pyplot_patterns:
        if re.search(pattern, code, re.MULTILINE):
            return True
    
    return False

def make_part_titles_clickable_and_collapsible(html_root_dir, dry_run=False,
                                               language='it'):
    '''Add collapsible functionality to part sub-TOCs without making part
    titles clickable.'''
    
    # Parse the TOC file to find parts
    toc_file = f'source/{language}/_toc.yml'
    if not os.path.exists(toc_file):
        print(f"TOC file {toc_file} not found")
        return
        
    with open(toc_file, 'r', encoding='utf-8') as f:
        toc_data = yaml.safe_load(f)
    
    # Find all parts (treat all parts equally - no links, just collapsible)
    part_captions = []
    
    for part in toc_data.get('parts', []):
        caption = part.get('caption', '')
        if caption:
            part_captions.append(caption)
            # print(f"Found part '{caption}' - will be made collapsible")
    
    if not part_captions:
        print(f"No parts found for language {language}")
        return
        
    print(f"Making part titles collapsible for {language}...")
    html_files = glob.glob(os.path.join(html_root_dir, '**', '*.html'),
                           recursive=True)

    with open(SNIPPETS + 'collapsible.js',
              'r', encoding='utf-8') as f:
        snippet = f.read()
    collapsible_js = f'<script>\n{snippet}\n</script>'
    
    files_modified = 0
    processed_parts = set()  # Track which parts we've already logged
    
    print('Add collapsible class to TOC parts')
    for html_file in tqdm(html_files):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            soup = BeautifulSoup(content, 'html.parser')
            changed = False
            has_parts = False
            
            # Process all parts (make them collapsible only, no links)
            
            for part_caption in part_captions:
                # Find elements that are ACTUAL part headers, not just any
                # element containing the text Part headers should be <p>
                # elements with class="caption" and role="heading"
                potential_elements = soup.find_all(lambda tag: 
                    tag.name == 'p' and 
                    'caption' in tag.get('class', []) and
                    tag.get('role') == 'heading' and
                    tag.get_text(strip=True) == part_caption)
                
                if potential_elements:
                    has_parts = True
                
                
                for element in potential_elements:
                    # Check if this is in the TOC sidebar (has TOC-related
                    # classes or parents)
                    parent_classes = []
                    current = element
                    while current and current.name and len(parent_classes) < 10:
                        if current.get('class'):
                            parent_classes.extend(current.get('class'))
                        current = current.parent
                    
                    # If it's in the TOC, process it regardless of existing
                    # classes
                    classes = ['bd-links', 'bd-docs-nav', 'bd-sidebar',
                               'toctree', 'sidebar', 'nav']
                    if any(cls in parent_classes for cls in classes):

                        if not dry_run:
                            # Check if this element contains a link that should
                            # be removed
                            existing_link = element.find('a')
                            if existing_link:
                                # Remove the link but keep the text content
                                link_text = existing_link.get_text(strip=True)
                                existing_link.extract()  # Remove the <a> tag
                                
                                # If the element is now empty, add the text back
                                warn = f"Removed link from '{part_caption}'" \
                                       "but kept collapsible functionality"
                                if not element.get_text(strip=True):
                                    element.string = link_text
                                    changed = True
                                    if part_caption not in processed_parts:
                                        print(warn)
                                        processed_parts.add(part_caption)
                                elif element.get_text(strip=True) != link_text:
                                    # The element has other content, add back
                                    # just the text
                                    element.append(link_text)
                                    changed = True
                                    if part_caption not in processed_parts:
                                        print(warn)
                                        processed_parts.add(part_caption)
                            
                            # Ensure collapsible class is present (add if
                            # missing)
                            if 'part-collapsible' not in element.get('class',
                                                                     []):
                                element['class'] = element.get('class', []) + \
                                                        ['part-collapsible']
                                changed = True
                                # warn = "Added collapsible class to " \
                                #        f"'{part_caption}'"
                                if part_caption not in processed_parts:
                                    processed_parts.add(part_caption)
                            
                            # Find the following chapters list and ensure it
                            # has the right class
                            chapters_container = element.find_next_sibling()
                            if chapters_container and chapters_container.name \
                                    in ['ul', 'ol', 'div']:
                                if 'part-chapters' not in \
                                        chapters_container.get('class', []):
                                    chapters_container['class'] = \
                                        chapters_container.get('class', []) + \
                                            ['part-chapters']
                                    changed = True
                        else:
                            # In dry run, check if there are links that would
                            # be removed
                            existing_link = element.find('a')
                            if existing_link:
                                changed = True
                    else:
                        pass  # Element not in TOC, skip

            # Convert chapter details elements to use the same custom
            # collapsible approach as parts
            if not dry_run:
                # Clean up: Remove part-collapsible class from elements that
                # shouldn't have it (regular chapter/section links that were
                # incorrectly classified)
                incorrect_part_elements = soup.find_all(lambda tag:
                    'part-collapsible' in tag.get('class', []) and
                    tag.name in ['li', 'a'] and
                    not (tag.name == 'p' and
                         'caption' in tag.get('class', []) and
                         tag.get('role') == 'heading'))
                
                incorrect_elements_found = []
                for element in incorrect_part_elements:
                    element_text = element.get_text(strip=True)[:50]
                    if element_text not in incorrect_elements_found:
                        incorrect_elements_found.append(element_text)
                        warn = 'Removed incorrect part-collapsible class from' \
                               f' {element.name} element: {element_text}'
                        print(warn)
                    
                    classes = element.get('class', [])
                    classes = [cls for cls in classes
                               if cls != 'part-collapsible']
                    element['class'] = classes
                    changed = True
                    
                # Find all details elements (used for chapters with sub-items)
                details_elements = soup.find_all('details')
                for details in details_elements:
                    # Get the parent li element
                    parent_li = details.find_parent('li')
                    if parent_li and parent_li.get('class') and \
                            'has-children' in parent_li.get('class', []):
                        # Get the main chapter link (before the details)
                        chapter_link = None
                        for sibling in parent_li.children:
                            if hasattr(sibling, 'name') and sibling.name == 'a':
                                chapter_link = sibling
                                break
                        
                        if chapter_link:
                            # Add custom collapsible class to the chapter link
                            chapter_link['class'] = \
                                chapter_link.get('class', []) + \
                                    ['chapter-collapsible']
                            
                            # Get the sub-items from details
                            sub_ul = details.find('ul')
                            if sub_ul:
                                # Add custom class to sub-items
                                sub_ul['class'] = sub_ul.get('class', []) + \
                                ['chapter-sub-items']
                                
                                # Remove the details wrapper and move sub-items
                                # after the chapter link
                                details.extract()  # Remove details element
                                # Add sub-items directly to parent li
                                parent_li.append(sub_ul)
                                
                                changed = True
            # Use only actually needed python packages in py-config
            if not dry_run:


                # # extract imports from the companion .py file
                # py_source = Path(html_file).with_suffix('.py')
                # if os.path.exists(py_source):
                #     with open(py_source, 'r', encoding='utf-8') as f:
                #         content_all = f.read()

                #     # Regex matches from #BEGIN# import matplotlib to #END#
                #     pattern = rf"(?ms)^#BEGIN# import {re.escape('matplotlib')}\s*\n.*?^#END#\s*\n?"

                #     match = re.search(pattern, content_all)
                #     if match:
                #         block = match.group(0)
                #         content_no_plt = content_all.replace(block, "", 1)
                #     else:
                #         msg = f'Could not find matplotlib import in {py_source}'
                #         raise ValueError(msg)

                #     needed_packages = _extract_imports(content_no_plt)

                #     if 'matplotlib' not in needed_packages:
                #         with open(py_source, 'w', encoding='utf-8') as f:
                #             f.write(content_no_plt)

                #     py_config = soup.find("py-config")
                #     needed_packages.discard('js')
                #     needed_packages.discard('pyscript')
                #     needed_packages.discard('pyodide')
                #     if needed_packages:
                #         custom_packages = sorted(needed_packages)

                #         config_data = json.loads(py_config.string)
                #         config_data["packages"] = custom_packages

                #         py_config.string = json.dumps(config_data, indent=2)
                #     else:
                #         # py_config.decompose()
                #         pass
                # # Replace %this% placeholders in script tags
                # script_tags = soup.find_all('script', type='py')
                # for script in script_tags:
                #     if script.string and '%this%' in script.string:
                #         # Generate a unique cell number based on position
                #         cell_num = len([s for s in soup.find_all('script', type='py') 
                #                     if s.sourceline < script.sourceline]) + 1
                #         script.string = script.string.replace('%this%', str(cell_num))
                #         changed = True

                # # Regex matches from #BEGIN# import matplotlib to #END#
                # pattern = rf"(?ms)^#BEGIN# import {re.escape('matplotlib')}\s*\n.*?^#END#\s*\n?"

                # match = re.search(pattern, content)
                # if match:
                #     block = match.group(0)
                #     content_no_plt = content.replace(block, "", 1)
                # else:
                #     msg = f'Could not find matplotlib import in {py_source}'
                #     raise ValueError(msg)

                # needed_packages = _extract_imports(content_no_plt)

                # if 'matplotlib' not in needed_packages:
                #     content = content_no_plt

                # py_config = soup.find("py-config")
                # needed_packages.discard('js')
                # needed_packages.discard('pyscript')
                # needed_packages.discard('pyodide')
                # if needed_packages:
                #     custom_packages = sorted(needed_packages)

                #     config_data = json.loads(py_config.string)
                #     config_data["packages"] = custom_packages

                #     py_config.string = json.dumps(config_data, indent=2)
                # else:
                #     # py_config.decompose()
                #     pass

                # REMOVED 2026-01-04 as double replacement generates errors
                # script_tags = soup.find_all('script', type='py')
                # for script in script_tags:
                #     if not script.string:
                #         continue
                #     if '%this%' in script.string:
                #         # Generate a unique cell number based on position
                #         cell_num = len([s for s in soup.find_all('script', type='py') 
                #                     if s.sourceline < script.sourceline]) + 1
                #         script.string = script.string.replace('%this%', str(cell_num))
                #         changed = True

                pattern = rf"(?ms)^#BEGIN# import {re.escape('matplotlib')}\s*\n.*?^#END#\s*\n?"
                if soup.string:
                    match = re.search(pattern, soup.string)
                    if match:
                        block = match.group(0)
                        content_no_plt = soup.string.replace(block, "", 1)
                        needed_packages = _extract_imports(content_no_plt)
                        if 'matplotlib' not in needed_packages:
                            soup.string.replace_with(content_no_plt)
                    else:
                        msg = f'Could not find matplotlib import in {html_file}'
                        raise ValueError(msg)

            # Add CSS and JavaScript if we have parts or chapters (regardless
            # of whether we made changes)
            if (has_parts or soup.find_all('details')):
                if not dry_run:
                    # Add CSS to head (replace if exists)
                    head = soup.find('head')
                    if head:
                        # Remove existing part-collapsible styles - find by
                        # content
                        for style_tag in head.find_all('style'):
                            if style_tag.string and \
                                'part-collapsible' in style_tag.string:
                                style_tag.decompose()
                        
                        changed = True
                    
                    # Add JavaScript before closing body (replace if exists)
                    body = soup.find('body')
                    if body:
                        # Remove existing part-collapsible script - find by
                        # content
                        for script_tag in body.find_all('script'):
                            if script_tag.string and \
                                    'part-collapsible' in script_tag.string:
                                script_tag.decompose()
                        
                        body.append(BeautifulSoup(collapsible_js,
                                                  'html.parser'))
                        changed = True
                else:
                    # In dry run, still mark that changes would be made for
                    # CSS/JS injection
                    head = soup.find('head')
                    body = soup.find('body')
                    if head or body:
                        changed = True
                
                if changed:
                    if not dry_run:
                        with open(html_file, 'w', encoding='utf-8') as f:
                            f.write(str(soup))
                            
                    files_modified += 1
                    
        except Exception as e:
            print(f"Error processing {html_file}: {e}")
    
    if not dry_run:
        print(f"Collapsible functionality applied successfully!")
        print(f"  - Modified {files_modified} HTML files")
        print(f"  - Processed {len(processed_parts)} unique part sections: "
              f"{', '.join(sorted(processed_parts))}")
    else:
        print(f"Would modify {files_modified} files")

def replace_mystnb_toggle_divs(html_root_dir, dry_run=False, language='it'):
    """
    Replace myst-nb generated toggle code divs with custom toggle structure.
    
    Args:
        html_root_dir (str): Path to the HTML build directory
        dry_run (bool): If True, don't actually modify files
        language (str): Language code for localization (default: 'it')
    """
    
    print("Replacing myst-nb toggle code divs...")
    html_files = list(Path(html_root_dir).rglob("*.html"))
    
    # Get localized labels
    labels = get_toggle_labels(language)
    
    files_modified = 0
    total_replacements = 0
    
    for html_file in tqdm(html_files):
        # Skip certain files
        if any(skip in str(html_file) 
               for skip in ['_static', 'genindex', 'search']):
            continue
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            changed = False
            
            # Find all details elements with the specific class pattern
            details_elements = soup.find_all('details', 
                                            class_='admonition hide above-input')
            
            for details in details_elements:
                # Verify it has the expected structure with summary
                summary = details.find('summary')
                if summary and summary.get('aria-label') == 'Toggle hidden content':
                    # Extract the code content (everything except the summary)
                    code_content = details.find('div', class_='cell_input')
                    
                    if not code_content:
                        continue
                    
                    # Create the wrapper div
                    wrapper_div = soup.new_tag('div', **{'class': 'toggle-code-wrapper'})
                    
                    # Create the button (collapsed state, no 'expanded' class)
                    button = soup.new_tag('button', **{
                        'class': 'toggle-code-button',
                        'data-toggle-processed': 'true'
                    })
                    
                    # Add triangle span
                    triangle_span = soup.new_tag('span', **{'class': 'triangle'})
                    triangle_span.string = '▶'
                    button.append(triangle_span)
                    
                    # Add button text span
                    button_text_span = soup.new_tag('span', **{'class': 'button-text'})
                    button_text_span.string = f' {labels["show"]}'
                    button.append(button_text_span)
                    
                    wrapper_div.append(button)
                    
                    # Create the content div (collapsed state, no 'expanded' class)
                    content_div = soup.new_tag('div', **{'class': 'toggle-code-content'})
                    
                    # Create cell container
                    cell_div = soup.new_tag('div', **{'class': 'cell docutils container'})
                    
                    # Move the code content into the cell div
                    cell_div.append(code_content.extract())
                    content_div.append(cell_div)
                    wrapper_div.append(content_div)
                    
                    # Replace the details element with our new structure
                    details.replace_with(wrapper_div)
                    changed = True
                    total_replacements += 1
            
            # Add toggle initialization script if we made changes
            if changed and not dry_run:
                # Check if toggle script already exists
                body = soup.find('body')
                if body:
                    existing_script = body.find('script', string=lambda s: s and 'toggle-code-button' in s)
                    if not existing_script:
                        # Add the toggle script
                        with open(SNIPPETS + 'toggle-code-script.js', 'r', encoding='utf-8') as f:
                            toggle_js = f.read()
                        
                        script_tag = soup.new_tag('script')
                        script_tag.string = toggle_js
                        body.append(script_tag)
            
            if changed:
                files_modified += 1
                if not dry_run:
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                else:
                    print(f"Would modify: {html_file}")
        
        except Exception as e:
            print(f"Error processing {html_file}: {e}")
            continue
    
    print(f"\nSummary:")
    print(f"  Files modified: {files_modified}")
    print(f"  Total replacements: {total_replacements}")
    
    return files_modified, total_replacements



def process_html_py_roles(html_root_dir, dry_run=False, language='en'):
    '''
    Process HTML files to replace any remaining {py} roles with interactive
    spans.
    
    This function handles {py} roles that weren't processed during MyST
    pre-processing or that were stripped/modified by Sphinx during HTML
    generation.
    
    Args:
        html_root_dir (str): Path to the HTML build directory
        dry_run (bool): If True, show what would be changed without making
            changes
        language (str): Language code for localization
    
    Returns:
        dict: Summary of changes made
    '''
    
    changes_summary = {
        'files_processed': 0,
        'files_modified': 0,
        'total_replacements': 0,
        'replacements_by_file': {},
        'errors': []
    }
    
    # Find all HTML files
    html_files = list(Path(html_root_dir).rglob("*.html"))
    
    cell_counter = 1  # Global counter for inline expressions
    all_inline_expressions = []  # Collect all inline expressions for PyScript
    
    for html_file in html_files:
        # Skip certain files that shouldn't be modified
        if any(skip in str(html_file)
               for skip in ['_static', 'genindex', 'search']):
            continue
            
        changes_summary['files_processed'] += 1
        file_replacements = 0
        file_inline_expressions = []
        
        try:
            # Read the HTML file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            
            # Pattern to match {py} roles in HTML
            # This could appear in various forms after Sphinx processing:
            # 1. As literal text: {py}`code`
            # 2. As code elements: <code>{py}`code`</code>
            # 3. Remaining MyST format: {py}`code`
            
            py_role_patterns = [
                # Pattern 1: Direct {py} role syntax
                r'\{py\}`([^`]+)`',
                # Pattern 2: Inside code tags
                r'<code[^>]*>\{py\}`([^`]+)`</code>',
                # Pattern 3: Sphinx might convert it to emphasis
                r'<em[^>]*>\{py\}`([^`]+)`</em>',
            ]
            
            for pattern in py_role_patterns:
                matches = list(re.finditer(pattern, content))
                # Process in reverse to maintain positions
                for match in reversed(matches):
                    python_code = match.group(1)
                    
                    # Generate the inline Python HTML
                    inline_html = generate_inline_python(python_code,
                                                         cell_counter,
                                                         language)
                    
                    # Store the expression for PyScript execution
                    file_inline_expressions.append((cell_counter, python_code))
                    all_inline_expressions.append((cell_counter, python_code))
                    
                    if not dry_run:
                        # Replace the match with our generated HTML
                        content = content[:match.start()] + \
                            inline_html + content[match.end():]
                    
                    file_replacements += 1
                    cell_counter += 1
            
            # If we made changes, save the file
            if file_replacements > 0:
                changes_summary['files_modified'] += 1
                changes_summary['total_replacements'] += file_replacements
                changes_summary['replacements_by_file'][str(html_file)] = \
                    file_replacements
                
                if not dry_run:
                    # Create backup
                    backup_file = html_file.with_suffix('.html.backup')
                    with open(backup_file, 'w', encoding='utf-8') as f:
                        f.write(original_content)
                    
                    # Write modified content
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"✓ {html_file.relative_to(html_root_dir)}: "
                          f"{file_replacements} {{py}} role(s) replaced")
                else:
                    print(f"Would replace {file_replacements} {{py}} role(s) "
                          f"in {html_file.relative_to(html_root_dir)}")
                    
        except Exception as e:
            error_msg = f"Error processing {html_file}: {e}"
            changes_summary['errors'].append(error_msg)
            print(f"Error: {error_msg}")
    
    # Add PyScript execution for all inline expressions found
    if all_inline_expressions and not dry_run:
        _add_pyscript_for_inline_expressions(html_root_dir,
                                             all_inline_expressions)
    
    return changes_summary


def _add_pyscript_for_inline_expressions(html_root_dir, inline_expressions):
    '''
    Add PyScript execution code to the first HTML file to handle inline
    expressions.
    
    Args:
        html_root_dir (str): Path to the HTML build directory  
        inline_expressions (list): List of (cell_number, python_code) tuples
    '''
    
    # Find the first suitable HTML file (not in _static, genindex, etc.)
    html_files = list(Path(html_root_dir).rglob("*.html"))
    target_file = None
    
    for html_file in html_files:
        if not any(skip in str(html_file)
                   for skip in ['_static', 'genindex', 'search']):
            target_file = html_file
            break
    
    if not target_file:
        print("Warning: No suitable HTML file found to add PyScript execution")
        return
    
    try:
        # Read the target file
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create the PyScript execution code
        with open(SNIPPETS + 'pyscript-inline.pysnippet',
                  'r', encoding='utf-8') as f:
            snippet = f.read()
            pyscript_code = snippet.format(
                inline_expressions=inline_expressions)
        
        # Try to insert the PyScript code before the closing </body> tag
        if '</body>' in content:
            content = content.replace('</body>', pyscript_code + '\n</body>')
        else:
            # Fallback: append at the end
            content += pyscript_code
        
        # Write the modified content
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Added PyScript execution for {len(inline_expressions)} "
              f"inline expressions to {target_file.relative_to(html_root_dir)}")
        
    except Exception as e:
        print(f"Error adding PyScript to {target_file}: {e}")

def generate_toc(language='it', toc_data=None, dry_run=False):
    '''
    Reads the _toc.yml file for a specified language and creates an OrderedDict
    with chapter and section numbering.
    
    Args:
        language (str): Language code ('it', 'en', 'fr', 'es')
        toc_data (dict): Optional TOC data dictionary. If provided, will use 
                        this instead of reading from file.
    
    Returns:
        OrderedDict: Dictionary mapping titles to numbers where:
                    - chapters get numbers like "1", "2", "3"
                    - sections get numbers like "1.1", "1.2", "2.1"
                    - appendix chapters get letters like "A", "B", "C"
                    - appendix sections get numbers like "A.1", "A.2", "B.1"
    '''

    appendix_keyword = {'it': 'Appendici', 'en': 'Appendices',
                        'fr': 'Annexes', 'es': 'Apéndices'}

    # If toc_data is not provided, read from the _toc.yml file
    if toc_data is None:
        # Find the corresponding _toc.yml file
        toc_file = f'source/{language}/_toc.yml'
        if not os.path.exists(toc_file):
            raise FileNotFoundError(f"TOC file for language '{language}' "
                                    f"not found: {toc_file}")

        try:
            with open(toc_file, 'r', encoding='utf-8') as f:
                toc_data = yaml.safe_load(f)
        except Exception as e:
            raise RuntimeError(f"Error reading TOC file {toc_file}: {e}")
        
        mock = False
    else:
        mock = True
    
    # Function to extract title and label from markdown file
    def extract_title_and_label_from_file(file_path):
        """Extract the first heading and its immediately preceding label
        from a markdown file."""

        if mock:
            title = file_path.split('/')[-1].split('.')[0].capitalize()
            label = file_path.replace('/', '_')
        else:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                label = None
                title = None
                for i, line in enumerate(lines):
                    # Look for the first h1 heading
                    title_match = re.match(r'^#\s+(.+)$', line)
                    if title_match:
                        # Check previous non-empty line for label
                        j = i - 1
                        while j >= 0 and lines[j].strip() == '':
                            j -= 1
                        if j >= 0:
                            # Match (label)= format
                            label_match = re.match(r'^\(([\w\-:]+)\)=\s*$',
                                                   lines[j].strip())
                            if label_match:
                                label = label_match.group(1)

                        title = title_match.group(1).strip()
                        title = title.replace('<span class=\"ast\">\\*</span>',
                                              '<span class=\"ast\">*</span>')
                        break

            except Exception as e:
                raise RuntimeError(f"Error reading file {file_path}: {e}")
        return title, label

    toc = TOC(language=language)
    for part in toc_data.get('parts', []):
        caption = part.get('caption', '')
        chapters = part.get('chapters', [])

        if caption == appendix_keyword.get(language, ''):
            toc.start_appendix()

        for chapter in chapters:
            file_path = chapter.get('file', '')
            label = None
            title = None

            full_file_path = f'source/{language}/{file_path}.md'
            title, label = extract_title_and_label_from_file(full_file_path)
            if not title:
                raise RuntimeError(f"Missing chapter title in {full_file_path}")
            if not label:
                raise RuntimeError("Missing cross-reference label before "
                                   f"chapter title in {full_file_path}")
            
            toc.add_chapter(file_path, label, title)
            
            # Sections
            sections = chapter.get('sections', [])
            for section in sections:
                section_file = section.get('file', '')
                section_title = section.get('title')
                section_label = None
                section_title = None
                
                full_section_path = f'source/{language}/{section_file}.md'
                section_title, section_label = \
                    extract_title_and_label_from_file(full_section_path)
                if not section_title:
                    raise RuntimeError("Missing section title in "
                                       f"{full_section_path}")
                if not section_label:
                    raise RuntimeError("Missing cross-reference label before "
                                       f"section title in {full_section_path}")
            
                toc.add_section(section_file, section_label, section_title)
                
    return toc

def apply_numbering(language):
    '''
    Recursively list all HTML files in build/sds/<language> and print their
    paths.
    
    Args:
        language (str): Language code (e.g., 'it', 'en', 'fr', 'es').
    '''

    html_dir = os.path.join('build', 'sds', language)
    html_files = glob.glob(os.path.join(html_dir, '**', '*.html'),
                           recursive=True)
    skip_list = ['genindex.html', # get_root_doc(language) + '.html',
                 'prf-prf.html', 'search.html', 'index.html']
    
    numbered_toc = generate_toc(language=language)
    print('Fixing cross-reference numbers and dealing with localization')
    for file_path in tqdm(html_files):
        if file_path in [f'build/sds/{language}/' + f for f in skip_list]:
            continue
        if '_static' in file_path or '_sources' in file_path:
            continue

        short_path = file_path if len(file_path) < 60 \
                               else '...' + file_path[-57:]
        if len(short_path) < 60:
            short_path = short_path.ljust(60)
        # print(f"Apply numbering to: {short_path}", end='\r', flush=True)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
        except Exception as e:
            raise IOError(f"Error reading file {file_path}: {e}")

        # Try to parse the HTML content into a DOM object
        try:
            file_soup = BeautifulSoup(html_content, 'html.parser')
        except Exception as e:
            raise RuntimeError("Error parsing HTML content "
                               f"with BeautifulSoup: {e}")
        
        toc_nav = file_soup.find("nav", class_="bd-links")
        if toc_nav is None:
            # fallback: try bd-docs-nav
            toc_nav = file_soup.find("nav", class_="bd-docs-nav")
        if toc_nav is None:
            raise ValueError("TOC navigation element not found")
        
        def sanitize(text):
            """Sanitize text to remove unwanted characters."""
            return text.replace('’', "'").strip()
        
        for t, n in zip (toc_nav.find_all('li')[1:], numbered_toc.toc):
            a_tag = t.find('a')
            original_title = sanitize(a_tag.decode_contents())
            if original_title != n['title']:
                print(f"  - Mismatching TOC item: '{original_title}' "
                      f"with '{n['title']}'")
                continue
            a_tag.insert(0, NavigableString(f"{n['number']}. "))

        title = file_soup.find('h1')
        
        relative_file_path = file_path[len(f'build/sds/{language}/'):][:-5]
        if relative_file_path != get_root_doc(language):
            title.insert(0, \
                NavigableString( \
                    f"{numbered_toc.file_to_number[relative_file_path]}. "))

        # find all a tags in the file_soup having class "reference internal"
        for a_tag in file_soup.find_all('a', class_='reference internal'):
            label = a_tag['href'].split('#')[-1]
            if label in numbered_toc.label_to_caption:
                a_tag.string = numbered_toc.label_to_caption[label]

        for a_tag in file_soup.find_all('a',
                                class_='only-number reference internal'):
            label = a_tag['href'].split('#')[-1]
            if label in numbered_toc.label_to_caption:
                a_tag.string = (numbered_toc.label_to_caption[label]
                                            .split(' ')[-1])
        
        # for text_node in file_soup.find_all(string=True):
        #     if "Theorem" in text_node:
        #         text_node.replace_with(text_node.replace("Theorem", 
        #                                 LABELS[language]["theorem"]))
        for text_node in file_soup.find_all(string=True):
            for key in LABELS:
                if key in text_node:
                    text_node.replace_with(text_node.replace(key,
                                        LABELS[key][language]))



        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(file_soup))
    print()
    return

def fix_pyscript_dataframe_outputs(html_root_dir, dry_run=False):
    """
    Move cell-div-container divs outside toggle-code-wrapper for PyScript cells
    that output DataFrames.
    
    Args:
        html_root_dir (str): Path to the HTML build directory
        dry_run (bool): If True, don't actually modify files
    """
    
    print("Fixing PyScript DataFrame outputs in toggle wrappers...")
    html_files = list(Path(html_root_dir).rglob("*.html"))
    
    files_modified = 0
    total_fixes = 0
    
    for html_file in tqdm(html_files):
        if any(skip in str(html_file) 
               for skip in ['_static', 'genindex', 'search']):
            continue
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            changed = False
            
            # Find all toggle-code-wrapper divs
            toggle_wrappers = soup.find_all('div', class_='toggle-code-wrapper')
            
            for wrapper in toggle_wrappers:
                # Look for cell-div-container inside the wrapper
                cell_div_container = wrapper.find('div', class_='cell-div-container')
                
                if cell_div_container:
                    # Extract it from its current position
                    cell_div_container = cell_div_container.extract()
                    
                    # Insert it right after the wrapper
                    wrapper.insert_after(cell_div_container)
                    
                    changed = True
                    total_fixes += 1
            
            if changed:
                files_modified += 1
                if not dry_run:
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                else:
                    print(f"Would modify: {html_file}")
        
        except Exception as e:
            print(f"Error processing {html_file}: {e}")
            continue
    
    print(f"\nSummary:")
    print(f"  Files modified: {files_modified}")
    print(f"  Total fixes: {total_fixes}")
    
    return files_modified, total_fixes

def main():
    '''Command-line interface for sds.py functions.'''

    parser = argparse.ArgumentParser(description='Process documentation files')
    subparsers = parser.add_subparsers(dest='command',
                                       help='Available commands')

    # Add subparser for chapter-section numbering
    parser_numbering = subparsers.add_parser('apply-numbering',
                    help='Apply chapter and section numbering to HTML files')
    parser_numbering.add_argument('--language', default='it', 
                    help='Language code (it, en, fr, es)')
    
    # Add subparser for making parts clickable and collapsible
    parser_clickable = subparsers.add_parser('make-parts-clickable',
                    help='Make part titles clickable and collapsible in TOC')
    parser_clickable.add_argument('html_dir', help='HTML build directory')
    parser_clickable.add_argument('--language', default='it', 
                    help='Language code (it, en, fr, es)')
    parser_clickable.add_argument('--dry-run', action='store_true',
                    help='Show what would be changed without making changes')
    
    # Add subparser for processing py roles in HTML
    parser_py_roles = subparsers.add_parser('process-py-roles',
                    help='Process {py} roles in HTML files')
    parser_py_roles.add_argument('html_dir', help='HTML build directory')
    parser_py_roles.add_argument('--language', default='en',
                    help='Language code (it, en, fr, es)')
    parser_py_roles.add_argument('--dry-run', action='store_true',
                    help='Show what would be changed without making changes')
    
    args = parser.parse_args()
    
    if args.command == 'make-parts-clickable':
        make_part_titles_clickable_and_collapsible(args.html_dir, 
                                                   args.dry_run,
                                                   args.language)
        replace_mystnb_toggle_divs(args.html_dir, dry_run=args.dry_run)
        fix_pyscript_dataframe_outputs(args.html_dir, dry_run=args.dry_run)

    elif args.command == 'process-py-roles':
        c = process_html_py_roles(args.html_dir, args.dry_run, args.language)
        print("\nSummary of changes:")
        print(c)
    elif args.command == 'apply-numbering':
        apply_numbering(args.language)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
