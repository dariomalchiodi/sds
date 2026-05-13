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

(sec_set-relations)=
# Set relations

Among the fundamental concepts of set theory, that of a _subset_ occupies a
central role: from it a series of general relations between sets can be
defined. More precisely:

```{margin}
Alternatively one says that $T$ is a _superset_ of $S$ and writes
$T \supseteq S$.
```
- when every element $s$ belonging to a set $S$ also belongs to a second set
  $T$, we say that $S$ is a _subset_ of $T$ (or that $S$ is _contained in_
  $T$) and denote this fact by $S \subseteq T$:

  ```{math}
  S \subseteq T \leftrightarrow \forall s \in \Omega \;
  (s \in S \rightarrow s \in T) \enspace.
  ```

- two sets are said to be equal when each is a subset of the other:

```{math}
S = T \leftrightarrow S \subseteq T \wedge T \subseteq S ;
```

- two sets are said to be different when they are not equal;

- the _strict inclusion_ relation holds between two sets when one is contained
  in the other and in addition the two sets are not equal:

```{math}
S \subset T \leftrightarrow S \subseteq T \wedge T \neq S .
```

````{prf:example}
:label: ex-en-subsets

{numref}`fig_en-venn-subsets` illustrates the Venn diagram for the set $O$
from {numref}`fig_en-venn-universe`, viewed as a subset of
$A = \{ \text{Avengers members} \}$, both contained within the universe
$\Omega$ of all superheroes.
````

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

def subset_venn():
    fig, ax = plt.subplots(facecolor=BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)

    rect = Rectangle((0.1, 0.1), 11.8, 7.8,
                     facecolor=BG_COLOR, edgecolor=EDGE_COLOR,
                     linewidth=1.1, zorder=0)
    ax.add_patch(rect)
    ax.text(11.6, 7.6, r'$\Omega$', fontsize=MATH_SIZE, ha='right', va='top')

    ellipse_A = Ellipse(xy=(6, 4), width=10.5, height=6.0,
                        facecolor=FILL_COLOR_A, edgecolor=EDGE_COLOR,
                        linewidth=1.2, zorder=1)
    ax.add_patch(ellipse_A)
    ax.text(1.7, 6.7, r'$A$', fontsize=MATH_SIZE, va='top')

    ellipse_O = Ellipse(xy=(6, 3.8), width=5.5, height=3.2,
                        facecolor=FILL_COLOR_O, edgecolor=EDGE_COLOR,
                        linewidth=1.2, zorder=2)
    ax.add_patch(ellipse_O)
    ax.text(3.9, 5.7, r'$O$', fontsize=MATH_SIZE, va='top')

    for name, x, y, xof, yof in [('Thor',              5.2, 4.7,  0.8,  0.),
                                  ('Hulk',              8.,  4.,  -0.8,  0.),
                                  ('Captain\nAmerica',  4.,  3.3,  1.2,  0.),
                                  ('Iron\nMan',         1.7, 5.,   0.8,  0.),
                                  ('Black\nWidow',      9.8, 5.5,  0.,  -0.9),
                                  ('Hawkeye',           2.5, 2.6, -0.1,  0.4),
                                  ('Ant-Man',           9.5, 2.2, -1.1,  0.)]:
        ax.plot(x, y, "o", markersize=4, color=DOT_COLOR, zorder=4)
        ax.text(x + xof, y + yof, name, ha='center', va='center',
                fontsize=TEXT_SIZE, zorder=5)

    return fig

fig = subset_venn()
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_en-venn-subsets

A Venn diagram illustrating two sets $O$ and $A$ such that $O \subseteq A$:
$O$ is the set of Avengers with superhuman strength (Thor, Hulk, and Captain
America), $A$ is the set of all Avengers, and $\Omega$ is the universe of all
superheroes.
````


It is straightforward to verify that every set is always contained in the
universe, and that the empty set is always contained in every set:

```{math}
\forall S \subseteq \Omega \quad \varnothing \subseteq S \subseteq \Omega ,
```

and this relation continues to hold for strict inclusion, provided $S$ differs
from the empty set (so that the left part holds) and from the universe (so
that the right part holds).
