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

(sec_set-operations)=
# Set operations

Beyond the relations described in the previous section, it is possible to
construct new sets from existing ones using the operations described below.

- The _union_ of two sets $S$ and $T$ is the set $S \cup T$ of all elements
  that belong to at least one of them. Formally,
  $S \cup T = \{x \in \Omega \mid x \in S \vee x \in T \}$.
- The _intersection_ of two sets $S$ and $T$ is the set $S \cap T$ of
  elements common to both:
  $S \cap T = \{ x \in \Omega \mid x \in S \wedge x \in T \}$.
- The _difference_ between a set $S$ and a set $T$ is the set $S \setminus T$
  of elements of $S$ that do not belong to $T$:
  $S \setminus T = \{ x \in \Omega \mid x \in S \wedge x \notin T \}$.
- The _symmetric difference_ between two sets $S$ and $T$ is the set
  $S \ominus T$ of elements belonging to exactly one of the two sets:
  $S \ominus T = \{ x \in \Omega \mid ( x \in S \wedge x \notin T )
  \vee ( x \notin S \wedge x \in T) \}$.
- The _complement_ of a set $S$ is the set $\overline S$ of elements of the
  universe that do not belong to $S$:
  $\overline S = \{ x \in \Omega \mid x \notin S \} = \Omega \setminus S$.


```{code-cell} python
:tags:  [hide-input]

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch

MATH_SIZE = 9
TEXT_SIZE = 7
EDGE_COLOR = '#333333'
BG_COLOR   = '#eaf3f5'
FILL_COLOR = '#d6e4f7'
HIGHLIGHT  = '#aac5e8'
DOT_COLOR  = '#2255aa'

O_XY = (5, 3.7); O_W, O_H = 5.5, 4.8
V_XY = (7.8, 4.0); V_W, V_H = 4.5, 3.8

ELEMS_O   = [('Captain\nAmerica', 3.0, 4.5,  1.0,  0.),
             ('Hulk',             3.5, 2.8,  0.65, 0.0)]
ELEMS_OV  = [('Thor',             6.2, 4.2,  0.75, 0.0)]
ELEMS_V   = [('Iron\nMan',        9.3, 4.5,  -0.6,  0.)]
ELEMS_OUT = [('Black\nWidow',     1.2, 7.0,  0, -0.6),
             ('Hawkeye',         10.8, 1.5, -0.85, -0.4)]
ELEMS_COMPLEMENT = [('Ant-Man',      10.5, 6.5, -0.85, -0.4)]

def _setup_ax(ax, s=1, box_fill=None, labels=True):
    ax.set_facecolor(BG_COLOR)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.add_patch(FancyBboxPatch((0.2, 0.2), 11.6, 7.6,
                               boxstyle='square,pad=0',
                               facecolor=box_fill or BG_COLOR, edgecolor=EDGE_COLOR,
                               linewidth=1.1 * s, zorder=0))
    ax.text(11.5, 7.5, r'$\Omega$', fontsize=MATH_SIZE * s, ha='right', va='top')
    if labels:
        ax.text( 3, 6.3, r'$O$', fontsize=MATH_SIZE * s, va='top')
        ax.text(9, 6.2, r'$V$',  fontsize=MATH_SIZE * s, va='top')

def _add_borders(ax, s=1):
    for xy, w, h in [(O_XY, O_W, O_H), (V_XY, V_W, V_H)]:
        ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                             facecolor='none', edgecolor=EDGE_COLOR,
                             linewidth=1.2 * s, zorder=4))

def _add_elements(ax, s=1):
    for name, x, y, xof, yof in ELEMS_O + ELEMS_OV + ELEMS_V + ELEMS_OUT:
        ax.plot(x, y, 'o', markersize=4 * s, color=DOT_COLOR, zorder=5)
        ax.text(x + xof, y + yof, name, ha='center', va='center',
                fontsize=TEXT_SIZE * s, zorder=6)

def _fill_intersection(ax, color):
    """Highlight O ∩ V by clipping a filled O ellipse to V."""
    clip = Ellipse(xy=V_XY, width=V_W, height=V_H,
                   facecolor='none', edgecolor='none')
    ax.add_patch(clip)
    hl = Ellipse(xy=O_XY, width=O_W, height=O_H,
                 facecolor=color, edgecolor='none', zorder=2)
    ax.add_patch(hl)
    hl.set_clip_path(clip)

def venn_union(ax, s=1):
    _setup_ax(ax, s)
    for xy, w, h in [(O_XY, O_W, O_H), (V_XY, V_W, V_H)]:
        ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                             facecolor=HIGHLIGHT, edgecolor='none', zorder=1))
    _add_borders(ax, s)
    _add_elements(ax, s)

def venn_intersection(ax, s=1):
    _setup_ax(ax, s)
    for xy, w, h in [(O_XY, O_W, O_H), (V_XY, V_W, V_H)]:
        ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                             facecolor=FILL_COLOR, edgecolor='none', zorder=1))
    _fill_intersection(ax, HIGHLIGHT)
    _add_borders(ax, s)
    _add_elements(ax, s)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.8, 4.8), facecolor=BG_COLOR)
venn_union(ax1, s=2)
venn_intersection(ax2, s=2)
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_en-venn-union-intersection

Venn diagrams for the union $O \cup V$ (left) and the intersection
$O \cap V$ (right), where $O$ is the set of Avengers with superhuman strength
and $V$ is the set of Avengers who can fly. In both cases, the darker blue
region describes the set of interest and the lighter region indicates the
parts of $O$ or $V$ that do not belong to it.
````

````{prf:example}
:label: ex-en-set-operations

Consider the universe $\Omega$ of all Avengers, and define within it the sets
$O = \{\text{Captain America}, \text{Hulk}, \text{Thor}\}$ and
$V = \{\text{Thor}, \text{Iron Man}\}$, containing respectively the Avengers
with superhuman strength and those who can fly.
{numref}`fig_en-venn-union-intersection` shows the Venn diagrams of
- $O \cup V = \{\text{Captain America}, \text{Hulk}, \text{Thor},
\text{Iron Man}\}$, which includes all the heroes considered, and
- $O \cap V = \{\text{Thor}\}$, containing the only Avenger with superhuman
  strength who can also fly.

Similarly, {numref}`fig_en-venn-difference` illustrates the difference
$O \setminus V = \{\text{Captain America}, \text{Hulk}\}$ of all super-strong
heroes who cannot fly, and the symmetric difference
$O \ominus V = \{\text{Captain America}, \text{Hulk}, \text{Iron Man}\}$,
from which Thor is excluded because he belongs to both sets. It is important
to note that set difference is not symmetric: a simple counterexample is the
fact that $V \setminus O = \{\text{Iron Man}\} \neq O \setminus V$.

Finally, the complement $\overline O$ corresponds to the set of Avengers
without superhuman strength: Iron Man, Black Widow, Hawkeye, and Ant-Man, as
illustrated in {numref}`fig_en-venn-complement`.
````

```{code-cell} python
:tags:  [hide-input]

def venn_difference(ax, s=1):
    _setup_ax(ax, s)
    ax.add_patch(Ellipse(xy=O_XY, width=O_W, height=O_H,
                         facecolor=HIGHLIGHT, edgecolor='none', zorder=1))
    ax.add_patch(Ellipse(xy=V_XY, width=V_W, height=V_H,
                         facecolor=FILL_COLOR, edgecolor='none', zorder=2))
    _add_borders(ax, s)
    _add_elements(ax, s)

def venn_symdiff(ax, s=1):
    _setup_ax(ax, s)
    for xy, w, h in [(O_XY, O_W, O_H), (V_XY, V_W, V_H)]:
        ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                             facecolor=HIGHLIGHT, edgecolor='none', zorder=1))
    _fill_intersection(ax, FILL_COLOR)
    _add_borders(ax, s)
    _add_elements(ax, s)

fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.8, 4.8), facecolor=BG_COLOR)
venn_difference(ax1, s=2)
venn_symdiff(ax2, s=2)
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_en-venn-difference

Venn diagrams for the difference $O \setminus V$ (left) and the symmetric
difference $O \ominus V$ (right). Same notation as in
{numref}`fig_en-venn-union-intersection`.
````



```{code-cell} python
:tags:  [hide-input]

def venn_complement(ax, s=1):
    _setup_ax(ax, s, box_fill=HIGHLIGHT, labels=False)
    ax.text(3.5, 6.7, r'$O$', fontsize=MATH_SIZE * s, va='top')
    ax.add_patch(Ellipse(xy=O_XY, width=O_W, height=O_H,
                         facecolor=FILL_COLOR, edgecolor=EDGE_COLOR,
                         linewidth=1.2 * s, zorder=1))
    for name, x, y, xof, yof in ELEMS_O + ELEMS_OV:
        ax.plot(x, y, 'o', markersize=4 * s, color=DOT_COLOR, zorder=4)
        ax.text(x + xof, y + yof, name, ha='center', va='center',
                fontsize=TEXT_SIZE * s, zorder=5)
    for name, x, y, xof, yof in ELEMS_V + ELEMS_OUT + ELEMS_COMPLEMENT:
        ax.plot(x, y, 'o', markersize=4 * s, color=DOT_COLOR, zorder=4)
        ax.text(x + xof, y + yof, name, ha='center', va='center',
                fontsize=TEXT_SIZE * s, zorder=5)

fig3, ax = plt.subplots(facecolor=BG_COLOR)
venn_complement(ax)
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_en-venn-complement

Venn diagram for the complement $\overline O$: the highlighted region
contains all Avengers that do not belong to $O$. Same notation as in
{numref}`fig_en-venn-union-intersection`.
````

It is straightforward to verify that union and intersection are

- commutative: $S \cup T = T \cup S$ and $S \cap T = T \cap S$ always hold,
  so the two sets can be swapped while leaving their union and intersection
  unchanged;
- associative: $S \cup ( T \cup U ) = (S \cup T ) \cup U$ and
  $S \cap ( T \cap U ) = (S \cap T ) \cap U$, meaning that the order in
  which two unions (or two intersections) are performed is immaterial, so one
  can write for example $S \cup T \cup U$ without ambiguity;
- distributive over each other: $S \cup (T \cap U) = (S \cup T) \cap (S \cup U)$
  and $S \cap (T \cup U) = (S \cap T) \cup (S \cap U)$, in analogy with the
  distribution of multiplication over addition in arithmetic (where
  $a \cdot (b + c) = a \cdot b + a \cdot c$ holds), with the difference that
  here the property holds in both directions.

````{prf:theorem} De Morgan's laws
:label: teo-en-de-morgan

For every pair of sets $S, T \subseteq \Omega$, _De Morgan's laws_ hold:

1. $\overline{\left( S \cup T \right)} = \overline S \cap \overline T$;
2. $\overline{\left( S \cap T \right)} = \overline S \cup \overline T$.
````
````{admonition} _
:class: myproof

We prove the first law. Fix $x \in \overline{\left( S \cup T \right)}$; by
definition of complement, $x \notin \left( S \cup T \right)$, which implies
$x \notin S$ and $x \notin T$. Using the definition of complement again, we
obtain $x \in \overline S$ and $x \in \overline T$, and hence
$x \in \overline S \cap \overline T$. Since no assumption on $x$ was made
other than $x \in \overline{(S \cup T)}$, we have shown that
$\overline{\left( S \cup T \right)} \subseteq \overline S \cap \overline T$.
Proceeding in the reverse direction (starting from
$x \in \overline S \cap \overline T$) one can show that
$\overline S \cap \overline T \subseteq \overline{\left( S \cup T \right)}$,
yielding the first De Morgan law. The second law is proved analogously.
````

De Morgan's laws tell us essentially that the complement operation can be
«transferred» from the union of two sets to the two sets individually, taking
care to convert the union into an intersection (and the analogous operation
holds for the complement of an intersection).

The following relations also connect symmetric difference, union, intersection,
and set difference.

````{prf:theorem}
:label: teo-en-set-difference

Given two sets $S, T \subseteq \Omega$:

1. $S \ominus T = (S \setminus T) \cup (T \setminus S)$,
2. $S \ominus T = (S \cup T) \setminus (S \cap T)$.
````
````{admonition} _
:class: myproof

The first relation follows directly from the definition of symmetric
difference: indeed, for every $x \in \Omega$,

```{math}
x \in S \ominus T \leftrightarrow
(x \in S \wedge x \notin T) \vee (x \notin S \wedge x \in T) \leftrightarrow
(x \in S \setminus T) \vee (x \in T \setminus S) \leftrightarrow
x \in (S \setminus T) \cup (T \setminus S) \enspace.
```

For the second relation, suppose $x \in (S \cup T) \setminus (S \cap T)$;
then $x \in (S \cup T)$ and $x \notin (S \cap T)$, which implies
$(x \in S \vee x \in T) \wedge (x \notin S \cap T)$. Distributing the
disjunction over the conjunction gives
$(x \in S \wedge x \notin S \cap T) \vee (x \in T \wedge x \notin S \cap T)$.
Therefore $x \in S \setminus T \vee x \in T \setminus S$, and the first
relation just proved implies $x \in S \ominus T$. Hence
$(S \cup T) \setminus (S \cap T) \subseteq S \ominus T$. Proceeding
analogously one shows $S \ominus T \subseteq (S \cup T) \setminus (S \cap T)$,
which gives the claim.
````

Union and intersection allow us to introduce the _partition_ of a set, meaning
a decomposition of it into non-overlapping parts.

````{prf:definition} Partition
:label: def-en-partition

A _partition_ of a set $S$ is a family
$\mathcal{P} = \{ P_1, P_2, \ldots, P_k \}$ of non-empty subsets of $S$,
called _blocks_ or _classes_, such that:

1. $P_i \cap P_j = \varnothing$ for every $i \neq j$ (the blocks do not
   overlap);
2. $\cup_{i=1}^k P_i = S$ (the blocks cover $S$).
````

In other words, a partition assigns every element of $S$ to exactly one class:
each element belongs to one and only one block. An immediate consequence of
the definition is that two distinct blocks $P_i$ and $P_j$ cannot share an
element.

````{prf:example}
:label: ex-en-partitions

Consider the set of Avengers in their original line-up:
$S = \{ \text{Captain America}, \text{Hulk}, \text{Thor},
\text{Iron Man}, \text{Black Widow}, \text{Hawkeye} \}$.

- The family
  $\mathcal{P}_1 = \bigl\{
  \{\text{Captain America}, \text{Iron Man}\},\,
  \{\text{Hulk}, \text{Thor}\},\,
  \{\text{Black Widow}, \text{Hawkeye}\}
  \bigr\}$
  is a partition of $S$: the three blocks are disjoint and together cover
  all heroes.

- In contrast, the family
  $\mathcal{P}_2 = \bigl\{
  \{\text{Captain America}, \text{Hulk}, \text{Thor}\},\,
  \{\text{Thor}, \text{Iron Man}, \text{Black Widow}, \text{Hawkeye}\}
  \bigr\}$
  is not a partition of $S$, because Thor appears in both blocks.

- Similarly,
  $\mathcal{P}_3 = \bigl\{
  \{\text{Captain America}, \text{Thor}, \text{Iron Man}\},\,
  \{\text{Hulk}, \text{Black Widow}\}
  \bigr\}$
  is not a partition of $S$, because Hawkeye does not belong to any block.
````

A set $S$ always admits two trivial partitions: the one consisting of a single
block $\{S\}$, and the one in which every block is a singleton,
$\bigl\{ \{s\} \mid s \in S \bigr\}$. Finally, a partition of $S$ into two
blocks is closely related to the complement operation: if $A \subseteq S$ is
a non-empty subset different from $S$, then $\{A,\, S \setminus A\}$ is a
partition of $S$ into two blocks.


## Exercises

````{exercise}
:label: ex-en-sets-base

Let
```{math}
\Omega = \{ \text{Batman}, \text{Superman}, \text{Thor}, \text{Wolverine},
        \text{Deadpool}, \text{Storm}, \text{Cyborg} \} \enspace.
```
Starting from the following sets of superheroes:

```{math}
\begin{align*}
A &= \{ \text{Batman}, \text{Thor}, \text{Deadpool},
        \text{Cyborg} \} \enspace, \\
B &= \{ \text{Superman}, \text{Thor}, \text{Storm},
        \text{Wolverine} \} \enspace, \\
C &= \{ \text{Deadpool}, \text{Cyborg}, \text{Batman} \} \enspace,
\end{align*}
```

describe the following sets extensively:

1. $A \cap B$,
2. $\overline C$,
3. $A \setminus C$,
4. $A \ominus B$,
5. $\overline A \cap (B \cup C)$,
6. $A \cup (B \cap C)$,
7. $(A \cap \overline B) \cup C$,
8. $(A \cap C) \cup (B \cap C)$.
````

````{solution} ex-en-sets-base
:class: dropdown

1. $A \cap B = \{\text{Thor}\}$.
2. $\overline C = B = \{ \text{Superman}, \text{Thor}, \text{Storm},
   \text{Wolverine} \}$.
3. $A \setminus C = \{ \text{Thor} \}$.
4. $A \cup B = \Omega$ and $A \cap B = \{\text{Thor}\}$, so
   $A \ominus B = \Omega \setminus \{ \text{Thor} \} =
   \{ \text{Batman}, \text{Superman}, \text{Wolverine},
   \text{Deadpool}, \text{Storm}, \text{Cyborg} \}$.
5. $\overline A = \{\text{Superman}, \text{Wolverine}, \text{Storm} \}$ and
   $B \cup C = \Omega$, so $\overline A \cap (B \cup C) = \overline A
   = \{ \text{Superman}, \text{Wolverine}, \text{Storm} \}$.
6. $B \cap C = \varnothing$, so $A \cup (B \cap C) = A = \{ \text{Batman},
   \text{Thor}, \text{Deadpool}, \text{Cyborg}\}$.
7. $A \cap \overline B = \{ \text{Batman}, \text{Deadpool}, \text{Cyborg} \}
   = C$, so $(A \cap \overline B) \cup C = C = \{ \text{Batman}, \text{Deadpool},
   \text{Cyborg} \}$.
8. Since $C \subseteq A$, we have $A \cap C = C$. Also $B \cap C = \varnothing$,
   so $(A \cap C) \cup (B \cap C) = C = \{ \text{Batman}, \text{Deadpool},
   \text{Cyborg} \}$.
````

````{exercise}
:label: ex-en-three-sets

Let $E$, $F$, and $G$ be three sets of superheroes. Write the algebraic
expressions, in terms of intersections, unions, and complements, that describe
the following sets.

 1. Only the superheroes in $E$.
 2. The superheroes in $E$ and $G$, but not in $F$.
 3. The superheroes in at least one of the three sets.
 4. The superheroes in at least two of the three sets.
 5. The superheroes in all three sets.
 6. No superhero (the empty set).
 7. The superheroes in at most one set.
 8. The superheroes in at most two sets.
 9. The superheroes in exactly two sets.
10. The superheroes in at most three sets.
````
````{solution} ex-en-three-sets
:class: dropdown

 1. $E \cap \overline F \cap \overline G$.
 2. $E \cap G \cap \overline F$.
 3. $E \cup F \cup G$.
 4. $(E \cap F) \cup (E \cap G) \cup (F \cap G)$.
 5. $E \cap F \cap G$.
 6. $\emptyset$.
 7. This is the complement of the set in part 4:

    ```{math}
    \overline{E \cap F} \cap \overline{E \cap G} \cap \overline{F \cap G}.
    ```

 8. The required set is the complement of that obtained in part 5:
    $\overline{E \cap F \cap G}$.
 9. Being in exactly two sets is equivalent to being in at least two but not
    all three:

    ```{math}
    \bigl( (E \cap F) \cup (E \cap G) \cup (F \cap G) \bigr)
    \cap \overline{E \cap F \cap G}.
    ```

10. Every superhero belongs to at most three sets by definition. Hence the
    required set is the universe $\Omega$.
````

````{exercise}
:label: ex-en-simplify

Simplify the following expressions where possible.

1. $E \cup \overline E$.
2. $E \cap \overline E$.
3. $(E \cup F) \cap (E \cup \overline F)$.
4. $(E \cup F) \cap (\overline E \cup F) \cap (E \cup \overline F)$.
5. $(E \cup F) \cap (F \cup G)$.
````

````{solution} ex-en-simplify
:class: dropdown

1. $E \cup \overline E = \Omega$ by the _law of excluded middle_: a
   proposition must be either true or false, so for every $\omega \in \Omega$
   either $\omega \in E$ or $\omega \notin E$ holds, which makes
   $\omega \in E \cup \overline E$ and gives the universe.

2. $E \cap \overline E = \varnothing$ by the _law of non-contradiction_: a
   proposition cannot be both true and false, so for every $\omega \in \Omega$
   exactly one of $\omega \in E$ and $\omega \notin E$ is true, making their
   conjunction false. Hence no $\omega \in \Omega$ belongs to
   $E \cap \overline E$, which characterises it as the empty set.

3. By the distributivity of union over intersection,
   $(E \cup F) \cap (E \cup \overline F) = E \cup (F \cap \overline F) =
   E \cup \varnothing = E$.

4. By associativity of intersection,
   $(E \cup F) \cap (\overline E \cup F) \cap (E \cup \overline F) =
   (E \cup F) \cap (E \cup \overline F) \cap (\overline E \cup F)$; by the
   result in part 3, the first intersection equals $E$, so the whole
   expression reduces to $E \cap (\overline E \cup F) =
   (E \cap \overline E) \cup (E \cap F) = \varnothing \cup (E \cap F) =
   E \cap F$.

5. By commutativity of intersection,
   $(E \cup F) \cap (F \cup G) = (F \cup E) \cap (F \cup G)$, and applying
   the distributivity of intersection over union gives
   $(F \cup E) \cap (F \cup G) = F \cup (E \cap G)$.
````

````{exercise}
:label: ex-en-justice-league-dark

Given three sets $M$, $D$, $H$ in a universe $\Omega$, prove the following
relations using Venn diagrams.

1. $M \cap D \subseteq M \subseteq M \cup D$.
2. If $H \subseteq \overline M$, then $M \subseteq \overline H$.
3. $D = (D \cap M) \cup (D \cap \overline M)$.
4. $M \cup D = M \cup (\overline M \cap D)$.
````

````{solution} ex-en-justice-league-dark
:class: dropdown

1. $M \cap D \subseteq M \subseteq M \cup D$

The diagram below shows the three sets: the descending diagonal hatch covers
the union $M \cup D$; the blue fill of $M$ overlaps this hatch, making it
visible that $M$ is contained in $M \cup D$; the ascending diagonal hatch
marks $M \cap D$, which is therefore entirely contained in $M$.

```{code-cell} python
:tags: [hide-input]

BG_COLOR = 'white'

def _ex_setup_ax(ax):
    ax.set_facecolor(BG_COLOR)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.add_patch(FancyBboxPatch((0.2, 0.2), 11.6, 7.6,
                                boxstyle='square,pad=0',
                                facecolor=BG_COLOR, edgecolor=EDGE_COLOR,
                                linewidth=1.1, zorder=0))
    ax.text(11.5, 7.5, r'$\Omega$', fontsize=MATH_SIZE, ha='right', va='top')

_M2_XY = (5.0, 3.7); _M2_W, _M2_H = 5.5, 4.8
_D2_XY = (7.8, 4.0); _D2_W, _D2_H = 4.5, 3.8

fig, ax = plt.subplots(figsize=(3.2, 2.4), facecolor=BG_COLOR)
_ex_setup_ax(ax)
ax.text(2.5, 6.3, r'$M$', fontsize=MATH_SIZE, va='top')
ax.text(9.3, 6.1, r'$D$', fontsize=MATH_SIZE, va='top')


ax.add_patch(Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                        facecolor=FILL_COLOR, edgecolor=EDGE_COLOR,
                        hatch='\\\\', linewidth=0, zorder=2))
ax.add_patch(Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                        facecolor=BG_COLOR, edgecolor=EDGE_COLOR,
                        hatch='\\\\', linewidth=0, zorder=1))


ax.add_patch(Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                     facecolor=HIGHLIGHT, alpha=0.5, edgecolor='none', zorder=1))


_clip_D = Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                  facecolor='none', edgecolor='none')
ax.add_patch(_clip_D)
_inter_hatch = Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                       facecolor='none', edgecolor=EDGE_COLOR, hatch='//', zorder=3)
ax.add_patch(_inter_hatch)
_inter_hatch.set_clip_path(_clip_D)

for xy, w, h in [(_M2_XY, _M2_W, _M2_H), (_D2_XY, _D2_W, _D2_H)]:
    ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                          facecolor='none', edgecolor=EDGE_COLOR,
                          linewidth=1.2, zorder=4))
plt.tight_layout()
plt.show()
```

2. If $H \subseteq \overline{M}$, then $M \subseteq \overline{H}$

Since $H \subseteq \overline{M}$, every element of $H$ is not an element of
$M$, meaning the two sets must be disjoint, as shown in the diagram below.
Consequently, every element of $M$ cannot be an element of $H$, which means
$M \subseteq \overline{H}$.

```{code-cell} python
:tags: [hide-input]

_H2_XY  = (3.5, 4.0); _H2_W,  _H2_H  = 4.2, 3.8
_M2d_XY = (8.5, 4.0); _M2d_W, _M2d_H = 4.2, 3.8

fig, ax = plt.subplots(figsize=(3.2, 2.4), facecolor=BG_COLOR)
_ex_setup_ax(ax)
ax.text(1.2,  6.2, r'$H$', fontsize=MATH_SIZE, va='top')
ax.text(10.4, 6.2, r'$M$', fontsize=MATH_SIZE, va='top')

ax.add_patch(Ellipse(xy=_H2_XY, width=_H2_W, height=_H2_H,
                          facecolor=FILL_COLOR, edgecolor=EDGE_COLOR,
                          linewidth=1.2, zorder=4))
ax.add_patch(Ellipse(xy=_M2d_XY, width=_M2d_W, height=_M2d_H,
                          facecolor='none', edgecolor=EDGE_COLOR,
                          linewidth=1.2, zorder=4))

plt.tight_layout()
plt.show()
```

3. $D = (D \cap M) \cup (D \cap \overline{M})$

The diagram below highlights $D \cap M$ (the part of $D$ that overlaps $M$)
with one hatch pattern, and $D \cap \overline{M}$ (the part of $D$ outside
$M$) with another. Together, these two sets cover exactly $D$.

```{code-cell} python
:tags: [hide-input]

_M2_XY = (5.0, 3.7); _M2_W, _M2_H = 5.5, 4.8
_D2_XY = (7.8, 4.0); _D2_W, _D2_H = 4.5, 3.8

fig, ax = plt.subplots(figsize=(3.2, 2.4), facecolor=BG_COLOR)
_ex_setup_ax(ax)
ax.text(2.5, 6.3, r'$M$', fontsize=MATH_SIZE, va='top')
ax.text(9.3, 6.1, r'$D$', fontsize=MATH_SIZE, va='top')

# M (full): /// hatch
ax.add_patch(Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                     facecolor=FILL_COLOR, edgecolor=EDGE_COLOR,
                     hatch='///', linewidth=0, zorder=1))
# D full: BG_COLOR — blanks out M's color and hatch everywhere inside D
ax.add_patch(Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                     facecolor=BG_COLOR, edgecolor='none',
                     linewidth=0, zorder=2))
# Clip ellipse for D
_clip_D = Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                  facecolor='none', edgecolor='none')
ax.add_patch(_clip_D)
# Restore FILL_COLOR in the intersection
_inter_fill = Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                      facecolor=FILL_COLOR, edgecolor='none', zorder=3)
ax.add_patch(_inter_fill)
_inter_fill.set_clip_path(_clip_D)
# Apply \\\ hatch to the intersection
_inter_hatch = Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                       facecolor='none', edgecolor=EDGE_COLOR, hatch=3*'\\', zorder=4)
ax.add_patch(_inter_hatch)
_inter_hatch.set_clip_path(_clip_D)

for xy, w, h in [(_M2_XY, _M2_W, _M2_H), (_D2_XY, _D2_W, _D2_H)]:
    ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                          facecolor='none', edgecolor=EDGE_COLOR,
                          linewidth=1.2, zorder=4))
plt.tight_layout()
plt.show()
```

4. $M \cup D = M \cup (\overline{M} \cap D)$

In the diagram below, one hatch pattern highlights $\overline{M} \cap D$,
which contains all points in $D$ but not in $M$. The latter is shown with a
different hatch, and considering all areas carrying either hatch gives exactly
$M \cup D$.

```{code-cell} python
:tags: [hide-input]

_M2_XY = (5.0, 3.7); _M2_W, _M2_H = 5.5, 4.8
_D2_XY = (7.8, 4.0); _D2_W, _D2_H = 4.5, 3.8

fig, ax = plt.subplots(figsize=(3.2, 2.4), facecolor=BG_COLOR)
_ex_setup_ax(ax)
ax.text(2.5, 6.3, r'$M$', fontsize=MATH_SIZE, va='top')
ax.text(9.3, 6.1, r'$D$', fontsize=MATH_SIZE, va='top')

# D full: HIGHLIGHT + \\\ hatch (gives D\M its hatch and color)
ax.add_patch(Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                     facecolor=HIGHLIGHT, edgecolor=EDGE_COLOR,
                     hatch=3*'\\', linewidth=0, zorder=1))
# M full: HIGHLIGHT solid (covers D's hatch in the intersection)
ax.add_patch(Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                     facecolor=HIGHLIGHT, edgecolor='none',
                     linewidth=0, zorder=2))
# M hatch: /// over all of M
ax.add_patch(Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                     facecolor='none', edgecolor=EDGE_COLOR,
                     hatch='///', linewidth=0, zorder=3))

for xy, w, h in [(_M2_XY, _M2_W, _M2_H), (_D2_XY, _D2_W, _D2_H)]:
    ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                          facecolor='none', edgecolor=EDGE_COLOR,
                          linewidth=1.2, zorder=4))
plt.tight_layout()
plt.show()
```
````

````{exercise}
:label: ex-en-partition

Consider the universe $\Omega$ and the sets $A$, $B$, and $C$ defined in
{ref}`ex-en-sets-base`.

1. Determine whether each of the following families is a partition of
   $\Omega$, justifying your answer.

   - $\mathcal{F}_1 = \{ A, B, C \}$.
   - $\mathcal{F}_2 = \{ A, \overline A\}$.
   - $\mathcal{F}_3 = \{ A \cap B, A \setminus B, \overline A \}$.
   - $\mathcal{F}_4 = \{ A \cap B, A \ominus B, \overline{A \cup B} \}$.
   - $\mathcal{F}_5 = \{ C, B \setminus C, \overline C \}$.

2. Find a partition of $\Omega$ into four blocks such that one of the blocks
   is $\{\text{Wolverine}, \text{Deadpool}\}$.

3. Find all partitions of $\Omega$ that contain $A \ominus B$.
````

````{solution} ex-en-partition
:class: dropdown

Recalling the sets from {ref}`ex-en-sets-base`:

```{math}
\begin{align*}
A &= \{\text{Batman}, \text{Thor}, \text{Deadpool}, \text{Cyborg}\},\\
B &= \{\text{Superman}, \text{Thor}, \text{Storm}, \text{Wolverine}\},\\
C &= \{\text{Batman}, \text{Deadpool}, \text{Cyborg}\}.
\end{align*}
```

1. We consider the five cases separately.

   - $\mathcal{F}_1 = \{ A, B, C \}$ is not a partition of $\Omega$, since
     $A$ and $B$ are not disjoint (both contain Thor), and neither are $A$
     and $C$ (which both contain Batman, Deadpool, and Cyborg).
   - $\mathcal{F}_2 = \{ A, \overline A \}$ is a partition of $\Omega$, for
     any non-empty $A \subseteq \Omega$: $A$ and $\overline A$ are disjoint
     and their union is $\Omega$.
   - $\mathcal{F}_3 = \{ A \cap B, A \setminus B, \overline A \}$ is a
     partition of $\Omega$, formed by the three blocks $\{ \text{Thor} \}$,
     $\{ \text{Batman}, \text{Deadpool}, \text{Cyborg} \}$, and
     $\{ \text{Superman}, \text{Wolverine}, \text{Storm} \}$, which are
     pairwise disjoint and whose union is $\Omega$. Note that this reflects
     the decomposition $\Omega = (A \cap B) \cup (A \setminus B) \cup \overline A$,
     which holds for any pair of sets $A, B$.
   - $\mathcal{F}_4 = \{ A \cap B, A \ominus B, \overline{A \cup B} \}$
     is not a partition of $\Omega$: since $A \cup B = \Omega$, we have
     $\overline{A \cup B} = \varnothing$, which is an empty block, violating
     the definition of partition.
   - $\mathcal{F}_5 = \{ C, B \setminus C, \overline C \}$ is not a
     partition of $\Omega$, since $B \setminus C$ and $\overline C$ are not
     disjoint (both contain Thor).

2. One possible partition into four blocks containing
   $\{\text{Wolverine}, \text{Deadpool}\}$ as one block is:

```{math}
\bigl\{
\{\text{Wolverine}, \text{Deadpool}\},\;
\{\text{Batman}, \text{Cyborg}\},\;
\{\text{Superman}, \text{Storm}\},\;
\{\text{Thor}\}
\bigr\}.
```

3. $A \ominus B = \{ \text{Batman}, \text{Deadpool}, \text{Cyborg},
   \text{Superman}, \text{Storm}, \text{Wolverine} \} = \Omega \setminus
   \{ \text{Thor} \}$, so the only possible partition is

```{math}
\bigl\{ A \ominus B, \{\text{Thor}\} \bigr\}.
```
````
