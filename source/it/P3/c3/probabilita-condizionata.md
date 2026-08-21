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

(sec_probabilita-condizionata)=
# Probabilità condizionata

Immaginiamo di fissare un esperimento casuale $\mathscr E$ e definire il
corrispondente spazio di probabilità $(\Omega, \mathsf A, \mathbb P)$. Dato
un generico evento $E \in \mathsf A$, se dopo che $\mathscr E$ è stato eseguito
noi sapessimo qual è l'esito $\omega \in \Omega$ che è stato osservato,
sapremmo automaticamente se $E$ si è verificato oppure no. Immaginiamo di non
conoscere con precisione $\omega$, ma di avere accesso a qualche forma
_parziale_ di informazione: più precisamente, supponiamo di sapere che si sia
verificato un altro evento $F$, e &mdash; sulla base di questa informazione
&mdash; di voler valutare se la probabilità di $E$ ne risulti in qualche modo
influenzata.


````{customfigure}
:name: fig-prob-cond-dadi-venn

```{code-cell} python
:tags: [hide-input]

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

rosso, blu = np.meshgrid(range(1, 7), range(1, 7))
rosso, blu = rosso.ravel(), blu.ravel()

in_e = rosso + blu >= 8
in_f = blu >= 4
in_intersezione = in_e & in_f
solo_e = in_e & ~in_f
solo_f = in_f & ~in_e
fuori = ~(in_e | in_f)

with mpl.rc_context({'figure.figsize': (3, 3),
           'figure.dpi': 150,
           'figure.titlesize': 8,
           'xtick.labelsize': 7,
           'ytick.labelsize': 7,
           'axes.labelsize': 7,}):

  fig, ax = plt.subplots()

  bg_color = '#eaf3f5'
  fill_color = '#d6e4f7'
  highlight = '#aac5e8'
  dot_color = '#2255aa'
  edge_color = '#333333'

  ax.set_facecolor(bg_color)

  ax.axhspan(3.5, 6.5, facecolor=fill_color, alpha=0.65, zorder=0)
  ax.add_patch(
    Polygon(
      [(1.0, 6.5), (6.5, 6.5), (6.5, 1.0)],
      closed=True,
      facecolor=highlight,
      edgecolor="none",
      alpha=0.6,
      zorder=0,
    )
  )

  ax.axhline(3.5, color=edge_color, linestyle="--", linewidth=1.0, zorder=1)
  ax.plot([1.0, 6.5], [6.5, 1.0], color=edge_color, linestyle="--",
    linewidth=1.0, zorder=1)

  ax.scatter(rosso[fuori], blu[fuori], s=20, c="white",
    edgecolors=edge_color, linewidths=0.5, zorder=3)
  ax.scatter(rosso[solo_e], blu[solo_e], s=20, c=highlight,
    edgecolors=edge_color, linewidths=0.5, zorder=4)
  ax.scatter(rosso[solo_f], blu[solo_f], s=20, c=fill_color,
    edgecolors=edge_color, linewidths=0.5, zorder=4)
  ax.scatter(rosso[in_intersezione], blu[in_intersezione],
    s=20, c=dot_color, edgecolors=edge_color, linewidths=0.5, zorder=5)

  ax.text(1.5, 4.5, r"$F \setminus E$", ha="center", va="center", fontsize=7)
  ax.text(4.5, 5.5, r"$E \cap F$", ha="center", va="center", fontsize=7)
  ax.text(5.85, 2.45, r"$E \setminus F$", ha="center", va="center", fontsize=7)

  ax.set_xlabel("Risultato del dado rosso")
  ax.set_ylabel("Risultato del dado blu")
  ax.set_xticks(range(1, 7))
  ax.set_yticks(range(1, 7))
  ax.set_xlim(0.5, 6.5)
  ax.set_ylim(0.5, 6.8)
  ax.grid(True, color=edge_color, alpha=0.12)
  ax.set_aspect("equal")
  plt.show()
```

Rappresentazione cartesiana degli eventi $E =$ «la somma dei due dadi è almeno
$8$» e $F =$ «il dado blu mostra almeno $4$» nel lancio di due dadi
distinguibili. I $36$ punti della griglia rappresentano gli esiti elementari di
$[1 .. 6]^2$.
````
```{prf:example}
:label: ex-prob-cond-justif

La {numref}`fig-prob-cond-dadi-venn` mostra lo spazio degli esiti nello
spazio di probabilità che descrive il risultato del lancio di due dadi
bilanciati e distinguibili, uno rosso e uno blu. Nella figura è evidenziato
il diagramma di Venn degli eventi $E =$ «la somma dei due risultati è almeno
$8$» e $F =$ «il risultato del dado blu è almeno $4$». In particolare, i cerchi
rispettivamente al di sopra e a destra delle linee tratteggiate gialla e blu
individuano esiti in $F$ e in $E$. Applicando la regola classica per il
calcolo delle probabilità, si ottiene $\mathbb P(E) = \frac{5}{12}$: dal
diagramma si vede infatti che esattamente quindici dei $36$ cerchi individuano
una somma dei risultati ottenuti che è maggiore o uguale a $8$. Analogamente,
è facile convincersi che $F$ si può verificare in $18$ modi diversi, dei quali
solo $12$ portano anche $E$ a verificarsi. Sapere quindi che $F$ si è
verificato aumenta la probabilità di $E$, portandola a $\frac{2}{3}$.
```

La _probabilità condizionata_ è uno strumento che ci permette di capire quanto,
in generale, l'incertezza su un evento $E$ venga modificata nel momento in cui
è noto che un altro evento si è verificato.

```{margin}
Oltre a garantire che il rapporto {eq}`eq_prob-cond` non abbia un denominatore
nullo, richiedere che $\mathbb P(F) \neq 0$ è strettamente legato al
significato di probabilità condizionata: l'unico evento con probabilità nulla è
quello impossibile, e dunque non ha senso ipotizzare che esso si sia
verificato.
```
````{prf:definition} Probabilità condizionata
:label: def-conditional_probability

Siano $E, F \in \mathsf A$ due eventi in uno spazio di probabilità
$(\Omega, \mathsf A, \mathbb P)$: se $\mathbb P(F) \neq 0$ si definisce
_probabilità condizionata di $E$ dato $F$_ (o, più brevemente, _probabilità di
$E$ dato $F$_) il rapporto

```{math}
:label: eq_prob-cond

\mathbb P(E \mid F) = \frac{\mathbb P(E \cap F)}{\mathbb P(F)}.
```

Quando invece $\mathbb P(F) = 0$, la probabilità $\mathbb P(E \mid F)$ è
indefinita.
````

La formula della definzione precedente si può leggere in modo molto concreto:
quando sappiamo che $F$ si è verificato, smettiamo di considerare tutti gli
esiti non contenuti in esso (che, per definizione, non possono essere stati
osservati) e ridistribuiamo la probabilità totale $1$ sui soli esiti
che restano. In questo senso, la probabilità condizionata non modifica
l'evento $E$, ma cambia l'universo di riferimento nel quale lo stiamo
misurando: quello che prima era $\Omega$, ora è diventato $F$.

````{admonition} Nota
:class: tip

Fissato un evento $B$ tale che $\mathbb P(B) \neq 0$, la funzione che a ogni
evento $A$ associa il valore $\mathbb P(A \mid B)$ si comporta a tutti gli
effetti come una nuova probabilità. In questo senso, condizionare rispetto a
$B$ equivale a introdurre un nuovo spazio di probabilità, nel quale
l'universo effettivo è $B$ e continuano a valere tutte le proprietà generali
già viste.

Per esempio, restano validi il teorema sull'evento complementare,

```{math}
\mathbb P(\overline A \mid B) = 1 - \mathbb P(A \mid B) \enspace,
```

o la formula generale per l'unione di due eventi,

```{math}
\mathbb P(A \cup C \mid B)
= \mathbb P(A \mid B) + \mathbb P(C \mid B) - \mathbb P(A \cap C \mid B)
\enspace.
```

In modo analogo, valgono anche la monotonia e tutte le altre proprietà che
discendono dagli assiomi di Kolmogorov, purché si legga la probabilità sempre
all'interno del contesto fissato da $B$.
````

In uno spazio equiprobabile, la {prf:ref}`def-conditional_probability` assume
una forma ancora più trasparente:

```{math}
\mathbb P(E \mid F) = \frac{|E \cap F|}{|F|} \enspace,
```

cioè la probabilità condizionata è semplicemente la proporzione degli esiti di
$F$ che appartengono anche a $E$.

````{prf:example} Due dadi e probabilità condizionata
:label: ex-prob-cond-dadi

Riconsiderando lo spazio di probabilità dell’{prf:ref}`ex-prob-cond-justif`,
e gli eventi $E$ e $F$, il diagramma di Venn in
{numref}`fig-prob-cond-dadi-venn` ci permette di verificare che

- $|F| = 18$, perché per il dado blu ci sono tre valori possibili ($4$, $5$ e
  $6$), mentre quello rosso può assumere qualunque valore in $[1 .. 6]$;
- $|E \cap F| = 12$, perché tra questi $18$ esiti ce ne sono $12$ in cui la
  somma è almeno $8$.

Ne segue che

```{math}
\mathbb P(E \mid F) = \frac{|E \cap F|}{|F|} = \frac{12}{18} = \frac{2}{3}
\enspace,
```

confermando quanto già ricavato nel precedente esercizio.
````

````{prf:example} Una teca di supereroi
:label: ex-prob-cond-supereroi

Supponiamo che Nick Fury estragga uniformemente una scheda da una teca che
contiene otto personaggi: Iron Man, Thor, Hulk, Black Widow, Superman, Wonder
Woman, Batman e Storm. Consideriamo gli eventi $V =$ «il personaggio sa volare»
e $S =$ «il personaggio ha super-forza». I personaggi in $V$ sono Iron Man,
Thor, Superman e Storm, quindi $|V| = 4$. Tra questi, quelli che appartengono
anche a $S$ sono Thor e Superman, dunque $|S \cap V| = 2$. Pertanto

```{math}
\mathbb P(S \mid V) = \frac{|S \cap V|}{|V|} = \frac{1}{2} \enspace.
```

L'informazione «il personaggio sa volare» riduce la nostra attenzione a quattro
schede; una volta ristretto l'universo a queste, la domanda diventa
semplicemente quale frazione di esse rappresenti un personaggio con super-forza.
````


## Regola di fattorizzazione

La definizione di probabilità condizionata si può riscrivere moltiplicando
i due membri di {eq}`eq_prob-cond` per $\mathbb P(F)$. In questo modo si
ottiene una formula che permette di calcolare la probabilità dell'intersezione
di due eventi, fattorizzandola in un prodotto di probabilità.

````{prf:theorem} Regola di fattorizzazione
:label: teo-factorization

Siano $E, F \in \mathsf A$ due eventi. Se $\mathbb P(F) \neq 0$, allora vale

```{math}
:label: eq-factorization

\mathbb P(E \cap F) = \mathbb P(F) \mathbb P(E \mid F) \enspace.
```

Se inoltre $\mathbb P(E) \neq 0$, allora si può scrivere anche

```{math}
\mathbb P(E \cap F) = \mathbb P(E) \mathbb P(F \mid E) \enspace.
```
````

Intuitivamente, la regola di fattorizzazione si legge molto bene da destra
verso sinistra: per far sì che si verifichino contemporaneamente $F$ ed $E$,
può accadere prima $F$, e poi, nel mondo in cui $F$ è vero, può accadere anche
$E$. La probabilità dell'intersezione viene quindi scomposta nel prodotto di
due termini, uno «esterno» e uno «interno» al caso considerato.


````{prf:example} Fattorizzare il caso dei due dadi
:label: ex-factorization-dice

Riprendiamo gli eventi dei due esempi precedenti. Siccome lo spazio di
probabilità considerato è equiprobabile, ispezionando il diagramma di Venn
della {numref}`fig-prob-cond-dadi-venn` si ottiene


```{math}
\mathbb P(F) = \frac{18}{36} = \frac{1}{2} \enspace.
```

Analogamente, dall’{prf:ref}`ex-prob-cond-dadi` sappiamo che
$\mathbb P(E \mid F) = \frac{12}{18} = \frac{2}{3}$: applicando la regola di
fattorizzazione otteniamo pertanto

```{math}
\mathbb P(E \cap F) = \mathbb P(F) \mathbb P(E \mid F)
= \frac{1}{2} \cdot \frac{2}{3} = \frac{1}{3} \enspace.
```

Il risultato coincide con il conteggio diretto degli esiti nell'intersezione
$E \cap F$, che sono $12$ su $36$. Il vantaggio della fattorizzazione è che il
calcolo diventa naturale anche quando non è immediato conteggiare il numero di
esiti nell'intersezione, ed è più facile ragionare prima nei termini di uno
degli eventi, considerando poi quello rimanente, condizionandone l'osservazione
a quella del primo.
````


## Teorema delle probabilità totali

Oltre che per calcolare la probabilità dell'intersezione di eventi, la regola
di fattorizzazione è utile quando vogliamo determinare $\mathbb P(E)$
distinguendo casi diversi. Cominciamo dal caso più semplice, in cui lo spazio
degli esiti è suddiviso in due parti distinte, descritte da un evento $F$ e
dal suo complementare $\overline{F}$. In questa situazione, ogni modo in cui
può verificarsi $E$ ricade necessariamente in uno dei due casi $E \cap F$
oppure $E \cap \overline{F}$. Più precisamente,

- per la proprietà distributiva dell'intersezione sull'unione, si ha
  $(E \cap F) \cup (E \cap \overline{F})
  = E \cap (F \cup \overline{F}) = E \cap \Omega = E$;
- l'associatività e la commutatività dell'intersezione implicano
  $(E \cap F) \cap (E \cap \overline{F})
  = E \cap (F \cap \overline{F}) = E \cap \varnothing = \varnothing$.

In altre parole, $E$ si può esprimere come l'unione dei due eventi disgiunti
$E \cap F$ ed $E \cap \overline{F}$, e dal terzo assioma di Kolmogorov si
ottiene

```{math}
\mathbb P(E) = \mathbb P(E \cap F) + \mathbb P(E \cap \overline{F})
\enspace,
```

come evidenziato nella {numref}`fig-prob-totali-binario`. Se inoltre
$0 < \mathbb P(F) < 1$, applicando la regola di fattorizzazione ai due addendi
otteniamo

```{math}
:label: eq-prob-totali-2

\mathbb P(E) = \mathbb P(E \mid F) \mathbb P(F)
             + \mathbb P(E \mid \overline{F}) \mathbb P(\overline{F})
             = \mathbb P(E \mid F) \mathbb P(F)
             + \mathbb P(E \mid \overline{F}) (1 - \mathbb P(F)) \enspace,
```

che rappresenta l'enunciato della forma più semplice del _teorema delle
probabilità totali_. Questa formula permette di calcolare la probabilità di
un evento relativamente complesso, che diventa più facile da gestire quando
lo si considera a fronte del risultato di un altro evento, che lo condiziona.
Più  precisamente, lo spazio campionario viene suddiviso in due casi
mutuamente esclusivi che esauriscono tutte le possibilità, e la probabilità di
$E$ si ottiene sommando i contributi di tutti questi casi.

```{code-cell} python
:tags: [hide-input]

from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon
from myst_nb import glue

MATH_SIZE = 9
EDGE_COLOR = '#333333'
BG_COLOR = '#eaf3f5'
FILL_COLOR = '#d6e4f7'
HIGHLIGHT = '#aac5e8'
BOX_X0, BOX_Y0 = 0.2, 0.2
BOX_W, BOX_H = 11.6, 7.6

E_XY = (6.0, 4.0)
E_W, E_H = 6.6, 4.1
LINE_TOP = (5.2, BOX_Y0 + BOX_H)
LINE_BOTTOM = (6.15, BOX_Y0)

fig, ax = plt.subplots(facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)

ax.add_patch(FancyBboxPatch((BOX_X0, BOX_Y0), BOX_W, BOX_H,
                            boxstyle='square,pad=0',
                            facecolor=BG_COLOR, edgecolor=EDGE_COLOR,
                            linewidth=1.1, zorder=0))

left_clip = Polygon([
  (BOX_X0, BOX_Y0),
  (BOX_X0, BOX_Y0 + BOX_H),
  LINE_TOP,
  LINE_BOTTOM,
], closed=True, facecolor='none', edgecolor='none')
right_clip = Polygon([
  LINE_TOP,
  (BOX_X0 + BOX_W, BOX_Y0 + BOX_H),
  (BOX_X0 + BOX_W, BOX_Y0),
  LINE_BOTTOM,
], closed=True, facecolor='none', edgecolor='none')
ax.add_patch(left_clip)
ax.add_patch(right_clip)

left_part = Ellipse(xy=E_XY, width=E_W, height=E_H,
          facecolor=FILL_COLOR, edgecolor='none', zorder=1)
right_part = Ellipse(xy=E_XY, width=E_W, height=E_H,
           facecolor=HIGHLIGHT, edgecolor='none', zorder=1)
ax.add_patch(left_part)
ax.add_patch(right_part)
left_part.set_clip_path(left_clip)
right_part.set_clip_path(right_clip)

ax.add_patch(Ellipse(xy=E_XY, width=E_W, height=E_H,
                      facecolor='none', edgecolor=EDGE_COLOR,
                      linewidth=1.2, zorder=4))
ax.plot([LINE_TOP[0], LINE_BOTTOM[0]], [LINE_TOP[1], LINE_BOTTOM[1]],
    color=EDGE_COLOR, linewidth=1.2, zorder=4)

ax.text(11.5, 7.5, r'$\Omega$', fontsize=MATH_SIZE, ha='right', va='top')
ax.text(11, 0.7, r'$F$', fontsize=MATH_SIZE, ha='center')
ax.text(1., 0.7, r'$\overline{F}$', fontsize=MATH_SIZE, ha='center')
ax.text(8.9, 5.8, r'$E$', fontsize=MATH_SIZE, ha='center')
ax.text(4.35, 3.73, r'$E \cap F$', fontsize=MATH_SIZE, ha='center')
ax.text(7.5, 3.73, r'$E \cap \overline{F}$', fontsize=MATH_SIZE, ha='center')

plt.tight_layout()
glue('prob-totali-binario', fig, display=False)
```
````{glue:figure} prob-totali-binario
:name: fig-prob-totali-binario

Diagramma di Venn per la forma più semplice del teorema delle probabilità
totali. Gli eventi $F$ e $\overline{F}$ formano una partizione di $\Omega$,
mentre l'evento $E$ si scompone nell'unione disgiunta di $E \cap F$ ed
$E \cap \overline{F}$.
````

````{prf:example}
:label: ex-total-probability-heroes

Un osservatorio segreto monitora le missioni di alcuni individui dell'universo
di {extlink}`Heroes <https://heroes.fandom.com/wiki/Heroes_Wiki>`, allo scopo
di individuare e prevenire paradossi temporali. In particolare, le missioni
vengono divise in due categorie:

- missioni ad alta instabilità, affidate a personaggi delle cui azioni è
  difficile prevedere l'effetto (come Hiro Nakamura, che manipola spazio e
  tempo, o Peter Petrelli, che può replicare i poteri delle persone vicine);

- missioni a instabilità moderata, gestite da personaggi con poteri più
  controllabili (per esempio Claire Bennet, che è in grado di rigenerarsi, o
  Matt Parkman, che possiede capacità telepatiche).

La probabilità che si verifichi un paradosso temporale è $0.35$ per le missioni
ad alta instabilità e $0.1$ in quelle a instabilità moderata. Inoltre, un
quarto di tutte le missioni è ad alta instabilità.

La probabilità dell'evento $P$ che si verifica quando durante una missione
viene generato un paradosso temporale si può calcolare applicando
{eq}`eq-prob-totali-2`:

```{math}
\mathbb P(P) = \mathbb P(P \mid A) P(A) + \mathbb P(P \mid M) \mathbb P(M)
= 0.35 \cdot 0.25 + 0.10 \cdot 0.75 = 0.1625 \enspace.
```

In altre parole, anche se solo una parte relativamente piccola delle missioni
coinvolge poteri molto instabili, questi incidono molto sul rischio complessivo
perché hanno una probabilità decisamente più alta di generare paradossi
temporali.
````

```{code-cell} python
:tags: [hide-input]

from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon

MATH_SIZE = 9
EDGE_COLOR = '#333333'
BG_COLOR = '#eaf3f5'
PART_COLORS = ['#d6e4f7', '#c5d8f0', '#aac5e8', '#8eb3dc']
BOX_X0, BOX_Y0 = 0.2, 0.2
BOX_W, BOX_H = 11.6, 7.6

E_XY = (6.0, 4.0)
E_W, E_H = 8.8, 4.0
TOP_X = [BOX_X0, 3.6, 5.7, 7.9, BOX_X0 + BOX_W]
BOTTOM_X = [BOX_X0, 4.4, 6.4, 8.6, BOX_X0 + BOX_W]

fig, ax = plt.subplots(facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)

ax.add_patch(FancyBboxPatch((BOX_X0, BOX_Y0), BOX_W, BOX_H,
              boxstyle='square,pad=0',
              facecolor=BG_COLOR, edgecolor=EDGE_COLOR,
              linewidth=1.1, zorder=0))

clips = []
for index in range(4):
  clip = Polygon([
      (TOP_X[index], BOX_Y0 + BOX_H),
      (TOP_X[index + 1], BOX_Y0 + BOX_H),
      (BOTTOM_X[index + 1], BOX_Y0),
      (BOTTOM_X[index], BOX_Y0),
  ], closed=True, facecolor='none', edgecolor='none')
  ax.add_patch(clip)
  clips.append(clip)

for color, clip in zip(PART_COLORS, clips):
  part = Ellipse(xy=E_XY, width=E_W, height=E_H,
          facecolor=color, edgecolor='none', zorder=1)
  ax.add_patch(part)
  part.set_clip_path(clip)

ax.add_patch(Ellipse(xy=E_XY, width=E_W, height=E_H,
            facecolor='none', edgecolor=EDGE_COLOR,
            linewidth=1.2, zorder=4))

for top_x, bottom_x in zip(TOP_X[1:-1], BOTTOM_X[1:-1]):
  ax.plot([top_x, bottom_x], [BOX_Y0 + BOX_H, BOX_Y0],
          color=EDGE_COLOR, linewidth=1.2, zorder=4)

ax.text(11.5, 7.5, r'$\Omega$', fontsize=MATH_SIZE, ha='right', va='top')
ax.text(2.0, 0.7, r'$F_1$', fontsize=MATH_SIZE, ha='center')
ax.text(4.95, 0.7, r'$F_2$', fontsize=MATH_SIZE, ha='center')
ax.text(7.35, 0.7, r'$F_3$', fontsize=MATH_SIZE, ha='center')
ax.text(10.2, 0.7, r'$F_4$', fontsize=MATH_SIZE, ha='center')
ax.text(2.0, 5.65, r'$E$', fontsize=MATH_SIZE, ha='center')
ax.text(2.9, 3.8, r'$E \cap F_1$', fontsize=MATH_SIZE, ha='center')
ax.text(5.1, 3.8, r'$E \cap F_2$', fontsize=MATH_SIZE, ha='center')
ax.text(7.1, 3.8, r'$E \cap F_3$', fontsize=MATH_SIZE, ha='center')
ax.text(9.15, 3.8, r'$E \cap F_4$', fontsize=MATH_SIZE, ha='center')

plt.tight_layout()
glue('prob-totali-partizione', fig, display=False)
```
````{glue:figure} prob-totali-partizione
:name: fig-prob-totali-partizione

Diagramma di Venn schematico per il teorema delle probabilità totali, quando
viene considerata la partizione $\mathcal P = \{ F_1, F_2, F_3, F_4 \}$ di
$\Omega$.
````

La formulazione generale del teorema delle probabilità totali estende il
ragionamento fatto finora, considerando più di due possibili alternative.
Come evidenziato nella {numref}`fig-prob-totali-partizione`, ciò equivale a
ragionare nei termini di una partizione $\mathcal P$ di $\Omega$. Anche in
questo caso, ogni parte di $E$ sarà contenuta al più in uno e un solo blocco
della partizione, e la probabilità si ottiene sommando i contributi dei blocchi
di quest'ultima.

````{prf:theorem} Teorema delle probabilità totali
:label: teo-total-probability

Sia $\mathcal P = \{ F_1, \dots, F_n \}$ una partizione di $\Omega$ composta
da eventi $F_i \in \mathsf A$, tali che $\mathbb P(F_i) \neq 0$, per ogni
$i = 1, \dots, n$. Fissato un generico $E \in \mathsf A$, vale

```{math}
:label: eq-total-probability

\mathbb P(E) = \sum_{i=1}^n \mathbb P(E \mid F_i) \mathbb P(F_i) \enspace.
```
````
````{sds-proof}
Come si evince anche dalla {numref}`fig-prob-totali-partizione`, per ogni
$i \neq j$ si ha $(E \cap F_i) \cap (E \cap F_j) = E \cap (F_i \cap F_j)
= E \cap \varnothing = \varnothing$, tenuto conto dell'associativitià e della
commutatività dell'intersezione. Inoltre, considerando la distributività
dell'intersezione sull'unione, si ha

```{math}
\bigcup_{i=1}^n (E \cap F_i) = E \cap \bigcup_{i=1}^n F_i = E \cap \Omega = E
\enspace,
```

il che permette di esprimere $E$ come l'unione di eventi disgiunti, e dunque
di calcolarne la probabilità come

```{math}
\mathbb P(E) = \sum_{i=1}^n \mathbb P(E \cap F_i) \enspace.
```

Per ogni $i = 1, \dots, n$ si ha per ipotesi $\mathbb P(F_i) \neq 0$, e la
regola di fattorizzazione implica $\mathbb P(E \cap F_i) =
\mathbb P(E \mid F_i) \mathbb P(F_i)$, da cui si ottiene la tesi.
````

Anche in questo caso, la scelta di $\mathcal P$ rappresenta una parte molto
importante del ragionamento: bisogna considerare una partizione che rende il
calcolo delle probabilità condizionate $\mathbb P(E \mid F_i)$ più facile
rispetto a quella di $\mathbb P(E)$.

````{prf:example} Scegliere un dado tra tre
:label: ex-total-probability-three-dice

Consideriamo tre dadi bilanciati a sei facce: il primo è un dado ordinario con
le facce numerate da $1$ a $6$; il secondo ha le facce numerate come $1$, $3$,
$4$, $5$, $5$ e $6$; il terzo ha le facce numerate con $2$, $4$, $5$, $5$, $6$
e $6$. Indichiamo con $D_1$, $D_2$ e $D_3$ gli eventi che si verificano,
rispettivamente, quando viene scelto il primo, il secondo e il terzo dado, e
supponiamo che le relative probabilità siano $\mathbb P(D_1) = \frac{1}{2}$,
$\mathbb P(D_2) = \frac{1}{3}$ e $\mathbb P(D_3) = \frac{1}{6}$.

Immaginiamo di selezionare uno dei tre dadi con queste probabilità, e di
lanciarlo. Sia $E =$ «il risultato del lancio è almeno $5$». Allora

```{math}
\mathbb P(E \mid D_1) = \frac{2}{6} = \frac{1}{3},
\qquad
\mathbb P(E \mid D_2) = \frac{3}{6} = \frac{1}{2} \text{ e }
\qquad
\mathbb P(E \mid D_3) = \frac{4}{6} = \frac{2}{3} \enspace.
```

Poiché $\{ D_1, D_2, D_3 \}$ è una partizione dello spazio degli eventi che non
contiene l'insieme vuoto, apllicando il teorema delle probabilità totali si
ottiene

```{math}
\mathbb P(E)
= \mathbb P(E \mid D_1)\mathbb P(D_1)
 + \mathbb P(E \mid D_2)\mathbb P(D_2)
 + \mathbb P(E \mid D_3)\mathbb P(D_3)
= \frac{1}{3} \cdot \frac{1}{2}
 + \frac{1}{2} \cdot \frac{1}{3}
 + \frac{2}{3} \cdot \frac{1}{6}
= \frac{4}{9} \enspace.
```

La formula finale nell'esempio precedente mette in risalto un'altra
interpretazione del teorema delle probabilità totali: la probabilità di $E$ si
può esprimere come la media delle tre probabilità condizionate, pesata rispetto
alle probabilità degli eventi $D_1$, $D_2$ e $D_3$.
````

````{prf:example} Volare, distinguendo per universo narrativo
:label: ex-total-probability-fly

Consideriamo nove schede che descrivono Iron Man, Thor, Hulk, Black Widow,
Wolverine, Storm, Batman, Superman e Invincible, e immaginiamo di selezionarne
una dopo averle mischiate, in modo che ogni scheda abbia la stessa probabilità
di essere estratta. Sia $V =$ «la scheda riguarda un eroe che sa volare», e
immaginiamo di volerne calcolare la probabilità. Consideriamo la seguente
suddivisione dello spazio campionario in tre sottoinsiemi:

- $M =$ «è stata estrata la scheda di un eroe Marvel» (dunque uno tra i primi
  sei nell'elenco iniziale);
- $D =$ «è stata estrata la scheda di un eroe DC» (Batman o Superman);
- $I =$ «è stata estrata la scheda di un eroe Image Comics» (che deve
  necessariamente essere Invincible, perché è l'unico eroe Image Comics
  nell'elenco).

È chiaro che $\{ M, D, I \}$ rappresenta una partizione di $\Omega$, con

```{math}
\mathbb P(M) = \frac{6}{9},
\qquad
\mathbb P(D) = \frac{2}{9} \text{ e }
\qquad
\mathbb P(I) = \frac{1}{9} \enspace,
```

dunque una partizione che permette di considerare l'applicazione del teorema
delle probabilità totali, in quanto nessun evento ha probabiltà nulla. Inoltre,

- tra i personaggi Marvel volano Iron Man, Thor e Storm, dunque
  $\mathbb P(V \mid M) = 3/6 = 1/2$;
- tra i personaggi DC vola solo Superman, quindi
  $\mathbb P(V \mid D) = 1/2$;
- l'unico personaggio Image è Invincible, che vola, quindi
  $\mathbb P(V \mid I) = 1$.

Applicando il teorema delle probabilità totali otteniamo

```{math}

\mathbb P(V)= \mathbb P(V \mid M)\mathbb P(M)
 + \mathbb P(V \mid D)\mathbb P(D)
 + \mathbb P(V \mid I)\mathbb P(I)
= \frac{1}{2} \cdot \frac{6}{9}
 + \frac{1}{2} \cdot \frac{2}{9}
 + 1 \cdot \frac{1}{9}
= \frac{5}{9} \enspace.
```

Naturalmente, si otterrebbe il medesimo risultato anche contando direttamente
quanti tra i personaggi elencati sanno volare, e applicando la regola classica
per il calcolo delle probabilità. Il vantaggio del teorema delle probabilità
totali è quello di organizzare il calcolo per casi: un'idea che tornerà utile
ogni volta che le probabilità condizionate risultano più facili da calcolare
rispetto alla probabilità che non conosciamo.
````

````{prf:example}
:label: ex-tot-prob-xmen

Il Professor X sospetta che alcuni allievi della scuola ospitata nella
{extlink}`X-mansion
<https://marvel.fandom.com/wiki/Xavier%27s_School_for_Gifted_Youngsters>` abbiano
usato le proprie abilità per alterare i risultati degli esami di fine anno.
Per farsi un'idea di quanti tra essi lo abbiano fatto, senza esporre nessuno,
organizza la seguente rilevazione: in un'urna vengono poste cento sfere,
numerate da uno a $100$. Ogni allievo estrae una sfera e osserva il numero
riportato, senza che nessuno possa sapere di quale numero si tratti. Se tale
numero è minore o uguale a $70$, allora l'allievo risponde alla domanda
«Hai usato i tuoi poteri per cambiare il risultato dell'esame?». Altrimenti,
risponde alla _domanda di controllo_ «Il numero che hai estratto è pari?».
In entrambi i casi, la risposta deve essere «sì» oppure «no» e la sfera deve
essere reinserita nell'urna. Questo modo di procedere garantisce che, anche
conoscendo la risposta data da ogni singolo studente, il Prof. X non possa
sapere a quale domanda si riferisce. Così facendo, vengono incentivate risposte
sincere, in funzione dell'anonimità garantita dal protocollo adottato.

Ipotizzando che l'estrazione delle sfere avvenga in un contesto equiprobabile,
la probabilità dell'evento $C =$ «è stata data risposta alla domanda di
controllo» è $\frac{3}{10}$. Indichiamo con $S$ l'evento «si osserva una
risposta affermativa». Poiché tra le cento sfere ce ne sono cinquanta con un
numero pari e cinquanta con un numero dispari, si ha
$\mathbb P(S \mid C) = \frac{1}{2}$. Infine, $\{ C, \overline C \}$ è una
partizione dello spazio degli eventi che non contiene $\varnothing$, quindi
il teorema delle probabilità totali ci dice che

```{math}
\mathbb P(S) = \mathbb P(S \mid C) \mathbb P(C) +
\mathbb P(S \mid \overline C) \mathbb P(\overline C) \enspace,
```

ovvero $\mathbb P(S) = \frac{1}{2} \cdot \frac{3}{10} +
\mathbb P(S \mid \overline C) \cdot \frac{7}{10}$, o equivalentemente

```{math}
:label: eq-rand-resp

\mathbb P(S \mid \overline C) = \frac{10}{7} \left( \mathbb P(S) - \frac{3}{20}
\right) \enspace.
```

```{margin}
In generale, quando una probabilità teorica viene approssimata mediante una
frequenza relativa osservata, si dice che si effettua un procedimento di
_stima_. Studieremo in modo sistematico questo tipo di procedimento nell'ultima
parte del libro.
```

Supponiamo ora che, al termine del sondaggio, $25$ risposte su $100$ siano
«sì». Nell'accezione frequentista della probabilità, e assumendo che il numero
complessivo di risposte sia abbastanza grande, possiamo considerare la
frequenza relativa osservata, $\frac{25}{100} = \frac{1}{4}$, come una buona
approssimazione di $\mathbb P(S)$. Sostituendo questo valore in
{eq}`eq-rand-resp` otteniamo $\mathbb P(S \mid \overline C) \approx
\frac{1}{7}$, il che suggerisce che circa un settimo degli allievi abbia
usato i propri poteri per alterare il risultato dell'esame
(approssimativamente il $14 \%$).
````

````{admonition} Metodo della risposta randomizzata
:class: tip

Il procedimento illustrato in questo esempio è noto come _metodo della
risposta randomizzata_ {cite:p}`warner1965`. Si tratta di una tecnica di
rilevazione statistica progettata per raccogliere dati veritieri su argomenti
delicati, nei quali il timore di essere riconosciuti può indurre i partecipanti
a mentire o a rifiutarsi di rispondere. Esempi di argomenti delicati includono:

- il consumo di sostanze stupefacenti o l'abuso di alcol;
- l'evasione fiscale o i comportamenti illegali sul lavoro;
- le pratiche sessuali a rischio;
- episodi di bullismo o di violenza subita;
- l'uso scorretto di risorse accademiche (plagio, copiatura).

Il principio è semplice: un meccanismo casuale nel quale i rispondenti hanno
fiducia (come il lancio di una moneta o l'estrazione da un'urna) decide ogni
volta quale domanda riceve un partecipante. Chi somministra il sondaggio
conosce solo la risposta («sì» oppure «no»), non la domanda, e quindi non può
risalire al comportamento del singolo. In questo modo, la sincerità è
incentivata strutturalmente, e non affidata alla buona volontà.

È importante sottolineare che {eq}`eq-rand-resp` è un'identità esatta quando
si conosce davvero $\mathbb P(S)$. Nell'esempio, però, $\mathbb P(S)$ viene
rimpiazzata con la frequenza relativa delle risposte affermative, assumendo
che il numero complessivo di risposte sia abbastanza grande perché, in ottica
frequentista, tale frequenza approssimi bene la probabilità corrispondente. In
questo passaggio il valore risultante potrebbe, in linea di principio, essere
minore di $0$ o maggiore di $1$. Ciò avviene tipicamente quando il numero di
risposte raccolte non è sufficientemente elevato, ma anche quando il numero di
risposte affermative osservate è troppo lontano da quello atteso sotto le
ipotesi del modello.
````

````{prf:example}
:label: ex-tot-prob-misfits

Il quartiere di Wertham è sorvegliato da tre squadre di
{extlink}`Misfits <https://e4-misfits.fandom.com/wiki/Misfits_Wiki>`,
formate in anni diversi nel corso dei servizi sociali obbligatori. Il prospetto
seguente indica le percentuali degli interventi gestite da ciascuna squadra,
unitamente al tasso di interventi che si concludono in modo disastroso &mdash;
per colpa dei poteri ancora non padroneggiati.

| Squadra | Componenti | Quota di interventi | Tasso di disastri |
|:-:|:-------------------------------------:|:----:|:---:|
| A | Nathan, Simon, Alisha, Kelly e Curtis | 55 % | 3 % |
| B | Rudy e Seth                           | 30 % | 4 % |
| C | Finn, Jess e Abbey                    | 15 % | 5 % |


Indichiamo con $A$, $B$ e $C$ gli eventi che corrispondono al fatto che
un intervento sia stato gestito dalla squadra omonima, e con $D$ l'evento
«l'intervento si è concluso in modo disastroso». Le probabilità dei primi tre
eventi si ricavano immediatamente dal prospetto precedente:
$\mathbb P(A) = 0.55$, $\mathbb P(B) = 0.30$ e $\mathbb P(C) = 0.15$. La
probabilità di $D$ si può ricavare a partire da queste ultime, applicando il
teorema delle probabilità totali. Infatti $\{ A, B, C \}$ è una partizione
dello spazio degli esiti, in quanto ogni intervento è affidato a una e una sola
squadra. I dati a disposizione definiscono inoltre la probabilità di un
intervento disastroso, condizionato rispetto alla squadra che lo ha preso in
carico: $\mathbb P(D \mid A) = 0.03$, $\mathbb P(D \mid B) = 0.04$ e
$\mathbb P(D \mid C) = 0.05$. Nessuna delle probabilità degli eventi
condizionanti è nulla, quindi

```{math}
\begin{align*}
\mathbb P(D) &= \mathbb P(D \mid A) \mathbb P(A) +
                \mathbb P(D \mid B) \mathbb P(B) +
                \mathbb P(D \mid C) \mathbb P(C) \\
             &= 0.03 \cdot 0.55 + 0.04 \cdot 0.30 + 0.05 \cdot 0.15 = 0.036
                \enspace.
\end{align*}
```

La probabilità che un intervento scelto a caso si concluda in modo disastroso
corrisponde al $3.6 \%$ del totale. Ciò è dovuto al fatto che la squadra C,
che è quella meno efficiente, ha un peso sul totale degli interventi molto
ridotto ($15 \%$) e contribuisce solo per $0.75$ punti percentuali al risultato
finale. È invece la squadra A &mdash; quella più affidabile &mdash; a pesare
di più sul risultato complessivo, proprio perché gestisce la maggioranza
degli interventi. Intuitivamente, quando si è in presenza di più fonti, il
rischio complessivo dipende non solo dai tassi specifici di ciascuna di esse,
ma anche dalla loro quota di contributo al totale.
````


## Teorema di Bayes

Le formule viste finora permettono di calcolare quantità come
$\mathbb P(E \mid F)$, cioè la probabilità di $E$ quando sappiamo che vale
$F$. È importante però non attribuire automaticamente a questa scrittura un
significato temporale: condizionare rispetto a $F$ non vuol dire
necessariamente che prima accada $F$ e poi accada $E$. Più spesso, il legame
tra i due eventi è di natura causale, piuttosto che temporale: $F$ rappresenta
un'ipotesi, una causa o una condizione che aiuta a spiegare perché $E$ sia più
o meno plausibile. Proprio per questo ha senso anche scambiare i due ruoli.
In molte situazioni conosciamo infatti la probabilità dell'effetto $E$ sotto
una certa ipotesi $F$, cioè $\mathbb P(E \mid F)$, ma dopo avere osservato $E$
vogliamo risalire a quanto diventi plausibile l'ipotesi stessa, cioè a
$\mathbb P(F \mid E)$. 

```{prf:example}
:label: ex-bayes-intro

Supponiamo di essere coinvolti in una campagna di test clinici, volti a
valutare la presenza di una specifica condizione (per esempio un'infezione, una
carenza ormonale o una mutazione genetica). Indichiamo con $C$ l'evento che si
verifica quando la condizione è presente in un individuo, e con $P$ l'evento
che corrisponde a un test positivo su un individuo. Di solito si conosce bene
$\mathbb P(P \mid C)$, cioè la probabilità che il test individui la condizione
quando essa è davvero presente. Per chi riceve il referto, però, la domanda più
interessante è quella inversa: se il test è positivo, qual è la probabilità che
la condizione ci sia davvero, cioè quanto vale $\mathbb P(C \mid P)$? In questo
caso non stiamo invertendo un ordine temporale, ma un nesso esplicativo: la
condizione, se presente, spiega la positività del test, e dall'effetto
osservato cerchiamo di risalire alla possibile causa.
```

Il teorema di Bayes permette di calcolare le probabilità condizionate proprio
quando si effettua questo cambio di prospettiva. Nella formulazione più
semplice, il condizionamento viene fatto in termini di due possibili opzioni,
come indicato nel teorema seguente.

````{prf:theorem} Teorema di Bayes I
:label: teo-bayes

Siano $E, F \in \mathsf A$ due eventi tali che $\mathbb P(E) \neq 0$ e
$0 < \mathbb P(F) < 1$. Allora

```{math}
:label: eq-bayes

\mathbb P(F \mid E) =
\frac{\mathbb P(E \mid F)\mathbb P(F)}
     {\mathbb P(E \mid F)\mathbb P(F)
  + \mathbb P(E \mid \overline{F})\mathbb P(\overline{F})}
\enspace.
```
````

````{sds-proof}
Dalla definizione di probabilità condizionata, applicando la regola di
fattorizzazione si ottiene

```{math}
\mathbb P(F \mid E) = \frac{\mathbb P(E \cap F)}{\mathbb P(E)}
                     = \frac{\mathbb P(E \mid F)\mathbb P(F)}{\mathbb P(E)}
\enspace,
```

e poiché $\{ F, \overline{F} \}$ è una partizione di $\Omega$ che permette
l'applicazione del teorema delle probabilità totali,

```{math}
\mathbb P(E) = \mathbb P(E \mid F)\mathbb P(F)
             + \mathbb P(E \mid \overline{F})\mathbb P(\overline{F})
\enspace.
```

Sostituendo questa espressione nel denominatore si ottiene la tesi.
````

La formula alla base del teorema si può interpretare nel modo seguente.
Il numeratore valuta quanto è probabilità che $E$ si verifichi simultaneamente all'ipotesi $F$. Il denominatore confronta questo contributo con quello dell'ipotesi alternativa, che coinvolge $\overline{F}$. Se $E$ è molto più
probabile sotto l'ipotesi $F$ che sotto $\overline{F}$, allora l'osservazione
di $E$ tende ad aumentare il valore di $\mathbb P(F \mid E)$. Viceversa, se
è più probabile osservare $E$ in concomitanza con $\overline{F}$, il
verificarsi del primo evento andrà a diminuire la probabilità condizionata.

```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Thomas_Bayes.gif/250px-Thomas_Bayes.gif
---
figclass: margin
name: fig_thomas_bayes
width: 200px
align: left
---
Ritratto ritenuto raffigurare Thomas Bayes (Autore ignoto, attribuzione del soggetto incerta. Immagine di pubblico dominio. Fonte: {extlink}`Wikimedia
Commons <https://commons.wikimedia.org/wiki/File:Thomas_Bayes.gif>`).
```

````{admonition} Nomenclatura
:class: naming

L’espressione _teorema di Bayes_ fa riferimento a Thomas Bayes, ministro
presbiteriano e matematico inglese, presumibilmente ritratto[^ubayes] nella
{numref}`fig_thomas_bayes`. Il risultato è associato al suo saggio postumo _An
Essay Towards Solving a Problem in the Doctrine of Chances_ {cite:p}`bayes`,
comunicato alla Royal Society nel 1763 dal suo amico Richard Price. La forma
oggi più diffusa è però il frutto di successive riformulazioni e
generalizzazioni, dovute in particolare a Pierre-Simon Laplace. Per questo,
nella letteratura si incontrano anche le espressioni _formula di Bayes_,
_regola di Bayes_ e, talvolta, _formula_ o _teorema di Bayes-Laplace_.
````

````{prf:example} Un test clinico
:label: ex-bayes-clinical-test

```{margin}
Nel linguaggio dei test diagnostici, $\mathbb P(P \mid C)$ si chiama
_sensibilità_ (o _sensitività_), mentre
$\mathbb P(\overline{P} \mid \overline{C})$ si chiama _specificità_. Di
conseguenza, il tasso di falsi positivi è
$\mathbb P(P \mid \overline{C}) = 1 - \mathbb P(\overline{P} \mid
\overline{C})$.
```
Riprendendo l’{prf:ref}`ex-bayes-intro`, supponiamo che:

- la condizione oggetto del test sia presente in un generico individuo con
  probabilità $\mathbb P(C) = 0.001$ (cioè nel $0.1 \%$ dei casi);
- il test sia positivo nel $99 \%$ dei casi in cui la condizione è presente,
  cioè $\mathbb P(P \mid C) = 0.99$;
- il tasso di falsi positivi del test sia dell’$1 \%$, cioè
  $\mathbb P(P \mid \overline{C}) = 0.01$.

Applicando il teorema di Bayes si ricava la probabilità $\mathbb P(C \mid P)$:

```{math}
\mathbb P(C \mid P) =
\frac{0.99 \cdot 0.001}{0.99 \cdot 0.001 + 0.01 \cdot 0.999} \approx 0.09
\enspace.
```

Quindi, a fronte di un test positivo, la probabilità che la condizione sia
presente in un individuo è solo di circa il $9\%$. Il punto cruciale è che la
condizione resta molto rara nella popolazione, e quindi i falsi positivi,
pur pochi in termini relativi, possono superare i veri positivi in valore
assoluto. Anche in questo caso, non stiamo invertendo una sequenza temporale:
il test positivo è l'evidenza osservata, mentre la condizione è l'ipotesi
causale a cui vogliamo risalire.
````

Il risultato può sembrare sorprendente, e infatti viene talvolta presentato
come un piccolo paradosso: è un caso tipico di ciò che si discute sotto il
nome di {extlink}`fallacia del tasso di
base <https://it.wikipedia.org/wiki/Fallacia_del_tasso_di_base>`. Un test che
sembra molto affidabile non basta, da solo, a rendere probabile una condizione
che è per sua natura molto rara. L'interpretazione frequentista può aiutare a
comprendere meglio questo punto. Se immaginiamo di sottoporre al test $2\,000$
individui, ci aspettiamo in media che la condizione sia presente in circa due
persone (lo $0.1 \%$ di $2\,000$). Di queste, il $99 \%$ risulterà positivo: i
conti ci dicono che dovrebbero essere $0.99 \cdot 2 = 1.98$ individui, ma
dobbiamo pensare in termini di numeri interi. Arrotondiamo quindi il risultato
e diciamo che saranno positivi al test entrambi gli individui. Nei restanti
$1998$, la condizione non è presente, ma il tasso di falsi positivi fa sì che
venga erroneamente rilevata in venti di essi &mdash; anche in questo caso, il
numero previsto dalla formula sarebbe $0.01 \cdot 1\,998 = 19.98$, ma va
arrotondato. Concludendo, ci aspettiamo circa $22$ test positivi, a fronte di
due soli individui in cui la condizione è presente: calcolando il rapporto tra
questi valori si ottiene $2/22 \approx 9\%$, che è coerente con il valore di
$\mathbb P(C \mid P)$ ottenuto applicando il teorema di Bayes.

````{prf:example} Due dadi: Bayes con due ipotesi
:label: ex-bayes-dice

Riconsideriamo l'esperimento che consiste nel lanciare due dadi bilanciati e
distinguibili, e in particolare gli eventi $E =$ «la somma dei due risultati è almeno $8$» e $F =$ «il dado blu mostra almeno $4$».
Nell’{prf:ref}`ex-prob-cond-dadi` abbiamo visto che
$\mathbb P(E \mid F) = \frac{2}{3}$, e dalla {numref}`fig-prob-cond-dadi-venn`
è facile convincersi del fatto che $\mathbb P(F) = \frac{1}{2}$. Immaginiamo
di voler calcolare $\mathbb P(F \mid E)$, e cioè la probabilità che il
risultato del dado blu sia almeno $4$, sapendo che la somma dei risultati è
maggiore o uguale a otto. Per applicare il teorema di Bayes è necessario
valutare preventivamente $\mathbb P(E \mid \overline F)$: sempre ispezionando
il diagramma di Venn, si vede che dei diciotto esiti nei quali il risultato
del dado blu è al più uguale a $3$, solamente per $(6, 2)$, $(5, 3)$ e $(6, 3)$
la somma è almeno $8$ solo in , quindi
$\mathbb P(E \mid \overline{F}) = \frac{1}{6}$, e

```{math}
\mathbb P(F \mid E)
= \frac{\mathbb P(E \mid F)\mathbb P(F)}
  {\mathbb P(E \mid F)\mathbb P(F)
   + \mathbb P(E \mid \overline{F})\mathbb P(\overline{F})}
= \frac{\frac{2}{3} \cdot \frac{1}{2}}
  {\frac{2}{3} \cdot \frac{1}{2} + \frac{1}{6} \cdot \frac{1}{2}}
= \frac{4}{5} \enspace.
```

Quindi, sapendo che la somma è almeno $8$, la probabilità che il dado blu abbia
mostrato almeno $4$ è pari a $4/5$. 
````

L'esempio precedente mostra che, in generale,
$\mathbb P(E \mid F) \neq \mathbb P(F \mid E)$: nel caso in questione, infatti,
$\mathbb P(E \mid F) = 2/3$, mentre $\mathbb P(F \mid E) = 4/5$.

Il risultato del teorema di Bayes si estende facilmente al caso in cui il
condizionamento riguardi più di due ipotesi possibili. Il ragionamento da
seguire resta lo stesso, ma al posto della coppia $F$, $\overline{F}$ si
considera una generica partizione dello spazio degli esiti.

````{prf:theorem} Teorema di Bayes II
:label: teo-bayes-general

Sia $\mathcal P = \{ F_1, \dots, F_n \}$ una partizione di $\Omega$ i cui
blocchi sono membri dell'algebra $\mathsf A$ e hanno probabilità non nulla. Se
$E \in \mathsf A$ è un evento tale che $\mathbb P(E) \neq 0$, allora per ogni
$i = 1, \dots, n$ vale

```{math}
:label: eq-bayes-general

\mathbb P(F_i \mid E)
= \frac{\mathbb P(E \mid F_i)\mathbb P(F_i)}
  {\sum_{j=1}^n \mathbb P(E \mid F_j)\mathbb P(F_j)}
\enspace.
```
````

````{sds-proof}
Partendo dalla definizione di probabilità condizionata, sfruttando la
commutatività dell'intersezione e applicando la regola di fattorizzazione si ha

```{math}
\mathbb P(F_i \mid E)
= \frac{\mathbb P(E \cap F_i)}{\mathbb P(E)}
= \frac{\mathbb P(E \mid F_i)\mathbb P(F_i)}{\mathbb P(E)}
\enspace.
```

Poiché $\mathcal P$ permette di applicare il teorema delle probabilità totali,
si ha che

```{math}
\mathbb P(E) = \sum_{j=1}^n \mathbb P(E \mid F_j)\mathbb P(F_j) \enspace,
```

e sostituendo questa espressione nel denominatore della formula precedente si
 ottiene la tesi.
````

````{prf:example} Un personaggio volante di quale editore è?
:label: ex-bayes-heroes

Riconsideriamo le schede dell’{prf:ref}`ex-total-probability-fly`, in cui
abbiamo indicato con $M$, $D$ e $I$ gli eventi che corrispondono
rispettivamente all'estrazione di un personaggio Marvel, DC e Image Comics, e
con $V$ l'evento «il personaggio sa volare». Abbiamo già visto che

```{math}
\mathbb P(V \mid M) = \frac{1}{2},
\qquad
\mathbb P(V \mid D) = \frac{1}{2},
\qquad
\mathbb P(V \mid I) = 1,
\qquad
\mathbb P(M) = \frac{6}{9},
\qquad
\mathbb P(D) = \frac{2}{9} \text{ e}
\qquad
\mathbb P(I) = \frac{1}{9} \enspace.
```

Siccome $\{ M, D, I \}$ formano una partizione di $\Omega$ che permette
l'applicazione del teorema di Bayes, avremo

```{math}
\mathbb P(M \mid V)
= \frac{\mathbb P(V \mid M)\mathbb P(M)}
  {\mathbb P(V \mid M)\mathbb P(M)
   + \mathbb P(V \mid D)\mathbb P(D)
   + \mathbb P(V \mid I)\mathbb P(I)}
= \frac{\frac{1}{2} \cdot \frac{6}{9}}
  {\frac{1}{2} \cdot \frac{6}{9}
   + \frac{1}{2} \cdot \frac{2}{9}
   + 1 \cdot \frac{1}{9}}
= \frac{3}{5} \enspace,
```

e analogamente $\mathbb P(D \mid V) = \frac{1}{5}$ e
$\mathbb P(I \mid V) = \frac{1}{5}$. Sapere che il personaggio vola ci
permette quindi di aggiornare la nostra valutazione iniziale sull'editore, come
evidenziato nello schema che segue.

|                     | Marvel | DC     | Image Comics |
|:--------------------|:------:|:------:|:------------:|
| Incondizionata      | $0.67$ | $0.22$ | $0.11$       |
| Condizionata a $V$  | $0.6$  | $0.2$  | $0.2$        |

La Marvel resta l'ipotesi più probabile, ma i rapporti tra le tre alternative
sono cambiati: ora Image comics e DC sono equiprobabili, mentre a priori il
secondo editore aveva una probabilità doppia rispetto al primo.

````

```{margin}
Il tema dell'inferenza statistica verrà ripreso in forma più generale nei
Capitoli
{numref}`chap_statistica-inferenziale`&ndash;{numref}`chap_stime-per-intervalli`,
dove l'attenzione si sposterà dalla sola revisione di ipotesi discrete a
problemi più ampi di stima a partire da dati campionari.
```
Più in generale, questo modo di leggere il teorema di Bayes costituisce uno
dei fondamenti dell’_inferenza bayesiana_. In questa prospettiva, una
situazione nella quale si possono verificare due o più opzioni, associate ad
altrettanti eventi $F_1, \dots, F_n$, viene modellata dapprima tramite delle
probabilità _a priori_, che quantificano il grado di plausibilità che si
ipotizza per queste opzioni sulla base di informazioni inizialmente
disponibili. A seguito del verificarsi di un evento $E$ &mdash; detto
_evidenza_ &mdash; e partendo dai valori di _verosimiglianza_
$\mathbb P(E \mid F_1), \dots, \mathbb P(E \mid F_n)$, che misurano quanto
l'evidenza osservata sia compatibile con le ipotesi, si utilizza il teorema di
Bayes perottenere le probabilità _a posteriori_
$\mathbb P(F_1 \mid E), \dots, \mathbb P(F_n \mid E)$, che permettono di
aggiornare le probabilità delle varie ipotesi, incorporando l'informazione
portata dall'evidenza $E$.

Come ho già sottolineato, il punto concettuale essenziale in questo passaggio
sistematico da una valutazione _a priori_ ad una _a posteriori_ delle
probabilità non è l'inversione di una successione temporale di eventi, bensì la
revisione della conoscenza disponibile in un dato istante, sulla base di nuova
informazione: si parte da un quadro iniziale di plausibilità, si osservano
nuovi dati e si ridistribuisce in modo razionale il peso assegnato alle ipotesi
concorrenti. In questa prospettiva, una valutazione _a posteriori_ ottenuta in
un dato momento può a sua volta diventare la valutazione _a priori_ in una fase
successiva, qualora siano disponibili ulteriori osservazioni. È questa dinamica
di aggiornamento a caratterizzare l'approccio bayesiano e a renderlo centrale
in molti problemi di classificazione, diagnosi e inferenza statistica.

````{prf:example} Un indizio nell'Umbrella Academy
:label: ex-bayes-umbrella

Immaginiamo di dover stabilire quale tra i sette fratelli Hargreeves abbia
lasciato un messaggio anonimo nella casa
dell’{extlink}`Umbrella Academy <https://umbrellaacademy.fandom.com/>`.
Indichiamo con $C$ l'ipotesi «l'autore del messaggio è Numero Cinque». Possiamo
adottare come valutazione iniziale, cioè prima di osservare il contenuto del
messaggio, l'ipotesi che ciascuno dei sette fratelli sia ugualmente plausibile
come autore; in tal caso
$\mathbb P(C) = \frac{1}{7}$ e $\mathbb P(\overline{C}) = \frac{6}{7}$.
Ipotizziamo ora che il messaggio che osserviamo contenga dei riferimenti
precisi a salti temporali e a linee temporali alternative, e indichiamo con $E$
l'evento corrispondente. Siccome, tra tutti i fratelli, solo Numero Cinque
ha il potere di viaggiare tra diverse linee temporali, così che per esempio
$\mathbb P(E \mid C) = 0.9$, mentre $\mathbb P(E \mid \overline{C}) = 0.05$.
Applicando il teorema di Bayes si ottiene

```{math}
\mathbb P(C \mid E)
= \frac{0.9 \cdot \frac{1}{7}}
  {0.9 \cdot \frac{1}{7} + 0.05 \cdot \frac{6}{7}}
= \frac{3}{4}
\enspace.
```

L'osservazione del messaggio porta quindi a rivedere drasticamente la
valutazione iniziale: l'ipotesi che l'autore sia Numero Cinque passa da
$1/7 \approx 14.3\%$ a $3/4 = 75\%$. Questo esempio mostra bene che, in
ottica bayesiana, la nuova informazione non sostituisce arbitrariamente la
valutazione iniziale, ma la trasforma in modo controllato alla luce della
maggiore o minore compatibilità dell'evidenza con le ipotesi in gioco.
````


````{prf:example}
:label: ex-carol-danvers

{extlink}`Carol Danvers
<https://marvel.fandom.com/wiki/Carol_Danvers_(Earth-616)>` rileva un segnale
di soccorso Kree di origine incerta. Potrebbe provenire da uno di tre pianeti,
indicati di seguito, ognuno con la probabilità inizialmente stimata.

| Pianeta      | Probabilità a priori |
|:------------:|:--------------------:|
| **Hala**     | $1/2$                |
| **Torfa**    | $1/3$                |
| **Kree-Lar** | $1/6$                |

Carol raggiunge inizialmente Hala, e non riesce a intercettare il segnale. Le
tempeste solari nel sistema planetario generano interferenze magnetiche su Hala,
che fanno sì che, anche se il segnale provenisse davvero da lì, lei riuscirebbe
a localizzarlo con probabilità $1 - \alpha$ &mdash; dove $\alpha \in [0, 1]$
modella l'intensità di tali tempeste.

Alla luce di queste informazioni, possiamo usare il teorema di Bayes per
rivedere le probabilità a priori inizialmente considerate. Definiamo
rispettivamente con $H$, $T$ e $K$ gli eventi che si verificano quando il
segnale proviene da Hala, Torfa o Kree-Lar, e sia $E =$ «la ricerca del
segnale su Hala ha dato esito negativo». Sicuramente,
$\mathbb P(E \mid H) = \alpha$ (è la probabilità di non rilevare il segnale su
Hala, nel caso in cui il segnale provenga effettivamente da quel pianeta).
Inoltre, $\mathbb P(E \mid T) = \mathbb P(E \mid K) = 1$, perché quando si
cerca di localizzare il segnale su Hala, sicuramente l'operazione avrà esito
negativo se questo proviene da un altro pianeta. Sulla base di queste
probabilità e di quelle a priori, il teorema delle probabilità totali permette
di calcolare

```{math}
\mathbb P(E) = \alpha \cdot \frac{1}{2} + 1 \cdot \frac{1}{3}
       + 1 \cdot \frac{1}{6} = \frac{\alpha + 1}{2} \enspace.
```

Infine, dal teorema di Bayes si ottiene

```{margin}
Si può verificare che $\mathbb P(H \mid E) + \mathbb P(T \mid E) +
\mathbb P(K \mid E) = 1$, perché il segnale deve provenire da uno dei tre
pianeti.
```
```{math}
\begin{align*}
\mathbb P(H \mid E) &= \alpha \cdot \frac{1}{2} \cdot \frac{2}{\alpha+1}
                     = \frac{\alpha}{\alpha + 1} \enspace, \\
\mathbb P(T \mid E) &= 1 \cdot \frac{1}{3} \cdot \frac{2}{\alpha+1}
                     = \frac{2}{3(\alpha+1)} \enspace, \\
\mathbb P(K \mid E) &= 1 \cdot \frac{1}{6} \cdot \frac{2}{\alpha+1}
                     = \frac{1}{3(\alpha+1)} \enspace.
\end{align*}
```

Va notato che il valore di $\alpha$ modifica notevolmente il modo in cui
l'esito negativo della scansione aggiorna le probabilità:

- se $\alpha \to 0$, le interferenze su Hala sono trascurabili, quindi diventa
  impossibile che il segnale provenga da questo pianeta, mentre la probabilità
  che arrivi da Torfa è doppia rispetto a Kree-Lar (in proporzione alle
  probabilità a priori);
- se invece $\alpha \to 1$, le interferenze rendono la scansione inutile:
  l'esito della ricerca su Hala non aggiunge informazione e le probabilità a
  posteriori restano invariate.
````

[^ubayes]: Il celebre ritratto tradizionalmente associato a Thomas Bayes è in
realtà problematico: l’immagine comparve soltanto nel 1936 nel volume _History
of Life Insurance in Its Formative Years_ di Terence O’Donnell, senza però una
documentazione chiara della sua provenienza. Negli anni Ottanta la questione
attirò l’interesse dell’Institute of Mathematical Statistics, che promosse
un’indagine storica e bandì un premio dedicato ad alcuni aspetti biografici
relativi a Bayes e al presunto ritratto. Tra i principali studiosi coinvolti vi
fu David Bellhouse, il quale osservò che l’abbigliamento, il colletto
ecclesiastico e altri elementi iconografici del dipinto sembrano incompatibili
con quelli tipici di un ministro dissenziente inglese della prima metà del
Settecento. Per questo motivo, oggi il ritratto è generalmente considerato di
autenticità incerta.

## Vero o falso?

Analizzate ciascuna delle seguenti affermazioni sulla probabilità condizionata,
e dite se è vera o falsa, motivando il vostro ragionamento. Cliccate su di essa
per visualizzare la risposta corretta.

````{tf-item}
Per qualunque coppia di eventi con probabilità non nulla,
$\mathbb P(E \mid F) = \mathbb P(F \mid E)$.
+++
**Falsa**. In generale le due quantità sono diverse: dalla
{prf:ref}`def-conditional_probability` è facile verificare che le due
probabilità coincidono solo quando $\mathbb P(E) = \mathbb P(F)$.
````

````{tf-item}
Se $E$ e $F$ sono mutuamente esclusivi e $\mathbb P(F) \neq 0$, allora
$\mathbb P(E \mid F) = 0$.
+++
**Vera**. Se $E \cap F = \varnothing$, allora $\mathbb P(E \cap F) = 0$ e
dunque, per la {prf:ref}`def-conditional_probability`,

$$\mathbb P(E \mid F) = \frac{\mathbb P(E \cap F)}{\mathbb P(F)}
= \frac{0}{\mathbb P(F)} = 0 \enspace.$$

Intuitivamente, sapere che $F$ si è verificato riduce l’universo di
riferimento a $F$, e se $E$ e $F$ non hanno esiti in comune, in questo nuovo
universo $E$ risulta impossibile.
````

````{tf-item}
Fissato un evento $F$ con $\mathbb P(F) \neq 0$, la funzione
$E \mapsto \mathbb P(E \mid F)$ è una funzione di probabilità su
$(\Omega, \mathsf A)$.
+++
**Vera**. Come mostrato nella nota al paragrafo sulla probabilità condizionata,
$\mathbb P(\cdot \mid F)$ soddisfa tutti e tre gli assiomi di Kolmogorov:
la non-negatività segue da quella di $\mathbb P$, la normalizzazione vale
perché $\mathbb P(\Omega \mid F) = \mathbb P(\Omega \cap F) / \mathbb P(F) = 1$
e l’additività per eventi disgiunti si trasferisce in modo diretto dalla
probabilità originale.
````

````{tf-item}
La probabilità condizionata $\mathbb P(E \mid F)$ è definita anche quando
$\mathbb P(F) = 0$.
+++
**Falsa**. La {prf:ref}`def-conditional_probability` richiede esplicitamente
$\mathbb P(F) \neq 0$, perché altrimenti il rapporto in {eq}`eq-prob-cond`
avrebbe denominatore nullo. Dietro questo problema formale si nasconde il fatto
che la definizione di probabilità condizionata consiste nel restringere la
probabilità all'evento $F$ e poi rinormalizzarla dividendo per $\mathbb P(F)$.
Se $\mathbb P(F)=0$, tale rinormalizzazione non è possibile.
````

````{tf-item}
Il teorema delle probabilità totali richiede che ogni blocco della partizione
abbia probabilità non nulla.
+++
**Vera**. Il {prf:ref}`teo-total-probability` richiede esplicitamente
$\mathbb P(F_i) \neq 0$ per ogni $i$. Questa ipotesi è necessaria perché la
dimostrazione si basa sulla regola di fattorizzazione
$\mathbb P(E \cap F_i) = \mathbb P(E \mid F_i)\mathbb P(F_i)$, che richiede a
sua volta che la probabilità condizionata $\mathbb P(E \mid F_i)$ sia definita.
````

````{tf-item}
Conoscere $\mathbb P(E \mid F)$ e $\mathbb P(F)$ è sufficiente per calcolare
$\mathbb P(E)$.
+++
**Falsa**. La regola di fattorizzazione (introdotta nel
{prf:ref}`teo-factorization`) permette di ricavare
$\mathbb P(E \cap F) = \mathbb P(E \mid F)\mathbb P(F)$, ma per ottenere
$\mathbb P(E)$ serve anche il contributo di $E$ al di fuori di $F$. Ciò è
evidente, per esempio, nella forma del teorema delle probabilità totali
espressa in {eq}`eq-prob-totali-2`:

```{math}
\mathbb P(E) = \mathbb P(E \mid F)\mathbb P(F)
        + \mathbb P(E \mid \overline{F})\mathbb P(\overline{F}) \enspace,
```

cioè occorre conoscere anche
$\mathbb P(E \mid \overline{F})$ e $\mathbb P(\overline{F})$.
````


## Esercizi

````{exercise} •
:label: ex-prob-cond-dadi-esercizio-base

Considerate l'esperimento del lancio di due dadi bilanciati e distinguibili,
soffermandovi sugli eventi $A =$ «la somma dei due risultati è uguale a $7$» e
$B =$ «il dado blu mostra un numero pari». Verificate che
$\mathbb P(A \mid B) \neq \mathbb P(B \mid A)$.
````

````{solution} ex-prob-cond-dadi-esercizio-base
:class: dropdown

L'evento $B$ contiene $18$ esiti, perché il dado blu può mostrare $2$, $4$ o
$6$, mentre il dado rosso è arbitrario. Tra questi, quelli in cui la somma è
$7$ sono $(5, 2)$, $(3, 4)$ e $(1, 6)$, dunque

```{math}
\mathbb P(A \mid B) = \frac{3}{18} = \frac{1}{6} \enspace.
```

Analogamente, $A$ contiene invece i sei esiti $(1, 6)$, $(2, 5)$, $(3, 4)$,
$(4, 3)$, $(5, 2)$ e $(6, 1)$.` Tra questi, quelli in cui il dado blu è pari
sono ancora tre, quindi

```{math}
\mathbb P(B \mid A) = \frac{3}{6} = \frac{1}{2} \enspace.
```

I due valori sono dunque diversi.
````


````{exercise} ••
:label: ex-prob-cond-factorization-heroes

Consideriamo lo schedario dell’{prf:ref}`ex-prob-cond-supereroi`, che contiene
le otto schede dedicate a Iron Man, Thor, Hulk, Black Widow, Superman, Wonder
Woman, Batman e Storm. Siano $V$ ed $S$, rispettivamente, gli eventi «il
personaggio può volare» e «il personaggio ha super-forza».

1. Calcolate $\mathbb P(V)$ e $\mathbb P(S \mid V)$.
2. Usate la regola di fattorizzazione per determinare $\mathbb P(S \cap V)$.
3. Verificate il risultato del punto precedente con un conteggio diretto.
````

````{solution} ex-prob-cond-factorization-heroes
:class: dropdown

I personaggi che possono volare sono Iron Man, Thor, Superman e Storm, quindi

```{math}
\mathbb P(V) = \frac{1}{2} \enspace.
```

Tra questi, quelli con super-forza sono Thor e Superman, dunque

```{math}
\mathbb P(S \mid V) = \frac{1}{2} \enspace.
```

La regola di fattorizzazione fornisce allora

```{math}
\mathbb P(S \cap V) = \mathbb P(V)\mathbb P(S \mid V)
= \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4} \enspace.
```

Il conteggio diretto conferma il risultato, perché i personaggi che stanno in
$S \cap V$ sono esattamente due su otto.
````


````{exercise} ••
:label: ex-prob-cond-prob-totali-dadi

Nel lancio di due dadi distinguibili di colore blu e rosso, considerate gli
eventi che seguono:

```{math}
\begin{align*}
F_1 &= \{ \text{il dado blu vale } 1 \text{ oppure } 2 \}, \\
F_2 &= \{ \text{il dado blu vale } 3 \text{ oppure } 4 \}, \\
F_3 &= \{ \text{il dado blu vale } 5 \text{ oppure } 6 \} \enspace.
\end{align*}
```

Sia inoltre $E$ l'evento «la somma dei due risultati è almeno $9$».

1. Mostrate che $\mathcal P = \{ F_1, F_2, F_3 \}$ è una partizione dello
   spazio degliesiti.
2. Calcolate $\mathbb P(E \mid F_1)$, $\mathbb P(E \mid F_2)$ e
  $\mathbb P(E \mid F_3)$.
3. Usate il teorema delle probabilità totali per ricavare $\mathbb P(E)$.
4. Verificate il risultato ottenuto al punto precedente  con un conteggio
   diretto degli esiti favorevoli.
````

````{solution} ex-prob-cond-prob-totali-dadi
:class: dropdown

Ogni evento $F_i$ contiene $12$ esiti, quindi ha probabilità $1/3$.

1. $F_1 = \{ (i, j) \mid i \in [1 .. 2], j \in [1 .. 6] \}$,
   $F_2 = \{ (i, j) \mid i \in [3 .. 4], j \in [1 .. 6] \}$ e
   $F_3 = \{ (i, j) \mid i \in [5 .. 6], j \in [1 .. 6] \}$, dunque l'unione di
   questi tre eventi è $\Omega$. Valutando i primi elementi delle coppie
   ordinate, si vede facilmente che $F_i \cap F_j$ ogni volta che $i \neq j$,
   quindi $\mathcal P$ è effettivamente una partizione di $\Omega$.

2. Se il risultato del dado blu è al massimo $2$, la somma dei due risultati
   non può eccedere $8$, pertanto $\mathbb P(E \mid F_1) = 0$. Quando invece
   il valore del dado blu è $3$ oppure $4$, gli esiti $(6, 3)$, $(5, 4)$ e
   $(6, 4)$, portano a una somma maggiore o uguale a $9$, e dunque
   $\mathbb P(E \mid F_2) = \frac{1}{4}$. Se infine otteniamo $5$ oppure $6$
   per il dado blu, gli esiti $(5, j)$ per $j \in [4 .. 6]$ e $(6, j)$ per
   $j \in [3 .. 6]$ sono contenuti in $E$, così che
   $\mathbb P(E \mid F_3) = \frac{7}{12}$.

3. Applicando il teorema delle probabilità totali si ottiene

  ```{math}
  \mathbb P(E)
  = \sum_{i=1}^3 \mathbb P(E \mid F_i)\mathbb P(F_i)
  = 0 \cdot \frac{1}{3} + \frac{1}{4} \cdot \frac{1}{3}
    + \frac{7}{12} \cdot \frac{1}{3}
  = \frac{5}{18} \enspace.
  ```

4. Gli esiti in $E$ sono quelli per cui la somma dei risultati dei due dadi è
   $9$, $10$, $11$ o $12$. Come si può vedere dallo schema sottostante, il
   numero di esiti possibile per questi valori della somma è, rispettivamente,
   quattro, tre, due e uno. In totale, si tratta di dieci esiti, il che porta
   a $\mathbb P(E) \frac{5}{18}$.

   |Somma | Esiti                            |
   |:----:|:--------------------------------:|
   | $9$  | $(3, 6), (4, 5), (5, 4), (6, 3)$ |
   | $10$ | $(4, 6), (5, 5), (6, 5)$         |
   | $11$ | $(5, 6), (6, 5)$                 |
   | $12$ | $(6, 6)$                         |

````

````{exercise} •••
:label: ex-prob-cond-bayes-binario

Torniamo alla schede dell’{prf:ref}`ex-prob-cond-supereroi`, e indichiamo con
$M$ l'evento «la scheda estratta è Marvel» e con $V$ l'evento «il personaggio
sa volare».

1. Calcolate $\mathbb P(M)$ e $\mathbb P(\overline{M})$.
2. Calcolate $\mathbb P(V \mid M)$ e $\mathbb P(V \mid \overline{M})$.
3. Usate il teorema di Bayes per determinare $\mathbb P(M \mid V)$.

Interpretate il risultato ottenuto.
````

````{solution} ex-prob-cond-bayes-binario
:class: dropdown

1. Tra le otto schede, quelle di Iron Man, Thor, Hulk, Black Widow e Storm
   fanno riferimento a eroi Marvel, quindi $\mathbb P(M) = \frac{5}{8}$ e
   $\mathbb P(\overline{M}) = \frac{3}{8}$.

2. Tra i cinque personaggi Marvel, quelli che volano sono Iron Man, Thor e
   Storm, perciò $\mathbb P(V \mid M) = \frac{3}{5}$. D'altro canto, le schede
   degli altri supereroi fanno riferimento a Superman, Wonder Woman e Batman, e
   solo il primo vola, quindi $\mathbb P(V \mid \overline{M}) = \frac{1}{3}$.

3. Applicando il teorema di Bayes si ottiene

```{math}
\mathbb P(M \mid V)
= \frac{\mathbb P(V \mid M)\mathbb P(M)}
      {\mathbb P(V \mid M)\mathbb P(M)
  + \mathbb P(V \mid \overline{M})\mathbb P(\overline{M})} \\
= \frac{\frac{3}{5} \cdot \frac{5}{8}}
      {\frac{3}{5} \cdot \frac{5}{8} + \frac{1}{3} \cdot \frac{3}{8}}
= \frac{3}{4} \enspace.
```

Sapere che il personaggio vola rende quindi l'ipotesi Marvel la più plausibile,
ma non abbastanza da renderla certa: resta infatti una probabilità del $25 \%$
che la scheda appartenga a un personaggio non Marvel.
````

````{exercise} •••
:label: ex-prob-cond-bayes-generale-dadi

Riconsiderate l’{numref}`%s <ex-prob-cond-prob-totali-dadi>`, e calcolate

1. $\mathbb P(F_1 \mid E)$,
2. $\mathbb P(F_2 \mid E)$,
3. $\mathbb P(F_3 \mid E)$,

verificando che queste tre probabilità sommino a $1$.
````

````{solution} ex-prob-cond-bayes-generale-dadi
:class: dropdown

Dall’esercizio precedente sappiamo che $\mathbb P(F_i) = \frac{1}{3}$ per ogni
$i \in [1 .. 3]$, e che $\mathbb P(E \mid F_1) = 0$,
$\mathbb P(E \mid F_2) = \frac{1}{4}$, $\mathbb P(E \mid F_3) = \frac{7}{12}$ e
$\mathbb P(E) = \frac{5}{18}$. Pertanto

```{math}
\mathbb P(F_1 \mid E)
= \frac{\mathbb P(E \mid F_1)\mathbb P(F_1)}{\mathbb P(E)}
= \frac{0 \cdot \frac{1}{3}}{\frac{5}{18}}
= 0 \enspace,
```

analogamente

```{math}
\mathbb P(F_2 \mid E)
= \frac{\mathbb P(E \mid F_2)\mathbb P(F_2)}{\mathbb P(E)}
= \frac{\frac{1}{4} \cdot \frac{1}{3}}{\frac{5}{18}}
= \frac{3}{10} \enspace,
```

e infine

```{math}
\mathbb P(F_3 \mid E)
= \frac{\mathbb P(E \mid F_3)\mathbb P(F_3)}{\mathbb P(E)}
= \frac{\frac{7}{12} \cdot \frac{1}{3}}{\frac{5}{18}}
= \frac{7}{10} \enspace.
```

Sommando le tre probabilità si ottiene

```{math}
\mathbb P(F_1 \mid E) + \mathbb P(F_2 \mid E) + \mathbb P(F_3 \mid E)
= 0 + \frac{3}{10} + \frac{7}{10} = 1 \enspace.
```
````


## Concetti fondamentali

Pensate ai concetti fondamentali illustrati in questo paragrafo ed elencateli.
Nella lista qui sotto sono già presenti gli stessi concetti, ma nascosti.
Cliccate sul pulsante per mostrarli sotto forma di parole chiave, quindi
confrontateli con la vostra lista. Provate infine a descrivere ciascun concetto
con parole vostre.

````{sds-wordcloud}
Probabilità condizionata
Evento condizionante
Evento condizionato
Regola di fattorizzazione
Teorema delle probabilità totali
Partizione dello spazio degli esiti
Teorema di Bayes
Probabilità a priori
Verosimiglianza
Probabilità a posteriori
Evidenza
````

