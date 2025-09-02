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

(sec:modello-binomiale)=
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

```{math}
\begin{align*}
\mathbb P(\{\text{SSSFFFF}\}) = \\
\mathbb P \left( \bigcap_{i=1}^3 \{\text{successo alla $i$-esima ripetizione}\}
\cap \bigcap_{i=4}^7 \{\text{insuccesso alla $i$-esima ripetizione}\} \right)
\end{align*}
```

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
\mathbb P(\{ \text{SSSFFFF} \}) = p^3 (1-p)^4.
```

Usando lo stesso ragionamento si verifica facilmente che si ottiene la stessa
probabilità se invece di $\text{SSSFFFF}$ si considera $\text{FFFFSSS}$,
$\text{FSFSFSF}$ o in generale qualunque esito che contiene tre successi e
quattro insuccessi. Se indichiamo con $e_1, \dots, e_m$ tutti e soli gli
esiti di questo tipo e per ogni $i = 1, \dots, m$ definiamo
$E_i \triangleq \{ e_i \}$, avremo $\mathbb P(E_i) = p^3 (1-p)^4$ e
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

````{prf:definition} La famiglia delle distribuzioni binomiali
:label: def:binomial-distribution

Fissati $n \in \mathbb N$ e $p \in [0, 1]$, la distribuzione _binomiale_ di
parametri $n$ e $p$ è definita dalla funzione di massa di probabilità

```{math}
:label: eq:binomial-pdf

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
:label: eq:binomial-pdf-ratio

\frac{f_X(x+1; n, p)}{f_X(x; n, p)} = \frac{n-x}{x+1} \frac{p}{1-p} \enspace,
```

e lo stesso rapporto diventa uguale a $1$ quando $x = (n+1)p - 1$. Se tale
valore è intero, lo sarà anche $(n+1)p$ e $f_X(x+1; n, p) = f_X(x; n, p)$. In
tal caso, sempre calcolando $f_X$ solo in corrispondenza delle specificazioni
della distribuzione, avremo che la funzione di massa di probabilità

- è strettamente crescente da $x = 0$ a $x = (n+1)p - 1$,
- assume il suo massimo per $x = (n+1)p - 1$ e $x = (n+1)p$, che sono quindi
  i due valori modali, e
- decresce strettamente da $x = (n+1)p$ in avanti.

Quando invece $(n+1)p - 1$ non è intero, i valori della funzione di massa di
probabilità crescono strettamente fino alla moda $x = \lfloor (n+1)p \rfloor$,
per poi decrescere, sempre strettamente, come illustrato nella
{numref}`fig:binomial-behaviour`, che mostra i grafici della funzione di massa
di probabilità della distribuzione binomiale di parametri $n = 10$ e $p$ uguale
a $\frac{4}{11} \approx 0.36$ (a sinistra) e $0.4$ (a destra).

````{customfigure}
:name: fig:binomial-behaviour

```{code-block} python
:class: toggle-code

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

fig, axes = plt.subplots(1, 2, sharey=True)

n = 10
x = np.arange(n+1)

for ax, p in zip(axes, (4 / (n+1), 0.4)):

    X = st.binom(n, p)

    ax.vlines(x, 0, X.pmf(x))
    ax.plot(x, X.pmf(x), 'o')
    ax.set_xticks(range(0, 11, 2))

plt.show()
```

Grafici della funzione di massa di probabilità della distribuzione binomiale di
parametri $n = 10$ e $p$ rispettivamente uguale a $\frac{4}{11} \approx 0.36$
(a sinistra) e $0.4$ (a destra).
````

Va notato come le due distribuzioni mostrate in questa figura sono
_approssimativamente_ simmetriche rispetto all'asse che coincide con il suo
valore massimo (o che è posto esattamente a metà tra i due massimi). Si ha
invece una simmetria completa quando
$f_X(x; n, p) = f_X(n-x; n, k)$ per ogni $x = 1, \dots, \lfloor n/2 \rfloor$,
che equivale a richiedere

```{margin}
Questa uguaglianza segue dal fatto che $\binom{n}{n-k} = \binom{n}{k}$.
```
```{math}
p^x (1-p)^{n-x} = p^{n-x} (1-p)^x \enspace,
```

che a sua volta coincide con $p = 1-p$, che è verifcata solo quando $p = 1/2$.
Il modo più semplice per esprimere la forma analitica della funzione di
ripartizione di $X \sim \mathrm B(n, p)$ è

```{math}
:label: eq:binomial-cdf

F_X(x; n, p) = \mathbb P(X \leq x)
             = \sum_{y=0}^{\lfloor x \rfloor} \binom{n}{y} p^y (1 - p)^{n - y}
               \mathrm{I}_{[0, n]}(x) + \mathrm I_{(n, +\infty)}(x) \enspace,
```

perché a differenza di quanto succede per buona parte delle distribuzioni che
studieremo, non è possibile semplificare ulteriormente la sommatoria.
Riassumendo, la funzione di massa di probabilità di una distribuzione ha un
grafico a bastoncini approssimativamente simmetrico (con eccezione del caso $p
= n/2$, nel quale è simmetrico) le cui altezze crescono fino a un valore della
specificazione che si trova vicino a $np$ per poi iniziare a diminuire. Da ciò
segue il fatto che la somma dei valori di massa di probabilità che si trovano a
sinistra dell'asse di simmetria sarà approssimativamente uguale a
$\frac{1}{2}$, e lo stesso vale per i valori a destra di questo asse. La
funzione di ripartizione ha di conseguenza un grafico costante a tratti che è
approssimativamente simmetrico rispetto a un punto non troppo distante da $(np,
1/2)$. Ciò è illustrato in {numref}`fig:binomial-pdf-cdf`, nel quale i grafici
delle funzioni di massa di probabilità e di ripartizione vengono sovrapposti,
evidenziando rispettivamente con un segmento tratteggiato e con un quadrato i
suddetti asse e punto di simmetria. Modificando i valori dei due parametri si
può vedere come cambia il grafico prodotto.

````{customfigure}
:name: fig:binomial-pdf-cdf

```{code-block} python
:class: toggle-code 

import numpy as np
import scipy.stats as st
from js import document
from pyodide.ffi import create_proxy
import io
import base64

def binomial_pdf_cdf(n, p):
    fig, ax = plt.subplots()

    B = st.binom(n, p)

    x = np.arange(0, n+1)
    y = B.pmf(x)

    ax.hlines([0] + list(B.cdf(x)), range(-1, n+1), list(range(n+1)) + [20])

    ax.vlines(x, 0, y, color='k')
    ax.plot(x, y, 'o')

    ax.set_title(f'n = {n}, p = {p:.2f}')
    ax.set_xlim(-1, 21)
    ax.set_ylim(0, 1.1)
    ax.set_xticks(range(0, 21, 2))
    
    # Manual rendering to avoid MathJax processing
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format='png', bbox_inches='tight', dpi=100)
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    img_buffer.close()
    
    # Display in protected div
    img_html = '<div class="no-mathjax"><img src="data:image/png;base64,' + \
               img_base64 + '" style="max-width: 100%; height: auto;" /></div>'
    Element("pdf-cdf-output").write(img_html)
    
    plt.close(fig)

def update_plot(event=None):
    n = int(document.getElementById("n-slider").value)
    document.getElementById("n-value").innerText = f"{n:d}"
    p = float(document.getElementById("p-slider").value)
    document.getElementById("p-value").innerText = f"{p:.1f}"
    binomial_pdf_cdf(n, p)


p_slider = document.getElementById("p-slider")
p_slider.addEventListener("input", create_proxy(update_plot))

n_slider = document.getElementById("n-slider")
n_slider.addEventListener("input", create_proxy(update_plot))

# Initial plot
binomial_pdf_cdf(10, 0.5)
```
```{raw} html

<div id="plot-container" style="visibility: none;">
    <div class="slider-container" style="float: left;">
        <label for="n-slider">\( n \): </label>
        <input type="range" id="n-slider"
               min="2" max="20" value="10" step="1" />
        <span id="n-value">0</span>
    </div>

    <div class="slider-container" style="float: right;">
        <label for="p-slider">\( p \): </label>
        <input type="range" id="p-slider"
               min="0" max="1" value="0.5" step="0.1" />
        <span id="p-value">0.5</span>
    </div>

    <div id="pdf-cdf-output" class="no-mathjax"
            style="clear: both; display: flex; justify-content: center; margin-bottom: 2em;">
    </div>
</div>
```

Grafici delle funzioni di massa di probabilità e di ripartizione del modello
binomiale.
````

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

che dimostreremo in modo formale nel Paragrafo {ref}`sec:binomial-moments`, ma
che utilizzeremo già nel prossimo paragrafo per semplificare il calcolo del
valore atteso e della varianza della distribuzione binomiale. Ragionando in
modo analogo, date due variabili aleatorie indipendenti
$X_1 \sim \mathrm B(n_1, p)$ e $X_2 \sim \mathrm B(n_2, p)$, ponendo
$Y = X_1 + X_2$ si può dimostrare che $Y \sim \mathrm B(n_1 + n_2, p)$.


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
````{admonition} _
:class: myproof

Applicando la definizione di valore atteso si ha

```{math}
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
```

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
````{admonition} _
:class: myproof

Procedendo in modo analogo al {prf:ref}`teo:binomial-expected-value` si ha

```{math}
\begin{align*}
\mathbb E\left(X^2\right)
        &= \sum_{x=0}^n x^2 \binom{n}{x} p^x (1 - p)^{n - x}
         = \sum_{x=1}^n x^2 \binom{n}{x} p^x (1 - p)^{n - x} \\
        &= n \sum_{x=1}^n x \binom{n-1}{x-1} p^x (1 - p)^{n - x} \\
        &= np \sum_{y=0}^{n-1} (y + 1) \binom{n-1}{y} p^y (1 - p)^{n - 1 - y} \\
        &= np \sum_{y=0}^{n-1} (y + 1) f_Y(y; n - 1, p)
         = np \mathbb E(Y + 1) \\
        &= np \left( (n - 1)p + 1 \right)
         = n^2p^2 - np^2 + np \enspace,
\end{align*}
```

così che $\mathrm{Var}(X) = \mathbb E \left( X^2 \right) - \mathbb E(X)^2
= np - n^2p^2 = n p (1 - p)$.
````

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
````{admonition} _
:class: myproof

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
$i = 1, 2$. Definita $Y \triangleq X_1 + X_2$, si ha
$Y \sim \mathbb B(n_1+n_2, p)$.
````
````{admonition} _
:class: myproof

Anche in questo caso, indicando per semplicità con $m_1$ e $m_2$ le funzioni
generatrici dei momenti di $X_1$ e $X_2$, possiamo applicare il
{prf:ref}`teo:mgf-method`, ottenendo

```{math}
\begin{align*}
m_Y(t) &= m_1(t) \cdot m_2(t)
        = (1 + p\left( \mathrm e^t - 1 \right))^{n_1}
         (1 + p\left( \mathrm e^t - 1 \right))^{n_2} \\
       &= (1 + p\left( \mathrm e^t - 1 \right))^{n_1 + n_2} \enspace,
\end{align*}
```

che individua per $Y$ una distribuzione binomiale di parametri $n_1 + n_2$
e $p$.
````

Derivare la funzione generatrice dei momenti della distribuzione binomiale
risulta abbastanza intricato. Questo rende più ragionevole il calcolo dei
momenti della distribuzione applicando direttamente la loro definizione, e
sfruttando la stessa tecnica utilizzata nel
Paragrafo {ref}`sec:binomial-expected-val-and-var` per derivare i
momenti primo e secondo. Per esempio, il momento terzo si ottiene nel modo
seguente:

```{math}
\begin{align*}
\mu^\prime_3 &= \mathbb E\left( X^3 \right)
              = \sum_{x=0}^n x^3 \binom{n}{x} p^x (1 - p)^{n - x}
              = n \sum_{x=1}^n x^2 \binom{n-1}{x-1} p^x (1 - p)^{n - x} \\
       &= np \sum_{y=0}^{n-1} (y + 1)^2 \binom{n-1}{y} p^y (1 - p)^{n - 1 - y}
        = np \mathbb E\left((Y + 1)^2\right) \enspace,
\end{align*}
```

dove $Y \sim \mathrm B(n - 1, p)$, e dunque

```{math}
\begin{align*}
\mu^\prime_3 &= np \left( \mathrm{Var}(Y + 1) + \mathbb E(Y + 1)^2 \right)
              = np \left( \mathrm{Var}(Y) + (\mathbb E(Y) + 1)^2 \right) \\
            &= np \left( (n-1)p(1-p) + ((n-1)p + 1)^2 \right)
             = np \left( n^2p^2 - 3np^2 + 2p^2 + 3np -3p + 1 \right) \enspace.
\end{align*}
```

Il momento centrale terzo sarà quindi uguale a

```{math}
\begin{align*}
\mu_3 &= \mathbb E\left( (X - np)^3 \right)
       = \mathbb E\left( X^3 \right) - 3np \mathbb E\left( X^2 \right)
         + 3n^2p^2 \mathbb E( X ) - n^3p^3 \\
      &= np \left( n^2p^2 - 3np^2 + 2p^2 + 3np -3p + 1 \right)
         -3np \left( n^2p^2 - np^2 + np \right) + 2 n^3p^3 \\
      &= np(1 - p)(1 - 2p)
\end{align*}
```

e di conseguenza la skewness vale

```{math}
\frac{\mu_3}{\sigma^3} = \frac{np(1 - p)(1 - 2p)}{np(1 - p)\sqrt{np(1 - p)}}
                       = \frac{1 - 2p}{\sqrt{np(1 - p)}} \enspace,
```

evidenziando come la distribuzione binomiale sia simmetrica quando $p =
\frac{1}{2}$, asimmetrica a destra quando $p < \frac{1}{2}$ e asimmetrica a
sinistra nei casi rimanenti, come esemplificato in
{numref}`fig:binomial-asymmetry`, che mostra il grafico della funzione di
massa di probabilità binomiali di parametri $n = 10$ e $p$ rispettivamente
uguale a $0.3$ (a sinistra), $0.5$ (al centro) e $0.7$ (a destra), evidenziando
rispettivamente l'asimmetria a destra, la simmetria e l'asimmetria a sinistra
delle corrispondenti distribuzioni.

````{customfigure}
:name: fig:binomial-asymmetry

```{code-block} python
:class: toggle-code

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
```

Grafico della funzione di massa di probabilità delle distribuioni binomiali
caratterizzate da $n = 10$ e $p$ rispettivamente
uguale a $0.3$ (a sinistra), $0.5$ (al centro) e $0.7$ (a destra); i tre casi
esemplificano, nell'ordine, il concetto di distribuzione asimmetrica a destra,
simmetrica e asimmetrica a sinistra.
````

Va notato come i due parametri influenzino in modo diverso questo coefficiente:
infatti, indipendentemente da $n$ il suo valore tende a infinito tanto più $p$
si avvicina a $0$ oppure a $1$, e ciò è dovuto al fatto che la distribuzione
non possiede una delle sue due code, essendo localizzata vicino agli estremi
del suo supporto; d'altra parte, quando $p$ è abbastanza lontano dai suoi
valori estremi la simemtria della distribuzione è maggiormente influenzata da
$n$, perché quanto più esso aumenta, tanto più si estendono la sue due code.

In modo simile si ottiene il momento quarto: sempre introducendo
$Y \sim \mathbb B(n-1, p)$,

```{math}
\begin{align*}
\mu^\prime_4 &= \mathbb E \left( X^4 \right)
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
```

così che il momento centrale corrispondente è

```{math}
\begin{align*}
\mu_4 &= \mathbb E \left( (X - np)^4  \right)
       = \mu'_4 - 4 np \mu'_3 + 6 n^2p^2 \mu'_2 - 4 n^4p^4 + n^4p^4 \\
      &= np \left( 3np^3 - 6np^2 + 3np - 6p^3 + 12p^2 - 7p + 1 \right)
       = np (1-p) \left( 3p(n-2)(1-p) + 1 \right) \enspace.
\end{align*}
```

Ciò permette di ricavare la curtosi:

```{math}
:label: eq:binomial_kurtosis

\frac{\mu_4}{\sigma^4} - 3 = \frac{np (1-p) \left( 3p(n-2)(1-p) + 1 \right)}
                                  {\left( np(1-p) \right)^2} - 3
                           = \frac{1 - 6p(1-p)}{np(1-p)} \enspace,
```

da cui si verifica che, indipendentemente dal valore di $n$, la distribuzione
risulta rispettivamente platicurtica, mesocurtica o leptocurtica negli stessi
casi di una distribuzione di Bernoulli il cui parametro coincide con $p$. Fatto
salvo tutto ciò, $n$ influisce comunque sulla propensione della distribuzione a
generare valori fuori scala: {eq}`eq:binomial_kurtosis` mostra infatti che
quando $n$ aumenta, se la distribuzione è platicurtica deve aumentare anche la
curtosi, e ciò è dovuto al fatto che il supporto diventa sempre più grande e
quindi le specificazioni che si possono considerare dei valori fuori scala
diventano sempre di più; al contrario, quando la distribuzione è platicurtica
l'aumentare del supporto tenderà ad accentuare la propensione della
distribuzione a non generare valori fuori scala. La
{numref}`fig:binomial-sk-graph` illustra il grafico skewness-curtosi per la
famiglia delle distribuzioni di Bernoulli, generando diverse curve per
differenti valori di $n$.

````{customfigure}
:name: fig:binomial-sk-graph

```{code-block} python
:class: toggle-code

from matplotlib import cm

fig, ax = plt.subplots()

n_values = (1, 2, 3, 5, 10, 100)
p = np.linspace(0.001, 0.999, 500)

colors = cm.Blues(np.linspace(0.4, 0.9, len(n_values)))

for n, c in zip(n_values, colors):
    skewness = (1 - 2*p) / (n * p * (1 - p))**0.5
    kurtosis = (1 - 6 * p * (1 - p)) / (n * p * (1 - p))

    plt.plot(skewness, kurtosis, label=n, color=c)

plt.xlim(-3, 3)
plt.ylim(-2, 2)
plt.legend()
plt.show()
```

Grafico skewness-curtosi del modello binomiale.
````


(sec:binomial-quantiles)=
## Quantili della distribuzione binomiale (*)

Analizzando {eq}`eq:binomial-cdf` si vede come determinare in modo esatto un
generico quantile per la distribuzione binomiale sia decisamente complesso:
occorrerebbe, dato $q \in [0, 1]$, determinare $x_q$ tale che

```{math}
\sum_{y=0}^{x_q} \binom{n}{y} p^y (1 - p)^{n - y} = q \enspace,
```

e in effetti trovare una forma analitica per la soluzione di questa equazione
richiederebbe di introdurre delle funzioni, cosiddette _speciali_, definite
in termini di particolari integrali. Possiamo però analizzare il caso
particolare della mediana con un po' più di attenzione, ricordando che il
grafico della funzione di massa di probabilità della distribuzione binomiale
è approssimativamente simmetrico attorno al valore (o ai valori) della sua
moda.

Consideriamo prima il caso nel quale ci sono due valori modali, che abbiamo
visto essere i due valori interi successivi $m_1 = (n+1)p - 1$ e
$m_2 = (n+1)p$. La simmetria approssimata ci permette di dire che

```{math}
f_X(m_1 - i; n, p) \approx f_X(m_2 + i; n, p)
```

```{margin}
Il valore massimo di $i$ per cui questa formula è valida è il minimo tra due
quantità che rappresentano quante specificazioni della variabile aleatoria si
trovano a sinistra e a destra, rispettivamente, del più piccolo e del più
grande tra i due valori modali. Va ricordato, infatti, che quando
$p \neq \frac{1}{2}$ il grafico della funzione di massa di probabilità ha
una coda a sinistra oppure a destra, e tutte le specificazioni in questa coda
non hanno delle omologhe specificazioni simmetriche rispetto alle mode.
```
per ogni $i = 1, \dots, \min\{m_1, n - m_2 \}$, e inoltre l'uguaglianza
diventa esatta per $i = 0$. Ciò significa che

```{math}
\sum_{x = 0}^{m_1} f_X(x; n, p) \approx \sum_{x = m_2}^n f_X(x; n, p)
\enspace,
```

e quindi $\mathbb P(X \leq m_1) \approx \mathbb P(X \geq m_2)$. La somma di
queste due probabilità è uguale a $1$, dunque è ragionevole supporre che
entrambe siano uguali a $\frac{1}{2}$. Se questo fosse vero, allora la
mediana di $X$ sarebbe necessariamente uguale a $m_1$, perché
$F_X(m_1) = \frac{1}{2}$ e $m_1$ è la più piccola specificazione di $X$ in
corrispondenza della quale la funzione di ripartizione è maggiore o uguale
di $\frac{1}{2}$ (perché i valori della ripartizione in corrispondenza delle
specificazioni più piccole di $m_1$, se esistono, saranno necessariamente più
piccoli di $\frac{1}{2}$). Va sottolineato, inoltre, che in questo caso
$m_1 = \lfloor np \rfloor$.

Nei casi rimanenti, c'è un unico valore modale
$m = \lfloor(n+1)p\rfloor = \lceil np \rceil$, e usando la stessa
argomentazione legata alla simmetria della funzione di massa di probabilità,
possiamo assumere

```{math}
\mathbb P(X < m) \approx \mathbb P(X > m) \enspace,
```

e i valori di queste due probabilità devono essere necessariamente minori di
$\frac{1}{2}$, altrimenti la specificazione che corrisponde alla moda
avrebbe probabilità nulla. Se le due probabilità fossero uguali, ciò
implicherebbe che $m$ è anche la mediana della distribuzione. Ciò non è
necessariamente vero, ma in generale si può dimostrare che la mediana della
distribuzione è sempre compresa tra $\lfloor np \rfloor$ e $\lceil np \rceil$.

```{margin}
Ovviamente, vale la pena calcolare i quantili utilizzando direttamente
l'implementazione messa a disposizione da `scipy.stats`, descritta in
dettaglio nel paragrafo seguente.
```
Questo tipo di ragionamento non si può estendere facilmente al calcolo dei
rimanenti quantili utilizzando una formula analitica, ma questo non ci
impedisce di calcolarli _operativamente_, scrivendo del codice che somma i
valori della funzione di massa di probabilità fino a quando non si ottiene un
risultato che supera il livello del quantile. La cella seguente implementa
questa strategia per implementare la funzione `quantiles`, che restituisce una
lista di valori che corrispondono ai quantili di una distribuzione binomiale,
specificando i parametri di quest'ultima e una lista dei livelli
corrispondenti.

```{code-block} python

from scipy.special import binom

def quantiles(n, p, levels):
    x = 0

    pdf = (1-p)**n
    cdf = pdf
    quantiles = []

    for q in levels:
        while cdf < q:
            pdf *= (n - x) / (x + 1) * p / (1 - p)
            cdf += pdf
            x += 1
        quantiles.append(x)

    return quantiles
```

Invece di ricalcolare da zero tutti i valori della funzione di ripartizione
$F$, questa implementazione li ottiene sfruttando una strategia basata
sull'accumulazione[^accumulazione]: una volta ottenuto $F(0)$, ogni valore
successivo $F(x+1)$ è ricavato sommando a $F(x)$, che è già stato ricavato, la
probabilità della nuova specificazione $x$. In questo modo, l'esecuzione
richiede meno tempo. C'è un aspetto ancora più importante che coinvolge
l'efficienza del codice: anche la funzione di massa di probabilità viene
calcolata accumulandone i valori, sfruttando esplicitamente
{eq}`eq:binomial-pdf-ratio`. Calcolare la funzione di massa di probabilità
usando la formula {eq}`eq:binomial-pdf` nella relativa definizione richierebbe
ogni volta di valutare tre fattoriali e due elevamenti a potenza, che
risulterebbero nell'esecuzione di $3n$ moltiplicazioni. In questo modo si
calcola ogni valore di $f$ partendo da quello precedentemente ottenuto, al
prezzo di $4$ moltiplicazioni.

La funzione `quantiles` si può utilizzare per tabulare i quantili della
distribuzione binomiale, come fatto per esempio nella cella seguente e
relativamente al caso $n = 32$ e $p = 0.65$.

```{code-block} python

import pandas as pd

n = 32
p = 0.65
levels = np.arange(0.05, 1, 0.05)


content = []
for q, x in zip(levels, quantiles(n, p, levels)):
    content.append({'Livello': q, 'Quantile': x})

table = pd.DataFrame.from_records(content)

table.set_index('Livello')
```

Analogamente, la {numref}`fig:binomial-boxplot` mostra il diagramma a scatola
di una generica distribuzione binomiale (e se guardate nel codice nascosto
scoprirete che per produrlo viene utilizzata proprio la funzione `quantiles`),
evidenziando i valori numerici di mediana, primo e terzo quartile.Agendo sui
selettori che corrispondono ai due parametri della distribuzione è possibile
vedere come cambia il diagramma.

````{customfigure}
:name: fig:binomial-boxplot

```{code-block} python
:class: toggle-code

def bp_binomial(n, p):
    fig, ax = plt.subplots(figsize=(6, 2))

    levels = [0.25, 0.5, 0.75]
    if p < 1:
      first_quartile, median, third_quartile = quantiles(n, p, levels)
    else:
      first_quartile, median, third_quartile = [n, n, n]

    lw = 1
    height = 0.2

    ax.plot([median, median], [-height, height-.01], c='k', linewidth=2)

    ax.plot([0, 0], [-.1, .1], c='k', linewidth=lw)
    ax.plot([0, first_quartile], [0, 0], c='k', linewidth=lw)

    ax.plot([first_quartile, first_quartile], [-height, height],
            c='k', linewidth=lw)

    ax.plot([third_quartile, third_quartile], [-height, height],
            c='k', linewidth=lw)

    ax.plot([first_quartile, third_quartile], [height, height],
            c='k', linewidth=lw)
    ax.plot([first_quartile, third_quartile], [-height, -height],
            c='k', linewidth=lw)

    ax.plot([third_quartile, n], [0, 0], c='k', linewidth=lw)
    ax.plot([n, n], [-.1, .1], c='k', linewidth=lw)

    if p > 0:
        ax.text(0, -0.5, 0, ha='center')

    ax.text(median, -0.6, median, ha='center')

    if 0 < p < 1:
        ax.text(first_quartile, 0.5, first_quartile, ha='center')
        ax.text(third_quartile, 0.5, third_quartile, ha='center')

    if p < 1:
        ax.text(n, -0.5, n, ha='center')

    ax.set_xlim(-0.1, 20.1)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    # Manual rendering to avoid MathJax processing
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format='png', bbox_inches='tight', dpi=100)
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    img_buffer.close()
    
    # Display in protected div
    img_html = '<div class="no-mathjax"><img src="data:image/png;base64,' + \
               img_base64 + '" style="max-width: 100%; height: auto;" /></div>'
    Element("bp-output").write(img_html)
    
    plt.close(fig)

def update_boxplot(event=None):
    n = int(document.getElementById("n-bp-slider").value)
    document.getElementById("n-bp-value").innerText = f"{n:d}"
    p = float(document.getElementById("p-bp-slider").value)
    document.getElementById("p-bp-value").innerText = f"{p:.1f}"
    bp_binomial(n, p)


p_slider = document.getElementById("p-bp-slider")
p_slider.addEventListener("input", create_proxy(update_boxplot))

n_slider = document.getElementById("n-bp-slider")
n_slider.addEventListener("input", create_proxy(update_boxplot))

# Initial plot
bp_binomial(10, 0.5)
```
```{raw} html

<div id="boxplot-container" style="visibility: none;">
    <div class="slider-container" style="float: left;">
        <label for="n-bp-slider">\( n \): </label>
        <input type="range" id="n-bp-slider"
               min="2" max="20" value="10" step="1" />
        <span id="n-bp-value">10</span>
    </div>

    <div class="slider-container" style="float: right;">
        <label for="p-bp-slider">\( p \): </label>
        <input type="range" id="p-bp-slider"
               min="0" max="1" value="0.5" step="0.1" />
        <span id="p-bp-value">0.5</span>
    </div>

    <div id="bp-output" class="no-mathjax"
            style="clear: both; display: flex; justify-content: center; margin-bottom: 2em;">
        
    </div>
</div>
```

Diagramma a scatola del modello binomiale.
````

## Implementazione della distribuzione binomiale

```{margin}
È possibile specificare gli argomenti di `binom` in modo posizionale, avendo
cura di indicare prima $n$ e poi $p$, oppure utilizzando `n` e `p` come nomi
per gli argomenti, indipendentemente dall'ordine scelto. È in ogni caso
richiesto di specificare entrambi gli argomenti, pena l'emissione di
un'eccezione.
```
La creazione di oggetti che corrispondono a una distribuzione binomiale
viene effettuata in `scipy.stats` dalla funzione `binom`, che accetta come
argomenti i valori per i parametri $n$ e $p$ della distribuzione. Una volta
che questi oggetti sono stati creati, è possibile invocare su di essi tutti i
metodi visti nel capitolo precedente. Per esempio, nella cella seguente
vengono calcolati i decili della distribuzione binomiale di parametri
$n = 132$ e $p = 0.73$ (si tratta della stessa distribuzione di cui abbiamo
tabulato i quantili nel paragrafo precedente, e come si può verificare i
valori ottenuti coincidono con quelli equivalenti in quella tabulazione).

```{code-block} python

import scipy.stats as st

X = st.binom(n, p)

X.ppf(np.arange(0.1, 1, .1))
```


Analogamente, è possibile ottenere il grafico delle funzioni di massa di
probabilità e di ripartizione della stessa distribuzione.

```{code-block} python

fig, axes = plt.subplots(1, 2, sharey=True)

x = np.arange(-0.1, n+0.1, 0.01)
axes[0].step(x, X.cdf(x))

x = np.arange(*X.support())
axes[1].vlines(x, 0, X.pmf(x), color='k')

for ax in axes:
    ax.set_xlabel(r'$x$')

axes[1].set_xlim(10, 30)

axes[0].set_ylabel(r'$F_X$', rotation='horizontal')
axes[1].set_ylabel(r'$f_X$', rotation='horizontal')
plt.show()
```

Usando le stesse convenzioni grafiche del capitolo precedente, anche in questo
caso è possibile simulare l'osservazione di un campione di osservazioni da
una distribuzione binomiale e confrontare il grafico delle sue frequenze
relative con quello della funzione di massa di probabilità. Nella
{numref}`fig:binomial-simulation`, questo viene fatto relativamente alla stessa
distribuzione binomiale che abbiamo considerato finora, ma i selettori che
corrispondono ai due parametri permettono, nella versione interattiva, di
verificare come il grafico risultante rimanga coerente al variare dei parametri
coinvolti.

````{customfigure}
:name: fig:binomial-simulation

```{code-block} python
:class: toggle-code

import pandas as pd

def binomial_simulation(n, p, m):

    fig, ax = plt.subplots()
    X = st.binom(n, p)

    x = X.rvs(m)
    freq = pd.Series(x).value_counts(normalize=True)
    freq = freq.reindex(np.arange(0, n+1), fill_value=0)
    ax.bar(freq.index, freq.values, facecolor='lightgray', edgecolor='gray')

    x = np.arange(*X.support())
    ax.vlines(x, 0, X.pmf(x))
    ax.plot(x, X.pmf(x), 'o')

    ax.set_xlim(-1, 21)
    ax.set_ylim(0, 1.1)
    # Manual rendering to avoid MathJax processing
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format='png', bbox_inches='tight', dpi=100)
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    img_buffer.close()
    
    # Display in protected div
    img_html = '<div class="no-mathjax"><img src="data:image/png;base64,' + \
               img_base64 + '" style="max-width: 100%; height: auto;" /></div>'
    Element("sim-output").write(img_html)
    
    plt.close(fig)

def update_simulation_boxplot(event=None):
    n = int(document.getElementById("n-sim-slider").value)
    document.getElementById("n-sim-value").innerText = f"{n:d}"
    p = float(document.getElementById("p-sim-slider").value)
    document.getElementById("p-sim-value").innerText = f"{p:.1f}"
    m = int(document.getElementById("m-sim").value)

    binomial_simulation(n, p, m)


p_slider = document.getElementById("p-sim-slider")
p_slider.addEventListener("input", create_proxy(update_simulation_boxplot))

n_slider = document.getElementById("n-sim-slider")
n_slider.addEventListener("input", create_proxy(update_simulation_boxplot))

m_menu = document.getElementById("m-sim")
m_menu.addEventListener("change", create_proxy(update_simulation_boxplot))

# Initial plot
binomial_simulation(10, 0.5, 50)
```
```{raw} html

<div id="boxplot-container" style="visibility: none;">
    <div class="slider-container" style="float: left;">
        <label for="n-sim-slider">\( n \): </label>
        <input type="range" id="n-sim-slider"
               min="2" max="20" value="10" step="1" />
        <span id="n-sim-value">10</span>
    </div>

    <div class="slider-container" style="float: left; margin-left: 1em;">
        <label for="p-sim-slider">\( p \): </label>
        <input type="range" id="p-sim-slider"
               min="0" max="1" value="0.5" step="0.1" />
        <span id="p-sim-value">0.5</span>
    </div>

    <div class="slider-container" style="float: right;">
        <label for="m-sim">\( m \): </label>
        <select id="m-sim">
          <option value="5">5</option>
          <option value="50" selected>50</option>
          <option value="500">500</option>
          <option value="5000">5000</option>
        </select>
    </div>

    <div id="sim-output" class="no-mathjax"
            style="clear: both; display: flex; justify-content: center; margin-bottom: 2em;">
        
    </div>
</div>
```

Diagramma a barre delle frequenze di un insieme di osservazioni estratte da
un modello binomiale, sovrapposto al diagramma a bastoncini della
corrispondente funzione di massa di probabilità.
````


[^accumulazione]: Nell'ambito della programmazione, il termine _accumulazione_
indica una tecnica che consiste nell'ottenere il risultato di un calcolo
generando in modo separato (tipicamente, all'interno di un ciclo) una serie di
valori e aggregandoli insieme tramite un'operazione associativa, come la somma
o il prodotto. In particolare, si introduce una variabile il cui _ruolo_ è
quello di fungere da _accumulatore_, e la si inizializza all'elemento neutro
dell'operazione considerata. L'aggregazione viene fatta via via che i valori
risultano disponibili, eseguendo l'operazione applicandola a un nuovo valore e
al precedente contenuto dell'accumulatore, e assegnando il risultato a
quest'ultimo.