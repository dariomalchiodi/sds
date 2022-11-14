---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# La distribuzione uniforme continua

Dato $n \in \mathbb N$, consideriamo l'insieme $D_n = \{ \frac{i}{n}, i = 0,
\dots, n \}$ e la variabile aleatoria $X_n$ definita dalla funzione di massa
di probabilità

```{math}
:label: eq:uniform
p_{X_n}(x; n) = \frac{1}{n+1} \mathrm I_{D_n}(x).
```

Chiaramente, la distribuzione di $X_n$ ricorda il modello uniforme discreto,
con la sola differenza che in questo caso il dominio include la specificazione
$0$. Supponiamo ora che $n$ assuma un valore molto grande: dato un generico
$k \in D_n$, si ha $\mathbb P(X_n = k) = \frac{1}{n + 1}$ e dunque diventa
molto vicina a zero la probabilità che $X_n$ assuma una qualsiasi delle sue
specificazioni. Ciò non deve sembrare strano, perché queste ultime si
addensano in $[0, 1]$ man mano che $n$ cresce, pertanto specificazioni molto
vicine tra loro diventeranno praticamente indistinguibili.

```{margin}
Il multiverso è stato inizialmente introdotto per risolvere in modo ingegnoso
una serie di problemi di coerenza tra varie personificazioni di uno stesso
supereroe: per esempio Terra-Uno è popolata dai protagonisti dei fumetti DC
degli anni '60 (la cosiddetta «Silver age»), mentre quelli introdotti
precedentemente (nella «Golden age») vivono su Terra-Due.
```
````{prf:example} Il multiverso DC
:label: ex-multiverso-dc

A partire dal 1961, e in particolare nel numero 123 di «The Flash», le storie
dei fumetti pubblicati da DC non avvengono in un unico universo, bensì in più
universi che esistono in uno spazio comune, ma i cui abitanti "vibrano" a
frequenze diverse. Ogni universo è identificato in modo univoco da un nome,
che nella maggior parte dei casi indica come viene denominato il pianeta
Terra, e l'insieme di tutti gli universi è chiamato multiverso
[^meccanica-quantistica]. Ogni protagonista può avere caratteristiche
molto diverse a seconda del corrispondente universo: per esempio, Wonder Woman
è buona quasi sempre, ma sicuramente non su Terra-Ventidue. Ora, ipotizziamo
che in ognuno di questi universi esistano esattamente $n = 15000$ protagonisti
diversi, oguno con il proprio allineamento (buono, neutrale o cattivo).
Immaginiamo anche che esista un criterio per scegliere a caso un universo
all'interno del multiverso. La variabile aleatoria $X_n$ che indica la
frazione di protagonisti "buoni" nell'universo selezionato è distribuita sul
dominio $D_{15000}$ secondo la funzione di massa di probabilità
{eq}`eq:uniform`. Ora, ha poco senso discriminare, per dire, tra le
specificazioni $\frac{42}{15000}$, $\frac{43}{15000}$ e $\frac{49}{15000}$,
perché la loro differenza massima equivale a meno dello $0.05\%$ del totale.
````

In altre parole, valori tra loro abbastanza vicini per le specificazioni
risultano fondamentalmente equivalenti, e dunque ha più senso ragionare in
termini della probabilità che $X_n$ assuma valori in un intervallo (anche
piccolo) di specificazioni piuttosto che studiare eventi in cui essa risulta
uguale a una fissata specificazione. Calcoliamo dunque la funzione di
distribuzione cumulativa di $X_n$: fissato $x \in [0, 1]$, esisteranno
$i \in \{ 0, \dots, n \}$ ed $\epsilon < \frac{1}{n}$ tali che
$x = \frac{i}{n} + \epsilon$, e pertanto

```{margin}
Siccome $n x = i + n \epsilon$ e $0 \leq n \epsilon < 1$, abbiamo
$i \leq nx < i + 1$ e dunque $i = \lfloor n x \rfloor$.
```
```{math}
:label: eq:cdf-discrete-uniform
\begin{align}
F_{X_n} (x) &= \mathbb P(X_n \leq x)
            = \mathbb P \Big( X_n \leq \frac{i}{n} \Big) \\
            &= \frac{i+1}{n+1} = \frac{\lfloor n x \rfloor + 1}{n+1},
\end{align}
```

così che in generale

```{math}
F_{X_n}(x) = \frac{\lfloor n x \rfloor + 1}{n+1} \mathrm I_{[0, 1]}(x) +
\mathrm I_{(1, +\infty)}(x).
```

A questo punto possiamo calcolare la probabilità che $X_n$ assuma valori in un
intervallo: fissati $a, b \in [0, 1]$ con
$a \leq b$ esisteranno $i, j \in \{ 0, \dots, n \}$ con $i < j$ ed
$\epsilon_1, \epsilon_2 \in [0, \frac{1}{n})$  tali che
$a = \frac{i}{n} - \epsilon_1$ e $b = \frac{j}{n} + \epsilon_2$. Pertanto

```{margin}
In questo caso abbiamo $n a = i - n \epsilon_1$ e $0 \leq n \epsilon_1 < 1$,
quindi $i -1 \leq na < i$ e $i = \lceil na \rceil$.
```
\begin{align*}
\mathbb P(a \leq X_n \leq b) & =
     \mathbb P \Big( \frac{i}{n} \leq X_n \leq \frac{j}{n} \Big)
     = \sum_{k=i}^j p_{X_n}(k; n) \\
     &= \sum_{k=i}^j \frac{1}{n+1} = \frac{j-i+1}{n+1}
     = \frac{\lfloor nb \rfloor - \lceil na \rceil + 1}{n+1}.
\end{align*}

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

import math
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('sds.mplstyle')

from myst_nb import glue

def cdf(x, n):
    return np.clip((np.floor(n * x) + 1) / (n + 1), 0, 1)

def cdf_graph(n, ax):
    x = np.linspace(-0.1, 1.1, 100)
    y = cdf(x, n)
    ax.step(x, y)
    ax.plot(x, np.clip(x, 0, 1), dashes=[2,], linewidth=1.2, color='#1f77b4')
    ax.set_title(rf'$n = {n}$')

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

for i in range(1, 4):
    cdf_graph(10 * i, ax[i-1])

plt.show()

glue("discrete-to-continuous", fig, display=True)
```

```{glue:figure} discrete-to-continuous
:name: fig:discrete-to-continuous

Le spezzate piene mostrano i grafici della funzione di distribuzione
cumulativa di $X_n$ per $n$ rispettivamente uguale a $10$, $20$ e $30$
(da sinistra verso destra); la spezzata tratteggiata evidenzia il grafico
di $F_X$.
```

```{margin}
In altre parole, $F_{X_n}$ è una _successione di funzioni_ della quale
consideriamo il limite in senso _puntuale_, mostrando che per ogni
$x \in \mathbb R$ si ha $\lim_{n \to +\infty} F_{X_n}(x) = F(x)$
[^convergenza-uniforme].
```
Che cosa succede a $F_{X_n}$ se il valore di $n$ aumenta progressivamente?
Consideriamo la funzione $F: \mathbb R \to [0, 1]$ definita da

```{math}
F(x) = \begin{cases}
    0 & \text{se $x \leq 0$,} \\
    x & \text{se $0 < x \leq 1$,} \\
    1 & \text{se $x \geq 1$.}
\end{cases}
```

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

fig = plt.figure(figsize=(5, 1))

plt.plot([2, 4], [0, 0], 'k')

plt.xticks([])
plt.yticks([])

s  = -1
spacing = {-1: -.4, 1: .2}
for x, l in zip([2, np.pi - 1, np.floor(np.pi), np.pi, 4],
                ['2', r'$\pi - 1$', r'$\lfloor \pi \rfloor$', r'$\pi$', '4']):
    plt.plot([x] * 2, [-.1, .1], 'k')
    plt.text(x, spacing[s], l, ha='center', fontsize=18)
    s *= -1

plt.ylim([-.5, .5])
plt.show()


glue("floor-proof", fig, display=True)
```

```{glue:figure} floor-proof
---
name: fig:floor-proof
figclass: margin
---
Si ricava $x - 1 \leq \lfloor x \rfloor \leq x$ considerando banalmente
il fatto che un qualsiasi numero reale è necessariamente maggiore o uguale
del suo troncamento all'intero inferiore, 
```


La {numref}`fig:discrete-to-continuous`, che mostra i grafici di $F_{X_{10}}$,
$F_{X_{20}}$ e $F_{X_{30}}$ affiancandoli a quello di $F$, suggerisce
l'intuizione che $F_{X_n}$ tenda a $F$ quando $n \to +\infty$. Non è
difficile provare formalmente che questa intuizione è corretta: ricordando che
per ogni $x$ vale $x - 1 \leq \lfloor x \rfloor \leq x$,
da {eq}`eq:cdf-discrete-uniform` si verifica che

```{math}
:label: eq:cdf-continuous-uniform
\frac{n x}{n + 1} \leq F_{X_n}(x) \leq \frac{nx + 1}{n + 1},
```

```{margin}
Il teorema dei due Carabinieri, o teorema del confronto, dice che, date tre
successioni $\left\{ l_n \right\}$, $\left\{ a_n \right\}$ e
$\left\{ r_n \right\}$, se $\lim_{n \to +\infty} l_n =
\lim_{n \to +\infty} r_n = \ell$ allora $\ell$ è anche il limite di
$\left\{ a_n \right\}$.
```
e applicando il teorema dei due Carabinieri si ottiene
$F_{X_n}(x) \to x = F(x)$ per ogni $x \in [0, 1]$. Estendere questo
risultato a ogni $x \in \mathbb R$ è banale [^convergenza-xn].

Notiamo che $F$ soddisfa tutti i criteri indicati nel
{prf:ref}`teo:proprieta-F`, dunque essa deve essere la funzione di
distribuzione cumulativa di una qualche variabile aleatoria $X$. Questa
variabile aleatoria è però completamente diversa da quelle che abbiamo
finora considerato: il grafico di $F$ non evidenzia discontinuità alle quali
far corrispondere i punti di massa della distribuzione perché questa funzione
è continua. D'altronde da {eq}`eq:uniform` si vede facilmente che
$\lim_{n \to + \infty} p_{X_n}(x; n) = 0$ per ogni $x \in \mathbb R$, e
quindi qunado $n$ tende a infinto non ci sono più punti di massa di
probabilità.

Quando questo succede, si dice che la variabile aleatoria
corrispondente ha una distribuzione _continua_, o più brevemente che è
_continua_. In particolare, $X$ ha una distribuzione _uniforme continua_
sull'intervallo $[0, 1]$. Prima di addentrarci in una descrizione formale
per le variabili aleatorie continue (cosa che faremo nel
{numref}`sec:modelli-continui`), vale la pena soffermarci su alcune importanti
differenze tra queste e le variabili aleatorie discrete. Innanzitutto, il
fatto che non abbia più senso parlare di punti di massa richiede sia di
definire in modo diverso il dominio delle variabili aleatorie continue, sia
di rimpiazzare la funzione di massa di probabilità con un altro strumento
che permetta di calcolare le probabilità di eventi che coinvolgono queste
variabili aleatorie. Vale però la pena di osservare prima un'altra cosa
interessante: facendo un ragionamento analogo a quello che ci ha
portato a mostrare la convergenza di $F_{X_n}$ a $F$ possiamo facilmente
dimostrare che

```{math}
\mathbb P(a \leq X_n \leq b) \to b - a
        = F(b) - F(a) = \mathbb P(a \leq X \leq b),
```

e questa formula è apparentemente incoerente rispetto a
{eq}`eq:cdf-e-intervalli` perché quest'ultima fa riferimento a un intervallo
semiaperto di specifcazioni. In realtà, si può verificare in modo
relativamente facile che se avessimo posto $D_n = \{1, \dots, n \}$ e definito
la funzione di massa di probabilità di $X_n$ come
$p_{X_n}(x; n) = \frac{1}{n} \mathrm I_{D_n}(x)$, escludendo in altre parole
il punto di massa $0$ dal dominio, avremmo comunque ottenuto $F$ come limite
delle corrispondenti funzioni di ripartizione quando $n \to +\infty$. Il
risultato sarebbe stato lo stesso se avessimo deciso di escludere il punto
di massa $1$ al posto di $0$, o di escluderli entrambi. Pertanto non ci sono
differenze nelle distribuzioni uniformi continue costruite sugli insiemi
$[0, 1]$, $[0, 1)$, $(0, 1]$ o $(0, 1)$.

Tenuto conto di quanto appena ricavato, possiamo momentaneamente identificare
il dominio di una variabile aleatoria continua $X$ con il sottoinsieme
$D_X \subseteq \mathbb R$ sul quale la funzione di ripartizione $F_X$ non è
costante, includendo la frontiera in questo sottoinsieme.




 

```{margin}
In alcuni testi si preferisce utilizzare la notazione $f_X$ per indicare
sia la funzione di massa di probabilità, sia la funzione di densità. Io ho
preferito usare rispettivamente $p_X$ e $f_X$ per rimarcare ulteriormente
la differenza tra i due concetti coinvolti.
```
In altre parole, calcolare la probabilità che $X$ assumere una fissata
specificazione non porta alcuna informazione, coerentemente con quanto messo
in evidenza all'inizio di questo paragrafo. Questo ci dice anche che non ha
più senso ragionare in termini della funzione di massa di probabilità.
Per una variabile aleatorie continua $X$ questo strumento è sostituito
da un'altra funzione, detta di _densità di probabilità_ e indicata con
$f_X$, il cui valore $f_X(x)$ esprime intuitivamente "quanta" massa di
probabilità è concentrata attorno alla specificazione $x$. In analogia con
il concetto fisico di densità, 















[^meccanica-quantistica]: Per quanto bizzarro possa sembrare il concetto di
multiverso, è interessante notare che una delle interpretazioni proposte per
la meccanica quantistica (la teoria—oggi ampiamente accettata—che descrive
il comportamento della materia nella scala sub-atomica) preveda l'esistenza
di mondi paralleli. Semplificando parecchio, in un dato istante di tempo
ognuna delle cosiddette "particelle elementari" (protoni, elettroni o entità
ancora più piccole) non ha una posizione fissa, bensì si trova simultaneamente
in più punti dello spazio. Solo quando viene effettuato un esperimento per
osservare una di queste particelle (il verbo va inteso in senso lato, perché
stiamo parlando di cose non visibili a occhio nudo) questa assume una
posizione precisa. Tra l'altro, sono proprio le leggi della probabilità a
descrivere la posizione della particella rilevata dell'esperimento in
questione. Tra le interpretazioni proposte per la meccanica quantistica,
quella cosiddetta "a molti mondi" prevede che ogni volta che viene effettuato
un esperimento di questo tipo si ottiene come conseguenza la creazione di
tanti mondi distinti, uno per ogni risultato possibile.

[^convergenza-uniforme]: Si dimostra facilmente che il limite vale anche in
un senso più restrittivo, relativo alla convergenza _uniforme_:
 per ogni $\epsilon > 0$ esiste $n_0 \in \mathbb N$
tale che per ogni $n > n_0$ e per ogni $x \in \mathbb R$ si ha
$| F_{X_n}(x) - F(x) | \leq \epsilon$. Infatti, il grafico di $F_{X_n}(x)$
supera sempre quello di $F(x)$ e quindi $| F_{X_n}(x) - F(x) | =
F_{X_n}(x) - F(x) = \frac{\lfloor n x \rfloor + 1}{n} - x
\leq \frac{n x + 1}{n} - n = \frac{1}{n}$, dunque
$| F_{X_n}(x) - F(x) | \leq \epsilon$ per ogni $n > \frac{1}{\epsilon}$.

[^convergenza-xn]: Notate come il ragionamento che abbiamo effettuato
dimostri la convergenza della sequenza delle funzioni di distribuzione
cumulativa delle varie $X_n$, e non delle variabili aleatorie stesse.
In altre parole, allo scopo di aprire la porta sul mondo delle variabili
aleatorie continue, abbiamo dimostrato che la _distribuzione_ corrispondente
a un particolare modello uniforme discreto su $D_n$ converge al crescere di
$n$ a una distribuzione che fa riferimento a un nuovo tipo di modello, detto
_uniforme continuo_. Non abbiamo invece dimostrato che la successione delle
$X_n$ converge a una variabile aleatoria $X$ la cui distribuzione è un caso
particolare del modello uniforme continuo. Lo studio della convergenza di
successioni di variabili aleatorie richiede di studiare la teoria della
probabilità in modo più approfondito rispetto a quanto descritto in questo
libro. Ma se volete uno _spoiler_, il limite di una successione di variabili
aleatorie può essere definito in più modi, e in nessuno di questi si ha una
convergenza delle $X_n$ alla distribuzione uniforme continua su $[0, 1]$. 
