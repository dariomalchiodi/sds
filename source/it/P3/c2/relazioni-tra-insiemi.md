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

(sec_relazioni-tra-insiemi)=
# Relazioni tra insiemi

Tra i concetti fondamentali della teoria degli insiemi, quello di
_sottoinsieme_ occupa un ruolo centrale: a partire da esso è possibile
definire una serie di relazioni tra insiemi di carattere generale. Più
precisamente:

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

````{prf:example}
:label: ex-subst

La {numref}`fig_venn-sottoinsiemi` illustra  il diagramma
di Venn per l'insieme $O$ della {numref}`fig_venn-universe`, inteso come
sottoinsieme di $A = \{ \text{membri degliAvengers} \}$, entrambi inclusi
nell'universo $\Omega$ di tutti i supereroi.
````

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

def subset_venn():
    fig, ax = plt.subplots(facecolor=BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)

    rect = Rectangle((0.1, 0.1), 11.8, 7.8,
                     facecolor=BG_COLOR, edgecolor=EDGE_COLOR,
                     linewidth=1.1, zorder=0)
    ax.add_patch(rect)
    ax.text(11.6, 7.6, r'$\Omega$', fontsize=MATH_SIZE, ha='right', va='top')

    ellipse_A = Ellipse(xy=(6, 4), width=10.5, height=6.0,
                        facecolor=FILL_COLOR_A, edgecolor=EDGE_COLOR,
                        linewidth=1.2, zorder=1)
    ax.add_patch(ellipse_A)
    ax.text(1.7, 6.7, r'$A$', fontsize=MATH_SIZE, va='top')

    ellipse_O = Ellipse(xy=(6, 3.8), width=5.5, height=3.2,
                        facecolor=FILL_COLOR_O, edgecolor=EDGE_COLOR,
                        linewidth=1.2, zorder=2)
    ax.add_patch(ellipse_O)
    ax.text(3.9, 5.7, r'$O$', fontsize=MATH_SIZE, va='top')

    for name, x, y, xof, yof in [('Thor',             5.2, 4.7,  0.8,  0.),
                                  ('Hulk',             8.,  4.,  -0.8,  0.),
                                  ('Capitan\nAmerica', 4.,  3.3,  1.2,  0.),
                                  ('Iron\nMan',        1.7, 5.,   0.8,  0.),
                                  ('Black\nWidow',     9.8, 5.5,  0.,  -0.9),
                                  ('Hawkeye',          2.5, 2.6, -0.1,  0.4),
                                  ('Ant-Man',          9.5, 2.2, -1.1,  0.)]:
        ax.plot(x, y, "o", markersize=4, color=DOT_COLOR, zorder=4)
        ax.text(x + xof, y + yof, name, ha='center', va='center',
                fontsize=TEXT_SIZE, zorder=5)

    return fig

fig = subset_venn()
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_venn-sottoinsiemi

Un diagramma di Venn che illustra due insiemi $O$ e $A$ tali che $O \subseteq
A$: $O$ è l'insieme degli Avengers con forza sovrumana (Thor, Hulk e Capitan 
America), $A$ è l'insieme di tutti gli Avengers e $\Omega$ è l'insieme universo
di tutti i supereroi.
````


Si verifica facilmente come qualunque insieme risulti sempre incluso
nell'insieme universo, e come analogamente l'insieme vuoto risulti sempre
incluso in qualunque insieme:

```{math}
\forall S \subseteq \Omega \quad \varnothing \subseteq S \subseteq \Omega ,
```

e questa relazione continua a valere se si considera la relazione di inclusione
in senso stretto, a patto che $S$ sia diverso dall'insieme vuoto (affinché
valga la prima parte della relazione) e dall'insieme universo (affinché possa
valere la sua seconda parte).

## Vero o falso?

Analizzate ciascuna delle seguenti affermazioni, che riguardano le relazioni
tra insiemi, e dite se è vera o falsa, motivando il vostro ragionamento.
Cliccate su di essa per visualizzare la risposta corretta.

````{tf-item}
Se $S \subseteq T$, allora ogni elemento di $S$ appartiene anche a $T$.
+++
**Vera**. Questa è esattamente la definizione di sottoinsieme: $S \subseteq T$
significa che per ogni $s \in \Omega$, se $s \in S$ allora $s \in T$. In altri
termini, $T$ contiene almeno tutti gli elementi di $S$ (e possibilmente altri).
````

````{tf-item}
Se $S \subset T$, allora $S$ e $T$ non possono essere uguali.
+++
**Vera**. La definizione di inclusione in senso stretto richiede esplicitamente
che $S \subseteq T$ e che $S \neq T$. L'uguaglianza è quindi esclusa per
costruzione: $S \subset T$ garantisce che $T$ contiene almeno un elemento che
non appartiene a $S$.
````

````{tf-item}
Se $S \subseteq T$, allora necessariamente $S \neq T$.
+++
**Falsa**. L'inclusione $S \subseteq T$ ammette anche il caso $S = T$: due
insiemi uguali si includono sempre mutuamente, quindi in particolare
$S \subseteq S$ è sempre vera. Quando si vuole escludere l'uguaglianza si
deve usare la relazione di inclusione in senso stretto $S \subset T$.
````

````{tf-item}
Due insiemi sono uguali se e solo se si includono mutuamente.
+++
**Vera**. Questa è la definizione di uguaglianza tra insiemi: $S = T$ se e
solo se $S \subseteq T$ e $T \subseteq S$. La condizione è bidirezionale:
ogni elemento di $S$ appartiene a $T$ e viceversa, quindi i due insiemi
contengono esattamente gli stessi elementi.
````

````{tf-item}
L'insieme vuoto $\varnothing$ è un sottoinsieme di qualunque insieme.
+++
**Vera**. Da un punto di vista logico, $\varnothing \subseteq S$ equivale alla
proposizione $\forall \omega \in \Omega \quad \omega \in \varnothing
\rightarrow \omega in S$.  Questo è un esempio di «verità vacua»: nella logica
classica, un'implicazione $P \rightarrow Q$ è considerata vera ogni volta che
$P$ è falsa, indipendentemente dal valore di verità di $Q$. Poiché nessun
elemento appartiene all'insieme vuoto, l'antecedente $x \in \varnothing$ è
sempre falso e quindi l'implicazione risulta automaticamente vera.
````

````{tf-item}
L'insieme vuoto $\varnothing$ è un sottoinsieme stretto di qualunque insieme.
+++
**Falsa**. L'inclusione stretta $\varnothing \subset S$ richiede che
$\varnothing \subseteq S$ e che $\varnothing \neq S$. La seconda condizione
non vale quando $S = \varnothing$: in quel caso i due insiemi sono uguali, e
l'inclusione stretta non sussiste.
````


## Esercizi

````{exercise}
:label: ex-alpha-flight-inclusioni

Considerate i seguent universo composto da membri della
[Alpha flight](https://marvel.fandom.com/wiki/Alpha_Flight_(Canada)):

```{math}
\Omega = \{ \text{Guardian}, \text{Sasquatch}, \text{Snowbird}, \text{Puck}, \text{Shaman} \} .
```

Siano inoltre

- $A = \{ \text{Guardian}, \text{Sasquatch}, \text{Snowbird}, \text{Puck} \}$,
- $B = \{ \text{Guardian}, \text{Sasquatch} \}$,
- $C = \{ \text{Sasquatch}, \text{Guardian} \}$,
- $D = \{ \text{Guardian}, \text{Puck}, \text{Shaman} \}$.

1. Stabilite quali tra le relazioni seguenti sono vere:
  $B \subseteq A$, $A \subseteq B$, $B = C$, $D \subseteq A$, $D \subset A$.
2. Trovate un insieme $E$ tale che $B \subset E \subset A$.
3. Trovate un insieme $F$ tale che $A \subset F \subseteq \Omega$.
````

````{solution} ex-alpha-flight-inclusioni
:class: dropdown

1. Sono vere $B \subseteq A$ e $B = C$. Infatti tutti gli elementi di $B$
   appartengono ad $A$, mentre $B$ e $C$ contengono esattamente gli stessi
   elementi, solo in ordine diverso. Sono invece false $A \subseteq B$ (in
   quanto vale $B \subseteq A$ e i due insiemi sono diversi),
   $D \subseteq A$ e a maggior ragione $D \subset A$ (perché Shaman appartiene
   a $D$ ma non ad $A$).
2. Si può scegliere $E = \{ \text{Guardian}, \text{Sasquatch}, \text{Puck} \}$
   oppure $E = \{ \text{Guardian}, \text{Sasquatch}, \text{Snowbird} \}$.
3. L'unica scelta possibile è $F = \Omega$.
````

````{exercise}
:label: ex-guardiani-badge

In un archivio dei [Guardiani della
Galassia](https://marvel.fandom.com/wiki/Guardians_of_the_Galaxy_(Earth-616)),
sia $\Omega$ l'insieme di tutti gli eroi registrati. Si considerano i due
insiemi

```{math}
S = \{ x \in \Omega \mid x \text{ ha partecipato alla missione su Knowhere} \}
```

e

```{math}
T = \{ x \in \Omega \mid x \text{ ha ricevuto un badge per la missione su Knowhere} \} .
```

Sapendo che ogni eroe che ha partecipato alla missione ha ricevuto un badge e
che ogni eroe con badge ha effettivamente partecipato:

1. Scrivete le due inclusioni che legano $S$ e $T$.
2. Deducete la relazione tra $S$ e $T$.
3. Spiegate perché conoscere soltanto $S \subseteq T$ non basterebbe per
  concludere che $S = T$.
````

````{solution} ex-guardiani-badge
:class: dropdown

1. Le ipotesi si traducono nelle inclusioni $S \subseteq T$ e $T \subseteq S$.
2. Poiché i due insiemi si includono mutuamente, si conclude che $S = T$.
3. La sola inclusione $S \subseteq T$ garantisce soltanto che ogni elemento di
  $S$ appartiene anche a $T$, ma non esclude che $T$ contenga elementi in più.
  Per ottenere l'uguaglianza serve anche l'inclusione opposta $T \subseteq S$.
````

````{exercise}
:label: ex-teen-titans-python

Considerate gli insiemi

```{math}
\begin{align*}
A &= \{ \text{Robin}, \text{Starfire}, \text{Raven} \} \enspace, \\
B &= \{ \text{Robin}, \text{Starfire}, \text{Raven}, \text{Beast Boy} \}
     \enspace, \\
C &= \{ \text{Starfire}, \text{Robin}, \text{Raven} \} \enspace.
\end{align*}
```

Con riferimento alla parte del {ref}`sec_dati-strutturati` che descrive
gli insiemi in Python, e in particolare alla {ref}`table-set-operators`:

1. costruite gli oggetti python corrispondenti ad $A$, $B$ e $C$ e
   memorizzateli nelle variabili `a`, `b` e `c`;
2. determinate, senza eseguire codice, il valore delle espressioni `a <= b`,
   `a < b`, `a == c` e `b <= c`;
2. scrivete uno script che stampi il valore di verità di ciascuna di
   queste espressioni, ed eseguitelo, verificando che i risultati siano
   coerenti con i risultati del punto precedente;
3. modificate $A$ aggiungendo un elemento, in modo che il nuovo insieme non
   sia più un sottoinsieme di $B$.
````

````{solution} ex-teen-titans-python
:class: dropdown

1. Se identifichiamo ogni eroe con una stringa che ne descrive il nome, il modo
   più semplice di procedere è quello di utilizzare dei letterali di tipo
   `set`.

```{code-cell} python
a = {'Robin', 'Starfire', 'Raven'}
b = {'Robin', 'Starfire', 'Raven', 'Beast Boy'}
c = {'Starfire', 'Robin', 'Raven'}
```
2. Tutte le espressioni devono essere vere, a parte `b <= c`. Le prime due sono
   vere perché $A \subset B$, e dunque $A \subseteq B$; la terza è vera perché
   le descrizioni estensive dei due insiemi si equivalgono, a meno di una
   permutazione degli elementi; infine, Beasty Boy appartiene a $B$ ma non a
   $C$.
2. Un possibile script è il seguente.

```{code-cell} python

expr = { 'A <= B': a <= b,
        'A < B': a < b,
        'A == C': a == c,
        'B <= C': b <= c }

for e, v in expr.items():
    print(f'{e}: {v}')
```

3. Nessuno tra i supereroi indicati può essere utilizzato, perché $A = C$;
   risulta dunque necessario aggiungere ad $A$ un nuovo supereroe. Siccome
   tutti i personaggi sono membri dei [Teen
   Titans](https://dc.fandom.com/wiki/Teen_Titans_(New_Earth)), possiamo ad
   esempio considerare $A' = A \cup \{ \text{Cyborg} \}$, ottenendo un insieme
   che non è più contenuto in $B$.
````


## Concetti fondamentali

Pensate ai concetti fondamentali illustrati in questo paragrafo ed elencateli.
Nella lista qui sotto sono già presenti gli stessi concetti, ma nascosti.
Cliccate sul pulsante per mostrarli sotto forma di parole chiave, quindi
confrontateli con la vostra lista. Provate infine a descrivere ciascun concetto
con parole vostre.

````{sds-wordcloud}
Sottoinsieme
Sovrainsieme
Inclusione
Inclusione stretta
Uguaglianza tra insiemi
````
