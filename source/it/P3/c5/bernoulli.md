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

(sec:modello-bernoulliano)=
# Le distribuzioni di Bernoulli

Il tipo più semplice di modello casuale è quello nel quale l'esecuzione di
un esperimento ha due soli possibili esiti. Esperimenti di questo tipo,
che vengono tipicamente chiamati _esperimenti di Bernoulli_, danno luogo a
una famiglia di distribuzioni di probabilità che è anch'essa detta
_famiglia di Bernoulli_.

## Il modello di Bernoulli

Si usa generalmente il termine _esperimento di Bernoulli_ per indicare un
esperimento casuale ha due soli possibili esiti, che vengono convenzionalmente
indicati come «successo» e «fallimento», così che lo spazio degli eventi
risulta essere  $\Omega = \{ \text{fallimento}, \text{successo} \}$. 

```{prf:example}
:label: ex:bernoulli

Le denominazioni «successo» e «fallimento» non hanno generalmente le
connotazioni positive e negative che diamo loro nel linguaggio comune, ma come
_etichette_ usate per rappresentare in modo astratto i due esiti
dell'esperimento in questione. Se l'esecuzione dell'esperimento consiste
nel selezionare secondo qualche criterio non deterministico un fumetto
all'interno di una pila, il successo potrebbe essere associato all'estrazione
di un volume
- con una pagina strappata,
- che contiene almeno una storia della nostra supereroina preferita,
- in cui c'è almeno una vignetta con un personaggio che indossa un
  cappotto blu.

In linea generale, queste tre situazioni vengono valutate rispettivamente in
modo negativo, positivo e neutro, ma in tutti i casi ci stiamo riferendo al
successo in un esperimento di Bernoulli. Vale la pena sottolineare che
in modo del tutto analogo potremmo pensare a esperimenti di Bernoulli,
un un certo senso duali rispetto a quelli sopra indicati, nei quali i medesimi
avvenimenti identificano il fallimento.
```

Dato un generico esperimento di Bernoulli, sia $p \in [0, 1]$ la probabilità
di ottenere un successo come esito. La variabile aleatoria
$X: \Omega \to \{ 0, 1 \}$ definita in modo tale che

```{math}
X(w) = \begin{cases}
       0 & \text{se $w = \text{fallimento}$,} \\
       1 & \text{se $w = \text{successo}$,}
       \end{cases}
```

segue una distribuzione detta _di Bernoulli_, parametrizzata rispetto alla
probabilità di successo $p$ e il cui supporto è l'insieme $\{ 0, 1 \}$.
Chiaramente, gli eventi $X =0$ e $X = 1$ avranno rispettivamente probabilità
uguali a $1 - p$ e $p$, da cui segue la prossima definizione.

````{prf:definition} La famiglia delle distribuzioni di Bernoulli
:label: def:bernoulli-distribution

Dato $p \in [0, 1]$, la distribuzione di Bernoulli di parametro $p$ è
definita dalla funzione di massa di probabilità

```{math}
f(x; p) = p^x (1 - p)^{1 - x} \mathrm I_{\{ 0, 1 \}}(x)
```

o, equivalentemente, dalla funzione di ripartizione

```{math}
F(x; p) = (1 -  p) \mathrm I_{[0, 1)}(x) + \mathrm I_{[1, +\infty)}(x) \enspace.
```

Scriveremo $X \sim \mathrm B(p)$ per indicare che la variabile aleatoria $X$
segue una distribuzione di Bernoulli di parametro $p$. L'insieme di tutte
le distribuzioni di Bernoulli al variare dei possibili valori per il
relativo parametro viene detta _famiglia delle distribuzioni di Bernoulli_.
````

Chiaramente, la visualizzazione di questo tipo di funzione di massa di
probabilità consiste nel mostrare due bastoncini aventi ascisse nulla e
unitaria e altezza uguale a $1-p$ e $p$, mentre la funzione di ripartizione
avrà un grafico costante a tratti, con due salti posizionati nelle stesse
ascisse: il primo cambierà l'ordinata da $0$ a $1 - p$ e il secondo la
modificherà da quest'ultimo valore a $1$, come evidenziato nella
{numref}`fig:bernoulli-pdf-cdf`, nella quale la spezzata blu mostra il grafico
della funzione di ripartizione e il grafico a bastoncini indica la funzione di
massa di probabilità. Modificando il valore del parametro $p$ agendo sul
relativo selettore si può vedere come cambiano i due grafici.

````{customfigure}
:name: fig:bernoulli-pdf-cdf

```{code-block} python
:class: toggle-code 

import numpy as np
import scipy.stats as st
from js import document
from pyodide.ffi import create_proxy
import io
import base64

def bernoulli_pdf_cdf(p):
    fig, ax = plt.subplots()

    B = st.bernoulli(p)

    ax.hlines([0, B.pmf(0), 1], [-1, 0, 1], [0, 1, 2])

    ax.vlines([0, 1], 0, [B.pmf(0), B.pmf(1)], color='k')
    ax.plot([0, 1], [B.pmf(0), B.pmf(1)], 'o')

    ax.set_title(f'p = {p:.2f}')
    
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
    p = float(document.getElementById("p-slider").value)
    document.getElementById("p-value").innerText = f"{p:.1f}"
    bernoulli_pdf_cdf(p)


p_slider = document.getElementById("p-slider")

p_slider.addEventListener("input", create_proxy(update_plot))

# Initial plot
bernoulli_pdf_cdf(0.5)
```
```{raw} html

<div id="plot-container" style="visibility: none;">
    <div class="slider-container" style="float: left;">
        <label for="p-slider">\( p \): </label>
        <input type="range" id="p-slider"
               min="0" max="1" value="0.5" step="0.05" />
        <span id="p-value">0.5</span>
    </div>

    <div id="pdf-cdf-output" class="no-mathjax"
            style="clear: both; display: flex;
                   justify-content: center; margin-bottom: 2em;">
    </div>
</div>
```

I grafici della funzione di massa di probabilità e di ripartizione del modello
Bernoulliano.
````


```{figure} https://upload.wikimedia.org/wikipedia/commons/1/19/Jakob_Bernoulli.jpg
---
figclass: margin
name: fig:jakob-bernoulli
width: 200px
align: left
---
Ritratto di Jakob Bernoulli (immagine di pubblico dominio, disponibile su
wikimedia).
```
````{admonition} Nomenclatura
:class: naming

Questa distribuzione deve il suo nome allo scienziato svizzero Jakob
Bernoulli (ritratto nella {numref}`fig:jakob-bernoulli`, e da non
confondere con il figlio Daniel, anch'esso noto matematico), che la introduce
nel suo libro «Ars Conjectandi», considerato una tra le prime  opere che
trattano della teoria delle probabilità. Nella terminologia comune, e in
alcuni casi anche in fonti scritte in lingua italiana, è abbastanza comune
rimpiazzare la dicitura "di Bernoulli" con l'aggettivo _bernoulliano_, o
perfino _bernulliano_ (in alcuni casi con iniziale maiuscola) quando si vuole
definire un esperimento di questo tipo o le distribuzioni e variabili
aleatorie ad esso collegate. Dunque è possibile imbattersi nelle diciture
«esperimento bernoulliano», «distribuzione Bernoulliana», «variabile aleatoria
bernoulliana» e così via.
````

## Valore atteso e varianza della distribuzione di Bernoulli

Il fatto che siano presenti due sole specificazioni permette di ottenere
agevolmente il valore atteso e la varianza della distribuzione calcolando
estensivamente le sommatorie alla base dei corrispondenti valori attesi.
Infatti, data una variabile aleatoria $X \sim \mathrm B(p)$,

```{math}
\mathbb E(X) = \sum_{i=0}^1 i \; \mathbb P(X = i)
             = 0 \cdot (1 - p) + 1 \cdot p
             = p \enspace.
```

D'altra parte, $X^2 = X$ perché elevare $0$ oppure $1$ al quadrato non ne
cambia il valore, e quindi $\mathbb E(X^2) = \mathbb E(X) = p$, il che implica
$\mathrm{Var}(X) = \mathbb E(X^2) - \mathbb E(X)^2 = p - p^2 = p (1 - p)$.

La distribuzione di Bernoulli è decisamente semplice da trattare, essendo
la relativa algebra formata dai soli quattro eventi

```{math}
\mathcal A = \{ \emptyset, \text{fallimento}, \text{successo}, \Omega \}
```


che hanno rispettivamente probabilità $0$, $1-p$, $p$ e $1$. Normalmente,
la parte più impegnativa legata al calcolo delle probabilità di questi eventi
consiste nel determinare correttamente il valore del parametro $p$ partendo
dalla descrizione dell'esperimento di Bernoulli dal quale si parte. In alcuni
casi la probabilità di successo si determina in modo elementare, mentre in
altri è necessario ricorrere alle tecniche di combinatorica che abbiamo visto
nel {ref}`chap:calcolo-combinatorio`.

````{prf:example}
:label: ex:bernoulli

Uno scatolone contiene 50 albi di fumetti, in dodici dei quali compare una e
una sola storia con Aquaman come protagonista, mentre nei restanti albi
Aquaman non compare mai. Scelgo a caso due albi dallo scatolone e indico con
$X$ la variabile aleatoria che assume il valore $1$ quando negli albi che ho
pescato posso leggere due storie diverse di Aquaman, e che vale $0$ in tutti
gli altri casi. Chiaramente $X$ segue una distribuzione di Bernoulli, e il
suo parametro è uguale alla probabilità $p$ che selezionando due albi dai 50 a
disposizione, entrambi facciano parte del gruppo di dodici che parlano di
Aquaman. A sua volta, $p$ è uguale al rapporto tra il numero di combinazioni
di dodici oggetti in due posti (il numero di casi favorevoli) e il numero di
combinazioni di cinquanta oggetti in due posti (il numero di casi possibili),
pertanto

```{math}
p = \frac{\binom{12}{2}}{\binom{50}{2}} = \frac{12 \cdot 11}{50 \cdot 49}
    \approx 0.054 \enspace,
```

e dunque $X \sim \mathrm B(0.054)$. Pertanto
- la probabilità di non pescare albi con due storie di Aquaman differenti è
  $\mathbb P(X = 0) = 0.946$, e
- $\mathbb E(X) = 0.054$, il che significa che mediamente possiamo aspettarci
  che in poco più di cinque volte su cento selezioni casuali di due albi si
  arrivi a pescarne due con due storie diverse di Aquaman.

Se sapessimo che sei delle dodici copie in questione sono dei doppioni tutti
identici tra loro, ci troveremmo di fronte a una variabile aleatoria $X'$ che
segue ancora distribuzione di Bernoulli, ma in questo il calcolo del relativo
parametro richiede un po' più di perizia. In particolare, quello che si
complica è il calcolo del numero di casi favorevoli. Per ottenerlo possiamo
seguire, per esempio, uno dei due seguenti ragionamenti:

- il numero di modi di scegliere due albi dai dodici a
  disposizione è $\binom{12}{2} = 66$, ma $\binom{6}{2} = 15$ di questi
  corrispondono a coppie che contengono due albi uguali, dunque il numero di
  coppie con albi distinti è $66 - 15 = 51$;
- ci sono $\binom{6}{2} = 15$ modi di comporre una coppia considerando solo
  gli albi di cui possediamo un'unica copia, e a questi   bisogna aggiungere
  $6 \cdot 6 = 36$, che corrisponde al numero di possibili coppie che
  contengono uno dei doppioni e un altro albo; il risultato è, anche in questo
  caso, $51$.

La probabilità $p^\prime$ di estrarre due albi con due storie diverse di
Aquaman in è quindi

```{math}
p^\prime = \frac{51}{\frac{50 \cdot 49}{2}} \approx 0.041 \enspace.
```

Riassumendo, $X^\prime \sim \mathrm B(0.042)$, il che significa ad esempio che
la media del numero di volte in cui si arriva a leggere due storie diverse di
Aquaman scende a poco più di quattro volte su cento.
````

## Momenti della distribuzione di Bernoulli (*)

La funzione generatrice dei momenti per una distribuzione di Bernoulli si
ottiene facilmente, assumendo questa distribuzione solamente due
specificazioni. Infatti, dati $p \in [0, 1]$ e $X \sim \mathrm B(p)$,

```{math}
m_X(t) = \mathbb E\left( \mathrm e^{tX} \right)
       = (1 - p) \mathrm e^0 + p \mathrm e^t
       = 1 + p \left( \mathrm e^t - 1 \right) \enspace.
```

Pertanto il momento primo della distribuzione è

```{math}
\mu = m_X^\prime(0) = \left. p \mathrm e^t \right|_{t=0} = p \enspace,
```

che coincide con il valore atteso che abbiamo già calcolato. Per quanto
riguarda invece i momenti centrali, poniamo $Y \triangleq X - p$ e calcoliamo

```{math}
m_Y(t) = \mathbb E \left( \mathrm e^{tY} \right)
       = (1 - p) \mathrm e^{-tp} + p \mathrm e^{t(1-p)} \enspace,
```

così che il momento centrale $n$-esimo sarà uguale a

```{math}
\begin{align*}
\mu_n = m_Y^{(n)}(0) &= \left. p (1 - p)
                        \left( (1 - p)^{n-1} \mathrm e^{t(1-p)}
                               + (-1)^n p^{n-1} \mathrm e^{-tp} \right)
                       \right|_{t=0} \\
                     &= p (1 - p)
                        \left( (1 - p)^{n-1} + (-1)^n p^{n-1} \right)
                        \enspace.
\end{align*}
```

Dunque possiamo concludere che per una distribuzione di Bernoulli di parametro
$p$

- la varianza è $p (1 - p)$, come già calcolato;
- il momento centrale terzo è $\mu_3 =p(1 - p)(1 - 2p)$, così che la skewness
  vale
  ```{math}
  \frac{\mu_3}{\sigma^3} = \frac{p(1 - p)(1 - 2p)}{(p(1 - p))^{3/2}}
                         = \frac{1 - 2p}{\sqrt{p(1 - p)}}
  ```
  e la distribuzione è asimmetrica verso sinistra, simmetrica e asimmetrica
  verso destra rispettivamente a seconda del fatto che $p$ sia minore di,
  uguale a oppure maggiore di $\frac{1}{2}$;
- il momento centrale quarto è uguale a $\mu_4 = p(1 - p)(1 - 3p + 3p^2)$ e
  pertanto la curtosi sarà
  ```{math}
  \frac{\mu_4}{\sigma^4} - 3 = \frac{(1 - 3p + 3p^2)}{p(1 - p)} - 3
                             = \frac{1 - 6p(1-p)}{p(1 - p)}
                             = \frac{1}{p(1-p)} - 6 \enspace.
  ```

Questo ultimo punto merita una riflessione più approfondita: la curtosi è
positiva, e dunque la distribuzione è leptocurtica, quando $p$ si trova
all'interno dell'intervallo

```{math}
\left[ \frac{1}{2} - \frac{1}{\sqrt{12}},
       \frac{1}{2} + \frac{1}{\sqrt{12}} \right] \enspace,
```

mesocurtica quando lo stesso parametro coincide con uno degli estremi di questo
intervallo e platicurtica nei casi rimanenti. Informalmente, questo risultato
riflette il fatto che quando $p$ si avvicina a $0$, la distribuzione di
Bernoulli tenderà a produrre sempre più raramente la specificazione $1$, che
sarà dunque assimilabile a un valore fuori scala. Un comportamento analogo si
ha ovviamente quando $p$ approssima $1$ (con $0$ che diventa ) Al contrario,
più $p$ si avvicina a $\frac{1}{2}$ e più le due specificazioni diventano
equiprobabili, così che la distribuzione tenderà sempre di meno a produrre
valori fuori scala, e quindi a essere leptocurtica. In particolare, si può
dimostrare che per $p = \frac{1}{2}$ si ottiene la più platicurtica delle
distribuzioni. La {numref}`fig:bernoulli-sc-graph` illustra il grafico
skewness-curtosi per la famiglia delle distribuzioni di Bernoulli.

````{customfigure}
:name: fig:bernoulli-sc-graph

```{code-block} python
:class: toggle-code

fig, ax = plt.subplots()

p = np.linspace(0.01, 0.99, 300)
skewness = (1 - 2*p) / (p * (1 - p))**0.5
kurtosis = 1 / (p * (1 - p)) - 6

plt.plot(skewness, kurtosis)
plt.show()
```

Il grafico skewness-curtosi per il modello di Bernoulli.
````

(sec:bernoulli_quantiles)=
## Quantili della distribuzione di Bernoulli (*)

La distribuzione di Bernoulli ha solo due specificazioni, e di conseguenza
la sua funzione di ripartizione assume al massimo tre valori distinti, e ciò
ha un notevole impatto sui quantili della distribuzione stessa. Consideriamo
pertanto una variabile aleatoria $X \sim \mathrm B(p)$ e analizziamo
innanzitutto il caso $p \in (0, 1)$, per il quale si ha

```{math}
F_X(x) = \begin{cases}
    0     & \text{per $x < 0$} \enspace, \\
    1 - p & \text{per $0 \leq x < 1$} \enspace,  \\
    1     & \text{per $x \geq 1$} \enspace.
\end{cases}
```

Dato un generico livello $q \in (1-p, 1]$ si avrà

```{math}
x_q = \arg\min_x \{ F_X(x) \geq q \} = \arg\min_x \{ F_X(x) = 1 \}
    = \arg\min_x \{ x \geq 1 \} = 1 \enspace.
```

Analogamente, per ogni livello $q \in (0, 1-p]$

```{math}
x_q = \arg\min_x \{ F_X(x) \geq q \} = \arg\min_x \{ F_X(x) = 1-p \}
    = \arg\min_x \{ x \geq 0 \} = 0 \enspace.
```

Riassumendo, $0$ è il quantile per tutti i livelli $q \in (0, 1-p]$ e $1$
è il quantile per tutti i livelli successivi.

Rimangono da analizzare i casi $p = 0$ e $p = 1$. Consideriamo il secondo, nel
quale la variabile aleatoria degenera nella costante $1$, così che la sua
funzione di ripartizione diventa

```{math}
F_X(x) = \begin{cases}
    0     & \text{per $x < 1$} \enspace, \\
    1     & \text{per $x \geq 1$} \enspace,
\end{cases}
```

e quindi per ogni $q > 0$ si ha $x_q = \arg\min_x \{ F_X(x) \geq q \}
= \arg\min_x \{ F_X(x) = 1 \} = \arg\min_x \{ x \geq 1 \} = 1$. Dunque
il quantile di qualsiasi livello non nullo è uguale a $1$. Si verifica
facilmente che si ottiene un risultato analogo quando $p = 0$, con l'unica
differenza che ora, sempre indipendentemente dal livello $q > 0$, il quantile
è uguale a $0$.

Essendo i quantili per la distribuzione di Bernoulli sempre uguali a $0$ o a
$1$, non risulta affatto utile disegnare il suo diagramma a scatola, perché
si otterrebbe sempre un grafico senza scatola o senza baffi. Più precisamente,

- quando $0 < p \leq \frac{1}{4}$ il primo e il terzo quartile, e quindi anche
  la mediana, sono uguali a $0$, dunque la scatola del diagramma collassa in
  un segmento verticale sovrapposto all'estremo del baffo sinistro;
- quando $\frac{1}{4} < p \leq \frac{1}{2}$ il primo quartile e la mediana
  si annullano mentre il terzo quartile è uguale a $1$, quindi la scatola
  occupa tutto l'intervallo $[0, 1]$ e i baffi scompaiono, e il segmento che
  evidenzia la mediana coincide con l'estremo sinistro della scatola;
- quando $\frac{1}{2} < p \leq \frac{3}{4}$ il primo quartile è nullo mentre
  la mediana e il terzo quartile sono uguali a $1$, pertanto il grafico è
  analogo a quello descritto nel punto precedente, con l'unica differenza che
  la mediana è evidenziata sovrapponendola all'estremo destro della scatola;
- quando $\frac{3}{4} < p \leq 1$ i primi tre quartili sono tutti uguali a
  $1$, quindi la scatola collassa in un segmento verticale sovrapposto
  all'estremo del baffo destro. 

I diagrammi riportati in {numref}`fig:bernoulli-boxplot` riepilogano questi
quattro casi.

````{customfigure}
:name: fig:bernoulli-boxplot

```{code-block} python
:class: toggle-code

lw = 1
height = 0.1

def bernoulli_bp(q1, m, q3, ax, label):

    ax.plot([m, m], [-height, height*0.95], c='k', linewidth=1.8)

    ax.plot([0, 0], [-.05, .05], c='k', linewidth=lw)
    ax.plot([0, q1], [0, 0], c='k', linewidth=lw)

    ax.plot([q1, q1], [-height, height],
            c='k', linewidth=lw)

    ax.plot([q3, q3], [-height, height],
            c='k', linewidth=lw)

    ax.plot([q1, q3], [height, height],
            c='k', linewidth=lw)
    ax.plot([q1, q3], [-height, -height],
            c='k', linewidth=lw)

    ax.plot([q3, q3], [-height, height],
            c='k', linewidth=lw)
    ax.plot([q3, 1], [0, 0], 'k', linewidth=lw)
    ax.plot([1, 1], [-0.05, 0.05], 'k', linewidth=lw)

    ax.text(0, -.21, '0', ha='center')
    ax.text(1, -.21, '1', ha='center')
    ax.text(0.5, .18, label, ha='center')

    ax.set_ylim(-.3, .3)

fig, axes = plt.subplots(2, 4,figsize=(8, 3))
bernoulli_bp(0, 0, 0, axes[0, 1], r'$0 < p \leq \frac{1}{4}$')
bernoulli_bp(0, 0, 1, axes[0, 2], r'$\frac{1}{4} < p \leq \frac{1}{2}$')
bernoulli_bp(0, 1, 1, axes[1, 1], r'$\frac{1}{2} < p \leq \frac{3}{4}$')
bernoulli_bp(1, 1, 1, axes[1, 2], r'$\frac{3}{4} < p < 1$')

for a in axes.flatten():
    a.axis('off')

plt.show()
```

I quattro possibili boxplot per le distribuzioni di Bernoulli.
````

Nella figura non sono contemplati i casi $p = 0$ e $p = 1$, per i quali la
distribuzione è degenere e le variabili aleatorie corrispondenti vanno
rispettivamente a coincidere con le costanti $0$ e $1$, e dunque i primi tre
quartili, così come il minimo e il massimo delle specificazioni, coincidono
queste costanti. Pertanto, l'intero diagramma collassa in un segmento
verticale posizionato nel primo caso nell'ascissa nulla e nel secondo in
quella unitaria.



## Implementazione della distribuzione di Bernoulli (*)

Il modulo `scipy.stats` contiene una serie di classi che implementano le
famiglie di distribuzioni comunemente utilizzate, e in particolare tutte
quelle che descritte in questo libro. Più precisamente, ogni classe
corrisponde a una famiglia di distribuzioni, e gli oggetti di una di queste
classi implementano una distribuzione della famiglia per la quale sono stati
specificati tutti i parametri. Su questi oggetti è possibile invocare metodi
che permettono di calcolare automaticamente gli indici e le funzioni associati
alla distribuzione che abbiamo studiato. Il punto di partenza per ottenere un
siffatto oggetto non è il costruttore della classe, bensì una funzione
fabbrica[^factory] specificamente progettata per creare le istanze e
restituirle. Questa funzione ha un nome che ricorda quello della famiglia a
cui essa fa riferimento, e per quanto riguarda le distribuzioni discrete
essa accetta un argomento per ogni valore dei parametri coinvolti.
Per quanto riguarda le distribuzioni di Bernoulli, questa funzione si chiama
(banalmente) `bernoulli`, e la cella che segue mostra come ottenere le
corrispondenti istanze.

```{margin}
Va notato che in questa cella ho violato la convenzione che richiede di non
iniziare il nome di una variabile con una lettera maiuscola. D'altronde,
questa variabile `X` (nel contesto della programmazione) è la naturale
controparte di una variabile aleatoria $X$ (nel contesto del calcolo delle
probabilità). Per essere coerente con la notazione matematica che ho
utilizzato nel resto del libro ho scelto, in casi come questo, di utilizzare
come nome delle variabili coinvolte delle lettere maiuscole.
```

```{code-block} python
import scipy.stats as st

X = st.bernoulli(0.7)
```

Una volta istanziata una distribuzione discreta, i metodi `pmf` e `cdf`
permettono di calcolarne le funzioni di massa di probabilità e di
ripartizione.

```{code-block} python
p=0.7
fig, axes = plt.subplots(1, 2, sharey=True)

B = st.bernoulli(p)
x = np.arange(-0.1, 1.1, 0.01)

axes[0].step(x, B.cdf(x))
axes[1].vlines(B.support(), 0, B.pmf(B.support()), color='k')

for ax in axes:
    ax.set_ylim(0, 1.1)
    ax.set_xticks([0, 0.5, 1])
    ax.set_xlabel(r'$x$')

axes[0].set_ylabel(r'$F_X$', rotation='horizontal')
axes[1].set_ylabel(r'$f_X$', rotation='horizontal')
plt.show()
```

Analogamente, i metodi `mean`, `median`, `var` e `std` permettono di calcolare
valore atteso, mediana, varianza e deviazione standard della distribuzione.

```{code-block} python

print(f'Per la distribuzione di Bernoulli di parametro {p} si ha')
print(f'valore atteso {B.mean():.2f}')
print(f'mediana {B.median():.2f}')
print(f'varianza {B.var():.2f}')
print(f'deviazione standard {B.std():.2f}')
```

Inoltre, il metodo `ppf` calcola un generico quantile della distribuzione,
specificando come argomento il livello corrispondente. Per esempio, nella
cella seguente viene calcolato il range interquartile di una distribuzione di
Bernoulli di parametro $p = 0.7$ che, come abbiamo visto al termine del
Paragrafo {ref}`sec:bernoulli_quantiles` vale $1$.

```{code-block} python
B.ppf(0.75) - B.ppf(0.25)
```

```{margin}
In questo caso la funzione di massa di probabilità è mostrata utilizzando
un diagramma a barre e non uno a bastoncini, altrimenti sarebbe stato
difficile distinguere le frequenze relative del campione con le probabilità
teoriche.
```
Infine, il metodo `rvs` permette di simulare l'estrazione di specificazioni
dalla distribuzione, come nella cella seguente che ne genera $10$:

```{code-block} python
B.rvs(10)
```

Nella {numref}`fig:bernoulli-simulation` vengono simulate $5000$
osservazioni di una variabile aleatoria di Bernoulli di parametro
$\frac{1}{2}$, e il diagramma a barre delle frequenze relative del campione
ottenuto viene confrontato con il grafico a bastoncini della funzione di massa
di probabilità. Anche in questo caso, nella versione interattiva del libro
è possibile modificare il valore del parametro della distribuzione di
Bernoulli e vedere come viene modificato il grafico.

````{customfigure}
:name: fig:bernoulli-simulation

```{code-block} python
:class: toggle-code 

import numpy as np
import pandas
import scipy.stats as st
from js import document
from pyodide.ffi import create_proxy
import io
import base64

def bernoulli_simulation(p, m):
    fig, ax = plt.subplots()

    B = st.bernoulli(p)

    x = B.rvs(m)
    freq = pd.Series(x).value_counts(normalize=True)
    freq = freq.reindex([0, 1], fill_value=0).values
    ax.bar([0, 1], freq, facecolor='lightgray', edgecolor='gray', width=.1)

    ax.vlines([0, 1], 0, [B.pmf(0), B.pmf(1)])
    ax.plot([0, 1], [B.pmf(0), B.pmf(1)], 'o')

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
    bernoulli_simulation(p, m)


p_slider = document.getElementById("p-sim-slider")
p_slider.addEventListener("input", create_proxy(update_simulation))

m_menu = document.getElementById("m-sim")
m_menu.addEventListener("change", create_proxy(update_simulation))

# Initial plot
bernoulli_simulation(0.5, 50)
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
un modello di Bernoulli, sovrapposto al diagramma a bastoncini della
corrispondente funzione di massa di probabilità.
````


[^factory]: Nel contesto della progettazione del software, si utilizza il
termine _fabbrica_ (o, più spesso, l'equivalente inglese _factory_) per
indicare un disegno progettuale (anche qui, nel gergo comune si tende
piuttosto a utilizzare il termine originale _design pattern_) nel quale una
funzione o un metodo ha la responsabilità di creare oggetti che hanno una
superclasse comune. In questo caso specifico, la superclasse si chiama
`rv_discrete` e corrisponde a una generica distribuzione discreta. L'utilizzo
di questo disegno progettuale ha, tra gli altri, lo scopo di mantenere in una
parte localizzata del codice tutta la logica legata alla creazione degli
oggetti, nonché quello di permettere l'estensione del numero di differenti
tipi di oggetti che si possono creare senza che ciò richieda di intervenire
direttamente sul codice esistente. Quello dei disegni progettuali è un
argomento parecchio interessante, ma decisamente al di fuori dello scopo di
questo libro. Per approfondirlo si può fare riferimento al testo storico noto
nel gergo dei programmatori come _Gang of Four_ {cite}`gang-of-four`.