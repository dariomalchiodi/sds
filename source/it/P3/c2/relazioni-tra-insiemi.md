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

(sec_relazioni-tra-insiemi)=
# Relazioni tra insiemi

Tra i concetti fondamentali della teoria degli insiemi, quello di
_sottoinsieme_ occupa un ruolo centrale: a partire da esso è possibile
definire una serie di relazioni tra insiemi di carattere generale. Più
precisamente:

```{margin}
In alternativa si dice che $T$ è un _sovrainsieme_ di $S$ e si scrive
$T \supseteq S$.
```
- quando ogni elemento $s$ appartenente a un insieme $S$ risulta appartenente
  anche a un secondo insieme $T$, si dice che $S$ è un _sottoinsieme_ di $T$ (o
  che $S$ è _incluso_  in $T$) e si indica questo fatto con la notazione
  $S \subseteq T$:

  ```{math}
  S \subseteq T \leftrightarrow \forall s \in \Omega \;
  (s \in S \rightarrow s \in T) \enspace.
  ```

- due insiemi si dicono uguali quando si includono mutuamente:

```{math}
S = T \leftrightarrow S \subseteq T \wedge T \subseteq S ;
```

- due insiemi si dicono diversi quando non sono uguali;

- tra due insiemi sussiste la relazione di inclusione _in senso stretto_ quando
  uno dei due è incluso nell'altro e in aggiunta i due insiemi non sono uguali:

```{math}
S \subset T \leftrightarrow S \subseteq T \wedge T \neq S .
```

````{prf:example}
:label: ex-subst

La {numref}`fig_venn-sottoinsiemi` illustra  il diagramma
di Venn per l'insieme $O$ della {numref}`fig_venn-universe`, inteso come
sottoinsieme di $A = \{ \text{membri degliAvengers} \}$, entrambi inclusi
nell'universo $\Omega$ di tutti i supereroi.
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

    for name, x, y, xof, yof in [('Thor',             5.2, 4.7,  0.8,  0.),
                                  ('Hulk',             8.,  4.,  -0.8,  0.),
                                  ('Capitan\nAmerica', 4.,  3.3,  1.2,  0.),
                                  ('Iron\nMan',        1.7, 5.,   0.8,  0.),
                                  ('Black\nWidow',     9.8, 5.5,  0.,  -0.9),
                                  ('Hawkeye',          2.5, 2.6, -0.1,  0.4),
                                  ('Ant-Man',          9.5, 2.2, -1.1,  0.)]:
        ax.plot(x, y, "o", markersize=4, color=DOT_COLOR, zorder=4)
        ax.text(x + xof, y + yof, name, ha='center', va='center',
                fontsize=TEXT_SIZE, zorder=5)

    return fig

fig = subset_venn()
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_venn-sottoinsiemi

Un diagramma di Venn che illustra due insiemi $O$ e $A$ tali che $O \subseteq
A$: $O$ è l'insieme degli Avengers con forza sovrumana (Thor, Hulk e Capitan 
America), $A$ è l'insieme di tutti gli Avengers e $\Omega$ è l'insieme universo
di tutti i supereroi.
````


Si verifica facilmente come qualunque insieme risulti sempre incluso
nell'insieme universo, e come analogamente l'insieme vuoto risulti sempre
incluso in qualunque insieme:

```{math}
\forall S \subseteq \Omega \quad \varnothing \subseteq S \subseteq \Omega ,
```

e questa relazione continua a valere se si considera la relazione di inclusione
in senso stretto, a patto che $S$ sia diverso dall'insieme vuoto (affinché
valga la prima parte della relazione) e dall'insieme universo (affinché possa
valere la sua seconda parte).
