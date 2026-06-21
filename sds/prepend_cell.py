# prepend_cell.py
import os
import re

_STYLE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sds.mplstyle'))

# The code to run at the top of every notebook
_SETUP_CODE = """\
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use(r'__SDS_STYLE_PATH__')
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

from matplotlib.axes import Axes as _Axes
from matplotlib.axis import YAxis as _YAxis, XAxis as _XAxis
from matplotlib.figure import Figure as _Figure

_orig_ylabel_update = _YAxis._update_label_position
def _sds_ylabel_update(self, renderer):
    if not getattr(self.axes, '_sds_ylabel_at_top', True):
        _orig_ylabel_update(self, renderer)
    else:
        self.label.set_clip_on(False)
        self.label.set_transform(self.axes.transAxes)
        self.label.set_position((0.02, 1.06))
        self.label.set_ha('left')
        self.label.set_va('bottom')
_YAxis._update_label_position = _sds_ylabel_update

_orig_xlabel_update = _XAxis._update_label_position
def _sds_xlabel_update(self, renderer):
    if not getattr(self.axes, '_sds_xlabel_at_end', True):
        _orig_xlabel_update(self, renderer)
    else:
        self.label.set_clip_on(False)
        self.label.set_transform(self.axes.transAxes)
        self.label.set_position((1.06, 0))
        self.label.set_ha('left')
        self.label.set_va('center')
_XAxis._update_label_position = _sds_xlabel_update

_orig_set_ylabel = _Axes.set_ylabel
def _sds_set_ylabel(self, ylabel, fontdict=None, labelpad=None, *, loc=None, **kwargs):
    if loc == 'default':
        self._sds_ylabel_at_top = False
        return _orig_set_ylabel(self, ylabel, fontdict, labelpad, loc=None, **kwargs)
    self._sds_ylabel_at_top = True
    if labelpad is None:
        labelpad = 1
    kwargs.setdefault('rotation', 0)
    kwargs.setdefault('fontsize', mpl.rcParams['axes.labelsize'] + 1)
    ha = kwargs.pop('ha', kwargs.pop('horizontalalignment', 'left'))
    va = kwargs.pop('va', kwargs.pop('verticalalignment', 'bottom'))
    result = _orig_set_ylabel(self, ylabel, fontdict, labelpad, loc=loc, **kwargs)
    self.yaxis.label.set_ha(ha)
    self.yaxis.label.set_va(va)
    return result
_Axes.set_ylabel = _sds_set_ylabel

_orig_set_xlabel = _Axes.set_xlabel
def _sds_set_xlabel(self, xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs):
    if loc == 'default':
        self._sds_xlabel_at_end = False
        loc = 'center'
        ha = kwargs.pop('ha', kwargs.pop('horizontalalignment', 'center'))
        va = kwargs.pop('va', kwargs.pop('verticalalignment', 'top'))
    else:
        self._sds_xlabel_at_end = True
        if loc is None:
            loc = 'right'
        if labelpad is None:
            labelpad = 1
        kwargs.setdefault('fontsize', mpl.rcParams['axes.labelsize'] + 1)
        ha = kwargs.pop('ha', kwargs.pop('horizontalalignment', 'left'))
        va = kwargs.pop('va', kwargs.pop('verticalalignment', 'center'))
    result = _orig_set_xlabel(self, xlabel, fontdict, labelpad, loc=loc, **kwargs)
    self.xaxis.label.set_ha(ha)
    self.xaxis.label.set_va(va)
    return result
_Axes.set_xlabel = _sds_set_xlabel

def _sds_setup_arrow_axes(ax):
    if getattr(ax, '_sds_arrows_added', False):
        return
    ax._sds_arrows_added = True
    c = mpl.rcParams.get('axes.edgecolor', 'black')
    lw = mpl.rcParams.get('axes.linewidth', 1.0)
    kw = dict(xycoords='axes fraction', textcoords='axes fraction',
              arrowprops=dict(arrowstyle='->', color=c, lw=lw, mutation_scale=8),
              annotation_clip=False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ann_x = ax.annotate('', xy=(1.04, 0), xytext=(-0.02, 0), **kw)
    ann_y = ax.annotate('', xy=(0, 1.04), xytext=(0, -0.02), **kw)
    ax._sds_arrow_annots = [ann_x, ann_y]

_orig_set_axis_off = _Axes.set_axis_off
def _sds_set_axis_off(self, *args, **kwargs):
    _orig_set_axis_off(self, *args, **kwargs)
    for ann in getattr(self, '_sds_arrow_annots', []):
        ann.set_visible(False)
_Axes.set_axis_off = _sds_set_axis_off

_orig_set_axis_on = _Axes.set_axis_on
def _sds_set_axis_on(self, *args, **kwargs):
    _orig_set_axis_on(self, *args, **kwargs)
    for ann in getattr(self, '_sds_arrow_annots', []):
        ann.set_visible(True)
_Axes.set_axis_on = _sds_set_axis_on

if not getattr(_Figure, '_sds_patched', False):
    _Figure._sds_patched = True
    _orig_add_subplot = _Figure.add_subplot
    def _sds_add_subplot(self, *args, **kwargs):
        ax = _orig_add_subplot(self, *args, **kwargs)
        _sds_setup_arrow_axes(ax)
        return ax
    _Figure.add_subplot = _sds_add_subplot

"""

# Wrap it in a hidden myst-nb code cell
_HIDDEN_CELL = f"""\
```{{code-cell}} python
:tags: [remove-cell]

{_SETUP_CODE.replace('__SDS_STYLE_PATH__', _STYLE_PATH)}
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