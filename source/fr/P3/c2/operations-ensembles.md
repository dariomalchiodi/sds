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

(sec_operations-ensembles)=
# Opérations sur les ensembles

En plus d'utiliser les relations décrites dans la section précédente, il
est possible de construire de nouveaux ensembles à partir d'ensembles
existants en utilisant les opérations décrites ci-dessous.

- L'_union_ de deux ensembles $S$ et $T$ est l'ensemble $S \cup T$ de tous
  les éléments qui appartiennent à au moins l'un d'eux. Formellement,
  $S \cup T = \{x \in \Omega \mid x \in S \vee x \in T \}$.
- L'_intersection_ de deux ensembles $S$ et $T$ est l'ensemble $S \cap T$
  des éléments communs aux deux :
  $S \cap T = \{ x \in \Omega \mid x \in S \wedge x \in T \}$.
- La _différence_ entre un ensemble $S$ et un ensemble $T$ est l'ensemble
  $S \setminus T$ des éléments de $S$ qui n'appartiennent pas à $T$ :
  $S \setminus T = \{ x \in \Omega \mid x \in S \wedge x \notin T \}$.
- La _différence symétrique_ entre deux ensembles $S$ et $T$ est
  l'ensemble $S \ominus T$ des éléments appartenant à exactement l'un des
  deux ensembles :
  $S \ominus T = \{ x \in \Omega \mid ( x \in S \wedge x \notin T )
  \vee ( x \notin S \wedge x \in T) \}$.
- Le _complémentaire_ d'un ensemble $S$ est l'ensemble $\overline S$ des
  éléments de l'univers qui n'appartiennent pas à $S$ :
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
:name: fig_fr-venn-union-intersection

Diagrammes de Venn pour l'union $O \cup V$ (à gauche) et l'intersection
$O \cap V$ (à droite), où $O$ est l'ensemble des Avengers dotés d'une
force surhumaine et $V$ celui des Avengers capables de voler. Dans les
deux cas, la région bleu foncé décrit l'ensemble d'intérêt et la région
claire indique les parties de $O$ ou $V$ qui n'en font pas partie.
````

````{prf:example}
:label: ex-fr-operations-ensembles

Considérons l'univers $\Omega$ de tous les Avengers, et définissons en son
sein les ensembles $O = \{\text{Captain America}, \text{Hulk}, \text{Thor}\}$
et $V = \{\text{Thor}, \text{Iron Man}\}$, contenant respectivement les
Avengers dotés d'une force surhumaine et ceux capables de voler.
La {numref}`fig_fr-venn-union-intersection` montre les diagrammes de Venn de
- $O \cup V = \{\text{Captain America}, \text{Hulk}, \text{Thor},
\text{Iron Man}\}$, qui inclut tous les héros considérés, et
- $O \cap V = \{\text{Thor}\}$, contenant le seul Avenger doté d'une force
  surhumaine qui peut également voler.

De même, la {numref}`fig_fr-venn-difference` illustre la différence
$O \setminus V = \{\text{Captain America}, \text{Hulk}\}$ de tous les héros
à super-force qui ne savent pas voler, et la différence symétrique
$O \ominus V = \{\text{Captain America}, \text{Hulk}, \text{Iron Man}\}$,
dont Thor est exclu car il appartient aux deux ensembles. Il est important
de souligner que la différence entre ensembles n'est pas symétrique : un
simple contre-exemple est le fait que
$V \setminus O = \{\text{Iron Man}\} \neq O \setminus V$.

Enfin, le complémentaire $\overline O$ correspond à l'ensemble des Avengers
sans force surhumaine : Iron Man, Black Widow, Hawkeye et Ant-Man, comme
illustré dans la {numref}`fig_fr-venn-complement`.
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
:name: fig_fr-venn-difference

Diagrammes de Venn pour la différence $O \setminus V$ (à gauche) et la
différence symétrique $O \ominus V$ (à droite). Mêmes notations que dans
la {numref}`fig_fr-venn-union-intersection`.
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
:name: fig_fr-venn-complement

Diagramme de Venn pour le complémentaire $\overline O$ : la région mise en
évidence contient tous les Avengers qui n'appartiennent pas à $O$. Mêmes
notations que dans la {numref}`fig_fr-venn-union-intersection`.
````

Il est facile de vérifier que les opérations d'union et d'intersection sont

- commutatives : $S \cup T = T \cup S$ et $S \cap T = T \cap S$ sont
  toujours valables, de sorte que les deux ensembles peuvent être échangés
  sans modifier leur union ni leur intersection ;
- associatives : $S \cup ( T \cup U ) = (S \cup T ) \cup U$ et
  $S \cap ( T \cap U ) = (S \cap T ) \cap U$, ce qui signifie que l'ordre
  dans lequel deux unions (ou deux intersections) sont effectuées est sans
  importance, de sorte qu'on peut écrire par exemple $S \cup T \cup U$
  sans ambiguïté ;
- distributives l'une par rapport à l'autre :
  $S \cup (T \cap U) = (S \cup T) \cap (S \cup U)$ et
  $S \cap (T \cup U) = (S \cap T) \cup (S \cap U)$, en analogie avec la
  distribution de la multiplication par rapport à l'addition en arithmétique
  (où $a \cdot (b + c) = a \cdot b + a \cdot c$), à la différence que
  ici la propriété vaut dans les deux sens.

````{prf:theorem} Lois de De Morgan
:label: teo-fr-de-morgan

Pour toute paire d'ensembles $S, T \subseteq \Omega$, les _lois de De
Morgan_ sont valables :

1. $\overline{\left( S \cup T \right)} = \overline S \cap \overline T$ ;
2. $\overline{\left( S \cap T \right)} = \overline S \cup \overline T$.
````
````{admonition} _
:class: myproof

Nous démontrons la première loi. Fixons
$x \in \overline{\left( S \cup T \right)}$ ; par définition du
complémentaire, $x \notin \left( S \cup T \right)$, ce qui implique
$x \notin S$ et $x \notin T$. En utilisant à nouveau la définition du
complémentaire, on obtient $x \in \overline S$ et $x \in \overline T$, et
donc $x \in \overline S \cap \overline T$. Comme aucune hypothèse
particulière n'a été faite sur $x$ si ce n'est $x \in \overline{(S \cup T)}$,
nous avons montré que
$\overline{\left( S \cup T \right)} \subseteq \overline S \cap \overline T$.
En procédant en sens inverse (en partant de $x \in \overline S \cap \overline T$),
on peut montrer que
$\overline S \cap \overline T \subseteq \overline{\left( S \cup T \right)}$,
ce qui donne la première loi de De Morgan. La seconde loi se démontre de
façon analogue.
````

Les lois de De Morgan nous disent essentiellement qu'il est possible de
«transférer» l'opération de complémentation de l'union de deux ensembles
aux deux ensembles eux-mêmes, en prenant soin de convertir l'union en
intersection (et une opération analogue vaut pour le complémentaire d'une
intersection).

Les relations suivantes relient également la différence symétrique, l'union,
l'intersection et la différence entre ensembles.

````{prf:theorem}
:label: teo-fr-set-difference

Étant donnés deux ensembles $S, T \subseteq \Omega$ :

1. $S \ominus T = (S \setminus T) \cup (T \setminus S)$,
2. $S \ominus T = (S \cup T) \setminus (S \cap T)$.
````
````{admonition} _
:class: myproof

La première relation est une conséquence directe de la définition de la
différence symétrique : en effet, pour tout $x \in \Omega$,

```{math}
x \in S \ominus T \leftrightarrow
(x \in S \wedge x \notin T) \vee (x \notin S \wedge x \in T) \leftrightarrow
(x \in S \setminus T) \vee (x \in T \setminus S) \leftrightarrow
x \in (S \setminus T) \cup (T \setminus S) \enspace.
```

Pour la seconde relation, supposons $x \in (S \cup T) \setminus (S \cap T)$ ;
alors $x \in (S \cup T)$ et $x \notin (S \cap T)$, ce qui implique
$(x \in S \vee x \in T) \wedge (x \notin S \cap T)$. En distribuant la
disjonction sur la conjonction, on obtient
$(x \in S \wedge x \notin S \cap T) \vee (x \in T \wedge x \notin S \cap T)$.
Donc $x \in S \setminus T \vee x \in T \setminus S$, et la première
relation déjà démontrée implique $x \in S \ominus T$. Ainsi
$(S \cup T) \setminus (S \cap T) \subseteq S \ominus T$. En procédant de
façon analogue, on démontre
$S \ominus T \subseteq (S \cup T) \setminus (S \cap T)$, ce qui donne
la thèse.
````

Les opérations d'union et d'intersection permettent d'introduire la
_partition_ d'un ensemble, entendue comme une décomposition de celui-ci en
parties non chevauchantes.

````{prf:definition} Partition
:label: def-fr-partition

Une _partition_ d'un ensemble $S$ est une famille
$\mathcal{P} = \{ P_1, P_2, \ldots, P_k \}$ de sous-ensembles non vides
de $S$, appelés _blocs_ ou _classes_, telle que :

1. $P_i \cap P_j = \varnothing$ pour tout $i \neq j$ (les blocs ne se
   chevauchent pas) ;
2. $\cup_{i=1}^k P_i = S$ (les blocs recouvrent $S$).
````

En d'autres termes, une partition assigne chaque élément de $S$ à
exactement une classe : chaque élément appartient à un et un seul bloc.
Une conséquence immédiate de la définition est que deux blocs distincts
$P_i$ et $P_j$ ne peuvent pas partager un élément.

````{prf:example}
:label: ex-fr-partitions

Considérons l'ensemble des Avengers dans leur formation originale :
$S = \{ \text{Captain America}, \text{Hulk}, \text{Thor},
\text{Iron Man}, \text{Black Widow}, \text{Hawkeye} \}$.

- La famille
  $\mathcal{P}_1 = \bigl\{
  \{\text{Captain America}, \text{Iron Man}\},\,
  \{\text{Hulk}, \text{Thor}\},\,
  \{\text{Black Widow}, \text{Hawkeye}\}
  \bigr\}$
  est une partition de $S$ : les trois blocs sont disjoints et couvrent
  ensemble tous les héros.

- En revanche, la famille
  $\mathcal{P}_2 = \bigl\{
  \{\text{Captain America}, \text{Hulk}, \text{Thor}\},\,
  \{\text{Thor}, \text{Iron Man}, \text{Black Widow}, \text{Hawkeye}\}
  \bigr\}$
  n'est pas une partition de $S$, car Thor apparaît dans les deux blocs.

- De même,
  $\mathcal{P}_3 = \bigl\{
  \{\text{Captain America}, \text{Thor}, \text{Iron Man}\},\,
  \{\text{Hulk}, \text{Black Widow}\}
  \bigr\}$
  n'est pas une partition de $S$, car Hawkeye n'appartient à aucun bloc.
````

Un ensemble $S$ admet toujours deux partitions triviales : celle composée
d'un unique bloc $\{S\}$, et celle où chaque bloc est un singleton,
$\bigl\{ \{s\} \mid s \in S \bigr\}$. Enfin, une partition de $S$ en deux
blocs est étroitement liée à l'opération de complémentation : si
$A \subseteq S$ est un sous-ensemble non vide et différent de $S$, alors
$\{A,\, S \setminus A\}$ est une partition de $S$ en deux blocs.


## Exercices

````{exercise}
:label: ex-fr-ensembles-base

Soit
```{math}
\Omega = \{ \text{Batman}, \text{Superman}, \text{Thor}, \text{Wolverine},
        \text{Deadpool}, \text{Storm}, \text{Cyborg} \} \enspace.
```
En partant des ensembles de super-héros suivants :

```{math}
\begin{align*}
A &= \{ \text{Batman}, \text{Thor}, \text{Deadpool},
        \text{Cyborg} \} \enspace, \\
B &= \{ \text{Superman}, \text{Thor}, \text{Storm},
        \text{Wolverine} \} \enspace, \\
C &= \{ \text{Deadpool}, \text{Cyborg}, \text{Batman} \} \enspace,
\end{align*}
```

décrivez extensivement les ensembles suivants :

1. $A \cap B$,
2. $\overline C$,
3. $A \setminus C$,
4. $A \ominus B$,
5. $\overline A \cap (B \cup C)$,
6. $A \cup (B \cap C)$,
7. $(A \cap \overline B) \cup C$,
8. $(A \cap C) \cup (B \cap C)$.
````

````{solution} ex-fr-ensembles-base
:class: dropdown

1. $A \cap B = \{\text{Thor}\}$.
2. $\overline C = B = \{ \text{Superman}, \text{Thor}, \text{Storm},
   \text{Wolverine} \}$.
3. $A \setminus C = \{ \text{Thor} \}$.
4. $A \cup B = \Omega$ et $A \cap B = \{\text{Thor}\}$, donc
   $A \ominus B = \Omega \setminus \{ \text{Thor} \} =
   \{ \text{Batman}, \text{Superman}, \text{Wolverine},
   \text{Deadpool}, \text{Storm}, \text{Cyborg} \}$.
5. $\overline A = \{\text{Superman}, \text{Wolverine}, \text{Storm} \}$ et
   $B \cup C = \Omega$, donc $\overline A \cap (B \cup C) = \overline A
   = \{ \text{Superman}, \text{Wolverine}, \text{Storm} \}$.
6. $B \cap C = \varnothing$, donc $A \cup (B \cap C) = A = \{ \text{Batman},
   \text{Thor}, \text{Deadpool}, \text{Cyborg}\}$.
7. $A \cap \overline B = \{ \text{Batman}, \text{Deadpool}, \text{Cyborg} \}
   = C$, donc $(A \cap \overline B) \cup C = C = \{ \text{Batman},
   \text{Deadpool}, \text{Cyborg} \}$.
8. Puisque $C \subseteq A$, on a $A \cap C = C$. De plus,
   $B \cap C = \varnothing$, donc $(A \cap C) \cup (B \cap C) = C =
   \{ \text{Batman}, \text{Deadpool}, \text{Cyborg} \}$.
````

````{exercise}
:label: ex-fr-trois-ensembles

Soient $E$, $F$ et $G$ trois ensembles de super-héros. Écrivez les
expressions algébriques, en termes d'intersections, d'unions et de
complémentaires, qui permettent d'exprimer les ensembles suivants.

 1. Seulement les super-héros dans $E$.
 2. Les super-héros dans $E$ et $G$, mais pas dans $F$.
 3. Les super-héros dans au moins un des trois ensembles.
 4. Les super-héros dans au moins deux des trois ensembles.
 5. Les super-héros dans les trois ensembles.
 6. Aucun super-héros (l'ensemble vide).
 7. Les super-héros dans au plus un ensemble.
 8. Les super-héros dans au plus deux ensembles.
 9. Les super-héros dans exactement deux ensembles.
10. Les super-héros dans au plus trois ensembles.
````
````{solution} ex-fr-trois-ensembles
:class: dropdown

 1. $E \cap \overline F \cap \overline G$.
 2. $E \cap G \cap \overline F$.
 3. $E \cup F \cup G$.
 4. $(E \cap F) \cup (E \cap G) \cup (F \cap G)$.
 5. $E \cap F \cap G$.
 6. $\emptyset$.
 7. C'est le complémentaire de l'ensemble au point 4 :

    ```{math}
    \overline{E \cap F} \cap \overline{E \cap G} \cap \overline{F \cap G}.
    ```

 8. L'ensemble requis est le complémentaire de celui obtenu au point 5 :
    $\overline{E \cap F \cap G}$.
 9. Être exactement dans deux ensembles équivaut à être dans au moins deux
    mais pas dans les trois :

    ```{math}
    \bigl( (E \cap F) \cup (E \cap G) \cup (F \cap G) \bigr)
    \cap \overline{E \cap F \cap G}.
    ```

10. Tout super-héros appartient à au plus trois ensembles par définition.
    L'ensemble requis est donc l'univers $\Omega$.
````

````{exercise}
:label: ex-fr-simplifier

Simplifiez, lorsque c'est possible, les expressions suivantes.

1. $E \cup \overline E$.
2. $E \cap \overline E$.
3. $(E \cup F) \cap (E \cup \overline F)$.
4. $(E \cup F) \cap (\overline E \cup F) \cap (E \cup \overline F)$.
5. $(E \cup F) \cap (F \cup G)$.
````

````{solution} ex-fr-simplifier
:class: dropdown

1. $E \cup \overline E = \Omega$ par le _principe du tiers exclu_ : une
   proposition doit être vraie ou fausse, donc pour tout $\omega \in \Omega$
   soit $\omega \in E$ soit $\omega \notin E$, ce qui rend
   $\omega \in E \cup \overline E$ et donne l'univers.

2. $E \cap \overline E = \varnothing$ par le _principe de non-contradiction_ :
   une proposition ne peut pas être à la fois vraie et fausse, donc pour
   tout $\omega \in \Omega$ exactement l'une des propositions $\omega \in E$
   et $\omega \notin E$ est vraie, rendant leur conjonction fausse. Ainsi
   aucun $\omega \in \Omega$ n'appartient à $E \cap \overline E$, ce qui
   le caractérise comme l'ensemble vide.

3. Par la distributivité de l'union sur l'intersection,
   $(E \cup F) \cap (E \cup \overline F) = E \cup (F \cap \overline F) =
   E \cup \varnothing = E$.

4. Par l'associativité de l'intersection,
   $(E \cup F) \cap (\overline E \cup F) \cap (E \cup \overline F) =
   (E \cup F) \cap (E \cup \overline F) \cap (\overline E \cup F)$ ; par
   le résultat du point précédent, la première intersection est égale à
   $E$, donc toute l'expression se réduit à $E \cap (\overline E \cup F) =
   (E \cap \overline E) \cup (E \cap F) = \varnothing \cup (E \cap F) =
   E \cap F$.

5. Par la commutativité de l'intersection,
   $(E \cup F) \cap (F \cup G) = (F \cup E) \cap (F \cup G)$, et en
   appliquant la distributivité de l'intersection sur l'union on obtient
   $(F \cup E) \cap (F \cup G) = F \cup (E \cap G)$.
````

````{exercise}
:label: ex-fr-justice-league-dark

Étant donnés trois ensembles $M$, $D$, $H$ dans un univers $\Omega$,
démontrez la validité des relations suivantes à l'aide de diagrammes de Venn.

1. $M \cap D \subseteq M \subseteq M \cup D$.
2. Si $H \subseteq \overline M$, alors $M \subseteq \overline H$.
3. $D = (D \cap M) \cup (D \cap \overline M)$.
4. $M \cup D = M \cup (\overline M \cap D)$.
````

````{solution} ex-fr-justice-league-dark
:class: dropdown

1. $M \cap D \subseteq M \subseteq M \cup D$

Le diagramme ci-dessous montre les trois ensembles : le hachage diagonal
descendant couvre l'union $M \cup D$ ; le remplissage bleu de $M$ se
superpose à ce hachage, rendant visible que $M$ est contenu dans $M \cup D$ ;
le hachage diagonal montant marque $M \cap D$, qui est donc entièrement
contenu dans $M$.

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

2. Si $H \subseteq \overline{M}$, alors $M \subseteq \overline{H}$

Puisque $H \subseteq \overline{M}$, tout élément de $H$ n'est pas un
élément de $M$, ce qui signifie que les deux ensembles doivent être
disjoints, comme le montre le diagramme ci-dessous. Par conséquent, tout
élément de $M$ ne peut pas être un élément de $H$, ce qui signifie
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

Le diagramme ci-dessous met en évidence $D \cap M$ (la partie de $D$ qui
chevauche $M$) avec un type de hachage, et $D \cap \overline{M}$ (la
partie de $D$ à l'extérieur de $M$) avec un autre. Ensemble, ces deux
ensembles couvrent exactement $D$.

```{code-cell} python
:tags: [hide-input]

_M2_XY = (5.0, 3.7); _M2_W, _M2_H = 5.5, 4.8
_D2_XY = (7.8, 4.0); _D2_W, _D2_H = 4.5, 3.8

fig, ax = plt.subplots(figsize=(3.2, 2.4), facecolor=BG_COLOR)
_ex_setup_ax(ax)
ax.text(2.5, 6.3, r'$M$', fontsize=MATH_SIZE, va='top')
ax.text(9.3, 6.1, r'$D$', fontsize=MATH_SIZE, va='top')

ax.add_patch(Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                     facecolor=FILL_COLOR, edgecolor=EDGE_COLOR,
                     hatch='///', linewidth=0, zorder=1))
ax.add_patch(Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                     facecolor=BG_COLOR, edgecolor='none',
                     linewidth=0, zorder=2))
_clip_D = Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                  facecolor='none', edgecolor='none')
ax.add_patch(_clip_D)
_inter_fill = Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                      facecolor=FILL_COLOR, edgecolor='none', zorder=3)
ax.add_patch(_inter_fill)
_inter_fill.set_clip_path(_clip_D)
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

Dans le diagramme ci-dessous, un type de hachage met en évidence
$\overline{M} \cap D$, qui contient tous les points dans $D$ mais pas
dans $M$. Ce dernier est montré avec un hachage différent, et en
considérant toutes les zones portant l'un ou l'autre hachage, on obtient
exactement $M \cup D$.

```{code-cell} python
:tags: [hide-input]

_M2_XY = (5.0, 3.7); _M2_W, _M2_H = 5.5, 4.8
_D2_XY = (7.8, 4.0); _D2_W, _D2_H = 4.5, 3.8

fig, ax = plt.subplots(figsize=(3.2, 2.4), facecolor=BG_COLOR)
_ex_setup_ax(ax)
ax.text(2.5, 6.3, r'$M$', fontsize=MATH_SIZE, va='top')
ax.text(9.3, 6.1, r'$D$', fontsize=MATH_SIZE, va='top')

ax.add_patch(Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                     facecolor=HIGHLIGHT, edgecolor=EDGE_COLOR,
                     hatch=3*'\\', linewidth=0, zorder=1))
ax.add_patch(Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                     facecolor=HIGHLIGHT, edgecolor='none',
                     linewidth=0, zorder=2))
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
:label: ex-fr-partition

Considérez l'univers $\Omega$ et les ensembles $A$, $B$ et $C$ définis
dans l'{ref}`ex-fr-ensembles-base`.

1. Déterminez si chacune des familles suivantes est une partition de
   $\Omega$, en justifiant votre réponse.

   - $\mathcal{F}_1 = \{ A, B, C \}$.
   - $\mathcal{F}_2 = \{ A, \overline A\}$.
   - $\mathcal{F}_3 = \{ A \cap B, A \setminus B, \overline A \}$.
   - $\mathcal{F}_4 = \{ A \cap B, A \ominus B, \overline{A \cup B} \}$.
   - $\mathcal{F}_5 = \{ C, B \setminus C, \overline C \}$.

2. Trouvez une partition de $\Omega$ en quatre blocs telle qu'un des blocs
   soit $\{\text{Wolverine}, \text{Deadpool}\}$.

3. Déterminez toutes les partitions de $\Omega$ qui contiennent $A \ominus B$.
````

````{solution} ex-fr-partition
:class: dropdown

Rappelons les ensembles de l'{ref}`ex-fr-ensembles-base` :

```{math}
\begin{align*}
A &= \{\text{Batman}, \text{Thor}, \text{Deadpool}, \text{Cyborg}\},\\
B &= \{\text{Superman}, \text{Thor}, \text{Storm}, \text{Wolverine}\},\\
C &= \{\text{Batman}, \text{Deadpool}, \text{Cyborg}\}.
\end{align*}
```

1. Considérons les cinq cas séparément.

   - $\mathcal{F}_1 = \{ A, B, C \}$ n'est pas une partition de $\Omega$,
     car $A$ et $B$ ne sont pas disjoints (ils contiennent tous deux Thor),
     et $A$ et $C$ non plus (ils contiennent tous deux Batman, Deadpool et
     Cyborg).
   - $\mathcal{F}_2 = \{ A, \overline A \}$ est une partition de $\Omega$,
     pour tout $A \subseteq \Omega$ non vide : $A$ et $\overline A$ sont
     disjoints et leur union est $\Omega$.
   - $\mathcal{F}_3 = \{ A \cap B, A \setminus B, \overline A \}$ est une
     partition de $\Omega$, formée des trois blocs $\{ \text{Thor} \}$,
     $\{ \text{Batman}, \text{Deadpool}, \text{Cyborg} \}$ et
     $\{ \text{Superman}, \text{Wolverine}, \text{Storm} \}$, qui sont deux
     à deux disjoints et dont l'union est $\Omega$. Notez que cela reflète
     la décomposition $\Omega = (A \cap B) \cup (A \setminus B) \cup \overline A$,
     valable pour toute paire d'ensembles $A, B$.
   - $\mathcal{F}_4 = \{ A \cap B, A \ominus B, \overline{A \cup B} \}$
     n'est pas une partition de $\Omega$ : comme $A \cup B = \Omega$, on a
     $\overline{A \cup B} = \varnothing$, qui est un bloc vide, ce qui
     viole la définition de partition.
   - $\mathcal{F}_5 = \{ C, B \setminus C, \overline C \}$ n'est pas une
     partition de $\Omega$, car $B \setminus C$ et $\overline C$ ne sont
     pas disjoints (ils contiennent tous deux Thor).

2. Une partition possible en quatre blocs contenant
   $\{\text{Wolverine}, \text{Deadpool}\}$ comme l'un des blocs est :

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
   \{ \text{Thor} \}$, donc l'unique partition possible est

```{math}
\bigl\{ A \ominus B, \{\text{Thor}\} \bigr\}.
```
````
