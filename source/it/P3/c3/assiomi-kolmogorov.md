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

(sec_assiomi-kolmogorov)=
# Assiomi di Kolmogorov 

Nel paragrafo precedente ho introdotto le algebre degli eventi, anticipando che
esse costituiscono il dominio di una funzione che associa a ciascun evento un
valore numerico, rappresentante la sua probabilità. L'approccio didattico
comunemente adottato per definire questa funzione opera in modo indiretto.
Invece di procedere in modo operativo, rifacendosi a una delle possibili
interpretazioni del concetto di probabilità (vedi il
{ref}`sec_concetto-probabilita`), si preferisce partire da una domanda più
generale: quali proprietà vanno rispettate quando si associa un numero a un
evento, se tale valore deve essere interpretato, in modo coerente e non
ambiguo, come una probabilità? La risposta a questa domanda è fornita dal
sistema assiomatico proposto da Andrej Nikolaevič Kolmogorov[^kolmogorov] nel
1933, che costituisce ancora oggi il fondamento della teoria della probabilità
moderna. 


```{figure} https://upload.wikimedia.org/wikipedia/commons/4/43/Andrej_Nikolajewitsch_Kolmogorov.jpg
---
figclass: margin
name: fig_kolmogorov
width: 200px
align: left
---
Ritratto di Andrej Nikolaevič Kolmogorov (Fotografia di Konrad Jacobs, © Mathematisches Forschungsinstitut Oberwolfach (MFO). Licenza CC BY-SA 2.0 DE. Fonte: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Andrej_Nikolajewitsch_Kolmogorov.jpg)).
```
````{prf:definition} Assiomi di Kolmogorov
:label: def-assiomi-kolmogorov
Dato uno spazio degli esiti $\Omega$ su cui è definita un'algebra $\mathsf A$,
una _funzione di probabilità_ è qualsiasi funzione
$\mathbb P: \mathsf A \rightarrow \mathbb R$ che soddisfa i seguenti
_assiomi di Kolmogorov_:

1. la probabilità associata a un evento è sempre non negativa:
   ```{math}
   :label: kolmogorov-axiom-1
   \forall E \in \mathsf A \quad \mathbb P(E) \geq 0,
   ```
2. la probabilità associata allo spazio degli esiti è uguale a $1$:
   ```{math}
   :label: kolmogorov-axiom-2
   \mathbb P(\Omega) = 1,
   ```
3. la probabilità associata all'unione di due eventi disgiunti è uguale alla
   somma delle probabilità associate ai due eventi:
   ```{math}
   :label: kolmogorov-axiom-3
   \forall E, F \in \mathsf A \quad E \cap F = \varnothing \rightarrow
   \mathbb P(E \cup F) = \mathbb P(E) + \mathbb P(F).
   ```

Nel caso in cui $\mathsf A$ sia una sigma-algebra, quest'ultimo assioma si
estende a ogni successione infinita di eventi:

```{math}
:label: kolmogorov-axiom-3-sigma-algebra
\forall E_1, E_2, \ldots \in \mathsf A
\quad (\forall i \neq j \; E_i \cap E_j = \varnothing)
\rightarrow \mathbb P \left( \bigcup_{i=1}^{+\infty} E_i \right)
= \sum_{i=1}^{+\infty} \mathbb P (E_i).
```

La terna $(\Omega, \mathsf A, \mathbb P)$ viene detta _spazio di probabilità_.

````

Grazie agli assiomi di Kolmogorov, $\mathbb P$ viene caratterizzata
esclusivamente attraverso le proprietà formali che essa deve rispettare:
qualunque funzione che soddisfi tali proprietà è una funzione di probabilità,
indipendentemente dal _significato_ che viene dato al concetto stesso di
probabilità, garantendo al contempo che agli eventi vengano assegnate delle
probabilità secondo uno schema _coerente_.

A partire da questi assiomi è possibile derivare, per via puramente deduttiva,
un insieme di teoremi di carattere generale, la cui validità è indipendente
dall'interpretazione che si attribuisce al concetto di probabilità.

````{prf:theorem} Probabilità dell'evento complementare
:label: probabilita-evento-complementare

```{math}
\forall E \subseteq \Omega \quad \mathbb P(\overline E) = 1 - \mathbb P(E).
```
````
````{admonition} _
:class: myproof

Dato un generico $E \subseteq \Omega$, si ha $E \cup \overline E = \Omega$ e
$E \cap \overline E = \varnothing$, pertanto

```{math}
1 = \mathbb P(\Omega) = \mathbb P(E \cup \overline E)
  = \mathbb P(E) + \mathbb P(\overline E),
```
dove il primo e l'ultimo passaggio sono basati sul secondo e terzo assioma di
Kolmogorov, rispettivamente. La tesi si ottiene ricavando
$\mathbb P(\overline E)$.

````


````{prf:corollary} Probabilità dell'evento impossibile
:label: probabilita-evento-impossibile

```{math}
\mathbb P(\varnothing) = 0
```
````
````{admonition} _
:class: myproof

La tesi si ottiene dal {prf:ref}`probabilita-evento-complementare`,
quando $E = \Omega$.
````

````{prf:theorem} Probabilità dell'unione di eventi
:label: probabilita-unione-eventi

```{math}
\forall E, F \subseteq \Omega \quad \mathbb P(E \cup F) =
\mathbb P(E) + \mathbb P(F) - \mathbb P(E \cap F).
```
````
````{admonition} _
:class: myproof

Per la distributività dell'intersezione rispetto all'unione si ha

```{math}
(E \cap \overline F) \cup (E \cap F) = E \cap (\overline F \cup F)
= E \cap \Omega = E,
```

inoltre sfruttando le proprietà di associatività, commutatività
e idempotenza si ottiene

```{math}
(E \cap \overline F) \cap (E \cap F) =
(E \cap E) \cap (F \cap \overline F) = E \cap \varnothing = \varnothing.
```

Per il terzo assioma di Kolmogorov, si ha dunque
$\mathbb P(E) = \mathbb P(E \cap \overline F) + \mathbb P (E \cap F)$, e in
modo analogo si dimostra che
$\mathbb P(F) = \mathbb P(\overline E \cap F) + \mathbb P (E \cap F)$, che
equivale a
$\mathbb P(\overline E \cap F) = \mathbb P(F) - \mathbb P (E \cap F)$ (vedi
{numref}`fig_venn-union-theorem`).


Si verifica facilmente che $E \cap \overline F$, $E \cap F$ e
$\overline E \cap F$ sono a due a due disgiunti e che la loro unione coincide
con $E \cup F$, pertanto per l'estensione del terzo assioma di Kolmogorov
all'unione di tre insiemi disgiunti si ha

```{math}
\mathbb P(E \cup F) =
\underbrace{\mathbb P(E \cap \overline F) + \mathbb P(E \cap F)}_{\mathbb P(E)}
+
\underbrace{\mathbb P(\overline E \cap F)}_{\mathbb P(F) - \mathbb P(E \cap F)}
```
da cui segue la tesi.
````



```{code-cell} python
:tags:  [hide-input]

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib_venn import venn2_circles, venn2

venn_set_edge = '#333333'
background_color = '#eaf3f5'
font_size = 7



# Three distinct blue shades
color_E_only    = '#AED6F1'  # light blue  → E \ F  (region '10')
color_intersect = '#2E86C1'  # medium blue → E ∩ F  (region '11')
color_F_only    = '#1A5276'  # dark blue   → F \ E  (region '01')

fig, ax = plt.subplots()

# Set both the axes and figure background
ax.set_facecolor(background_color)
fig.patch.set_facecolor(background_color)

# Rectangle for the universal set Ω
r = patches.Rectangle((-0.75, -0.6), 1.5, 1.1,
                       edgecolor=venn_set_edge,
                       facecolor=background_color, alpha=1, lw=0.7)
ax.add_patch(r)

v = venn2(subsets=(3, 3, 1), set_labels=(r'$E$', r'$F$'), ax=ax)
c = venn2_circles(subsets=(3, 3, 1), ax=ax)

for l in v.set_labels:
    l.set_fontsize(font_size)

for contour in c:
    contour.set_lw(0.7)
    contour.set_edgecolor(venn_set_edge)

# Color each region with a distinct blue shade
v.get_patch_by_id('10').set_color(color_E_only)     # E \ F
v.get_patch_by_id('10').set_alpha(1)

v.get_patch_by_id('11').set_color(color_intersect)  # E ∩ F
v.get_patch_by_id('11').set_alpha(1)

v.get_patch_by_id('01').set_color(color_F_only)     # F \ E
v.get_patch_by_id('01').set_alpha(1)

v.get_label_by_id('10').set_text(r'$E \cap \overline{F}$')
v.get_label_by_id('10').set_fontsize(font_size)

v.get_label_by_id('11').set_text(r'$E \cap F$')
v.get_label_by_id('11').set_fontsize(font_size)

v.get_label_by_id('01').set_text(r'$\overline{E} \cap F$')
v.get_label_by_id('01').set_fontsize(font_size)

ymin, ymax = ax.get_ylim()
ax.set_ylim(ymin - 0.1, ymax)
ax.text(0.55, 0.4, r'$\Omega$', fontsize=font_size)

plt.show()
```
````{customfigure}
:name: fig_venn-union-theorem

Il diagramma di Venn che illustra la scomposizione di $E \cup F$ nell'unione
disgiunta di $E \cap \overline F$, $E \cap F$ ed $\overline E \cap F$.
````

````{prf:theorem}
:label: teo_prob_sottoinsiemi

```{math}
\forall E, F \subseteq \Omega \quad E \subseteq F \rightarrow
\mathbb P(E) \leq \mathbb P(F).
```
````
````{admonition} _
:class: myproof

Siccome $F = E \cup (F \cap \overline E)$ ed $E$ e $F \cap \overline E$ sono
disgiunti, per il terzo assioma di Kolmogorov si ha
$\mathbb P(F) = \mathbb P(E) + \mathbb P(F \cap \overline E) \geq \mathbb P(E)$.
````


-----

[^kolmogorov]: Ho scelto di fare riferimento allo standard [ISO
9](https://it.wikipedia.org/wiki/Traslitterazione_scientifica_del_cirillico)
per traslitterare dall'alfabeto cirillico a quello latino, così che il nome
originale Андре́й Никола́евич Колмого́ров diventa Andrej Nikolaevič Kolmogorov.
In realtà, esistono varie forme di traslitterazione, che dipendono anche dalla
lingua di destinazione. Per questo motivo, nella letteratura e nei testi di
riferimento si possono trovare denominazioni differenti dello stesso autore:
per esempio, nel momento in cui scrivo questa nota (aprile 2026),
[Wikipedia](https://wikipedia.org) utilizza Andrey Nikolaevich Kolmogorov nella
versione in inglese, Andreï Nikolaïevitch Kolmogorov in quella francese, Andrei
Nikolajewitsch Kolmogorow in quella tedesca e Andrej Nikolaevič Kolmogorov in
quella italiana.



## Esercizi

````{exercise} ••
Sia $(\Omega, \mathsf A, \mathbb P)$ uno spazio di probabilità. Dimostrate
che vale la seguente proprietà di _sub-additività_ per la funziona di
probabilità:

```{math}
\forall E_1, \dots, E_n \quad \mathbb P \left( \bigcup_{i=1}^n E_i  \right)
\leq \sum_{i=1}^n \mathbb P(E_i) \enspace.
```

````