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

(sec_concetti-base-insiemi)=
# Concetti di base

In accordo con la definizione riportata all'inizio del capitolo, nonché con
la comune notazione matematica, indicherò di norma gli insiemi con le lettere
maiuscole dell'alfabeto latino e i loro elementi con le corrispondenti lettere
minuscole. Per indicare che un elemento $a$ appartiene a un insieme $A$
scriverò $a \in A$, mentre per indicare che $b$ non vi appartiene scriverò
$b \notin A$.

Un insieme può essere rappresentato:

- _estensivamente_, cioè elencando tutti i suoi elementi: per esempio,
  l'insieme $O$ dei membri degli
  [Avengers](https://marvel.fandom.com/wiki/Avengers_(Earth-616)) che hanno
  una forza sovrumana si può indicare estensivamente come 
  $O = \{ \text{Capitan America}, \text{Hulk}, \text{Thor} \}$;
- _intensivamente_, specificando una proprietà che individua tutti e soli gli
  elementi dell'insieme: l'insieme descritto al punto precedente ammette per
  esempio la descrizione intensiva

```{math}
O = \{ \text{Componenti degli Avengers con forza sovrumana} \} \enspace;
```
- tramite un _diagramma di Venn_, indicando gli elementi come punti in una
  porzione di piano e racchiudendoli dentro un'ellisse: l'insieme $O$ descritto
  nei punti precedenti è illustrato nella {numref}`fig_venn-simple`.


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
                                 ('Capitan\nAmerica', 4,   3.3, 1.2, 0)]:
        ax.plot(x, y, "o", markersize=4, color=DOT_COLOR, zorder=4)
        ax.text(x + xof, y + yof, name, ha='center', va='center',
                fontsize=TEXT_SIZE, zorder=5)

    return fig

fig = simple_venn()
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_venn-simple


Un diagramma di Venn che descrive l'insieme $O = \{ \text{Componenti degli Avengers con forza sovrumana} \}$.
````

La descrizione tramite diagramma di Venn presuppone di conoscere, almeno in
linea di principio, tutti gli elementi che potrebbero far parte di un insieme.
L'insieme di tutti i possibili elementi si chiama _insieme universo_ e si
indica di solito con $\Omega$. Nell'esempio precedente, una scelta ragionevole per l'universo potrebbe far coincidere
$\Omega$ con l'insieme degli Avengers, quindi un diagramma di Venn più completo
per $O$ è quello riportato nella {numref}`fig_venn-universe`.

```{code-cell} python
:tags: [hide-input]

fig = simple_venn(universe=True)
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_venn-universe

Un diagramma di Venn che illustra l'insieme $O$ della {numref}`fig_venn-simple`
all'interno dell'universo $\Omega$ degli Avengers.
````

L'insieme universo contiene qualunque elemento, e &mdash; all'estremo opposto
&mdash; è utile considerare l'insieme che non ne contiene nessuno: si chiama
_insieme vuoto_ e lo indicherò con $\varnothing$, in modo che per ogni
$a \in \Omega$ valga $a \notin \varnothing$.

