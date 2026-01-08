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

```{code-cell} python
:tags: [remove-cell]

import matplotlib.pyplot as plt
plt.style.use('../../_static/sds.mplstyle')
%matplotlib inline
plt.ioff()
```

(sec_spazi-equiprobabili)=
# Spazi equiprobabili

In molte situazioni, l'esperimento casuale alla base di uno spazio di
probabilità ha la proprietà di assegnare un valore di probabilità costante
a tutti gli eventi elementari. In casi come questo, si parla di _spazio
equiprobabile di probabilità_, o più semplicemente di _spazio equiprobabile_.

````{prf:definition} Spazio equiprobabile di probabilità
:label: def-spazio-equiprobabile
Sia $(\Omega, \mathsf A, \mathbb P)$ uno spazio di probabilità. Se esiste una
costante $p \in [0, 1]$ tale che $\mathbb P(\{w\}) = p$ per ogni $w \in \Omega$,
si dice che $(\Omega, \mathsf A, \mathbb P)$ è uno _spazio equiprobabile di
probabilità_, o più semplicemente uno _spazio equiprobabile_.
````

Pertanto, negli spazi di questo tipo l'equiprobabilità riguarda gli eventi
elementari, e la loro probabilità è legata alla numerosità dell'insieme degli
esiti, come illustrato nel seguente teorema.

````{prf:theorem}
:label: teo-prob-equiprobabile
In uno spazio equiprobabile, l'insieme degli esiti deve avere una cardinalità
finita $n \in \mathbb N$ e $p = \frac{1}{n}$.
````
````{admonition} _
:class: myproof

Iniziamo mostrando che quando $\Omega$ è finito e $n$ indica la sua
cardinalità, la probabilità di ogni evento elementare è uguale a $\frac{1}{n}$.
Dalla definizione di cardinalità si ottiene necessariamente che devono esistere
$n$ esiti $w_1, \ldots, w_n$ tali che $\Omega = \{ w_1, \ldots, w_n \}$, e
l'ipotesi di equiprobabilità implica che $\mathbb P(\{w_i\}) = p$ per ogni
$i = 1, \ldots, n$. Gli $n$ eventi elementari possibili costituiscono una
partizione di $\Omega$, nel senso che
$\{ w_1 \} \cup \ldots \cup \{ w_n \} = \Omega$ e
$\{ w_i \} \cap \{ w_j \} = \{\}$ ogni volta che $i \neq j$. Pertanto,
applicando il secondo e il terzo assioma di Kolmogorov si ottiene che

```{math}
1 = \mathbb P(\Omega) = \mathbb P( \{ w_1 \} \cup \ldots \cup \{ w_n \} )
= \sum_{i=1}^n \mathbb P(\{ w_i \}) = \sum_{i=1}^n p = np \enspace.
```

Dunque $p = \frac{1}{n}$. Inoltre è impossibile che $\Omega$ sia infinito,
perché dalla formula precedente si vede come il valore di $p$ diminuisca
strettamente al crescere della cardinalità di $\Omega$, e quando questa tende
all'infinito il valore di $p$ dovrebbe tendere a zero. Ciò non può però
verificarsi perché andrebbbe a contraddire gli assiomi di Kolmogorov: in
particolare, in tal caso si avrebbe
$\mathbb P(\Omega) = \sum_{i=1}^n P(\{ w_i \}) = \sum_{i=1}^n 0 = 0$.
````

Gli eventi non elementare, in generale, avranno probabilità diverse tra loro.
Ma è facile vedere come anche queste probabilità dipendono da $p$, come
evidenziato nel seguente teorema.

````{prf:theorem}
Per ogni evento $E \subseteq \Omega$ nello spazio equiprobabile
$(\Omega, \mathsf A, \mathbb P)$ si ha

```{math}
:label: eq_prob-classica

\mathbb P(E) = \frac{|E|}{n} \enspace.
```
````

````{admonition} _
:class: myproof

Siccome per il {prf:ref}`teo-prob-equiprobabile` lo spazio degli esiti $\Omega$
deve avere una cardinalità finita $n$, per ogni $E \subseteq \Omega$ devono
esistere $k$ esiti $w_1, \ldots, w_k$, con $k \leq n$ tali che
$E = \{ w_1, \ldots, w_k \}$, e quindi

```{math}
\mathbb P(E) = \sum_{i=1}^k \mathbb P(\{ w_i \})
   = \sum_{i=1}^k \frac{1}{n} = \frac{k}{n} \enspace.
```

La tesi si ottiene notando che $|E| = k$.
````

Questo teorema fornisce un fondamento teorico alla cosiddetta
_definizione classica della probabilità_, secondo la quale la probabilità di
un evento si calcola come il rapporto tra il numero degli esiti favorevoli
(intesi come esiti che sono contenuti nell'evento) e il numero di quelli
possibili. Intuitivamente, questa regola ha senso quando il «peso» di ogni
esito, favorevole o possibile che esso sia, è identico. Questa ipotesi è
soddisfatta quando si può assumere una sorta di _uniformità_ nell'incertezza
dell'esperimento casuale che si vuole studiare, come per esempio quando

- si lanciano dadi o monete bilanciati,
- si pescano carte da un mazzo che è stato mischiato,
```{margin}
Anche in questo caso _contenitore_ e _oggetto_ sono termini che prescindono
dalla loro effettiva tangibilità.
```
- si effettuano estrazioni da un contenitore dopo che gli oggetti in esso
  inseriti sono stati mescolati.

In casi come questo, le regole del calcolo combinatorio descritte nel
{ref}`chap_calcolo-combinatorio` sono spesso di aiuto per
calcolare numeratore e denominatore in {eq}`eq_prob-classica`.

```{margin}
Se in questo esempio si sostituiscono gli anni di prima apparizione dei
supereroi con il giorno di nascita di un gruppo di persone presenti in una
stanza, si ottiene il cosiddetto _problema dei compleanni_.
```
````{prf:example}
:label: ex-problema-compleanni
Ipotizzando che l'anno di prima apparizione dei supereroi sia uniformemente
distribuito tra i valori minimo e massimo, calcoliamo la probabilità di
estrarre a caso $n$ supereroi senza trovarne due che sono apparsi per la prima
volta nello stesso anno.

Indichiamo con $a$ il numero di valori distinti per l'anno di prima
apparizione. L'ipotesi di distribuzione uniforme dell'anno di prima apparizione
ci permette di lavorare in uno spazio equiprobabile, nel senso che possiamo
assumere come costante la probabilità che un supereroe estratto a caso dal
_dataset_ sia apparso per la prima volta in un dato anno, e dunque di applicare
la definizione classica di probabilità come indicato di seguito.

- Un esito favorevole corrisponde all'estrazione di $n$ supereroi, ognuno dei
  quali ha un anno di prima apparizione diverso dagli altri: possiamo quindi
  visualizzare questo esito come una sequenza di $n$ anni tutti diversi tra
  loro, scegliendo ogni anno tra $a$ valori distinti, che equivale a
  considerare una disposizione senza ripetizione di $a$ oggetti in $n$ posti.
  Pertanto il numero di esiti favorevoli è uguale a
  $D_{a, n} = \frac{a!}{(a-n)!}$.
- Un esito possibile corrisponde invece all'estrazione di $n$ supereroi,
  indipendentemente dal loro anno di prima apparizione, e tale esito è
  codificabile come una sequenza di $n$ anni, con eventuali ripetizioni. Dunque
  gli esiti possibili coincidono con le disposizioni con ripetizione di $a$
  oggetti in $n$ posti, e il loro numero è $d_{a, n} = a^n$.

Concludendo, la probabilità che estraendo a caso $n$ supereroi non succeda mai
che due di questi abbiano lo stesso anno di prima apparizione è pari a

```{math}
\frac{D_{a, n}}{d_{a, n}} = \frac{a!}{(a-n)! a^n} \enspace.
```
````

Possiamo applicare i risultati ottenuti nell'esempio precedente ai dati a
nostra disposizione: innanzitutto calcoliamo il valore di $a$ in funzione della
differenza tra i valori massimo e minimo per l'anno di prima apparizione.

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

```{margin}
Il valore di questa probabilità è necessariamente uguale a 0 quando $n > a$,
ma si avvicina a 0 per valori relativamente piccoli di $n$, come si può vedere
nel grafico qui sotto.
```
Ora possiamo calcolare la probabilità $p_{n, a}$ che su $n$ supereroi
considerati a caso non ve ne siano nemmeno due che hanno in comune l'anno di
prima apparizione, come indicato nella cella seguente, e graficare il valore
ottenuto al variare di $n$.


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

