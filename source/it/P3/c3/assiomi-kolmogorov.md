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

````{prf:definition} Assiomi di Kolmogorov
:label: def-assiomi-kolmogorov
A partire da un fissato spazio misurabile $(\Omega, \mathsf A)$, definiamo
_funzione di probabilità_ ogni funzione
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
   \forall E, F \in \mathsf A \quad E \cap F = \{\} \rightarrow
   \mathbb P(E \cup F) = \mathbb P(E) + \mathbb P(F).
   ```

Nel caso in cui $\mathsf A$ sia una sigma-algebra, quest'ultimo assioma si
estende a ogni successione infinita di eventi:

```{math}
:label: kolmogorov-axiom-3-sigma-algebra
\forall E_1, E_2, \ldots \in \mathsf A \; (\forall i, j E_i \cap E_j = \{\})
\rightarrow \bigcup_{i=1}^{+\infty} E_i \in \mathsf A.
```

````

Gli assiomi di Kolmogorov permettono di definire la funzione di probabilità
per uno spazio misurabile (i) indipendentemente dal _significato_ che viene
dato al concetto stesso di probabilità e (ii) in modo da garantire che agli
eventi vengano assegnate delle probabilità secondo uno schema _coerente_.

Dato uno spazio misurabile $(\Omega, \mathsf A)$ e fissata una funzione di
probabilità $\mathbb P$ che soddisfa la {prf:ref}`def-assiomi-kolmogorov`,
si dice che la terna $(\Omega, \mathsf A, \mathbb P)$ rappresenta uno
_spazio di probabilità_.

````{prf:theorem} Probabilità dell'evento complementare
:label: probabilita-evento-complementare

```{math}
\forall E \subseteq \Omega \quad \mathbb P(\overline E) = 1 - \mathbb P(E).
```
````
````{admonition} _
:class: myproof

Dato un generico $E \subseteq \Omega$, si ha $E \cup \overline E = \Omega$ e
$E \cap \overline E = \{\}$, pertanto

```{math}
1 \underset{(11.2)}{=} \mathbb P(\Omega) = \mathbb P(E \cup \overline E)
   \underset{(11.3)}{=} \mathbb P(E) + \mathbb P(\overline E),
```
da cui si ottiene la tesi.

````


````{prf:corollary} Probabilità dell'evento impossibile
:label: probabilita-evento-impossibile

```{math}
\mathbb P(\{\}) = 0
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
(E \cap E) \cap (F \cap \overline F) = E \cap \{\} = \{\}.
```

Per il terzo assioma di Kolmogorov, si ha dunque
$\mathbb P(E) = \mathbb P(E \cap \overline F) + \mathbb P (E \cap F)$, e in
modo analogo si dimostra che
$\mathbb P(F) = \mathbb P(\overline E \cap F) + \mathbb P (E \cap F)$, che
equivale a
$\mathbb P(\overline E \cap F) = \mathbb P(F) - \mathbb P (E \cap F)$.
Vedi {numref}`fig_venn-union-theorem`.


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