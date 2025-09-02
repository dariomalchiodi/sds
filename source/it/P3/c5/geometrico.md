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
dalla famiglia delle distribuzioni geometriche.

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

```{math}
f(x; p) = (1-p)^x p \; \mathrm I_{\mathbb N \cup \{ 0 \}}(x) \enspace.
```

Userò la sintassi $X \sim \mathrm G(p)$ per indicare che una variabile
aleatoria $X$ segue una distribuzione geometrica di parametro $p$. L'insieme
di tutte le distribuzioni geometriche al variare dei valori del reltivo
parametro prende il nome di _famiglia delle distribuzioni geometriche_.
````

Siccome le varie ripetizioni dell'esperimento di Bernoulli di parametro $p$
sono tra loro indipendenti, si ha

```{math}
\begin{align*}
&f(x; p) = (1-p)^x p = \\
        & \mathbb P(\text{insuccesso alla prima ripetizione}) \dots \\
        & \dots\mathbb P(\text{insuccesso alla $x$-esima ripetizione})
\mathbb P(\text{successo alla $(x+1)$-esima ripetizione}) \enspace,
\end{align*}
```

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

```{math}
\begin{align}
\sum_{x=0}^{+\infty}\mathrm f(x; p) = \sum_{x=0}^{+\infty} (1-p)^x p =
p \sum_{x=0}^{+\infty}(1-p)^x
 = p \frac{1}{1-(1-p)} = 1.
\end{align}
```

````{admonition} Nomenclatura
:class: naming

La distribuzione geometrica prende il nome dalla serie omonima, utilizzata
nel penultimo passaggio dell'equazione precedente e definita da

```{math}
\sum_{i=0}^{+\infty} \alpha^i = \frac{1}{1-\alpha} \enspace,
```

a patto che che $|\alpha| < 1$. Nel nostro caso questa condizione equivale a
$0 < p < 2$, che è sempre verificata, essendo $p \in (0, 1]$.
````

La forma analitica per la funzione di ripartizione di una generica
distribuzione geometrica si ottiene nel modo seguente:

````{prf:theorem}
:label: teo:geometric-cdf

Fissato $p \in (0, 1]$ e data $X \sim \mathrm G(p)$,
$\forall n \in \mathbb N \cup \{ 0 \}$ e $\forall x \in \mathbb R$ 

```{math}
:label: eq:geometric-cdf

F_X(x; p) = \left( 1 - (1 - p)^{\lfloor x \rfloor + 1} \right)
            \mathrm I_{[0, +\infty]}(x) \enspace.
```
````
````{admonition} _
:class: myproof

Indipendentemente dal valore di $n$ si ha che

```{math}
\begin{align*}
\mathbb P(X > n) &= \sum_{x=n+1}^{+\infty}f_X(x; p)
                  = \sum_{x=n+1}^{+\infty}(1-p)^x p \\
                 &= p (1-p)^{n+1} \sum_{x=n+1}^{+\infty}(1-p)^{x - (n+1)}
                  = p (1-p)^{n+1} \sum_{i=0}^{+\infty}(1-p)^i \\
                 &= p (1-p)^{n+1} \frac{1}{1-(1-p)}
                  = (1-p)^{n+1} \enspace,
\end{align*}
```

dove nel terzultimo passaggio ho applicato la sostituzione $i = x - (n + 1)$.
Pertanto $F_X(n; p) = \mathbb P(X \leq n) = 1 - \mathbb P(X > n)
= 1 - (1-p)^{n+1}$. Fissato ora un generico $x \in \mathbb R^+$ e indicato con
$\lfloor x \rfloor$ l'intero ottenuto troncando $x$ (o, equivalentemente,
arrotondandolo per difetto), l'evento $X \leq x$ equivarrà a
$X \leq \lfloor x \rfloor$. Tenuto infine conto del fatto che le specificazioni
di una distribuzione geometrica sono non negative, si ottiene

```{math}
F_X(x; p) = \left( 1 - (1 - p)^{\lfloor x \rfloor + 1} \right)
                                 \mathrm I_{[0, +\infty]}(x)
```

come forma più generale per la funzione di ripartizione.
````

La {numref}`fig:geometric-pdf-cdf` mostra i grafici delle funzioni di massa di
probabilità e di ripartizione di una generica distribuzione geometrica. Essendo
in questo caso infinito il supporto della distribuzione, il primo grafico
contiene in teoria un numero infinito di bastoncini, e solo quelli relativi ai
valori più piccoli delle specificazioni sono mostrati effettivamente. È
possibile modificare il valore del parametro $p$ agendo sul relativo selettore
e verificare in che modo i grafici vengono modificati.

````{customfigure}
:name: fig:geometric-pdf-cdf

```{code-block} python
:class: toggle-code

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pyodide.ffi import create_proxy
import io
import base64


def geometric_pdf_cdf(p):
    fig, ax = plt.subplots()

    x = np.arange(0, 11)
    pmf = (1-p) ** x * p
    cdf = 1 - (1-p)**(np.floor(x)+1)

    ax.vlines(x, 0, pmf, color='k')
    ax.plot(x, pmf, 'o')
    
    ax.hlines(cdf[:-1], x[:-1], x[1:])
    ax.vlines(x[:-1], cdf[:-1]-.01, cdf[:-1]+.01)
    ax.plot([-1, 0], [0, 0], color='C0')

    ax.set_title(f'p = {p:.2f}')
    ax.set_ylim(0, 1.1)

    #  Manual rendering to avoid MathJax processing
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
    p = float(document.getElementById("p-slider").value)
    document.getElementById("p-value").innerText = f"{p:.1f}"
    geometric_pdf_cdf(p)


p_slider = document.getElementById("p-slider")
p_slider.addEventListener("input", create_proxy(update_plot))

# Initial plot
geometric_pdf_cdf(0.3)
```
```{raw} html

<div id="plot-container" style="visibility: none;">

    <div class="slider-container" style="float: left;">
        <label for="p-slider">\( p \): </label>
        <input type="range" id="p-slider"
               min="0" max="1" value="0.3" step="0.1" />
        <span id="p-value">0.3</span>
    </div>

    <div id="pdf-cdf-output" class="no-mathjax"
            style="clear: both; display: flex; justify-content: center; margin-bottom: 2em;">
    </div>
</div>
```

Grafici della funzione di massa di probabilità e di ripartizione per il
modello geometrico.
````


## Valore atteso e varianza della distribuzione geometrica

Il calcolo dei valori attesi che coinvolgono la distribuzione geometrica
richiede tipicamente di valutare il valore di serie infinite. Pertanto
conviene iniziare dal seguente risultato intermedio.

````{prf:lemma}
:label: lemma:geom-ev
Per ogni $\alpha \in (-1, 1)$ valgono le seguenti identità:

```{math}
\begin{align*}
\sum_{i=0}^{+\infty}i \alpha^{i - 1} = \frac{1}{(1-\alpha)^2} \enspace, \\
\sum_{i=0}^{+\infty}i^2 \alpha^{i - 1} = \frac{\alpha + 1}{(1-\alpha)^3}
                                                              \enspace.
\end{align*}
```
````
```{margin}
Nel secondo passaggio ho sfruttato la linearità dell'operatore di derivata
prima, scambiandolo con la sommatoria.
```
````{admonition} _
:class: myproof

Osservando che $i \alpha^{i - 1}$ è la derivata prima di $\alpha^i$
rispetto ad $\alpha$, otteniamo:
```{math}
\begin{align*}
\sum_{i=0}^{+\infty}i \alpha^{i-1}
        &= \sum_{i=0}^{+\infty} \frac{\mathrm d}{\mathrm d \alpha} \alpha^i
         = \frac{\mathrm d}{\mathrm d \alpha} \sum_{i=0}^{+\infty} \alpha^i \\
        &= \frac{\mathrm d}{\mathrm d \alpha} \frac{1}{1-\alpha}
         = \frac{1}{(1-\alpha)^2},
\end{align*}
```

e ciò completa la dimostrazione della prima identità, tenendo conto del fatto
che i valori considerati per $\alpha$ garantiscono sempre che la serie
geometrica converga. Procedendo in modo analogo,

```{math}
\begin{align*}
\sum_{i=0}^{+\infty}i^2 \alpha^{i-1}
        &= \sum_{i=0}^{+\infty} \frac{\mathrm d}{\mathrm d \alpha} i \alpha^i
         = \frac{\mathrm d}{\mathrm d \alpha} \sum_{i=0}^{+\infty} i\alpha^i \\
        &= \frac{\mathrm d}{\mathrm d \alpha} \alpha
                   \sum_{i=0}^{+\infty} i \alpha^{i - 1}
         = \frac{\mathrm d}{\mathrm d \alpha} \frac{\alpha}{(1-\alpha)^2}
         = \frac{\alpha + 1}{(1 - \alpha)^3} \enspace,
\end{align*}
```

il che dimostra anche la seconda identità.
````

Questo risultato ci permette di calcolare agevolmente il valore atteso della
distribuzione.

````{prf:theorem}
:label: teo:mean-geometric

Dati $p \in (0, 1]$, e $X \sim \mathrm G(p)$,

```{math}
\mathbb E(X) = \frac{1 - p}{p} \enspace.
```
````
````{admonition} _
:class: myproof

Applicando la definizione di valore atteso si ottiene

```{math}
\mathbb E(X) = \sum_{x=0}^{+ \infty} x f_X(x; p)
             = \sum_{i=0}^{+ \infty} x (1-p)^x p
             = p (1 - p) \sum_{x=0}^{+ \infty} x (1 - p)^{x - 1} \enspace,
```

e quindi ponendo $\alpha = 1 - p$ e applicando la prima identità del
{prf:ref}`lemma:geom-ev` si ottiene

```{math}
\mathbb E(X) = p (1 - p) \frac{1}{p^2} = \frac{1 - p}{p} \enspace.
```

che dimostra la proposizione.
````

La {numref}`fig:geometric-ev` visualizza graficamente l'andamento del valore
atteso della distribuzione geometrica in funzione del corrispondente parametro
$p$.

````{customfigure}
:name: fig:geometric-ev

```{code-block} python
:class: toggle-code

fig, ax = plt.subplots()

p = np.arange(0.01, 1.01, 0.01)
e = (1 - p) / p

ax.plot(p, e)
ax.set_ylim(0, 10)
fig.show()
```

Grafico del valore atteso del modello geometrico in funzione del valore del suo
parametro $p$.
````

Il risultato è coerente con il significato dato a questo parametro: più il suo
valore si avvicina a $1$, più è probabile che si ottenga un successo nel primo
esperimento bernoulliano alla base della distribuzione geometrica, così che il
numero atteso di fallimenti tende a $0$. Parimenti, quando $p$ diminuisce
diventa meno probabile ottenere un successo e quindi aumenta il numero atteso
di esecuzioni dell'esperimento casuale da effettuare. In particolare, al
tendere di $p$ a zero l'esperimento bernoulliano non avrà mai successo e quindi
il numero atteso di ripetizioni tenderà a infinito.

Procedendo in modo simile a quanto abbiamo visto per il valore atteso è
possibile calcolare anche la varianza della distribuzione.

````{prf:theorem}
:label: teo:var-geometric

Data $X \sim \mathrm G(p)$ con $p \in (0, 1]$,

```{math}
\mathbb V(X) = \frac{1 - p}{p^2} \enspace.
```
````
````{admonition} _
:class: myproof

Il calcolo del momento secondo si ottiene applicando la seconda identità del
{prf:ref}`lemma:geom-ev`:

```{math}
\begin{align*}
\mathbb E(X^2) &= \sum_{x=0}^{+\infty} x^2 f_X(x; p)
                = \sum_{x=0}^{+\infty} x^2 (1 - p)^x p
                = p (1 - p) \sum_{x=0}^{+\infty} x^2 (1 - p)^{x - 1} \\
               &= p (1 - p) \frac{2 - p}{p^3}
                = \frac{(1 - p)(2 - p)}{p^2} \enspace,
\end{align*}
```

e di conseguenza

```{math}
\mathbb V(X) = \mathbb E(X^2) - \mathbb E(X)^2
             = \frac{(1 - p)(2 - p)}{p^2} - \frac{(1 - p)^2}{p^2}
             = \frac{1 - p}{p^2}(2 - p - 1 + p)
             = \frac{1 - p}{p^2}
```

è il valore per la varianza della distribuzione geometrica.
````

Come già fatto per il valore atteso, nella {numref}`fig:geometric-variance` è
possibile vedere l'andamento della varianza $\mathbb V(X)$ al variare del
parametro $p \in (0, 1]$ di una variabile aleatoria $X \sim \mathrm G(p)$.

````{customfigure}
:name: fig:geometric-variance

```{code-block} python
:class: toggle-code

fig, ax = plt.subplots()

x = np.arange(0.01, 1.01, 0.01)
y = list(map(lambda p: (1-p)/p**2, x))

plt.plot(x, y)
plt.ylim(0, 50)
plt.show()
```

Grafico della varianza del modello geometrico in funzione del valore del suo
parametro $p$.
````

Anche in questo caso il grafico ottenuto è coerente con l'esperimento casuale
alla base della distribuzione: al diminuire di $p$ la massa di probabilità si
concentra su un insieme sempre più grande di valori, dunque la varianza
aumenta. Quando $p=1$ il numero di insuccessi è sempre nullo e quindi la
variabile aleatoria degenera in una costante che per definizione ha varianza
nulla.


## Assenza di memoria e tempi di attesa

La distribuzione geometrica gode di una particolare proprietà, descritta
dal seguente teorema.

````{prf:theorem}
:label: teo:memoryless-geo

Dati $p \in (0, 1]$ e $X \sim \mathrm G(p)$, per ogni $x, y \in \mathbb N$
```{math}
:label: eq:memoryless-geo

\mathbb P(X \geq x+y \mid X \geq x)= \mathbb P(X \geq y) \enspace.
```
````
````{admonition} _
:class: myproof

Nella dimostrazione del {prf:ref}`teo:geometric-cdf` abbiamo visto che
$\mathbb P(X > x) = (1 - p)^{\lfloor x \rfloor +1}$, pertanto
$\mathbb P(X \geq x) = \mathrm P(X \geq \lfloor x \rfloor) =
\mathrm P(X > \lfloor x \rfloor - 1) = (1-p)^{\lfloor x \rfloor}$. Sfruttando
questo risultato otteniamo

```{math}
\begin{align*}
\mathbb P(X \geq x+y \mid X \geq x)
            &= \frac{\mathbb  P(X \geq x+y, X \geq x)}{\mathrm  P(X \geq x)}
             = \frac{\mathbb  P(X \geq x+y)}{\mathrm  P(X \geq x)} \\
            &= \frac{(1-p)^{\lfloor x \rfloor + \lfloor y \rfloor}}
                    {(1-p)^{\lfloor x \rfloor}}
            = (1-p)^{\lfloor y \rfloor}
            = \mathbb P(X \geq y) \enspace,
\end{align*}
```

e quindi la tesi è dimostrata.
````

La proprietà espressa da {eq}`eq:memoryless-geo` prende il nome di _assenza di
memoria_. Essa indica che durante la ripetizione dell'esperimento bernoulliano
alla base della distribuzione geomatrica, il fatto che sia avvenuto un numero
$n$ (anche elevato) di insuccessi consecutivi non permette di dire alcunché sul
numero di successivi insuccessi prima che si verifichi il primo successo. In
altre parole, non c'è nessuna differenza, da un punto di vista probabilistico,
dalla ripetizione degli esperimenti che vanno dal $n+1$-esimo in poi e dal
ricominciare da capo la ripetizione.

## I momenti della distribuzione geometrica (*)

Fissato $p \in (0, 1]$, la funzione generatrice dei momenti per una variabile
aleatoria $X \sim \mathrm{g}(p)$ ha la seguente forma analitica:

```{math}
:label: eq:mgf-geometric

m_X(t) = \mathbb E\left( \mathrm e^{tX} \right)
       = \sum_{x=0}^{+\infty}(1 - p)^x p \mathrm e^{tx}
       = p \sum_{x=0}^{+\infty}((1 - p) \mathrm e^t)^x
       = p (1 - (1 - p) \mathrm e^t)^{-1} \enspace,
```

ed è definita per i valori di $t$ per i quali è garantita la convergenza della
serie geometrica contenuta in {eq}`eq:mgf-geometric`, cioè quando
$| (1 - p) \mathrm e^t | < 1$, che equivale a $t < - \log(1-p)$. Pertanto le
prime quattro derivate della funzione generatrice dei momenti saranno

```{math}
\begin{align*}
m_X'(t)    = & m_X(t)^2 \frac{1 - p}{p} \mathrm e^t \enspace, \\
m_X''(t)   = & \frac{1-p}{p} \mathrm e^t (m_X(t)^2 + 2 m_X(t) m_X'(t))
               \enspace, \\
m_X'''(t)  = & \frac{1-p}{p} \mathrm e^t ( m_X(t)^2 + 4 m_X(t) m_X'(t)
             + 2 m_X'(t)^2 + 2 m_X(t) m_X''(t)) \enspace, \\
m_X^{\mathrm{IV}}(t) = & \frac{1-p}{p} \mathrm e^t ( m_X(t)^2 + 6 m_X(t) m_X'(t) +
               6 m_X'(t)^2 + 6 m_X(t) m_X''(t) + 6 m_X'(t) m_X''(t)
               + 2 m_X(t) m_X'''(t) ) \enspace.
\end{align*}
```

Pertanto:
- $\mathbb E(X) = m_X^\prime(0) = \frac{1-p}{p}$, a conferma di quanto abbiamo
  ricavato nel {prf:ref}`teo:mean-geometric`;
- $\mathbb E(X^2) = m_X^{\prime(0)\prime} = \frac{(1 - p)(2 - p)}{p^2}$, come
  ottenuto nella dimostrazione del {prf:ref}`teo:var-geometric`;
- i momenti terzo e quarto sono rispettivamente $\mu_3^\prime =
  m_X^{\prime\prime\prime}(0) = \frac{(1-p)(p^2 -6p + 6)}{p^3}$ e $\mu^\prime_4
  = m_X^{\mathrm{IV}}(0) = \frac{1-p}{p} (24 - 36p + 14p^2 - p^3)$. 

Per calcolare i momenti centrali si può utilizzare il
{prf:ref}`teo:central-moments`: posto $Y \triangleq X - \frac{1-p}{p}$ si ha

```{math}
\begin{align*}
m_Y'(t)  &= \mathrm e^{-t\frac{1-p}{p}}
            \left( m_X'(t) - \frac{1-p}{p} m_X(t) \right) \enspace, \\
m_Y''(t) &= \mathrm e^{-t\frac{1-p}{p}}
            \left( m_X''(t) - 2 \frac{1-p}{p} m_X'(t) +
                       \left( \frac{1-p}{p} \right)^2 m_X(t) \right) \enspace,
\end{align*}
```

e pertanto i primi due momenti centrali sono $\mu_1 = m_Y^\prime(0) = 0$, come
deve necessariamente essere, e $\mu_2 = m_Y^{\prime\prime}(0) = \frac{1 -
p}{p^2}$, che coincide con la varianza della distribuzione geometrica ricavata
nel {prf:ref}`teo:var-geometric`. Analogamente

```{math}
m_Y'''(t) = \mathrm e^{-t\frac{1-p}{p}} \left( m_X'''(t)
            - 3 \frac{1-p}{p} m_X''(t)
            + 3 \left( \frac{1-p}{p} \right)^2 m_X'(t)
            - \left( \frac{1-p}{p} \right)^3 m_X(t) \right) \enspace,
```

da cui si ricava che il terzo momento centrale è

```{math}
\mu_3 = m_Y'''(0) = \frac{(1- p)(2 - p)}{p^3}
```

e quindi la skewness della distribuzione è pari a

```{math}
\frac{\mu_3}{\sigma^3} = \frac{(1- p)(2 - p)}{p^3} \frac{p^3}{(1-p)^{3/2}}
                       = \frac{2-p}{\sqrt{1-p}} \enspace.
```

Infine,

```{math}
m_Y^{\mathrm{IV}}(t) = \mathrm e^{-t\frac{1-p}{p}} \left( m_X^{\mathrm{IV}}(t)
            - 4 \frac{1-p}{p} m_X'''(t)
            + 6 \left( \frac{1-p}{p} \right)^2 m_X''(t)
            - 4 \left( \frac{1-p}{p} \right)^3 m'_X(t)
            + \left( \frac{1-p}{p} \right)^4 m_X(t) \right)
```

e

```{math}
\mu_4 = m_Y^{\mathrm{IV}}(0) = \frac{1-p}{p^4}(p^2 -9p + 9) \enspace,
```

e pertanto la curtosi della distribuzione geometrica è

```{math}
\frac{\mu_4}{\sigma^4} - 3 =
      \frac{1-p}{p^4}(p^2 -9p + 9) \frac{p^4}{(1 - p)^2} - 3
      = 6 + \frac{p^2}{1 - p} \enspace,
```

che è sempre strettamente positiva, il che rende la distribuzione leptocurtica:
tenderà a produrre più valori fuori scala se confrontata con una distribuzione
normale con gli stessi valore atteso e deviazione standard. Questo fatto è
abbastanza ovvio, avendo la distribuzione geometrica una coda a destra. In
particolare, più $p$ si avvicina a $1$ e più la curtosi aumenta, coerentemente
con il fatto che in questi casi la distribuzione tende a degenerare alla
costante $0$. La {numref}`fig:geometric-sc-graph` illustra il grafico
skewness-curtosi per la famiglia delle distribuzioni geometriche.

````{customfigure}
:name: fig:geometric-sc-graph

```{code-block} python
:class: toggle-code

fig, ax = plt.subplots()

p = np.linspace(0.01, 0.99, 300)
skewness = (2 - p) / (1 - p)**0.5
kurtosis = 6 + p**2 / (1 - p)

plt.plot(skewness, kurtosis)
plt.show()
```

Il grafico skewness-curtosi del modello geometrico.
````


## Quantili della distribuzione geometrica

Abbiamo visto nel {prf:ref}`teo:geometric-cdf` come nella distribuzione geometrica
sia possibile semplificare la sommatoria alla base del calcolo della funzione
di ripartizione. Questo permette di calcolare in modo abbastanza agevole un
generico quantile della distribuzione. Infatti, dato $p \in (0, 1]$ e
applicando {eq}`eq:geometric-cdf` a una variabile aleatoria
$X \sim \mathrm G(p)$, dato un generico livello $q \in [0, 1]$ si ha

```{margin}
Nel penultimo passaggio si utilizza il logaritmo in base due per semplificare
i conti che seguono, ma si sarebbe potuta considerare una qualsiasi altra base
ottenendo un risultato analogo.
```
```{math}
\begin{align*}
x_q &= \min_x \left\{ F_X(x; p) \geq q \right\} = \min_x
       \left\{ 1 - (1 - p)^{\lfloor x \rfloor + 1} \geq q \right \}
     = \min_x \left\{ (1 - p)^{\lfloor x \rfloor + 1} \leq 1 - q \right \} \\
    &= \min_x \left\{ \lfloor x \rfloor \geq
                         \frac{\log_2 (1 - q)}{\log_2 (1 - p)} - 1 \right \}
     = \left\lceil \frac{\log_2 (1 - q)}{\log_2 (1 - p)} \right\rceil - 1
       \enspace.
\end{align*}
```

Pertanto la mediana, il primo e il terzo quartile della distribuzione saranno

```{math}
\begin{align*}
x_{1/2} &= \left\lceil \frac{\log_2 \frac{1}{2}}{\log_2 (1 - p)}
                                                           \right\rceil - 1
         = \left\lceil \frac{-1}{\log_2 (1 - p)} \right\rceil - 1 \enspace, \\
x_{1/4} &= \left\lceil \frac{\log_2 3 -2}{\log_2 (1 - p)} \right\rceil - 1
                                                                  \enspace, \\
x_{3/4} &= \left\lceil \frac{-2}{\log_2 (1 - p)} \right\rceil - 1 \enspace,
\end{align*}
```

come evidenziato nel diagramma a scatola di {numref}`fig:geometric-boxplot`,
nel quale ho fissato $p = 0.2$. Il baffo a destra della scatola è parzialmente
tratteggiato per enfatizzare il fatto che si estende fino a $+\infty$.

````{customfigure}
:name: fig:geometric-boxplot

```{code-block} python
:class: toggle-code

fig, ax = plt.subplots(figsize=(6, 0.3))

p = 0.2
third_quartile = np.ceil(-2 / np.log2(1 - p)) - 1
median = np.ceil(-1 / np.log2(1 - p)) - 1
first_quartile = np.ceil((np.log2(3) - 2) / np.log2(1 - p)) - 1

lw = 1
height = 0.2

plt.plot([median, median], [-height, height], c='k', linewidth=1.5)

plt.plot([0, 0], [-.1, .1], c='k', linewidth=lw)
plt.plot([0, first_quartile], [0, 0], c='k', linewidth=lw)

plt.plot([first_quartile, first_quartile], [-height, height],
         c='k', linewidth=lw)

plt.plot([third_quartile, third_quartile], [-height, height],
         c='k', linewidth=lw)

plt.plot([first_quartile, third_quartile], [height, height],
         c='k', linewidth=lw)
plt.plot([first_quartile, third_quartile], [-height, -height],
         c='k', linewidth=lw)

plt.plot([third_quartile, third_quartile*1.2], [0, 0], c='k', linewidth=lw)
plt.plot([third_quartile*1.2, third_quartile*1.5], [0, 0],
         'k--', linewidth=lw)

plt.text(0, -0.5, '0', ha='center')
plt.text(median+.2, -0.6,
         f'{median}',
         ha='center')

plt.text(first_quartile+.5, 0.6,
         f'{first_quartile}',
         ha='center')

plt.text(third_quartile+.1, 0.6,
         f'{third_quartile}',
         ha='center')

plt.axis('off')
pad = .5
plt.xlim(0-pad, third_quartile*1.5+pad) 
plt.show()
```

Diagramma a scatola della distribuzione geometrica di parametro $p = 0.2$.
````

## Implementazione della distribuzione geometrica

Un modo intuitivo di simulare l'estrazione di valori da una distribuzione
geometrica consiste nel ripetere l'esecuzione del corrispondente esperimento
bernoulliano, fermandosi quando si ottiene il primo successo e restituendo il
numero di tentativi effettuati. Partendo dalla classe `bernoulli` implementata
in `scipy.stats`, è possibile definire in modo semplice la seguente funzione
che permette di simulare una generica distribuzione geometrica, specificando il
valore del corrispondente parametro come argomento.

```{margin}
Questa implementazione verifica anche che il valore del parametro della
distribuzione sia valido.
```
```python
from scipy.stats import bernoulli

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
efficienti per simulare la distribuzione geometrica, per esempio evitando l'uso
di cicli. È questo l'approccio seguito dalla classe `geom` fornita dal package
`scipy.stats`, che nella {numref}`fig:geometric-simulation` viene utilizzata
per generare una sequenza in modo analogo a quanto fatto usando la funzione
`geom_rv` nell'esempio precedente.

````{customfigure}
:name: fig:geometric-simulation

```python
from scipy.stats import geom

g = geom(.3, loc=-1)
g.rvs(10)
```

```{code-block} python
:class: toggle-code 

from pyodide.ffi import create_proxy
import io
import base64

def geometric_simulation(p, m):
    x_max = 7
    fig, ax = plt.subplots()

    G = geom(p, loc=-1)
    x = G.rvs(m)
    freq = pd.Series(x).value_counts(normalize=True)
    freq = freq.reindex([0, 1], fill_value=0).values
    ax.bar([0, 1], freq, facecolor='lightgray', edgecolor='gray', width=.4)

    s = np.arange(0, x_max+1)
    ax.vlines(s, 0, G.pmf(s))
    ax.plot(s, G.pmf(s), 'o')

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
    Element("simulation-output").write(img_html)

    msg = "Campione: {" + ",".join(map(str, x[:30])) + "}"
    Element("sample-excerpt").write(msg)
    
    plt.close(fig)

def update_simulation(event=None):
    p = float(document.getElementById("p-sim-slider").value)
    document.getElementById("p-sim-value").innerText = f"{p:.1f}"
    m = int(document.getElementById("m-sim").value)
    geometric_simulation(p, m)


p_slider = document.getElementById("p-sim-slider")
p_slider.addEventListener("input", create_proxy(update_simulation))

m_menu = document.getElementById("m-sim")
m_menu.addEventListener("change", create_proxy(update_simulation))

# Initial plot
geometric_simulation(0.5, 50)
```
```{raw} html

<div id="sample-excerpt" float:right;></div>
<div id="plot-container" style="visibility: none;">
    <div class="slider-container" style="float: left;">
        <label for="p-sim-slider">\( p \): </label>
        <input type="range" id="p-sim-slider"
               min="0" max="1" value="0.5" step="0.05" />
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

    <div id="simulation-output" class="no-mathjax"
            style="clear: both; display: flex;
                   justify-content: center; margin-bottom: 2em;">
    </div>
</div>
```

Diagramma a barre delle frequenze di un insieme di osservazioni estratte da
un modello geometrico, sovrapposto al diagramma a bastoncini della
corrispondente funzione di massa di probabilità.
````
