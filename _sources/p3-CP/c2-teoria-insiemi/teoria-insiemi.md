---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib_venn import venn2_circles, venn2
from myst_nb import glue

import matplotlib
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
matplotlib.rcParams['mathtext.fontset'] = 'cm'
font_size = 18
matplotlib.rcParams['font.size'] = str(font_size)
```

# Teoria degli insiemi

## Che cos'è un insieme?

Nel 1895 Georg Cantor ha proposto una definizione che coglie particolarmente bene il concetto intuitivo di insieme {cite}`cantor-1883`: "per molteplicità o insieme intendo ogni molti che si può pensare come uno" [^citazione-cantor]. Secondo questa definizione, un insieme è essenzialmente un raggruppamento di oggetti che, sebbene tra loro distinti, sono accomunati da una qualche proprietà. Nel 1895 lo stesso Cantor riformulò la sua definizione come segue: "per 'insieme' intendiamo qualsiasi combinazione $M$ di certi oggetti $m$ ben differenziati nella nostra visione o del nostro pensiero (che sono detti 'elementi' di $M$)" {cite}`cantor-1895`. Pochi anni dopo i matematici hanno scoperto che fornire una definizione formalmente corretta di insieme richede molta più attenzione, tipicamente appoggiandosi a un approccio assiomatico {cite}`suppes`. Nonostante ciò, nel seguito faremo riferimento alle definizioni sopra indicate, e in particolare alla seconda, al fine di rendere la trattazione più semplice e più focalizzata rispetto allo scopo di questo libro. D'altronde, come ricorda Rudy Rucker, è significativo che la parola _set_ abbia la definizione più lunga tra tutte le parole che compaiono nello Oxford English Dictionary {cite}`rucker`.

## Concetti di base

In accordo con la definizione sopra riportata, nonché con la comune notazione matematica, indicheremo di norma gli insiemi utilizzando le lettere maiuscole dell'alfabeto latino e i loro elementi usando le corrispondenti lettere minuscole. Per indicare che un elemento $a$ appartiene a un insieme $A$ scriveremo $a \in A$, mentre per indicare che un elemento $b$ non appartiene all'insieme $A$ scriveremo $b \notin A$.

Un insieme può essere rappresentato:

- _estensivamente_, cioé elencando tutti i suoi elementi tramite una sequenza: per esempio l'insieme $O$ dei possibili esiti del lancio di un dado che corrispondono a un numero dispari si può indicare estensivamente come $O = \{ 1, 3, 5, 6 \}$;
- _intensivamente_, specificando una proprietà matematica valida per tutti gli elementi dell'insieme: l'insieme descritto al punto precedente ammette la descrizione intensiva

$$
O = \{ k \in \mathbb N \text{ tale che } 1 \leq k \leq 6 \text{ e } k \text{ è pari} \};
$$
- tramite un _diagramma di Venn_, indicando gli elementi come punti in una porzione di piano e racchiudendoli dentro un'ellisse: l'insieme $O$ descritto nei due punti precedenti può anche essere rappresentato tramite il diagramma di Venn illustrato in {numref}`Figura %s <venn>`.

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

venn_set_color = '#cc0000'
venn_set_edge= '#333333'

fig = plt.figure()

v = venn2(subsets=(3, 3, 0), set_labels=('$O$', ''))
c = venn2_circles(subsets=(3, 3, 0))

for l in v.set_labels:
    l.set_fontsize(font_size)

for area in ['01', '10', '11']:
    if area != '11':
        #v.get_patch_by_id(area).set_color('skyblue')
        #v.get_patch_by_id(area).set_alpha(1)
        txt = v.get_label_by_id(area)
        if txt:
            txt.set_text('')
        
v.get_patch_by_id('10').set_color(venn_set_color)
v.get_patch_by_id('10').set_alpha(1)

v.get_patch_by_id('01').set_color('white')
c[1].set_edgecolor('white')

#plt.gca().set_axis_on()
plt.gca().set_facecolor('white')

ymin, ymax = plt.gca().get_ylim()
plt.ylim(ymin - 0.1, ymax)
plt.text(-0.85, 0, '$1$', fontsize=30)
plt.text(-0.55, 0.15, '$3$', fontsize=30)
plt.text(-0.55, -0.2, '$5$', fontsize=30)
plt.show()

glue("venn-picture", fig, display=False)
```

```{glue:figure} venn-picture
:figwidth: 100%
:name: "venn"

Un semplice diagramma di Venn per descrivere l'insieme $O = \{ 1, 3, 5, 6 \}$.
```

+++

In particolare, la descrizione tramite i diagrammi di Venn presuppone la conoscenza, in linea di principio, di tutti gli elementi che potrebbero far parte di un insieme. L'insieme di tutti i possibili elementi si indica in genere con il simbolo $\Omega$ che viene chiamato _insieme universo_. Nell'esempio precedente facciamo ovviamente riferimento all'universo $\Omega = \{ 1, 2, 3, 4, 5, 6 \}$, il diagramma di Venn dell'insieme $O$ è visualizzato in modo più corretto nella {numref}`Figura %s <venn-universe>`.

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

fig = plt.figure()

v = venn2(subsets=(3, 3, 0), set_labels=('$O$', ''))
c = venn2_circles(subsets=(3, 3, 0))

for l in v.set_labels:
    l.set_fontsize(font_size)

for area in ['01', '10', '11']:
    if area != '11':
        #v.get_patch_by_id(area).set_color('skyblue')
        #v.get_patch_by_id(area).set_alpha(1)
        txt = v.get_label_by_id(area)
        if txt:
            txt.set_text('')
        
v.get_patch_by_id('10').set_color(venn_set_color)
v.get_patch_by_id('10').set_alpha(1)

v.get_patch_by_id('01').set_color('white')
c[1].set_edgecolor('white')

#plt.gca().set_axis_on()
plt.gca().set_facecolor('white')

ymin, ymax = plt.gca().get_ylim()
plt.ylim(ymin - 0.1, ymax)
plt.gca().set_facecolor('white')
plt.gca().set_axis_on()

plt.text(-0.85, 0, '$1$', fontsize=30)
plt.text(-0.55, 0.15, '$3$', fontsize=30)
plt.text(-0.55, -0.2, '$5$', fontsize=30)

plt.text(.6, .1, '$2$', fontsize=30)
plt.text(.2, -0.1, '$4$', fontsize=30)
plt.text(.5, -0.3, '$6$', fontsize=30)

plt.text(0.95, 0.35, '$\Omega$')
plt.show()

glue("venn-universe-picture", fig, display=False)
```

```{glue:figure} venn-universe-picture
:figwidth: 100%
:name: "venn-universe"

Un diagramma di Venn per descrivere l'insieme $O$ della {numref}`Figura %s <venn>` evidenziando il corrispondente insieme universo $\Omega$.
```

+++

Così come l'insieme universo è tale da contenere qualunque elemento, è matematicamente rilevante pensare ad un insieme che dualmente, non contiene alcun elemento. Tale insieme viene chiamato insieme vuoto, e lo indicheremo scrivendo $\{\}$ (anche se è comune l'uso del simbolo $\varnothing$), così che per qualsiasi elemento $a$ si avrà $a \notin \{\}$.

## Insiemi finiti e infiniti
È abbastanza facile farsi venire in mente degli insiemi che contengono un numero finito di elementi, come ad esempio l'insieme dei membri della Justice League, quello dei giorni della settimana e quello dei numeri primi minori di $100$. Diciamo che insiemi di questo tipo sono _finiti_. Esistono però anche insiemi che non contengono un numero finito di elementi, come l'insieme di tutte le frazioni, o anche l'insieme di tutti gli insiemi. Per questi insiemi _infiniti_ si distinguono due casi:

- si dice che un insieme è _infinito numerabile_ quando risulta possibile costruire una sequenza (infinita) $x_1, x_2, \dots$ che contiene in qualche posizione ognuno dei suoi elementi: l'insieme $D$ dei numeri dispari sopra introdotto è pertanto un insieme infinito numerabile;
- in tutti gli altri casi si dice che l'insieme è _infinito non numerabile:_ l'insieme dei punti di una retta e l'insieme dei numeri reali sono entrambi infiniti e non numerabili.

La modalità di descrizione estensiva non è, strettamente parlando, adottabile per gli insiemi infiniti, visto che per definizione non è possibile elencare tutti i loro elementi. Qaundo però si ha a che fare con un insieme infinito numerabile e quest'ultimo è associabile a una sequenza che si può intuitivamente continuare dopo avere visto solo alcuni tra i suoi elementi iniziali, risulta accettabile estendere la descrizione estensiva elencando solo questi elementi, aggiungendo dei punti di sospensione per enfatizzare la non finitezza dell'insieme. Ad esempio l'insieme dei numeri dispari si può indicare estensivamente come $D = \{1, 3, 5, 7, 9, ... \}$, sebbene la descrizione intensiva

$$D = \{ x \in \mathbb N \text{ tale che }
         x = 2n+1 \text{ per qualche } n \in \mathbb N \}$$

sia decisamente più precisa. Ciò non vale invece per gli insiemi infiniti non numerabili, per i quali sono generalmente utilizzabili sono descrizioni di tipo intensivo.

## Relazioni tra insiemi

A partire dalla nozione di _sottoinsieme_ è possibile derivare una serie di relazioni tra insiemi di carattere generale; più precisamente:

- quando ogni elemento sappartenente a un insieme $S$ risulta appartenente anche a un secondo insieme $T$, si dice che $S$ è un _sottoinsieme_ di $T$ (o che $S$ è _incluso_ in $T$) e si indica questo fatto con la notazione $S \subseteq T$ (vedi {numref}`venn-subset`):

$$ S \subseteq T \leftrightarrow \forall s \in \Omega \ (s \in S \rightarrow s \in T) ;$$

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

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

plt.text(0.47, 0.5, '$\Omega$')

plt.show()

glue("venn-subset-picture", fig, display=False)
```

```{glue:figure} venn-subset-picture
:figwidth: 100%
:name: "venn-subset"

Un diagramma di Venn per descrivere due insiemi $S$ e $T$ tali che $S \subseteq T$.
```

+++

- due insiemi si dicono uguali quando si includono mutuamente:

$$ S = T \leftrightarrow S \subseteq T \wedge T \subseteq S ;$$

- due insiemi si dicono diversi quando non sono uguali;

- tra due insiemi sussiste la relazione di inclusione _in senso stretto_ quando uno dei due è incluso nell'altro e in aggiunta i due insiemi non sono uguali:

$$ S \subset T \leftrightarrow S \subseteq T \wedge T \neq S .$$

Si verifica facilmente come qualunque insieme risulti sempre incluso nell'insieme universo, e come analogamente l'insieme vuoto risulti sempre incluso in qualunque insieme:

$$ \forall S \subseteq \Omega \ \{\} \subseteq S \subseteq \Omega ,$$

e questa relazione continua a valere se si considera la relazione di inclusione in senso stretto, a patto che $S$ sia diverso dall'insieme vuoto (affinché valga la prima parte della relazione) e dall'insieme universo (affinché possa valere la sua seconda parte).

+++

## Operazioni tra insiemi

Oltre alle relazioni descritte nel paragrafo precedente, è possibile costruire nuovi insiemi a partire da insiemi esistenti utilizzando le operazioni descritte di seguito.

- L'_unione_ di due insiemi $S$ e $T$ (vedi {numref}`venn-union`) è costituita dall'insieme $S \cup T$ contenente tutti gli elementi che appartengono ad almeno uno di essi:

$$ S \cup T = \{x \in \Omega | x \in S \vee x \in T \} .$$

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

fig = plt.figure()

v = venn2(subsets=(3, 3, 1), set_labels=('$S$', '$T$'))
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

plt.gca().set_facecolor('white')
plt.gca().set_axis_on()
ymin, ymax = plt.gca().get_ylim()
plt.ylim(ymin - 0.1, ymax)
plt.text(0.7, 0.43, '$\Omega$')
plt.show()

glue("venn-union-picture", fig, display=False)
```

```{glue:figure} venn-union-picture
:figwidth: 100%
:name: "venn-union"

Un diagramma di Venn per descrivere l'unione degli insiemi $S$ e $T$.
```

+++

- L'_intersezione_ di due insiemi $S$ e $T$ (vedi {numref}`venn-intersection`) è costituita dall'insieme $S \cap T$ contenente tutti gli elementi comuni a $S$ e $T$:

$$ S \cap T = \{ x \in \Omega | x \in S \wedge x \in T \} .$$

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

fig = plt.figure()

v = venn2(subsets=(3, 3, 1), set_labels=('$S$', '$T$'))
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

v.get_patch_by_id('10').set_color('white')
v.get_patch_by_id('11').set_color(venn_set_color)
v.get_patch_by_id('11').set_alpha(1)
v.get_patch_by_id('01').set_color('white')

plt.gca().set_facecolor('white')
plt.gca().set_axis_on()
plt.text(0.7, 0.43, '$\Omega$')
ymin, ymax = plt.gca().get_ylim()
plt.ylim(ymin - 0.1, ymax)
plt.show()

glue("venn-intersection-picture", fig, display=False)
```

```{glue:figure} venn-intersection-picture
:figwidth: 100%
:name: "venn-intersection"

Un diagramma di Venn per descrivere l'intersezione degli insiemi $S$ e $T$.
```

+++

- La _differenza_ tra un insieme $S$ e un insieme $T$ (vedi {numref}`venn-difference` è costituita dall'insieme $S \backslash T$ contenente tutti gli elementi di $S$ che non appartengono a $T$:

$$ S \backslash T = \{ x \in \Omega | x \in S \wedge x \notin T \} .$$

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

fig = plt.figure()

v = venn2(subsets=(3, 3, 1), set_labels=('$S$', '$T$'))
c = venn2_circles(subsets=(3, 3, 1))

for l in v.set_labels:
    l.set_fontsize(font_size)

for contour in c:
    contour.set_lw(1.4)
    contour.set_edgecolor(venn_set_edge)

v.get_patch_by_id('10').set_color('white')
v.get_patch_by_id('11').set_color(venn_set_color)
v.get_patch_by_id('11').set_alpha(.5)
v.get_patch_by_id('01').set_color('white')


for area in ['01', '10', '11']:
    color = venn_set_color if area == '10' else "white"
    v.get_patch_by_id(area).set_color(color)
    v.get_patch_by_id(area).set_alpha(1)
    txt = v.get_label_by_id(area)
    if txt:
        txt.set_text('')

plt.gca().set_facecolor('white')
plt.gca().set_axis_on()
plt.text(0.7, 0.43, '$\Omega$')
ymin, ymax = plt.gca().get_ylim()
plt.ylim(ymin - 0.1, ymax)
plt.show()

glue("venn-difference-picture", fig, display=False)
```

```{glue:figure} venn-difference-picture
:figwidth: 100%
:name: "venn-difference"

Un diagramma di Venn per descrivere la differenza tra l'insieme $S$ e l'insieme $T$.
```

+++

- La _differenza simmetrica_ tra due insiemi $S$ e $T$ (vedi {numref}`venn-symm-difference`) è costituita dall'insieme $S \ominus T$ contenente tutti gli elementi che appartengono solamente a $S$ o solamente a $T$:

$$ S \ominus T = \{ x \in \Omega | ( x \in S \wedge x \notin T ) \vee ( x \notin S \wedge x \in T) \} .$$

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

fig = plt.figure()

v = venn2(subsets=(3, 3, 1), set_labels=('$S$', '$T$'))
c = venn2_circles(subsets=(3, 3, 1))

for l in v.set_labels:
    l.set_fontsize(font_size)

for contour in c:
    contour.set_lw(1.4)
    contour.set_edgecolor(venn_set_edge)


for area in ['01', '10', '11']:
    color = venn_set_color if area != '11' else "white"
    v.get_patch_by_id(area).set_color(color)
    v.get_patch_by_id(area).set_alpha(1)
    txt = v.get_label_by_id(area)
    if txt:
        txt.set_text('')

plt.gca().set_facecolor('white')
plt.gca().set_axis_on()
plt.text(0.7, 0.43, '$\Omega$')
ymin, ymax = plt.gca().get_ylim()
plt.ylim(ymin - 0.1, ymax)
plt.show()

glue("venn-symm-difference-picture", fig, display=False)
```

```{glue:figure} venn-symm-difference-picture
:figwidth: 100%
:name: "venn-symm-difference"

Un diagramma di Venn per descrivere la differenza simmetrica degli insiemi $S$ e $T$.
```

+++

- Il _complemento_ di un insieme $S$ è costituito dall'insieme $\overline S$ (vedi {numref}`venn-complement`) contenente tutti gli elementi dell'insieme universo che non appartengono a $S$:

$$ \overline S = \{ x \in \Omega | x \notin S \} = \Omega \backslash S. $$

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

fig = plt.figure()

v = venn2(subsets=(3, 3, 1), set_labels=('$S$', '$T$'))
c = venn2_circles(subsets=(3, 3, 1))

for l in v.set_labels:
    l.set_fontsize(font_size)

for contour in c:
    contour.set_lw(1.4)
    contour.set_edgecolor(venn_set_edge)

for area in ['01', '10', '11']:
    color = venn_set_color if area == '01' else "white"
    v.get_patch_by_id(area).set_color(color)
    v.get_patch_by_id(area).set_alpha(1)
    txt = v.get_label_by_id(area)
    if txt: txt.set_text('')

plt.gca().set_axis_on()
plt.text(0.7, 0.43, '$\Omega$')
plt.gca().set_facecolor(venn_set_color)
ymin, ymax = plt.gca().get_ylim()
plt.ylim(ymin - 0.1, ymax)
plt.show()

glue("venn-complement-picture", fig, display=False)
```

```{glue:figure} venn-complement-picture
:figwidth: 100%
:name: "venn-complement"

Un diagramma di Venn per descrivere il complemento dell'insieme $S$.
```

+++

Si verifica facilmente come le operazioni di unione e intersezione siano

- commutative: vale sempre $S \cup T = T \cup S$ e $S \cap T = T \cap S$, e quindi è possibile invertire due insiemi senza che cambino la loro unione o la loro intersezione;
- associative: $S \cup ( T \cup U ) = (S \cup T ) \cup U$ e $S \cap ( T \cap U ) = (S \cap T ) \cap U$, il che significa che l'ordine con cui vengono eseguite due unioni (o due intersezioni) è ininfluente, pertanto è possibile scrivere per esempio $S \cup T \cup U$ senza che l'espressione risultante sia ambigua.

Valgono inoltre le cosiddette _leggi di De Morgan_:

1. $\overline{\left( S \cup T \right)} = \overline S \cap \overline T$;
1. $\overline{\left( S \cap T \right)} = \overline S \cup \overline T$.

Le leggi di De Morgan ci dicono essenzialmente che è possibile "trasferire" l'operazione di complemento dall'unione di due insiemi ai due insiemi stessi, avendo cura di convertire l'uione in intersezione (e un'analoga operazione vale per il complemento di un'intersezione). Dimostriamo la prima delle due leggi: se $x \in \overline{\left( S \cup T \right)}$, per definizione di complemento $x \notin \left( S \cup T \right)$, il che implica $x \notin S$ e $x \notin T$. Da questo fatto si ottiene, sempre sfruttando la definizione di complemento, che $x \in \overline S$ e $x \in \overline T$, e dunque $x \in \overline S \cap \overline T$. Siccome non abbiamo fatto particolari ipotesi su $x$ se non quella che fosse un elemento di $S$, abbiamo dunque dimostrato che $\overline{\left( S \cup T \right)} \subseteq \overline S \cap \overline T$. Procedendo in modo inverso (cioè partendo da $x \in \overline S \cap \overline T$) si può dimostrare che $\overline S \cap \overline T \subseteq \overline{\left( S \cup T \right)}$, ottenendo pertanto la prima legge di De Morgan. Un'analoga dimostrazione permette di ottenere la seconda legge.

Valgono, infine, le seguenti relazioni tra la differenza simmetrica, l'unione, l'intersezione e la differenza tra insiemi:

1. $S \ominus T = (S \backslash T) \cup (T \backslash S)$,
1. $S \ominus T = (S \cup T) \backslash (S \cap T)$.

Guardando il diagramma di Venn della {numref}`venn-symm-difference` è facile convincersi della validità di queste due uguaglianze. Dimostriamo parzialmente la seconda ipotizzando valida la prima, adottando la stessa tecnica utilizzata per le leggi di De Morgan: se $x \in (S \cup T) \backslash (S \cap T)$, allora $x \in (S \cup T)$ e $x \notin (S \cap T)$, il che implica $(x \in S \vee x \in T) \wedge (x \notin S \cap T)$. Per la distribuzione della disgiunzione sulla congiunzione si ottiene $(x \in S \wedge x \notin S \cap T) \vee (x \in T \wedge x \notin S \cap T)$. Pertanto $x \in S \backslash T \vee x \in T \backslash S$, e assumendo vera la prima delle due relazioni si ottiene $x \in S \ominus T$.

+++

## Gli insiemi in Python

+++

[^citazione-cantor]: Traduzione dal testo originale "Unter einer 'Mannigfaltigkeit' oder 'Menge' verstee ich nämlich allgemein jedes Viele, welches sich als Eines denken lässt".
