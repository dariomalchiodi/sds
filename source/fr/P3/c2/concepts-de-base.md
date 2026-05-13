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

(sec_concepts-base-ensembles)=
# Concepts de base

Conformément à la définition donnée au début du chapitre, et à la notation
mathématique usuelle, je désignerai en général les ensembles par des lettres
majuscules de l'alphabet latin et leurs éléments par les lettres minuscules
correspondantes. Pour indiquer qu'un élément $a$ appartient à un ensemble
$A$, j'écrirai $a \in A$, et pour indiquer que $b$ n'y appartient pas,
j'écrirai $b \notin A$.

Un ensemble peut être représenté :

- _extensivement_, en énumérant tous ses éléments : par exemple, l'ensemble
  $O$ des membres des
  [Avengers](https://marvel.fandom.com/wiki/Avengers_(Earth-616)) qui ont
  une force surhumaine peut s'écrire extensivement comme
  $O = \{ \text{Captain America}, \text{Hulk}, \text{Thor} \}$ ;
- _intensivement_, en spécifiant une propriété qui caractérise exactement
  tous les éléments de l'ensemble : l'ensemble décrit ci-dessus admet par
  exemple la description intensive

```{math}
O = \{ \text{Avengers dotés d'une force surhumaine} \} \enspace ;
```
- via un _diagramme de Venn_, en indiquant les éléments comme des points
  dans une région du plan et en les enfermant dans une ellipse : l'ensemble
  $O$ décrit ci-dessus est illustré dans la {numref}`fig_fr-venn-simple`.


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
:name: fig_fr-venn-simple


Un diagramme de Venn décrivant l'ensemble $O = \{ \text{Avengers dotés d'une force surhumaine} \}$.
````

La représentation par diagramme de Venn suppose de connaître, au moins en
principe, tous les éléments qui pourraient appartenir à un ensemble.
L'ensemble de tous les éléments possibles s'appelle l'_univers_ et se
désigne habituellement par $\Omega$. Dans l'exemple précédent, un choix
naturel pour l'univers ferait coïncider $\Omega$ avec l'ensemble des
Avengers, de sorte qu'un diagramme de Venn plus complet pour $O$ est celui
représenté dans la {numref}`fig_fr-venn-univers`.

```{code-cell} python
:tags: [hide-input]

fig = simple_venn(universe=True)
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_fr-venn-univers

Un diagramme de Venn illustrant l'ensemble $O$ de la {numref}`fig_fr-venn-simple`
au sein de l'univers $\Omega$ des Avengers.
````

L'univers contient tout élément, et — à l'extrême opposé — il est utile de
considérer l'ensemble qui ne contient aucun élément : on l'appelle
l'_ensemble vide_ et je le noterai $\varnothing$, de sorte que pour tout
$a \in \Omega$ on ait $a \notin \varnothing$.
