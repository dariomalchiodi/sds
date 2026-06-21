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

(sec_va-discrete)=
# Variabili aleatorie discrete

```{margin}
Ho anche brevemente parlato delle variabili di tipo _misto_, che vedremo nel
{ref}`sec-va-continue`.
```
All'inizio del capitolo e nel {ref}`sec-concetti-fondamentali-VA` ho anticipato
che le variabili aleatorie che considereremo possono essere di tipo _discreto_
e _continuo_, ma l'unica differenza finora emersa tra queste due categorie
riguarda la forma assunta dalle loro funzioni di ripartizione: costante a
tratti per le variabili discrete, continua per quelle continue. In questo
paragrafo, mi concentro sulle variabili di tipo discreto e sulle loro
specificità.

````{prf:definition} Variabile aleatoria discreta
:label: def-va-discreta

Una variabile aleatoria $X$ si dice _discreta_ se l'insieme $S_X$ dei valori
che essa può assumere, detto _supporto_, è finito oppure infinito numerabile.
````

Chiaramente, il supporto di una variabile aleatoria discreta è un insieme
discreto. I suoi elementi vengono spesso chiamati _punti di massa_, o più
breventente _valori_ o _atomi_ della varriabile aleatoria. Una caratteristica
delle distribuzioni associate alle variabili discrete è quella di poter
essere completamente definite da una particolare funzione, che associa a ogni
punto di massa la probabilità corrispondente.

```{margin}
Quando la variabile aleatoria a cui ci si riferisce è chiara dal contesto,
ometterò il pedice e scriverò semplicemente $p(x)$.
```
````{prf:definition} Funzione di massa di probabilità
:label: def-massa-di-probabilita
La _funzione di massa di probabilità_ di una variabile aleatoria $X$ è la
funzione $p_X \colon \mathbb R \to [0, 1]$ definita da

```{math}
p_X(x) = \mathbb P(X = x) \enspace.
```
````

È importante sottolineare che la funzione di massa di probabilità ha come
dominio l'intera retta reale: assume valori positivi solo nei punti di massa
della distribuzione, mentre per ogni $x \notin S_X$ vale $p_X(x) = 0$. Per
questo motivo il suo grafico viene spesso tracciato in modo analogo a quanto
visto nel Paragrafo {ref}`sec-frequenze-visualizzazione` per le frequenze di un
attributo discreto, cioè mediante un grafico a bastoncini: in corrispondenza di
ciascun punto di massa si disegna un segmento verticale di altezza pari alla
probabilità assegnata, mentre altrove il grafico resta sull'asse delle ascisse.


````{prf:example}
:label: ex-va-discreta-scoiattoli

La variabile $X$ dell'{prf:ref}`ex-va-scoiattoli` è chiaramente di tipo
discreto: il suo supporto è infatti $S_X = [-5 .. 5]$, e tutti gli interi
compresi tra $-5$ e $5$ sono i punti di massa della variabile. La funzione di
massa di probabilità di $X$ è definita nel modo seguente:

```{math}
:label: eq-pdf-scoiattoli

p_X(x) =
\begin{cases}
\frac{6 - |x|}{36} & \text{se } x \in \{-5, -4, \dots, 5\} \enspace, \\
0 & \text{altrimenti.}
\end{cases}
```

Infatti, fissato un intero $x \in [-5 .. 5]$, le coppie equiprobabili
$(g_1, g_2) \in [1 .. 6]^2$ che soddisfano $g_1 - g_2 = x$ sono esattamente
$6 - |x|$, per cui $\mathbb P(X = x) = \frac{6 - |x|}{36}$.
Il grafico della funzione di massa di probabilità è dunque quello mostrato
nella {numref}`fig-va-discreta-scoiattoli-massa`.

````

```{code-cell} python
:tags: [hide-input]

import matplotlib.pyplot as plt
import numpy as np

mass_point = np.arange(-5, 6)
prob = (6 - np.abs(mass_point)) / 36

fig, ax = plt.subplots()
markerline, stemline, baseline = ax.stem(mass_point, prob)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$p_X$')
ax.set_xticks(mass_point)
ax.set_xlim(-5.5, 5.5)
ax.set_ylim(0, 0.18)
plt.show()
```

````{customfigure}
:name: fig-va-discreta-scoiattoli-massa

Grafico a bastoncini della funzione di massa di probabilità della variabile
$X$ introdotta nell'{prf:ref}`ex-va-scoiattoli`.
````

````{prf:example} I sottosistemi di un'armatura
:label: ex-va-mach-x

{extlink}`Mach-X
<https://marvel.fandom.com/wiki/Abner_Jenkins_(Earth-616)>` indossa
un'armatura il cui funzionamento dipende da due sottosistemi indipendenti, i
propulsori e il puntamento, ciascuno dei quali entra in funzione correttamente
con probabilità $0.7$ e si guasta con probabilità $0.3$. Lo spazio degli esiti
è $\Omega = \{(g, g), (g, f), (f, g), (f, f)\}$, dove $g$ indica un
sottosistema guasto e $f$ uno funzionante. Sfruttando l'indipendenza dei due
sottosistemi (vedi la {prf:ref}`def-indipendenza`), le probabilità degli esiti
si ottengono nel modo seguente:

```{math}
\mathbb P\bigl((f, f)\bigr) = 0.7 \times 0.7 = 0.49, \quad
\mathbb P\bigl((f, g)\bigr) = \mathbb P\bigl((g, f)\bigr) = 0.21, \quad
\mathbb P\bigl((g, g)\bigr) = 0.09 \enspace.
```

Consideriamo la variabile aleatoria $X$ che conta il numero di sottosistemi
funzionanti. Si tratta chiaramente di una variabile aleatoria discreta, con
$S_X = \{0, 1, 2\}$, la cui funzione di massa di probabilità è definita da

```{math}
p_X(0) = 0.09, \qquad p_X(1) = 0.42, \qquad p_X(2) = 0.49 \enspace,
```

dove $p_X(1) = 0.21 + 0.21$ tiene conto dei due esiti in cui uno e un solo
sottosistema funziona.
````

````{admonition} Massa di probabilità
:class: tip

```{margin}
Nella letteratura avanzata si incontra anche il termine _atomo_, inteso come
valore della distribuzione che possiede una massa positiva. I termini «punto di
massa» e «atomo» si riferiscono quindi alla stessa idea: una quota non nulla di
probabilità concentrata in un singolo valore.
```
Nel caso di una variabile aleatoria discreta, la probabilità dell'intero spazio
degli esiti sottostante, pari a $1$, può essere immaginata come una _massa_
unitaria distribuita tra i possibili valori della variabile. In altre parole, a
ciascun $x \in S_X$ viene assegnata una quantità di massa pari a
$\mathbb P(X=x)$. Per questo motivo i valori $x$ per i quali $P(X=x)>0$ vengono
chiamati punti di massa e $p_X$ è detta funzione di massa di probabilità: essa
indica quanta massa della probabilità è associata a ciascun valore possibile
della variabile.
L'uso del termine «massa» deriva da un'analogia con la fisica: così come una
massa materiale può essere concentrata in determinati punti, nelle
distribuzioni discrete la probabilità è concentrata nei valori che la variabile
può assumere.
````

Prima di proseguire, risulta utile introdurre uno strumento notazionale che
ricorre spesso quando si lavora con le variabili aleatorie: una funzione che
codifica quando un elemento appartiene a un insieme prefissato all'interno di
un universo di riferimento.

````{prf:definition} Funzione indicatrice
:label: def-indicatrice

Sia $U$ un insieme universo. Fissato un qualsiasi sottoinsieme $A \subseteq U$,
la sua _funzione indicatrice_ è la funzione $\mathbb 1_A \colon U \to \{0, 1\}$
definita nel modo seguente:

```{math}
\mathbb 1_A(x) =
\begin{cases}
1 & \text{se } x \in A, \\
0 & \text{se } x \notin A.
\end{cases}
```
````

Quasi sempre, l'universo di riferimento che utilizzeremo per le funzioni
indicatrici è $\mathbb R$. Ciò consente di scrivere in forma compatta le
funzioni che altrimenti andrebbero definite per casi. Ad esempio,
{eq}`eq-pdf-scoiattoli` si può scrivere come

```{math}
p_X(x) = \frac{6 - |x|}{36} \mathbb 1_{[-5 .. 5]} \enspace.
```
Più in generale, le funzioni indicatrici sono particolarmente utile quando
è necessario annullare le probabilità ovunque al di fuori dei punti di
massa. In alcuni casi, però, risulta utile scrivere delle funzioni indicatrici
basate su uno spazio degli esiti $\Omega$: dato un evento $E$, infatti,
$\mathbb 1_E$ indica una particolare variabile aleatoria discreta, detta
_variabile indicatrice_ di $E$, i cui punti di massa sono $0$ e $1$. Questa
variabile rappresenta un modo naturale di tradurre in termini numerici il
verificarsi o meno di un evento.

````{prf:example}
:label: ex-indic

Riprendendo l'{prf:ref}`ex-va-mach-x`, supponiamo che, ai fini della missione,
ciò che conta non sia il numero preciso di sottosistemi attivi, ma soltanto il
fatto che l'armatura sia in grado di operare, cosa che accade non appena
_almeno uno_ dei due sottosistemi funziona. Si può descrivere questa situazione
con la variabile indicatrice $\mathbb 1_{\{X \geq 1\}}$, che vale $1$ quando
$X \geq 1$ e $0$ altrimenti: si tratta della funzione indicatrice associata
all'evento $X \geq 1$ (che equivale a «l'armatura è operativa»). La
funzione di massa di probabilità di questa variabile aleatoria è definita da

```{math}
\mathbb P(\mathbb 1_{\{X \geq 1\}} = 1) = p_X(1) + p_X(2) = 0.91, \qquad
\mathbb P(\mathbb 1_{\{X \geq 1\}} = 0) = p_X(0) = 0.09 \enspace.
```
````

````{prf:theorem} Proprietà della funzione di massa di probabilità
:label: teo-proprieta-massa

Siano $X$ una variabile aleatoria e $p_X$ la sua funzione di massa di
probabilità. Allora $p_X(x) \geq 0$ per ogni $x \in \mathbb R$ e

```{math}
:label: eq-massa-somma-uno
\sum_{x \in S_X} p_X(x) =  1 \enspace.
```
````
````{sds-proof}
La prima proprietà si dimostra in modo banale: fissato $x \in \mathbb R$, si ha
$p_X(x) = \mathbb P(X = x)$, e le probabilità sono non negative per il primo
assioma di Kolmogorov. Per quanto riguarda la seconda, basta osservare che se
$x_1, x_2 \in S_X$ sono due punti di massa diversi, allora gli eventi
$\{ X = x_1 \}$ e $\{ X = x_2 \}$ sono mutuamente esclusivi perché una
variabile aleatoria non può assumere due valori distinti nello stesso esito.
Per il terzo assioma di Kolmogorov si ha dunque

```{math}
\sum_{x \in S_X} p_X(x) = \sum_{x \in S_X} \mathbb P(X = x) =
\mathbb P(\cup_{x \in S_X} \{ X = x \}).
```

La definizione di supporto implica che l'unione ottenuta nella formula
precedente sia uguale allo spazio degli esiti. Il secondo assioma di Kolmogorov
implica che

```{math}
\sum_{x \in S_X} p_X(x) = \mathbb P(\Omega) = 1 \enspace,
```

dunque la proprietà è dimostrata.
````

````{prf:example} Il teletrasporto imperfetto
:label: ex-va-doorman

{extlink}`Doorman
<https://marvel.fandom.com/wiki/DeMarr_Davis_(Earth-616)>` teletrasporta gli
altri membri dei {extlink}`Great Lakes
Avengers  <https://marvel.fandom.com/wiki/Great_Lakes_Avengers_(Earth-616)>`
all'interno di un edifitcio, ma con una certa imprecisione: non è in grado di
stabilire a priori in quale dei tre piani si materializzerà. Indichiamo con
$X$ la variabile aleatoria che indica il piano di arrivo, e supponiamo di
sapere che

```{math}
\mathbb P(X = 1) = \tfrac{1}{2}, \qquad \mathbb P(X = 2) = \tfrac{1}{3}
\enspace.
```

Il valore $\mathbb P(X = 3)$ si ricava imponendo che {eq}`eq-massa-somma-uno`
sia soddisfatta: da $p_X(1) + p_X(2) + p_X(3) = 1$ si ricava

```{math}
p_X(3) = 1 - p_X(1) - p_X(2) = 1 - \tfrac{1}{2} - \tfrac{1}{3}
       = \tfrac{6 - 3 - 2}{6} = \tfrac{1}{6}
\enspace.
```

La funzione di massa di probabilità di $X$ è dunque quella rappresentata nella
{numref}`fig-va-doorman-massa`.
````

```{code-cell} python
:tags: [hide-input]

import matplotlib as mpl
import matplotlib.pyplot as plt

mass_points = [1, 2, 3]
prob = [1 / 2, 1 / 3, 1 / 6]

fig, ax = plt.subplots()
markerline, stemline, baseline = ax.stem(mass_points, prob)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$p_X$')
ax.set_xticks(mass_points)
ax.set_ylim(0, 0.6)
plt.show()
```
````{customfigure}
:name: fig-va-doorman-massa

Funzione di massa di probabilità del piano di arrivo $X$
nell'{prf:ref}`ex-va-doorman`.
````


La funzione di massa di probabilità definisce in modo completo la
distribuzione di una variabile aleatoria discreta. Infatti, qualunque evento
della forma $\{X \in A\}$ si può scomporre nell'unione di un numero finito o
numerabile di insiemi singoletto, quindi $\mathbb P_X(A)$ si può sempre
esprimere come la somma di valori di $p_X$.

````{prf:theorem}
:label: thm-eventi-singoletto

Sia $X$ una variabile aleatoria discreta con supporto $S_X$, e sia
$A \subseteq \mathbb R$. Allora

```{math}
\mathbb P(X \in A) = \sum_{x \in A \cap S_X} p_X(x) \enspace.
```
````

````{sds-proof}
Possiamo assumere $A = \{ x_1, x_2, \dots \}$, perché, essendo $X$ discreta,
$A$ deve essere composto da una quantità finita o numerabile di elementi.
Pertanto $\{ X \in A \}$ è uguale all'evento $\bigcup_{x \in A} \{X = x\}$.
Come già visto nella dimostrazione del {prf:ref}`teo-proprieta-massa`, gli
eventi della forma $\{X = x\}$, al variare di $X \in A$, sono mutuamente
esclusivi. Applicando allora il terzo assioma di Kolmogorov, si ottiene

```{math}
\mathbb P(X \in A) =
\mathbb P\left(\bigcup_{x \in A} \{X = x\}\right) =
\sum_{x \in A} \mathbb P(X = x) = \sum_{x \in A} p_X(x) \enspace.
```
````

````{prf:example} Un teletrasporto a un piano dispari
:label: ex-va-doorman-singoletto

Considerando ancora una volta la variabile $X$ dell'{prf:ref}`ex-va-doorman`,
focalizziamoci sull'evento in cui la destinazione del teletrasporto corrisponde
a un piano dispari dell'edificio, che possiamo descrivere come
$X \in \{1, 3\}$. Applicando il {prf:ref}`thm-eventi-singoletto` si ottiene

```{math}
\mathbb P(X \in \{1, 3\}) = p_X(1) + p_X(3) =
   \tfrac{1}{2} + \tfrac{1}{6} = \tfrac{2}{3} \enspace.
```
````
Il risultato precedente permette di mettere in relazione in modo preciso la
funzione di massa di probabilità e la funzione di ripartizione. Per una
variabile aleatoria discreta, queste due descrizioni sono equivalenti: ciascuna
determina completamente l'altra.

````{prf:theorem}
:label: teo-equiv-f-F

Sia $X$ una variabile aleatoria discreta, con funzione di massa di probabilità
$p_X$ e funzione di ripartizione $F_X$. Allora, per ogni $x \in \mathbb R$,

```{math}
:label: eq-ripartizione-da-massa

F_X(x) = \mathbb P(X \leq x) = \sum_{a \leq x} p_X(a)
```

e

```{math}
:label: eq-massa-da-ripartizione

p_X(x) = F_X(x) - \lim_{t \to x^-} F_X(t) \enspace.
```
````

````{sds-proof}
La prima formula si ottiene applicando il {prf:ref}`thm-eventi-singoletto`
all'insieme $A = (-\infty, x]$. Per dimostrare la seconda, basta notare che
$\{ X \leq x \} = \{ X < x \} \cup \{ X = x \}$, e i due eventi alla destra
di quest'uguaglianza sono disgiunti. Quindi

```{math}
\mathbb P(X = x) = \mathbb P(X \leq x) - \mathbb P(X < x)
= F_X(x) - \mathbb P(X < x) \enspace.
```

D'altra parte, $\lim_{t \to x^-} F_X(t) = \mathbb P(X < x)$, ricordando la
tipica forma delle funzioni di ripartizione per le variabili discrete.
Sostituendo questa identità nella formula precedente, si ottiene la tesi.
Questo dimostra formalmente un fatto già accennato nel capitolo precedente:
$p_X(x)$ coincide con l'ampiezza del salto di $F_X$ nel punto $x$.
````

````{prf:example} La ripartizione del teletrasporto
:label: ex-va-doorman-ripartizione

Il teorema precedente permette di ricavare la funzione di ripartizione della
variabile $X$ dell'{prf:ref}`ex-va-doorman`. Esaminando uno alla volta i casi
coinvolti, si verifica che:

- nessun $x < 1$ è un punto di massa di $X$, quindi $F_X(x) = 0$ per tali
  valori;
- l'unico punto di massa $x$ tale che $1 \leq x < 2$ è $1$, quindi
  $F_X(x) = p_X(1) = \tfrac{1}{2}$;
- per $2 \leq x < 3$, l'evento $X \leq x$ si verifica in corrispondenza dei
  punti di massa $1$ e $2$, quindi
  $F_X(x) = p_X(1) + p_X(2) = \tfrac{1}{2} + \tfrac{1}{3} = \tfrac{5}{6}$;
- quando $x \geq 3$, qualsiasi punto di massa di $X$ verifica $X \leq x$, che
  diventa l'evento certo, e infatti $F_X(x) = p_X(1) + p_X(2) + p_X(3) = 1$.

Riassumendo, la funzione di ripartizione $F_X$ è la seguente:

```{math}
F_X(x) =
\begin{cases}
0 & \text{se } x < 1, \\[2pt]
\tfrac{1}{2} & \text{se } 1 \leq x < 2, \\[2pt]
\tfrac{5}{6} & \text{se } 2 \leq x < 3, \\[2pt]
1 & \text{se } x \geq 3.
\end{cases}
```

Il suo grafico, riportato nella {numref}`fig-va-doorman-ripartizione`, mostra
la struttura a scalini della ripartizione che già conosciamo: in ogni salto il
valore della funzione è quello del gradino superiore, in accordo con la
continuità da destra enunciata nella {prf:ref}`thm-proprieta-ripartizione`;
inoltre, l'altezza di ciascun salto è esattamente la massa $p_X(x)$ del valore
$x$ che individua il salto stesso.
````

```{code-cell} python
:tags: [hide-input]

from fractions import Fraction
import matplotlib.pyplot as plt
import scipy.stats as st

v = np.arange(1, 4)
p = np.array([1/2, 1/3, 1/6])

X = st.rv_discrete(values=(v, p))

fig, ax = plt.subplots()

x_plot = np.concatenate(([v[0] - 2], v, [v[-1] + 2]))
y_plot = np.concatenate(([0], X.cdf(v), [1]))
ax.step(x_plot, y_plot, where='post', color='C0')

prev = np.concatenate(([0.0], X.cdf(v)[:-1]))
ax.plot(v, X.cdf(v), 'o', color='C0', zorder=3)

ticks = np.cumsum(p)
labels = [str(Fraction(t).limit_denominator(36)) for t in ticks]
ax.set_yticks(ticks)
ax.set_yticklabels(labels)

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$F_X$')
plt.show()
```
````{customfigure}
:name: fig-va-doorman-ripartizione

Funzione di ripartizione $F_X$ della variabile aleatoria che descrive il piano
di arrivo nell'{prf:ref}`ex-va-doorman`. 
````

Il teorema precedente mostra che la funzione di massa di probabilità determina
la funzione di ripartizione. Vale anche il viceversa: per descrivere la legge
di una variabile aleatoria discreta è sufficiente assegnare una massa non
negativa ai punti del supporto, purché la massa totale sia uguale a $1$.

````{prf:theorem} Caratterizzazione delle funzioni di massa di probabilità
:label: thm-caratterizzazione-massa

Una funzione $p \colon \mathbb R \to [0, 1]$ che assume valori non nulli su
un insieme discreto $S$ è la funzione di massa di probabilità di una qualche
variabile aleatoria se e solo se

1. $p(x) \geq 0$ per ogni $x \in \mathbb R$, e
2. $\sum_{x \in S}p(x) = 1$.
````
````{sds-proof} traccia

La necessità segue immediatamente dal {prf:ref}`teo-proprieta-massa`.
Viceversa, supponiamo che $p$ soddisfi le due proprietà enunciate. Procedendo
in modo analogo a quanto fatto per {eq}`eq-massa-da-ripartizione`, possiamo
definire

```{math}
F(x) = \sum_{a \leq x} p(a) \enspace,
```

ottenendo una funzione non decrescente, continua da destra, con limite $0$
per $x \to -\infty$ e limite $1$ per $x \to +\infty$. Per il
{prf:ref}`thm-caratterizzazione-ripartizione`, essa è dunque la funzione di
ripartizione di una qualche variabile aleatoria $X$. L'ampiezza dei salti di
$F$ coincide con i valori di $p$, che è dunque la funzione di massa di
probabilità di $X$.
````

A questo punto disponiamo dei due strumenti fondamentali per descrivere una
variabile aleatoria discreta $X$: la funzione di massa di probabilità $p_X$,
che indica quanta probabilità è concentrata in ciascun valore, e la funzione di
ripartizione $F_X$, che ne accumula i contributi. Queste due descrizioni sono
equivalenti da un punto di vista matematico, nel senso che da ciascuna si
ricava l'altra. Nel seguito userò l'una o l'altra di queste funzioni,
scegliendo ogni volta quella che rende più naturale sviluppare un ragionamento
o risolvere un problema.


## Vero o falso?

Analizzate ciascuna delle seguenti affermazioni, che riguardano una variabile
aleatoria discreta $X$, e dite se è vera o falsa, motivando il vostro
ragionamento. Cliccate su di essa per visualizzare la risposta corretta.

````{tf-item}
Il supporto $S_X$ è necessariamente finito.
+++
**Falsa**. Per la {prf:ref}`def-va-discreta`, il supporto di una variabile
aleatoria discreta può essere finito oppure infinito numerabile.
````

````{tf-item}
Per ogni $x \notin S_X$ vale $p_X(x) = 0$.
+++
**Vera**. Se $x$ non appartiene al supporto, allora $X$ non può assumere il
valore $x$; dunque, per definizione di funzione di massa,
$p_X(x) = \mathbb P(X = x) = 0$.
````

````{tf-item}
$\pi$ non può essere un punto di massa di $X$.
+++
**Falsa**. La discretezza di $X$ non riguarda i suoi singoli punti di massa,
ma il suo supporto: è quindi possibile che $\pi \in S_X$, a patto che
quest'utimo sia un insieme finito o numerabile. Lo stesso vale per qualsiasi
altro numero reale.
````

````{tf-item}
Per ogni insieme $A \subseteq \mathbb R$ si ha $\mathbb P(X \in A) = \sum_{x \in A \cap S_X} p_X(x)$.
+++
**Vera**. È precisamente il contenuto del
{prf:ref}`thm-eventi-singoletto`: per una variabile aleatoria discreta,
qualunque evento della forma $\{ X \in A \}$ si ottiene sommando le masse dei
punti del supporto contenuti in $A$.
````

````{tf-item}
Se $p_X(x_0) > 0$, allora la funzione di ripartizione $F_X$ non è continua nel punto $x_0$.
+++
**Vera**. Dalla formula {eq}`eq-massa-da-ripartizione` segue che $p_X(x_0)$
coincide con l'ampiezza del salto di $F_X$ in $x_0$. Se $p_X(x_0) > 0$, il
salto è non nullo e quindi $F_X$ non può essere continua in quel punto.
````

````{tf-item}
Se due variabili aleatorie discrete hanno la stessa funzione di ripartizione, allora hanno anche la stessa funzione di massa di probabilità.
+++
**Vera**. Per {eq}`eq-massa-da-ripartizione`, la funzione di massa si
ricava univocamente dalla funzione di ripartizione tramite
$p_X(x) = F_X(x) - \lim_{t \to x^-} F_X(t)$. Quindi due variabili con la stessa
funzione di ripartizione hanno necessariamente la stessa funzione di massa di
probabilità.
````

````{tf-item}
La variabile indicatrice $\mathbb 1_E$ di un evento $E$ può assumere anche valori diversi da $0$ e $1$.
+++
**Falsa**. La {prf:ref}`def-indicatrice` specifica che i punti di massa di una
variabile indicatrice sono soltanto $0$ e $1$.
````


## Esercizi

````{exercise} •
:label: ex-va-speedball

{extlink}`Speedball
<https://marvel.fandom.com/wiki/Robert_Baldwin_(Earth-616)>` rimbalza su una
parete un numero aleatorio di volte, compreso tra $1$ e $4$. Sapendo che
$\mathbb P(N = k)$ è proporzionale a $k$, cioè $\mathbb P(N = k) = c\,k$ per
una costante $c$ da determinare,

1. determinate il valore di $c$;
2. calcolate $\mathbb P(N \leq 2)$.
````

````{solution} ex-va-speedball
:class: dropdown

1. La condizione {eq}`eq-massa-somma-uno` impone che la somma delle masse sia
   $1$, quindi
   ```{math}
   1 = c(1 + 2 + 3 + 4) = 10c
   ```
   e $c = \tfrac{1}{10}$.

2. Applicando il {prf:ref}`thm-eventi-singoletto` si ottiene
   ```{math}
   \mathbb P(N \leq 2) = \mathbb P(N = 1) + \mathbb P(N = 2)
   = \tfrac{1}{10} + \tfrac{2}{10} = \tfrac{3}{10} \enspace.
   ```
````

````{exercise} ••
:label: ex-va-armatura-ripartizione

Sia $X$ la variabile aleatoria definita nell'{prf:ref}`ex-va-mach-x`, per cui
valeva $p_X(0) = 0.09$, $p_X(1) = 0.42$ e $p_X(2) = 0.49$.

1. Ricavate la funzione di ripartizione $F_X$.
2. Usando $F_X$, calcolate $\mathbb P(0 < X \leq 2)$.
3. Verificate che $\mathbb P(X \geq 1)$ coincide con la probabilità calcolata
   nell'{prf:ref}`ex-va-mach-x` per l'evento «l'armatura è operativa».
````

````{solution} ex-va-armatura-ripartizione
:class: dropdown

1. Accumulando le masse secondo {eq}`eq-ripartizione-da-massa`, si ha

   ```{math}
   F_X(x) =
   \begin{cases}
      0 & \text{se $x < 0$}, \\ 
      0.09 & \text{se $0 \leq x < 1$}, \\
      0.51 & \text{se $1 \leq x < 2$}, \\  
      1 & \text{se $x \geq 2$}.
   \end{cases}
   ```

2. Per il {prf:ref}`lemma-ripartizione-intervallo`,

```{math}
\mathbb P(0 < X \leq 2) = F_X(2) - F_X(0) = 1 - 0.09 = 0.91 \enspace.
```

3. L'evento $\{X \geq 1\}$ è il complementare di $\{X = 0\}$, quindi
   $\mathbb P(X \geq 1) = 1 - p_X(0) = 1 - 0.09 = 0.91$, esattamente la
   probabilità che l'armatura sia operativa.
````

````{exercise} ••
:label: ex-va-sensori

Un'armatura monta tre sensori indipendenti, ciascuno dei quali funziona
correttamente con probabilità $p$, indipendentemente dal comportamento dei
rimamenti sensori. Sia $X$ la variabile aleatoria che conta il numero di
sensori funzionanti.

1. Determinate la funzione di massa di probabilità di $X$ in funzione di $p$.
2. Esprimete $\mathbb P(X \geq 1)$ in funzione di $p$.
3. Valutate $\mathbb P(X \geq 1)$ nel caso $p = 0.8$.
````
````{solution} ex-va-sensori
:class: dropdown

1. Ciascuna configurazione che corrisponde a un valore fissato di $k$ ha
   esattamente $k$ sensori funzionanti e $3 - k$ sensori difettosi. Il
   comportamento indipendente dei sensori ci permette di dire che la
   probabilità di una siffatta configurazione è $p^k (1 - p)^{3 - k}$, ed
   esistono $c_{3, k} = \binom{3}{k}$ configurazioni possibili (corrispondenti
   al numero di modi nei quali si possono scegliere i $k$ sensori funzionanti
   a partire dai tre disponibili). Dunque, per ogni $k = 0, 1, 2, 3$,

   ```{math}
   p_X(k) = \binom{3}{k} p^k (1 - p)^{3 - k} \enspace.
   ```

2. L'evento $\{X \geq 1\}$ è il complementare di $\{X = 0\}$, che si verifica
   solo quando tutti e tre i sensori si guastano, quindi

   ```{math}
   \mathbb P(X \geq 1) = 1 - p_X(0) = 1 - (1 - p)^3 \enspace.
   ```

3. Per $p = 0.8$ si ha $(1 - 0.8)^3 = 0.2^3 = 0.008$, dunque
   $\mathbb P(X \geq 1) = 1 - 0.008 = 0.992$.
````

````{exercise} •••
:label: ex-va-thunderbolts-somma

Durante un'operazione, {extlink}`Songbird
<https://marvel.fandom.com/wiki/Melissa_Gold_(Earth-616)>` e
{extlink}`Moonstone
<https://marvel.fandom.com/wiki/Karla_Sofen_(Earth-616)>` neutralizzano in modo
indipendente un certo numero di avversari ciascuna. Assumete che ognuna delle
due neutralizzi $0$, $1$ oppure $2$ avversari, con la stessa probabilità
$\tfrac{1}{3}$ per ciascun valore. Sia $X$ il numero totale di avversari
neutralizzati.

1. Determinate la funzione di massa di probabilità di $X$.
2. Verificate che le masse di probabilità sommano a $1$.
3. Scrivete la funzione di ripartizione $F_X$ e visualizzatene il grafico.
4. Calcolate $\mathbb P(1 < X \leq 3)$.
````

````{solution} ex-va-thunderbolts-somma
:class: dropdown

Indichiamo con $S$ e $M$ il numero di nemici neutralizzati rispettivamente da
Songbird e Moonstone. Per ogni $h, k \in \{ 0, 1, 2 \}$, gli eventi $S = h$ ed
$M = k$ hanno ciascuno probabilità $\tfrac{1}{3}$, e gli eventi che coinvolgono
$S$ sono indipendenti da quelli che coinvolgono $M$.

1. Consideriamo separatamente i valori possibili di $X = S + M$.
   - $X = 0$ si verifica quando entrambe le supereroine non neutralizzano alcun
     avversario, quindi
     ```{math}
     p_X(0) = \mathbb P(\{ S = 0 \} \cap \{ M = 0 \})
            = \mathbb P(\{ S = 0 \}) \mathbb P(\{ M = 0 \})
            = \frac{1}{9} \enspace.
     ```
   - Si procede in modo analogo per $X = 4$: ora sia Songbird che Moonstone
     neutralizzano due avversari e $p_X(4) =
     \mathbb P(\{ S = 2 \}) \mathbb P(\{ M = 2 \}) = \frac{1}{9}$.
   - L'evento $X = 1$ si verifica quando una supereroina neutralizza un
     avversario e l'altra nessuno, e la sua probabilità è
     $\tfrac{1}{9} + \tfrac{1}{9}$, tenuto conto del fatto che ciascun evento
     può verificarsi in due modi diversi: $S = 1$ ed $M = 0$ oppure $S = 0$ ed
     $M = 1$. Riassumendo, $p_X(1) = \tfrac{2}{9}$.
   - Analogamente, $X = 3$ si verifica quando Songbird neutralizza un
     avversario e Moonstone ne neutralizza due, o viceversa; ripetendo il
     medesimo ragionamento del punto precedente si ottiene
     $p_X(3) = \tfrac{2}{9}$.
   - Infine, $X = 2$ nei tre sotto casi $S = 2, M = 0$, $S = M = 1$ ed
     $S = 0, M = 2$; ognuno di essi ha probabilità $\tfrac{1}{9}$, così che
     $p_X(2) = \tfrac{1}{3}$.

2. Sostituendo i valori ottenuti al punto precedente, si ottiene
   $p_X(0) + p_X(1) + p_X(2) + p_X(3) + p_X(4) = \tfrac{1 + 2 + 3 + 2 + 1}{9}
   = 1$.

3. La funzione di ripartizione si ottiene applicando
   {eq}`eq-ripartizione-da-massa`:

   ```{math}
   F_X(x) =
   \begin{cases}
      0            & \text{se $x < 0$}, \\
      \tfrac{1}{9} & \text{se $0 \leq x < 1$}, \\
      \tfrac{3}{9} & \text{se $1 \leq x < 2$}, \\
      \tfrac{6}{9} & \text{se $2 \leq x < 3$}, \\
      \tfrac{8}{9} & \text{se $3 \leq x < 4$}, \\
      1 & \text{se $x \geq 4$}.
   \end{cases}
   ```

4. Applicando il {prf:ref}`lemma-ripartizione-intervallo` si ottiene

   ```{math}
   \mathbb P(1 < X \leq 3) = F_X(3) - F_X(1)
   = \tfrac{8}{9} - \tfrac{3}{9} = \tfrac{5}{9} \enspace.
   ```

   Il grafico di $F_X$ si ottiene nel modo seguente.

```{code-cell} python
v = np.arange(0, 5)
p = np.array([1/9, 2/9, 3/9, 2/9, 1/9])

X = st.rv_discrete(values=(v, p))

fig, ax = plt.subplots()

x_plot = np.concatenate(([v[0] - 1], v, [v[-1] + 1]))
y_plot = np.concatenate(([0], X.cdf(v), [1]))
ax.step(x_plot, y_plot, where='post', color='C0')

prev = np.concatenate(([0.0], X.cdf(v)[:-1]))
ax.plot(v, X.cdf(v), 'o', color='C0', zorder=3)

ticks = np.cumsum(p)
labels = [str(Fraction(t).limit_denominator(36)) for t in ticks]
ax.set_yticks(ticks)
ax.set_yticklabels(labels)

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$F_X$')
plt.show()
```
````

````{exercise} •••
:label: ex-va-salti-ripartizione

Sia $X$ una variabile aleatoria discreta con funzione di ripartizione $F_X$ e
funzione di massa di probabilità $p_X$.

1. Spiegate perché, in un punto $x_0$ in cui $p_X(x_0) > 0$, la funzione $F_X$
   presenta un salto di ampiezza esattamente $p_X(x_0)$.
2. Deducetene che $F_X$ è continua da destra ma, in generale, _non_ è continua
   da sinistra.
3. Argomentate perché, viceversa, nei punti in cui $p_X$ è nulla la funzione
   $F_X$ è continua.
````

````{solution} ex-va-salti-ripartizione
:class: dropdown

1. Per valori $x$ di poco inferiori a $x_0$, la somma in
   {eq}`eq-ripartizione-da-massa` include tutti i valori di $X$ strettamente
   minori di $x_0$, ma non $x_0$ stesso; per $x = x_0$ si aggiunge il termine
   $p_X(x_0)$. La differenza tra il valore «appena dopo» e quello «appena
   prima» di $x_0$ è quindi proprio $p_X(x_0)$, che è l'ampiezza del salto.

2. Nel punto $x_0$ il valore di $F_X$ coincide con quello del gradino
   superiore, perché la somma include il termine $p_X(x_0)$: questo è il senso
   della continuità da destra. Il limite da sinistra, invece, vale
   $F_X(x_0) - p_X(x_0)$, che è strettamente minore di $F_X(x_0)$ ogni volta
   che $p_X(x_0) > 0$; in tali punti $F_X$ non è continua da sinistra.

3. Se $p_X(x_0) = 0$, allora l'attraversamento di $x_0$ non aggiunge alcun
   contributo alla somma in&nbsp;{eq}`eq-ripartizione-da-massa`: i limiti da destra
   e da sinistra coincidono entrambi con $F_X(x_0)$, e dunque la funzione è
   continua in $x_0$.
````


## Concetti fondamentali

Pensate ai concetti fondamentali illustrati in questo paragrafo ed elencateli.
Nella lista qui sotto sono già presenti gli stessi concetti, ma nascosti.
Cliccate sul pulsante per mostrarli sotto forma di parole chiave, quindi
confrontateli con la vostra lista. Provate infine a descrivere ciascun concetto
con parole vostre.

````{sds-wordcloud}
Variabile aleatoria discreta
Supporto
Punto di massa
Funzione di massa di probabilità
Massa di probabilità
Funzione indicatrice
Variabile indicatrice
````

