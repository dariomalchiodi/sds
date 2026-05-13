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

(sec_relations-ensembles)=
# Relations entre ensembles

Parmi les concepts fondamentaux de la théorie des ensembles, celui de
_sous-ensemble_ occupe un rôle central : à partir de lui, on peut définir
une série de relations générales entre ensembles. Plus précisément :

```{margin}
On dit aussi que $T$ est un _sur-ensemble_ de $S$ et on écrit
$T \supseteq S$.
```
- lorsque tout élément $s$ appartenant à un ensemble $S$ appartient
  également à un second ensemble $T$, on dit que $S$ est un _sous-ensemble_
  de $T$ (ou que $S$ est _inclus_ dans $T$) et on note ce fait par
  $S \subseteq T$ :

  ```{math}
  S \subseteq T \leftrightarrow \forall s \in \Omega \;
  (s \in S \rightarrow s \in T) \enspace.
  ```

- deux ensembles sont dits égaux lorsque chacun est sous-ensemble de
  l'autre :

```{math}
S = T \leftrightarrow S \subseteq T \wedge T \subseteq S ;
```

- deux ensembles sont dits différents lorsqu'ils ne sont pas égaux ;

- la relation d'_inclusion stricte_ entre deux ensembles a lieu lorsque
  l'un est inclus dans l'autre et que de plus les deux ensembles ne sont
  pas égaux :

```{math}
S \subset T \leftrightarrow S \subseteq T \wedge T \neq S .
```

````{prf:example}
:label: ex-fr-sous-ensembles

La {numref}`fig_fr-venn-sous-ensembles` illustre le diagramme de Venn pour
l'ensemble $O$ de la {numref}`fig_fr-venn-univers`, considéré comme
sous-ensemble de $A = \{ \text{membres des Avengers} \}$, tous deux inclus
dans l'univers $\Omega$ de tous les super-héros.
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
:name: fig_fr-venn-sous-ensembles

Un diagramme de Venn illustrant deux ensembles $O$ et $A$ tels que
$O \subseteq A$ : $O$ est l'ensemble des Avengers dotés d'une force
surhumaine (Thor, Hulk et Captain America), $A$ est l'ensemble de tous
les Avengers, et $\Omega$ est l'univers de tous les super-héros.
````


Il est facile de vérifier que tout ensemble est toujours inclus dans
l'univers, et que l'ensemble vide est toujours inclus dans tout ensemble :

```{math}
\forall S \subseteq \Omega \quad \varnothing \subseteq S \subseteq \Omega ,
```

et cette relation continue de valoir pour l'inclusion stricte, à condition
que $S$ soit différent de l'ensemble vide (pour que la première partie soit
valable) et de l'univers (pour que la seconde partie le soit).
