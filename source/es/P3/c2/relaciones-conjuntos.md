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

(sec_relaciones-conjuntos)=
# Relaciones entre conjuntos

Entre los conceptos fundamentales de la teoría de conjuntos, el de
_subconjunto_ ocupa un papel central: a partir de él se puede definir una
serie de relaciones generales entre conjuntos. Más precisamente:

```{margin}
Alternativamente se dice que $T$ es un _superconjunto_ de $S$ y se escribe
$T \supseteq S$.
```
- cuando todo elemento $s$ perteneciente a un conjunto $S$ pertenece
  también a un segundo conjunto $T$, se dice que $S$ es un _subconjunto_
  de $T$ (o que $S$ está _contenido_ en $T$) y se denota este hecho por
  $S \subseteq T$:

  ```{math}
  S \subseteq T \leftrightarrow \forall s \in \Omega \;
  (s \in S \rightarrow s \in T) \enspace.
  ```

- dos conjuntos se dicen iguales cuando cada uno es subconjunto del otro:

```{math}
S = T \leftrightarrow S \subseteq T \wedge T \subseteq S ;
```

- dos conjuntos se dicen distintos cuando no son iguales;

- la relación de _inclusión estricta_ entre dos conjuntos se da cuando uno
  está contenido en el otro y además los dos conjuntos no son iguales:

```{math}
S \subset T \leftrightarrow S \subseteq T \wedge T \neq S .
```

````{prf:example}
:label: ex-es-subconjuntos

La {numref}`fig_es-venn-subconjuntos` ilustra el diagrama de Venn para el
conjunto $O$ de la {numref}`fig_es-venn-universo`, considerado como
subconjunto de $A = \{ \text{miembros de los Avengers} \}$, ambos
contenidos en el universo $\Omega$ de todos los superhéroes.
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
:name: fig_es-venn-subconjuntos

Un diagrama de Venn que ilustra dos conjuntos $O$ y $A$ tales que
$O \subseteq A$: $O$ es el conjunto de los Avengers con fuerza sobrehumana
(Thor, Hulk y Captain America), $A$ es el conjunto de todos los Avengers,
y $\Omega$ es el universo de todos los superhéroes.
````


Es fácil verificar que todo conjunto está siempre contenido en el universo,
y que el conjunto vacío está siempre contenido en cualquier conjunto:

```{math}
\forall S \subseteq \Omega \quad \varnothing \subseteq S \subseteq \Omega ,
```

y esta relación sigue siendo válida para la inclusión estricta, siempre
que $S$ sea distinto del conjunto vacío (para que la primera parte sea
válida) y del universo (para que la segunda parte lo sea).
