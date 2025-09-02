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

(sec:relazioni-tra-insiemi)=
# Relazioni tra insiemi

A partire dalla nozione di _sottoinsieme_ è possibile derivare una serie di
relazioni tra insiemi di carattere generale; più precisamente:

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

Il diagramma di Venn per due siffatti insiemi è illustrato nella
{numref}`fig:venn-sottoinsiemi`.

````{customfigure}
:name: fig:venn-sottoinsiemi

```{code-block} python
:class:  toggle-code

import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles

venn_set_color = '#00CCFF'
venn_set_edge= '#333333'
background_color = '#eaf3f5'
font_size = 9

def subset_venn():
    fig = plt.figure()

    v = venn2(subsets=(5, 0, 2), set_labels=(r'$T$', r'$S$'))
    c = venn2_circles(subsets=(5, 0, 2))
    for _ in c:
        _.set_linewidth(0.6)
        _.set_color(venn_set_color)
        _.set_alpha(0)

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

    plt.gca().set_facecolor(background_color)
    ymin, ymax = plt.gca().get_ylim()
    plt.ylim(ymin - 0.1, ymax)

    plt.text(0.47, 0.5, r'$\Omega$', fontsize=font_size)

    return fig

fig = subset_venn()
fig.show()
```

Un diagramma di Venn che illustra due insiemi $S$ e $T$ tali che
$S \subseteq T$.
````

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

Si verifica facilmente come qualunque insieme risulti sempre incluso
nell'insieme universo, e come analogamente l'insieme vuoto risulti sempre
incluso in qualunque insieme:

```{math}
\forall S \subseteq \Omega \ \{\} \subseteq S \subseteq \Omega ,
```

e questa relazione continua a valere se si considera la relazione di inclusione
in senso stretto, a patto che $S$ sia diverso dall'insieme vuoto (affinché
valga la prima parte della relazione) e dall'insieme universo (affinché possa
valere la sua seconda parte).
