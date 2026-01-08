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

(sec_modello-poisson)=
# Le distribuzioni di Poisson

Consideriamo un esperimento binomiale nel quale il numero $n$ di ripetizioni
è elevato. Questo fatto non cambia la validità delle formule che descrivono
la distribuzione della variabile aleatoria $X \sim \mathrm B(n, p)$ che
conteggia il numero di successi. Consideriamo però il codice che ho introdotto
nel Paragrafo {ref}`sec_binomial-quantiles` per il calcolo dei
quantili, e che riporto qui di seguito per comodità.

```python
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

Nel corpo della funzione `quantiles`, la variabile `pdf` viene inizializzata
al valore che corrisponde a $(1 - p)^n$. Ora, se $n$ assume un valore elevato.
diciamo dell'ordine delle decine di migliaia, indipendentemente dal valore di
$p$ è ragionevole il risutato del calcolo della potenza venga memorizzato come
$0$, tenendo conto della precisione dei numeri in virgola mobile. Analoghe
considerazioni valgono per esempio per il calcolo della funzione di massa di
probabilità. In casi come questo, se il valore elevato di $n$ è in qualche
modo controbilanciato da un valore basso di $p$, è possibile introdurre una
nuova famiglia di distribuzioni che permette di approssimare quella di $X$.

In particolare, fissato $\lambda \in \mathbb R^+$ consideriamo una successione
di variabili aleatorie $X_1, X_2, \dots$, dove per ogni $n \in \mathbb N$ si
ha $X_n \sim \mathrm B(n, p_n)$ e $n p_n = \lambda$. Evitando di considerare
la funzione indicatrice sul supporto della distribuzione, per evitare di
appesantire la notazione, la funzione di massa di probabilità di una generica
variabile di questa successione è tale che

```{math}
\begin{align*}
f_{X_n}(x; n, p_n) &= \binom{n}{x} p_n^x (1-p_n)^{n-x} \\
     &= \frac{n \cdot (n-1) \cdot \dots \cdot (n - x + 1)}{x!}
        \left( \frac{\lambda}{n} \right)^x 
        \frac{\left(1 - \frac{\lambda}{n}\right )^n}
             {\left(1 - \frac{\lambda}{n}\right )^x} \\
     &= \frac{n}{n} \cdot \dots \frac{n - x + 1}{n}
        \frac{\lambda^x}{x!}
        \frac{\left(1 - \frac{\lambda}{n}\right )^n}
             {\left(1 - \frac{\lambda}{n}\right )^x} \enspace.
\end{align*}
```

Se ora consideriamo il limite per $n \to +\infty$,

- ognuna delle prime $n-x$ frazioni tende a $1$,
- il numeratore dell'ultima funzione tende a $\mathrm e^{-\lambda}$, e
- il suo denominatore tende a $1$,

e dunque la successione delle funzioni di massa di probabilità ha come limite
puntuale la seguente funzione

```{math}
f(x; \lambda) = \mathrm e^{-\lambda} \frac{\lambda^x}{x!}
                \mathrm I_{\mathbb N \cup \{ 0 \}}(x) \enspace.
```

Va notato che questa funzione è la funzione di massa di probabilità di una
qualche distribuzione, essendo i sui valori sempre non negativi e valendo

```{margin}
In questa catena di uguaglianze, l'ultima serie corrisponde alla serie di
Taylor della funzione $g(u) = \mathrm e^u$ centrata in $0$.
```
```{math}
\sum_{x=0}^{+\infty} f(x; \lambda) = \mathrm e^{-\lambda}
         \sum_{x=0}^{+\infty} \frac{\lambda^x}{x!}
         = \mathrm e^{-\lambda} \cdot \mathrm e^{\lambda} = 1 \enspace.
```

Pertanto, la successione delle distribuzioni binomiali nella quale il
parametro $n$ cresce e, contemporaneamente, il parametro $p$ diminuisce
in modo che il prodotto dei due parametri sia costante converge a un nuovo
tipo di distribuzione, che viene detta distribuzione di Poisson. La
corrispondente famiglia di distribuzioni è descritta in modo formale nella
definizione che segue.

````{prf:definition} La famiglia delle distribuzioni di Poisson
Fissato $\lambda \in \mathbb R^+$, la distribuzione definita dalla funzione
di massa di probabilità

```{math}
f(x; \lambda) = \mathrm e^{-\lambda} \frac{\lambda^x}{x!}
                \mathrm I_{\mathbb N \cup \{ 0 \}}(x)
```

è detta _distribuzione di Poisson_ di parametro $\lambda$, e userò la
notazione $X \sim \mathrm P(\lambda)$ per indicare che una variabile aleatoria
$X$ segue una siffatta distribuzione. La _famiglia delle distribuzioni di
Poisson_ è definita come l'insieme di tutte queste distribuzioni, al variare
dei possibili valori del corrispondente parametro $\lambda$.
````


Per analizzare il generico andamento della funzione funzione di massa di
probabilità $f_X$ di una generica variabile aleatoria
$X \sim \mathrm P(\lambda)$, vale la pena studiare il rapporto $\rho$ tra i
valori che essa assume per due valori successivi della relativa
specificazione:

```{math}
\rho = \frac{f_X(x+1; \lambda)}{f_X(x; \lambda)}
     = \mathrm e^{-\lambda} \frac{\lambda^x}{x!}
       \mathrm e^\lambda \frac{\lambda^{x+1}}{(x+1)!}
     = \frac{\lambda}{x + 1} \enspace,
```

così che:

- $\rho > 1$, e quindi $f_X(x+1; \lambda) > f_X(x; \lambda)$,
  se e solo se $x < \lambda - 1$,
- $\rho = 1$, che equivale a $f_X(x+1; \lambda) = f_X(x; \lambda)$,
  se e solo se $x = \lambda - 1$,
- $\rho < 1$ nei casi rimanenti.

```{code-cell} python
:tags: [hide-input]

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

def poisson_graph(lambda_, ax):
    n = 10
    x = np.arange(0, n+1)

    X = st.poisson(lambda_)
    ax.vlines(x, 0, X.pmf(x))
    ax.plot(x, X.pmf(x), 'o')

fig, axes = plt.subplots(1, 3, sharey=True, figsize=(8, 4))

for lambda_, ax in zip([0.9, 2.7, 3], axes):
    poisson_graph(lambda_, ax)
    ax.set_yticks([0.1, 0.2, 0.3, 0.4])
    ax.set_xlabel(fr'$\lambda = {lambda_!r}$')
fig
```
````{customfigure}
:name: fig_poisson_template

Grafici della funzione di massa di probabilità per le distribuzioni di Poisson
di parametro $0.9$ (sinistra), $2.7$ (centro) e $3$ (destra).
````

Tenuto conto del fatto che le specificazioni $x$ assumono valori interi non
negativi, da queste relazioni si ricava che in funzione di $\lambda$ si hanno
tre differenti situazioni possibili, illustrate in
{numref}`fig_poisson_template`:

- se $\lambda \not\in \mathbb N$ e $\lambda < 1$, $f_X(0; \lambda)$
  rappresenta il massimo valore di massa di probabilità, la relativa funzione
  è strettamente decrescente e $0$ è la moda della distribuzione;

```{raw} html
<div class="margin">
```
```{code-cell} python
:tags: [hide-input]

lambda_ = 2.2
i = 2

fig,ax = plt.subplots(figsize=(5, 1))

ax.plot([i-1.5, i+1.5], [0, 0], 'k')

ax.set_xticks([])
ax.set_yticks([])

s  = -1
spacing = {-1: -.4, 1: .2}
for x, l in zip([i-1, lambda_-1, i, lambda_, i+1],
                [r'$i-1$', r'$\lambda - 1$', r'$i$', r'$\lambda$', r'$i+1$']):
    ax.plot([x] * 2, [-.1, .1], 'k')
    ax.text(x, spacing[s], l, ha='center', fontsize=18)
    s *= -1

ax.set_ylim([-.5, .5])
ax.axis('off')
fig
```
```{raw} html
</div>
```
````{margin}

L'ultimo valore intero per il quale $\rho > 1$ è
$i - 1 = \lfloor \lambda -1 \rfloor$, pertanto la moda coincide con l'intero
successivo, e quest'ultimo è uguale a
$i = \lceil \lambda - 1 \rceil = \lfloor \lambda \rfloor.$
````

- quando $\lambda \not\in \mathbb N$ ma $\lambda > 1$, la funzione di massa di
  probabilità è inizialmente crescente e ha un massimo nel valore modale
  $\lceil \lambda \rceil$ (come evidenziato nella nota a margine;
- quando $\lambda \in \mathbb N$ la situazione è simile al punto precedente,
  ma in questo caso vi sono due valori modali: $\lambda - 1$ e $\lambda$.


Così come nel caso della distribuzione binomiale, non è possibile esprimere
analiticamente la funzione di ripartizione $F_X$ se non in termini di una
somma che coinvolge la funzione di massa di probabilità:

```{math}
F_X(x; \lambda) = \mathrm e^{-\lambda}
                  \sum_{y=0}^{\lfloor x \rfloor} \frac{\lambda^y}{y!}
                  \mathrm I_{\mathbb N \cup \{ 0 \}}(x) \enspace.
```

La {numref}`fig_poisson_pdf_cdf` mostra la sovrapposizione delle funzioni di
massa di probabilità e di ripartizione di una generica distribuzione di
Poisson. Nella versione interattiva del libro è possibile modificare il valore
di $\lambda$ e visualizzare interattivamente come cambiano i grafici delle due
funzioni.

````{customfigure}
:name: fig_poisson_pdf_cdf
:class: left-align

```{interactive-code} python
:tags: [toggle-code] 

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from pyscript import display
from pyscript.web import page, when

fig_1, ax_1 = plt.subplots()

lambda_1 = float(page['#lambda'][0].value)
P_1 = st.poisson(lambda_1)

x_1 = np.arange(0, 11)
y_1 = P_1.pmf(x_1)

cdf_y = [0] + list(P_1.cdf(x_1))
cdf_xmin = list(range(-1, 11))
cdf_xmax = list(range(0, 11)) + [20]
cdf = ax_1.hlines(cdf_y, cdf_xmin, cdf_xmax)
pmf_lines = ax_1.vlines(x_1, 0, y_1, color='k')
pmf_dots = ax_1.plot(x_1, y_1, 'o')[0]

ax_1.set_xlabel('$x$', fontsize=12, ha='right')
ax_1.set_ylabel('$f, F$', fontsize=12, rotation=0)
ax_1.set_xlim(-1, 11)
ax_1.set_ylim(0, 1.1)
ax_1.set_xticks(range(0, 12, 2))

@when("input", "#lambda")
def poisson_plot(event):
    lambda_1 = float(page['#lambda'][0].value)
    page['#lambda-value'][0].innerHTML = f'{lambda_1:.1f}'

    P_1 = st.poisson(lambda_1)

    x_1 = np.arange(0, 11)
    y_1 = P_1.pmf(x_1)

    cdf_y = [0] + list(P_1.cdf(x_1))
    cdf_xmin = list(range(-1, 11))
    cdf_xmax = list(range(0, 11)) + [20]
    cdf_segments = [[[xmin, y_val], [xmax, y_val]] 
                    for y_val, xmin, xmax in zip(cdf_y, cdf_xmin, cdf_xmax)]

    cdf.set_segments(cdf_segments)
    
    # Update PMF vertical lines
    pmf_segments = [[[xi, 0], [xi, yi]] for xi, yi in zip(x_1, y_1)]
    pmf_lines.set_segments(pmf_segments)

    pmf_dots.set_data(x_1, y_1)
    
    display(fig_1, target='graph-%this%', append=False)


display(fig_1, target='graph-%this%', append=False)
```
```{raw} html

<div class="plot-container">
    <div class="model-slider-container">
        <label for="lambda">\( \lambda \): </label>
        <input type="range" id="lambda"
               min="0" max="10" value="0.5" step="0.01" />
        <span id="lambda-value">0.5</span>
    </div>
</div>
```

Grafico delle funzioni di massa di probabilità e di ripartizione del modello
di Poisson.
````

```{figure} http://www.sil.si.edu/digitalcollections/hst/scientific-identity/fullsize/SIL14-P005-06a.jpg
---
figclass: margin
name: fig_simeon-poisson
width: 200px
align: left
---
Ritratto di Siméon Denis Poisson (immagine di pubblico dominio, disponibile su
wikimedia).
```
````{admonition} Nomenclatura
:class: naming

La distribuzione di Poisson prende il suo nome da quello del matematico e
fisico francese Siméon Denis Poisson, ritratto nella
{numref}`Figura %s <fig_simeon-poisson>`. In effetti, tale distribuzione è
descritta nel suo libro «Recherches sur la probabilité des jugements en matière
criminelle et en matière civile» pubblicato nel 1837, sebbene fosse già
presente nell'articolo scientifico «Probabilitate Eventuum in Ludis a Casu
Fortuito Pendentibus» pubblicato nel 1711 da un altro matematico francese,
Abraham de Moivre. Come per il caso della distribuzione di Bernoulli, è
relativamente frequente l'uso dell'aggettivo «poissoniano» per indicare
questa distribuzione, così come i concetti matematici a essa collegati.
````

## Valore atteso e varianza della distribuzione di Poisson

Abbiamo visto come una distribuzione di Poisson di parametro $\lambda$ sia il
risultato della convergenza di una successione di distribuzioni binomiali di
parametri $n$ e $p_n$, ognuna caratterizzata dalla relazione
$n p_n = \lambda$. Essendo pertanto il valore atteso di ognuna di queste
distribuzioni esattamente uguale a $\lambda$, è ragionevole aspettarsi che
lo stesso valga per la distribuzione di Poisson che rappresenta il limite
della successione. Ciò è quello che effettivamente accade, come dimostrato
nel seguente teorema.

````{prf:theorem}
:label: teo-poisson-mean

Dati $\lambda \in \mathbb R^+$ e $X \sim \mathrm P(\lambda)$,
$\mathbb E(X) = \lambda$.
````
````{admonition} _
:class: myproof
Applicando la definizione di valore atteso di variabile aleatoria si ottiene

```{math}
\begin{align*}
\mathbb E(X) &= \sum_{x=0}^{+\infty}x f_X(x)
              = \lambda \mathrm e^{-\lambda }\sum_{x=0}^{+\infty}
                                            x \frac{\lambda^{x-1}}{x!}
              = \lambda \mathrm e^{-\lambda }\sum_{x=1}^{+\infty}
                                            \frac{\lambda^{x-1}}{(x-1)!} \\
             &=  \lambda \mathrm e^{-\lambda }\sum_{y=0}^{+\infty}
                                            \frac{\lambda^y}{y!}
              = \lambda \mathrm e^{-\lambda } \mathrm e^\lambda
              = \lambda \enspace,
\end{align*}
```

dove nel terzo passaggio l'indice $x=0$ è omesso dalla sommatoria perché
l'addendo corrispondente è nullo, e nel quarto passaggio è stata applicata
la trasformazione $y = x - 1$. 
````

Il valore della varianza in una distribuzione di Poisson non si riesce a
ottenere in modo altrettanto intuitivo, ed è necessario calcolarlo in modo
formale, per esempio nel modo descritto dal seguente teorema.

````{prf:theorem}
:label: teo-poisson-variance

Dati $\lambda \in \mathbb R^+$ e $X \sim \mathrm P(\lambda)$,
$\mathrm{Var}(X) = \lambda$.
````
````{admonition} _
:class: myproof
Il momento secondo della distribuzione è uguale a

```{math}
\begin{align*}
\mathbb E\left( X^2 \right)
   &= \sum_{x=0}^{+\infty}x^2 f_X(x)
    = \lambda \mathrm e^{-\lambda }\sum_{x=0}^{+\infty}
                                   x^2 \frac{\lambda^{x-1}}{x!}
    = \lambda \mathrm e^{-\lambda }\sum_{x=1}^{+\infty}
                                   x \frac{\lambda^{x-1}}{(x-1)!} \\
   &=  \lambda \mathrm e^{-\lambda }\sum_{y=0}^{+\infty}
                                    (y + 1) \frac{\lambda^y}{y!}
    = \lambda \underbrace{
           \mathrm e^{-\lambda }\sum_{y=0}^{+\infty} y \frac{\lambda^y}{y!}
         }_{
           =\mathbb E(X) = \lambda
         }
      + \lambda \mathrm e^{-\lambda } \underbrace{
              \sum_{y=0}^{+\infty} \frac{\lambda^y}{y!}}_{= \mathrm e^\lambda}
    = \lambda^2 + \lambda \enspace.
\end{align*}
```

Pertanto la varianza della distribuzione sarà $\mathrm{Var}(X) =
\mathbb E\left( X^2 \right) - \mathbb E(X) ^2 = \lambda^2 + \lambda - \lambda^2
= \lambda$.
````

## Momenti della distribuzione di Poisson (*)

La funzione generatrice dei momenti di una generica distribuzione di Poisson
ha una particolare forma, nella quale compare un doppio elevamento a potenza,
come ottenuto nel seguente risultato.

```{margin}
Nella formula, $\mathrm{exp}(t)$ è una notazione alternativa per indicare
$\mathrm e^t$. In questo modo si evita di utilizzare un doppio apice, che
rischia di risultare poco leggibile.
```
````{prf:theorem}
Dato $\lambda \in \mathbb R^+$, la funzione generatrice dei momenti di una
variabile aleatoria $X \sim \mathrm P(\lambda)$ assume la seguente forma:

```{math}
m_X(t) = \mathrm e^{-\lambda} \mathrm{exp}\left( \lambda \mathrm e^t \right)
         \enspace.
```
````
````{admonition} _
:class: myproof
Dalla definizione di funzione generatrice dei momenti si ottiene

```{math}
m_X(t) = \mathbb E \left( \mathrm e^{tX} \right)
       = \sum_{x=0}^{+\infty}\mathrm e^{tx} \mathrm e^{-\lambda}
                             \frac{\lambda^x}{x!}
       = \mathrm e^{-\lambda} \sum_{x=0}^{+\infty}
                  \frac{\left(\lambda \mathrm e^t \right)^x}{x!}
       = \mathrm e^{-\lambda} \mathrm{exp}\left( \lambda \mathrm e^t \right)
         \enspace,
```

dove il valore della somma infinita è ottenuto considerando lo sviluppo in
serie di Taylor dell'elevamento alla potenza di $\mathrm e$, centrata in $0$.
````

La particolare forma analitica della funzione generatrice dei momenti
permette di dimostrare che la distribuzione di Poisson è _riproducibile_,
come dettagliato nel seguente teorema.

```{prf:theorem}
:label: teo-poisson-reproducibility

Dati $n \in \mathbb N$ e $\lambda_1, \dots, \lambda_n \in \mathbb R^+$,
per ogni $i = 1, \dots, n$ sia $X_i \sim \mathrm P(\lambda_i)$. Se le
variabili aleatorie appena definite sono tra loro indipendenti, allora
$Y \coloneqq \sum_{i=1}^n X_i \sim \mathrm P(\sum_{i=1}^n \lambda_i)$.
```
````{admonition} _
:class: myproof
L'indipendenza delle $X_i$ permette di esprimere la funzione generatrice dei
momenti di $Y$ come prodotto di quelle delle $X_i$:

```{math}
m_Y(t) = \prod_{i=1}^n \mathrm e^{-\lambda_i}
         \mathrm{exp}\left( \lambda_i \mathrm e^t \right)
       = \mathrm e^{-\sum_{i=1}^n\lambda_i}
         \mathrm{exp}\left(\mathrm e^t \sum_{i=1}^n \lambda_i \right)\enspace,
```

e il risultato ottenuto coincide con la funzione generatrice dei momenti di
una distribuzione di Poisson di parametro $\sum_{i=1}^n \lambda_i$.
````

Il calcolo delle derivate di $m_X$ si può esprimere in un'elegante forma
ricorrente, infatti

```{math}
\begin{align*}
m'_X(t)      &= \lambda \mathrm e^{-\lambda}
                \mathrm{exp}\left( \lambda \mathrm e^t \right) \mathrm e^t
              = \lambda \mathrm e^t m_X(t) \enspace, \\
m''_X(t)     &= \lambda \mathrm e^t m_X(t) + \lambda \mathrm e^t m'_X(t)
              = \lambda \mathrm e^t \left(m_X(t) + m'_X(t) \right) \enspace, \\
m'''_X(t)    &= \lambda\mathrm e^t \left(m_X(t) + 2m_X'(t) + m''_X(t)\right)
                \enspace, \\
m^{(4)}_X(t) &= \lambda\mathrm e^t \left(m_X(t) + 3m_X'(t)
                                   + 3m''_X(t) + m'''_X(t)\right) \enspace,
\end{align*}
```

e più in generale

```{math}
m^{(n)}_X(t) = \lambda\mathrm e^t \sum_{i=0}^n \binom{n}{i}m^{(i)}m_X(t)
               \enspace.
```

Calcolando le prime due derivate in zero si ottengono i primi due momenti:
$\mu'_1 = \lambda$ e $\mu'_2 = \lambda + \lambda^2$, in coerenza con quanto
abbiamo già visto per il calcolo di media e varianza di questa distribuzione.
I successivi due momenti sono

```{math}
\begin{align*}
\mu'_3 &= m'''_X(0) = \lambda^3 + 3 \lambda^2 + \lambda \enspace, \\
\mu'_4 &= m^{(4)}_X(0) = \lambda^4 + 6 \lambda^3 + 7 \lambda^2 + \lambda
          \enspace.
\end{align*}
```

Per calcolare i momenti centrali, introduciamo $Y \coloneqq X - \lambda$ e
calcoliamo le derivate della funzione generatrice dei momenti di $Y$
applicando il {prf:ref}`teo-central-moments`:

```{math}
\begin{align*}
m'_Y(t)      &= \mathrm e^{-\lambda t} \left( m'_X(t) -
                                          \lambda m_X(t) \right) \enspace, \\
m''_Y(t)     &= \mathrm e^{-\lambda t} \left( m''_X(t) - 2\lambda m'_X(t) +
                                        \lambda^2 m_X(t) \right) \enspace, \\
m'''_Y(t)    &= \mathrm e^{-\lambda t} \left( m'''_X(t) - 3\lambda m''_X(t) +
                    3\lambda^2 m'_X(t) -\lambda^3 m_X(t) \right) \enspace, \\
m^{(4)}_Y(t) &= \mathrm e^{-\lambda t} \left( m^{(4)}_X(t) -
                                4\lambda m'''_X(t) + 6\lambda^2 m''_X(t) -
                                4\lambda^3 m'_X(t) +
                                \lambda^4 m_X(t) \right) \enspace. \\
\end{align*}
```

Azzerando le prime due quantità si ottiene, come atteso, $0$ (il valore
atteso di una variabile aleatoria alla quale è stato sottrato il suo valore
atteso) e $\lambda$ (la varianza della distribuzione di Poisson). Azzerando
le rimanenti due si ottengono i relativi momenti centrali:

```{math}
\begin{align*}
\mu_3 &= \lambda \enspace, \\
\mu_4 &= \lambda + 3 \lambda^3 \enspace,
\end{align*}
```

e pertanto la skewness della distribuzione di Poisson è uguale a

```{math}
\frac{\mu_3}{\sigma^3} = \frac{\lambda}{\lambda \sqrt{\lambda}}
                       = \frac{1}{\sqrt{\lambda}} \enspace,
```

che risulta sempre positiva, riflettendo il fatto che indipendentemente dal
valore del suo parametro, la massa di probabilità della distribuzione è
concentrata in modo relativamente vicino a $0$, ma è sempre presente una
coda infinita a destra. Analogamente, la curtosi è

```{math}
\frac{\mu_4}{\sigma^4} - 3 = \frac{\lambda + 3 \lambda^3}{\lambda^2} - 3
                           = \frac{1}{\lambda} \enspace,
```

che anche in questo caso è un valore positivo: la distribuzione di Poisson è
dunque sempre leptocurtica, e la ragione è dovuta alla presenza della coda a
destra che non è controbilanciata da un'analoga coda a sinistra. Va anche
sottolineato che la curtosi è per questa distribuzione sempre uguale al
quadrato della skewness, e ciò facilita la scrittura del codice alla base
della {numref}`fig_poisson-sk-plot` che illustra il grafico
skewness-curtosi per la famiglia delle distribuzioni di Poisson.

```{code-cell} python
:tags: [hide-input]

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

skewness = np.linspace(0.001, 10, 500)
kurtosis = skewness**2
ax.plot(skewness, kurtosis)
fig
```
````{customfigure}
:name: fig_poisson-sk-plot


Il grafico skewness-curtosi per la famiglia delle distribuzioni di Poisson.
````