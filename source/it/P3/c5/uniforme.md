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

(sec_modello-uniforme-discreto)=
# Le distribuzioni uniformi discrete

Dopo quello di Bernoulli, l'esperimento casuale più semplice è molto
probabilmente quello in cui $\Omega$ contiene un numero finito di esiti
caratterizzati dal fatto che la probabilità dei relativi eventi elementari
è costante. Abbiamo visto come il relativo spazio di probabilità, che viene
per ovvie ragioni detto _equiprobabile_, permette di modellare varie
situazioni del mondo reale come ad esempio quelle relative a molti giochi
d'azzardo. In questi casi, posto $\Omega = \{ e_1, \dots, e_n\}$, la variabile
aleatoria $X: \Omega \to \{ 1, \dots, n \}$ tale che $X(e_i) = i$ per ogni
$i = 1, \dots, n$, che dunque associa agli esiti un numero intero progressivo
partendo da $1$, è caratterizzata da una distribuzione appartenente alla
famiglia _uniforme discreta_, definita qui di seguito.

````{prf:definition}
:label: def-disc-unif-distribution

Fissato $n \in \mathbb N$, la distribuzione _uniforme discreta_ di parametro
$n$ è definita dalla funzione di massa di probabilità

```{math}
f(x; n) = \frac{1}{n} \mathrm I_{\{1, \dots n\}}(x) \enspace.
```

Per indicare che una variabile aleatoria $X$ segue una siffatta distribuzione
utilizzerò la notazione $X \sim \mathrm U(N)$. L'insieme di tutte le
distribuzioni uniformi discrete al variare del relativo parametro prende il
nome di _famiglia delle distribuzioni uniformi continue_.
````

Chiaramente, l'equiprobabilità degli esiti nell'esperimento casuale che
origina una variabile aleatoria uniforme discreta si riflette
nell'equiprobabilità per le corrispondenti specificazioni. Come conseguenza,
la funzione di ripartizione aumenta in modo costante, tenendo conto del suo
andamento costante a tratti.

````{prf:theorem}
:label: teo-disc-unif-cdf

Datpo $n \in \mathbb N$, la funzione di ripartizione di una variabile
aleatoria $X \sim \mathrm U(n)$ è tale che

```{math}
F_X(x; n) = \frac{\lfloor x \rfloor}{n} \mathrm I_{[1, n)}(x) +
            \mathrm I_{[n, +\infty)}(x) \; \forall x \in \mathbb R
            \enspace.
```
````
````{admonition} _
:class: myproof

Chiaramente, per ogni $x < 1 $ si ha $F_X(x; n) = 0$ in quanto l'evento
$X \leq x$ ha probabilità nulla, tenuto conto del fatto che le specificazioni
della distribuzione uniforme discreta partono da $1$. Sempre a causa del fatto
che le specificazioni sono numeri interi, inoltre, per ogni $x \in [1, n]$
gli eventi $X \leq x$ e $X \leq \lfloor x \rfloor$ sono equivalenti e dunque
hanno la stessa probabilità, per cui

```{math}
F_X(x; n) = \mathbb P(X \leq \lfloor x \rfloor) =
            \sum_{i \leq \lfloor x \rfloor} f_X(i; n) =
            \sum_{i = 1}^{\lfloor x \rfloor} \frac{1}{n} =
            \frac{\lfloor x \rfloor}{n} \enspace.
```

Infine, per ogni $x > 1$ si ha $F_X(x; n) = 1$ in quanto $x$ è maggiore della
massima specificazione della variabile aleatoria. Mettendo insieme questi
tre casi si ottiene la tesi.
````

## Valore atteso e varianza della distribuzione uniforme discreta

Il valore atteso e la varianza per le distribuzioni appartenenti alla famiglia
uniforme discreta si calcolano in modo abbastanza semplice, sfruttando alcune
sommatorie notevoli.

````{prf:theorem}
:label: teo-unif-disc-expected-value

Dato $n \in \mathbb N$ e una variabile aleatoria $X \sim \mathrm U(n)$,

```{math}
\mathbb E(X) = \frac{n+1}{2} \enspace.
```
````
````{admonition} _
:class: myproof

Applicando la definizione di valore atteso si ha

```{math}
\mathbb E(X) = \sum_{x=1}^n x f_X(x; n)
             = \sum_{x=1}^n \frac{x}{n}
             = \frac{1}{n} \sum_{x=1}^n x
             = \frac{1}{n} \frac{n(n+1)}{2}
             = \frac{n+1}{2} \enspace,
```

dove il penultimo passaggio sfrutta la formula nota {eq}`eq_sum-pow-1`.
````

In modo analogo si calcola anche la varianza di questa distribuzione.

````{prf:theorem}
:label: teo-unif-disc-var

Dato $n \in \mathbb N$ e una variabile aleatoria $X \sim \mathrm U(n)$,

```{math}
\mathrm{Var}(X) = \frac{n^2-1}{12} \enspace.
```
````
````{admonition} _
:class: myproof

Il momento secondo si calcola in modo analogo al valore atteso:

```{math}
\mathbb E\left( X^2 \right) = \sum_{x=1}^n x^2 f_X(x; n)
                            = \sum_{x=1}^n \frac{x^2}{n}
                            = \frac{1}{n} \sum_{x=1}^n x^2
                            = \frac{1}{n} \frac{n(n+1)(2n + 1)}{6}
                            = \frac{(n+1)(2n + 1)}{6} \enspace,
```

dove il penultimo passaggio si basa sull'applicazione di {eq}`eq_sum-pow-2`.
Applicando a questo punto {eq}`eq_var-alternative` si ottiene

```{math}
\begin{align*}
\mathrm{Var}(X) &= \mathbb E\left( X^2 \right) - \mathbb E(X)^2
                 = \frac{(n+1)(2n + 1)}{6} - \left( \frac{n+1}{2} \right)^2 \\
                &= \frac{n+1}{2} \left(\frac{2n+1}{3} - \frac{n+1}{2} \right)
                 = \frac{n+1}{2} \frac{4n + 2 - 3n - 3}{6}
                 = \frac{(n+1)(n-1)}{12} \enspace,
\end{align*}
```

da cui si ottiene la tesi.
````

Come nel caso delle altre distribuzioni discrete, i grafici delle funzioni
di massa di probabilità e di ripartizione corrispondono rispettivamente a
un grafico a bastoncini e alla visualizzazione di una funzione costante a
tratti, come mostrato in {numref}`fig_discrete-uniform-pdf-cdf`.
Anche in questo caso, è possibile modificare il
valore di $n$ per visualizzare come cambiano questi due grafici.

````{customfigure}
:name: fig_discrete-uniform-pdf-cdf
:class: left-align

```{interactive-code} python
:tags: [toggle-code] 

import matplotlib.pyplot as plt
import numpy as np
from pyscript import display
from pyscript.web import page, when


n_1 = int(page['#n'][0].value)

x_1 = np.arange(1, n_1 + 1)
y_1 = np.ones(n_1) / n_1
cdf_1 = y_1.cumsum()

fig_1, ax_1 = plt.subplots()

cdf_y = [0] + list(cdf_1)
cdf_xmin = list(range(0, n_1 + 1))
cdf_xmax = list(range(1, n_1 + 1)) + [20]
cdf = ax_1.hlines(cdf_y, cdf_xmin, cdf_xmax)
pmf_lines = ax_1.vlines(x_1, 0, y_1, color='k')
pmf_dots = ax_1.plot(x_1, y_1, 'o')[0]

ax_1.set_xlabel('$x$', fontsize=12, ha='right')
ax_1.set_ylabel('$f, F$', fontsize=12, rotation=0)
ax_1.set_xlim(-1, 21)
ax_1.set_ylim(0, 1.1)
ax_1.set_xticks(range(0, 21, 2))

@when("input", "#n")
def uniform_plot(event):
    n_1 = int(page['#n'][0].value)
    page['#n-value'][0].innerHTML = f'{n_1}'

    x_1 = np.arange(1, n_1 + 1)
    y_1 = np.ones(n_1) / n_1
    cdf_1 = y_1.cumsum()

    cdf_y = [0] + list(cdf_1)
    cdf_xmin = list(range(0, n_1 + 1))
    cdf_xmax = list(range(1, n_1 + 1)) + [20]
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
        <label for="n">\( n \): </label>
        <input type="range" id="n"
               min="1" max="20" value="10" step="1" />
        <span id="n-value">10</span>
    </div>
</div>
```

I grafici delle funzioni di massa di probabilità e di ripartizione per il
modello uniforme discreto.
````


## Momenti della distribuzione uniforme discreta (*)

Dato $n \in \mathbb N$, per ogni $t \in \mathbb R$ vale

```{margin}
Nella prima uguaglianza, ho applicato la trasformazione $j = x - 1$ agli
indici della sommatoria.
```
```{math}
\sum_{x=1}^n \mathrm e^{t x} = \sum_{j=0}^{n-1} \mathrm e^{t(j+1)}
                             = \mathrm e^t \sum_{j=0}^{n-1} \mathrm e^{t j}
                             = \mathrm e^t \sum_{j=0}^{n-1}
                                   \left(\mathrm e^t \right)^j \enspace.
```

L'ultima sommatoria ottenuta rappresenta la somma parziale della serie
geometrica, pertanto

```{math}
\sum_{x=1}^n \mathrm e^{t x}
     = \mathrm e^t \frac{1 - \left(\mathrm e^{t}\right)^n}{1 - \mathrm e^t}
     = \mathrm e^t \frac{1 - \mathrm e^{n t}}{1 - \mathrm e^t} \enspace.
```

La funzione generatrice dei momenti di una variabile aleatoria
$X \sim \mathrm U(n)$ è quindi individuata da

```{math}
m_X(t) = \mathbb E \left( \mathrm e^{tX} \right)
       = \sum_{x=1}^n \frac{1}{n} \mathrm e^{t x}
       = \frac{\mathrm e^t \left( 1 - \mathrm e^{n t} \right)}
              {n \left( 1 - \mathrm e^t \right)} \enspace.
```

Nel caso delle distribuzioni uniformi continue, in realtà, calcolare i momenti
utilizzando la corrispondente funzione generatrice risulta abbastanza scomodo,
perché calcolare le derivate di quest'ultime non è particolarmente agevole.
Diventa invece relativamente meno complesso applicare direttamente le
definizioni di momento e di momento centrale. Per quanto riguarda la prima
categoria di momenti si avrà quindi, per ogni $i \in \mathbb N$,

```{math}
\mu'_i = \mathbb E \left( X^i \right) = \sum_{x=1}^n \frac{1}{n} x^i
          = \frac{1}{n} \sum_{x=1}^n x^i \enspace,
```

da cui segue immediatamente, ricordando le formule da {eq}`eq_sum-pow-1` a
{eq}`eq_sum-pow-4`,

```{math}
\begin{align*}
\mu'_1 &= \frac{1}{n} \sum_{x=1}^n x = \frac{1}{n} \frac{n (n+1)}{2}
        = \frac{n+1}{2} \enspace, \\
\mu'_2 &= \frac{1}{n} \sum_{x=1}^n x^2 = \frac{1}{n} \frac{n(n+1)(2n + 1)}{6}
        = \frac{(n+1)(2n + 1)}{6} \enspace, \\
\mu'_3 &= \frac{1}{n} \sum_{x=1}^n x^3 = \frac{1}{n} \frac{n^2(n+1)^2}{4}
        = \frac{n(n+1)^2}{4} \enspace, \\
\mu'_4 &= \frac{1}{n} \sum_{x=1}^n x^4
        = \frac{1}{n} \frac{n(n+1)(2n + 1)(3n^2 + 3n - 1)}{30}
        = \frac{(n+1)(2n + 1)(3n^2 + 3n - 1)}{30} \enspace.
\end{align*}
```

Anche il calcolo del momento centrale $i$-esimo si può effettuare in modo
relativamente agevole, calcolando direttamente
$\mathbb E\left( \left( X - \frac{n+1}{2} \right)^i \right)$ e ottenendo

```{margin}
Questi calcoli sono abbastanza lunghi (soprattutto per quanto riguarda
$\mu_4$), ma richiedono solo di armarsi di pazienza e di fare riferimento,
come per i momenti, alle formule note che calcolano la somma dei primi $n$
numeri elevati alle potenze che vanno da uno a quattro.
```
```{math}
\begin{align*}
\mu_1 &= \frac{1}{n} \sum_{x=1}^n \left( x - \frac{n+1}{2} \right)
       = \frac{1}{n}\frac{n(n+1)}{2} - \frac{n+1}{2}
       = 0 \enspace, \\
\mu_2 &= \frac{1}{n} \sum_{x=1}^n \left( x - \frac{n+1}{2} \right)^2
       = \frac{1}{n} \sum_{x=1}^n x^2 - \frac{n+1}{n} \sum_{x=1}^n x
         + \frac{(n+1)^2}{4} \\
      &= \frac{(n+1)(2n+1)}{6} - \frac{(n+1)^2}{2} + \frac{(n+1)^2}{4}
       = \frac{n^2 - 1}{12} \enspace, \\
\mu_4 &= \frac{1}{n} \sum_{x=1}^n \left( x - \frac{n+1}{2} \right)^4 \\
      &= \frac{1}{n} \sum_{x=1}^n x^4 - 2 \frac{n+1}{n} \sum_{x=1}^n x^3
         + \frac{6}{n} \left( \frac{n+1}{2} \right)^2 \sum_{x=1}^n x^2
         - \frac{4}{n} \left( \frac{n+1}{2} \right)^3 \sum_{x=1}^n x
         + \left( \frac{n+1}{2} \right)^4 \\
      &= \frac{(n+1)(2n+1)(3n^2+3n-1)}{30} - \frac{n(n+1)^3}{2}
         + \frac{(n+1)^2(2n+1)}{2} - \frac{(n+1)^4}{4} + \frac{(n+1)^4}{16} \\
      &= \frac{(n^2 - 1)(3n^2 - 7)}{240} \enspace.
\end{align*}
```

La seconda uguaglianza conferma quanto già sappiamo relativamente alla
varianza della distribuzione. Non ho calcolato il momento centrale  terzo
perché la distribuzione è chiaramente simmetrica attorno al suo valore atteso
e quindi questo momento si annulla, così come è nulla la _skewness_ della
distribuzione. Il quarto momento permette infine di ottenere che la curtosi
della distribuzione è

```{math}
\frac{\mu_4}{\sigma^4} - 3
    = \frac{(n^2 - 1)(3n^2 - 7)}{240} \frac{144}{n^2 - 1} - 3
    = \frac{6(3n^2 - 7)}{10(n^2 - 1)} - 3
    = -\frac{6}{5} \frac{n^2 + 1}{n^2 - 1} \enspace,
```

che è negativa per ogni intero $n > 1$. Escludendo quindi il caso $n=1$, nel
quale peraltro la distribuzione degenera in una costante, le distribuzioni
uniformi discrete sono sempre bradicurtiche: se confrontate con una
distribuzione normale di pari valore atteso e varianza, tendono a produrre meno
valori fuori scala. Questa cosa è abbastanza ovvia, tenuto conto del fatto che,
a differenza di quella normale, la distribuzione uniforme discreta ha un
supporto finito. La figura {numref}`fig_discrete-uniform-sk-graph` mostra il
grafico skewness-curtosi per la famiglia delle distribuzioni uniformi discrete.

```{code-cell} python
:tags: [remove-cell]
import matplotlib.pyplot as plt
import numpy as np
```
```{code-cell} python
:tags: [hide-input]

fig, ax = plt.subplots()

n = np.arange(2, 10)
skewness = [0] * len(n)
kurtosis = -6/5 * (n**2 + 1) / (n**2 - 1)

ax.plot(skewness, kurtosis, 'o')
fig
```
````{customfigure}
:name: fig_discrete-uniform-sk-graph

Grafico skewness-curtosi per il modello uniforme discreto.
````

## Quantili della distribuzione uniforme discreta (*)

A partire dalla forma analitica per la funzione di ripartizione ottenuta
all'inizio del Paragrafo, si ricava la seguente relazione che vale per
qualsiasi quantile della distribuzione uniforme discreta: ricordando che
fissati $n \in \mathbb N$ e $X \sim \mathrm U(n)$ vale

```{math}
F_X(x; n) = \frac{\lfloor x \rfloor}{n} \mathrm I_{[0, n)}(x)
          + \mathrm I_{[n, +\infty)}(x) \enspace,
```

e che per ogni $q \in [0, 1]$ il quantile di livello $q$ è definito come
$x_q = \arg\min_x \{F_X(x; n) \geq q \}$, si hanno i seguenti casi:

- se $q < 1/n$, per ogni $x < 1$ si ha $F_X(x; n) = 0 < q$, e quindi non
  esiste il corrispondente quantile;
- se $q = i / n$ per qualche $i \in \{ 1, 2, \dots, n \}$, si ha
  $x_q = \arg\min_x \{ \lfloor x \rfloor \geq i \} = i = nq$;
- nei casi rimanenti si ha necessariamente che $q = \frac{i}{n} + \epsilon$
  per qualche $i \in \{ 1, 2, \dots, n-1 \}$ e qualche
  $\epsilon \in (0, \frac{1}{n})$, e pertanto

```{margin}
L'ultima uguaglianza si ottiene verificando che $i = nq - n\epsilon$, ed
essendo $0 < n\epsilon < 1$ si ha come risultato che $i \in [nq - 1, nq]$,
da cui segue $i = \lfloor nq \rfloor$ e $i+1 = \lceil np \rceil$.
```
```{math}
x_q = \arg\min_x \left\{ \frac{\lfloor x \rfloor}{n} \geq \frac{i}{n}
                            + \epsilon \right\}
       = \arg\min_x \{ \lfloor x \rfloor \geq i + n \epsilon \}
       = i + 1 = \lceil n q \rceil \enspace.
```

Riassumendo, $x_q = \lceil nq \rceil$ per ogni $q \in (1/n, 1]$, mentre in
tutti gli altri casi il quantile non esiste. La
{numref}`fig_discrete-uniform-bp-1` e la {numref}`fig_discrete-uniform-bp-2`
illustrano i diagrammi a scatola per due distribuzioni uniformi discrete,
rispettivamente di parametro $n = 40$ e $n = 10$.

```{code-cell} python
:tags: [hide-input]

def unif_discr_quantile(q, n):
    if q < 1/n:
        raise ValueError(f'the quantile of a uniform discrete distribution '
                         f'of parameter {n!r} does not exist for all levels '
                         f'smaller than {1/n!r}.')
    return int(np.ceil(n*q))

def unif_discr_bp(n):

    fig, ax = plt.subplots(figsize=(6, 0.3))

    third_quartile = unif_discr_quantile(0.75, n)
    median = unif_discr_quantile(0.5, n)
    first_quartile = unif_discr_quantile(0.25, n)

    lw = 1
    height = 0.2

    ax.plot([median, median], [-height, height], c='k', linewidth=1.5)

    ax.plot([1, 1], [-.1, .1], c='k', linewidth=lw)
    ax.plot([1, first_quartile], [0, 0], c='k', linewidth=lw)

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

    ax.text(1, -0.4, '1', ha='center')
    ax.text(n, -0.4, f'{n}', ha='center')

    ax.text(median, -0.5,
            f'{median}',
            ha='center')

    ax.text(first_quartile, 0.4,
            f'{first_quartile}',
            ha='center')

    ax.text(third_quartile, 0.4,
            f'{third_quartile}',
            ha='center')

    ax.axis('off')
    pad = .5
    ax.set_xlim(0-pad, third_quartile*1.5+pad)

    return fig

fig = unif_discr_bp(40)
fig
```
````{customfigure}
:name: fig_discrete-uniform-bp-1

Il grafico a scatola per la distribuzione uniforme discreta di parametro
$n=40$.
````

```{code-cell} python
:tags: [hide-input]

fig = unif_discr_bp(10)
fig
```
````{customfigure}
:name: fig_discrete-uniform-bp-2

Il grafico a scatola per la distribuzione uniforme discreta di parametro
$n=10$.
````

(sec_generalized-discrete-uniform)=
## La forma generalizzata della distribuzione uniforme discreta (*)

Nel caso in cui gli $n$ esiti possibili di un esperimento equiprobabile
vengano trasformati in interi successivi, ma senza necessariamente partire da
$1$, la distribuzione della variabile aleatoria $X$ che ne risulta è
leggermente diversa rispetto a quella che abbiamo finora studiato. Ciò è
dovuto al fatto che, se indichiamo con $a \in \mathbb Z$ la più piccola delle
immagini degli esiti, il supporto della variabile aleatoria diventa ora
l'insieme $\{a, a+1, \dots, a+n \}$, o equivalentemente l'insieme di tutti
i numeri interi compresi tra $a$ e $b = a + n$, estremi inclusi. Per brevità
mi riferirò a tale insieme chiamandolo
_intervallo discreto_[^intervalli-discreti] e indicandolo
tramite la notazione $[a..b]$. Fissati $a, b \in \mathbb Z$ con $a < b$, dirò
che una variabile aleatoria $X$ segue una distribuzione
_uniforme discreta generalizzata_ su $[a..b]$, abbreviandolo tramite la
notazione $X \sim \mathrm U([a..b])$, se la sua funzione di massa di
probabilità è tale che per ogni $x \in \mathbb R$

```{math}
f_X(x; a, b) = \frac{1}{b - a + 1} \mathrm I_{[a..b]}(x) \enspace.
```

Si può facilmente verificare che la variabile aleatoria $X' = X - a + 1$ segue
una distribuzione uniforme discreta di parametro $b - a + 1$. Pertanto la
funzione di ripartizione per $X'$ coincide con la funzione costante a tratti
che si ottiene considerando la funzione di ripartizione di $X$ e traslandola a
destra di una quantità pari ad $a - 1$, ottenendo dunque una funzione costante
a tratti che è inizialmente nulla e cresce di una quantità
$\frac{1}{b - a + 1}$ in corrispondenza di ogni intero nell'insieme $[a..b]$.
Inoltre il valore atteso della distribuzione generalizzata è

```{math}
\mathbb E(X) = \mathbb E(X' + a) = \mathbb E(X) + a - 1
             = \frac{b - a + 2}{2} + a - 1 = \frac{a + b}{2} \enspace,
```

e si posiziona correttamente nel punto medio del più piccolo intervallo che
contiene il supporto della variabile aleatoria. Infine, essendo la varianza
insensibile alle traslazioni si avrà che

```{math}
\mathrm{Var}(X) = \mathrm{Var}(X') = \frac{(b - a + 1)^2 - 1}{12} \enspace.
```

## Implementazione dellla distribuzione uniforme discreta

L'implementazione delle distribuzioni uniformi discrete in `scipy.stats`
passa attraverso la funzione `randint`, che in realtà permette di
fare riferimento alla formulazione descritta nel Paragrafo
{ref}`sec_generalized-discrete-uniform`. In particolare, l'invocazione
di `randint(a, b)` restituisce un oggetto relativo alla
distribuzione uniforme discreta sull'insieme $\{a, \dots, b-1\}$. Pertanto,
specificando come argomenti di questa funzione rispettivamente $1$ e $n-1$
si ottiene un oggetto collegato alla distribuzione $\mathrm U(n)$, come
esemplificato nella cella seguente, il cui codice visualizza i grafici
delle funzioni di massa di probabilità e di ripartizione nel caso $n=7$ già
illustrato in precedenza.

```{code-cell} python
:tags: [hide-input]

import scipy.stats as st

n = 7
fig, axes = plt.subplots(1, 2, sharey=True)

(ax_pdf, ax_cdf) = axes
X = st.randint(1, n+1)
x = np.arange(-1, n+2, 0.01)
observations = np.arange(1, n+1)

ax_cdf.step(x, X.cdf(x))
ax_pdf.vlines(observations, 0, X.pmf(observations), color='k')
ax_pdf.plot(observations, X.pmf(observations), 'o', color='k')

for ax in axes:
    ax.set_ylim(0, 1.1)
    ax.set_xticks(observations)
    ax.set_xlabel(r'$x$')

ax_cdf.set_ylabel(r'$F_X$', rotation='horizontal')
ax_pdf.set_ylabel(r'$f_X$', rotation='horizontal')

ax_cdf.set_xlim(-1, n+2)
ax_pdf.set_xlim(0, n+1)

fig
```

La {numref}`fig_discrete-uniform-simulation` mostra inoltre come utilizzare il
metodo `rvs` su un oggetto relativo a una distribuzione uniforme discreta, così
da simulare l'osservazione di $5000$ sue specificazioni, il cui grafico delle
frequenze relative viene confrontato con quello della rispettiva funzione di
massa di probabilità. Nella versione interattiva del libro è possibile
modificare il valore del parametro $n$, preimpostato a $7$.

````{customfigure}
:name: fig_discrete-uniform-simulation
:class: left-align

```{interactive-code} python
:tags: [toggle-code]

import pandas as pd
import scipy.stats as st

fig_sim, ax_sim = plt.subplots()
console.log('uno'

@when("input", "#n-sim, #m-sim")
def discrete_uniform_simulation(event):

    n_sim = int(page['#n-sim'][0].value)
    page['#n-sim-value'][0].innerHTML = f'{n_sim}'
    m_sim = int(page['#m-sim'][0].value)

    U_sim = st.randint(1, n_sim + 1)
    x_sim = U_sim.rvs(m_sim)

    freq_sim = pd.Series(x_sim).value_counts(normalize=True)
    freq_sim = freq_sim.reindex(np.arange(1, n_sim + 1), fill_value=0).values

    ax_sim.clear()
    x_sim = np.arange(1, n_sim + 1)
    ax_sim.bar(x_sim, freq_sim, facecolor='lightgray', edgecolor='gray', width=.1)

    ax_sim.vlines(x_sim, 0, U_sim.pmf(x_sim))
    ax_sim.plot(x_sim, U_sim.pmf(x_sim), 'o')

    ax_sim.set_xlim(-1, 21)
    ax_sim.set_ylim(0, 1.1)

    display(fig_sim, target='graph-%this%', append=False)

discrete_uniform_simulation(None)
```
```{raw} html
<div class="plot-container">
    <div class="model-slider-container">
        <label for="n-sim">\( n \): </label>
        <input type="range" id="n-sim"
               min="1" max="20" value="10" step="1" />
        <span id="n-sim-value">10</span>
    </div>
    <div class="model-slider-container">
        <label for="m-sim">\( m \): </label>
        <select id="m-sim">
          <option value="5">5</option>
          <option value="50" selected>50</option>
          <option value="500">500</option>
          <option value="5000">5000</option>
        </select>
    </div>
</div>
```

Diagramma a barre delle frequenze di un insieme di osservazioni estratte da
un modello uniforme discreto, sovrapposto al diagramma a bastoncini della
corrispondente funzione di massa di probabilità.
````



[^intervalli-discreti]: Il concetto classico di intervallo coinvolge i numeri
reali compresi tra due estremi, ma fissata una relazione di ordine totale
si può banalmente estendere questo concetto modificando l'insieme di partenza.
Pertanto ha senso definire l'intervallo intero delimitato da $a$ e $b$ come
l'insieme $\{x \in \mathbb Z \text{ tale che } a \leq x \leq b\}$. Gli
intervalli interi sono relativamente poco utilizzati nella matematica
classica, ma ampiamente presenti nelle formalizzazioni presenti nelle branche
più moderne di questa disciplina, e ancora di più in quelle relative
all'informatica. Per questo motivo, non vi è unanimità nella letteratura
scientifica relativamente a una notazione compatta da usare per definire un
intervallo discreto: molto spesso viene utilizzato $[a..b]$, ma anche $a..b$ è
molto diffuso, e sono presenti altre opzioni, come per esempio $[[a, b]]$
(volendo, si può evitare di introdurre una notazione nuova, scrivendo
$[a, b] \cap \mathbb Z$, che risulta però un po’ troppo prolisso). Va notato,
infine, che venendo meno la proprietà di continuità, non ha più senso parlare
di intervalli discreti aperti, chiusi o semiaperti. Sebbene sia in linea di
principio possibile definire per esempio $(a..b) \triangleq [a+1..b-1]$,
mantenendo quindi la possibilità di considerare insiemi di valori compresi tra
due estremi escludendo questi ultimi, ho scelto di evitare di complicare
ulteriormente la notazione già non universalmente accettata, riferendomi
sempre a intervalli discreti i cui estremi sono sempre inclusi nell'insieme in
questione.