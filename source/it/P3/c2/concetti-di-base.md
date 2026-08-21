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

(sec_concetti-base-insiemi)=
# Concetti di base

In accordo con la definizione riportata all'inizio del capitolo, nonché con
la comune notazione matematica, indicherò di norma gli insiemi con le lettere
maiuscole dell'alfabeto latino e i loro elementi con le corrispondenti lettere
minuscole. Per indicare che un elemento $a$ appartiene a un insieme $A$
scriverò $a \in A$, mentre per indicare che $b$ non vi appartiene scriverò
$b \notin A$.

Un insieme può essere rappresentato:

- _estensivamente_, cioè elencando tutti i suoi elementi: per esempio,
  l'insieme $O$ dei membri degli
  [Avengers](https://marvel.fandom.com/wiki/Avengers_(Earth-616)) che hanno
  una forza sovrumana si può indicare estensivamente come 
  $O = \{ \text{Capitan America}, \text{Hulk}, \text{Thor} \}$;
- _intensivamente_, specificando una proprietà che individua tutti e soli gli
  elementi dell'insieme: l'insieme descritto al punto precedente ammette per
  esempio la descrizione intensiva

```{math}
O = \{ \text{Componenti degli Avengers con forza sovrumana} \} \enspace;
```
- tramite un _diagramma di Venn_, indicando gli elementi come punti in una
  porzione di piano e racchiudendoli dentro un'ellisse: l'insieme $O$ descritto
  nei punti precedenti è illustrato nella {numref}`fig_venn-simple`.


````{customfigure}
:name: fig_venn-simple

```{code-cell} python
:tags:  [hide-input]

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle

MATH_SIZE = 9
TEXT_SIZE = 7

EDGE_COLOR = '#333333'
BG_COLOR = '#eaf3f5'
FILL_COLOR_A = '#d6e4f7'
FILL_COLOR_O = '#aac5e8'
DOT_COLOR = '#2255aa'


def simple_venn(universe=False):
    fig, ax = plt.subplots(facecolor=BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)

    if universe:
        rect = Rectangle((0.1, 0.1), 11.8, 7.8,
                        facecolor=BG_COLOR, edgecolor=EDGE_COLOR,
                        linewidth=1.1, zorder=0)
        ax.add_patch(rect)
        ax.text(11.6, 7.6, r'$\Omega$', fontsize=MATH_SIZE, ha='right', va='top')

        for name, x, y, xof, yof in [('Iron\nMan',    1.7, 5,    0.8, 0),
                                 ('Black\nWidow', 9.8, 5.5,  0,  -0.9),
                                 ('Hawkeye',      2.5, 2.6, -0.1, 0.4),
                                 ('Ant-Man',      9.5, 2.2, -1.1, 0)]:
            ax.plot(x, y, "o", markersize=4, color=DOT_COLOR, zorder=4)
            ax.text(x + xof, y + yof, name, ha='center', va='center',
                    fontsize=TEXT_SIZE, zorder=5)

    ellipse_O = Ellipse(xy=(6, 3.8), width=5.5, height=3.2,
                        facecolor=FILL_COLOR_O, edgecolor=EDGE_COLOR,
                        linewidth=1.2, zorder=2)
    ax.add_patch(ellipse_O)
    ax.text(3.9, 5.7, r'$O$', fontsize=MATH_SIZE, va='top')

    for name, x, y, xof, yof in [('Thor',             5.2, 4.7, 0.8, 0),
                                 ('Hulk',             8,   4,  -0.8, 0),
                                 ('Capitan\nAmerica', 4,   3.3, 1.2, 0)]:
        ax.plot(x, y, "o", markersize=4, color=DOT_COLOR, zorder=4)
        ax.text(x + xof, y + yof, name, ha='center', va='center',
                fontsize=TEXT_SIZE, zorder=5)

    return fig

fig = simple_venn()
plt.tight_layout()
plt.show()
```

Un diagramma di Venn che descrive l'insieme $O = \{ \text{Componenti degli Avengers con forza sovrumana} \}$.
````
La descrizione tramite diagramma di Venn presuppone di conoscere, almeno in
linea di principio, tutti gli elementi che potrebbero far parte di un insieme.
L'insieme di tutti i possibili elementi si chiama _insieme universo_ e si
indica di solito con $\Omega$. Nell'esempio precedente, una scelta ragionevole per l'universo potrebbe far coincidere
$\Omega$ con l'insieme degli Avengers, quindi un diagramma di Venn più completo
per $O$ è quello riportato nella {numref}`fig_venn-universe`.

````{customfigure}
:name: fig_venn-universe

```{code-cell} python
:tags: [hide-input]

fig = simple_venn(universe=True)
plt.tight_layout()
plt.show()
```

Un diagramma di Venn che illustra l'insieme $O$ della {numref}`fig_venn-simple`
all'interno dell'universo $\Omega$ degli Avengers.
````
L'insieme universo contiene qualunque elemento, e &mdash; all'estremo opposto
&mdash; è utile considerare l'insieme che non ne contiene nessuno: si chiama
_insieme vuoto_ e lo indicherò con $\varnothing$, in modo che per ogni
$a \in \Omega$ valga $a \notin \varnothing$.


## Vero o falso?

Analizzate ciascuna delle seguenti affermazioni, che riguardano il concetto di
insieme, e dite se è vera o falsa, motivando il vostro ragionamento. Cliccate
su di essa per visualizzare la risposta corretta.

````{tf-item}
Se $a \in A$, allora la scrittura $a \notin A$ è falsa.
+++
**Vera**. Le notazioni $a \in A$ (leggi: «$a$ appartiene ad $A$») e
$a \notin A$ («$a$ non appartiene ad $A$») sono la negazione l'una dell'altra:
se un elemento appartiene a un insieme, affermare che non vi appartiene è
necessariamente falso. Le due scritture non possono essere vere allo stesso
tempo.
````

````{tf-item}
La rappresentazione estensiva di un insieme consiste nello specificare una
proprietà che ne caratterizza gli elementi.
+++
**Falsa**. Quella descritta è la rappresentazione _intensiva_: specificare una
proprietà che individua tutti e soli gli elementi dell'insieme. La
rappresentazione _estensiva_ consiste invece nell'elencare esplicitamente tutti
gli elementi, come in
$O = \{\text{Capitan America}, \text{Hulk}, \text{Thor}\}$.
````

````{tf-item}
Lo stesso insieme può essere descritto sia estensivamente sia intensivamente.
+++
**Vera**. Il testo mostra esattamente questo per l'insieme $O$ degli Avengers
con forza sovrumana: esso ammette la rappresentazione estensiva
$O = \{\text{Capitan America}, \text{Hulk}, \text{Thor}\}$ e quella intensiva
$O = \{\text{Componenti degli Avengers con forza sovrumana}\}$. Le due
descrizioni individuano la stessa collezione di oggetti.
````

````{tf-item}
Per costruire un diagramma di Venn è necessario avere in mente l'insieme
universo.
+++
**Vera**. Come osservato nel testo, la descrizione tramite diagramma di Venn
presuppone di conoscere, almeno in linea di principio, tutti gli elementi che
potrebbero far parte di un insieme. Questi elementi costituiscono l'insieme
universo $\Omega$, che nel diagramma viene di solito raffigurato come il
rettangolo esterno in cui sono contenute le ellissi degli insiemi.
````

````{tf-item}
L'insieme universo $\Omega$ è uguale per tutti i problemi.
+++
**Falsa**. La scelta di $\Omega$ dipende dal contesto. Nel testo, per
descrivere l'insieme $O$ degli Avengers con forza sovrumana, si può scegliere
come universo l'insieme degli Avengers. In un altro problema lo stesso $O$
potrebbe essere inserito in un universo più ampio. La scelta di $\Omega$ è
parte della modellazione del problema, non è fissata a priori.
````

````{tf-item}
Per ogni elemento $a$ dell'insieme universo $\Omega$, vale
$a \notin \varnothing$.
+++
**Vera**. Questa è esattamente la definizione dell'insieme vuoto $\varnothing$
riportata nel testo: non contiene nessun elemento, quindi per ogni
$a \in \Omega$ vale $a \notin \varnothing$. In altri termini, qualunque
elemento si scelga nell'universo, esso non potrà mai appartenere all'insieme
vuoto.
````

## Esercizi

````{exercise}
:label: ex-concetti-base-rappresentazione

Considerate come insieme universo $\Omega$ i sei personaggi Capitan America,
Iron Man, Thor, Hulk, Black Widow e Hawkeye. Sia $S$ l'insieme dei personaggi
di $\Omega$ che possiedono capacità fisiche sovrumane senza ricorrere a
gadget o armature.

1. Scrivete $S$ in forma estensiva.
2. Scrivete una possibile descrizione intensiva di $S$.
3. Indicate due elementi di $\Omega$ che non appartengono a $S$.
````

````{solution} ex-concetti-base-rappresentazione
:class: dropdown

1. Una possibile rappresentazione estensiva è
  $S = \{ \text{Capitan America}, \text{Thor}, \text{Hulk} \}$.
2. Una descrizione intensiva possibile è «personaggi di $\Omega$ con capacità
   fisiche sovrumane non dovute a equipaggiamenti esterni».
3. Ad esempio, Iron Man e Hawkeye non appartengono a $S$.
   Anche Black Widow non vi appartiene.
````

````{exercise}
:label: ex-concetti-base-universo

Nel testo, l'insieme $O$ dei componenti degli Avengers con forza sovrumana è
inserito nell'universo degli Avengers. Proponete un altro possibile insieme
universo $\Omega'$ per lo stesso insieme $O$, più ampio del precedente, e
spiegate:

1. perché $O$ resta lo stesso insieme;
2. in che senso cambierebbe il diagramma di Venn.
````

````{solution} ex-concetti-base-universo
:class: dropdown

Una possibile scelta è prendere come universo $\Omega'$ l'insieme di tutti i
supereroi Marvel, o anche quello di tutti i personaggi Marvel.

1. L'insieme $O$ resta lo stesso perché continua a essere formato dai
  componenti degli Avengers che hanno forza sovrumana: cambia il contesto
  in cui lo osserviamo, ma non la proprietà che ne definisce gli elementi.
2. Nel diagramma di Venn, l'ellisse che rappresenta $O$ conterrebbe gli stessi
  punti di prima, ma il rettangolo dell'universo sarebbe più grande e
  includerebbe molti più elementi esterni a $O$.
````

````{exercise}
:label: ex-concetti-base-insieme-vuoto

Considerate come insieme universo
$\Omega = \{ \text{Batman}, \text{Superman}, \text{Wonder Woman}, \text{Flash} \}$.
Sia $E$ l'insieme degli elementi di $\Omega$ che sono contemporaneamente
kryptoniani e amazzoni.

1. Scrivete $E$ in forma estensiva.
2. Spiegate perché $E = \varnothing$.
3. Stabilite se l'affermazione $\text{Flash} \in E$ è vera o falsa.
````

````{solution} ex-concetti-base-insieme-vuoto
:class: dropdown

1. L'insieme $E$ non contiene nessun elemento, quindi in forma estensiva si
  scrive $E = \varnothing$.
2. Nell'universo scelto nessun personaggio è allo stesso tempo kryptoniano e
  amazzone. Superman è kryptoniano ma non è un'amazzone; Wonder Woman è
  un'amazzone ma non è kryptoniana; Batman e Flash non soddisfano nessuna
  delle due proprietà.
3. L'affermazione $\text{Flash} \in E$ è falsa, perché nessun elemento
  appartiene all'insieme vuoto.
````

## Concetti fondamentali

Pensate ai concetti fondamentali illustrati in questo paragrafo ed elencateli.
Nella lista qui sotto sono già presenti gli stessi concetti, ma nascosti.
Cliccate sul pulsante per mostrarli sotto forma di parole chiave, quindi
confrontateli con la vostra lista. Provate infine a descrivere ciascun concetto
con parole vostre.

````{sds-wordcloud}
Insieme
Elemento
Appartenenza
Rappresentazione estensiva
Rappresentazione intensiva
Diagramma di Venn
Insieme universo
Insieme vuoto
````


