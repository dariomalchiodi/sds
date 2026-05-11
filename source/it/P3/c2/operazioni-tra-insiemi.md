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

(sec_operazioni-tra-insiemi)=
# Operazioni tra insiemi

Oltre a utilizzare le relazioni descritte nel paragrafo precedente, è possibile
costruire nuovi insiemi a partire da insiemi esistenti utilizzando le
operazioni descritte di seguito.

- L’_unione_ di due insiemi $S$ e $T$ è l'insieme $S \cup T$ di tutti gli
  elementi che appartengono ad almeno uno di essi. Formalmente,
  $S \cup T = \{x \in \Omega \mid x \in S \vee x \in T \}$.
- L’_intersezione_ di due insiemi $S$ e $T$ è l'insieme $S \cap T$ degli
  elementi comuni a entrambi, ovvero
  $S \cap T = \{ x \in \Omega \mid x \in S \wedge x \in T \}$.
- La _differenza_ tra un insieme $S$ e un insieme $T$ è l'insieme
  $S \setminus T$ degli elementi di $S$ che non appartengono a $T$:
  $S \setminus T = \{ x \in \Omega \mid x \in S \wedge x \notin T \}$.
- La _differenza simmetrica_ tra due insiemi $S$ e $T$ è l'insieme
  $S \ominus T$ degli elementi che appartengono a uno solo dei due insiemi;
  pertanto, $S \ominus T = \{ x \in \Omega \mid ( x \in S \wedge x \notin T )
  \vee ( x \notin S \wedge x \in T) \}$.
- Il _complemento_ di un insieme $S$ è l'insieme $\overline S$ degli elementi
  dell'universo che non appartengono a $S$, così che
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

ELEMS_O   = [('Capitan\nAmerica', 3.0, 4.5,  1.0,  0.),
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
:name: fig_venn-union-intersection

Diagrammi di Venn per l'unione $O \cup V$ (a sinistra) e l'intersezione
$O \cap V$ (a destra), dove $O$ è l'insieme degli Avengers con forza sovrumana
e $V$ quello degli Avengers in grado di volare. In entrambi i casi, il colore
azzurro scuro descrive l'insieme di interesse e quello chiaro indica le parti
di $O$ o $V$ che non ne fanno parte.
````

````{prf:example}
:label: ex-set-operations  

Consideriamo l'universo $\Omega$ di tutti gli Avengers, e definiamo al suo
interno gli insiemi $O = \{\text{Capitan America}, \text{Hulk}, \text{Thor}\}$
e $V = \{\text{Thor}, \text{Iron Man}\}$, che contengono rispettivamente gli
Avengers con forza sovrumana e quelli in grado di volare. La
{numref}`fig_venn-union-intersection` mostra i diagrammi di Venn di
- $O \cup V = \{\text{Capitan America}, \text{Hulk}, \text{Thor},
\text{Iron Man}\}$, che include tutti gli eroi considerati, e
- $O \cap V = \{\text{Thor}\}$, contente il solo Avenger con forza sovrumana
  che può anche volare.

Analogamente, la {numref}`fig_venn-difference` illustra la differenza
$O \setminus V = \{\text{Capitan America}, \text{Hulk}\}$ di tutti gli eroi con
super-forza che non sanno volare e la differenza simmetrica
$O \ominus V = \{\text{Capitan America}, \text{Hulk}, \text{Iron Man}\}$, da
cui Thor è escluso perché appartiene a entrambi gli insiemi. È importante
sottolineare come la differenza tra insiemi non sia simmetrica: un semplice
controesempio è dato dal fatto che
$V \setminus O = \{\text{Iron Man}\} \neq O \setminus V$.

Infine, il complemento $\overline O$ corrisponde all'insieme degli Avengers
privi di forza sovrumana: Iron Man, Black Widow, Hawkeye ed Ant-Man, come
illustrato nella {numref}`fig_venn-complement`.
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
:name: fig_venn-difference

Diagrammi di Venn per la differenza $O \setminus V$ (a sinistra) e la
differenza simmetrica $O \ominus V$ (a destra). Stesse notazioni della
{numref}`fig_venn-union-intersection`.
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
:name: fig_venn-complement

Diagramma di Venn per il complemento $\overline O$: la regione evidenziata
contiene tutti gli Avengers che non appartengono a $O$. Stesse notazioni della
{numref}`fig_venn-union-intersection`.
````

Si verifica facilmente come le operazioni di unione e intersezione siano

- commutative: vale sempre $S \cup T = T \cup S$ e $S \cap T = T \cap S$, e
  quindi è possibile scambiare i due insiemi mantenendo invariate la loro
  unione e la loro intersezione;
- associative: $S \cup ( T \cup U ) = (S \cup T ) \cup U$ e
  $S \cap ( T \cap U ) = (S \cap T ) \cap U$, il che significa che l'ordine con
  cui vengono eseguite due unioni (o due intersezioni) è ininfluente, pertanto
  è possibile scrivere per esempio $S \cup T \cup U$ senza che l'espressione
  risultante sia ambigua;
- distributive l'una rispetto all'altra, nel senso che vale
  $S \cup (T \cap U) = (S \cup T) \cap (S \cup U)$ e
  $S \cap (T \cup U) = (S \cap T) \cup (S \cap U)$, in analogia con la
  distribuzione della moltiplicazione rispetto all'addizione nell'aritmetica
  (dove vale $a \cdot (b + c) = a \cdot b + a \cdot c$), con la differenza
  che qui la proprietà vale in entrambe le direzioni.

````{prf:theorem} Leggi di De Morgan
:label: teo-de-morgan

Per ogni coppia di insiemi $S, T \subseteq \Omega$, valgono le _leggi di De
Morgan_:

1. $\overline{\left( S \cup T \right)} = \overline S \cap \overline T$;
2. $\overline{\left( S \cap T \right)} = \overline S \cup \overline T$.
````
````{admonition} _
:class: myproof

Dimostriamo la prima delle due leggi. Se fissiamo
$x \in \overline{\left( S \cup T \right)}$, per definizione di complemento
si ha che $x \notin \left( S \cup T \right)$, il che implica
$x \notin S$ e $x \notin T$. Da questo fatto si ottiene, sempre sfruttando la
definizione di complemento, che $x \in \overline S$ e $x \in \overline T$, e
dunque $x \in \overline S \cap \overline T$. Siccome non abbiamo fatto
particolari ipotesi su $x$ se non quella di appartenere a
$\overline{(S \cup T)}$, abbiamo dunque dimostrato che
$\overline{\left( S \cup T \right)} \subseteq \overline S \cap \overline T$.
Procedendo in modo inverso (cioè partendo da
$x \in \overline S \cap \overline T$) si può dimostrare che
$\overline S \cap \overline T \subseteq \overline{\left( S \cup T \right)}$,
ottenendo pertanto la prima legge di De Morgan. La seconda legge si dimostra
in modo analogo.
````

Le leggi di De Morgan ci dicono essenzialmente che è possibile «trasferire»
l'operazione di complemento dall'unione di due insiemi ai due insiemi stessi,
avendo cura di convertire l'unione in intersezione (e un'analoga operazione
vale per il complemento di un'intersezione). 

Valgono, infine, delle particolari relazioni tra la differenza simmetrica,
l'unione, l'intersezione e la differenza tra insiemi, come indicato nel
teorema che segue.

````{prf:theorem}
:label: teo-set-difference

Dati due insiemi $S, T \subseteq \Omega$:

1. $S \ominus T = (S \backslash T) \cup (T \backslash S)$,
2. $S \ominus T = (S \cup T) \backslash (S \cap T)$.
````
````{admonition} _
:class: myproof

La prima relazione è una conseguenza diretta della definizione di differenza
simmetrica: infatti, per ogni $x \in \Omega$,

```{math}
x \in S \ominus T \leftrightarrow
(x \in S \vee x \notin T) \wedge (x \notin S \vee x \in T) \leftrightarrow
(x \in S \backslash T) \wedge (x \in T \backslash S) \leftrightarrow
x \in (S \backslash T) \cup (T \backslash S) \enspace.
```

Per quanto riguarda invece la seconda relazione, se
$x \in (S \cup T) \backslash (S \cap T)$, allora
$x \in (S \cup T)$ e $x \notin (S \cap T)$, il che implica
$(x \in S \vee x \in T) \wedge (x \notin S \cap T)$. Per la distribuzione della
disgiunzione sulla congiunzione si ottiene
$(x \in S \wedge x \notin S \cap T) \vee (x \in T \wedge x \notin S \cap T)$.
Pertanto $x \in S \backslash T \vee x \in T \backslash S$, e la relazione al
primo punto, appena dimostrata, implica $x \in S \ominus T$. Dunque
$(S \cup T) \backslash (S \cap T) \subseteq S \ominus T$. Procedendo in modo
analogo si dimostra $S \ominus T \subseteq (S \cup T) \backslash (S \cap T)$,
il che implica la tesi.
````

Le operazioni di unione e intersezione permettono di introdurre la _partizione_
di un insieme, intesa come una sua scomposizione in parti non sovrapposte.

````{prf:definition} Partizione
:label: def-partizione

Una _partizione_ di un insieme $S$ è una famiglia
$\mathcal{P} = \{ P_1, P_2, \ldots, P_k \}$ di sottoinsiemi non vuoti di $S$,
detti _blocchi_ o _classi_, tale che:

1. $P_i \cap P_j = \varnothing$ per ogni $i \neq j$ (i blocchi non si
   sovrappongono);
2. $\cup_{i=1}^k P_i = S$ (i blocchi ricoprono $S$).
````

In altre parole, una partizione assegna ogni elemento di $S$ a esattamente
una delle classi: ogni elemento appartiene a uno e un solo blocco. Una
conseguenza immediata della definizione è che, dati due blocchi distinti
$P_i$ e $P_j$, un elemento non può appartenere a entrambi.

````{prf:example}
:label: ex-partizioni

Consideriamo l'insieme degli Avengers, nella loro formazione originale:
$S = \{ \text{Capitan America}, \text{Hulk}, \text{Thor},
\text{Iron Man}, \text{Black Widow}, \text{Hawkeye} \}$.

- La famiglia
  $\mathcal{P}_1 = \bigl\{
  \{\text{Capitan America}, \text{Iron Man}\},\,
  \{\text{Hulk}, \text{Thor}\},\,
  \{\text{Black Widow}, \text{Hawkeye}\}
  \bigr\}$
  è una partizione di $S$: i tre blocchi sono disgiunti e insieme
  coprono tutti gli eroi.

- Al contrario, la famiglia
  $\mathcal{P}_2 = \bigl\{
  \{\text{Capitan America}, \text{Hulk}, \text{Thor}\},\,
  \{\text{Thor}, \text{Iron Man}, \text{Black Widow}, \text{Hawkeye}\}
  \bigr\}$
  non è una partizione di $S$, in quanto Thor compare in entrambi i blocchi.

- Analogamente,
  $\mathcal{P}_3 = \bigl\{
  \{\text{Capitan America}, \text{Thor}, \text{Iron Man}\},\,
  \{\text{Hulk}, \text{Black Widow}\}
  \bigr\}$
  non è una partizione di $S$, perché Hawkeye non appartiene a nessun
  blocco.
````

Un insieme $S$ ammette sempre due partizioni banali: quella composta da un
unico blocco $\{S\}$ e quella in cui ogni blocco è un singoletto,
$\bigl\{ \{s\} \mid s \in S \bigr\}$. Infine, una partizione di un insieme $S$
in due blocchi è strettamente legata all'operazione di complemento: se
$A \subseteq S$ è un sottoinsieme non vuoto e diverso da $S$, allora
$\{A,\, S \setminus A\}$ è una partizione di $S$ in due blocchi.


## Esercizi

````{exercise}
:label: ex-insiemi-base

Sia
```{math}
\Omega = \{ \text{Batman}, \text{Superman}, \text{Thor}, \text{Wolverine},
        \text{Deadpool}, \text{Storm}, \text{Cyborg} \} \enspace.
```
Partendo dai seguenti insiemi di supereroi:

```{math}
\begin{align*}
A &= \{ \text{Batman}, \text{Thor}, \text{Deadpool},
        \text{Cyborg} \} \enspace, \\
B &= \{ \text{Superman}, \text{Thor}, \text{Storm},
        \text{Wolverine} \} \enspace, \\
C &= \{ \text{Deadpool}, \text{Cyborg}, \text{Batman} \} \enspace,
\end{align*}
```

descrivete i seguenti insiemi in modo estensivo:

1. $A \cap B$,
2. $\overline C$,
3. $A \setminus C$,
4. $A \ominus B$,
5. $\overline A \cap (B \cup C)$,
6. $A \cup (B \cap C)$,
7. $(A \cap \overline B) \cup C$,
8. $(A \cap C) \cup (B \cap C)$.
````

````{solution} ex-insiemi-base
:class: dropdown

1. $A \cap B = \{\text{Thor}\}$.
2. $\overline C = B = \{ \text{Superman}, \text{Thor}, \text{Storm},
   \text{Wolverine} \}$,
3. $A \setminus C = \{ \text{Thor} \}$.
4. $A \cup B = \Omega$ e $A \cap B = \{\text{Thor}\}$, per cui
   $A \ominus B = \Omega \setminus \{ \text{Thor} \} =
   \{ \text{Batman}, \text{Superman}, \text{Wolverine},
   \text{Deadpool}, \text{Storm}, \text{Cyborg} \}$
5. $\overline A = \{\text{Superman}, \text{Wolverine}, \text{Storm} \}$ e
   $B \cup C = \Omega$, quindi $\overline A \cap (B \cup C) = \overline A
   = \{ \text{Superman}, \text{Wolverine}, \text{Storm} \}$.
6. $B \cap C = \varnothing$, quindi $A \cup (B \cap C) = A = \{ \text{Batman},
   \text{Thor}, \text{Deadpool}, \text{Cyborg}\}$.
7. $A \cap \overline B = \{ \text{Batman}, \text{Deadpool}, \text{Cyborg} \}
   = C$, quindi $(A \cap \overline B) \cup C = C = \{ \text{Batman}, \text{Deadpool},
   \text{Cyborg} \} = C$.
8. Poiché $C \subseteq A$, si ha $A \cap C = C$. Inoltre,
   $B \cap C = \varnothing$, per cui $(A \cap C) \cup (B \cap C) = C =
   C = \{ \text{Batman}, \text{Deadpool}, \text{Cyborg} \}$.
````

````{exercise}
:label: ex-tre-insiemi

Siano $E$, $F$ e $G$ tre insiemi di supereroi. Indicate le espressioni
algebriche, in termini di intersezioni, unioni e complementi, che permettono
di esprimere gli insiemi che seguono.

 1. Solo i supereroi in $E$.
 2. I supereroi in $E$ e in $G$, ma non in $F$.
 3. I supereroi in almeno uno dei tre insiemi.
 4. I supereroi in almeno due dei tre insiemi.
 5. I supereroi in tutti e tre gli insiemi.
 6. Nessun supereroe (l'insieme vuoto).
 7. I supereroi in non più di un insieme.
 8. I supereroi in non più di due insiemi.
 9. I supereroi in esattamente due insiemi.
10. I supereroi in non più di tre insiemi.
````
````{solution} ex-tre-insiemi
:class: dropdown

 1. $E \cap \overline F \cap \overline G$.
 2. $E \cap G \cap \overline F$.
 3. $E \cup F \cup G$.
 4. $(E \cap F) \cup (E \cap G) \cup (F \cap G)$.
 5. $E \cap F \cap G$.
 6. $\emptyset$.
 7. Si tratta del complementare dell'insieme al punto 4:

    ```{math}
    \overline{E \cap F} \cap \overline{E \cap G} \cap \overline{F \cap G}.
    ```

 8. L'insieme richiesto è il complementare di quello ottenuto al punto 5:
    $\overline{E \cap F \cap G}$.
 9. Essere esattamente in due insiemi equivale ad essere almeno in due, ma non
    in tutti e tre:

    ```{math}
    \bigl( (E \cap F) \cup (E \cap G) \cup (F \cap G) \bigr)
    \cap \overline{E \cap F \cap G}.
    ```

10. Ogni supereroe appartiene ad al più tre insiemi per definizione. Dunque
    l'insieme richiesto è l'universo $\Omega$.
````

````{exercise}
:label: ex-semplifica

Semplificate, dove possibile, le seguenti espressioni.

1. $E \cup \overline E$.
2. $E \cap \overline E$.
3. $(E \cup F) \cap (E \cup \overline F)$.
4. $(E \cup F) \cap (\overline E \cup F) \cap (E \cup \overline F)$.
5. $(E \cup F) \cap (F \cup G)$.
````

````{solution} ex-semplifica
:class: dropdown

1. $E \cup \overline E = \Omega$ per il _principio del terzo escluso_: una
   proposizione deve essere vera oppure falsa, pertanto per ogni
   $\omega \in \Omega$ deve essere vero
   $\omega \in E$ oppure $\omega \notin E$,
   il che rende $\omega \in E \cup \overline E$, che coinciderà con l'universo.

2. $E \cap \overline E = \varnothing$ per il _principio di non contraddizione_:
   una proposizione non può essere al tempo stesso vera e falsa, dunque, per
   ogni $\omega \in \Omega$, una e una sola tra $\omega \in E$ e
   $\omega \notin E$ deve essere vera, il che rende falsa la loro congiunzione.
   Pertanto nessun $\omega \in \Omega$ appartiene a $E \cap \overline E$,
   proprietà che lo caratterizza come l'insieme vuoto.

3. Per la distributività dell'unione rispetto all'intersezione si ha
   $(E \cup F) \cap (E \cup \overline F) = E \cup (F \cap \overline F) =
   E \cup \varnothing = E$.

4. Per l'associatività dell'intersezione,
   $(E \cup F) \cap (\overline E \cup F) \cap (E \cup \overline F) = 
   (E \cup F) \cap (E \cup \overline F) \cap (\overline E \cup F)$; per il
   risultato al punto precedente, la prima intersezione è uguale a $E$, e
   dunque tutta l'espressione equivale a $E \cap (\overline E \cup F) =
   (E \cap \overline E) \cup (E \cap F) = \varnothing \cup (E \cap F) =
   E \cap F$.

5. Per la commutatività dell'intersezione,
   $(E \cup F) \cap (F \cup G) = (F \cup E) \cap (F \cup G)$, e applicando la
   distribuzione dell'intersezione rispetto all'unione si ottiene
   $(F \cup E) \cap (F \cup G) = F \cup (E \cap G)$.
````

````{exercise}
:label: ex-justice-league-dark

Dati tre insiemi $M, D, H$ in un universo $\Omega$, dimostrate la validità
delle seguenti relazioni usando i diagrammi di Venn.

1. $M \cap D \subseteq M \subseteq M \cup D$.
2. Se $H \subseteq \overline M$, allora $M \subseteq \overline H$.
3. $D = (D \cap M) \cup (D \cap M^c)$.
4. $M \cup D = M \cup (M^c \cap D)$.
````

````{solution} ex-justice-league-dark
:class: dropdown

1. $M \cap D \subseteq M \subseteq M \cup D$

Il diagramma che segue mostra i tre insiemi: il tratteggio diagonale
discendente copre l'unione $M \cup D$; il colore azzurro di $M$ si sovrappone a
a questo tratteggio, rendendo visibile che $M$ è contenuto in $M \cup D$; il
tratteggio diagonale ascendente contrassegna invece $M \cap D$, che risulta
dunque interamente contenuto in $M$.

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

2. Se $H \subseteq \overline{M}$, allora $M \subseteq \overline{H}$

Siccome $H \subseteq \overline{M}$, ogni elemento di $H$ non è un elemento di
$M$, il che sinifica che i due eventi devono essere disgiunti, come evidenziato
nel diagramma qui sotto. Di conseguenza, ogni elemento di $M$ non può essere
un elemento di $H$, il che significa $M \subseteq \overline{H}$.

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

3. $M = (M \cap D) \cup (M \cap \overline{D})$

Il diagramma che segue evidenzia rispettivamente $M \cap D$ (la parte di $M$
che si sovrappone a $D$) usando un tratteggio, e $M \cap \overline{D}$ (la
parte di $M$ esterna a $E$) usando un altro tratteggio. Come si vede, questi
due insiemi, considerati insieme, ricoprono esattamente $M$.

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

**5.** $M \cup D = M \cup (\overline{M} \cap D)$

Nel diagramma qui sotto, viene utilizzato un tipo di tratteggio per mettere in
evidenza $\overline{M} \cap D$, che contiene tutti i punti che si trovano
in $D$ ma non in $M$. Quet'ultimo è nvece descritto dall'altro tipo di
tratteggio, e si vede come considerando tutta l'area in cui è presente uno dei
due tratteggi si ottenga proprio $M \cup D$.

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
:label: ex-partizione

Considerate l'universo $\Omega$ e gli insiemi $A$, $B$ e $C$ definiti
nell’{ref}`ex-insiemi-base`.

1. Determinate se ciascuna delle seguenti famiglie è una partizione di
   $\Omega$, motivando la risposta.

   - $\mathcal{F}_1 = \{ A, B, C \}$.
   - $\mathcal{F}_2 = \{ A, \overline A\}$.
   - $\mathcal{F}_3 = \{ A \cap B, A \setminus B, \overline A \}$.
   - $\mathcal{F}_4 = \{ A \cap B, A \ominus B, \overline{A \cup B} \}$.
   - $\mathcal{F}_5 = \{ C, B \setminus C, \overline C \}$.

2. Trovate una partizione di $\Omega$ in quattro blocchi tale che uno dei
   blocchi sia $\{\text{Wolverine}, \text{Deadpool}\}$.

3. Determinate tutte le partizioni di $\Omega$ che contengono $A \ominus B$.
````

````{solution} ex-partizione
:class: dropdown

Richiamiamo gli insiemi dall’{ref}`ex-insiemi-base`:

```{math}
\begin{align*}
A &= \{\text{Batman}, \text{Thor}, \text{Deadpool}, \text{Cyborg}\},\\
B &= \{\text{Superman}, \text{Thor}, \text{Storm}, \text{Wolverine}\},\\
C &= \{\text{Batman}, \text{Deadpool}, \text{Cyborg}\}.
\end{align*}
```

1. Consideriamo i quattro casi separatamente.

   - $\mathcal{F}_2 = \{ A, B, C \}$ non è una partizione di $\Omega$, essendo
     $A$ e $B$ non disgiunti (contengono entrambi Thor), così come non lo sono
     $A$ e $C$ (che contengono Batman, Deadpool e Cyborg).
   - $\mathcal{F}_2 = \{ A, \overline A \}$ è una partizione di $\Omega$,
     per ogni insieme $A \subseteq \Omega$ non vuoto: $A$ e $\overline A$ sono
     disgiunti e la loro unione è $\Omega$.
   - $\mathcal{F}_3 = \{ A \cap B, A \setminus B, \overline A \}$ è una
     partizione di $\Omega$, formata dai tre blocchi $\{ \text{Thor} \}$,
     $\{ \text{Batman}, \text{Deadpool}, \text{Cyborg} \}$ e
     $\{ \text{Superman}, \text{Wolverine}, \text{Storm} \}$, che sono a due a
     due disgiunti e la cui unione è $\Omega$. Si noti che questo riflette la
     scomposizione $\Omega = (A \cap B) \cup (A \setminus B) \cup \overline A$,
     valida per qualsiasi coppia di insiemi $A, B$.
   - $\mathcal{F}_4 = \{ A \cap B, A \ominus B, \overline{A \cup B} \}$
     non è una partizione di $\Omega$: poiché $A \cup B = \Omega$, si ha
     $\overline{A \cup B} = \varnothing$, che è un blocco vuoto, e questo viola
     la definizione di partizione.
   - $\mathcal{F}_5 = \{ C, A \setminus C, \overline C \}$ non è una
     partizione di $\Omega$, in quanto $A \setminus C$ e $\overline C$ non sono
     disgiunti (contengono entrambi Thor).

2. Una possibile partizione in quattro blocchi che contiene
   $\{\text{Wolverine}, \text{Deadpool}\}$ come uno dei blocchi è la seguente:

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
   \{ \text{Thor} \}$, pertanto l'unica partizione possibile è 

```{math}
\bigl\{ A \ominus B, \{\text{Thor}\} \bigr\}.
```
````

