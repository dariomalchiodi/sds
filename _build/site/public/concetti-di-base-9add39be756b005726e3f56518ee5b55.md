
## Concetti di base

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

$$
O = \{ k \in \mathbb N \text{ tale che } 1 \leq k \leq 6 \text{ e } k \text{ è pari} \};
$$
- tramite un _diagramma di Venn_, indicando gli elementi come punti in una
  porzione di piano e racchiudendoli dentro un'ellisse: l'insieme $O$ descritto
  nei due punti precedenti può anche essere rappresentato tramite il diagramma
  di Venn illustrato in {numref}`venn`.

````{figure} venn-picture
:figwidth: 100%
:name: "venn"

```{code-cell} ipython3
:tags: [remove-input]
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib_venn import venn2_circles, venn2

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
        plt.text(0.95, 0.35, '$\\Omega$')

    plt.text(-0.85, 0, '$1$', fontsize=font_size)
    plt.text(-0.55, 0.15, '$3$', fontsize=font_size)
    plt.text(-0.55, -0.2, '$5$', fontsize=font_size)

    return fig

fig = simple_venn()
```

Un semplice diagramma di Venn per descrivere l'insieme $O = \{ 1, 3, 5, 6 \}$.
````

In particolare, la descrizione tramite i diagrammi di Venn presuppone la
conoscenza, in linea di principio, di tutti gli elementi che potrebbero far
parte di un insieme. L'insieme di tutti i possibili elementi si indica in
genere con il simbolo $\Omega$ che viene chiamato _insieme universo_.
Nell'esempio precedente facciamo ovviamente riferimento all'universo
$\Omega = \{ 1, 2, 3, 4, 5, 6 \}$, il diagramma di Venn dell'insieme $O$ è
visualizzato in modo più corretto nella {numref}`venn-universe`.

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

fig = simple_venn(universe=True)

glue("venn-universe-picture", fig, display=False)
```

```{glue:figure} venn-universe-picture
:figwidth: 100%
:name: "venn-universe"

Un diagramma di Venn per descrivere l'insieme $O$ della {numref}`venn`
evidenziando il corrispondente insieme universo $\Omega$.
```

Così come l'insieme universo è tale da contenere qualunque elemento, è
matematicamente rilevante pensare ad un insieme che dualmente, non contiene
alcun elemento. Tale insieme viene chiamato insieme vuoto, e lo indicheremo
scrivendo $\{\}$ (anche se è comune l'uso del simbolo $\varnothing$), così che
per qualsiasi elemento $a$ si avrà $a \notin \{\}$.
