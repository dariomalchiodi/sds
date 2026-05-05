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

````{code-cell} python
:tags: [remove-cell]

import matplotlib.pyplot as plt
plt.style.use('../../_static/sds.mplstyle')
%matplotlib inline
plt.ioff()
````

(sec_dal-discreto-al-continuo)=
# Dal discreto al continuo

Dato $n \in \mathbb N$, consideriamo l'insieme $D_n = \{ \frac{i}{n},
i = 0, \dots, n \}$ e la variabile aleatoria $X_n$ definita dalla
funzione di massa di probabilità

````{math}
:label: eq_uniform
p_{X_n}(x; n) = \frac{1}{n+1} \mathrm I_{D_n}(x).
````

Chiaramente, la distribuzione di $X_n$ ricorda il modello uniforme
discreto, con la sola differenza che in questo caso il dominio include
la specificazione $0$. Supponiamo ora che $n$ assuma un valore molto
grande: dato un generico $k \in D_n$, si ha
$\mathbb P(X_n = k) = \frac{1}{n + 1}$ e dunque diventa molto vicina a
zero la probabilità che $X_n$ assuma una qualsiasi delle sue
specificazioni. Ciò non deve sembrare strano, perché queste ultime si
addensano in $[0, 1]$ man mano che $n$ cresce, pertanto specificazioni
molto vicine tra loro diventeranno praticamente indistinguibili.


````{margin}
Il multiverso è stato inizialmente introdotto per risolvere in modo
ingegnoso una serie di problemi di coerenza tra varie personificazioni
di uno stesso supereroe: per esempio Terra-Uno è popolata dai
protagonisti dei fumetti DC degli anni '60 (la cosiddetta
«Silver age»), mentre quelli introdotti precedentemente (nella
«Golden age») vivono su Terra-Due.
````
````{prf:example} Il multiverso DC
:label: ex-multiverso-dc

A partire dal 1961, e in particolare nel numero 123 di «The Flash»,
le storie dei fumetti pubblicati da DC non avvengono in un unico
universo, bensì in più universi che esistono in uno spazio comune, ma
i cui abitanti "vibrano" a frequenze diverse. Ogni universo è
identificato in modo univoco da un nome, che nella maggior parte dei
casi indica come viene denominato il pianeta Terra, e l'insieme di
tutti gli universi è chiamato multiverso [^meccanica-quantistica].
Ogni protagonista può avere caratteristiche molto diverse a seconda
del corrispondente universo: per esempio, Wonder Woman è buona quasi
sempre, ma sicuramente non su Terra-Ventidue. Ora, ipotizziamo che in
ognuno di questi universi esistano esattamente $n = 15000$ protagonisti
diversi, oguno con il proprio allineamento (buono, neutrale o cattivo).
Immaginiamo anche che esista un criterio per scegliere a caso un
universo all'interno del multiverso. La variabile aleatoria $X_n$ che
indica la frazione di protagonisti "buoni" nell'universo selezionato è
distribuita sul dominio $D_{15000}$ secondo la funzione di massa di
probabilità {eq}`eq_uniform`. Ora, ha poco senso discriminare, per
dire, tra le specificazioni $\frac{42}{15000}$, $\frac{43}{15000}$ e
$\frac{49}{15000}$, perché la loro differenza massima equivale a meno
dello $0.05\%$ del totale.
````

Prima di approfondire che cosa succede all'aumentare di $n$, calcoliamo
il valore atteso e la varianza di $X_n$, perché ci saranno utili in
seguito.

````{prf:lemma}
:label: lemma-ex_var_uniform

Il valore atteso e la varianza di $X_n$ sono rispettivamente uguali a
$\frac{1}{2}$ e a $\frac{1}{12} + \frac{1}{6 n}$.
````

````{admonition} _
:class: myproof

Applicando le formule per il calcolo di valore atteso e varianza si
ottiene:

```{math}
\begin{align*}
\mathbb E(X) &= \sum_{i=0}^n \frac{i}{n} \frac{1}{n+1}
              = \frac{1}{n(n+1)} \sum_{i=0}^n i \\
             &= \frac{1}{n(n+1)} \frac{n(n+1)}{2}
              = \frac{1}{2} \enspace;
\end{align*}
```

```{math}
\begin{align*}
\mathbb E(X^2) &= \sum_{i=0}^n \frac{i^2}{n^2} \frac{1}{n+1}
                = \frac{1}{n^2(n+1)} \sum_{i=0}^n i^2 \\
               &= \frac{1}{n^2(n+1)} \frac{n(n+1)(2n+1)}{6}
                = \frac{1}{3} + \frac{1}{6n} \enspace;
\end{align*}
```

```{math}
\mathrm{Var}(X) = \frac{1}{3} + \frac{1}{6n} - \frac{1}{4}
                = \frac{1}{12} + \frac{1}{6n} \enspace.
```

Va notato come il valore atteso sia sempre uguale a $\frac{1}{2}$
indipendentemente dal valore di $n$, come ci si può aspettare tenuto
conto del fatto che, essendo la massa di probabilità costante, la
centralità della distribuzione deve coincidere con il baricentro delle
osservazioni. Per quanto riguarda invece la varianza, è presente un
termine che dipende da $n$ ma il cui contributo tende a diventare
trascurabile man mano che questo parametro cresce.

````



Come dicevamo, valori tra loro abbastanza vicini per le specificazioni
risultano fondamentalmente equivalenti, e dunque ha più senso ragionare
in termini della probabilità che $X_n$ assuma valori in un intervallo
(anche piccolo) di specificazioni piuttosto che studiare eventi in cui
essa risulta uguale a una fissata specificazione. Calcoliamo dunque la
funzione di distribuzione cumulativa di $X_n$: fissato $x \in [0, 1]$,
esisteranno $i \in \{ 0, \dots, n \}$ ed $\epsilon < \frac{1}{n}$
tali che $x = \frac{i}{n} + \epsilon$, e pertanto

````{margin}
Siccome $n x = i + n \epsilon$ e $0 \leq n \epsilon < 1$, abbiamo
$i \leq nx < i + 1$ e dunque $i = \lfloor n x \rfloor$.
````
````{math}
:label: eq_cdf-discrete-uniform
\begin{align*}
F_{X_n} (x) &= \mathbb P(X_n \leq x)
            = \mathbb P \Big( X_n \leq \frac{i}{n} \Big) \\
            &= \frac{i+1}{n+1} = \frac{\lfloor n x \rfloor + 1}{n+1},
\end{align*}
````

così che in generale

````{math}
F_{X_n}(x) = \frac{\lfloor n x \rfloor + 1}{n+1}
             \mathrm I_{[0, 1]}(x) +
             \mathrm I_{(1, +\infty)}(x).
````

A questo punto possiamo calcolare la probabilità che $X_n$ assuma
valori in un intervallo: fissati $a, b \in [0, 1]$ con $a \leq b$
esisteranno $i, j \in \{ 0, \dots, n \}$ con $i < j$ ed
$\epsilon_1, \epsilon_2 \in [0, \frac{1}{n})$ tali che
$a = \frac{i}{n} - \epsilon_1$ e $b = \frac{j}{n} + \epsilon_2$.
Pertanto

````{margin}
In questo caso abbiamo $n a = i - n \epsilon_1$ e
$0 \leq n \epsilon_1 < 1$, quindi $i -1 \leq na < i$ e
$i = \lceil na \rceil$.
````
````{math}
\begin{align*}
\mathbb P(a \leq X_n \leq b) & =
     \mathbb P \Big( \frac{i}{n} \leq X_n \leq \frac{j}{n} \Big)
     = \sum_{k=i}^j p_{X_n}(k; n) \\
     &= \sum_{k=i}^j \frac{1}{n+1} = \frac{j-i+1}{n+1}
     = \frac{\lfloor nb \rfloor - \lceil na \rceil + 1}{n+1}.
\end{align*}
````

Prima di approfondire cosa succede quando $n \to +\infty$, osserviamo
il comportamento di questa probabilità al crescere di $n$. Usando la
disuguaglianza $x - 1 < \lfloor x \rfloor \leq x$ applicata
separatamente a $\lfloor nb \rfloor$ e $\lceil na \rceil$, e
applicando il teorema dei due Carabinieri, si ottiene

````{math}
\lim_{n \to +\infty}
\frac{\lfloor nb \rfloor - \lceil na \rceil + 1}{n+1} = b - a.
````

Nel passaggio al limite, dunque, la probabilità che la variabile
aleatoria cada nell'intervallo $[a, b]$ tende alla sua semplice
_ampiezza_. Questo risultato sarà il filo conduttore per capire come
si calcolano le probabilità nel caso continuo.

````{code-cell} python
:tags: [hide-input]

import matplotlib.pyplot as plt
import numpy as np

def cdf(x, n):
    return np.clip((np.floor(n * x) + 1) / (n + 1), 0, 1)

def cdf_graph(n, ax):
    x = np.linspace(-0.1, 1.1, 100)
    y = cdf(x, n)
    ax.step(x, y)
    ax.plot(x, np.clip(x, 0, 1), dashes=[2,], linewidth=1.2,
            color='#1f77b4')
    ax.set_xlabel(rf'$n = {n}$')

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

for i in range(1, 4):
    cdf_graph(10 * i, ax[i-1])

fig
````
````{customfigure}
:name: fig_discrete-to-continuous

Le spezzate piene mostrano i grafici della funzione di distribuzione
cumulativa di $X_n$ per $n$ rispettivamente uguale a $10$, $20$ e
$30$ (da sinistra verso destra); la spezzata tratteggiata evidenzia
il grafico di $F_X$.
````

````{margin}
In altre parole, $F_{X_n}$ è una _successione di funzioni_ della
quale consideriamo il limite in senso _puntuale_, mostrando che per
ogni $x \in \mathbb R$ si ha
$\lim_{n \to +\infty} F_{X_n}(x) = F(x)$ [^convergenza-uniforme].
````
Che cosa succede a $F_{X_n}$ se il valore di $n$ aumenta
progressivamente? Consideriamo la funzione $F: \mathbb R \to [0, 1]$
definita da

````{math}
F(x) = \begin{cases}
    0 & \text{se $x \leq 0$,} \\
    x & \text{se $0 < x \leq 1$,} \\
    1 & \text{se $x \geq 1$.}
\end{cases}
````

````{margin}

```{interactive-code} python
:class: toggle-code margin

fig = plt.figure(figsize=(5, 1))

plt.plot([2, 4], [0, 0], 'k')

plt.xticks([])
plt.yticks([])

s  = -1
spacing = {-1: -.4, 1: .2}
for x, l in zip([2, np.pi - 1, np.floor(np.pi), np.pi, 4],
                ['2', r'$\pi - 1$', r'$\lfloor \pi \rfloor$',
                 r'$\pi$', '4']):
    plt.plot([x] * 2, [-.1, .1], 'k')
    plt.text(x, spacing[s], l, ha='center', fontsize=18)
    s *= -1

plt.ylim([-.5, .5])
plt.axis('off')
plt.show()
```

Si ricava $x - 1 \leq \lfloor x \rfloor \leq x$ considerando
banalmente il fatto che un qualsiasi numero reale è necessariamente
maggiore o uguale del suo troncamento all'intero inferiore.
````

La {numref}`fig_discrete-to-continuous`, che mostra i grafici di
$F_{X_{10}}$, $F_{X_{20}}$ e $F_{X_{30}}$ affiancandoli a quello di
$F$, suggerisce l'intuizione che $F_{X_n}$ tenda a $F$ quando
$n \to +\infty$. Non è difficile provare formalmente che questa
intuizione è corretta: ricordando che per ogni $x$ vale
$x - 1 \leq \lfloor x \rfloor \leq x$,
da {eq}`eq_cdf-discrete-uniform` si verifica che

````{math}
:label: eq_cdf-continuous-uniform
\frac{n x}{n + 1} \leq F_{X_n}(x) \leq \frac{nx + 1}{n + 1},
````

````{margin}
Il teorema dei due Carabinieri, o teorema del confronto, dice che,
date tre successioni $\left\{ l_n \right\}$, $\left\{ a_n \right\}$
e $\left\{ r_n \right\}$, se $\lim_{n \to +\infty} l_n =
\lim_{n \to +\infty} r_n = \ell$ allora $\ell$ è anche il limite di
$\left\{ a_n \right\}$.
````
e applicando il teorema dei due Carabinieri si ottiene
$F_{X_n}(x) \to x = F(x)$ per ogni $x \in [0, 1]$. Estendere questo
risultato a ogni $x \in \mathbb R$ è banale [^convergenza-xn].

Notiamo che $F$ soddisfa tutti i criteri indicati nel
{prf:ref}`teo-proprieta-F`, dunque essa deve essere la funzione di
distribuzione cumulativa di una qualche variabile aleatoria $X$.
Questa variabile aleatoria è però completamente diversa da quelle che
abbiamo finora considerato: il grafico di $F$ non evidenzia
discontinuità alle quali far corrispondere i punti di massa della
distribuzione perché questa funzione è continua. D'altronde da
{eq}`eq_uniform` si vede facilmente che per ogni $x \in \mathbb R$
si ha $\lim_{n \to + \infty} p_{X_n}(x; n) = 0$, o equivalentemente
$\mathbb P(X = x) = 0$. Analogamente, dato un qualsiasi insieme
finito $A = \{ a_1, \dots, a_n \} \subseteq [0, 1]$ si avrà

````{math}
\mathbb P(X \in A) =
    \mathbb P\left(\displaystyle\cup_{i=1}^n \{a_i\}\right)
    = \sum_{i=1}^n \mathbb P(X=a_i)
    = \sum_{i=1}^n 0 = 0 .
````

In altre parole, quando $n$ tende a infinito ci troviamo di fronte a
una distribuzione che non evidenzia alcun punto di massa di
probabilità. Ciò richiede innanzitutto di definire in modo diverso il
concetto di dominio per la distribuzione stessa. Nel caso che stiamo
considerando, solo valori compresi tra $0$ e $1$ possono essere
specificazioni valide, quindi il dominio di $X$ può essere
intuitivamente individuato nell'intervallo corrispondente. Si può
inoltre verificare abbastanza facilmente che se all'inizio del
paragrafo avessimo posto $D_n = \{\frac{1}{n}, \dots, n \}$ e definito la
funzione di massa di probabilità di $X_n$ come
$p_{X_n}(x; n) = \frac{1}{n} \mathrm I_{D_n}(x)$, escludendo in
altre parole il punto di massa $0$ dal dominio, avremmo comunque
ottenuto $F$ come limite delle corrispondenti funzioni di ripartizione
quando $n \to +\infty$. Il risultato non sarebbe cambiato se avessimo
deciso di escludere il punto di massa $1$ al posto di $0$, o di
escluderli entrambi. Tenuto conto di quanto appena ricavato, possiamo
per convenzione scegliere $[0, 1]$ come dominio di $X$.

La differenza fondamentale tra $X$ e le variabili aleatorie che
abbiamo studiato finora sta proprio nel fatto che il suo dominio è un
insieme continuo. Quando questo succede, si parla di variabili
aleatorie aventi una distribuzione _continua_, o più brevemente di
_variabili aleatorie continue_. La formalizzazione di questo tipo di
variabili aleatorie e delle relative famiglie di distribuzione verrà
descritta a partire dal {ref}`sec_va-continue`: in particolare, nel
{ref}`sec_modello-uniforme-continuo` vedremo che $X$ segue una
distribuzione _uniforme continua_ sull'intervallo $[0, 1]$.

Tornando a concentrarci sul caso che stiamo analizzando, la mancanza
di punti di massa di probabilità richiede di rimpiazzare la
corrispondente funzione con un altro strumento che permetta di
calcolare le probabilità di eventi che coinvolgono $X$. La risposta è
già nascosta nella funzione di ripartizione $F$ che abbiamo appena
costruito.
Ricordiamo che $F(x)$ misura quanta probabilità si è «accumulata»
fino al punto $x$. Nel caso discreto, ogni volta che $x$ attraversa
una specificazione $k$, la funzione $F_{X_n}$ compie un salto di
ampiezza $\frac{1}{n+1}$: è in quei punti che si concentra tutta la
massa di probabilità. Nel caso limite, invece, $F$ non compie mai
salti: cresce in modo regolare e uniforme su tutto $[0, 1]$, senza
punti privilegiati.
Possiamo però chiederci _quanto velocemente_ $F$ cresca in ciascun
punto. Fissato $x \in [0,1]$ e un $\varepsilon > 0$ piccolo, la
probabilità che $X$ cada nell'intervallo $(x, x+\varepsilon]$ è

````{math}
\mathbb{P}(x < X \leq x + \varepsilon) = F(x+\varepsilon) - F(x).
````

Dividendo per $\varepsilon$ si ottiene il tasso di crescita medio di
$F$ attorno a $x$:

````{math}
\frac{\mathbb{P}(x < X \leq x + \varepsilon)}{\varepsilon}
    = \frac{F(x+\varepsilon) - F(x)}{\varepsilon}.
````

Quando $\varepsilon \to 0$, questo rapporto tende alla derivata di
$F$ nel punto $x$. La funzione $F'$ misura quindi la _velocità con
cui la probabilità si accumula_ al variare di $x$: è alta nelle
regioni in cui la probabilità è concentrata, bassa dove essa è
rarefatta.
Questa funzione è la _funzione di densità di probabilità_ (o, più
brevemente, _funzione di densità_) di $X$, che indichiamo con $f_X$:

````{margin}
In alcuni testi si preferisce utilizzare la notazione $f_X$ per
indicare sia la funzione di massa di probabilità, sia la funzione di
densità. Io ho preferito usare rispettivamente $p_X$ e $f_X$ per
rimarcare ulteriormente la differenza tra i due concetti coinvolti.
````
````{math}
f_X(x) = F'(x).
````

````{margin}
Chi ha familiarità con la fisica può riconoscere in questa
costruzione una struttura analoga a quella della densità di massa:
così come la densità fisica misura quanta massa è concentrata attorno
a un punto dello spazio, la densità di probabilità misura quanta
probabilità è concentrata attorno a una specificazione. Tuttavia, a
differenza della densità fisica, $f_X$ non descrive nessuna sostanza
reale: è semplicemente la derivata di $F$.
````

Nel caso che stiamo analizzando, $F(x) = x$ per $x \in [0,1]$, e dunque

````{math}
f_X(x) = F'(x) = 1 \qquad \text{per ogni } x \in [0, 1],
````

e $f_X(x) = 0$ altrove. La densità è costante: ogni punto
dell'intervallo contribuisce in uguale misura all'accumulo di
probabilità, esattamente come ci si aspetta da un modello uniforme.
Riassumendo, $f_X(x) = \mathrm I_{[0, 1]}(x)$.

Sapere che $f_X = F'$ non determina $F$ in modo univoco: qualsiasi funzione
della forma $F(x) + C$, con $C$ costante reale, ha la stessa
derivata $f_X$. Tuttavia nel nostro contesto sappiamo qualcosa in
più: $F$ è una funzione di ripartizione, e deve quindi soddisfare
$\lim_{x \to -\infty} F(x) = 0$. Questo vincolo seleziona
univocamente la costante $C = 0$, e ci permette di scrivere

````{math}
F(x) = \int_{-\infty}^x f_X(t)\, \mathrm{d}t.
````

In altre parole, $F$ non è una generica primitiva di $f_X$, ma
_l'unica_ primitiva che si annulla a $-\infty$. A partire da questa
relazione, il teorema fondamentale del calcolo integrale fornisce
immediatamente un modo per calcolare la probabilità di qualsiasi
intervallo $(a, b]$:

````{math}
:label: eq_prob-uniform-interval
\mathbb P(X \in (a, b]) = \int_a^b f_X(x)\, \mathrm{d}x.
````

Vale inoltre la pena osservare che questo risultato è coerente con il
limite calcolato nel caso discreto: avevamo ricavato che
$\mathbb P(a \leq X_n \leq b) \to b - a$ quando $n \to +\infty$, e
integrare la densità uniforme $f_X = 1$ sull'intervallo $[a, b]$ dà
esattamente $b - a$.

Infine, la relazione $F(x) = \int_{-\infty}^x f_X(t)\, \mathrm{d}t$
ci fornisce anche le due proprietà fondamentali che ogni densità di
probabilità deve soddisfare. Poiché $F$ è non decrescente, la sua
derivata è non negativa ovunque, quindi $f_X(x) \geq 0$ per ogni
$x \in \mathbb{R}$. Poiché $F$ tende a $0$ per $x \to -\infty$ e a
$1$ per $x \to +\infty$, applicando il teorema fondamentale del
calcolo agli estremi si ottiene

````{math}
\int_{-\infty}^{+\infty} f_X(x)\, \mathrm{d}x =
    \lim_{x \to +\infty} F(x) - \lim_{x \to -\infty} F(x)
    = 1 - 0 = 1.
````

Queste due condizioni — non negatività e integrale unitario — sono
per la funzione di densità esattamente ciò che la non negatività e
la somma uguale a uno erano per la funzione di massa: le proprietà
minime affinché $f_X$ descriva una distribuzione di probabilità
coerente.

Risulta quindi molto facile calcolare la probabilità che $X$ sia
contenuta in un intervallo $(a, b] \subseteq [0, 1]$:

````{math}
\mathbb P(X \in (a, b]) = \int_a^b f_X(x)\, \mathrm d x
                        = \int_a^b \mathrm d x = b - a .
````

Questo risultato è coerente con quello che otterremmo ricavando la
stessa probabilità usando la funzione di ripartizione come indicato
in {eq}`eq_cdf-e-intervalli`: infatti,

````{math}
\mathbb P(X \in (a, b]) = \mathbb P(a < X \leq b) = F(b) - F(a)
                        = b - a .
````

Vale la pena osservare una cosa interessante: questo risultato non
dipende dalla particolare forma dell'intervallo considerato, che può
essere aperto, semichiuso o chiuso. Infatti, le proprietà
dell'integrale di Riemann ci assicurano che calcolando, per esempio,
$\mathbb P(X \in [a, b])$ in modo analogo a quanto fatto in
{eq}`eq_prob-uniform-interval`, otterremmo lo stesso valore di
probabilità. Non c'è alcuna incoerenza in questo risultato, in quanto
$\mathbb P(X \in [a, b]) = \mathbb P(X \in (a, b]) +
\mathbb P(X = a)$ e l'ultima di queste probabilità è nulla. Con un
ragionamento analogo è facile mostrare che succede lo stesso quando
si considerano intervalli della forma $(a, b)$ o $[a, b)$.

Vedremo in modo preciso come la maggior parte dei concetti già
introdotti per le variabili aleatorie discrete si possono estendere
in modo naturale alle variabili aleatorie continue. Questo richiederà
quasi sempre di modificare le formule relative sostituendo la
funzione di massa di probabilità con la funzione di densità e le
sommatorie con integrali, ma in alcuni casi non sarà strettamente
necessario utilizzare il formalismo matematico. Consideriamo per
esempio il valore atteso di $X$: per calcolarlo è sufficiente
osservare che la sua densità è costante in $[0, 1]$ e nulla altrove,
pertanto la centralità della distribuzione di $X$, e dunque il suo
valore atteso, deve essere uguale a $\frac{1}{2}$. D'altra parte,
abbiamo visto come $\mathbb E(X_n) = \frac{1}{2}$, dunque è naturale
che lo stesso valga per la distribuzione limite che stiamo
considerando. Facendo un ragionamento analogo, possiamo supporre che
la varianza di $X$ si ottenga come

````{math}
\mathrm{Var}(X) = \lim_{n \to +\infty}\mathrm{Var}(X_n) =
                  \frac{1}{12} \enspace.
````

Nel {ref}`sec_modello-uniforme-continuo` vedremo come calcolare
questi due valori in modo formale.


[^meccanica-quantistica]: Per quanto bizzarro possa sembrare il
concetto di multiverso, è interessante notare che una delle
interpretazioni proposte per la meccanica quantistica (la teoria—oggi
ampiamente accettata—che descrive il comportamento della materia nella
scala sub-atomica) preveda l'esistenza di mondi paralleli.
Semplificando parecchio, in un dato istante di tempo ognuna delle
cosiddette "particelle elementari" (protoni, elettroni o entità ancora
più piccole) non ha una posizione fissa, bensì si trova
simultaneamente in più punti dello spazio. Solo quando viene
effettuato un esperimento per osservare una di queste particelle (il
verbo va inteso in senso lato, perché stiamo parlando di cose non
visibili a occhio nudo) questa assume una posizione precisa. Tra
l'altro, sono proprio le leggi della probabilità a descrivere la
posizione della particella rilevata dell'esperimento in questione.
Tra le interpretazioni proposte per la meccanica quantistica, quella
cosiddetta "a molti mondi" prevede che ogni volta che viene effettuato
un esperimento di questo tipo si ottiene come conseguenza la creazione
di tanti mondi distinti, uno per ogni risultato possibile.

[^convergenza-uniforme]: Si dimostra facilmente che il limite vale
anche in un senso più restrittivo, relativo alla convergenza
_uniforme_: per ogni $\epsilon > 0$ esiste $n_0 \in \mathbb N$ tale
che per ogni $n > n_0$ e per ogni $x \in \mathbb R$ si ha
$| F_{X_n}(x) - F(x) | \leq \epsilon$. Infatti, il grafico di
$F_{X_n}(x)$ supera sempre quello di $F(x)$ e quindi
$| F_{X_n}(x) - F(x) | = F_{X_n}(x) - F(x) =
\frac{\lfloor n x \rfloor + 1}{n} - x \leq \frac{n x + 1}{n} - n =
\frac{1}{n}$, dunque $| F_{X_n}(x) - F(x) | \leq \epsilon$ per ogni
$n > \frac{1}{\epsilon}$.

[^convergenza-xn]: Notate come il ragionamento che abbiamo effettuato
dimostri la convergenza della sequenza delle funzioni di distribuzione
cumulativa delle varie $X_n$, e non delle variabili aleatorie stesse.
In altre parole, allo scopo di aprire la porta sul mondo delle
variabili aleatorie continue, abbiamo dimostrato che la
_distribuzione_ corrispondente a un particolare modello uniforme
discreto su $D_n$ converge al crescere di $n$ a una distribuzione che
fa riferimento a un nuovo tipo di modello, detto _uniforme continuo_.
Non abbiamo invece dimostrato che la successione delle $X_n$ converge
a una variabile aleatoria $X$ la cui distribuzione è un caso
particolare del modello uniforme continuo. Lo studio della convergenza
di successioni di variabili aleatorie richiede di studiare la teoria
della probabilità in modo più approfondito rispetto a quanto descritto
in questo libro. Ma se volete uno _spoiler_, il limite di una
successione di variabili aleatorie può essere definito in più modi, e
in nessuno di questi si ha una convergenza delle $X_n$ alla
distribuzione uniforme continua su $[0, 1]$.

[^attosecondi]: Se vi sembra che $0.0004678$ sia una frazione di
secondo esageratamente piccola, tenete presente che nel numero 709 di
_Superman comic_ Barry Allen (l'identità segreta di Flash) sostiene di
essere in grado di percepire eventi che durano meno di un
_attosecondo_, che equivale a $10^{-18}$ secondi (un miliardesimo di
un miliardesimo di secondo).