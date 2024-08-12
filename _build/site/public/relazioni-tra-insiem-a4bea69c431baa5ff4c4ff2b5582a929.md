
## Relazioni tra insiemi

A partire dalla nozione di _sottoinsieme_ è possibile derivare una serie di
relazioni tra insiemi di carattere generale; più precisamente:

```{margin}
in alternativa si dice che $T$ è un _sovrainsieme_ di $S$ e si scrive
$T \supseteq S$
```

- quando ogni elemento $s$ appartenente a un insieme $S$ risulta appartenente
  anche a un secondo insieme $T$, si dice che $S$ è un _sottoinsieme_ di $T$ (o
  che $S$ è _incluso_  in $T$) e si indica questo fatto con la notazione
  $S \subseteq T$ (vedi {numref}`venn-subset`):

$$ S \subseteq T \leftrightarrow \forall s \in \Omega
 (s \in S \rightarrow s \in T) ;$$

````{figure}
:figwidth: 100%
:name: "venn-subset"

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

def subset_venn():
    fig = plt.figure()

    v = venn2(subsets=(5, 0, 2), set_labels=('$T$', '$S$'))

    for l in v.set_labels:
        l.set_fontsize(font_size)

    for area in ['01', '10', '11']:
        v.get_patch_by_id(area).set_color(venn_set_color)
        v.get_patch_by_id(area).set_edgecolor(venn_set_edge)
        v.get_patch_by_id(area).set_alpha(1)
        txt = v.get_label_by_id(area)
        if txt:
          txt.set_text('')

    v.set_labels[1].set_position((-0.2, 0.3))

    plt.gca().set_axis_on()
    plt.gca().set_facecolor('white')
    ymin, ymax = plt.gca().get_ylim()
    plt.ylim(ymin - 0.1, ymax)

    plt.text(0.47, 0.5, r'$\Omega$')

    return fig

fig = subset_venn()
```

Un diagramma di Venn per descrivere due insiemi $S$ e $T$ tali che
$S \subseteq T$.
````

- due insiemi si dicono uguali quando si includono mutuamente:

$$ S = T \leftrightarrow S \subseteq T \wedge T \subseteq S ;$$

- due insiemi si dicono diversi quando non sono uguali;

- tra due insiemi sussiste la relazione di inclusione _in senso stretto_ quando
  uno dei due è incluso nell'altro e in aggiunta i due insiemi non sono uguali:

$$ S \subset T \leftrightarrow S \subseteq T \wedge T \neq S .$$

Si verifica facilmente come qualunque insieme risulti sempre incluso
nell'insieme universo, e come analogamente l'insieme vuoto risulti sempre
incluso in qualunque insieme:

$$ \forall S \subseteq \Omega \ \{\} \subseteq S \subseteq \Omega ,$$

e questa relazione continua a valere se si considera la relazione di inclusione
in senso stretto, a patto che $S$ sia diverso dall'insieme vuoto (affinché
valga la prima parte della relazione) e dall'insieme universo (affinché possa
valere la sua seconda parte).
