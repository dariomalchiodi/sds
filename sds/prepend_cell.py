# prepend_cell.py
import re

# The code to run at the top of every notebook
_SETUP_CODE = """\
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('sds')
mpl.rcParams.update({
   'figure.dpi': 150,
   'mathtext.fontset': 'cm',
   'figure.figsize': (3, 2),
   'font.size': 7,
   'xtick.labelsize': 6,
   'ytick.labelsize': 6,
   'legend.fontsize': 7,
   'axes.labelsize': 7,
   'axes.labelpad': 2,
   'axes.titlesize': 8
})
"""

# Wrap it in a hidden myst-nb code cell
_HIDDEN_CELL = f"""\
```{{code-cell}} python
:tags: [remove-cell]

{_SETUP_CODE}
```

"""

# Matches an optional YAML frontmatter block at the start of the file
_FRONTMATTER_RE = re.compile(r'^---\n.*?\n---\n', re.DOTALL)


def _source_read_handler(app, docname, source):
    src = source[0]

    # Only touch files that actually contain code cells
    if '{code-cell}' not in src:
        return

    match = _FRONTMATTER_RE.match(src)
    if match:
        # Insert after the frontmatter block
        insert_at = match.end()
        source[0] = src[:insert_at] + '\n' + _HIDDEN_CELL + src[insert_at:]
    else:
        source[0] = _HIDDEN_CELL + src


def setup(app):
    app.connect('source-read', _source_read_handler)
    return {'version': '0.1', 'parallel_read_safe': True}