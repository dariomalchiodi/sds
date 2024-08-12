import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib_venn import venn2_circles, venn2
from myst_nb import glue

import matplotlib
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
matplotlib.rcParams['mathtext.fontset'] = 'cm'
font_size = 18
matplotlib.rcParams['font.size'] = str(font_size)

venn_set_color = '#0071BC'
venn_set_edge= '#333333'


def simple_venn(universe=False):
    fig = plt.figure()

    v = venn2(subsets=(3, 3, 0), set_labels=('$O$', ''))
    c = venn2_circles(subsets=(3, 3, 0))

    for l in v.set_labels:
      l.set_fontsize(font_size)

    for area in ['01', '10', '11']:
        if area != '11':
          txt = v.get_label_by_id(area)
          if txt:
            txt.set_text('')

    v.get_patch_by_id('10').set_color(venn_set_color)
    v.get_patch_by_id('10').set_alpha(1)

    v.get_patch_by_id('01').set_color('white')
    c[1].set_edgecolor('white')

    plt.gca().set_facecolor('white')

    ymin, ymax = plt.gca().get_ylim()
    plt.ylim(ymin - 0.1, ymax)
    if universe:
        plt.gca().set_axis_on()
        plt.text(.6, .1, '$2$', fontsize=font_size)
        plt.text(.2, -0.1, '$4$', fontsize=font_size)
        plt.text(.5, -0.3, '$6$', fontsize=font_size)
        plt.text(0.95, 0.35, '$\Omega$')

    plt.text(-0.85, 0, '$1$', fontsize=font_size)
    plt.text(-0.55, 0.15, '$3$', fontsize=font_size)
    plt.text(-0.55, -0.2, '$5$', fontsize=font_size)

    return fig

def subset_venn():
    fig = plt.figure()

    v = venn2(subsets=(5, 0, 2), set_labels=('$T$', '$S$'))

    for l in v.set_labels:
        l.set_fontsize(font_size)

    for area in ['01', '10', '11']:
        v.get_patch_by_id(area).set_color(venn_set_color)
        v.get_patch_by_id(area).set_edgecolor(venn_set_edge)
        v.get_patch_by_id(area).set_alpha(1)
        txt = v.get_label_by_id(area)
        if txt:
          txt.set_text('')

    v.set_labels[1].set_position((-0.2, 0.3))

    plt.gca().set_axis_on()
    plt.gca().set_facecolor('white')
    ymin, ymax = plt.gca().get_ylim()
    plt.ylim(ymin - 0.1, ymax)

    plt.text(0.47, 0.5, '$\Omega$')

    return fig

def venn_operations(operation='union'):
    fig = plt.figure()

    v = venn2(subsets=(3, 3, 1), set_labels=('$S$', '$T$'))
    c = venn2_circles(subsets=(3, 3, 1))

    for l in v.set_labels:
        l.set_fontsize(font_size)

    for contour in c:
        contour.set_lw(1.4)
        contour.set_edgecolor(venn_set_edge)

    for area in ['01', '10', '11']:
        v.get_patch_by_id(area).set_color(venn_set_color)
        v.get_patch_by_id(area).set_alpha(1)
        txt = v.get_label_by_id(area)
        if txt:
            txt.set_text('')

    if operation == 'intersection':
        v.get_patch_by_id('10').set_color('white')
        v.get_patch_by_id('11').set_color(venn_set_color)
        v.get_patch_by_id('11').set_alpha(1)
        v.get_patch_by_id('01').set_color('white')
    elif operation == 'difference':
        v.get_patch_by_id('10').set_color(venn_set_color)
        v.get_patch_by_id('11').set_color('white')
        v.get_patch_by_id('01').set_color('white')
    elif operation == 'symdifference':
        v.get_patch_by_id('11').set_color('white')
    elif operation == 'complement':
        v.get_patch_by_id('10').set_color('white')
        v.get_patch_by_id('11').set_color('white')

    plt.gca().set_facecolor('white' if operation != 'complement' \
                                    else venn_set_color)
    plt.gca().set_axis_on()
    ymin, ymax = plt.gca().get_ylim()
    plt.ylim(ymin - 0.1, ymax)
    plt.text(0.7, 0.43, '$\Omega$')
    return fig
