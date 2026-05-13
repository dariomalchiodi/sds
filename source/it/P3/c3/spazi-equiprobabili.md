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
nell’{prf:ref}`ex-somma-due-dadi`, ma che diventino indistinguibili per un
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

````{exercise} •
:label: ex-spazi-equip-due-dadi-disposizioni

Nell’{prf:ref}`ex-somma-due-dadi`, il numero di esiti in $\Omega$ si può
calcolare anche facendo riferimento a uno dei concetti introdotti nel
{ref}`chap_calcolo-combinatorio`. Qual è questo concetto e come lo si applica
a questo esempio?
````
````{solution} ex-spazi-equip-due-dadi-disposizioni
:class: dropdown

Lo spazio degli esiti del lancio di due dadi distinguibili può essere visto
come l’insieme delle disposizioni con ripetizione di $6$ simboli in $2$ posti.
Infatti, per ciascuno dei due dadi si può scegliere liberamente uno qualunque
dei $6$ risultati possibili, e lo stesso valore può comparire su entrambi.

Il numero totale di esiti è quindi

```{math}
d_{6, 2} = 6^2 = 36 
\enspace.
```

Questo coincide con il conteggio ottenuto applicando il principio
fondamentale del calcolo combinatorio: sei possibilità per il dado rosso e,
indipendentemente da queste, sei per il dado blu.
````

````{exercise} •
:label: ex-spazi-equip-heroes-squadra

[Nick Fury](https://marvel.fandom.com/wiki/Nicholas_Fury_(Earth-616)) osserva
una teca con nove schede, tutte ugualmente probabili da estrarre: Iron Man,
Thor, Hulk, Black Widow, Wolverine, Storm (tutti personaggi Marvel), Batman,
Superman (personaggi DC) e
[Invincible](https://imagecomics.fandom.com/wiki/Invincible_(Mark_Grayson))
(Image Comics, quindi né Marvel né DC).

1. Qual è la probabilità di estrarre la scheda di Thor?
2. Qual è la probabilità di estrarre una scheda Marvel?
3. Qual è la probabilità di non estrarre una scheda DC?
````

```{solution} ex-spazi-equip-heroes-squadra
:class: dropdown

Lo spazio degli esiti ha nove elementi e il corrispondente spazio di
probabilità è equiprobabile, quindi possiamo usare la regola classica.

1. La scheda di Thor corrisponde a un solo esito favorevole, dunque
  $\mathbb P(\{ \text{Thor} \}) = 1/9$.
2. Le schede Marvel sono sei, quindi $\mathbb P(\text{Marvel}) = 6/9 = 2/3$.
3. Le schede non DC sono sette, perché oltre alle $6$ Marvel c’è anche
  Invincible. Dunque $\mathbb P(\text{non DC}) = 7/9$.
```

````{exercise} ••
:label: ex-spazi-equip-due-dadi-eventi

Facendo riferimento allo spazio di probabilità
dell’{prf:ref}`ex-somma-due-dadi`, calcolate la probabilità dei seguenti
eventi. Se volete, rappresentateli anche con un diagramma di Venn sull'universo
$[1..6]^2$:

1. $A =$ «il risultato del lancio del dado blu è uguale a $3$»;
2. $B =$ «il risultato del lancio del dado blu è minore di $3$»;
3. $C =$ «la somma dei risultati dei due lanci è uguale a $9$»;
4. $D =$ «la somma dei risultati dei due lanci è maggiore di $9$»;
5. $E =$ «la somma dei risultati dei due lanci è minore o uguale a $9$»;
6. $F =$ «la differenza in valore assoluto dei risultati dei due lanci è uguale
   a $1$».
````

```{solution} ex-spazi-equip-due-dadi-eventi
:class: dropdown

Poiché ci troviamo nello spazio equiprobabile dell’{prf:ref}`ex-somma-due-dadi`,
ogni evento elementare ha probabilità $1/36$.

1. Se il risultato per il dado blu è $3$, gli esiti favorevoli sono
   $(i, 3)$ per $i \in [1..6]$, dunque sono sei, e
   $\mathbb P(A) = 6/36 = 1/6$.
2. Se il risultato per il dado blu è minore di $3$, allora può valere solo $1$
   oppure $2$, dunque ci sono due possibilità, a fronte delle sei per il dado
   rosso.   Gli esiti favorevoli sono quindi $2 \cdot 6 = 12$, da cui
   $\mathbb P(B) = 12/36 = 1/3$.
3. La somma è uguale a nove negli esiti $(3, 6)$, $(4, 5)$, $(5, 4)$ e $(6, 3)$,
   che sono quattro. Quindi $\mathbb P(C) = 4/36 = 1/9$.
4. La somma è maggiore di nove se vale $10$, $11$ oppure $12$. Gli esiti
   favorevoli per i tre valori della somma sono rispettivamente $3$, $2$ e $1$,
   per un totale di $6$. Dunque $\mathbb P(D) = 6/36 = 1/6$.
5. Siccome $E = \overline D$, avremo
   $\mathbb P(E) = 1 - \mathbb P(D) = 1 - 1/6 = 5/6$.
6. La condizione $|R - B| = 1$ si verifica negli esiti $(i, i+1)$, per
   $i \in [1..5]$, così come in $(i-1, i)$, per $i \in [2..6]$. In entrambi i
   casi, si tratta di cinque esiti, per un totale di dieci configurazioni
   favorevoli. Pertanto $\mathbb P(F) = 10/36 = 5/18$.
```

````{exercise} •
:label: ex-spazi-equip-shield-dossier

In un archivio della [S.H.I.E.L.D.](https://marvel.fandom.com/wiki/S.H.I.E.L.D.)
ci sono dodici dossier, tutti ugualmente probabili da estrarre: cinque
riguardano gli Avengers, quattro gli X-Men e tre la Justice League. Calcolate
la probabilità degli eventi che seguono.

1. $A=$ «Si estrae un dossier che riguarda un gruppo Marvel».
2. $B=$ «Si estrae un dossier che non riguarda gli X-Men».

Quale proprietà dello spazio di probabilità giustifica il calcolo usato?
````

```{solution} ex-spazi-equip-shield-dossier
:class: dropdown

L’insieme dei dodici dossier è uno spazio degli esiti sul quale è stato
costruito uno spazio equiprobabile di probabilità, quindi possiamo usare
la regola classica {eq}`eq_prob-classica`.

1. I dossier che riguardano gruppi Marvel sono quelli sugli Avengers e quelli
   sugli X-Men, che sono in tutto nove. Quindi
   $\mathbb P(A) = 9/12 = 3/4$.
2. I dossier che non riguardano gli X-Men sono otto, dunque
  $\mathbb P(B) = 8/12 = 2/3$.

In entrambi i casi, il calcolo è giustificato proprio dal fatto che gli esiti
sono equiprobabili.
```

````{exercise} •
:label: ex-spazi-equip-regola-classica

Per ciascuno dei seguenti esperimenti, stabilite se la formula classica
$\mathbb P(E) = |E| / |\Omega|$ si può applicare direttamente, motivando la
vostra risposta.

1. Si estrae a caso una carta da un mazzo ben mescolato di $20$ carte tutte
  diverse, ciascuna dedicata a un supereroe.
2. Si osserva l’anno di prima apparizione di un personaggio scelto
  uniformemente dal dataset dei supereroi.
3. Si sceglie uniformemente uno tra questi nove personaggi: Iron Man, Thor,
   Hulk, Black Widow, Wolverine, Storm, Batman, Superman e Invincible, e si
   osserva soltanto l’universo editoriale di appartenenza del personaggio
   estratto.
````

```{solution} ex-spazi-equip-regola-classica
:class: dropdown

1. Sì. Se il mazzo è ben mescolato e ogni carta è equiprobabile, allora gli
  eventi elementari hanno tutti la stessa probabilità e la formula classica si
  può usare.
2. No. Anche se il personaggio è scelto uniformemente, gli anni di prima
  apparizione non sono in generale equiprobabili, come abbiamo visto nel
  {numref}`sec_disegnare-grafici`.
3. No. Lo spazio degli esiti è finito, ma non equiprobabile. Infatti gli
  esiti possibili sono gli universi editoriali osservati, per esempio Marvel,
  DC e Image Comics, ma essi non hanno la stessa probabilità: nel campione
  proposto, Marvel compare per sei personaggi su nove, DC per due su nove e
  Image Comics per uno su nove. Quindi non si può applicare direttamente la
  formula classica sullo spazio degli esiti così costruito.
```

````{exercise} ••
:label: ex-spazi-equip-dadi-indistinguibili-prob

Nel modello dell’{prf:ref}`ex-due-dadi-indistinguibili`, calcolate la
probabilità dei seguenti eventi:

1. $D =$ «la differenza tra il risultato più grande e quello più piccolo è
   uguale a $4$»;
2. $G =$ «il risultato più grande è minore o uguale di $2$».

Spiegate poi perché, pur avendo cardinalità diverse, questi due eventi hanno
la stessa probabilità.
````

````{solution} ex-spazi-equip-dadi-indistinguibili-prob
:class: dropdown

Nel modello con dadi indistinguibili, gli esiti $\{i, j\}$ con $i < j$ hanno
probabilità $2/36$, mentre quelli del tipo $\{i, i\}$ hanno probabilità
$1/36$.

1. La descrizione estensiva dell'evento $D$ è $\{ \{1, 5\}, \{2, 6\} \}$, per
   cui

   ```{math}
   \mathbb P(D) = 2 \times \frac{2}{36} = \frac{1}{9} \enspace.
   ```

2. Analogamente, $G = \{ \{1, 1\}, \{1, 2\}, \{2, 2\} \}$, che comporta

   ```{math}
   \mathbb P(G) = 2 \times \frac{1}{36} + \frac{2}{36} = \frac{1}{9} \enspace.
   ```

I due eventi hanno la stessa probabilità nonostante $|D| \neq |G|$: nel primo
evento ci sono due esiti, nel secondo tre. Ma tutti gli esiti di $D$ hanno
probabilità $2/36$, mentre solo uno degli esiti in $G$ ha questa probabilità:
gli altri due hanno una probabilità dimezzata.
````

````{exercise} ••
:label: ex-spazi-equip-evento-non-osservabile

Pensate a un evento che abbia senso nello spazio di probabilità
dell’{prf:ref}`ex-somma-due-dadi`, ma non in quello
dell’{prf:ref}`ex-due-dadi-indistinguibili`. Descrivetelo esplicitamente e
spiegate perché, una volta dimenticato l’ordine dei due risultati, non è più
possibile rappresentarlo come evento del secondo modello.
````

````{solution} ex-spazi-equip-evento-non-osservabile
:class: dropdown

Un esempio naturale è l’evento

```{math}
A = \{ (i, 2i) \mid i \in [1..3] \} 
\enspace,
```

cioè «il risultato del dado rosso è la metà di quello del dado blu». Questo
evento ha senso nel modello con dadi distinguibili, perché le due componenti
della coppia ordinata indicano due dadi diversi.

Nel modello con dadi indistinguibili, invece, l’esito osservato è una coppia
non ordinata $\{i, j\}$, quindi l’informazione su quale numero appartenga al
dado rosso e quale al dado blu viene perduta. Per esempio, gli esiti $(3, 6)$
e $(6, 3)$ diventano entrambi l’unico esito non ordinato $\{3, 6\}$, ma solo
il primo appartiene ad $A$.

Di conseguenza, osservando $\{3, 6\}$ non si può più decidere se l’evento si
sia verificato oppure no. Per questo motivo $A$ non può essere rappresentato
nello spazio di probabilità che riguarda i dadi indistinguibili.
````

````{exercise} •••
:label: ex-spazi-equip-eventi-simmetrici

Sia

```{math}
s : [1..6]^2 \to [1..6]^2, \qquad s(i, j) = (j, i)
```

la funzione che scambia i risultati dei due dadi distinguibili. Dimostrate che
un evento del modello con dadi distinguibili può essere descritto anche nel
modello con dadi indistinguibili se e solo se è invariato rispetto a tale
scambio, cioè se e solo se $s(A) = A$.
````

```{solution} ex-spazi-equip-eventi-simmetrici
:class: dropdown

Indichiamo con

```{math}
\pi(i, j) = \{i, j\}
```

la funzione che dimentica l’ordine dei due risultati.

Supponiamo anzitutto che un evento $A \subseteq [1..6]^2$ del modello con dadi
distinguibili possa essere descritto anche nel modello indistinguibile. Allora
esiste un evento $B$ formato da coppie non ordinate tale che
$A = \pi^{-1}(B)$. Se $(i, j) \in A$, allora $\{i, j\} \in B$, ma anche
$\{j, i\} = \{i, j\} \in B$, quindi $(j, i) \in A$. Questo mostra che
$s(A) = A$.

Viceversa, supponiamo che $A$ sia invariato per scambio, cioè che da
$(i, j) \in A$ segua sempre $(j, i) \in A$. Definiamo allora

```{math}
B = \{ \{i, j\} \mid (i, j) \in A \} 
\enspace.
```

Per costruzione, $A$ coincide con l’insieme di tutte le coppie ordinate che,
una volta dimenticato l’ordine, producono un esito di $B$. In altre parole,
$A = \pi^{-1}(B)$, quindi $A$ può essere rappresentato anche nel modello con
dadi indistinguibili.

La condizione $s(A) = A$ significa, in termini intuitivi, che l’evento dipende
solo dai due valori osservati, non da quale dei due dadi li abbia mostrati.
```

````{exercise} •
:label: ex-spazi-equip-dadi-indistinguibili-conta

Motivate il fatto che il numero di esiti in $\Omega$ per l’esperimento casuale
che consiste nel lanciare due dadi indistinguibili è uguale a $21$, e
spiegate perché lo spazio così ottenuto non è equiprobabile.
````

```{solution} ex-spazi-equip-dadi-indistinguibili-conta
:class: dropdown

Gli esiti possibili sono le coppie non ordinate $\{i, j\}$ con
$1 \leq i \leq j \leq 6$.

- Se i due dadi mostrano lo stesso numero, otteniamo i $6$ esiti
  $\{1, 1\}, \dots, \{6, 6\}$.
- Se invece mostrano numeri diversi, basta scegliere quali sono i due numeri,
  senza preoccuparsi dell’ordine: gli esiti di questo tipo sono quindi
  $\binom{6}{2} = 15$.

In totale si ottiene

```{math}
6 + 15 = 21 
\enspace.
```

Lo spazio non è equiprobabile perché gli esiti non hanno tutti lo stesso peso.
Se $i < j$, l’esito $\{i, j\}$ corrisponde infatti a due esiti ordinati del
modello con dadi distinguibili, cioè $(i, j)$ e $(j, i)$, e ha quindi
probabilità $2/36$. Invece ciascun esito del tipo $\{i, i\}$ corrisponde a un
solo esito ordinato e ha probabilità $1/36$. Poiché queste probabilità sono
diverse, lo spazio non è equiprobabile.
```