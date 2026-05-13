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

(sec_conceptos-basicos-conjuntos)=
# Conceptos básicos

De acuerdo con la definición dada al comienzo del capítulo, y con la
notación matemática estándar, designaré en general los conjuntos con
letras mayúsculas del alfabeto latino y sus elementos con las letras
minúsculas correspondientes. Para indicar que un elemento $a$ pertenece
a un conjunto $A$ escribiré $a \in A$, y para indicar que $b$ no
pertenece a él escribiré $b \notin A$.

Un conjunto puede representarse:

- _extensivamente_, enumerando todos sus elementos: por ejemplo, el
  conjunto $O$ de los miembros de los
  [Avengers](https://marvel.fandom.com/wiki/Avengers_(Earth-616)) que
  tienen fuerza sobrehumana puede escribirse extensivamente como
  $O = \{ \text{Captain America}, \text{Hulk}, \text{Thor} \}$;
- _intensivamente_, especificando una propiedad que identifica exactamente
  todos los elementos del conjunto: el conjunto descrito anteriormente
  admite, por ejemplo, la descripción intensiva

```{math}
O = \{ \text{Avengers con fuerza sobrehumana} \} \enspace;
```
- mediante un _diagrama de Venn_, indicando los elementos como puntos en
  una región del plano y encerrándolos dentro de una elipse: el conjunto
  $O$ descrito anteriormente está ilustrado en la {numref}`fig_es-venn-simple`.


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
:name: fig_es-venn-simple


Un diagrama de Venn que describe el conjunto $O = \{ \text{Avengers con fuerza sobrehumana} \}$.
````

La representación mediante diagrama de Venn presupone conocer, al menos en
principio, todos los elementos que podrían pertenecer a un conjunto.
El conjunto de todos los elementos posibles se llama el _universo_ y se
denota habitualmente por $\Omega$. En el ejemplo anterior, una elección
natural para el universo haría coincidir $\Omega$ con el conjunto de los
Avengers, por lo que un diagrama de Venn más completo para $O$ es el que
se muestra en la {numref}`fig_es-venn-universo`.

```{code-cell} python
:tags: [hide-input]

fig = simple_venn(universe=True)
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_es-venn-universo

Un diagrama de Venn que ilustra el conjunto $O$ de la {numref}`fig_es-venn-simple`
dentro del universo $\Omega$ de los Avengers.
````

El universo contiene cualquier elemento, y — en el extremo opuesto — es
útil considerar el conjunto que no contiene ningún elemento: se llama
el _conjunto vacío_ y lo denotaré por $\varnothing$, de modo que para
todo $a \in \Omega$ se tenga $a \notin \varnothing$.
