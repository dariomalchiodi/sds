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

# Il modello uniforme continuo

Dato $n \in \mathbb N$, consideriamo l'insieme $D_n = \{ \frac{i}{n}, i = 0,
\dots, n \}$ e la variabile aleatoria $X$ definita dalla funzione di massa di
probabilità

```{math}
:label: eq:uniform
p_X(x) = \frac{1}{n+1} \mathrm I_{D_n}(x).
```

Chiaramente, la distribuzione di $X$ ricorda il modello uniforme discreto, con
la sola differenza che in questo caso il dominio include la specificazione
$0$. Supponiamo ora che $n$ assuma un valore molto grande: dato un generico
$k \in D_n$, si ha $\mathbb P(X = k) = \frac{1}{n + 1}$ e dunque diventa molto
vicina a zero la probabilità che $X$ assuma una qualsiasi delle sue
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
Terra, e l'insieme di tutti gli universi è chiamato metaverso
[^meccanica-quantistica]. Ogni protagonista può avere caratteristiche
molto diverse a seconda del corrispondente universo: per esempio, Wonder Woman
è buona quasi sempre, ma sicuramente non su Terra-Ventidue. Ora, ipotizziamo
che in ognuno di questi universi esistano esattamente $n = 15000$ protagonisti
diversi, oguno con il proprio allineamento (buono, neutrale o cattivo).
Immaginiamo anche che esista un criterio per scegliere a caso un universo
all'interno del metaverso. La variabile aleatoria $X$ che indica la frazione
di protagonisti "buoni" nell'universo selezionato è distribuita sul dominio
$D_{15000}$ secondo la funzione di massa di probabilità {eq}`eq:uniform`.
Ora, ha poco senso discriminare, per dire, tra le specificazioni
$\frac{42}{15000}$. $\frac{43}{15000}$ e $\frac{49}{15000}$, perché la loro
differenza massima equivale a meno dello $0.05\%$ del totale.
````

In altre parole, valori tra loro abbastanza vicini per le specificazioni
risultano fondamentalmente equivalenti, e dunque ha più senso ragionare in
termini della probabilità che $X$ assuma valori in un intervallo (anche
piccolo) di specificazioni piuttosto che studiare eventi in cui essa risulta
uguale a una fissata specificazione. Calcoliamo dunque la funzione di
distribuzione cumulativa di $X$: fissato $x \in [0, 1]$, esisteranno
$i \in \{ 0, \dots, n \}$ ed $\epsilon < \frac{1}{n}$ tali che
$x = \frac{i}{n} + \epsilon$, e pertanto

```{margin}
Siccome $n x = i + n \epsilon$ e $0 \leq n \epsilon < 1$, abbiamo
$i = \lfloor nb \rfloor$.
```
```{math}
F_X (x) = \mathbb P(X \leq x) = \mathbb P \Big( X \leq \frac{i}{n} \Big)
        = \frac{i+1}{n} = \frac{\lfloor n x \rfloor + 1}{n},
     
```

così che in generale

```{math}
F_X(x) = \frac{\lfloor n x \rfloor + 1}{n} \mathrm I_{[0, 1]}(x) +
\mathrm I_{(1, +\infty)}(x).
```

A questo punto possiamo calcolare la probabilità che $X$ assuma valori in un
intervallo: fissati $a, b \in [0, 1]$ con
$a < b$ esisteranno $i, j \in \{ 0, \dots, n \}$ con $i < j$ ed
$\epsilon_1, \epsilon_2 \in [0, \frac{1}{n})$  tali che
$a = \frac{i}{n} - \epsilon_1$ e $b = \frac{j}{n} + \epsilon_2$. Pertanto

```{margin}
In questo caso abbiamo $n a = i - n \epsilon_1$ e $0 \leq n \epsilon_1 < 1$,
quindi $i = \lceil na \rceil$.
```
\begin{align*}
\mathbb P(a \leq X \leq b) & =
     \mathbb P \Big( \frac{i}{n} \leq X \leq \frac{j}{n} \Big) =
     \mathbb P \Big( \frac{i-1}{n} < X \leq \frac{j}{n} \Big) \\
     & = F_X \Big( \frac{j}{n} \Big) - F_X \Big( \frac{i-1}{n} \Big) =
     \frac{j+1}{n} - \frac{i}{n} \\
     & = \frac{\lfloor nb \rfloor - \lceil na \rceil + 1}{n}.
\end{align*}

Che cosa succederebbe se il dominio di $X$ diventasse infinito? Consideriamo
per esempio l'intero intervallo $[0, 1]$. Da {eq}`eq:uniform` sappiamo che
non ha più senso calcolare la probabilità di assumere una qualsiasi
specificazione, perché $\mathbb P(X = x) = 0$ per ogni $x \in \mathbb R$.


```{code-cell} ipython3
:tags: [hide-cell, remove-output]

import math
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('sds.mplstyle')

from myst_nb import glue

def cdf(x, n):
    return (np.floor(n * x) + 1) / n

def cdf_graph(n, ax):
    x = np.linspace(0, 1, 100)
    y = cdf(x, n)
    ax.step(x, y)
    ax.plot(x, x, dashes=[2,], linewidth=1.2, color='#1f77b4')
    ax.set_title(rf'$n = {n}$')

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

for i in range(1, 4):
    cdf_graph(10 * i, ax[i-1])

plt.show()

glue("discrete-to-continuous", fig, display=True)
```

```{glue:figure} discrete-to-continuous
:name: fig:discrete-to-continuous

Bla bla
```






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
descrivere l'esito dell'esperimento in questione. Tra le interpretazioni
proposte per la meccanica quantistica, quella cosiddetta "a molti mondi"
prevede che ogni volta che viene effettuato un esperimento di questo tipo
si ottiene come conseguenza la creazione di tanti mondi distinti, uno per ogni
esito possibile.