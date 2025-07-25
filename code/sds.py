import os
import re
from pathlib import Path

def generate_toc_dictionary(html_root_dir):
    """
    Parse HTML files to extract TOC structure with titles and numbers.
    
    Args:
        html_root_dir (str): Path to the root directory containing HTML files (e.g., 'build/it')
    
    Returns:
        dict: Dictionary mapping titles to (type, number) where:
              - type is either 'Chapter' or 'Section'  
              - number is the chapter/section number as string
    """
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("BeautifulSoup4 is required. Install with: pip install beautifulsoup4")
        return {}
    
    toc_dict = {}
    
    # Find an HTML file to parse the sidebar from (avoid landing page)
    html_files = list(Path(html_root_dir).rglob("*.html"))
    if not html_files:
        print(f"No HTML files found in {html_root_dir}")
        return toc_dict
    
    # Prefer a non-landing page for sidebar parsing
    target_file = None
    for f in html_files:
        if 'landing.html' not in str(f) and '_static' not in str(f):
            target_file = f
            break
    
    if not target_file:
        target_file = html_files[0]
    
    # Use the selected HTML file to get the sidebar structure
    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
    except Exception as e:
        print(f"Error reading HTML file: {e}")
        return toc_dict
    
    # Find the sidebar navigation
    sidebar = soup.find('nav', class_='bd-links')
    if not sidebar:
        print("Sidebar navigation not found")
        return toc_dict
    
    # Initialize counters
    chapter_counter = 0
    appendix_counter = 0
    section_counters = {}  # {chapter_num: section_count}
    appendix_section_counters = {}  # {appendix_letter: section_count}
    
    # Track if we're in the appendices section
    in_appendices = False
    
    # Find all list items in the sidebar
    all_lis = sidebar.find_all('li', recursive=True)
    
    # Track which items we've seen to avoid duplicates (when the same chapter appears in TOC of different pages)
    seen_titles = set()
    
    # First pass: check if we can detect the "Appendici" caption to know when appendices start
    appendices_start_detected = False
    for li in all_lis:
        # Look for caption elements or specific patterns that indicate appendices section
        caption_elements = li.find_all(class_='caption-text')
        for caption in caption_elements:
            if 'Appendici' in caption.get_text(strip=True):
                appendices_start_detected = True
                break
        if appendices_start_detected:
            break
    
    for li in all_lis:
        classes = li.get('class', [])
        link = li.find('a')
        
        # Check if this li contains a caption indicating start of appendices
        caption_elements = li.find_all(class_='caption-text')
        for caption in caption_elements:
            if 'Appendici' in caption.get_text(strip=True):
                in_appendices = True
                continue
        
        if not link:
            continue
            
        # Get the clean title text
        title = link.get_text(strip=True)
        
        # Skip the main title and empty entries
        if not title or 'Superhero Data Science' in title:
            continue
        
        # Skip if we've already processed this title to avoid duplicates
        if title in seen_titles:
            continue
        
        seen_titles.add(title)
        
        # Determine type based on CSS class
        if 'toctree-l1' in classes:
            # Skip part-level "Presentazione" entries - they are introductions, not numbered chapters
            # Also skip the very first "Presentazione" which appears to be a book-level introduction
            if title in ["Presentazione", "Présentation", "Presentation", "Presentación"]:
                continue
            
            # Check if this is an appendix (either we detected appendices section, or title suggests it's an appendix)
            if in_appendices or title in ['References', 'Bibliografia', 'Appendix', 'Appendice']:
                # This is an appendix
                appendix_counter += 1
                appendix_letter = chr(ord('A') + appendix_counter - 1)  # A, B, C, ...
                appendix_section_counters[appendix_letter] = 0
                toc_dict[title] = ('Appendix', appendix_letter)
            else:
                # This is a main chapter
                chapter_counter += 1
                section_counters[chapter_counter] = 0
                toc_dict[title] = ('Chapter', str(chapter_counter))
            
        elif 'toctree-l2' in classes:
            # This is a section
            if in_appendices and appendix_counter > 0:
                # This is an appendix section
                appendix_letter = chr(ord('A') + appendix_counter - 1)
                appendix_section_counters[appendix_letter] += 1
                section_num = f"{appendix_letter}.{appendix_section_counters[appendix_letter]}"
                toc_dict[title] = ('Section', section_num)
            elif chapter_counter > 0:
                # This is a regular chapter section
                section_counters[chapter_counter] += 1
                section_num = f"{chapter_counter}.{section_counters[chapter_counter]}"
                toc_dict[title] = ('Section', section_num)
    
    return toc_dict

def extract_python_roles(source):
    '''Extracts Python code blocks and inline roles from MyST Markdown source.
    
    Args:
        source (str): The MyST Markdown source as a string.
    Returns:
        list: A list of tuples (code_content, class_attr) where:
              - code_content is the Python code
              - class_attr is the CSS class from :class: directive or None
    '''
    import re
    
    # Comprehensive pattern to match different Python code block formats
    # Matches: ```python...``` or ```{python}...``` or ```{code-block} python...``` or {eval-python}`...`
    # For code-block format, capture the full block including options
    pattern = r"(?:```\{code-block\}\s+python\s*([\s\S]*?)```)|(?:```(?:\{?python\}?)\s*([\s\S]*?)```)|(?:\{eval-python\}`([^`]+)`)"
    matches = re.finditer(pattern, source)
    
    result = []
    for match in matches:
        # Group 1 is code-block content, group 2 is python content, group 3 is inline role content
        if match.group(1) is not None:
            # This is a {code-block} python block
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
            result.append((content.strip(), class_attr))
        elif match.group(2) is not None:
            # This is a regular python block
            content = match.group(2)
            result.append((content.strip(), None))
        else:
            # This is an inline eval-python role
            content = match.group(3)
            result.append((content.strip(), None))
    
    return result

def split_code(source):
    '''Splits Python source code into setup code and final statement.
    
    Args:
        source (str): The Python source code as a string.
    Returns:
        tuple: A pair (setup, final) where:
               - setup: string containing all code except the last statement (or all code if final doesn't produce output)
               - final: string containing only the last statement if it produces output, empty string otherwise
               If the source is empty, returns ('', '')
    '''
    import ast
    import astor
    
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
    import ast
    
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

def generate_myst_interactive(setup_code, final_code, cell_number):
    '''Generates MyST Markdown code for interactive Python execution.
    
    Args:
        setup_code (str): The setup code (from split_code output)
        final_code (str): The final expression code (from split_code output)
        cell_number (int): Progressive number for the cell
    Returns:
        str: MyST Markdown code with Python role and HTML divs with PyScript
    '''
    # Combine all code for the Python role
    if setup_code and final_code:
        all_code = f"{setup_code}\n{final_code}"
    elif setup_code:
        all_code = setup_code
    elif final_code:
        all_code = final_code
    else:
        all_code = ""
    
    # Create the Python code block
    python_block = f"```python\n{all_code}\n```"
    
    # Create the HTML raw block with divs and PyScript
    html_content = f'''<div id="splash-{cell_number}" class="splash"></div>
<div id="out-{cell_number}" class="cell-out"></div>
<div id="stdout-{cell_number}" class="cell-stdout"></div>
<div id="stderr-{cell_number}" class="cell-stderr"></div>

<py-script>
{setup_code}
'''
    
    # Add display call if there's a final expression
    if final_code:
        html_content += f'display({final_code}, target="out-{cell_number}")\n'
    
    html_content += '</py-script>'
    
    html_block = f"```{{raw}} html\n{html_content}\n```"
    
    # Combine both blocks
    return f"{python_block}\n\n{html_block}"

def generate_pyscript_setup():
    '''Generates the initial PyScript setup with common imports and utilities.
    
    Returns:
        str: HTML block with PyScript setup that should be included once per document
    '''
    return '''```{raw} html
<py-script>
# Common imports and utilities for interactive Python cells
import sys
from io import StringIO
from js import document, console

# Utility function to hide splash loading indicators
def hide_splash(target_id):
    """Hide the splash loading div in the specified target element"""
    try:
        target_element = document.getElementById(target_id)
        if target_element:
            splash_divs = target_element.getElementsByClassName('splash')
            for splash in splash_divs:
                splash.style.display = 'none'
    except Exception as e:
        console.log(f"Could not hide splash in {target_id}: {e}")

# Import matplotlib once at the beginning and make it available to all cells
try:
    import matplotlib
    import matplotlib.pyplot as plt
    import io
    import base64
    
    # Set matplotlib to use Agg backend to prevent auto-display
    matplotlib.use('Agg')
    
    # Apply custom SDS matplotlib style for consistent figure styling
    import matplotlib.pyplot as plt
    
    # Custom SDS style configuration (matching sds.mplstyle file)
    custom_style = {
        # Axes settings
        'axes.axisbelow': True,
        'axes.facecolor': '#eaf3f5',
        'axes.edgecolor': 'black',
        'axes.linewidth': 1.0,
        'axes.grid': True,
        'axes.grid.axis': 'both',
        'axes.labelsize': 10,
        'axes.labelpad': 10,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.titlesize': 12,
        
        # Boxplots settings
        'boxplot.boxprops.color': 'C0',
        'boxplot.whiskerprops.color': 'C0',
        'boxplot.medianprops.linewidth': 2,
        'boxplot.medianprops.color': 'C1',
        
        # Figure settings
        'figure.dpi': 100,
        'figure.edgecolor': 'none',
        'figure.facecolor': '#eaf3f5',
        'figure.figsize': [4, 3.2],
        
        # Grid settings
        'grid.color': 'lightgray',
        'grid.linestyle': '-',
        'grid.linewidth': 0.5,
        'grid.alpha': 0.7,
        
        # Line settings
        'lines.color': 'C4',
        'lines.linewidth': 2.0,
        'lines.markersize': 8,
        
        # Font settings
        'font.size': 12,
        'font.family': 'sans-serif',
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 11,
        
        # Legend
        'legend.frameon': True,
        'legend.framealpha': 0.8,
        'legend.fancybox': True,
        'legend.shadow': False,
        
        # Mathtext settings
        'mathtext.fontset': 'stix',
        'mathtext.rm': 'stix',
        'mathtext.it': 'stix',
        
        # Patch settings
        'patch.facecolor': 'xkcd:baby blue',
        'patch.edgecolor': 'xkcd:blue gray',
        'patch.force_edgecolor': True,
        
        # Text settings
        'text.usetex': False,
        
        # Savefig settings
        'savefig.dpi': 100,
        'savefig.bbox': 'tight',
        'savefig.facecolor': '#eaf3f5',
        'savefig.edgecolor': 'none',
        
        # Ticks
        'xtick.direction': 'inout',
        'ytick.direction': 'inout',
        'xtick.major.size': 4,
        'ytick.major.size': 4,
        'xtick.minor.size': 2,
        'ytick.minor.size': 2
    }
    
    # Apply the custom style
    plt.rcParams.update(custom_style)
    console.log("Custom SDS matplotlib style applied successfully")
    
    # Make matplotlib available globally
    import builtins
    builtins.plt = plt
    builtins.matplotlib = matplotlib
    builtins.io = io
    builtins.base64 = base64
    
    _matplotlib_available = True
    console.log("Matplotlib loaded successfully")
except ImportError:
    _matplotlib_available = False
    console.log("Matplotlib not available")

# Import pandas and altair globally
try:
    import pandas as pd
    import builtins
    builtins.pd = pd
    console.log("Pandas loaded successfully")
except ImportError:
    console.log("Pandas not available")

# Install and import altair
console.log("Installing altair...")
try:
    import micropip
    await micropip.install("altair")
    console.log("Altair installed via micropip")
except Exception as e:
    console.log(f"Error installing altair via micropip: {e}")

try:
    import altair as alt
    import builtins
    builtins.alt = alt
    console.log("Altair imported and made available globally")
except ImportError as e:
    console.log(f"Failed to import altair: {e}")
except Exception as e:
    console.log(f"Error with altair: {e}")

def display(obj, target=None, append=True):
    """Display an object in the specified target div."""
    if target:
        element = document.getElementById(target)
        if element:
            if append:
                element.innerHTML += str(obj)
            else:
                element.innerHTML = str(obj)
    else:
        console.log(str(obj))

def Element(element_id):
    """Helper class to write to DOM elements."""
    class ElementWriter:
        def __init__(self, id):
            self.id = id
            
        def write(self, content):
            element = document.getElementById(self.id)
            if element:
                element.innerHTML = str(content)
                
        def append(self, content):
            element = document.getElementById(self.id)
            if element:
                element.innerHTML += str(content)
                
        def clear(self):
            element = document.getElementById(self.id)
            if element:
                element.innerHTML = ""
    
    return ElementWriter(element_id)

# Make functions available globally (PyScript/Pyodide compatible)
import builtins
builtins.display = display
builtins.Element = Element
builtins._matplotlib_available = _matplotlib_available

console.log("PyScript utilities loaded successfully")
</py-script>
```'''

def get_toggle_labels(language='en'):
    '''Get localized labels for toggle buttons.
    
    Args:
        language (str): The language code (default: 'en')
    Returns:
        dict: Dictionary with 'show' and 'hide' keys for the labels
    '''
    labels = {
        'en': {
            'show': 'Show code',
            'hide': 'Hide code'
        },
        'it': {
            'show': 'Mostra codice',
            'hide': 'Nascondi codice'
        },
        'fr': {
            'show': 'Afficher le code',
            'hide': 'Masquer le code'
        },
        'es': {
            'show': 'Mostrar código',
            'hide': 'Ocultar código'
        }
    }
    
    return labels.get(language, labels['en'])

def process_myst_document(myst_content, include_setup=True, language='en'):
    '''Processes a MyST Markdown document and adds interactive HTML blocks after each Python code block.
    
    Args:
        myst_content (str): The MyST Markdown document content as a string
        include_setup (bool): Whether to include the initial PyScript setup (default: True)
        language (str): The language code for localization (default: 'en')
    Returns:
        str: The processed document with interactive HTML blocks added after Python code blocks
    '''
    import re
    
    # Extract all Python code blocks from the document
    python_codes = extract_python_roles(myst_content)
    
    if not python_codes:
        return myst_content
    
    # Split the document by Python code blocks to reconstruct it
    result_parts = []
    pyscript_blocks = []  # Collect all PyScript blocks to add at the end
    all_imports = set()  # Collect all imported packages
    current_pos = 0
    cell_number = 1
    
    # Pattern to find Python code blocks and their positions
    # Matches: ```python...``` or ```{python}...``` or ```{code-block} python...``` or {eval-python}`...`
    # For code-block format, capture the full block including options
    pattern = r"(?:```\{code-block\}\s+python\s*([\s\S]*?)```)|(?:```(?:\{?python\}?)\s*([\s\S]*?)```)|(?:\{eval-python\}`([^`]+)`)"
    
    python_code_index = 0
    for match in re.finditer(pattern, myst_content):
        # Check if this code block is already inside a toggle wrapper
        context_before = myst_content[max(0, match.start() - 500):match.start()]
        context_after = myst_content[match.end():min(len(myst_content), match.end() + 500)]
        
        # Skip if this code block is already inside a toggle wrapper
        if ('toggle-code-wrapper' in context_before and 
            'toggle-code-content' in context_before and 
            '</div>' in context_after):
            # This code block is already wrapped, skip it
            # Update current_pos to after this match
            current_pos = match.end()
            continue
        
        # Add content before this Python block
        result_parts.append(myst_content[current_pos:match.start()])
        
        # Get the Python code content and class from our extracted data
        if python_code_index < len(python_codes):
            python_code, class_attr = python_codes[python_code_index]
        else:
            # Fallback to regex extraction if index is out of bounds
            if match.group(1) is not None:
                # This is a {code-block} python block
                python_code = match.group(1)
                class_attr = None
                # Handle :class: directive extraction
                if python_code and ':class:' in python_code:
                    class_match = re.search(r':class:\s*([^\n]+)', python_code)
                    if class_match:
                        class_attr = class_match.group(1).strip()
                        python_code = re.sub(r':class:\s*[^\n]+\n?', '', python_code)
            elif match.group(2) is not None:
                # This is a regular python block
                python_code = match.group(2)
                class_attr = None
            else:
                # This is an inline eval-python role
                python_code = match.group(3)
                class_attr = None
        
        # Add the original Python block, with toggle wrapper if needed
        original_block = match.group(0)
        
        if class_attr and 'toggle-code' in class_attr:
            # Remove the toggle-code class from the original block to prevent double wrapping
            cleaned_block = original_block.replace(':class: toggle-code', '')
            # Remove any empty class attributes that might be left
            cleaned_block = re.sub(r':class:\s*\n', '', cleaned_block)
            cleaned_block = re.sub(r':class:\s*$', '', cleaned_block, flags=re.MULTILINE)
            
            # Get localized labels
            labels = get_toggle_labels(language)
            
            # Wrap the code block in a toggle wrapper
            result_parts.append(f'''
```{{raw}} html
<div class="toggle-code-wrapper">
    <button class="toggle-code-button"><span class="triangle">▶</span><span class="button-text"> {labels['show']}</span></button>
    <div class="toggle-code-content">
```

{cleaned_block}

```{{raw}} html
    </div>
</div>
```
''')
        else:
            result_parts.append(original_block)
        
        python_code_index += 1
        python_code = python_code.strip()
        
        # Extract imports from this code block
        imports = _extract_imports(python_code)
        all_imports.update(imports)
        
        # Split the Python code into setup and final parts
        setup_code, final_code = split_code(python_code)
        
        # Create only the HTML divs (no PyScript yet)
        html_divs = f'''
```{{raw}} html
<div id="splash-{cell_number}" class="splash"></div>
<div id="out-{cell_number}" class="cell-out"></div>
<div id="stdout-{cell_number}" class="cell-stdout"></div>
<div id="stderr-{cell_number}" class="cell-stderr"></div>
<div id="graph-{cell_number}" class="cell-graph no-mathjax"></div>
```'''
        
        result_parts.append(html_divs)
        
        # Check if matplotlib is used in this cell
        uses_matplotlib = _uses_matplotlib(python_code)
        
        # Create the PyScript block to be added later
        # Add class attribute if present, but NOT for toggle-code (that should only affect visible code)
        py_script_class = ""
        if class_attr and 'toggle-code' not in class_attr:
            py_script_class = f' class="{class_attr}"'
        
        pyscript_content = f'''
<py-script{py_script_class}>
# Cell {cell_number}: Execute Python code

# Ensure heroes.csv is available in data/ directory before executing any code
if not hasattr(__builtins__, '_heroes_csv_ready') or not getattr(__builtins__, '_heroes_csv_ready', False):
    # Import required modules for file download and filesystem operations
    from js import fetch
    import asyncio
    import os
    
    async def _ensure_heroes_csv():
        """Ensure heroes.csv is available in data/ directory, always download fresh version"""
        try:
            # Create data directory if it doesn't exist
            os.makedirs("data", exist_ok=True)
            
            console.log("Loading heroes.csv dataset into data/ directory...")
            
            # Always fetch fresh CSV content from GitHub to ensure latest version
            response = await fetch("https://raw.githubusercontent.com/dariomalchiodi/sds/main/data/heroes.csv")
            
            if response.ok:
                csv_content = await response.text()
                
                # Write to Pyodide's virtual filesystem in data/ directory
                with open("data/heroes.csv", "w") as f:
                    f.write(csv_content)
                
                console.log("Heroes dataset loaded successfully to data/heroes.csv")
                return True
            else:
                console.log(f"Failed to load heroes.csv: HTTP {{response.status}}")
                return False
                
        except Exception as e:
            console.log(f"Error loading heroes.csv: {{e}}")
            return False
    
    # Load the file and wait for completion
    await _ensure_heroes_csv()
    console.log("Heroes.csv is now available for pd.read_csv('data/heroes.csv')")
    
    # Set global flag to avoid repeated downloads
    import builtins
    builtins._heroes_csv_ready = True

# Ensure altair is available in this cell
if not hasattr(__builtins__, 'alt') or not getattr(__builtins__, 'alt', None):
    console.log("Installing altair in current cell...")
    try:
        import micropip
        await micropip.install("altair")
        import altair as alt
        import builtins
        builtins.alt = alt
        console.log("Altair installed and available in current cell")
    except Exception as altair_error:
        console.log(f"Error installing altair in current cell: {{altair_error}}")

# Load previously stored variables from builtins (for variable persistence across cells)
import builtins
builtin_attrs = list(dir(builtins))  # Create a list to avoid "dictionary changed size during iteration"
for attr_name in builtin_attrs:
    if not attr_name.startswith('_') and attr_name not in ['display', 'Element', 'plt', 'matplotlib', 'io', 'base64', 'pd', 'alt']:
        try:
            attr_value = getattr(builtins, attr_name)
            # Only load if it's not a built-in function/class
            if not callable(attr_value) or hasattr(attr_value, '__module__'):
                globals()[attr_name] = attr_value
                # Debug: log important variables being loaded
                if attr_name in ['heroes', 'source', 'data', 'chart', 'filter']:
                    console.log(f"Loading variable {{attr_name}} from builtins")
        except:
            pass  # Skip if there's any issue loading a variable

# Capture stdout and stderr
old_stdout = sys.stdout
old_stderr = sys.stderr
captured_stdout = StringIO()
captured_stderr = StringIO()

try:
    sys.stdout = captured_stdout
    sys.stderr = captured_stderr
    
    # Execute setup code
{_indent_code(setup_code, "    ")}'''
        
        if final_code:
            pyscript_content += f'''
    
    # Execute final code and capture result
    result = None'''
            
            # Only include matplotlib handling if matplotlib is actually used
            if uses_matplotlib:
                pyscript_content += f'''
    
    # Handle matplotlib plots (before executing final code that might display)
    matplotlib_handled = False
    if _matplotlib_available:
        # Check if there are any figures before final execution
        if plt.get_fignums():
            # Get the current figure
            fig = plt.gcf()
            
            # Save plot to base64 string
            img_buffer = io.BytesIO()
            fig.savefig(img_buffer, format='png', bbox_inches='tight', dpi=100)
            img_buffer.seek(0)
            img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
            img_buffer.close()
            
            # Display the image in the graph div
            img_html = '<div class="no-mathjax"><img src="data:image/png;base64,' + img_base64 + '" style="max-width: 100%; height: auto;" /></div>'
            Element("graph-{cell_number}").write(img_html)
            
            # Clear the figure to prevent it from being shown elsewhere
            plt.close(fig)
            matplotlib_handled = True
    
    # Execute final code only if it's not plt.show() and matplotlib wasn't handled
    if not matplotlib_handled:
        try:
            result = {final_code}
        except Exception as e:
            sys.stderr.write(f"Error executing code: {{str(e)}}\\n")
            import traceback
            traceback.print_exc()
            result = None'''
            else:
                pyscript_content += f'''
    try:
        result = {final_code}
    except Exception as e:
        sys.stderr.write(f"Error executing code: {{str(e)}}\\n")
        import traceback
        traceback.print_exc()
        result = None'''
        else:
            # Only include matplotlib handling if matplotlib is actually used (setup-only case)
            if uses_matplotlib:
                pyscript_content += '''
    
    # Handle matplotlib plots (after setup execution)
    if _matplotlib_available:
        # Check if there are any figures
        if plt.get_fignums():
            # Get the current figure
            fig = plt.gcf()
            
            # Save plot to base64 string
            img_buffer = io.BytesIO()
            fig.savefig(img_buffer, format='png', bbox_inches='tight', dpi=100)
            img_buffer.seek(0)
            img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
            img_buffer.close()
            
            # Display the image in the graph div
            img_html = '<div class="no-mathjax"><img src="data:image/png;base64,' + img_base64 + '" style="max-width: 100%; height: auto;" /></div>'
            Element("graph-{cell_number}").write(img_html)
            
            # Clear the figure to prevent it from being shown elsewhere
            plt.close(fig)
'''
        
        pyscript_content += f'''
finally:
    # Restore stdout and stderr
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    
    # Store variables in builtins for persistence across cells
    import builtins
    local_vars = dict(locals())  # Create a copy to avoid iteration issues
    for var_name, var_value in local_vars.items():
        if not var_name.startswith('_') and var_name not in ['sys', 'StringIO', 'console', 'document', 'old_stdout', 'old_stderr', 'captured_stdout', 'captured_stderr', 'builtins', 'local_vars']:
            try:
                setattr(builtins, var_name, var_value)
                # Debug: log important variables being saved
                if var_name in ['heroes', 'source', 'data', 'chart', 'filter']:
                    console.log(f"Saving variable {{var_name}} to builtins")
            except:
                pass  # Skip if there's any issue storing a variable
    
    # Display outputs
    stdout_content = captured_stdout.getvalue()
    stderr_content = captured_stderr.getvalue()
    
    # Hide the splash (loading) div
    splash_element = document.getElementById("splash-{cell_number}")
    if splash_element:
        splash_element.style.display = "none"
    
    if stdout_content:
        Element("stdout-{cell_number}").write(stdout_content)
    if stderr_content:
        Element("stderr-{cell_number}").write(stderr_content)'''
        
        if final_code:
            pyscript_content += f'''
    if result is not None:
        # Check if result is an Altair chart (look for Chart class or specific methods)
        result_type = str(type(result))
        console.log(f"Result type: {{result_type}}")
        
        # Check if it's an Altair chart by looking for specific Altair characteristics
        is_altair = ('altair' in result_type.lower() or 
                    'chart' in result_type.lower() or 
                    hasattr(result, 'to_json') and hasattr(result, 'data'))
        
        if is_altair:
            # This is likely an Altair chart - try different rendering methods
            try:
                console.log("Attempting to render Altair chart")
                
                # Debug: check available methods
                methods = [attr for attr in dir(result) if not attr.startswith('_')]
                console.log(f"Available methods: {{methods[:15]}}")  # Show first 15
                
                # Try multiple rendering approaches
                rendered = False
                
                # Method 1: Try to_json() and use Vega-Embed directly (most reliable)
                if hasattr(result, 'to_json') and not rendered:
                    try:
                        console.log("Trying to_json() method with Vega-Embed")
                        chart_spec = result.to_json()
                        console.log("Chart spec length:", len(chart_spec))
                        
                        # Parse the JSON spec
                        import json
                        spec_dict = json.loads(chart_spec)
                        console.log("Parsed spec successfully")
                        
                        # Create a unique div for this chart
                        chart_div_id = "altair-chart-{cell_number}"
                        chart_html = '<div id="' + chart_div_id + '" style="width: 100%; height: 400px;"></div>'
                        Element("graph-{cell_number}").write(chart_html)
                        
                        # Use Vega-Embed to render the chart - create JS code safely
                        # Build JavaScript code line by line to avoid conflicts
                        js_lines = []
                        js_lines.append("setTimeout(function() " + "{{")
                        js_lines.append("try " + "{{")
                        js_lines.append("const spec = " + chart_spec + ";")
                        js_lines.append("vegaEmbed('#" + chart_div_id + "', spec).then(function(result) " + "{{")
                        js_lines.append("console.log('Chart rendered successfully');")
                        js_lines.append("}}).catch(function(error) " + "{{")
                        js_lines.append("console.error('Vega-Embed error:', error);")
                        js_lines.append("}});")
                        js_lines.append("}} catch(e) " + "{{")
                        js_lines.append("console.error('Error rendering chart:', e);")
                        js_lines.append("}}")
                        js_lines.append("}}, 100);")
                        
                        js_code = " ".join(js_lines)
                        
                        # Execute the JavaScript code
                        from js import eval as js_eval
                        js_eval(js_code)
                        
                        rendered = True
                        console.log("Successfully rendered using to_json() and Vega-Embed")
                    except Exception as e:
                        console.log("to_json() with Vega-Embed failed:", str(e))
                
                # Method 2: Try to_html() - fallback approach
                if hasattr(result, 'to_html') and not rendered:
                    try:
                        console.log("Trying to_html() method - fallback approach")
                        html_repr = result.to_html()
                        console.log(f"HTML repr length: {{len(html_repr)}}")
                        if len(html_repr) > 100:  # Only use if we got substantial content
                            console.log("Writing HTML directly to graph container")
                            
                            # Simply write the HTML content directly without trying to execute scripts
                            # The script execution approach is too risky in this context
                            chart_container = '<div id="altair-fallback-{cell_number}" style="width: 100%; height: 400px; border: 1px solid #ddd; padding: 10px;">' + html_repr + '</div>'
                            Element("graph-{cell_number}").write(chart_container)
                            
                            rendered = True
                            console.log("Successfully rendered using to_html()")
                    except Exception as e:
                        console.log(f"to_html() failed: {{e}}")
                
                # Method 2: Try _repr_html_() method
                if hasattr(result, '_repr_html_') and not rendered:
                    try:
                        console.log("Trying _repr_html_() method")
                        html_repr = result._repr_html_()
                        console.log(f"HTML repr length: {{len(html_repr)}}")
                        if len(html_repr) > 100:  # Only use if we got substantial content
                            Element("graph-{cell_number}").write(html_repr)
                            rendered = True
                            console.log("Successfully rendered using _repr_html_()")
                    except Exception as e:
                        console.log(f"_repr_html_() failed: {{e}}")
                
                # Method 3: Try show() method
                if hasattr(result, 'show') and not rendered:
                    try:
                        console.log("Trying show() method")
                        result.show()
                        rendered = True
                        console.log("Successfully called show() method")
                    except Exception as e:
                        console.log(f"show() failed: {{e}}")
                
                # Method 4: Fallback - show chart spec as JSON
                if not rendered:
                    console.log("Using fallback - showing as JSON")
                    if hasattr(result, 'to_json'):
                        try:
                            chart_spec = result.to_json()
                            console.log(f"Chart spec length: {{len(chart_spec)}}")
                            Element("out-{cell_number}").write(f"Chart spec: {{chart_spec[:500]}}...")
                        except Exception as e:
                            console.log(f"to_json() failed: {{e}}")
                            Element("out-{cell_number}").write(f"Altair chart (methods: {{methods[:5]}}): {{str(result)[:200]}}")
                    else:
                        Element("out-{cell_number}").write(f"Altair chart (methods: {{methods[:5]}}): {{str(result)[:200]}}")
                
            except Exception as e:
                console.log(f"Error rendering Altair chart: {{e}}")
                Element("out-{cell_number}").write(f"Error rendering chart: {{str(e)}}")
        # Check if result is a pandas DataFrame and render as HTML table
        elif hasattr(result, 'to_html') and callable(getattr(result, 'to_html')) and hasattr(result, 'index'):
            # This is likely a pandas DataFrame - display as HTML table in graph div
            html_table = result.to_html(
                classes='table table-hover table-bordered table-sm',
                table_id=f'table-{cell_number}',
                border=0,
                escape=False
            )
            Element("graph-{cell_number}").write(html_table)
        else:
            # For other types, convert to string and display in out div
            console.log(f"Other result type: {{result_type}}")
            Element("out-{cell_number}").write(str(result))'''
        
        pyscript_content += '''
</py-script>'''
        
        pyscript_blocks.append(pyscript_content)
        
        current_pos = match.end()
        cell_number += 1
    
    # Add any remaining content after the last Python block
    result_parts.append(myst_content[current_pos:])
    
    # Add all PyScript blocks at the end
    if pyscript_blocks:
        result_parts.append('\n\n```{raw} html\n')
        
        # Add setup first if requested
        if include_setup:
            setup_content = generate_pyscript_setup()
            # Extract just the PyScript content from the setup
            setup_script = setup_content.split('<py-script>')[1].split('</py-script>')[0]
            result_parts.append(f'<py-script>{setup_script}</py-script>\n')
        
        # Add all collected PyScript blocks
        for pyscript_block in pyscript_blocks:
            result_parts.append(pyscript_block)
            result_parts.append('\n')
        
        # Add toggle initialization script at the end if any toggle-code blocks exist
        has_toggle_code = any('class="toggle-code"' in block for block in pyscript_blocks)
        if has_toggle_code:
            result_parts.append('''
<script>
// Initialize toggle code functionality after PyScript execution
setTimeout(function() {
    if (typeof window.initializeToggleCode === 'function') {
        window.initializeToggleCode();
    }
}, 100);
</script>
''')
        
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
        return ""
    
    lines = code.split('\n')
    indented_lines = [indent + line if line.strip() else line for line in lines]
    return '\n'.join(indented_lines)

def process_myst_file(file_path, include_setup=True):
    '''Processes a MyST Markdown file and replaces its contents with interactive HTML blocks.
    
    Creates a backup of the original file before processing.
    
    Args:
        file_path (str): Path to the MyST Markdown file to process
        include_setup (bool): Whether to include the initial PyScript setup (default: True)
    Returns:
        str: Path to the backup file that was created
    Raises:
        FileNotFoundError: If the input file doesn't exist
        IOError: If there are issues reading/writing files
    '''
    import os
    import shutil
    from pathlib import Path
    
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
        processed_content = process_myst_document(original_content, include_setup=include_setup, language=language)
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
    import ast
    import re
    
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
    
    # Filter out built-in modules and common standard library modules that don't need to be declared
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
        'atexit', 'traceback', 'gc', 'weakref', 'builtins'
    }
    
    # Return only packages that are not built-in
    return packages - builtin_modules

import re


def _uses_matplotlib(code):
    """Check if code uses matplotlib or pyplot functionality.
    
    Args:
        code (str): Python source code
        
    Returns:
        bool: True if matplotlib is used, False otherwise
    """
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

def replace_crossref_links(html_root_dir, toc_dict=None, dry_run=False, language='it'):
    """
    Recursively process HTML files and replace cross-reference link texts with correct type and number.
    
    Args:
        html_root_dir (str): Path to the root directory containing HTML files (e.g., 'build/it')
        toc_dict (dict): Dictionary mapping titles to (type, number). If None, will generate automatically.
        dry_run (bool): If True, only analyze and return what would be changed without modifying files
        language (str): Language code ('it' or 'en') for appropriate translations
    
    Returns:
        dict: Summary of changes made or that would be made
    """
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("BeautifulSoup4 is required. Install with: pip install beautifulsoup4")
        return {}
    
    # Generate TOC dictionary if not provided
    if toc_dict is None:
        toc_dict = generate_toc_dictionary(html_root_dir)
    
    if not toc_dict:
        print("No TOC dictionary available")
        return {}
    
    # Type mapping for different languages
    if language == 'it':
        type_mapping = {
            'Chapter': 'Capitolo',
            'Section': 'Paragrafo', 
            'Appendix': 'Appendice'
        }
    elif language == 'fr':
        type_mapping = {
            'Chapter': 'Chapitre',
            'Section': 'Section', 
            'Appendix': 'Annexe'
        }
    elif language == 'es':
        type_mapping = {
            'Chapter': 'Capítulo',
            'Section': 'Sección', 
            'Appendix': 'Apéndice'
        }
    else:  # English default
        type_mapping = {
            'Chapter': 'Chapter',
            'Section': 'Section', 
            'Appendix': 'Appendix'
        }
    
    changes_summary = {
        'files_processed': 0,
        'files_modified': 0,
        'total_replacements': 0,
        'replacements_by_file': {},
        'errors': []
    }
    
    # Find all HTML files
    html_files = list(Path(html_root_dir).rglob("*.html"))
    
    for html_file in html_files:
        # Skip certain files that shouldn't be modified
        if any(skip in str(html_file) for skip in ['_static', 'genindex', 'search']):
            continue
            
        changes_summary['files_processed'] += 1
        file_replacements = []
        
        try:
            # Read and parse the HTML file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            soup = BeautifulSoup(content, 'html.parser')
            content_modified = False
            
            # Find all internal links that could be cross-references
            # Look for links with class="reference internal" but exclude sidebar navigation
            internal_links = soup.find_all('a', class_='reference internal')
            
            for link in internal_links:
                # Skip links that are in the sidebar navigation
                # Check if the link is inside a navigation element or sidebar
                parent_nav = link.find_parent('nav')
                parent_sidebar = link.find_parent(class_=['bd-sidebar', 'bd-sidebar-primary', 'bd-sidebar-secondary'])
                parent_toc = link.find_parent(class_=['toctree-wrapper', 'toctree', 'bd-toc'])
                
                # Also check for parent elements with 'sidebar' in their class
                parent_any_sidebar = link.find_parent(class_=lambda x: x and 'sidebar' in x)
                
                if parent_nav or parent_sidebar or parent_toc or parent_any_sidebar:
                    continue
                    
                # Additional check: only process links that are in the main content area
                main_content = link.find_parent(class_=['bd-main', 'bd-article'])
                if not main_content:
                    continue
                link_text = link.get_text(strip=True)
                
                # Skip if this link already has a number pattern (to avoid double-processing)
                if language == 'it':
                    # Check for new format: "Capitolo X", "Paragrafo X.Y", "Appendice A"
                    if re.match(r'^(Capitolo|Paragrafo|Appendice)\s+[\dA-Z.]+$', link_text):
                        continue
                elif language == 'fr':
                    if re.match(r'^(Chapitre|Section|Annexe)\s+[\dA-Z.]+$', link_text):
                        continue
                elif language == 'es':
                    if re.match(r'^(Capítulo|Sección|Apéndice)\s+[\dA-Z.]+$', link_text):
                        continue
                else:  # English
                    if re.match(r'^(Chapter|Section|Appendix)\s+[\dA-Z.]+$', link_text):
                        continue
                
                # Check if the link text matches any title in our TOC dictionary
                # First try direct match
                if link_text in toc_dict:
                    type_name, number = toc_dict[link_text]
                    italian_type = type_mapping.get(type_name, type_name)
                    
                    # Format the link text according to type
                    if type_name == 'Chapter':
                        new_text = f"{italian_type} {number}"
                    elif type_name == 'Section':
                        new_text = f"{italian_type} {number}"  # Include "Paragrafo" for sections
                    else:  # Appendix
                        new_text = f"{italian_type} {number}"
                    
                    file_replacements.append({
                        'original': link_text,
                        'new': new_text,
                        'href': link.get('href', ''),
                        'type': type_name,
                        'number': number
                    })
                    
                    if not dry_run:
                        # Replace the link text and add title attribute for hover tooltip
                        link.string = new_text
                        link['title'] = link_text  # Show original title on hover
                        content_modified = True
                        
                # If direct match failed, try using the title attribute (for already numbered links)
                elif link.get('title'):
                    title_text = link.get('title')
                    if title_text in toc_dict:
                        type_name, number = toc_dict[title_text]
                        italian_type = type_mapping.get(type_name, type_name)
                        
                        # Format the link text according to type
                        if type_name == 'Chapter':
                            new_text = f"{italian_type} {number}"
                        elif type_name == 'Section':
                            new_text = f"{italian_type} {number}"  # Include "Paragrafo" for sections
                        else:  # Appendix
                            new_text = f"{italian_type} {number}"
                        
                        file_replacements.append({
                            'original': link_text,
                            'new': new_text,
                            'href': link.get('href', ''),
                            'type': type_name,
                            'number': number
                        })
                        
                        if not dry_run:
                            # Replace the link text and keep title attribute for hover tooltip
                            link.string = new_text
                            # Title attribute already exists with the original title
                            content_modified = True
            
            # Add numbering to main page titles (h1 elements)
            # Only process h1 elements that are in the main content area
            main_content_area = soup.find(class_=['bd-main', 'bd-article'])
            if main_content_area:
                main_titles = main_content_area.find_all('h1')
            else:
                main_titles = soup.find_all('h1')
                
            for h1 in main_titles:
                # Extract clean text, removing anchor links and extra whitespace
                h1_text_elements = []
                for item in h1.contents:
                    if hasattr(item, 'name') and item.name == 'a':
                        continue  # Skip anchor links
                    else:
                        h1_text_elements.append(str(item))
                h1_text = ''.join(h1_text_elements).strip()
                
                # Skip if already numbered (check new format)
                if language == 'it':
                    # Check for new format: "Capitolo X.", "Appendice A.", or just numbers like "3.1."
                    if (re.match(r'^(Capitolo|Appendice)\s+[\dA-Z]+\.', h1_text) or 
                        re.match(r'^\d+(\.\d+)*\.', h1_text)):
                        continue
                elif language == 'fr':
                    if (re.match(r'^(Chapitre|Annexe)\s+[\dA-Z]+\.', h1_text) or 
                        re.match(r'^\d+(\.\d+)*\.', h1_text)):
                        continue
                elif language == 'es':
                    if (re.match(r'^(Capítulo|Apéndice)\s+[\dA-Z]+\.', h1_text) or 
                        re.match(r'^\d+(\.\d+)*\.', h1_text)):
                        continue
                else:  # English
                    if (re.match(r'^(Chapter|Appendix)\s+[\dA-Z]+\.', h1_text) or 
                        re.match(r'^\d+(\.\d+)*\.', h1_text)):
                        continue
                
                # Extract original title from already numbered titles
                original_title = h1_text
                
                # If already numbered, extract the original title
                if language == 'it':
                    # Check for old format: "Capitolo X: Title" or "Paragrafo X.Y: Title"
                    colon_match = re.match(r'^(Capitolo|Paragrafo|Appendice)\s+[\dA-Z.]+:\s*(.+)$', h1_text)
                    if colon_match:
                        original_title = colon_match.group(2)
                    # Check for new format: "Capitolo X. Title" or "X.Y. Title"
                    elif re.match(r'^(Capitolo|Appendice)\s+[\dA-Z]+\.\s*(.+)$', h1_text):
                        dot_match = re.match(r'^(Capitolo|Appendice)\s+[\dA-Z]+\.\s*(.+)$', h1_text)
                        original_title = dot_match.group(2)
                    elif re.match(r'^\d+(\.\d+)*\.\s*(.+)$', h1_text):
                        num_match = re.match(r'^\d+(\.\d+)*\.\s*(.+)$', h1_text)
                        original_title = num_match.group(2)
                
                # Check if this title (original or extracted) exists in our TOC dictionary
                if original_title in toc_dict:
                    type_name, number = toc_dict[original_title]
                    italian_type = type_mapping.get(type_name, type_name)
                    
                    # Format the title according to type
                    if type_name == 'Chapter':
                        new_title = f"{italian_type} {number}. {original_title}"  # Point for chapters
                    elif type_name == 'Section':
                        new_title = f"{number}. {original_title}"  # Just number for sections
                    else:  # Appendix
                        new_title = f"{italian_type} {number}. {original_title}"  # Point for appendices
                    
                    if not dry_run:
                        # Replace the text content while preserving the anchor link
                        text_replaced = False
                        for i, content in enumerate(h1.contents):
                            if hasattr(content, 'name') and content.name == 'a':
                                continue  # Skip anchor links
                            elif hasattr(content, 'replace'):
                                # This is a NavigableString
                                content.replace_with(new_title)
                                content_modified = True
                                text_replaced = True
                                break
                            elif isinstance(content, str):
                                h1.contents[i] = new_title
                                content_modified = True
                                text_replaced = True
                                break
                        
                        # If no text content was found, add the numbered title at the beginning
                        if not text_replaced:
                            h1.insert(0, new_title)
                            content_modified = True
            
            # Record the replacements for this file and write if modified
            if file_replacements:
                changes_summary['replacements_by_file'][str(html_file)] = file_replacements
                changes_summary['total_replacements'] += len(file_replacements)
            
            if content_modified:
                changes_summary['files_modified'] += 1
                
                if not dry_run:
                    # Write the modified content back to the file
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                        
        except Exception as e:
            error_msg = f"Error processing {html_file}: {e}"
            changes_summary['errors'].append(error_msg)
            print(error_msg)
    
    return changes_summary


