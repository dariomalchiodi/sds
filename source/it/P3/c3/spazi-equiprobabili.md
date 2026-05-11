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

(sec_spazi-equiprobabili)=
# Spazi degli esiti finiti

Quando lo spazio degli esiti $\Omega$ è finito, per descrivere completamente
la funzione di probabilità è sufficiente stabilire il suo valore per ciascun
evento elementare. Il motivo è semplice: ogni evento dell'algebra considerata
si può &mdash; in questo caso &mdash; sempre esprimere come l'unione di un
numero finito di eventi elementari a due a due disgiunti. Quindi la sua
probabilità si ricava applicando il terzo assioma di Kolmogorov. Come vedremo,
emergono due casi distinti: quello _equiprobabile_, in cui tutti gli eventi
elementari hanno la stessa probabilità, e quello _non equiprobabile_, in cui
queste probabilità possono essere diverse tra loro.

````{admonition} Algebre banali e non banali
:class: tip
Nel teorema che segue, ho fissato come algebra l'insieme delle parti dello
spazio degli esiti. Questo permette di semplificare la dimostrazione, in quanto
implica che ogi esito di $\Omega$ individua un evento elementare nell'algebra.
In linea di principio, si potrebbe lavorare con un'algebra arbitraria
$\mathsf A \subseteq 2^\Omega$, ma ciò richiederebbe di modificare l'enunciato
del teorema, sostituendo agli insiemi singoletto quelli che sono detti gli
_atomi_ dell'algebra, che per un insieme finito coincidono con i blocchi non
vuoti minimi della partizione di $\Omega$ indotta dall'algebra.
Equivalentemente, gli atomi individuano i più piccoli eventi non vuoti dell'algebra, e ogni altro evento si ottiene come unione di alcuni di essi.
````

````{prf:theorem} Caratterizzazione delle probabilità su uno spazio finito
:label: teo-prob-spazio-finito

Sia $\Omega = \{ \omega_1, \ldots, \omega_n \}$ e sia
$\mathsf A = 2^\Omega$. Inoltre, dato un evento $E \in \mathsf A$, sia
$I_E = \{ i \in [1..n] \mid \omega_i \in E \}$ l'insieme degli indici degli
elementi contenuti nell'evento. Infine, sia data una funzione 
$\mathbb P : \mathsf A \to [0, 1]$. Le due seguenti condizioni sono
equivalenti:

1. $\mathbb P$ è una probabilità su $\mathsf A$;
2. esistono $n$ numeri reali $p_1, \ldots, p_n \geq 0$ tali che
   $\sum_{i=1}^n p_i = 1$ e, per ogni evento $E \in \mathsf A$, vale
   $\mathbb P(E) = \sum_{i \in I_E} p_i$. In tal caso, si ha
   necessariamente $p_i = \mathbb P(\{\omega_i\})$ per ogni $i = 1, \ldots, n$.

Quindi, su uno spazio degli esiti finito, una probabilità è completamente
determinata dai valori che assume per gli eventi elementari.
````
````{admonition} _
:class: myproof

Supponiamo che $\mathbb P$ sia una funzione di probabilità su $\mathsf A$, e
poniamo $p_i = \mathbb P(\{\omega_i\})$ per ogni $i = 1, \ldots, n$.

Dal primo assioma di Kolmogorov segue subito che $p_i \geq 0$ per ogni $i$.
Inoltre i singoletti $\{\omega_1\}, \ldots, \{\omega_n\}$ sono a due a due
disgiunti e la loro unione è $\Omega$, quindi

```{math}
1 = \mathbb P(\Omega)
= \mathbb P\left( \bigcup_{i=1}^n \{\omega_i\} \right)
= \sum_{i=1}^n \mathbb P(\{\omega_i\})
= \sum_{i=1}^n p_i \enspace.
```

Infine, ogni evento $E \in \mathsf A$ si può esprimere come l'unione disgiunta
$E = \bigcup_{i \in I_E} \{\omega_i\}$. Pertanto

```{math}
\mathbb P(E) = \sum_{i \in I_E} \mathbb P(\{\omega_i\})
= \sum_{i \in I_E} p_i \enspace.
```

Abbiamo quindi dimostrato che la prima condizione implica la seconda.
Dimostriamo ora l'implicazione inversa. Supponiamo che
$p_1, \ldots, p_n \geq 0$ siano tali che $\sum_{i=1}^n p_i = 1$, e definiamo
una funzione $\mathbb P : \mathsf A \to [0, 1]$ ponendo

```{math}
\mathbb P(E) = \sum_{i \in I_E} p_i
```

per ogni $E \in \mathsf A$. Dobbiamo verificare che $\mathbb P$ soddisfi gli
assiomi di Kolmogorov. La non negatività è immediata, perché ogni $p_i$ è non
negativo. Inoltre,

```{math}
\mathbb P(\Omega) = \sum_{i=1}^n p_i = 1 \enspace.
```

Infine, $\mathsf A$ è finita, quindi ogni sequenza di eventi a due a due
disgiunti deve essere anch'essa finita. Per una siffatta sequenza
$E_1, \dots, E_r$, si ha che $\cup_{k=1}^r E_k$ è l'insieme contenente tutti
gli esiti di $E_1$, di $E_2$, e così via. Quindi

```{math}
\mathbb P\left( \bigcup_{k=1}^r E_k \right)
= \sum_{i \in I_{\cup_k E_k}} p_i
= \sum_k \sum_{i \in I_{E_k}} p_i
= \sum_k \mathbb P(E_k) \enspace.
```

Quindi $\mathbb P$ è una probabilità su $\mathsf A$. Abbiamo pertanto mostrato
che la seconda condizione implica la prima, così che esse sono logicamente
equivalenti. Osserviamo infine che, se $\mathbb P$ soddisfa la seconda
condizione, allora $\mathbb P(\{\omega_i\}) = p_i$ per ogni $i = 1, \ldots, n$.
In altre parole, i numeri $p_i$ sono proprio le probabilità degli eventi
elementari in $\Omega$.
````

Riassumendo, in uno spazio campionario finito la probabilità si ricostruisce
interamente a partire dai valori che essa assume per gli eventi elementari. Una
volta noti $\mathbb P(\{\omega_1\}), \ldots, \mathbb P(\{\omega_n\})$,
la probabilità di qualunque evento $E$ si ottiene sommando i valori relativi
agli eventi elementari individuati dagli esiti contenuti in $E$.

## Spazi degli esiti equiprobabili

Il caso più semplice da trattare è quello in cui tutti gli eventi elementari
hanno la stessa probabilità.

````{prf:definition} Spazio equiprobabile di probabilità
:label: def-spazio-equiprobabile

Sia $(\Omega, \mathsf A, \mathbb P)$ uno spazio di probabilità con $\Omega$
finito. Se esiste una costante $p \in [0, 1]$ tale che
$\mathbb P(\{\omega\}) = p$ per ogni $\omega \in \Omega$, si dice che
$(\Omega, 2^\Omega, \mathbb P)$ è uno _spazio equiprobabile di probabilità_,
o più semplicemente uno _spazio equiprobabile_.
````

Negli spazi di questo tipo l'equiprobabilità riguarda gli eventi elementari, e
il loro numero individua il valore di $p$, come mostrato di seguito.

````{prf:theorem}
:label: teo-prob-equiprobabile
Sia $(\Omega, \mathsf A, \mathbb P)$ uno spazio equiprobabile, con
$|\Omega| = n$. Allora, per ogni $\omega \in \Omega$,

```{math}
\mathbb P(\{\omega\}) = \frac{1}{n} \enspace.
```
````
````{admonition} _
:class: myproof

Senza ledere la generalità del ragionamento, poniamo
$\Omega = \{ \omega_1, \dots \omega_n \}$. Se ogni evento elementare ha
probabilità $p$, applicando gli assiomi di Kolmogorov si ottiene

```{math}
1 = \mathbb P(\Omega) = 
\mathbb P \left( \cup_{i=1}^n \{ \omega_i \} \right) = 
\sum_{i=1}^n \mathbb P(\{\omega\}) = np \enspace,
```

da cui segue subito $p = \frac{1}{n}$.
````

Quando tutte le probabilità degli eventi elementari coincidono, la formula
generale del {prf:ref}`teo-prob-spazio-finito` si semplifica parecchio, come
dimostrato nel seguente teorema.

````{prf:theorem}
:label: teo-regola-classica

Sia $(\Omega, \mathsf A, \mathbb P)$ uno spazio equiprobabile, con
$|\Omega| = n$. Per ogni evento $E \in \mathsf A$, si ha

```{math}
:label: eq_prob-classica

\mathbb P(E) = \frac{|E|}{n} \enspace.
```
````

````{admonition} _
:class: myproof

Assumiamo, senza ledere la generalità, che $E$ contenga esattamente $k$ esiti
elementari. Allora,

```{math}
\mathbb P(E) = \sum_{\omega_i \in E} \mathbb P(\{\omega_i\})
= \sum_{\omega_i \in E} \frac{1}{n}
= \sum_{i=1}^k \frac{1}{n}
= \frac{k}{n} = \frac{|E|}{n} \enspace.
```
````

Questa formula giustifica la cosiddetta _definizione classica della
probabilità_: nel caso equiprobabile, la probabilità di un evento si calcola
come rapporto tra il numero degli esiti favorevoli e il numero degli esiti
possibili. È una regola comoda, ma va usata solo quando l'ipotesi di
equiprobabilità è davvero ragionevole. In pratica, la si usa quando è sensato
assumere una forma di uniformità nell'incertezza dell'esperimento casuale, per
esempio quando

- si lanciano dadi o monete bilanciati,
- si pescano carte da un mazzo ben mescolato,
```{margin}
Anche in questo caso _contenitore_ e _oggetto_ sono termini che prescindono
dalla loro effettiva tangibilità.
```
- si effettuano estrazioni da un contenitore dopo che gli oggetti in esso
  inseriti sono stati mescolati.

In casi come questo, le regole del calcolo combinatorio descritte nel
{ref}`chap_calcolo-combinatorio` sono spesso utili per calcolare numeratore e
denominatore in {eq}`eq_prob-classica`.

````{prf:example}
:label: ex-spazio-equiprobabile

Se $\Omega$ è l'insieme dei supereroi nel nostro dataset, e ogni supereroe
ha la stessa probabiilità di essere osservato, questa probabilità è uguale
all'inverso del numero totale di personaggi, come calcolato nella cella
seguente.

```{code-cell} python

import pandas as pd

heroes = pd.read_csv('data/heroes.csv', index_col='name')
n = len(heroes)
p = 1 / n
print(rf'La probabilità di estrarre un personaggio a caso è p = {p:.4f}.')
```

````

````{prf:example}
:label: ex-somma-due-dadi
Consideriamo il lancio di due dadi bilanciati di colori diversi, diciamo uno
rosso e uno blu. Lo spazio degli esiti è costituito da tutte le coppie
ordinate $(\omega_\text{rosso}, \omega_\text{blu})$, dove
$\omega_\text{rosso} \in [1..6]$ indica il risultato del dado rosso, e in modo
analogo si interpreta la seconda componente.

Per il principio fondamentale del calcolo combinatorio, il numero totale di
esiti possibili è $6 \times 6 = 36$. Siccome i dadi sono bilanciati e
distinguibili, ciascuna coppia ordinata ha probabilità $\frac{1}{36}$, quindi
ci troviamo in uno spazio equiprobabile con

```{math}
\Omega = \{ (\omega_\text{rosso}, \omega_\text{blu}) \mid
\omega_\text{rosso}, \omega_\text{blu} \in [1..6] \} \enspace.
```

Per esempio, l'evento

```{math}
E = \{ (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1) \}
```

si verifica quando la somma dei risultati è uguale a $7$, ed è illustrato
nella {numref}`fig_dice-sum`. La sua probabilità è

```{math}
\mathbb P(E) = \frac{|E|}{|\Omega|} = \frac{6}{36} = \frac{1}{6} \enspace.
```
````

```{code-cell} python
:tags:  [hide-input]

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

x, y = np.meshgrid(range(1, 7), range(1, 7))
x, y = x.ravel(), y.ravel()

with mpl.rc_context({'figure.figsize': (3, 3),
                     'figure.titlesize': 8,
                     'figure.dpi': 150,
                     'xtick.labelsize': 7,
                     'ytick.labelsize': 7,
                     'axes.labelsize': 7,}):

  fig, ax = plt.subplots()

  ellipse = Ellipse((3.5, 3.5), width=8, height=1, angle=-45,
                    facecolor='lightblue', edgecolor='lightblue',
                    linewidth=1, alpha=0.5, zorder=1)
  ax.add_patch(ellipse)

  ax.scatter(x, y, s=20, c='steelblue', edgecolors='black', linewidths=0.5)

  ax.set_xlabel('Risultato del dado rosso')
  ax.set_ylabel('Risultato del dado blu')
  ax.set_title(r'$\Omega = \{ (\omega_\text{rosso}, \omega_\text{blu}) \mid '
              r'\omega_\text{rosso}, \omega_\text{blu} \in [1..6] \}$')
  ax.set_xticks(range(1, 7))
  ax.set_yticks(range(1, 7))
  ax.set_xlim(0.5, 6.5)
  ax.set_ylim(0.5, 6.5)
  ax.grid(True, alpha=0.3)
  ax.set_aspect('equal')
  plt.show()
```
````{customfigure}
:name: fig_dice-sum

Rappresentazione dello spazio degli esiti per il lancio di due dadi
distinguibili (cerchi blu) e dell'evento in cui la somma dei risultati è uguale
a $7$ (ellisse azzurra).
````

```{margin}
Se in questo esempio si sostituiscono gli anni di prima apparizione dei
personaggi con il giorno di nascita di un gruppo di persone presenti in una
stanza, si ottiene il cosiddetto [paradosso del
compleanno](https://it.wikipedia.org/wiki/Paradosso_del_compleanno).
```
````{prf:example}
:label: ex-problema-compleanni
Supponiamo che l'anno di prima apparizione di un personaggio sia distribuito
uniformemente tra il valore minimo e il valore massimo osservati nel dataset, e
che le estrazioni siano indipendenti. In questo modello, vogliamo calcolare la
probabilità che, osservando $n$ personaggi, non compaiano due anni di prima
apparizione uguali.

Indichiamo con $a$ il numero di anni possibili. L'ipotesi di uniformità ci
permette di lavorare in uno spazio equiprobabile sulle sequenze di lunghezza
$n$ formate con questi $a$ anni.

- Un esito favorevole corrisponde a una sequenza di $n$ anni tutti diversi tra
  loro. Il numero di tali sequenze è $D_{a, n} = \frac{a!}{(a-n)!}$, perché a
  ognuna corrisponde una e una sola disposizione senza ripetizione di $a$
  oggetti in $n$ posti.
- Un esito possibile qualunque corrisponde invece a una sequenza di $n$ anni
  con eventuali ripetizioni. Dunque vi sono $d_{a, n} = a^n$ diverse sequenze.

Di conseguenza, la probabilità che non si ripeta mai un anno di prima
apparizione è

```{math}
\frac{D_{a, n}}{d_{a, n}} = \frac{a!}{(a-n)! a^n} \enspace.
```

Possiamo usare i dati a nostra disposizione per stimare il valore di $a$ a
partire dalla differenza tra anno massimo e anno minimo di prima apparizione.

```{margin}
La conversione a `int` è necessaria perché la presenza di valori mancanti
causa un'implicito utilizzo del tipo `float` per l'anno di apparizione quando
il _dataset_ viene caricato.
```
```{code-cell} python
import pandas as pd

heroes = pd.read_csv('data/heroes.csv', index_col=0)
years = heroes['first_appearance']
min_year, max_year = min(years), max(years)
a = int(max_year - min_year) + 1
print(a)
```

Ora possiamo calcolare la probabilità $p_{n, a}$ che, osservando $n$
personaggi scelti secondo questo modello, non ve ne siano due con lo stesso
anno di prima apparizione, e rappresentarne il valore al variare di $n$.
Il valore di questa probabilità è necessariamente uguale a 0 quando $n > a$,
ma si avvicina a 0 per valori relativamente piccoli di $n$, come si può vedere
nel grafico qui sotto.

```{code-cell} python

import math
import numpy as np
import matplotlib.pyplot as plt

def prob_no_common_year(n, a):
    return math.factorial(a) / (math.factorial(a-n) * a**n)

x = range(1, a//3)
p1 = [prob_no_common_year(n, a) for n in x]

plt.plot(list(x), p1)
plt.show()
```
````

## Il caso non equiprobabile

Quando lo spazio degli esiti è finito, ciò non significa che lo spazio di
probabilità costruito a partire da esso sia necessariamente equiprobabile.
Se i valori di $\mathbb P$ per gli eventi elementari sono diversi tra loro,
non è più possibile applicare {eq}`eq_prob-classica`, e bisogna tornare alla
formula generale del {prf:ref}`teo-prob-spazio-finito`, sommando le probabilità
degli eventi elementari favorevoli.

````{prf:example}
:label: ex-due-dadi-indistinguibili
Torniamo al lancio di due dadi bilanciati, ma immaginiamoli questa volta
_indistinguibili_. In questo modello, un esito elementare non è più una coppia
ordinata $(i, j)$, ma una coppia non ordinata $\{i, j\}$ con
$1 \leq i \leq j \leq 6$. Lo spazio degli esiti è quindi

```{math}
\Omega = \{ \{i, j\} \mid 1 \leq i \leq j \leq 6 \} \enspace,
```

```{margin}
Per chiarire meglio questo punto, immaginate che i dadi siano colorati come
nell’{prf:example}`ex-somma-due-dadi`, ma che diventino indistinguibili per un
osservatore che soffre di daltonismo: se $i < j$, le due coppie ordinate
$(i, j)$ e $(j, i)$ vengono percepite dall'osservatore come la coppia non
ordinata $\{ i, j \}$
```
e contiene $21$ esiti elementari: $d_{6, 2} / p_2 = 15$ corrispondono ai casi
in cui i lanci hanno esiti diversi, e sei a quelli in cui sono invece uguali.
Questi esiti, però, non sono equiprobabili. Infatti, se $i < j$, l'esito
$\{i, j\}$ si può realizzare in due modi distinti: $i$ in un dado e $j$
nell'altro, o viceversa. Ognuno di questi eventi elementari avrà pertanto
probabilità $2/36$. Quando invece $i = j$, esiste una sola configurazione dei
dadi che equivale all'evento elementare corrispondente, che avrà probabilità
$1/36$. In generale, $\{\{i, j\}\}$ ha dunque probabilità

```{math}
\mathbb P(\{\{i, j\}\}) =
\begin{cases}
\frac{2}{36} = \frac{1}{18} & \text{se } i < j, \\
\frac{1}{36} & \text{se } i = j.
\end{cases}
```

Per esempio, l'evento $E = \{ \{1, 6\}, \{2, 5\}, \{3, 4\} \}$ che corrisponde
a ottenere una somma dei due risultati pari a $7$, ha probabilità

```{math}
\mathbb P(E) = \frac{2}{36} + \frac{2}{36} + \frac{2}{36} = \frac{1}{6}
\enspace,
```

mentre il rapporto $\frac{|E|}{|\Omega|} = \frac{3}{21} = \frac{1}{7}$ sarebbe
errato. Questo esempio fa vedere bene il punto: in uno spazio finito contare
gli esiti basta solo nel caso equiprobabile; negli altri casi bisogna pesare
gli esiti, non solo contarli.
````



## Esercizi

```{exercise} •
Nell’{prf:ref}`ex-somma-due-dadi`, il numero di esiti in $\Omega$ si poteva
calcolare anche facendo riferimento a uno dei concetti introdotti nel
{ref}`chap_calcolo-combinatorio`. Qual è questo concetto e come lo si può
applicare a questo esempio?
```

```{exercise} •
Facendo riferimento allo spazio di probabilità
dell’{prf:ref}`ex-somma-due-dadi`, calcolate la probabilità dei seguenti
eventi, visualizzando i corrispondenti diagrammi di Venn:

- il risultato del lancio del dado blu è uguale a $3$;
- il risultato del lancio del dado blu è minore di $3$;
- la somma dei risultati dei due lanci è uguale a $9$;
- la somma dei risultati dei due lanci è maggiore di $9$;
- la somma dei risultati dei due lanci è minore o uguale di $9$;
- la differenza dei risultati dei due lanci è uguale a 1.
```

```{exercise} •
:label: ex-dadi-distinguibili-non-indistinguibili

Pensate a un evento che abbia senso nello spazio di probabilità
dell’{prf:ref}`ex-somma-due-dadi`, ma non in quello
dell’{prf:ref}`ex-due-dadi-indistinguibili`. Descrivetelo esplicitamente e
spiegate perché, una volta dimenticato l’ordine dei due risultati, non è più
possibile rappresentarlo come evento del secondo modello.
```
```{solution} ex-dadi-distinguibili-non-indistinguibili
:class: dropdown

Un esempio naturale è l’evento $A = \{ (i, 2i) \mid i \in [1..3] \}$, cioè
«il risultato del dado blu è uguale al doppio di quello del dado rosso». Questo
evento ha perfettamente senso quando i due dadi sono distinguibili, perché le
due componenti della coppia ordinata rappresentano due dadi diversi. Nel
modello con dadi indistinguibili, invece, l’esito osservato è una coppia non
ordinata $\{i, j\}$, quindi si perde l’informazione su quale risultato
appartenga al dado rosso e quale al dado blu. Per esempio, gli esiti ordinati
$(3, 6)$ e $(6, 3)$ diventano entrambi l’unico esito non ordinato $\{ 3, 6 \}$,
ma il primo appartiene ad $A$ mentre il secondo no. In altri termini,
osservando l’esito non ordinato $\{ 3, 6 \}$ non si può più stabilire se $A$
si sia verificato oppure no. Per questo motivo $A$ non può essere
rappresentato come evento nello spazio dei dadi indistinguibili. In generale,
solo gli eventi che non cambiano scambiando i due dadi possono essere
interpretati anche nel modello indistinguibile.
```

```{exercise} •
Motivate il fatto che il numero di esiti in $\Omega$ per l'esperimento casuale
che consiste nel lanciare due dadi indistinguibili è uguale a $21$, e
spiegate perché lo spazio così ottenuto non è equiprobabile.
```