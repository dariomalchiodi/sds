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

(sec:operazioni-tra-insiemi)=
# Operazioni tra insiemi

Oltre alle relazioni descritte nel paragrafo precedente, è possibile costruire
nuovi insiemi a partire da insiemi esistenti utilizzando le operazioni
descritte di seguito.

- L’_unione_ di due insiemi $S$ e $T$ è costituita dall'insieme $S \cup T$
  contenente tutti gli elementi che appartengono ad almeno uno di essi:
  ```{math}
  S \cup T = \{x \in \Omega
              \text{ tale che } x \in S \vee x \in T \} \enspace,
  ```
  come illustrato in {numref}`fig:venn-union`.

````{customfigure}
:name: fig:venn-union

```{code-block} python
:class:  toggle-code

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib_venn import venn2_circles, venn2

venn_set_color = '#00CCFF'
venn_set_edge= '#333333'
background_color = '#eaf3f5'
font_size = 9

def venn_operations(operation='union'):
    fig = plt.figure()

    if operation == 'complement':
        r = patches.Rectangle((-0.75, -0.6), 1.5, 1.1,
                              edgecolor=venn_set_edge,
                              facecolor=venn_set_color, alpha=1)
        plt.gca().add_patch(r)

    v = venn2(subsets=(3, 3, 1), set_labels=(r'$S$', r'$T$'))
    c = venn2_circles(subsets=(3, 3, 1))

    for l in v.set_labels:
        l.set_fontsize(font_size)

    for contour in c:
        contour.set_lw(1.4)
        contour.set_edgecolor(venn_set_edge)

    for area in ['01', '10', '11']:
        v.get_patch_by_id(area).set_color(venn_set_color)
        v.get_patch_by_id(area).set_alpha(1)
        txt = v.get_label_by_id(area)
        if txt:
            txt.set_text('')

    if operation == 'intersection':
        v.get_patch_by_id('10').set_color(background_color)
        v.get_patch_by_id('11').set_color(venn_set_color)
        v.get_patch_by_id('11').set_alpha(1)
        v.get_patch_by_id('01').set_color(background_color)
    elif operation == 'difference':
        v.get_patch_by_id('10').set_color(venn_set_color)
        v.get_patch_by_id('11').set_color(background_color)
        v.get_patch_by_id('01').set_color(background_color)
    elif operation == 'symdifference':
        v.get_patch_by_id('11').set_color(background_color)
    elif operation == 'complement':
        v.get_patch_by_id('10').set_color(background_color)
        v.get_patch_by_id('11').set_color(background_color)

    plt.gca().set_facecolor('white' if operation != 'complement' \
                                    else venn_set_color)

    ymin, ymax = plt.gca().get_ylim()
    plt.ylim(ymin - 0.1, ymax)
    plt.text(0.55, 0.4, r'$\Omega$', fontsize=font_size)
    return fig

fig = venn_operations()
plt.show()
```

Il diagramma di Venn che illustra l'unione tra due insiemi $S$ e $T$.
````

- L’_intersezione_ di due insiemi $S$ e $T$ (vedi
  {numref}`fig:venn-intersection`) è costituita dall'insieme $S \cap T$
  contenente tutti gli elementi comuni a $S$ e $T$:
  ```{math}
  S \cap T = \{ x \in \Omega
                  \text{ tale che } x \in S \wedge x \in T \} \enspace.
  ```

````{customfigure}
:name: fig:venn-intersection

```{code-block} python
:class:  toggle-code

fig = venn_operations('intersection')
plt.show()
```

Il diagramma di Venn che illustra l'intersezione tra due insiemi $S$ e $T$.
````

- La _differenza_ tra un insieme $S$ e un insieme $T$ è costituita dall'insieme
  $S \backslash T$ contenente tutti gli elementi di $S$ che non appartengono a
  $T$:
  ```{math}
  S \backslash T = \{ x \in \Omega
                  \text{ tale che } x \in S \wedge x \notin T \} \enspace,
  ```
  come indicato nella {numref}`fig:venn-difference`.

````{customfigure}
:name: fig:venn-difference

```{code-block} python
:class:  toggle-code

fig = venn_operations('difference')
plt.show()
```

Il diagramma di Venn che illustra la differenza tra un insieme $S$ e un insieme
$T$.
````

- La _differenza simmetrica_ tra due insiemi $S$ e $T$, esemplificata in
  {numref}`fig:venn-symdiff`, è costituita dall'insieme $S \ominus T$
  contenente tutti gli elementi che appartengono solamente a $S$ o solamente a
  $T$:
  ```{math}
  S \ominus T = \{ x \in \Omega \text{ tale che}
    ( x \in S \wedge x \notin T )
    \vee ( x \notin S \wedge x \in T) \} \enspace.
  ```

````{customfigure}
:name: fig:venn-symdiff

```{code-block} python
:class:  toggle-code

fig = venn_operations('symdifference')
plt.show()
```

Il diagramma di Venn che illustra la differenza simmetrica tra due insiemi $S$
e $T$.
````

- Il _complemento_ di un insieme $S$ è costituito dall'insieme $\overline S$
  contenente tutti gli elementi dell'insieme universo che non appartengono a
  $S$:
  ```{math}
  \overline S = \{ x \in \Omega \text{ tale che v} x \notin S \} =
  \Omega \backslash S \enspace,
  ```
  come mostrato nel diagramma in {numref}`fig:venn-complement`.

````{customfigure}
:name: fig:venn-complement

```{code-block} python
:class:  toggle-code

fig = venn_operations('complement')
plt.show()
```

Il diagramma di Venn che illustra il complemento di un insieme $S$.
````

Si verifica facilmente come le operazioni di unione e intersezione siano

- commutative: vale sempre $S \cup T = T \cup S$ e $S \cap T = T \cap S$, e
  quindi è possibile invertire due insiemi senza che cambino la loro unione o
  la loro intersezione;
- associative: $S \cup ( T \cup U ) = (S \cup T ) \cup U$ e
  $S \cap ( T \cap U ) = (S \cap T ) \cap U$, il che significa che l'ordine con
  cui vengono eseguite due unioni (o due intersezioni) è ininfluente, pertanto
  è possibile scrivere per esempio $S \cup T \cup U$ senza che l'espressione
  risultante sia ambigua.

Valgono inoltre le cosiddette _leggi di De Morgan_:

1. $\overline{\left( S \cup T \right)} = \overline S \cap \overline T$;
1. $\overline{\left( S \cap T \right)} = \overline S \cup \overline T$.

Le leggi di De Morgan ci dicono essenzialmente che è possibile "trasferire"
l'operazione di complemento dall'unione di due insiemi ai due insiemi stessi,
avendo cura di convertire l'uione in intersezione (e un'analoga operazione vale
per il complemento di un'intersezione). Dimostriamo la prima delle due leggi:
se $x \in \overline{\left( S \cup T \right)}$, per definizione di complemento
$x \notin \left( S \cup T \right)$, il che implica $x \notin S$ e $x \notin T$.
Da questo fatto si ottiene, sempre sfruttando la definizione di complemento,
che $x \in \overline S$ e $x \in \overline T$, e dunque
$x \in \overline S \cap \overline T$. Siccome non abbiamo fatto particolari
ipotesi su $x$ se non quella che fosse un elemento di $S$, abbiamo dunque
dimostrato che
$\overline{\left( S \cup T \right)} \subseteq \overline S \cap \overline T$.
Procedendo in modo inverso (cioè partendo da
$x \in \overline S \cap \overline T$) si può dimostrare che
$\overline S \cap \overline T \subseteq \overline{\left( S \cup T \right)}$,
ottenendo pertanto la prima legge di De Morgan. Un'analoga dimostrazione
permette di ottenere la seconda legge.

Valgono, infine, le seguenti relazioni tra la differenza simmetrica, l'unione,
l'intersezione e la differenza tra insiemi:

1. $S \ominus T = (S \backslash T) \cup (T \backslash S)$,
1. $S \ominus T = (S \cup T) \backslash (S \cap T)$.

Guardando il diagramma di Venn che illustra la differenza simmetrica è facile
convincersi della validità di queste due uguaglianze. Dimostriamo parzialmente
la seconda ipotizzando valida la prima, adottando la stessa tecnica utilizzata
per le leggi di De Morgan: se $x \in (S \cup T) \backslash (S \cap T)$, allora
$x \in (S \cup T)$ e $x \notin (S \cap T)$, il che implica
$(x \in S \vee x \in T) \wedge (x \notin S \cap T)$. Per la distribuzione della
disgiunzione sulla congiunzione si ottiene
$(x \in S \wedge x \notin S \cap T) \vee (x \in T \wedge x \notin S \cap T)$.
Pertanto $x \in S \backslash T \vee x \in T \backslash S$, e assumendo vera la
prima delle due relazioni si ottiene $x \in S \ominus T$.
