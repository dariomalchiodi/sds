---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  name: python3
  display_name: Python 3
---

(sec_basic-concepts-sets)=
# Basic concepts

In keeping with the definition given at the start of the chapter, and with
standard mathematical notation, I will normally denote sets by capital letters
of the Latin alphabet and their elements by the corresponding lower-case
letters. To indicate that an element $a$ belongs to a set $A$ I will write
$a \in A$, and to indicate that $b$ does not belong to it I will write
$b \notin A$.

A set can be represented:

- _extensively_, by listing all its elements: for example, the set $O$ of
  members of the
  [Avengers](https://marvel.fandom.com/wiki/Avengers_(Earth-616)) who have
  superhuman strength can be written extensively as
  $O = \{ \text{Captain America}, \text{Hulk}, \text{Thor} \}$;
- _intensively_, by specifying a property that identifies exactly all the
  elements of the set: the set described above admits, for example, the
  intensive description

```{math}
O = \{ \text{Avengers members with superhuman strength} \} \enspace;
```
- via a _Venn diagram_, by marking the elements as points in a region of the
  plane and enclosing them within an ellipse: the set $O$ described above is
  illustrated in {numref}`fig_en-venn-simple`.


```{code-cell} python
:tags:  [hide-input]

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle

MATH_SIZE = 9
TEXT_SIZE = 7

EDGE_COLOR = '#333333'
BG_COLOR = '#eaf3f5'
FILL_COLOR_A = '#d6e4f7'
FILL_COLOR_O = '#aac5e8'
DOT_COLOR = '#2255aa'


def simple_venn(universe=False):
    fig, ax = plt.subplots(facecolor=BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)

    if universe:
        rect = Rectangle((0.1, 0.1), 11.8, 7.8,
                        facecolor=BG_COLOR, edgecolor=EDGE_COLOR,
                        linewidth=1.1, zorder=0)
        ax.add_patch(rect)
        ax.text(11.6, 7.6, r'$\Omega$', fontsize=MATH_SIZE, ha='right', va='top')

        for name, x, y, xof, yof in [('Iron\nMan',    1.7, 5,    0.8, 0),
                                 ('Black\nWidow', 9.8, 5.5,  0,  -0.9),
                                 ('Hawkeye',      2.5, 2.6, -0.1, 0.4),
                                 ('Ant-Man',      9.5, 2.2, -1.1, 0)]:
            ax.plot(x, y, "o", markersize=4, color=DOT_COLOR, zorder=4)
            ax.text(x + xof, y + yof, name, ha='center', va='center',
                    fontsize=TEXT_SIZE, zorder=5)

    ellipse_O = Ellipse(xy=(6, 3.8), width=5.5, height=3.2,
                        facecolor=FILL_COLOR_O, edgecolor=EDGE_COLOR,
                        linewidth=1.2, zorder=2)
    ax.add_patch(ellipse_O)
    ax.text(3.9, 5.7, r'$O$', fontsize=MATH_SIZE, va='top')

    for name, x, y, xof, yof in [('Thor',             5.2, 4.7, 0.8, 0),
                                 ('Hulk',             8,   4,  -0.8, 0),
                                 ('Captain\nAmerica', 4,   3.3, 1.2, 0)]:
        ax.plot(x, y, "o", markersize=4, color=DOT_COLOR, zorder=4)
        ax.text(x + xof, y + yof, name, ha='center', va='center',
                fontsize=TEXT_SIZE, zorder=5)

    return fig

fig = simple_venn()
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_en-venn-simple


A Venn diagram describing the set $O = \{ \text{Avengers members with superhuman strength} \}$.
````

The Venn diagram representation presupposes knowing, at least in principle,
all the elements that could belong to a set. The set of all possible elements
is called the _universe_ and is usually denoted by $\Omega$. In the previous
example, a natural choice for the universe would make $\Omega$ coincide with
the set of all Avengers, so a more complete Venn diagram for $O$ is the one
shown in {numref}`fig_en-venn-universe`.

```{code-cell} python
:tags: [hide-input]

fig = simple_venn(universe=True)
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_en-venn-universe

A Venn diagram illustrating the set $O$ from {numref}`fig_en-venn-simple`
within the universe $\Omega$ of the Avengers.
````

The universe contains every element, and — at the opposite extreme — it is
useful to consider the set that contains no elements at all: it is called the
_empty set_ and I will denote it by $\varnothing$, so that for every
$a \in \Omega$ we have $a \notin \varnothing$.
