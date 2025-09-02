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

(sec:concetti-base-insiemi)=
# Concetti di base

In accordo con la definizione sopra riportata, nonché con la comune notazione
matematica, indicheremo di norma gli insiemi utilizzando le lettere maiuscole
dell'alfabeto latino e i loro elementi usando le corrispondenti lettere
minuscole. Per indicare che un elemento $a$ appartiene a un insieme $A$
scriveremo $a \in A$, mentre per indicare che un elemento $b$ non appartiene
all'insieme $A$ scriveremo $b \notin A$.

Un insieme può essere rappresentato:

- _estensivamente_, cioé elencando tutti i suoi elementi tramite una sequenza:
  per esempio l'insieme $O$ dei possibili esiti del lancio di un dado che
  corrispondono a un numero dispari si può indicare estensivamente come
  $O = \{ 1, 3, 5, 6 \}$;
- _intensivamente_, specificando una proprietà matematica valida per tutti gli
  elementi dell'insieme: l'insieme descritto al punto precedente ammette la
  descrizione intensiva

```{math}
O = \{ k \in \mathbb N \text{ tale che } 1 \leq k \leq 6
        \text{ e } k \text{ è pari} \} \enspace;
```
- tramite un _diagramma di Venn_, indicando gli elementi come punti in una
  porzione di piano e racchiudendoli dentro un'ellisse: l'insieme $O$ descritto
  nei due punti precedenti può anche essere rappresentato tramite il diagramma
  di Venn illustrato qui sotto per descrivere l'insieme
  $O = \{ 1, 3, 5, 6 \}$.

````{customfigure}
:name: fig:venn-simple

```{code-block} python
:class:  toggle-code

import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib_venn import venn2_circles, venn2

import io, base64

font_size = 9
venn_set_color = '#00CCFF'
venn_set_edge= '#333333'
background_color = '#eaf3f5'

def simple_venn(universe=False):
    fig, ax = plt.subplots()

    v = venn2(subsets=(3, 3, 0), set_labels=(r'$O$', ''), ax=ax) ##
    c = venn2_circles(subsets=(3, 3, 0), ax=ax)
    for _ in c:
        _.set_linewidth(0.6)

    for l in v.set_labels:
      l.set_fontsize(font_size)

    for area in ['01', '10', '11']:
        if area != '11':
          txt = v.get_label_by_id(area)
          if txt:
            txt.set_text('')

    v.get_patch_by_id('10').set_color(venn_set_color)
    v.get_patch_by_id('10').set_alpha(1)

    v.get_patch_by_id('01').set_color(background_color)
    c[1].set_edgecolor(background_color)

    if universe:
      ax.text(.6, .1, '2', fontsize=font_size)
      ax.text(.2, -0.1, '4', fontsize=font_size)
      ax.text(.5, -0.3, '6', fontsize=font_size)
      ax.text(0.75, 0.45, r'$\Omega$', fontsize=font_size)
      ax.plot([-1.1, 1.1, 1.1, -1.1, -1.1], [-0.6, -0.6, 0.6, 0.6, -0.6], lw=1)
    
    ax.set_ylim(-0.7, 0.7)
    ax.text(-0.85, 0, '1', fontsize=font_size)
    ax.text(-0.55, 0.15, '3', fontsize=font_size)
    ax.text(-0.55, -0.2, '5', fontsize=font_size)

    return fig

fig = simple_venn()
fig.show()
```

Un diagramma di Venn che descrive l'insieme $O = \{ 1, 3, 5, 6 \}$.
````

In particolare, la descrizione tramite i diagrammi di Venn presuppone la
conoscenza, in linea di principio, di tutti gli elementi che potrebbero far
parte di un insieme. L'insieme di tutti i possibili elementi si indica in
genere con il simbolo $\Omega$ che viene chiamato _insieme universo_.
Nell'esempio precedente facciamo ovviamente riferimento all'universo $\Omega =
\{ 1, 2, 3, 4, 5, 6 \}$, pertanto il diagramma di Venn che rappresenta $O$ più
correttamente è quello riportato nella {numref}`fig:venn-universe`.

````{customfigure}
:name: fig:venn-universe

```{code-block} python
:class:  toggle-code

fig = simple_venn(universe=True)
plt.show()
```
Un diagramma di Venn che illustra l'insieme $O$ della {numref}`fig:venn-simple`
all'interno dell'universo $\Omega = \{ 1, 2, 3, 4, 5, 6 \}$.
````

Così come l'insieme universo è tale da contenere qualunque elemento, è
matematicamente rilevante pensare ad un insieme che dualmente, non contiene
alcun elemento. Tale insieme viene chiamato insieme vuoto, e lo indicheremo
scrivendo $\{\}$ (anche se è comune l'uso del simbolo $\varnothing$), così che
per ogni $a \in \Omega$ si avrà $a \notin \{\}$.
