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

(chap:formule-notevoli)=
# Formule notevoli

````{prf:theorem} Somma dei primi $n$ interi
:label: teo-sum-1

La somma dei primi $n \in \mathbb N$ numeri interi è

```{math}
:label: eq:sum-pow-1

\sum_{i=1}^n i = \frac{n(n+1)}{2} \enspace.
```
````
````{admonition} _
:class: myproof

Sia $S = \sum_{i=1}^n i$: lo schema seguente elenca nella prima riga tutti
gli addendi della somma in $S$ dal primo all'ultimo, e nella seconda gli
stessi addendi nell'ordine inverso. In fondo a ognuna di queste due righe
è indicata la somma di tutti i relativi elementi, che per definizione è
in entrambi i casi $S$. Ogni elemento della terza riga è ottenuto sommando
i due elementi che stanno al di sopra di lui nella medesima colonna, e si
vede facilmente come il risultato di questa somma sia sempre uguale a $n+1$.

<table class="centered-content">
  <tr>
    <td>$1$</td>
    <td>$2$</td>
    <td>$3$</td>
    <td>$\dots$</td>
    <td>$n-2$</td>
    <td>$n-1$</td>
    <td>$n$</td>
    <td style="border-left: 1px solid black;">$S$</td>
  </tr>
  <tr>
    <td>$n$</td>
    <td>$n-1$</td>
    <td>$n-2$</td>
    <td>$\dots$</td>
    <td>$3$</td>
    <td>$2$</td>
    <td>$1$</td>
    <td style="border-left: 1px solid black;">$S$</td>
  </tr>
  <tr style="border-top: 1px solid black;">
    <td>$n+1$</td>
    <td>$n+1$</td>
    <td>$n+1$</td>
    <td>$\dots$</td>
    <td>$n+1$</td>
    <td>$n+1$</td>
    <td>$n+1$</td>
    <td style="border-left: 1px solid black;">$2S$</td>
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
:label: eq:sum-pow-2

\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6} \enspace.
```
````
````{admonition} _
:class: myproof

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
:label: eq:sum-pow-3

\sum_{i=1}^n i^2 = \frac{n^2(n+1)^2}{4} \enspace.
```
````
````{admonition} _
:class: myproof

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
:label: teo:sum-4

La somma delle quarte potenze dei primi $n \in \mathbb N$ numeri interi è

```{math}
:label: eq:sum-pow-4

\sum_{i=1}^n i^4 = \frac{n(n+1)(2n+1)(3n^2 + 3n - 1)}{30} \enspace.
```
````
````{admonition} _
:class: myproof

Applicando la tecnica di dimostrazione per induzione su $n$, il caso base
$n=1$ si verifica banalmente per ispezione: il membro sinistro
dell'uguaglianza vale $1$ e il suo membro destro vale
$\frac{1 \cdot 2 \cdot 3 \cdot 5}{30} = 1$. Per quanto riguarda il passo
dell'induzione, vale la pena scriverlo in questo modo: posto

$$ P(n) \triangleq n(n+1)(2n+1)(3n^2 + 3n - 1) \enspace, $$

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
D(n) &= (n + 1)(3n^2 + 3n - 1) \left( (n+2)(n+3) - n(2n+1) \right) + 6 (n+1)^2 (n+2) (2n+3) \\
     &= 6 (n+1)^2 (3n^2 + 3n - 1) + 6 (n+1)^2 (n+2) (2n+3) \\
     &= 6 (n+1)^2 (5n^2 + 10n + 5) \\
     &= 30 (n+1)^4 \enspace.
\end{align*}

````