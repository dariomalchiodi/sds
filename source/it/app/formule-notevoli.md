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

(chap_formule-notevoli)=
# Formule notevoli

````{prf:theorem} Somma dei primi $n$ interi
:label: teo-sum-1

La somma dei primi $n \in \mathbb N$ numeri interi è

```{math}
:label: eq_sum-pow-1

\sum_{i=1}^n i = \frac{n(n+1)}{2} \enspace.
```
````
````{sds-proof}
Sia $S = \sum_{i=1}^n i$: lo schema seguente elenca nella prima riga tutti
gli addendi della somma in $S$ dal primo all'ultimo, e nella seconda gli
stessi addendi nell'ordine inverso. In fondo a ognuna di queste due righe
è indicata la somma di tutti i relativi elementi, che per definizione è
in entrambi i casi $S$. Ogni elemento della terza riga è ottenuto sommando
i due elementi che stanno al di sopra di lui nella medesima colonna, e si
vede facilmente come il risultato di questa somma sia sempre uguale a $n+1$.

<table class="centered-content">
  <tr>
    <td>\( 1 \)</td>
    <td>\( 2 \)</td>
    <td>\( 3 \)</td>
    <td>\( \dots \)</td>
    <td>\( n-2 \)</td>
    <td>\( n-1 \)</td>
    <td>\( n \)</td>
    <td style="border-left: 1px solid black;">\( S \)</td>
  </tr>
  <tr>
    <td>\( n \)</td>
    <td>\( n-1 \)</td>
    <td>\( n-2 \)</td>
    <td>\( \dots \)</td>
    <td>\( 3 \)</td>
    <td>\( 2 \)</td>
    <td>\( 1 \)</td>
    <td style="border-left: 1px solid black;">\( S \)</td>
  </tr>
  <tr style="border-top: 1px solid black;">
    <td>\( n+1 \)</td>
    <td>\( n+1 \)</td>
    <td>\( n+1 \)</td>
    <td>\( \dots \)</td>
    <td>\( n+1 \)</td>
    <td>\( n+1 \)</td>
    <td>\( n+1 \)</td>
    <td style="border-left: 1px solid black;">\( 2S \)</td>
  </tr>
</table>

Pertanto, $2 S$ è uguale alla somma di tutti gli altri elementi sull'ultima
riga, ma questi sono sempre uguali a $n + 1$, e sono $n$ in tutto. Il che ci
permette di concludere che $2 S = n (n + 1)$, da cui segue la tesi.
````

````{prf:theorem} Somma dei quadrati dei primi $n$ interi
:label: teo-sum-2

La somma dei quadrati dei primi $n \in \mathbb N$ numeri interi è

```{math}
:label: eq_sum-pow-2

\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6} \enspace.
```
````
````{sds-proof}
Applicando la tecnica di dimostrazione per induzione su $n$, il caso base
$n=1$ si verifica banalmente per ispezione: il membro sinistro
dell'uguaglianza vale $1$ e il suo membro destro vale
$\frac{1 \cdot 2 \cdot 3}{6} = 1$. Per quanto riguarda il passo
dell'induzione,

```{math}
\begin{align*}
\sum_{i=1}^{n+1} i^2 &= \sum_{i=1}^n i^2 + (n+1)^2 \\
                     &= \frac{n(n+1)(2n+1)}{6} + (n+1)^2 \\
                     &= (n+1) \frac{n(2n+1) + 6(n+1)}{6} \\
                     &= (n+1) \frac{2n^2 + 7n +6}{6} \\
                     &= (n+1) \frac{(n + 2)(2n + 3)}{6} \enspace.
\end{align*}
```
````

````{prf:theorem} Somma dei cubi dei primi $n$ interi
:label: teo-sum-3

La somma dei cubi dei primi $n \in \mathbb N$ numeri interi è

```{math}
:label: eq_sum-pow-3

\sum_{i=1}^n i^2 = \frac{n^2(n+1)^2}{4} \enspace.
```
````
````{sds-proof}
Applicando la tecnica di dimostrazione per induzione su $n$, il caso base
$n=1$ si verifica banalmente per ispezione: il membro sinistro
dell'uguaglianza vale $1$ e il suo membro destro vale
$\frac{1^2 \cdot 2^2}{4} = 1$. Per quanto riguarda il passo
dell'induzione,

```{math}
\begin{align*}
\sum_{i=1}^{n+1} i^3 &= \sum_{i=1}^n i^3 + (n+1)^3 \\
                     &= \frac{n^2(n+1)^2}{4} + (n+1)^3 \\
                     &= (n+1)^2 \left( \frac{n^2}{4} + n + 1 \right) \\
                     &= (n+1)^2 \frac{n^2 + 4n + 4}{4} \\
                     &= (n+1)^2 \frac{(n + 2)^2}{4} \enspace.
\end{align*}
```
````

````{prf:theorem} Somma delle quarte potenze dei primi $n$ interi
:label: teo-sum-4

La somma delle quarte potenze dei primi $n \in \mathbb N$ numeri interi è

```{math}
:label: eq_sum-pow-4

\sum_{i=1}^n i^4 = \frac{n(n+1)(2n+1)(3n^2 + 3n - 1)}{30} \enspace.
```
````
````{sds-proof}
Applicando la tecnica di dimostrazione per induzione su $n$, il caso base
$n=1$ si verifica banalmente per ispezione: il membro sinistro
dell'uguaglianza vale $1$ e il suo membro destro vale
$\frac{1 \cdot 2 \cdot 3 \cdot 5}{30} = 1$. Per quanto riguarda il passo
dell'induzione, vale la pena scriverlo in questo modo: posto

```{math}
P(n) \triangleq n(n+1)(2n+1)(3n^2 + 3n - 1) \enspace,
```

dobbiamo dimostrare che 

```{math}
\begin{align*}
\sum_{i=1}^{n+1} i^4 &= \frac{P(n+1)}{30} \enspace.
\end{align*}
```

Ora, sfruttando l'ipotesi induttiva,
```{math}
\begin{align*}
\sum_{i=1}^{n+1} i^4 &= \sum_{i=1}^n i^4 + (n+1)^4 \\
                     &= \frac{P(n)}{30} + (n+1)^4 \enspace,
\end{align*}
```

pertanto ci basta dimostrare che $D(n) \triangleq P(n+1) - P(n) = 30 (n + 1)^4$. Questa
uguaglianza si verifica procedendo nel modo seguente: innanzitutto, vale

```{math}
\begin{align*}
D(n) &= (n+1)(n+2)(2n+3)(3n^2 + 9n + 5) - n(n+1)(2n+1)(3n^2 + 3n - 1) \\
     &= (n+1) \left( (n+2)(2n+3)(3n^2 + 9n + 5) - n(2n+1)(3n^2 + 3n - 1) \right) \enspace.
\end{align*}
```

Osservando ora che $(3n^2 + 9n + 5) = (3n^2 + 3n - 1) + 6(n + 1)$, si può
ricavare

```{math}
\begin{align*}
D(n) &= (n + 1)(3n^2 + 3n - 1) \left( (n+2)(n+3) - n(2n+1) \right) + \\
     & \quad\quad 6 (n+1)^2 (n+2) (2n+3) \\
     &= 6 (n+1)^2 (3n^2 + 3n - 1) + 6 (n+1)^2 (n+2) (2n+3) \\
     &= 6 (n+1)^2 (5n^2 + 10n + 5) \\
     &= 30 (n+1)^4 \enspace.
\end{align*}
````

La _serie geometrica_ è una serie numerica fondamentale, nota fin
dall'antichità. Si chiama così perché originariamente era usata per risolvere
problemi geometrici, come il calcolo della somma di aree o volumi in una
progressione in cui ogni termine è una frazione costante di quello precedente.
Oltre che al calcolo delle probabilità, viene applicata per esempio in fisica
ed economia, ma anche per analizzare altre serie. I prossimi risultati
mostrano come ricavare la formula della somma finita e della serie infinita,
in due varianti.

````{prf:definition} Serie geometrica
Dato $q \in \mathbb R$, la somma

```{math}
\sum_n q^n \enspace,
```

contata a partire da $n = 0$, viene detta _serie geometrica_ di _ragione_ $q$.
````

````{prf:theorem}
:label: teo-sum-geometrica

Per ogni $q \in \mathbb R$ e per ogni $n \in \mathbb N$ si ha

```{math}
:label: eq-sum-geometrica

\sum_{i=0}^n q^i =
\begin{cases}
n+1 & \text{se } q = 1 \\
\dfrac{1-q^{n+1}}{1-q} & \text{se } q \neq 1
\end{cases}
\enspace.
```
````
````{sds-proof}
Se $q = 1$, allora tutti gli addendi sono uguali a $1$, quindi la somma vale
immediatamente $n+1$.

Supponiamo ora $q \neq 1$ e poniamo

```{math}
S_n = \sum_{i=0}^n q^i = 1 + q + q^2 + \dots + q^n \enspace.
```

Moltiplicando entrambi i membri per $q$, otteniamo

```{math}
q S_n = q + q^2 + \dots + q^n + q^{n+1} \enspace.
```

Sottraendo membro a membro la seconda uguaglianza dalla prima, tutti i termini
intermedi si cancellano e rimane

```{math}
S_n - q S_n = 1 - q^{n+1} \enspace.
```

Raccogliendo $S_n$ al primo membro, si ricava quindi

```{math}
(1-q) S_n = 1 - q^{n+1} \enspace.
```

Poiché $q \neq 1$, possiamo dividere per $1-q$ e ottenere

```{math}
S_n = \frac{1-q^{n+1}}{1-q} \enspace,
```

che conclude la dimostrazione.
````

````{prf:theorem}
:label: teo-sum-geometrica-infinita

Se $q \in \mathbb R$ soddisfa $\lvert q \rvert < 1$, allora la serie geometrica infinita

```{math}
:label: eq-sum-geometrica-infinita

\sum_{i=0}^{+\infty} q^i
```

converge e la sua somma è uguale a

```{math}
:label: eq-lim-geometrica

\sum_{i=0}^{+\infty} q^i = \frac{1}{1-q} \enspace.
```
````
````{sds-proof}
Per il {prf:ref}`teo-sum-geometrica`, la somma parziale dei primi $n+1$ termini
è data da

```{math}
S_n = \sum_{i=0}^n q^i = \frac{1-q^{n+1}}{1-q} \enspace.
```

Se $|q| < 1$, allora $q^{n+1} \to 0$ per $n \to +\infty$. Passando quindi al
limite nelle somme parziali, si ottiene

```{math}
\sum_{i=0}^{+\infty} q^i = \lim_{n \to +\infty} S_n
= \lim_{n \to +\infty} \frac{1-q^{n+1}}{1-q}
= \frac{1}{1-q} \enspace.
```
````

````{prf:corollary}
Se $q \in \mathbb R$ soddisfa $|q| < 1$, allora

```{math}
:label: eq-serie-geometrica-da-uno
\sum_{i=1}^{+\infty} q^i = \frac{q}{1-q} \enspace.
```
````
````{sds-proof}
Per il {prf:ref}`teo-sum-geometrica-infinita`, si ha

```{math}
\sum_{i=0}^{+\infty} q^i = 1 + \sum_{i=1}^{+\infty} q^i = \frac{1}{1-q}
\enspace,
```

quindi

```{math}
\sum_{i=1}^{+\infty} q^i = \frac{1}{1-q} - 1 = \frac{q}{1-q} \enspace.
```

````

````{prf:theorem}
:label: thm-serie-e

Per ogni $x \in \mathbb R$ vale l'identità

```{math}
:label: eq-e-mclaurin
\sum_{n=0}^{\infty} \frac{x^n}{n!} = \mathrm e^x.
```
````
````{sds-proof}
Sia $f(x) \triangleq \mathrm e^n$. Questa funzione coincide con la sua derivata
di un ordine qualsiasi, per cui $f^{(n)}(0) = e^0 = 1$. Applicando lo sviluppo
in serie di Maclaurin si ottiene pertanto

```{math}
\mathrm e^x = \sum_{n=0}^{\infty} \frac{f^{(n)}(0) x^n}{n!}
= \sum_{n=0}^{\infty} \frac{x^n}{n!} \enspace.
```

Inoltre, per ogni $x \in \mathbb R$ si ha

```{math}
\lim_{n \to +\infty} \left\lvert \frac{x^{n+1}/(n+1)!}{x^n/n!} \right\rvert
= \lim_{n \to +\infty} \frac{\lvert x \rvert}{n+1} = 0 < 1 \enspace.
```

Per il criterio del rapporto, la serie {eq}`eq-e-mclaurin` ha un raggio di
convergenza infinito.
````

````{prf:theorem} Formula del binomio di Newton
:label: teo-binomio-newton

Dati $a, b \in \mathbb R$ e $n \in \mathbb N$, vale l'identità

```{math}
:label: eq-binomio-newton

(a+b)^n = \sum_{i=0}^{n} \binom{n}{i}a^i b^{n-i} \enspace,
```

detta _formula del binomio di Newton_[^binomio-newton].
````
````{sds-proof}
Fissando $a$ e $b$ e procedendo per induzione su $n$, il caso base è banalmente
vero:

```{math}
(a+b)^0 = 1 = \binom{0}{0}a^0b^0 = \sum_{i=0}^{0} \binom{0}{i}a^i b^{0-i}
\enspace.
```

Per quanto riguarda il passo induttivo, supponendo {eq}`eq-binomio-newton`
vera per un dato $n$, si ha

```{math}
\begin{align}
(a+b)^{n+1} &= (a+b) \sum_{i=0}^{n} \binom{n}{i}a^i b^{n-i} \notag \\
&= \sum_{i=0}^{n} \binom{n}{i}a^{i+1}b^{n-i}
+ \sum_{i=0}^{n} \binom{n}{i}a^i b^{n+1-i}  \notag\\
&= \sum_{j=1}^{n+1} \binom{n}{j-1}a^j b^{n+1-j}
+ \sum_{i=0}^{n} \binom{n}{i}a^i b^{n+1-i} \tag*{($i \mapsto j-1$)}\\
&= \sum_{i=1}^{n+1} \binom{n}{i-1}a^i b^{n+1-i}
+ \sum_{i=0}^{n} \binom{n}{i}a^i b^{n+1-i} \tag*{($j \mapsto i$)}
\end{align}
```

Estrando l'ultimo termine della prima sommatoria e il primo della seconda,
è possibile raccogliere $a^i b^{n+1-i}$ a fattore comune:

```{math}
:label: eq-tartaglia-ind

(a+b)^{n+1} = a^{n+1} + \sum_{i=1}^{n}\left[\binom{n}{i-1}+\binom{n}{i}\right]
a^i b^{n+1-i} + b^{n+1} \enspace.
```

Siccome

```{margin}
Questa formula è anche nota come _identità di Pascal_, ed è alla base della
creazione del famoso
[triangolo di Tartaglia](https://it.wikipedia.org/wiki/Triangolo_di_Tartaglia),
una disposizione grafica che permette di calcolare ricorsivamente i
coefficienti binomiali[^triangolo-tartaglia].
```
```{math}
\begin{aligned}
\binom{n}{i-1} + \binom{n}{i}
&= \frac{n!}{(i-1)! (n-i+1)!} + \frac{n!}{i! (n-i)!}
= \frac{i n! + (n-i+1) n!}{i! (n-i+1)!} \\
&= \frac{(n+1)!}{i! (n+1 - i)!}
= \binom{n+1}{i} \enspace,
\end{aligned}
```

è possibile riformulare {eq}`eq-tartaglia-ind` nel modo seguente:

```{math}
\begin{aligned}
(a+b)^{n+1} &= \binom{n+1}{0} b^{n+1} + \sum_{i=1}^{n}\binom{n+1}{i}
a^i b^{n+1-i} + \binom{n+1}{n+1} a^{n+1} \\
&= \sum_{i=0}^{n+1} \binom{n+1}{i}a^i b^{n+1-i} \enspace.
\end{aligned}
```

La formula è quindi vera per $n+1$ e, per il principio di induzione, per
ogni intero $n\geq 0$.
````

````{prf:theorem} Formula del binomio di Newton
:label: teo-binomio-newton

Per ogni $a, x \in \mathbb R$, con $a > 0$, vale l'identità

```{math}
:label: eq-doppia-exp

\mathrm e^{a \lvert x \rvert} \leq \mathrm e^{a x} + \mathrm e^{-a x} \enspace.
```

````
````{sds-proof}
Quando $x \geq 0$, l'identità assume la forma
$\mathrm e^{a x } \leq \mathrm e^{a x} + \mathrm e^{-a x}$, che equivale a
$\mathrm e^{-2ax} \geq 0$, che è banalmente vera. Analogamente, è facile
verificare che per $x < 0$ l'identità equivale a $\mathrm e^{2ax} \geq 0$.
````

[^binomio-newton]: In realtà, la forma dell'identità {eq}`eq-binomio-newton`
che coinvolge esponenti interi non negativi era già nota in Europa almeno dal
XVI secolo, e ancora prima nella tradizione matematica indiana, islamica e
cinese. Tra il 1664 e il 1665, tuttavia, Isaac Newton estese lo sviluppo del
binomio agli esponenti frazionari e negativi, ottenendo una serie generalmente
infinita. È principalmente a questa generalizzazione che si deve il nome
tradizionale di formula del binomio di Newton, applicato poi anche al caso
finito.

[^triangolo-tartaglia]: È interessante notare che, nel resto del mondo
occidentale, lo stesso schema è noto come _triangolo di Pascal_, sebbene, come
il binomio di Newton, sia stato utilizzato antecedentemente da altri matematici
europei (tra cui Tartaglia), e prima ancora cinesi, persiani e arabi. Un
contributo originale di Pascal è invece legato alla dimostrazione della
correttezza della procedura, fatta in modo combinatorio e organizzata nel modo
seguente. Partendo da un insieme $S$ di $n+1$ oggetti, sia $s$ uno di questi.
Un generico sottoinsieme di $S$ contenente $i$ elementi deve contenere $s$
oppure escluderlo. Quindi il numero di possibili sottoinsiemi di $i$ oggetti
(che è uguale a $\binom{n+1}{i}$) si ottiene sommando il numero di quelli che
includono $s$ (pari a $\binom{n}{i-1}$) a quello dei rimanenti sottoinsiemi
(che sono $\binom{n}{i}$).
