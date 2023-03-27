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

(sec:modello-geometrico)=
# Le distribuzioni geometriche

Bruce Banner si trasforma in Hulk ogni volta che non riesce a controllare
un attacco d'ira. Ipotizziamo che, indipendentemente da tutto il resto, ciò
avvenga con una prefissata probabilità: possiamo dunque modellare la
trasformazione nei termini di un esperimento bernoulliano. Convenzionalmente,
definiamo questo esperimento in modo che il successo si verifichi quando
Banner si arrabbia e si trasforma in Hulk; al contrario, il fallimento avviene
quando lui si arrabbia ma non si trasforma. Nel momento in cui iniziamo a
leggere un fumetto, possiamo domandarci dopo quante arrabbiature Bruce Banner
diventerà Hulk. La risposta sarà «uno» se la trasformazione avverrà al primo
colpo di rabbia, «due» se il primo attacco d'ira sarà superato ma il secondo
no, e così via. In linea di principio, non possiamo stabilire a priori un
numero massimo di arrabbiature entro il quale Banner si trasformerà. Pertanto
siamo di fronte a un esperimento casuale i cui esiti possono essere associati
a tutti i numeri interi positivi. Questo tipo di esperimento è ben descritto
dalla famiglia delle distribuzioni geometricche.

## Il modello geometrico

```{margin}
I processi geometrici, così come quelli binomiali, si possono paragonare al
concetto di _ciclo_ nella programmazione degli elaboratori. Ma in questo caso
la loro controparte è quella dei _cicli basati su condizione_.
```
Un processo di conteggio alternativo rispetto a quello binomiale consiste nel
considerare un esperimento di Bernoulli descritto dalla corrispondente
probabilità di successo $p \in (0, 1]$, e ripetendolo in condizioni di
indipendenza fino a che non si ottiene per la prima volta un successo come
esito. Questo processo viene modellato utilizzando la
_distribuzione geometrica_, definita di seguito.


````{prf:definition} La famiglia delle distribuzioni geometriche
:label: def:distribuzione-geometrica
Fissato $p \in (0, 1]$, la distribuzione geometrica di parametro $p$ è
definita dalla funzione di massa di probabilità

\begin{equation*}
f(x; p) = (1-p)^x p \; \mathrm I_{\mathbb N \cup \{ 0 \}}(x) \enspace.
\end{equation*}

Userò la sintassi $X \sim \mathrm G(p)$ per indicare che una variabile
aleatoria $X$ segue una distribuzione geometrica di parametro $p$. L'insieme
di tutte le distribuzioni geometriche al variare dei valori del reltivo
parametro prende il nome di _famiglia delle distribuzioni geometriche_.
````

Siccome le varie ripetizioni dell'esperimento di Bernoulli di parametro $p$
sono tra loro indipendenti, si ha

\begin{align*}
f(x; p) = & (1-p)^x p
        = \mathbb P(\text{insuccesso alla prima ripetizione}) \dots \\
          & \dots\mathbb P(\text{insuccesso alla $x$-esima ripetizione})
\mathbb P(\text{successo alla $(x+1)$-esima ripetizione}) \enspace,
\end{align*}

```{margin}
In alternativa sarebbe possibile definire la distribuzione geometrica contando
il numero totale di ripetizioni per ottenere il primo successo. In questo
questo modo si conteggerebbe un esperimento in più (che è esattamente
l'esperimento in cui si ottiene il successo). Ovviamente la distribuzione
ottenuta avrebbe delle proprietà (come per esempio il valore atteso e la
varianza) diversi da quelli che otterremo.
```
e quindi una distribuzione geometrica descrive il numero di ripetizioni di un
esperimento di Bernoulli che hanno come esito un fallimento che precedono
l'esecuzione del medesimo esperimento che per la prima volta ha come esito
un successo. Il supporto di una siffatta variabile aleatoria è l'insieme
$\mathbb N \cup \{ 0 \}$ dei numeri naturali allargato in modo da comprendere
la specificazione $0$, che corrisponde al caso in cui l'esperimento viene
eseguito una e una sola volta perché il primo esito che si verifica è un
successo (e pertanto il numero di insuccessi ottenuti è nullo).


Il motivo per il quale l'insieme dei possibili valori del parametro $p$ è un
intervallo semiaperto a sinistra è legato alla natura del processo di
conteggio. Il valore $p=1$ è ammissibile, sebbene in questo caso ogni
esecuzione dell'esperimento di Bernoulli avrebbe come esito un successo, e
quindi la distribuzione degenera nella descrizione della costante $0$. Al
contrario, la possibilità che $p$ sia nullo va esclusa a priori, perché in
questo caso non sarebbe mai possibile avere come esito un successo, e quindi
la ripetizione dell'esperimento non terminerebbe mai. Questo implicherebbe
in un certo qual senso che la specificazione assunta assume un valore
infinito, cosa che è proibita dalla {prf:ref}`def:variabile-aleatoria`.

Si verifica facilmente che sommando i valori di massa di probabilità per tutte
le specificazioni della distribuzione si ottiene come risultato 1:

\begin{align}
\sum_{x=0}^{+\infty}\mathrm f(x; p) = \sum_{x=0}^{+\infty} (1-p)^x p =
p \sum_{x=0}^{+\infty}(1-p)^x
 = p \frac{1}{1-(1-p)} = 1.
\end{align}


````{admonition} Nomenclatura
:class: naming

La distribuzione geometrica prende il nome dalla serie omonima, utilizzata
nel penultimo passaggio dell'equazione precedente e definita da

\begin{equation*}
\sum_{i=0}^{+\infty} \alpha^i = \frac{1}{1-\alpha} \enspace,
\end{equation*}

a patto che che $|\alpha| < 1$. Nel nostro caso questa condizione equivale a
$0 < p < 2$, che è sempre verificata, essendo $p \in (0, 1]$.
````

La forma analitica per la funzione di ripartizione di una generica
distribuzione geometrica si ottiene nel modo seguente:
data $X \sim \mathrm G(p)$ e fissato un generico
$n \in \mathbb N \cup \{ 0 \}$,

```{margin}
Nel terzultimo passaggio ho applicato alla sommatoria la sostituzione
$i = x - (n + 1)$.
```
\begin{align}
\mathbb P(X > n) &= \sum_{x=n+1}^{+\infty}f_X(x; p)
                  = \sum_{x=n+1}^{+\infty}(1-p)^x p \\
                 &= p (1-p)^{n+1} \sum_{x=n+1}^{+\infty}(1-p)^{x - (n+1)}
                  = p (1-p)^{n+1} \sum_{i=0}^{+\infty}(1-p)^i \\
                 &= p (1-p)^{n+1} \frac{1}{1-(1-p)} \\
                 &= (1-p)^{n+1} \enspace.
\end{align}

Pertanto $F_X(n; p) = \mathbb P(X \leq n) = 1 - \mathbb P(X > n)
= 1 - (1-p)^{n+1}$.

Fissato invece un generico $x \in \mathbb R^+$ e indicato con
$\lfloor x \rfloor$ l'intero ottenuto troncando $x$ (o, equivalentemente,
arrotondandolo per difetto), l'evento $X \leq x$ equivarrà a
$X \leq \lfloor x \rfloor$. Tenuto infine conto del fatto che le specificazioni
di una distribuzione geometrica sono non negative, si ottiene facilmente la
seguente forma più generale per la funzione di ripartizione:

\begin{equation*}
F_X(x; p) = \left( 1 - (1 - p)^{\lfloor x \rfloor + 1} \right)
                                 \mathrm I_{[0, +\infty]}(x) \enspace.
\end{equation*}



Un modo intuitivo di simulare l'estrazione di valori da una distribuzione
geometrica consiste nel ripetere l'esecuzione del corrispondente esperimento
bernoulliano, fermandosi quando si ottiene il primo successo e restituendo
il numero di tentativi effettuati. Utilizzando la funzione
`bernoulli` definita nel {numref}`sec:modello-bernoulliano`, è possibile
definire in modo semplice la seguente funzione che permette di simulare una
generica distribuzione geometrica, specificando il valore del
corrispondente parametro come argomento.

```{margin}
Questa implementazione verifica anche che il valore del parametro della
distribuzione sia valido.
```
```{code-cell} ipython3
from util import bernoulli

def geom_rv(p):
    """Simulate the extraction of a value from the geometric distribution

    :param p: parameter of the geometric distribution
    :type p: float
    :raises ValueError: if p is not in the interval (0, 1] 
    :return: simulated value of the distribution
    :rtype: int
    """
    if p <= 0 or p > 1:
        raise ValueError(f"{p} is not a valid parameter" \
                         " for the geometric distribution.")
    i = 0
    while bernoulli(p) == 0:
        i +=1

    assert i >= 0 and type(i) == int

    return i + 1

[geom_rv(.3) for _ in range(10)]
```

Si potrebbe dimostrare che esistono metodi che utilizzano approcci più
efficienti per simulare la distribuzione geometrica, per esempio evitando
l'uso di cicli. È questo l'approccio seguito dalla classe `geom` fornita dal
package `scipy.stats`, che nella cella seguente viene utilizzata per generare
una sequenza in modo analogo a quanto fatto usando la funzione `geom_rv`
nell'esempio precedente.

```{code-cell} ipython3
from scipy.stats import geom

g = geom(.3)
g.rvs(10)
```

Indichiamo con $\mathrm p_X$ la funzione di massa di probabilità di una
variabile aleatoria $X \sim \mathrm G(p)$. Dato $i \in \mathbb N$, l'evento
$X = i$ corrisponde alla situazione in cui il primo successo dell'esperimento
bernoulliano è avvenuto esattamente dopo $i$ ripetizioni. Questa situazione
avviene se e solo se nelle prime $i - 1$ ripetizioni l'esperimento ha come
esito un fallimento, mentre nell'$i$-esima si ottiene un successo. Tenendo
conto del fatto che le ripetizioni sono eseguite in modo indipendente le une
dalle altre, otteniamo $\mathbb P(X = i) = (1-p)^{i - 1} p$ e quindi la forma
analitica della funzione di massa di probabilità di $X$ risulta essere la
seguente:

$$
\mathrm p_X(i; p) = (1-p)^{i - 1} p \mathrm I_{\mathbb N}(i).
$$



Nella cella seguente viene definita una funzione `geom_pdf` che accetta come
argomenti rispettivamente un valore numerico $x$ e il parametro $p$ di una
distribuzione geometrica, e che restituisce il corrispondente valore della
funzione di massa di probabilità geometrica.

```{code-cell} ipython3
def geom_pdf(x, p):
    """Compute the p.d.f. of a geometric distribution

    :param x: arguments to the p.d.f.
    :type x: list, sequence or numpy array of numerical values
    :param p: parameter of the geometric distribution
    :type p: float
    :raises ValueError: if p is not in the interval (0, 1] 
    :return: computed values of the p.d.f.
    :rtype: numpy array of float
    """
    if p <= 0 or p > 1:
        raise ValueError(f"{p} is not a valid parameter " \
                         "for the geometric distribution.")
    invalid_indices = (x != np.floor(x)) | (x <= 0)
    pdf_values = (1 - p) ** (x - 1) * p
    pdf_values[invalid_indices] = 0

    return pdf_values
```

È quindi possibile visualizzare i valori di massa di probabilità, fissando per
esempio $p=\frac{1}{2}$ e usando un grafico a bastoncini. Ovviamente la
visualizzazione dovrà coinvolgere un sottoinsieme delle possibili
specificazioni, essendo il supporto della distribuzione infinito. Nella
versione interattiva del libro è possibile modificare il valore di $p$
rigenerando automaticamente il grafico.

```{code-cell} ipython3
:tags: [thebe-init]
from ipywidgets import *
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('matplotlibrc')

def gr_geom_pdf(p):
    """Show the graph of the p.d.f. of a geometric distribution

    :param p: parameter of the geometric distribution
    :type p: float
    """
    x = np.arange(0, 10, 1)
    pdf_values = geom_pdf(x, p)
    plt.vlines(x, [0]*len(x), pdf_values)
    plt.plot(x, pdf_values, 'o')
    plt.ylim(ymax=1, ymin=0)
    plt.xlim(xmax=11, xmin = -1)
    plt.show()

interact(gr_geom_pdf, p=(0.1, 1, 0.1))
plt.show()
```

Procediamo ora a determinare il valore atteso e la varianza della
distribuzione. Iniziamo mostrando un risultato intermedio.

```{prf:lemma}
Per ogni $\alpha \in (-1, 1)$

$$
\sum_{i=0}^{+\infty}i \alpha^{i - 1} = \frac{1}{(1-\alpha)^2}.
$$
```
```{margin}
Nel secondo passaggio ho sfruttato la linearità dell'operatore di derivata
prima, scambiandolo con la sommatoria.
```
```{prf:proof}
Osservando che $i \alpha^{i - 1}$ è la derivata prima di $\alpha^i$
rispetto ad $\alpha$, otteniamo:
\begin{align*}
\sum_{i=0}^{+\infty}i \alpha^{i-1} &= \sum_{i=0}^{+\infty} \frac{\mathrm d}{\mathrm d \alpha} \alpha^i = \frac{\mathrm d}{\mathrm d \alpha} \sum_{i=0}^{+\infty} \alpha^i \\
&= \frac{\mathrm d}{\mathrm d \alpha} \frac{1}{1-\alpha}
= \frac{1}{(1-\alpha)^2},
\end{align*}
e ciò completa la dimostrazione.
```

Questo risultato ci permette di calcolare agevolmente il valore atteso.

```{prf:proposition}
Il valore atteso della distribuzione geometrica di parametro
$p$ è pari a $\frac{1}{p}$.
```
```{prf:proof}
Innanzitutto

\begin{align*}
\mathrm E(X) &= \sum_{i=1}^{+ \infty} i \mathrm p_X(i; p)
              = \sum_{i=1}^{+ \infty} i (1-p)^{i - 1} p \\
             &= p \sum_{i=0}^{+ \infty} i (1-p)^{i - 1},
\end{align*}

dove nell'ultimo passaggio ho sfruttato il fatto che il valore della
serie non cambia se facciamo partire l'indice $i$ da $0$, in quanto ciò
equivale ad aggiungere un termine nullo. A questo punto, ponendo
$\alpha = 1 - p$ e applicando il lemma appena dimostrato si ha

$$
\mathrm E(X) = p \frac{1}{p^2} = \frac{1}{p}.
$$

che dimostra la proposizione.
```

Visualizziamo graficamente l'andamento del valore atteso in funzione del
parametro $p$.

```{code-cell} ipython3
p = np.arange(0.01, 1.01, 0.01)
e = 1 / p

plt.plot(p, e)
plt.ylim(1, 10)
plt.show()
```

Il risultato è coerente con il significato di $p$: più il suo valore si
avvicina a $1$, più è probabile che si ottenga un successo nel primo
esperimento bernoulliano alla base della distribuzione geometrica, così che
il numero atteso di ripetizioni tende a $1$. Parimenti, quando $p$ diminuisce
diventa meno probabile ottenere un successo e quindi il numero atteso di
esperimenti da effettuare aumenta. In particolare, al tendere di $p$ a zero
l'esperimento bernoulliano non avrà mai successo e quindi il numero atteso di
ripetizioni tenderà a più infinito.

Per calcolare la varianza, procediamo innanzitutto a determinare il valore di
$\mathrm E(X^2)$.

**Proposizione** Il valore atteso del quadrato della distribuzione geometrica
di parametro $p$ è pari a $\frac{(1-p)(2-p)}{p^2}$.

Dimostrazione.

\begin{align}
\mathrm E\left(X^2\right) &= \sum_{i=0}^{+\infty} i^2 p_X(i) \\
               &= \sum_{i=0}^{+\infty} i^2 p (1-p)^i \\
               &= p (1-p) \sum_{i=0}^{+\infty} i^2 (1-p)^{i-1} \\
               &= p (1-p) \sum_{i=0}^{+\infty} \frac{\mathrm d}{\mathrm d p}\left(-i(1-p)^i\right) \\
               &= -p (1-p) \frac{\mathrm d}{\mathrm d p} \sum_{i=0}^{+\infty} i(1-p)^i.
\end{align}

Applicando ancora il lemma dimostrato precedentemente si ottiene

\begin{align}
\mathrm E\left(X^2\right) &= -p (1-p) \frac{\mathrm d}{\mathrm d p}
                                \frac{1-p}{p^2} \\
      &= p (1-p) \frac{p^2 + 1p(1-p)}{p^4} \\
      &= \frac{(1-p)(2-p)}{p^2}.
\end{align}

Siamo ora in grado di calcolare la varianza della distribuzione.

**Proposizione**. La varianza della distribuzione geometrica di parametro $p$
è uguale a $\frac{1-p}{p^2}$.

Dimostrazione.

\begin{equation}
\mathrm{Var}(X) = \mathrm E \left(X^2\right) - \mathrm E(X)^2 =
                  \frac{(1-p)(2-p)}{p^2} - \frac{(1-p)^2}{p^2} =
                  \frac{1-p}{p^2}.
\end{equation}

Come già fatto per il valore atteso, visualizziamo graficamente l'andamento
della varianza in funzione del valore per il parametro $p$.

```{code-cell} ipython3
x = np.arange(0.01, 1.01, 0.01)
y = list(map(lambda p: (1-p)/p**2, x))

plt.plot(x, y)
plt.ylim(0, 50)
plt.show()
```

Anche in questo caso il grafico ottenuto è coerente con il significato
probabilistico della distribuzione: al diminuire di $p$ la massa di probabilità
si concentra su un insieme sempre più grande di valori, dunque la varianza
aumenta. Quando $p=1$ il numero di insuccessi è sempre nullo e quindi la
variabile aleatoria degenera in una costante che per definizione ha varianza
nulla.

Siamo ora in grado di accoppiare la visualizzazione della funzione di massa di
probabilità a un'indicazione del valore atteso e della dispersione della
distribuzione. Nella cella seguente viene rigenerato il precedente grafico
della massa di probabilità al quale viene aggiunto, nella parte superiore, un
rettangolo verde centrato in corrispondenza del valore atteso e largo due
deviazioni standard. Anche in questo caso la versione interattiva degli appunti
permette di modificare il valore di $p$ e ridisegnare automaticamente l'intero
grafico.

```{code-cell} ipython3
import matplotlib.patches as patches

def geom_pdf(x, p):
    assert p > 0 and p <= 1, '{} is not a valid parameter ' \
                             'for the geometric distribution.'.format(p)

    return p * (1 - p)**x if x==int(x) else 0

def gr_geom_pdf(p):
    x = np.arange(0, 10, 1)
    avg = (1 - p) / p
    stdev = (1-p)**0.5/p
    plt.gca().add_patch(patches.Rectangle(
        (avg-stdev, 0.95), 2*stdev, 0.05, edgecolor='None', facecolor='green'
    ))
    plt.plot([avg, avg], [0.9, 1], color='green')
    plt.vlines(x, [0]*len(x), list(map(lambda _: geom_pdf(_, p), x)))
    plt.plot(x, list(map(lambda _: geom_pdf(_, p), x)), 'o')

    plt.ylim(ymax=1, ymin=0)
    plt.xlim(xmax=11, xmin = -1)
    plt.show()

interact(gr_geom_pdf, p=(0.1, 1, 0.1))
plt.show()
```



che viene utilizzata nella cella seguente per implementare una funzione
`geom_cdf`.

```{code-cell} ipython3
def geom_cdf(x, p):
    assert p > 0 and p <= 1, '{} is not a valid parameter ' \
                             'for the geometric distribution.'.format(p)
    return 1 - (1-p)**(int(x) + 1) if x >= 0 else 0
```

Il grafico della funzione di ripartizione è visualizzato qui di seguito. Anche
in questo caso la visualizzazione, fatta scegliendo $p=0.5$, è modificabile
nella versione interattiva degli appunti.

```{code-cell} ipython3
def gr_geom_cdf(p):
    x = np.arange(-2, 10, .1)
    y = list(map(lambda _: geom_cdf(_, p), x))
    plt.step(x, y)

    plt.ylim(ymax=1, ymin=-.1)
    plt.xlim(xmax=10, xmin = -2)
    plt.show()

interact(gr_geom_cdf, p=(0.1, 1, 0.1))
plt.show()
```

Si noti infine che $\mathrm P(X \geq x) = \mathrm P(X \geq \lfloor x \rfloor) =
\mathrm P(X > \lfloor x \rfloor - 1) = (1-p)^{\lfloor x \rfloor}$, e quindi

\begin{align}
\mathrm P(X \geq x+y | X \geq x)
            &= \frac{\mathrm  P(X \geq x+y, X \geq x)}{\mathrm  P(X \geq x)} \\
            &= \frac{\mathrm  P(X \geq x+y)}{\mathrm  P(X \geq x)} \\
            &= \frac{(1-p)^{\lfloor x \rfloor + \lfloor y \rfloor}}
                    {(1-p)^{\lfloor x \rfloor}} \\
            &= (1-p)^{\lfloor y \rfloor} \\
            &= \mathrm P(X \geq y).
\end{align}

Questa proprietà prende il nome di _assenza di memoria_. Essa indica che
durante la ripetizione dell'esperimento bernoulliano, il fatto che sia avvenuto
un numero $n$ (anche elevato) di insuccessi consecutivi non permette di dire
alcunché sul numero di successivi insuccessi prima che si verifichi il primo
successo. In altre parole, non c'è nessuna differenza, da un punto di vista
probabilistico, dalla ripetizione degli esperimenti che vanno dal $n+1$-esimo
in poi e dal ricominciare da capo la ripetizione.
