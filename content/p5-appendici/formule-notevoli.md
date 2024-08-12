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

(sec:formule-notevoli)=
# Formule notevoli

````{prf:theorem} Somma dei primi $n$ interi
:label: teo:sum-1

Per ogni $n \in \mathbb N$

```{math}
:label: eq:sum-pow-1

\sum_{i=1}^n i = \frac{n(n+1)}{2} \enspace.
```
````
````{prf:proof}
Sia $S = \sum_{i=1}^n i$: lo schema seguente elenca nella prima riga tutti
gli addendi della somma in $S$ dal primo all'ultimo, e nella seconda gli
stessi addendi nell'ordine inverso. In fondo a ognuna di queste due righe
è indicata la somma di tutti i relativi elementi, che per definizione è
in entrambi i casi $S$. Ogni elemento della terza riga è ottenuto sommando
i due elementi che stanno al di sopra di lui nella medesima colonna, e si
vede facilmente come il risultato di questa somma sia sempre uguale a $n+1$,

\begin{tabular}[rrrrrrrr]
$1$   & $2$   & $3$   & $\dots$ & $n-2$ & $n-1$ & $n$   & $S$ \\
$n$   & $n-1$ & $n-2$ & $\dots$ & $3$   & $2$   & $1$   & $S$ \\
$n+1$ & $n+1$ & $n+1$ & $\dots$ & $n+1$ & $n+1$ & $n+1$ & $2S$
\end{tabular}
````

````{prf:theorem} Somma dei quadrati dei primi $n$ interi
:label: teo:sum-2

Per ogni $n \in \mathbb N$

```{math}
:label: eq:sum-pow-2

\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6} \enspace.
```
````
````{prf:proof}
Applicando la tecnica di dimostrazione per induzione su $n$, il caso base
$n=1$ si verifica banalmente per ispezione: il membro sinistro
dell'uguaglianza vale $1$ e il suo membro destro vale
$\frac{1 \cdot 2 \cdot 3}{6} = 1$. Per quanto riguarda il passo
dell'induzione,

\begin{equation*}
\sum_{i=1}^{n+1} i^2 = \sum_{i=1}^n+ i^2 + (n+1)^2
                     = \frac{n(n+1)(2n+1)}{6} + (n+1)^2
                     = (n+1) \frac{n(2n+1) + 6(n+1)}{6}
                     = (n+1) \frac{2n^2 + 7n +6}{6}
\end{eqaution*}

````

````{prf:theorem} Somma dei cubi dei primi $n$ interi
:label: teo:sum-3

Per ogni $n \in \mathbb N$

```{math}
:label: eq:sum-pow-3

\sum_{i=1}^n i^2 = \frac{n^2(n+1)^2}{4} \enspace.
```

````

````{prf:theorem} Somma delle quarte potenze dei primi $n$ interi
:label: teo:sum-4

Per ogni $n \in \mathbb N$

```{math}
:label: eq:sum-pow-4

\sum_{i=1}^n i^4 = \frac{n(n+1)(2n+1)(3n^2 + 3n - 1)}{30} \enspace.
```

````