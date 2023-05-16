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

# Le distribuzioni binomiali

Le Lanterne Verdi sono un gruppo di supereroi, a ognuno dei quali è affidato
un settore dell'Universo sul quale vegliare. Essi indossano un anello che
conferisce loro un insieme non ben definito di poteri, tra i quali la
capacità di creare oggetti, di volare e di sopravvivere nello spazio. La
potenza di questo anello diminuisce progressivamente, ed è quindi necessario
effettuare periodicamente delle operazioni di ricarica, inserendo l'anello
in una batteria a forma di lanterna (da cui il nome dei supereroi). Le
modalità con cui la potenza diminuisce e la frequenza di ricarica sono
cambiate via via che le serie che coinvolgono il gruppo delle Lanterne Verdi
hanno preso forma. Semplificando, immaginiamo che la potenza dell'anello
diminuisca di una quantità fissa ogni volta che questo viene utilizzato, e
che partendo da una piena ricarica sia possibile farlo per dieci volte.
Supponiamo che quando un (o una) Lanterna Verde affronta un nemico, ogni
attacco fatto grazie all'anello vada a segno con una probabilità $p$
prefissata. Se l'anello è completamente carico e Lanterna Verde ha di fronte
a sé dieci nemici che attacca uno dopo l'altro, ognuno per una sola volta,
di quanti di essi riuscirà adisfarsi? Sappiamo che l'anello può essere
utilizzato per dieci volte, quindi in teoria ogni attacco potrebbe avere
successo, sconfiggendo tutti e dieci gli avversari. D'altro canto, se nessuno
degli attacchi va a segno non vi sarà alcun nemico battuto. In generale, ci
potranno essere da zero a dieci attacchi vittoriosi, e ogni attacco può
essere pensato come un esperimento di Bernoulli di parametro fisso, nel quale
ovviamente il successo si verifica quando l'avversario viene battuto. Il
numero di vittorie si può quindi pensare come il numero di successi in dieci
ripetizioni di questo esperimento di Bernoulli. Se si esegue nuovamente
l'intero processo che consiste nell'eseguire le dieci ripetizioni e nel
contare i successi, il risultato sarà potenzialmente diverso, dunque siamo
in presenza di un nuovo tipo di esperimento casuale, i cui esiti vengono
generalmente descritti utilizzando una distribuzione binomiale.


## Il modello binomiale

Quando un fissato esperimento di Bernoulli di parametro $p$
viene ripetuto in condizioni di indipendenza per $n$ volte e si conta il
numero di successi, il risultato è un numero intero che definisce in modo
banale una variabile aleatoria, nel senso che è possibile definire una
variabile aleatoria $X$ che assume come valore esattamente il numero di
successi rilevato. La distribuzione di questa variabile aleatoria viene detta
di tipo _binomiale_, e il suo supporto sarà dunque l'insieme dei numeri
$D_X = \{ 0, 1, \dots, n \}$. Dato $x \in D_X$, per calcolare la probabilità
$\mathbb P(X=x)$ che esattamente $x$ delle $n$ ripetizioni abbiano come esito
un successo possiamo ragionare nel modo seguente. Per evitare ambiguità,
chiamiamo _esperimento binomiale_ l'esperimento casuale che consiste nel
contare il numero di successi nelle $n$ esecuzioni, così da non confonderlo
con l'esperimento di Bernoulli che viene ripetuto. Possiamo visualizzare lo
spazio $\Omega$ degli esiti dell'esperimento binomiale come l'insieme delle
parole di $n$ caratteri, ognuno dei quali può essere alternativamente
$\text{S}$ oppure $\text{F}$, a indicare, nell'ordine, un successo e un
fallimento. Per esempio, fissando $n=7$, $\text{SSSFFFF}$ indica l'esito che
si verifica quando nelle sette ripetizioni dell'esperimento di Bernoulli si
ottiene un successo alle prime tre ripetizioni, mentre tutte quelle che
seguono portano a un fallimento. Ora, la probabilità che questo succeda è

\begin{multline*}
\mathbb P(\{\text{SSSFFFF}\}) = \\
\mathbb P \left( \bigcap_{i=1}^3 \{\text{successo alla $i$-esima ripetizione}\}
\cap \bigcap_{i=4}^7 \{\text{insuccesso alla $i$-esima ripetizione}\} \right)
\end{multline*}

e l'indipendenza che governa per definizione la ripetizione degli esperimenti
permette di calcolare questa probabilità come

```{math}
\prod_{i=1}^3 \mathbb P \left(
  \{\text{successo alla $i$-esima ripetizione}\} \right)
\cdot \prod_{i=4}^7 \mathbb P \left(
  \{\text{insuccesso alla $i$-esima ripetizione}\} \right) \enspace.
```

Siccome le probabilità di successo e di insuccesso sono sempre uguali a $p$ e
a $1-p$, quale che sia la ripetizione considerata, avremo

```{math}
\mathbb P({\text{SSSFFFF}}) = p^3 (1-p)^4.
```

Usando lo stesso ragionamento si verifica facilmente che si ottiene la stessa
probabilità se invece di $\text{SSSFFFF}$ si considera $\text{FFFFSSS}$,
$\text{FSFSFSF}$ o in generale qualunque esito che contiene tre successi e
quattro insuccessi. Se indichiamo con $e_1, \dots, e_m$ tutti e soli gli
esiti di questo tipo e per ogni $i = 1, \dots, m$ definiamo
$E_i \coloneqq \{ e_i \}$, avremo $\mathbb P(E_i) = p^3 (1-p)^4$) e
$\{ X=3 \} = \cup_{i=1}^m E_i$. Essendo gli eventi $E_1, \dots, E_m$ a due a
due disgiunti, applicando il terzo assioma di Kolmogorov si ottiene

```{math}
\mathbb P(X = 3) = \sum_{i=1}^m \mathbb P(E_i) = m p^3 (1-p)^4 \enspace.
```

Rimane da calcolare il valore di $m$, che corrisponde al numero di modi
diversi di avere $3$ successi in $7$ esecuzioni dell'esperimento, o in
alternativa nel numero di parole di $7$ caratteri dei quali $3$ sono uguali
a $\text{S}$ e i rimanenti sono uguali a $\text{F}$. Questo conteggio si
effettua facilmente se si calcola il numero di modi nei quali è possibile
selezionare le tre posizioni nelle quali inserire $\text{S}$, perché una
volta fatto questo basterà completare le stringhe inserendo $\text{F}$ in
tutte le posizioni rimaste libere. Ognuna delle posizioni selezionate si può
descrivere con un numero intero da $1$ a $7$, e quindi le posizioni
selezionate descrivono un sottoinsieme di $\{1, 2, 3, 4, 5, 6, 7 \}$ che
contiene esattamente tre elementi. Il numero di siffatti sottoinsiemi è uguale
al numero di combinazioni di $7$ oggetti in $3$ posti, il che permette di
concludere che

```{math}
\mathbb P(X = 3) = \binom{7}{3} p^3 (1-p)^4 \enspace.
```

Se riconsideriamo ora l'intero ragionamento, ma in termini di un generico
numero $n$ di ripetizioni, fissato $x \in D_X$ si ottiene facilmente che

```{math}
\mathbb P(X = x) = \binom{n}{x} p^x (1-p)^{n-x} \enspace.
```

Siamo quindi in grado di definire in modo formale la famiglia delle
distribuzioni binomiali.

````{prf:definition} (La famiglia delle distribuzioni binomiali)
:label: def:binomial-distribution

Fissati $n \in \mathbb N$ e $p \in [0, 1]$, la distribuzione _binomiale_ di
parametri $n$ e $p$ è definita dalla funzione di massa di probabilità

```{math}
f(x; n, p) = \binom{n}{x} p^x (1 - p)^{n - x}
             \mathrm{I}_{\{0, 1, \dots, n\}}(x) \enspace.
```

Per indicare che una variabile aleatoria $X$ segue una siffatta distribuzione
utilizzerò la notazione $X \sim \mathrm B(n, p)$. L'insieme di tutte le
distribuzioni binomiale al variare dei relativi parametri prende il
nome di _famiglia delle distribuzioni binomiali_.
````

Si verifica facilmente che l'andamento della funzione
di massa di probabilità nei relativi punti di massa cresce inizialmente per
poi decrescere. Infatti, per un generico $x \in \{0, \dots, n-1\}$ vale

```{math}
\frac{f_X(x+1; n, p)}{f_X(x; n, p)} = \frac{n-x}{x+1} \frac{p}{1-p} \enspace,
```

e quindi per $x = (n+1)p - 1$, si dovrebbe avere
$f_X(x+1; n, p) = f_X(x; n, p)$, ma questo è vero solo se $(n+1)p - 1$ è
un valore intero (e in tal caso lo sarà anche $(n+1)p$). In tal caso, sempre
calcolando $f_X$ solo in corrispondenza delle specificazioni della
distribuzione, avremo che la funzione di massa di probabilità

- è strettamente crescente da $x = 0$ a $x = (n+1)p - 1$,
- assume il suo massimo per $x = (n+1)p - 1$ e $x = (n+1)p$, che sono quindi
  i due valori modali, e
- decresce strettamente da $x = (n+1)p$ in avanti.

Quando invece $(n+1)p - 1$ non è intero, i valori della funzione di massa di
probabilità crescono strettamente fino alla moda $x = \lfloor (n+1)p \rfloor$,
per poi decrescere, sempre strettamente, come illustrato nella
{numref}`Figura %s <fig:binomial-pmf>`. Va notato come le due distribuzioni
mostrate in questa figura sono _approssimativamente_ simmetriche rispetto
all'asse che coincide con il suo valore massimo (o che è posto esattamente a
metà tra i due massimi). Si ha invece una simmetria completa quando
$f_X(x; n, p) = f_X(n-x; n, k)$ per ogni $x = 1, \dots, \lfloor n/2 \rfloor$,
che equivale a richiedere

```{margin}
Questa uguaglianza segue dal fatto che $\binom{n}{n-k} = \binom{n}{k}$.
```
```{math}
p^x (1-p)^{n-x} = p^{n-x} (1-p)^x \enspace,
```

che a sua volta coincide con $p = 1-p$, che è verifcata solo quando $p = 1/2$.

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

from myst_nb import glue

fig, axes = plt.subplots(1, 2, sharey=True)

n = 10
x = np.arange(n+1)

for ax, p in zip(axes, (4 / (n+1), 0.4)):

    X = st.binom(n, p)

    ax.vlines(x, 0, X.pmf(x))
    ax.plot(x, X.pmf(x), 'o')
    ax.set_xticks(range(0, 11, 2))

plt.show()

glue("binomial-pmf", fig)
```

```{glue:figure} binomial-pmf
:name: fig:binomial-pmf
:figwidth: 100%

Grafici della funzione di massa di probabilità della distribuzione binomiale
di parametri $n = 10$ e $p$ uguale a $\frac{4}{11} \approx 0.36$ (sinistra) e
$0.4$ (destra).
```


Il modo più semplice per esprimere la forma analitica
della funzione di ripartizione di $X \sim \mathrm B(n, p)$ è

```{math}
F_X(x; n, p) = \mathbb P(X \leq x)
             = \sum_{y=0}^{\lfloor x \rfloor} \binom{n}{y} p^y (1 - p)^{n - y}
               \mathrm{I}_{[0, n]}(x) + \mathrm I_{(n, +\infty)}(x) \enspace,
```

perché a differenza di quanto succede per buona parte delle distribuzioni che
studieremo, non è possibile semplificare ulteriormente la sommatoria.
Riassumendo, la funzione di massa di probabilità di una distribuzione ha un
grafico a bastoncini approssimativamente simmetrico (con eccezione del caso
$p = n/2$, nel quale è simmetrico) le cui altezze crescono fino a un valore
della specificazione che si trova vicino a $np$ per poi iniziare a diminuire.
Da ciò segue il fatto che la somma dei valori di massa di probabilità che si
trovano a sinistra dell'asse di simmetria sarà approssimativamente uguale a
$\frac{1}{2}$, e lo stesso vale per i valori a destra di questo asse. La
funzione di ripartizione ha di conseguenza un grafico costante a tratti che è
approssimativamente simmetrico rispetto a un punto non troppo distante da
$(np, 1/2)$. Ciò è mostrato dal grafico prodotto dalla seguente cella
nascosta, nel quale i grafici delle funzioni di massa di probabilità e di
ripartizione vengono sovrapposti, evidenziando rispettivamente con un segmento
tratteggiato e con un quadrato i suddetti asse e punto di simmetria. Nella
versione interattiva del libro si possono modificare i valori dei due
parametri, vedendo come cambia il grafico prodotto.

```{code-cell} ipython3
:tags: [hide-input]

import ipywidgets as widgets

n_slider = widgets.IntSlider(value=4,
                             min=1,
                             max=20,
                             description='n',
                             continuous_update=True,
                             readout=False,
                             orientation='horizontal')

p_slider = widgets.FloatSlider(value=0.75,
                               min=0,
                               max=1,
                               step=0.1,
                               description='p',
                               continuous_update=True,
                               readout=False,
                               orientation='horizontal')

def binomial_pdf_cdf(n, p):
    B = st.binom(n, p)

    x = np.arange(0, n+1)
    y = B.pmf(x)

    plt.hlines([0] + list(B.cdf(x)), range(-1, n+1), list(range(n+1)) + [20])

    plt.vlines(x, 0, y, color='k')
    plt.plot(x, y, 'o')

    plt.plot([n*p], [0.5], 's')

    plt.title(rf'$n = {n}, p = {p:.2f}$')
    plt.xlim(-1, 21)
    plt.ylim(0, 1.1)
    plt.xticks(range(0, 21, 2))
    plt.show()

widgets.interactive(binomial_pdf_cdf, n=n_slider, p=p_slider)
```

Infine, vale la pena sottolineare un'importante relazione tra le distribuzioni
binomiale e di Bernoulli: abbiamo visto che il valore assunto da
$X \sim \mathrm B(n, p)$ corrisponde al numero di successi ottenuti ripetendo
$n$ volte un esperimento di Bernoulli in condizioni di indipendenza. Se
quindi introduciamo $n$ nuove variabili aleatorie $X_1, \dots, X_n$, tra loro
indipendenti e ognuna distribuita secondo una legge di Bernoulli di parametro
$p$, vale intuitivamente la relazione

```{math}
:label: eq:bernoulli-binomial

Y = \sum_{i=1}^n X_i \enspace,
```

che dimostreremo in modo formale nel
{numref}`Paragrafo %s <sec:binomial-moments>`, ma che utilizzeremo già nel
prossimo paragrafo per semplificare il calcolo del valore atteso e della
varianza della distribuzione binomiale. Ragionando in modo analogo, date due
variabili aleatorie indipendenti $X_1 \sim \mathrm B(n_1, p)$ e
$X_2 \sim \mathrm B(n_2, p)$, ponendo $Y = X_1 + X_2$ si può dimostrare che
$Y \sim \mathrm B(n_1 + n_2, p)$.


(sec:binomial-expected-val-and-var)=
## Valore atteso e varianza della distribuzione binomiale

Per quanto visto alla fine del paragrafo precedente, dati $n \in \mathbb N$,
$p \in [0, 1]$ e una variabile aleatoria $X \sim \mathbb B(n, p)$, possiamo
sempre scomporre quest'ultima nella somma di $n$ variabili aleatorie
$X_1, \dots, X_n$, tutte tra loro indipendenti e distribuite ciascuna secondo
una legge di Bernoulli di parametro $p$. Questo permette di calcolare il
valore atteso e la varianza della distribuzione binomiale in modo estremamente
semplice. Per quanto riguarda il valore atteso, infatti, si ha

```{math}
\mathbb E(X) = \mathbb E \left( \sum_{i=1}^n X_i \right)
             = \sum_{i=1}^n \mathbb E ( X_i )
             = \sum_{i=1}^n p = p \enspace,
```

mentre la varianza è uguale a

```{math}
\mathrm{Var}(X) = \mathrm{Var} \left( \sum_{i=1}^n X_i \right)
             = \sum_{i=1}^n \mathrm{Var} ( X_i )
             = \sum_{i=1}^n p(1-p) = np(1-p) \enspace,
```

dove il secondo passaggio è basato sul fatto che la varianza della somma di
variabili aleatorie indipendenti è uguale alla somma delle varianze delle
singole variabili.

Chiaramente, si arriva allo stesso risultato se si calcola il valore atteso
applicando la relativa definizione, come dimostrato nel seguente teorema.


```{prf:theorem}
:label: teo:binomial-expected-value
Dati $n \in \mathbb N$, $p \in [0, 1]$ e una variabile aleatoria
$X \sim \mathrm B(n, p)$, $\mathbb E(X) = np$.
```
````{prf:proof}
Applicando la definizione di valore atteso si ha

\begin{align*}
\mathbb E(X) &= \sum_{x=0}^n x \binom{n}{x} p^x (1 - p)^{n - x}
              = \sum_{x=1}^n x \binom{n}{x} p^x (1 - p)^{n - x}
              = n \sum_{x=1}^n \frac{(n-1)!}{(x-1)! (n-x)!} p^x (1 - p)^{n - x} \\
             &= n \sum_{x=1}^n \binom{n-1}{x-1} p^x (1 - p)^{n - x}
              = n \sum_{y=0}^{n-1} \binom{n-1}{y} p^{y+1} (1 - p)^{n - 1 - y} \\
             &= np \sum_{y=0}^{n-1} \binom{n-1}{y} p^y (1 - p)^{n - 1 - y} \\
             &= np \underbrace{\sum_{y=0}^{n-1} f_Y(y; n-1, p)}_{= 1}
              = np \enspace,
\end{align*}

dove

- nel terztultimo passaggio ho applicato all'indice muto della sommatoria
  la trasformazione $y = x - 1$, e
- nel penultimo ho messo in evidenza il fatto che il generico addendo della
  sommatoria coincide con il valore della funzione di massa di probabilità di
  variabile aleatoria $Y \sim \mathrm B(n - 1, p)$; essendo questi valori
  sommati per tutte le specificazioni di questa variabile aleatoria, il totale
  vale $1$.
````

Similmente, la varianza si può calcolare in modo analogo a quanto fatto finora
per le altre distribuzioni, come mostrato di seguito.

```{prf:theorem}
:label: teo:binomial-variance

Dati $n \in \mathbb N$, $p \in [0, 1]$, la varianza di una variabile aleatoria
$X \sim \mathrm B(n, p)$ è uguale a $np(1-p)$.
```
```{prf:proof}
Procedendo in modo analogo al {prf:ref}`teo:binomial-expected-value` si ha

\begin{align*}
\mathbb E\left(X^2\right)
        &= \sum_{x=0}^n x^2 \binom{n}{x} p^x (1 - p)^{n - x}
         = \sum_{x=1}^n x^2 \binom{n}{x} p^x (1 - p)^{n - x}
         = n \sum_{x=1}^n x \binom{n-1}{x-1} p^x (1 - p)^{n - x} \\
        &= np \sum_{y=0}^{n-1} (y + 1) \binom{n-1}{y} p^y (1 - p)^{n - 1 - y}
         = np \sum_{y=0}^{n-1} (y + 1) f_Y(y; n - 1, p)
         = np \mathbb E(Y + 1) \\
        &= np \left( (n - 1)p + 1 \right)
         = n^2p^2 - np^2 + np \enspace,
\end{align*}

così che $\mathrm{Var}(X) = \mathbb E \left( X^2 \right) - \mathbb E(X)^2
= np - n^2p^2 = n p (1 - p)$.
```

(sec:binomial-moments)=
## Momenti delle distribuzioni binomiali (*)

Fissati $n \in \mathbb N$ e $p \in [0, 1]$, la funzione generatrice dei momenti
di una variabile aleatoria $X \sim \mathrm B(n, p)$ soddisfa

```{math}
m_X(t) = \mathbb E \left( \mathrm e^{tX} \right)
       = \sum_{x=0}^n \mathrm e^{tx} \binom{n}{x} p^x (1 - p)^{n - x}
       = \sum_{x=0}^n \binom{n}{x} \left(p \mathrm e^t \right)^x (1 - p)^{n - x}
       = \left( p \mathrm e^t + 1 - p \right)^n
```

e permette di dimostrare {eq}`eq:bernoulli-binomial`.

````{prf:theorem}
:label: teo:sum-bernoulli

Dati $n \in \mathbb N$, $p \in [0, 1]$ e una variabile aleatoria
$X \sim \mathbb B(n, p)$, vale la relazione

```{math}
Y = \sum_{i=1}^n X_i \enspace,
```

dove per ogni $i = 1, \dots, n$ si ha $X_i \sim \mathrm B(p)$, e queste $n$
variabili aleatorie sono tra loro indipendenti.
````
````{prf:proof}
L'ipotesi di indipendenza di $X_1, \dots, X_n$ permette di applicare il
{prf:ref}`teo:mgf-method`: indicando con $m_X$ la funzione generatrice dei
momenti della distribuzione $\mathrm B(p)$ si ottiene

```{math}
m_Y(t) = m_X(t)^n = (1 + p\left( \mathrm e^t - 1 \right))^n \enspace,
```

da cui segue la tesi.
````

Procedendo in modo molto simile possiamo dimostrare che la somma di due
variabili aleatorie binomiali indipendenti e con lo stesso parametro $p$
segue anch'essa una distribuzione binomiale.

````{prf:theorem}
:label: teo:sum-binomial

Siano dati $n_1, n_2 \in \mathbb N$, $p \in [0, 1]$ e due variabili aleatorie
indipendenti $X_1$ e $X_2$ tali che $X_i \sim \mathbb B(n_i, p)$ per
$i = 1, 2$. Definita $Y \coloneqq X_1 + X_2$, si ha
$Y \sim \mathbb B(n_1+n_2, p)$.
````
````{prf:proof}
Anche in questo caso, indicando per semplicità con $m_1$ e $m_2$ le funzioni
generatrici dei momenti di $X_1$ e $X_2$, possiamo applicare il
{prf:ref}`teo:mgf-method`, ottenendo

\begin{align*}
m_Y(t) &= m_1(t) \cdot m_2(t)
        = (1 + p\left( \mathrm e^t - 1 \right))^{n_1}
         (1 + p\left( \mathrm e^t - 1 \right))^{n_2} \\
       &= (1 + p\left( \mathrm e^t - 1 \right))^{n_1 + n_2} \enspace,
\end{align*}

che individua per $Y$ una distribuzione binomiale di parametri $n_1 + n_2$
e $p$.
````

Derivare la funzione generatrice dei momenti della distribuzione binomiale
risulta abbastanza intricato. Questo rende più ragionevole il calcolo dei
momenti della distribuzione applicando direttamente la loro definizione, e
sfruttando la stessa tecnica utilizzata nel
{numref}`Paragrafo %s <sec:binomial-expected-val-and-var>` per derivare i
momenti primo e secondo. Per esempio, il momento terzo si ottiene nel modo
seguente:

\begin{align*}
\mu'_3 &= \mathbb E\left( X^3 \right)
        = \sum_{x=0}^n x^3 \binom{n}{x} p^x (1 - p)^{n - x}
        = n \sum_{x=1}^n x^2 \binom{n-1}{x-1} p^x (1 - p)^{n - x} \\
       &= np \sum_{y=0}^{n-1} (y + 1)^2 \binom{n-1}{y} p^y (1 - p)^{n - 1 - y}
        = np \mathbb E\left((Y + 1)^2\right) \enspace,
\end{align*}

dove $Y \sim \mathrm B(n - 1, p)$, e dunque

\begin{align*}
\mu'_3 &= np \left( \mathrm{Var}(Y + 1) + \mathbb E(Y + 1)^2 \right)
        = np \left( \mathrm{Var}(Y) + (\mathbb E(Y) + 1)^2 \right) \\
       &= np \left( (n-1)p(1-p) + ((n-1)p + 1)^2 \right)
        = np \left( n^2p^2 - 3np^2 + 2p^2 + 3np -3p + 1 \right) \enspace.
\end{align*}

Il momento centrale terzo sarà quindi uguale a

\begin{align*}
\mu_3 &= \mathbb E\left( (X - np)^3 \right)
       = \mathbb E\left( X^3 \right) - 3np \mathbb E\left( X^2 \right)
         + 3n^2p^2 \mathbb E( X ) - n^3p^3 \\
      &= np \left( n^2p^2 - 3np^2 + 2p^2 + 3np -3p + 1 \right)
         -3np \left( n^2p^2 - np^2 + np \right) + 2 n^3p^3 \\
      &= np(1 - p)(1 - 2p)
\end{align*}

e di conseguenza la skewness vale

```{math}
\frac{\mu_3}{\sigma^3} = \frac{np(1 - p)(1 - 2p)}{np(1 - p)\sqrt{np(1 - p)}}
                       = \frac{1 - 2p}{\sqrt{np(1 - p)}} \enspace,
```

evidenziando come la distribuzione binomiale sia simmetrica quando
$p = \frac{1}{2}$, asimmetrica a destra quando $p < \frac{1}{2}$ e asimmetrica
a sinistra nei casi rimanenti, come esemplificato in
{numref}`Figura %s <fig:binomial-skewness>`.  Va notato come i due parametri
influenzino in modo diverso questo coefficiente: infatti, indipendentemente da
$n$ il suo valore tende a infinito tanto più $p$ si avvicina a $0$ oppure a
$1$, e ciò è dovuto al fatto che la distribuzione non possiede una delle sue
due code, essendo localizzata vicino agli estremi del suo supporto; d'altra
parte, quando $p$ è abbastanza lontano dai suoi valori estremi la simemtria
della distribuzione è maggiormente influenzata da $n$, perché quanto più esso
aumenta, tanto più si estendono la sue due code.

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

def binomial_plot(p, ax):
    n = 10
    x = np.arange(0, n+1)
    B = st.binom(n, p)
    ax.vlines(x, 0, B.pmf(x))
    ax.plot(x, B.pmf(x), 'o')
    ax.set_ylim(0, 0.3)

fig, axes = plt.subplots(1, 3, sharey=True)
for p, ax in zip((.3, .5, .7), axes):
    binomial_plot(p, ax)
plt.show()

glue("binomial-skewness", fig)
```

```{glue:figure} binomial-skewness
:name: fig:binomial-skewness
:figwidth: 100%

Grafici della funzione di massa di probabilità della distribuzione binomiale
di parametri $n = 10$ e $p$ uguale a $0.3$ (sinistra), $0.5$ (centro) e $0.7$
(destra), evidenziando rispettivamente l'asimmetria a destra, la simmetria e
l'asimmetria a sinistra delle corrispondenti distribuzioni.
```

In modo simile si ottiene il momento quarto: sempre introducendo
$Y \sim \mathbb B(n-1, p)$,

\begin{align*}
\mu'_4 &= \mathbb E \left( X^4 \right)
        = \sum_{x=0}^n x^4 \binom{n}{x} p^x (1 - p)^{n - x}
        = np\sum_{y=0}^{n-1} (y+1)^3 \binom{n-1}{y} p^y (1 - p)^{n - 1 - y} \\
       &= np \mathbb E\left( (Y+1)^3 \right)
        = np \left( \mathbb E\left( Y^3 \right ) 
                    + 3 \mathbb E\left( Y^2 \right )
                    + 3 \mathbb E(Y) + 1 \right) \\
       &= np \left(
             n^3p^3 - 6n^2p^3 + 11np^3 -6p^3 +6n^2p^2 -18np^2
             + 12p^2 +7np -7p +1
             \right) \enspace,
\end{align*}

così che il momento centrale corrispondente è

\begin{align*}
\mu_4 &= \mathbb E \left( (X - np)^4  \right)
       = \mu'_4 - 4 np \mu'_3 + 6 n^2p^2 \mu'_2 - 4 n^4p^4 + n^4p^4 \\
      &= np \left( 3np^3 - 6np^2 + 3np - 6p^3 + 12p^2 - 7p + 1 \right)
       = np (1-p) \left( 3p(n-2)(1-p) + 1 \right) \enspace.
\end{align*}

Ciò permette di ricavare la curtosi:

```{math}
:label: eq:binomial_kurtosis

\frac{\mu_4}{\sigma^4} - 3 = \frac{np (1-p) \left( 3p(n-2)(1-p) + 1 \right)}
                                  {\left( np(1-p) \right)^2} - 3
                           = \frac{1 - 6p(1-p)}{np(1-p)} \enspace,
```

da cui si verifica che, indipendentemente dal valore di $n$, la distribuzione
risulta rispettivamente platicurtica, mesocurtica o leptocurtica negli stessi
casi di una distribuzione di Bernoulli il cui parametro coincide con $p$.
Fatto salvo tutto ciò, $n$ influisce comunque sulla propensione della
distribuzione a generare valori fuori scala: {eq}`eq:binomial_kurtosis` mostra
infatti che quando $n$ aumenta, se la distribuzione è platicurtica deve
aumentare anche la curtosi, e ciò è dovuto al fatto che il supporto diventa
sempre più grande e quindi le specificazioni che si possono considerare
dei valori fuori scala diventano sempre di più; al contrario, quando la
distribuzione è platicurtica l'aumentare del supporto tenderà ad accentuare
la propensione della distribuzione a non generare valori fuori scala. La
{numref}`Figura %s <fig:binomial-sk-plot>` illustra il grafico
skewness-curtosi per la famiglia delle distribuzioni di Bernoulli, generando
diverse curve per differenti valori di $n$.

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

fig, ax = plt.subplots()

n = 2
p = np.linspace(0.001, 0.999, 500)

for n in (1, 2, 3, 5, 10, 100):
    skewness = (1 - 2*p) / (n * p * (1 - p))**0.5
    kurtosis = (1 - 6 * p * (1 - p)) / (n * p * (1 - p))

    plt.plot(skewness, kurtosis, label=n)

plt.xlim(-3, 3)
plt.ylim(-2, 2)
plt.legend()
plt.show()

glue("binomial-sk-plot", fig, display=True)
```

```{glue:figure} binomial-sk-plot
:figwidth: 400pt
:name: "fig:binomial-sk-plot"

Il grafico skewness-curtosi per la famiglia delle distribuzioni
binomiali. Ogni curva corrisponde a un valore diverso per il parametro $n$,
come indicato dalla legenda.
```