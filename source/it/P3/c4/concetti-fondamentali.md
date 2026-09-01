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

(sec-concetti-fondamentali-VA)=
# Concetti fondamentali

Come ho anticipato a inizio capitolo, spesso un esperimento casuale si descrive
meglio non nei termini dell'esito in sé, ma attraverso un numero che ne cattura
un aspetto rilevante &mdash; e sul quale possiamo poi operare con strumenti
matematici, ove ciò abbia senso. La definizione seguente dà forma precisa a
questo passaggio dall'esito al numero, introducendo la nozione di variabile
aleatoria.

````{prf:definition} Variabile aleatoria
:label: def-variabile-aleatoria

Dato uno spazio di probabilità $(\Omega, \mathsf A, \mathbb P)$, una
_variabile aleatoria_ è una funzione $X \colon \Omega \to \mathbb R$ tale
che, per ogni $x \in \mathbb R$, l'insieme
$X^{-1}(x) = \{\omega \in \Omega : X(\omega) \leq x\}$ appartiene a
$\mathsf A$, ed è quindi un evento.
````

In linea di principio, il passaggio logico corretto consiste nell'eseguire
l'esperimento casuale, osservarne l'esito e applicare a quest'ultimo la
funzione $X$, ottenendo così un numero reale. Le variabili aleatorie presentano
però un importante vantaggio pratico: una volta definita la corrispondenza tra
esiti e valori numerici, spesso non è più necessario fare esplicito riferimento
all'esperimento casuale sottostante. Possiamo invece concentrarci direttamente
sulla variabile aleatoria stessa, immaginando di _osservarla_ e di ottenere
come risultato un valore $x \in \mathbb{R}$. In questo senso, la variabile
aleatoria diventa l'oggetto principale di studio, mentre i dettagli
dell'esperimento che l'ha generata passano in secondo piano.

```{admonition} _
:class: naming

Per convenzione, le variabili aleatorie sono indicate con lettere maiuscole,
come $X$, $Y$ e $Z$, mentre i valori da esse assunti, che per brevità vengono
spesso detti _realizzazioni_ o _osservazioni, sono indicati con le
corrispondenti lettere minuscole, come $x$, $y$ e $z$. Ciò permette di
ragionare su espressioni come $X = x$, $X \leq x$ e così via. Questa
distinzione tra lettere maiuscole e minuscole è uno standard quasi universale
nella teoria della probabilità e nella statistica.
```

La condizione richiesta dalla definizione precedente, detta _di misurabilità_,
garantisce che a ogni domanda della forma «$X$ è minore o uguale di $x$?»
corrisponda un evento ben definito, e quindi una probabilità. Più precisamente,
la probabilità dell'evento $\{ \omega \in \Omega \mid X(\omega) \leq x \}$,
che come anticipato indicherò con la notazione abbreviata $X \leq x$. Vedremo
che questo modo di procedere si estende anche a tutti gli eventi individuati
da una condizione sui valori assunti da $X$: per esempio, potremmo considerare
$X = x$, $X > 4$, $X$ è un numero primo e via discorrendo. Qualora dovesse
servire, racchiuderò questi eventi tra parentesi graffe (quindi gli esempi
precedenti potrebbero anche apparire indicati come $\{ X = x \}$,
$\{ X > 4 \}$ e $\{ X \text{ è primo} \}$ ); ciò mi permetterà di essere più
preciso quando costruirò degli eventi complessi, ma anche quando vorrò dare
enfasi al fatto che queste espressioni rappresentano in tutto e per tutto degli
eventi, dei quali può essere interessante calcolare la probabilità.

````{admonition} Sulla condizione di misurabilità
:class: note

Nel {ref}`sec-concetti-fondamentali` abbiamo visto che, quando $\Omega$ è
finito o numerabile, possiamo tranquillamente considerare $2^\Omega$ come
algebra: ogni sottoinsieme è un evento, e di conseguenza ogni funzione
$X \colon \Omega \to \mathbb R$ soddisfa la condizione di misurabilità. In
altre parole, qualunque funzione può essere considerata una variabile
aleatoria.
```{margin}
Quindi, tecnicamente, una variabile aleatoria non è altro che una funzione
$X \colon \Omega \to \mathbb R$ misurabile rispetto alla $\sigma$-algebra
$\mathsf A$.
```
Abbiamo anche visto che la situazione cambia quando si considerano variabili
aleatorie continue, perché non tutti i sottoinsiemi di $\Omega$ possono essere
eventi, e siamo costretti a considerare una $\sigma$-algebra più piccola di
$2^\Omega$. È allora che la condizione in questione diventa interessante,
perché non tutte le funzioni $X \colon \Omega \to \mathbb R$ sono _misurabili_
&mdash; è questo il nome che si dà alle funzioni che soddisfano la condizione
&mdash; ed è per questo motivo che la {prf:ref}`def-variabile-aleatoria` lo
richiede esplicitamente (riprenderò brevemente questo concetto nel
{ref}`sec-misure-di-centralita`).

In pratica, esibire una funzione non misurabile richiede costruzioni piuttosto
artificiose, che esulano dal livello di questo libro[^funzioni-patologiche].
Per questo, nel seguito considererò la misurabilità come un requisito
implicitamente soddisfatto, senza verificarlo di volta in volta.
````


````{prf:example} Avanscoperta in due quartieri
:label: ex-va-scoiattoli

{extlink}`Squirrel Girl
<https://marvel.fandom.com/wiki/Doreen_Green_(Earth-616)>` coordina due
gruppi di scoiattoli che perlustrano in modo indipendente due quartieri
distinti, in cerca di potenziali minacce. Ciascun gruppo, al rientro,
segnala un numero di minacce compreso tra $1$ e $6$. Se assumiamo, per
semplicità, che ognuno dei due gruppi segnali ciascuno di questi valori con la
stessa probabilità, indipendentemente dall'altro, lo spazio degli esiti è
$\Omega = \{ (g_1, g_2) \mid g_1, g_2 \in [1 .. 6] \}$, e ogni coppia è
equiprobabile. La funzione $X \colon \Omega \to \mathbb R$ tale che
$X((g_1, g_2)) = g_1 - g_2$ per ogni $(g_1, g_2) \in \Omega$ definisce la
variabile aleatoria che misura la differenza tra il numero di minacce nei due
quartieri. Se $X$ è positiva, il primo quartiere presenta più minacce del
secondo; se è negativa, accade il contrario.

L'evento $X \geq 2$ raccoglie gli esiti in cui il primo gruppo segnala
almeno due minacce in più del secondo. Come evidenziato nella
{numref}`fig-va-scoiattoli-griglia`, questi esiti sono dieci, e dunque

```{math}
\mathbb P(X \geq 2) = \frac{10}{36} = \frac{5}{18} \enspace.
```

Analogamente, la probabilità che il primo gruppo indichi al massimo una
minaccia in più del secondo sarà $\mathbb P(X < 2) = 1 - \mathbb P(X \geq 2)
= \frac{13}{18}$.
````

````{customfigure}
:name: fig-va-scoiattoli-griglia

```{code-cell} python
:tags: [hide-input]

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

g1, g2 = np.meshgrid(range(1, 7), range(1, 7))
g1, g2 = g1.ravel(), g2.ravel()
PRIMO_PEGGIORE = (g1 - g2) >= 2

with mpl.rc_context({'figure.figsize': (4, 3),
                'figure.dpi': 150,
                'xtick.labelsize': 7,
                'ytick.labelsize': 7,
                'axes.labelsize': 7}):

   EDGE_COLOR = '#010177'

   fig, ax = plt.subplots()
   ax.set_facecolor('#eaf3f5')
   ax.scatter(g1[~PRIMO_PEGGIORE], g2[~PRIMO_PEGGIORE], s=22, c='white',
      edgecolors=EDGE_COLOR, linewidths=0.5, zorder=3)
   ax.scatter(g1[PRIMO_PEGGIORE], g2[PRIMO_PEGGIORE], s=22, c='steelblue',
      edgecolors=EDGE_COLOR, linewidths=0.5, zorder=4)
   ax.set_xlabel('Primo gruppo', loc='default')
   ax.set_ylabel('Secondo gruppo', loc='default')
   ax.set_xticks(range(1, 7))
   ax.set_yticks(range(1, 7))
   ax.set_xlim(0.5, 6.5)
   ax.set_ylim(0.5, 6.5)
   ax.grid(True, color=EDGE_COLOR, alpha=0.12)
   ax.set_aspect('equal')
   plt.show()
```

Spazio degli esiti dell'{prf:ref}`ex-va-scoiattoli`: i punti colorati in blu
sono quelli per cui $X \geq 2$, cioè quelli in cui il primo gruppo segnala
almeno due minacce in più del secondo.
````
Nell'esempio precedente ci siamo posti due domande &mdash; quanto vale
$\mathbb P(X \geq 2)$ e quanto $\mathbb P(X < 2)$ &mdash; che, a ben vedere,
erano della stessa natura: chiedevano la probabilità che $X$ apartenesse a un
certo insieme di valori. Non si tratta di una particolarità di quell'esempio:
vedremo infatti che gran parte di ciò che vogliamo sapere su una variabile
aleatoria si formula proprio in questo modo. Conviene allora considerare in
blocco la totalità di queste risposte &mdash; una per ogni insieme di valori
che potremmo considerare &mdash; e dare un nome all'oggetto che ne risulta.

````{prf:definition} Distribuzione di una variabile aleatoria
:label: def-distribuzione

La _distribuzione_ (o _legge_) di una variabile aleatoria $X$ è la funzione
che a ogni insieme misurabile[^boreliani] $A$ di numeri reali associa la
probabilità $\mathbb P_X(A) = \mathbb P(X \in A)$ che $X$ assuma un valore in
$A$[^prob-immagine].
````

Resta però un problema pratico: $\mathbb P_X$ assegna una probabilità a
_tutti_ gli insiemi misurabili, ed è dunque definita su un'intera famiglia
di insiemi. Un oggetto di questo tipo è troppo ingombrante per sperare di
scriverlo in forma analitica, come faremmo con una funzione di una variabile
reale. Conviene allora cercare altri oggetti matematici, più facili da
trattare, da cui si possa recuperare per intero l'informazione contenuta in
$\mathbb P_X$. Il prossimo paragrafo ne introduce uno, che ha il vantaggio di
funzionare in modo identico per le variabili aleatorie continue e discrete.

## La funzione di ripartizione

La condizione di misurabilità introdotta nella
{prf:ref}`def-variabile-aleatoria` sembra fornire agli eventi della forma
$X \leq x$ un ruolo particolare. In effetti, il primo strumento matematico che
si introduce per lavorare con le variabili aleatorie è esattamente incentrato
su questo tipo di evento. Si tratta della funzione di ripartizione introdotta
di seguito.

````{prf:definition} Funzione di ripartizione
:label: def-funzione-ripartizione

Data una variabile aleatoria $X$, la sua _funzione di ripartizione_ (o
_funzione di distribuzione cumulativa_) è la funzione
$F_X \colon \mathbb R \to [0, 1]$ definita da

```{math}
F_X(x) = \mathbb P(X \leq x) \qquad \forall x \in \mathbb R \enspace.
```
````

```{margin}
Quando una variabile aleatoria $X$ ha funzione di ripartizione $F$, è
frequente scrivere $X \sim F$, che si legge «$X$ è distribuita secondo
$F$». Userò questa notazione, e all'occorrenza anche $X \sim F_X$, nei
capitoli successivi.
```
La funzione di ripartizione si può quindi pensare come la restrizione della
distribuzione di una variabile aleatoria $X$ agli intervalli della forma
$(-\infty, x]$.

````{prf:example} Il primo gruppo di scoiattoli
:label: ex-ripartizione-primo-gruppo

Con riferimento aell'{prf:ref}`ex-va-scoiattoli`, consideriamo la variabile
aleatoria definita da $Y((g_1, g_2)) = g_1$, che descrive il numero di minacce
segnalate dal primo gruppo di scoiattoli. Poiché la funzione può assumere i
valori $1, 2, \dots, 6$ e questi sei valori sono equiprobabili, la funzione di ripartizione di $Y$ cresce di un sesto ogni volta che la soglia supera uno di
tali valori:

```{math}
F_Y(x) =
\begin{cases}
0 & \text{se } x < 1, \\
	\frac{1}{6} & \text{se } 1 \leq x < 2, \\
	\frac{2}{6} & \text{se } 2 \leq x < 3, \\
	\frac{3}{6} & \text{se } 3 \leq x < 4, \\
	\frac{4}{6} & \text{se } 4 \leq x < 5, \\
	\frac{5}{6} & \text{se } 5 \leq x < 6, \\
1 & \text{se } x \geq 6.
\end{cases}
```

Questa forma a tratti è probabilmente la più utile per farsi un'idea
dell'andamento della funzione, che è costante a tratti, con dei salti che
sono  mostrati graficamente nella {numref}`fig-ripartizione-primo-gruppo`.
Se però si vuole una scrittura più compatta ed elegante, si può anche usare
l'operatore $\lfloor \cdot \rfloor$ di parte intera inferiore:

```{math}
F_Y(x) =
\begin{cases}
0 & \text{se } x < 1, \\
   \frac{\lfloor x \rfloor}{6} & \text{se } 1 \leq x < 6, \\
1 & \text{se } x \geq 6.
\end{cases}
```

Per esempio, si ha $F_Y(3) = \mathbb P(Y \leq 3) = \frac{3}{6} = \frac{1}{2}$,
perché tre dei sei valori possibili di $Y$ non superano la soglia $3$.
````

````{customfigure}
:name: fig-ripartizione-primo-gruppo

```{code-cell} python
:tags: [hide-input]


from fractions import Fraction
import scipy.stats as st

v = np.arange(1, 7)
p = np.array([1/6] * 6)

X = st.rv_discrete(values=(v, p))
fig, ax = plt.subplots()

x_plot = np.concatenate(([v[0] - 2], v, [v[-1] + 2]))
y_plot = np.concatenate(([0], X.cdf(v), [1]))
ax.step(x_plot, y_plot, where='post', color='C0')

prev = np.concatenate(([0.0], X.cdf(v)[:-1]))
ax.plot(v, X.cdf(v), 'o', color='C0', zorder=3)

ticks = np.arange(1, 7) / 6
labels = [str(Fraction(t).limit_denominator(36)) for t in ticks]
ax.set_yticks(ticks)
ax.set_yticklabels(labels)

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$F_X(x)$')
plt.show()
```

Funzione di ripartizione della variabile $Y$ definita
nell'{prf:ref}`ex-ripartizione-primo-gruppo`.
````
````{prf:example} La ripartizione della differenza tra i gruppi
:label: ex-ripartizione-scoiattoli

Sempre con riferimento all'{prf:ref}`ex-va-scoiattoli`, riconsideriamo la
variabile aleatoria $X$ ivi descritta, che era definita da
$X((g_1, g_2)) = g_1 - g_2$. La sua funzione di ripartizione $F_X$ associa a
ogni $x$ la probabilità che il primo gruppo segnali al più $x$ minacce in più
del secondo.

In modo non molto dissimile dall'esempio precedente, poiché $X$ può assumere
solo valori interi compresi tra $-5$ e $5$, $F_X$ resta costante tra due interi consecutivi e cambia valore soltanto quando la soglia $x$ supera uno di questi
undici valori. Contando, ogni volta, quante delle $36$ coppie equiprobabili
$(g_1, g_2)$ soddisfano la condizione $g_1 - g_2 \leq x$, si ottiene la
definizione

```{math}
F_X(x) =
\begin{cases}
0 & \text{se } x < -5, \\
	\frac{1}{36} & \text{se } -5 \leq x < -4, \\
	\frac{1}{12} & \text{se } -4 \leq x < -3, \\
	\frac{1}{6} & \text{se } -3 \leq x < -2, \\
	\frac{5}{18} & \text{se } -2 \leq x < -1, \\
	\frac{5}{12} & \text{se } -1 \leq x < 0, \\
	\frac{7}{12} & \text{se } 0 \leq x < 1, \\
	\frac{13}{18} & \text{se } 1 \leq x < 2, \\
	\frac{5}{6} & \text{se } 2 \leq x < 3, \\
	\frac{11}{12} & \text{se } 3 \leq x < 4, \\
	\frac{35}{36} & \text{se } 4 \leq x < 5, \\
1 & \text{se } x \geq 5.
\end{cases}
```

Anche in questo caso, $F_X$ è una funzione costante a tratti, come mostrato
anche nella {numref}`fig-ripartizione-scoiattoli`.
````

```{margin}
Non è un caso che, in entrambi gli esempi, si sia ottenuta una funzione di
ripartizione costante a tratti: vedremo che è una peculiarità delle variabili
aleatorie discrete.
```
````{customfigure}
:name: fig-ripartizione-scoiattoli

```{code-cell} python
:tags: [hide-input]

v = np.arange(-5, 6)
p = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) / 36

X = st.rv_discrete(values=(v, p))
fig, ax = plt.subplots()

x_plot = np.concatenate(([v[0] - 1], v, [v[-1] + 1]))
y_plot = np.concatenate(([0], X.cdf(v), [1]))
ax.step(x_plot, y_plot, where='post', color='C0')

prev = np.concatenate(([0.0], X.cdf(v)[:-1]))
ax.plot(v, X.cdf(v), 'o', color='C0', zorder=3)

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$F_X(x)$')

ticks = np.arange(4, 37, 4) / 36
labels = [str(Fraction(t).limit_denominator(36)) for t in ticks]
ax.set_yticks(ticks)
ax.set_yticklabels(labels)

plt.show()
```

Funzione di ripartizione della variabile $X$ descritta
nell'{prf:ref}`ex-ripartizione-scoiattoli`.
````
La funzione di ripartizione codifica per intero il comportamento probabilistico
di una variabile aleatoria $X$, nel senso che a partire da questa funzione si
possono calcolare le probabilità di tutti gli eventi che coinvolgono $X$. Il
caso più diretto è quello delle condizioni del tipo $a < X \leq b$, di cui si
occupa il prossimo risultato; ma anche le probabilità dei singoli valori si
possono leggere a partire dalla ripartizione, attraverso i suoi salti, come vedremo trattando le
variabili discrete.

````{prf:lemma}
:label: lemma-ripartizione-intervallo

Per ogni variabile aleatoria $X$ e per ogni coppia di numeri reali
$a \leq b$ vale

```{math}
:label: eq-ripartizione-intervallo

\mathbb P(a < X \leq b) = F_X(b) - F_X(a) \enspace.
```
````

````{sds-proof}
Poiché $a \leq b$, l'evento $\{X \leq b\}$ si decompone come

```{math}
\{X \leq b\} = \{X \leq a\} \cup \{a < X \leq b\} \enspace,
```

e i due eventi a secondo membro sono disgiunti, dato che il primo richiede
$X \leq a$ e il secondo $X > a$. Il terzo assioma di Kolmogorov assicura
allora che $\mathbb P(X \leq b) = \mathbb P(X \leq a) + \mathbb P(a < X \leq
b)$, vale a dire

```{math}
F_X(b) = F_X(a) + \mathbb P(a < X \leq b) \enspace,
```

da cui {eq}`eq-ripartizione-intervallo` segue isolando l'ultimo addendo.
````

La funzione di ripartizione gode di alcune proprietà generali, valide per
qualunque variabile aleatoria, che enuncio nel teorema seguente.

````{prf:theorem} Proprietà della funzione di ripartizione
:label: thm-proprieta-ripartizione

Siano $X$ una variabile aleatoria e $F_X$ la sua funzione di ripartizione.
Allora

1. $0 \leq F_X(x) \leq 1$ per ogni $x \in \mathbb R$;
2. $F_X$ è non decrescente, cioè $F_X(a) \leq F_X(b)$ quando $a \leq b$;
3. $\displaystyle \lim_{x \to -\infty} F_X(x) = 0$ e
   $\displaystyle \lim_{x \to +\infty} F_X(x) = 1$;
4. $F_X$ è continua da destra, cioè
   $\displaystyle \lim_{x \to x_0^+} F_X(x) = F_X(x_0)$ per ogni $x_0$.
````

````{sds-proof}
La prima proprietà è immediata, perché $F_X(x) = \mathbb P(X \leq x)$ è una
probabilità, e dunque appartiene per definizione all'intervallo $[0, 1]$.

La seconda discende dal {prf:ref}`lemma-ripartizione-intervallo`: se
$a \leq b$, allora

```{math}
F_X(b) - F_X(a) = \mathbb P(a < X \leq b) \geq 0 \enspace,
```

perché ancora una volta si tratta della probabilità di un evento, e quindi
$F_X(a) \leq F_X(b)$.

Le ultime due proprietà richiedono di passare al limite lungo successioni
di eventi, e si dimostrano applicando la continuità della probabilità
rispetto a successioni monotone di eventi. Mi limito a darne l'idea: per la
terza, basta osservare che gli eventi $\{X \leq x\}$ si riducono
all'insieme vuoto quando $x \to -\infty$ e crescono fino a riempire tutto
$\Omega$ quando $x \to +\infty$, sicché le loro probabilità tendono
rispettivamente a $0$ e a $1$. Per la quarta, gli eventi $\{X \leq x\}$ con
$x \to x_0^+$ decrescono fino all'evento $\{X \leq x_0\}$, e la continuità
della probabilità garantisce che $F_X(x)$ tenda a $F_X(x_0)$. Ometto i
dettagli tecnici, che riprenderò quando tratterò le successioni di eventi.
````

````{prf:theorem} Caratterizzazione delle funzioni di ripartizione
:label: thm-caratterizzazione-ripartizione

Una funzione $F \colon \mathbb R \to [0, 1]$ è la funzione di ripartizione
di una qualche variabile aleatoria se e solo se è non decrescente, continua
da destra, e soddisfa

```{math}
\lim_{x \to -\infty} F(x) = 0,
\qquad
\lim_{x \to +\infty} F(x) = 1 \enspace.
```
````

Una metà di questo enunciato ci è già nota: per il
{prf:ref}`thm-proprieta-ripartizione`, ogni funzione di ripartizione è non
decrescente, continua da destra e possiede i due limiti prescritti, sicché
la _necessità_ di queste tre condizioni è acquisita. Il contenuto
sostanziale del teorema è il viceversa, ovvero la loro _sufficienza_: ogni
funzione $F$ che le soddisfi è effettivamente la funzione di ripartizione di
una variabile aleatoria, nel senso che se ne può sempre costruire una che
ammette proprio $F$ come legge. Questa direzione richiede però di esibire
una tale variabile a partire da $F$, e presuppone strumenti che non ho
ancora introdotto: per questo la enuncio senza dimostrazione. Ne ricaviamo
comunque un criterio pratico, che useremo di frequente: per riconoscere se
una data funzione può descrivere la legge di una variabile aleatoria è
sufficiente verificarne la monotonicità, la continuità da destra e i limiti
agli estremi.

```{margin}
La variabile aleatoria con questa funzione di ripartizione segue la
distribuzione uniforme continua sull'intervallo $[150, 210]$. Studierò questo
modello in modo sistematico nel {ref}`sec_modello-uniforme-continuo`.
```

````{prf:example} L'altezza dell'ultimo supereroe
:label: ex-ripartizione-altezza

Torniamo all'esperimento, già incontrato in precedenza, di misurare l'altezza
dell'ultimo supereroe che compare in un fumetto. Consideriamo la funzione

```{math}
F_H(x) =
\begin{cases}
0 & \text{se } x < 150, \\
\dfrac{x - 150}{60} & \text{se } 150 \leq x < 210, \\
1 & \text{se } x \geq 210.
\end{cases}
```

e chiediamoci se possa essere la funzione di ripartizione di una variabile
aleatoria $H$ che rappresenta tale altezza, espressa in centimetri.

Il grafico nella {numref}`fig-ripartizione-altezza` mostra che $F_H$ è non
decrescente; inoltre il tratto obliquo che collega $(150, 0)$ a $(210, 1)$
evidenzia che la funzione è continua, quindi in particolare continua da
destra. Si vede anche che $F_H(x)$ tende a $0$ quando $x \to -\infty$ e a $1$
quando $x \to +\infty$. Per il {prf:ref}`thm-caratterizzazione-ripartizione`,
queste proprietà bastano a concludere che $F_H$ è effettivamente la funzione
di ripartizione di una qualche variabile aleatoria.

Per esempio,

```{math}
F_H(180) = \mathbb P(H \leq 180) = \frac{180 - 150}{60} = \frac{1}{2}
\enspace,
```

perché $180$ si trova esattamente a metà dell'intervallo in cui la funzione
cresce da $0$ a $1$.
````

````{customfigure}
:name: fig-ripartizione-altezza

```{code-cell} python
:tags: [hide-input]

fig, ax = plt.subplots()

x_plot = np.array([140, 150, 210, 220])
y_plot = st.uniform(150, 60).cdf(x_plot)
ax.plot(x_plot, y_plot)

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$F_H$')
ax.set_xticks([150, 180, 210])
ax.set_yticks([0, 1 / 2, 1])
ax.set_yticklabels(['0', '1/2', '1'])
plt.show()
```

Grafico della funzione $F_H$ dell'{prf:ref}`ex-ripartizione-altezza`: la
funzione è non decrescente, continua e ha i limiti corretti agli estremi,
quindi soddisfa le condizioni del
{prf:ref}`thm-caratterizzazione-ripartizione`.
````
La funzione di ripartizione visualizzata in {numref}`fig-ripartizione-altezza`
esibisce un comportamento che la distingue rispetto a quelle viste
precedentemente: a differenza di queste ultime, che sono costanti a tratti
(crescono «per salti»), varia in modo continuo. Questa caratteristica non è un
semplice dettaglio grafico, ma riflette la natura della variabile aleatoria
e della distribuzione sottostanti, nel senso che ho anticiato all'inizio di
questo capitolo. Più precisamente, quando la funzione di ripartizione è
costante a tratti la variabile aleatoria è discreta, e quando è continua allora
la variabile aleatoria è continua. Vedremo più avanti che esistono anche
situazioni intermedie, nelle quali convivono entrambe le caratteristiche.

Conviene quindi fissare un punto che ci farà da filo conduttore: la funzione di
ripartizione è un particolare descrittore di una variabile aleatoria, o,
equivalentemente, della sua distribuzione, che non dipende dal suo tipo. Le
proprietà che abbiamo appena visto, e la caratterizzazione che ne discende,
valgono per le variabili discrete, continue e miste. Nei prossimi capitoli
approfondirò questa distinzione, a partire dal caso discreto.

## Variabili aleatorie in Python

Il modulo `scipy.stats` fornisce due classi base per rappresentare variabili
aleatorie: `rv_discrete` per distribuzioni discrete e `rv_continuous` per
quelle continue. Una volta costruiti gli oggetti corrispondenti, la funzione di
ripartizione &mdash; così come altri oggetti matematici legati alla
distribuzione &mdash; è disponibile invocando il metodo `cdf`, senza che vi sia
bisogno di implementarla a mano.

Per costruire l'oggetto che corrisponde a una distribuzione discreta, è
sufficiente passare l'insieme dei valori e le probabilità corrispondenti:

```{code-cell} python
import numpy as np
import scipy.stats as st

v = np.arange(1, 7)
p = np.array([1/6] * 6)

X = st.rv_discrete(values=(v, p))
```

```{margin}
In realtà è possibile anche passare a `cdf` un argomento _scalare_, inteso come
un'espressione che viene valutata al valore di un tipo di dati semplice. In
casi come questo, tale valore viene automaticamente convertito in un array
di un elemento.
```
Come sopra indicato, su `X` è possibile invocare il metodo `cdf` per ottenere
i valori della funzione di ripartizione. È importante sottolineare che `cdf` è
una funzione _vettoriale_, che accetta come argomenti liste, vettori o altri
oggetti ad accesso posizionale[^nested-sequence] e restituisce un array NumPy
della stessa forma, applicando in modo efficiente il calcolo elemento per
elemento, senza cicli Python espliciti. Ciò comporta che invocare `cdf` su un
vettore di, diciamo $n$ elementi, è tendenzialmente più veloce che invocarlo
per $n$ volte sui singoli elementi.

```{code-cell} python
X.cdf([-4, 1, 1.1, 5, 7])
```

Uno dei modi più agevoli per disegnare il grafico delle funzioni di
ripartizione di variabili aleatorie discrete è quello di usare `ax.step`, che
è appunto pensato per le funzioni costanti a tratti. I pallini che evidenziano
la continuità da destra si aggiungono separatamente usando `ax.plot`.

```{code-cell} python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x_plot = np.concatenate(([v[0] - 2], v, [v[-1] + 2]))
y_plot = np.concatenate(([0], X.cdf(v), [1]))
ax.step(x_plot, y_plot, where='post', color='C0')

prev = np.concatenate(([0.0], X.cdf(v)[:-1]))
ax.plot(v, X.cdf(v), 'o', color='C0', zorder=3)

ticks = np.arange(1, 7) / 6
labels = [str(Fraction(t).limit_denominator(36)) for t in ticks]
ax.set_yticks(ticks)
ax.set_yticklabels(labels)

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$F_X(x)$')
plt.show()
```

Nell'invocazione di `ax.step` è importante specificare l'argomento opzionale
`where="post"`, per riprodurre correttamente la continuità da destra: in questo
modo, ogni segmento orizzontale parte dal valore a destra del salto, in accordo
con la definizione $F(x) = P(X \leq x)$.

In generale, userò `rv_discrete` solo per distribuzioni molto specifiche, che
individuano variabili aleatorie con pochi valori, così che la loro
distribuzione si possa descrivere in modo estensivo, specificando ogni valore
insieme alla relativa probabilità. All'atto pratico, vedremo nel
{ref}`chap_modelli-discreti` che si utilizzano dei particolari modelli di
distribuzione, per ognuno dei quali si utilizzano delle classi Python dedicate,
derivate da `rv_discrete`. Il caso delle distribuzioni continue è meno agevole
da trattare: sebbene `scipy.stats` metta a disposizione la classe
`rv_continuous`, le variabili aleatorie corrispondenti hanno infiniti valori
possibili, dunque non ha senso pensare di istanziare questa classe in modo
analogo all'esempio appena visto. Infatti, `rv_continuous` è normalmente usata
come base per derivare modelli di variabili aleatorie, tra cui quelli che
vedremo nel {ref}`chap_va-e-modelli-continui`[^st.cdf]. Per creare delle
variabili aleatorie che non sono annoverate in questi modelli è necessaria una
conoscenza sulla creazione di classi in Python, che in questo libro non
approfondirò.


[^boreliani]: Si parla di «insieme misurabile» perché non è possibile
considerare sottoinsiemi qualunque di $\mathbb R$: per essere precisi, l'unione
di tutte le preimmagini degli elementi di $A$ attraverso $X$ deve essere un
insieme misurabile nel senso della {prf:ref}`def-misurabile`. La condizione
imposta nella {prf:ref}`def-variabile-aleatoria` sui soli insiemi $(-\infty,
x]$ basta, per inciso, a garantire che $\{X \in A\}$ sia un evento per ogni $A$
di questo tipo.

[^funzioni-patologiche]: Oggetti di questo genere presentano caratteristiche
talmente insolite da essere talvolta indicati, in letteratura, come _funzioni
patologiche_. Tipicamente, non si costruiscono scrivendo una formula esplicita,
ma seguendo dei procedimenti indiretti. Un esempio classico è quello degli
{extlink}`insiemi di Vitali <https://it.wikipedia.org/wiki/Insieme_di_Vitali>`,
ottenuti suddividendo un insieme continuo in infinite classi di equivalenza
molto irregolari e scegliendo poi un rappresentante per ciascuna di esse.
Insiemi di questo tipo risultano così complessi da non poter essere trattati in
modo coerente dalla teoria della misura, e sono collegati a risultati
apparentemente insensati come il {extlink}`paradosso di Banach-Tarski
<https://it.wikipedia.org/wiki/Paradosso_di_Banach-Tarski>`. L'idea da
trattenere è quindi che si tratta di costruzioni molto astratte e poco
operative, ben lontane dagli esempi dei quali ci occuperemo in questo libro.

[^prob-immagine]: La somiglianza tra i simboli $\mathbb P$ e $\mathbb P_X$ non
è casuale: $\mathbb P_X$ è essa stessa una misura di probabilità, che soddisfa
gli stessi assiomi di $\mathbb P$, con l'unica differenza di essere definita
sugli insiemi di numeri reali anziché sugli esiti di $\Omega$. Il pedice
ricorda da quale variabile aleatoria essa è indotta. In questo senso la
distribuzione _trasporta_ su $\mathbb R$ la probabilità che viveva su $\Omega$,
ed è ciò che ci consente, da qui in avanti, di ragionare sui valori numerici
quasi dimenticando lo spazio degli esiti di partenza.

[^nested-sequence]: Più precisamente, qualsiasi oggetto da cui `np.asarray`
possa ricavare ciò che si definisce una sequenza annidata regolarmente (_nested
sequence_), cioè tale che a ogni livello di annidamento tutti gli elementi
abbiano la stessa lunghezza. Una lista di liste con lunghezze diverse è ad
accesso posizionale ma non soddisfa questo requisito, e `np.asarray` produce in
quel caso un array di oggetti Python invece che un array numerico. Dire che
`cdf` è vettoriale significa che i calcoli che essa effettua sono delegati a
codice nativo precompilat. Il costo fisso della chiamata &mdash; conversione
dell'input, allocazione dell'output &mdash; si paga una volta sola
indipendentemente dalla dimensione dell'array; il costo per elemento è quindi
decrescente all'aumentare dell'input. Il confronto rilevante non è tra `cdf(x)`
con `x` scalare e `cdf(x)` con `x` array di mille elementi, ma tra quest'ultimo
e un ciclo come `[cdf(_) for _ in x]`: i due producono lo stesso risultato, ma
il primo è molto più efficiente perché l'overhead della chiamata Python viene
pagato una volta sola invece di mille.

[^st.cdf]: Potete verificare facilmente che la funzione di ripartizione di una
distribuzione continua si ottiene invocando il metodo `cdf` andando per esempio
ad analizzare il codice Python che genera la
{numref}`fig-ripartizione-altezza`.

## Vero o falso?

Analizzate ciascuna delle seguenti affermazioni, che riguardano una variabile
aleatoria $X$, e dite se è vera o falsa, motivando il vostro
ragionamento. Cliccate su di essa per visualizzare la risposta corretta.

````{tf-item}
La funzione di ripartizione $F_X$ è non decrescente.
+++
**Vera**. Per il {prf:ref}`thm-proprieta-ripartizione`, se $x \leq y$ allora
$\{X \leq x\} \subseteq \{X \leq y\}$, quindi
$F_X(x) = \mathbb P(X \leq x) \leq \mathbb P(X \leq y) = F_X(y)$.
````

````{tf-item}
Per qualunque variabile aleatoria $X$ vale $\lim_{x \to +\infty} F_X(x) = 1$.
+++
**Vera**. Al crescere di $x$ verso $+\infty$, l'evento $\{X \leq x\}$
«esaurisce» l'intero spazio degli esiti, quindi la sua probabilità tende a
$\mathbb P(\Omega) = 1$.
````

````{tf-item}
La funzione di ripartizione è continua da sinistra in ogni punto.
+++
**Falsa**. Per il {prf:ref}`thm-proprieta-ripartizione`, $F_X$ è continua da
destra in ogni punto, ma non necessariamente da sinistra: nelle variabili
aleatorie discrete $F_X$ presenta salti nei valori del supporto, e in
corrispondenza di un salto il limite sinistro è strettamente minore del
valore della funzione.
````

````{tf-item}
Se $a < b$ e $F_X(a) = F_X(b)$, allora $X$ non può mai assumere valori nell'intervallo $(a, b]$.
+++
**Vera**. Per il {prf:ref}`lemma-ripartizione-intervallo`,
$\mathbb P(a < X \leq b) = F_X(b) - F_X(a) = 0$, il che significa che la
probabilità che $X$ cada nell'intervallo $(a, b]$ è nulla.
````

````{tf-item}
Due variabili aleatorie con la stessa funzione di ripartizione coincidono come funzioni da $\Omega$ a $\mathbb R$.
+++
**Falsa**. Consideriamo lo spazio degli esiti
$\Omega= \{ \omega_1, \omega_2 \}$, e su di esso definiamo
$\mathbb P(\{ \omega_1 \}) = \mathbb P(\{ \omega_2 \})=\frac{1}{2}$. Le due
variabili aleatorie $X$ e $Y$ definite da $X(\omega_1) = 0$, $X(\omega_2) = 1$,
$Y(\omega_1) = 1$ e $Y(\omega_2) = 0$ non coincidono come funzioni su $\Omega$,
poiché ad esempio $X(\omega_1) \neq Y(\omega_1)$. Tuttavia,
$\mathbb P(X=0) = \mathbb P(X=1) = \frac{1}{2}$ e
$\mathbb P(Y=0) = \mathbb P(Y=1) = \frac{1}{2}$. Di conseguenza le due funzioni
di ripartizione coincidono:

```{math}
F_X(x) = F_Y(x)=
\begin{cases}
0           & \text{se $x < 0$},\\
\frac{1}{2} & \text{se $0 \leq x <1$}, \\
1           & \text{se $x \geq 1$}.
\end{cases}
```

Quindi due variabili aleatorie possono avere la stessa funzione di ripartizione
pur essendo diverse come funzioni da $\Omega$ a $\mathbb R$.
````

````{tf-item}
La funzione di ripartizione caratterizza completamente la distribuzione di $X$.
+++
**Vera**. Per il {prf:ref}`thm-caratterizzazione-ripartizione`, la funzione
di ripartizione $F_X$ determina univocamente la distribuzione di $X$: due
variabili aleatorie con la stessa $F_X$ hanno la stessa distribuzione di
probabilità.
````

## Esercizi

````{exercise} •
:label: esercizio-moon-girl

Durante alcuni esperimenti sulle anomalie temporali, {extlink}`Moon Girl
<https://marvel.fandom.com/wiki/Lunella_Lafayette_(Earth-616)>`
utilizza un dispositivo che deve classificare tre segnali come provenienti o
meno da una distorsione temporale. Per semplificare il modello, assumiamo che
per ciascun segnale il dispositivo abbia la stessa probabilità di fornire una
classificazione corretta ($C$) o errata ($E$), e che le classificazioni siano
indipendenti tra loro. Sia $X$ la variabile aleatoria che conta il numero
di classificazioni corrette.

1. Descrivete lo spazio degli esiti $\Omega$ dell'esperimento aleatorio
   collegato.
2. Per ciascun valore $x$ che $X$ può assumere, elencate gli esiti che
   compongono l'evento $\{X = x\}$ e calcolate $\mathbb P(X = x)$.
3. Calcolate $\mathbb P(X \geq 2)$ e $\mathbb P(X \leq 1)$, e verificate che le
   due probabilità siano coerenti tra loro.
4. Calcolate la probabilità dell'evento «il numero di classificazioni corrette
   è pari», cioè $\mathbb P(X \in \{0, 2\})$.
````

````{solution} esercizio-moon-girl
:class: dropdown

1. Lo spazio degli esiti è $\Omega = \{ C, E \}^3$, cioè l'insieme delle terne
   ordinate di classificazioni: contiene $2^3 = 8$ esiti, ognuno dei quali
   ha probabilità $\tfrac{1}{8}$.
2. La variabile $X$ può assumere tutti i valori interi da $0$ (nessuna delle
   classificazioni è corretta) a $3$ (tutte le classificazioni sono corrette),
   e

   ```{math}
   \begin{aligned}
   \{ X = 0 \} &= \{ (E,E,E) \}, & \mathbb P(X = 0) &= \tfrac{1}{8}, \\
   \{ X = 1 \} &= \{ (C, E, E), (E, C, E), (E, E, C) \},
                                  & \mathbb P(X = 1) &= \tfrac{3}{8}, \\
   \{ X = 2 \} &= \{ (C, C, E), (C, E, C), (E, C, C) \},
                                  & \mathbb P(X = 2) &= \tfrac{3}{8}, \\
   \{ X = 3 \} &= \{ (C, C, C) \}, & \mathbb P(X = 3) &= \tfrac{1}{8}.
   \end{aligned}
   ```

   Si verifica immediatamente che la somma di queste probabilità è $1$.
3. L'evento $\{ X \geq 2 \}$ si può esprimere come
   $\{ X = 2 \} \cup \{ X = 3 \}$, e questi due ultimi eventi sono disgiunti,
   pertanto per il terzo assioma di Kolmogorov
   $\mathbb P(X \geq 2) = \mathbb P(X = 2) + \mathbb P(X = 3) = \tfrac{3}{8} +
   \tfrac{1}{8} = \tfrac{1}{2}$. Analogamente,
   $\mathbb P(X \leq 1) = \mathbb P(X = 0) + \mathbb P(X = 1) = \tfrac{1}{8} +
   \tfrac{3}{8} = \tfrac{1}{2}$. Le due probabilità ottenute sommano a $1$,
   riflettendo il fatto che $\{ X \geq 2 \}$ e $\{ X \leq 1 \}$ sono
   complementari l'uno dell'altro.
4. $\mathbb P(X \in \{ 0, 2 \}) = \mathbb P(X = 0) + \mathbb P(X = 2) =
   \tfrac{1}{8} + \tfrac{3}{8} = \tfrac{1}{2}$.
````

````{exercise} ••
:label: esercizio-moon-girl-2

Come cambierebbero le risposte all'esercizio precedente se le classificazioni
corretta ed errata avessero, rispettivamene, probabilità $\tfrac{3}{4}$ e
$\tfrac{1}{4}$?
````

````{solution} esercizio-moon-girl-2
:class: dropdown

1. Sebbene gli esiti non siano più equiprobabili, $\Omega$ resta invariato.
2. Anche i valori che $X$ può assumere non cambiano, però sono diverse le
   relative probabilità:

   ```{math}
   \begin{aligned}
   \{ X = 0 \} &= \{ (E,E,E) \}, & \mathbb P(X = 0) &= \tfrac{1}{64}, \\
   \{ X = 1 \} &= \{ (C, E, E), (E, C, E), (E, E, C) \},
                                  & \mathbb P(X = 1) &= \tfrac{9}{64}, \\
   \{ X = 2 \} &= \{ (C, C, E), (C, E, C), (E, C, C) \},
                                  & \mathbb P(X = 2) &= \tfrac{27}{64}, \\
   \{ X = 3 \} &= \{ (C, C, C) \}, & \mathbb P(X = 3) &= \tfrac{27}{64}.
   \end{aligned}
   ```

3. In questo caso, $\mathbb P(X \geq 2) = \tfrac{27}{32}$ e
   $\mathbb P(X \leq 1) = \tfrac{5}{32}$.
4. $\mathbb P(X \in \{ 0, 2 \}) = \tfrac{1}{64} + \tfrac{27}{64}
   = \tfrac{7}{16}$.
````

````{exercise} ••
:label: esercizio-blue-beetle

Quando si attiva, lo scarabeo di {extlink}`Blue Beetle
<https://dc.fandom.com/wiki/Jaime_Reyes>` seleziona una fra quattro
configurazioni di diversa potenza, dove quest'ultima è descritta da una
variabile aleatoria $X$ che assume i valori interi da $1$ a $4$. Queste
configurazioni non sono equiprobabili: lo scarabeo predilige quelle intermedie,
e in particolare

```{math}
\mathbb P(X = 1) = \tfrac{1}{8}, \quad
\mathbb P(X = 2) = \tfrac{1}{4}, \quad
\mathbb P(X = 3) = \tfrac{1}{2}, \quad
\mathbb P(X = 4) = \tfrac{1}{8} \enspace.
```

1. Verificate che questi quattro valori definiscano effettivamente una
   distribuzione, e scrivete la forma analitica della funzione di ripartizione
   $F_X$.
2. Disegnate l'andamento del grafico di $F_X$ e indicate dove la funzione è
   costante, dove siano localizzate le sue discontinuità e quale siano le
   ampiezze dei salti corrispondenti.
3. Indicate come analizzare il grafico del punto precedente per ottenere la
   probabilità $\mathbb P(X = 3)$.
````

````{solution} esercizio-blue-beetle
:class: dropdown

1. Le quattro probabilità sono non negative e la loro somma è $1$, e ogni
   evento che riguarda $X$ si può facilmente riscrivere in termini dell'unione
   di eventi della forma $\{ X = i \}$, con $i \in [1 .. 4]$. Quindi i quattro
   valori individuano la distribuzione $\mathbb P_X$. La funzione di
   ripartizione della variabile aleatoria è

   ```{math}
   F_X(x) =
   \begin{cases}
   0 & \text{se } x < 1, \\
   \tfrac18 & \text{se } 1 \leq x < 2, \\
   \tfrac38 & \text{se } 2 \leq x < 3, \\
   \tfrac78 & \text{se } 3 \leq x < 4, \\
   1 & \text{se } x \geq 4.
   \end{cases}
   ```

2. La funzione di ripartizione ha il tipico grafico delle distribuzioni
   discrete, costante a tratti. Come si vede nel grafico generato dalla cella
   che segue, sono presenti quattro salti, in corrispondenza dei valori di $X$:
   uno di ampiezza $\tfrac{1}{8}$ in $x = 1$, un secondo ampio $\tfrac{1}{4}$
   in $x = 2$ e altri due in $x = 3$ e $x = 4$, i cui salti sono
   rispettivamente grandi $\tfrac{1}{2}$ (è il salto più pronunciato) e
   $\tfrac{1}{8}$.

```{code-cell} python

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

v = np.arange(1, 5)
p = np.array([1/8, 1/4, 1/2, 1/8])

X = st.rv_discrete(values=(v, p))

fig, ax = plt.subplots()

x_plot = np.concatenate(([v[0] - 1], v, [v[-1] + 1]))
y_plot = np.concatenate(([0], X.cdf(v), [1]))
ax.step(x_plot, y_plot, where='post', color='C0')

prev = np.concatenate(([0.0], X.cdf(v)[:-1]))
ax.plot(v, X.cdf(v), 'o', color='C0', zorder=3)

ticks = np.array([1, 3, 7, 8]) / 8
labels = [str(Fraction(t)) for t in ticks]
ax.set_yticks(ticks)
ax.set_yticklabels(labels)

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$F_X(x)$')
plt.show()
```

3. Si ritrova la probabilità $\mathbb P(X = 3)$ considerando l'ampiezza del
   salto in $x = 3$. Nel punto precedente abbiamo visto che tale ampiezza è
   uguale a $\tfrac{1}{2}$. Da un punto di vista operativo, la si può
   determinare calcolando la differenza tra i valori della funzione di
   ripartizione in $3$ e in uno dei valori prossimi a sinistra; più
   precisamente,

   ```{math}
   \mathbb P(X = 3) = F_X(3) - \lim_{x \to 3^-} F_X(x)
   = F_X(3) - F_X(2)
   = \tfrac{7}{8} - \tfrac{3}{8} = \tfrac{1}{2} \enspace,
   ```

   che coincide con la probabilità assegnata in partenza.
````

````{exercise} ••
:label: esercizio-the-tick

Ogni volta che entra in azione, {extlink}`The Tick
<https://tick.fandom.com/wiki/The_Tick>` urla ogni volta il suo grido di
battaglia («SPOON!») un numero diverso di volte. Indichiamo con $X$ la
variabile aleatoria che indica il numero di grida lanciate, e assumiamo

```{math}
\mathbb P(X = 0) = \tfrac{1}{2}, \quad
\mathbb P(X = 1) = \tfrac{1}{4}, \quad
\mathbb P(X = 2) = \tfrac{1}{8}, \quad
\mathbb P(X = 3) = \tfrac{1}{8} \enspace.
```

Scrivete la funzione di ripartizione $F_X$, visualizzatene il graifco e poi
utilizzate il {prf:ref}`lemma-ripartizione-intervallo` per calcolare le
seguenti probabilità:

1. $\mathbb P(0 < X \leq 2)$,
2. $\mathbb P(0 \leq X \leq 2)$,
3. $\mathbb P(0 < X < 2)$,
4. $\mathbb P(X = 2)$.

Confrontate i primi tre risultati e spiegate perché differiscono, pur
riferendosi a intervalli con gli stessi estremi.
````

````{solution} esercizio-the-tick
:class: dropdown

La funzione di ripartizione è

```{math}
F_X(x) =
\begin{cases}
0 & \text{se } x < 0, \\
\tfrac{1}{2} & \text{se } 0 \leq x < 1 \enspace, \\
\tfrac{3}{4} & \text{se } 1 \leq x < 2 \enspace, \\
\tfrac{7}{8} & \text{se } 2 \leq x < 3 \enspace, \\
1 & \text{se } x \geq 3 \enspace,
\end{cases}
```

e il suo grafico si può tracciare nel modo seguente.

```{code-cell} python

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

v = np.arange(0, 4)
p = np.array([1/2, 1/4, 1/8, 1/8])

X = st.rv_discrete(values=(v, p))

fig, ax = plt.subplots()

x_plot = np.concatenate(([v[0] - 1], v, [v[-1] + 1]))
y_plot = np.concatenate(([0], X.cdf(v), [1]))
ax.step(x_plot, y_plot, where='post', color='C0')

prev = np.concatenate(([0.0], X.cdf(v)[:-1]))
ax.plot(v, X.cdf(v), 'o', color='C0', zorder=3)

ticks = np.arange(1, 5) / 4
labels = [str(Fraction(t)) for t in ticks]
ax.set_yticks(ticks)
ax.set_yticklabels(labels)

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$F_X(x)$')
plt.show()
```

1. Il {prf:ref}`lemma-ripartizione-intervallo` si applica direttamente:

   ```{math}
   \mathbb P(0 < X \leq 2) = F_X(2) - F_X(0) = \tfrac{7}{8} - \tfrac{1}{2} =
   \tfrac{3}{8} \enspace.
   ```

2. Rispetto al caso precedente bisogna includere anche il caso $X = 0$, che
   prima veniva escluso. Un modo per farlo è quello di diminuire l'estremo
   sinistro dell'insieme, aggiungendo il primo valore da escludere:

   ```{math}
   \mathbb P(0 \leq X \leq 2) = \mathbb P(-1 < X \leq 2)
   = F_X(2) - F_X(-1) = F_X(2) = \tfrac{7}{8} \enspace.
   ```

   In alternativa, la stessa probabilità si può calcolare come
   $\mathbb P(X = 0) + \mathbb P(0 < X \leq 2) =
   \mathbb P(X = 0) + F_X(2) - F_X(0) = \tfrac{1}{2} \times \tfrac{3}{8} =
   \tfrac{7}{8}$.

3. In questo caso, possiamo procedere come nel punto precedente, escludendo il
   caso $X = 2$:

   ```{math}
   \mathbb P(0 < X < 2) = \mathbb P(0 < X \leq 1) = F_X(1) - F_X(0) =
   \tfrac{3}{4} - \tfrac{1}{2} = \tfrac14 \enspace.
   ```

4. L'evento $\{ X = 2 \}$ coincide con $\{ 1 < X \leq 2 \}$, pertanto:

   ```{math}
   \mathbb P(X = 2) = F_X(2) - F_X(1)
   = \tfrac{7}{8} - \tfrac{3}{4} = \tfrac{1}{8} \enspace.
   ```

Gli insiemi considerati nei primi tre punti hanno gli stessi estremi $0$ e $2$,
ma differiscono per il fatto di includerli o meno. Poiché $X$ assume i valori
$0$ e $2$ con probabilità non nulla, includerli o escluderli cambia il
risultato che si ottiene quando si calcola la probabilità.
````

````{exercise} ••••
:label: esercizio-brainiac

{extlink}`Brainiac 5 <https://dc.fandom.com/wiki/Querl_Dox>`, fra le menti più
acute della Legione dei Super-Eroi, sottopone le seguenti funzioni
$F \colon \mathbb R \to [0, 1]$ al vaglio del
{prf:ref}`thm-caratterizzazione-ripartizione`. Per ciascuna di esse, stabilite
se si tratta della funzione di ripartizione di una qualche variabile
aleatoria; in caso negativo, indicate quali delle condizioni del teorema non
risultano soddisfatte.

```{math}
F_1(x) =
\begin{cases}
0 & x < 0 \enspace, \\
\tfrac{x}{2} & 0 \leq x < 2 \enspace, \\
1 & x \geq 2 \enspace.
\end{cases}
```
```{math}
F_2(x) =
\begin{cases}
0 & x < 0 \enspace, \\
\tfrac34 & 0 \leq x < 1 \enspace, \\
\tfrac12 & 1 \leq x < 2 \enspace, \\
1 & x \geq 2 \enspace.
\end{cases}
```

```{math}
F_3(x) =
\begin{cases}
0 & x < 0 \enspace, \\
\tfrac13 & 0 \leq x < 1 \enspace, \\
\tfrac23 & x \geq 1 \enspace.
\end{cases}
```
```{math}
F_4(x) =
\begin{cases}
0 & x \leq 1 \enspace, \\
1 & x > 1 \enspace.
\end{cases}
```

```{math}
F_5(x) = \tfrac12 + \tfrac1\pi \arctan x \enspace.
```

```{math}
F_6(x) =
\begin{cases}
0 & x < \pi \enspace, \\
1 & x \geq \pi \enspace.
\end{cases}
```

```{math}
F_7(x) =
\begin{cases}
0 & x < 0 \enspace, \\
\tfrac{2}{3} & 0 \leq x < 1 \enspace,
1 & x \geq 1 \enspace.
\end{cases}
```

In tutti i casi nei quali la funzione rispetta le condizioni del teorema,
specificate se la distribuzione corrispondente è continua o discreta.
````

````{solution} esercizio-brainiac
:class: dropdown

- $F_1$ è una funzione di ripartizione: è non decrescente, continua da destra
  (in quanto continua _tout court_) e tende ai limiti $0$ e $1$ quando il suo
  argomento tende rispettivamente a meno e più infinito.
- $F_2$ non è una funzione di ripartizione, perché non è non decrescente: per
  la precisione, è non decrescente fino a $x = 1$, da lì fino a $x = 2$ diviene
  non crescente $\tfrac{3}{4} = F(0) > F(1) = \tfrac{1}{2}$. Soddisfa invece
  tutte le altre proprietà indicate nella tesi del teorema.
- $F_3$ non è una funzione di ripartizione: è non decrescente e continua da
  destra, inoltre $\lim_{x \to +\infty} F_3(x) = 0$. Ma
  $\lim_{x \to +\infty} F_3(x) = \tfrac{2}{3} \neq 1$.
- Anche $F_4$ non è una funzione di ripartizione: rispetta tutti i requisiti
  richiesti, a parte la continuità da destra: $F_4(1) = 0$, mentre
  $\lim_{x \to 1^+} F_4(x) = 1 \neq 0$.
- $F_5$ è una funzione di ripartizione: l'arcotangente è strettamente
  crescente e continua, dunque $F_5$ è non decrescente e continua da destra;
  inoltre $\lim_{x \to \pm\infty} \arctan x = \pm\tfrac{\pi}{2}$, pertanto,
  quando $x$ tende a più e meno infinito, $F_5(x)$ tende a $0$ e $1$,
  rispettivamente.
- $F_6$ è una funzione di ripartizione, perché è definita in modo simile a
  $F_4$, garantendo però la continuità da destra: l'unico punto di
  discontinuità è $x = 1$, e $\lim_{x \to 1^+} F_6(x) = 1 = F_6(x).
- Infine, $F_7$ è una funzione di ripartizione: per costruzione i suoi limiti
  agli estremi sono $0$ e $1$ e la continuità a destra è assicurata, inoltre la
  funzione è non decrescente.

```{margin}
Il fatto che $F_7$ corrisponda a una variabile aleatoria che assume il valore
$\pi$ non deve trarre in inganno: la sua distribuzione è discreta, perché ciò
che conta è la continuità della ripartizione, o equivalentemente dell'insieme
dei valori assunti dalla variabile aleatoria.
```
Tra tutti i casi che individuano delle funzioni di ripartizione, $F_1$ ed $F_5$
individuano una distribuzione continua, perché sono continue (e non
solamente continue da destra). Invece, $F_6$ ed $F_7$ descrivono delle
variabili aleatorie discrete, essendo costanti a tratti.
````

````{exercise} ••
:label: esercizio-atomic-robo

Dopo un intervento sul campo, {extlink}`Atomic Robo
<https://8bittheater.fandom.com/wiki/Atomic_Robo_(Character)>` entra in
modalità di raffreddamento per un tempo pari a $T$ minuti, dove $T$ è una
variabile aleatoria la cui funzione di ripartizione è

```{math}
F_T(t) =
\begin{cases}
0 & \text{se } t < 0 \enspace, \\
\dfrac{t^2}{4} & \text{se } 0 \leq t < 2 \enspace, \\
1 & \text{se } t \geq 2 \enspace.
\end{cases}
```

1. Verificate che $F_T$ soddisfi le condizioni del
   {prf:ref}`thm-caratterizzazione-ripartizione`.
2. Calcolate $\mathbb P(T \leq 1)$ e $\mathbb P(1 < T \leq \tfrac32)$.
3. Trovate il _valore mediano_ di $T$, inteso come il numero
   $m \in \mathbb R$ per cui $F_T(m) = \tfrac{1}{2}$.
````

````{solution} esercizio-atomic-robo
:class: dropdown

1. Sull'intervallo $[0, 2)$ la funzione $t \mapsto t^2/4$ è crescente, e si
   raccorda con continuità ai tratti costanti:

   ```{math}
    F_T(0) = 0 = \lim_{t \to 0} F_T(t), \quad F_T(2) = 1 = \lim_{t \to 2} F_T(t)
    \enspace,
   ```

   il che mostra che $F_T$ è continua, e a maggior ragione continua da destra.
   Per costruzione, i suoi limiti a più e meno infinito sono rispettivamente
   $0$ e $1$. Nel tratto non costante si ha $F'_T(t) = t / 2$, e la derivata è
   sempre non negativa per $t \in [0, 2)$, quindi $F_T$ è anche non
   decrescente, come si vede nel grafico seguente. Le tre condizioni del
   teorema sono pertanto soddisfatte.

```{code-cell} python
def F_T(t):
   return np.clip(t, 0, 2)**2 / 4

fig, ax = plt.subplots()
t = np.linspace(-1, 3, 50)
plt.plot(t, F_T(t))
plt.show()
```

2. La prima probabilità si ottiene direttamente utilizzando la definizione di
   funzione di ripartizione:

   ```{math}
   \mathbb P(T \leq 1) = F_T(1) = \tfrac14 \enspace,
   ```

   mentre la seconda si ottiene applicando il
   {prf:ref}`lemma-ripartizione-intervallo`:

   ```{math}
   \mathbb P \left(1 < T \leq \tfrac{3}{2}\right) =
   F_T \left(\tfrac{3}{2}\right) - F_T(1) = \frac{(3/2)^2}{4} - \frac14 = \frac{9}{16} - \frac{4}{16} =
   \frac{5}{16} \enspace.
   ```

3. Imponendo $F_T(m) = \tfrac12$ si ha $m^2/4 = \tfrac12$,
   cioè $m^2 = 2$ e dunque $m = \sqrt 2 \approx 1{,}41$ minuti.
````

````{exercise} •••
:label: esercizio-bouncing-boy

{extlink}`Bouncing Boy <https://dc.fandom.com/wiki/Charles_Foster_Taine>` e
{extlink}`Matter-Eater Lad <https://dc.fandom.com/wiki/Tenzil_Kem>` si
allenano per partecipare a un gioco a squadre: ciascuno lancia, in modo
indipendente dall'altro, un dado bilanciato a quattro facce. Il più alto dei
due valori ottenuti diventa il punteggio della squadra, che sarà quindi
descritto dalla variabile aleatoria $X = \max(B, M)$, dove $B$ ed $M$ sono
a loro volta variabili aleatorie che indicano i punteggi di Bouncing Boy e di
Matter-Eater.

1. Descrivete lo spazio degli esiti e dite quante coppie equiprobabili lo
   compongono.
2. Osservando che $\{X \leq k\}$ equivale a «entrambi i punteggi non superano
   $k$», calcolate $\mathbb P(X \leq k)$ per $k = 1, 2, 3, 4$ e deducete tutti
   i possibili valori di $\mathbb P(X = k)$.
3. Scrivete la forma analitica della funzione di ripartizione $F_X$.
4. Calcolate $\mathbb P(X \geq 3)$.
````

````{solution} esercizio-bouncing-boy
:class: dropdown

1. Lo spazio degli esiti è $\Omega = \{(a, b) \mid a, b \in [1 .. 4]\}$, che
   contiene $16$ coppie equiprobabili.
2. Per ogni $k \in \{1, 2, 3, 4\}$, poniamo $B_k = \{B \leq k\}$ ed
   $M_k = \{M \leq k\}$. L'evento $\{X \leq k\}$
   coincide allora con $B_k \cap M_k$, perché il massimo tra $B$ ed $M$ non
   supera $k$ se e solo se entrambi i punteggi non superano $k$. Siccome i
   due lanci sono indipendenti, anche gli eventi $B_k$ ed $M_k$ sono
   indipendenti; inoltre $\mathbb P(B_k) = \mathbb P(M_k) = \tfrac{k}{4}$.
   Quindi

   ```{math}
   \mathbb P(X \leq k) = \mathbb P(B_k \cap M_k)
   = \mathbb P(B_k) \cdot \mathbb P(M_k)
   = \left(\tfrac{k}{4}\right)^2 \enspace.
   ```

   Dunque

   ```{math}
   \mathbb P(X \leq 1) = \tfrac{1}{16}, \quad
   \mathbb P(X \leq 2) = \tfrac{2}{8}, \quad
   \mathbb P(X \leq 3) = \tfrac{9}{16}, \quad
   \mathbb P(X \leq 4) = 1 \enspace.
   ```

   ```{margin}
   Si verifica immediatamente che questi valori sommano a $1$, come dev'essere.
   ```
   Le probabilità dei singoli valori si ottengono come differenze
   consecutive (ossia come salti):

   ```{math}
   \mathbb P(X = 1) = \tfrac{1}{16}, \quad
   \mathbb P(X = 2) = \tfrac{3}{16}, \quad
   \mathbb P(X = 3) = \tfrac{5}{16}, \quad
   \mathbb P(X = 4) = \tfrac{7}{16} \enspace.
   ```

3. I valori della funzione di ripartizione sono già stati calcolati al punto
   precedente:

   ```{math}
   F_X(x) =
   \begin{cases}
   0 & \text{se } x < 1, \\
   \tfrac{1}{16} & \text{se } 1 \leq x < 2, \\
   \tfrac{4}{16} & \text{se } 2 \leq x < 3, \\
   \tfrac{9}{16} & \text{se } 3 \leq x < 4, \\
   1 & \text{se } x \geq 4.
   \end{cases}
   ```

4. Possiamo calcolare la probabilità nei seguenti due modi:
   - utilizzando la funzione di ripartizione:
     $\mathbb P(X \geq 3) = 1 - \mathbb P(X \leq 2) = 1 - \tfrac{4}{16} =
     \tfrac{3}{4}$;
   - facendo riferimento alle probabilità che $X$ assuma i valori che
     comportano che l'evento si verifichi: $\mathbb P(X \geq 3) =
     \mathbb P(X = 3) + \mathbb P(X = 4) = \tfrac{5}{16} + \tfrac{7}{16} =
     \tfrac{3}{4}$.
````

````{exercise} •
:label: esercizio-scoiattoli-bis

Considerate la variabile aleatoria $X = g_1 - g_2$
dell'{prf:ref}`ex-va-scoiattoli`, la cui funzione di ripartizione $F_X$ è stata
ricavata nell'{prf:ref}`ex-ripartizione-scoiattoli`. Usando solamente $F_X$ (e
non nuovi conteggi sugli elementi dello spazio degli esiti), calcolate:

1. $\mathbb P(-1 < X \leq 2)$;
2. $\mathbb P(X = 0)$, ottenuta come salto di $F_X$ in $0$, verificando il
   risultato contando direttamente gli esiti per cui $g_1 = g_2$;
3. $\mathbb P(X > 3)$.
````

````{solution} esercizio-scoiattoli-bis
:class: dropdown

Richiamando i valori di $F_X$ dall'{prf:ref}`ex-ripartizione-scoiattoli`:

1. Per il {prf:ref}`lemma-ripartizione-intervallo`,

   ```{math}
   \mathbb P(-1 < X \leq 2) = F_X(2) - F_X(-1) = \tfrac{5}{6} - \tfrac{5}{12}
   = \tfrac{5}{12} \enspace.
   ```

2. Il salto di $F_X$ in $0$ vale

   ```{math}
   \mathbb P(X = 0) = F_X(0) - \lim_{x \to 0^-} F_X(x)
   = \tfrac{7}{12} - \tfrac{5}{12} = \tfrac{1}{6} \enspace.
   ```

   La verifica diretta è immediata: gli esiti per cui $g_1 = g_2$ sono i sei
   elementi dell'insieme $\{ (i, i) \mid i = 1, \dots, 6 \}$, dunque
   $\mathbb P(X = 0) = \tfrac{6}{36} = \tfrac{1}{6}$.
3. $\mathbb P(X > 3) = 1 - \mathbb P(X \leq 3) = 1 - F_X(3)
   = 1 - \tfrac{11}{12} = \tfrac{1}{12}$.
````

````{exercise} •••
:label: esercizio-vero-falso

Fissato uno spazio degli esiti $\Omega$, siano date una generica variabile
aleatoria $X$ e la la sua funzione di ripartizione $F_X$. Stabilite se ciascuna
delle seguenti affermazioni è vera o falsa, motivando brevemente la risposta. 

1. Qualunque funzione $X \colon \Omega \to \mathbb R$ è una variabile
   aleatoria.
2. Se $F_X(3) = F_X(5)$, allora $\mathbb P(3 < X \leq 5) = 0$.
3. Per ogni $a \in \mathbb R$ vale
   $\mathbb P(X = a) = F_X(a) - \lim_{x \to a^-} F_X(x)$.
4. Se $F_X$ è continua nel punto $a$, allora $\mathbb P(X = a) = 0$.
5. Se $F_X$ è continua da sinistra in ogni punto, allora è continua ovunque.
````

````{solution} esercizio-vero-falso
:class: dropdown

1. **Falsa**. Quando $\Omega$ è finito o numerabile e si lavora in
   $2^\Omega$ ogni funzione soddisfa la condizione di misurabilità ed è quindi
   una variabile aleatoria; ma se la $\sigma$-algebra è più piccola di
   $2^\Omega$ &mdash; come accade necessariamente nel caso continuo &mdash;
   esistono funzioni non misurabili, che la {prf:ref}`def-variabile-aleatoria`
   esclude.
2. **Vera**. Per il {prf:ref}`lemma-ripartizione-intervallo`,
   $\mathbb P(3 < X \leq 5) = F_X(5) - F_X(3) = 0$.
3. **Vera**. Si ha $\mathbb P(X = a) = \mathbb P(X \leq a) -
   \mathbb P(X < a) = F_X(a) - \lim_{x \to a^-} F_X(x)$: la probabilità del
   singolo valore è l'ampiezza del salto di $F_X$ in $a$.
4. **Vera**. È il caso particolare del punto precedente in cui il limite da
   sinistra coincide con $F_X(a)$: il salto è nullo, quindi $\mathbb P(X = a) =
   0$.
5. **Vera**. Per il {prf:ref}`thm-proprieta-ripartizione`, $F_X$ è sempre
   continua da destra; se è anche continua da sinistra in ogni punto, allora i
   due limiti laterali coincidono con il valore della funzione ovunque, ed è
   dunque continua.
````


## Concetti fondamentali

Pensate ai concetti fondamentali illustrati in questo paragrafo ed elencateli.
Nella lista qui sotto sono già presenti gli stessi concetti, ma nascosti.
Cliccate sul pulsante per mostrarli sotto forma di parole chiave, quindi
confrontateli con la vostra lista. Provate infine a descrivere ciascun concetto
con parole vostre.

````{sds-wordcloud}
Variabile aleatoria
Misurabilità
Distribuzione di una variabile aleatoria
Funzione di ripartizione
Distribuzione discreta
Distribuzione continua
Caratterizzazione delle funzioni di ripartizione
````

