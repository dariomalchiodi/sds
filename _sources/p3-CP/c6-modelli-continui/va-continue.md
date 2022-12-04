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

(sec:va-continue)=
# Variabili aleatorie continue

Di seguito formalizziamo e generalizziamo i nuovi concetti che sono emersi nel
paragrafo precedente. In particolare, partiamo dalla definizione di _variabile
aleatoria continua_.

```{margin}
Come indicato nella {prf:ref}`def:dominio`, per dominio si intende qui
l'insieme delle specificazioni di una variabile aleatoria.
```
````{prf:definition} Variabile aleatoria continua
:label: def:va-continua

Una variabile aleatoria $X$ si dice _continua_ quando il suo dominio $D_X$ è
un insieme continuo.
````

Il calcolo di probabilità di eventi collegati a una variabile aleatoria
continua viene normalmente fatto utilizzando la relativa funzione di
ripartizione, che è definita esattamente come nel caso di una variabile
aleatoria discreta, oppure in termini della funzione di densità introdotta
in modo informale nel paragrafo precedente. Per definire questo concetto in
modo più preciso, notiamo innanzitutto che per $x \in \mathbb R$ e
$\Delta x \in \mathbb R^+$, è sempre possibile considerare l'evento
$X \in (x, x + \Delta x]$ che si verifica quando $X$ assume valori
nell'intervallo che ha $x$ come estremo sinistro e $\Delta x$ come ampiezza.
Infatti, in base alla {prf:ref}`def:variabile-aleatoria` sappiamo che

```{math}
X^{-1}((-\infty, a]) = \{ w \in \Omega \text{ tale che } X(\omega) \leq a \}
```

è sempre contenuto nell'algebra degli eventi $\mathsf A$ che stiamo
considerando, e siccome

```{math}
X \in (x, x + \Delta x] = X^{-1}((-\infty, x + \Delta x]) \,\backslash\,
                          X^{-1}((-\infty, x]) \,,
```

il {prf:ref}`teo-chiusura-algebra-eventi` ci permette di concludere che anche
$X \in (x, x + \Delta x]$ è contenuto in $\mathsf A$. Risulta dunque ben
definito il rapporto

```{math}
\frac{\mathbb P(X \in (x, x + \Delta x])}{\Delta x} \,,
```

così come il suo limite per $\Delta x \to 0$, che permette di definire la
la densità di probabilità in $x$.

````{prf:definition} Funzione di densità
:label: def:densita

La _funzione di densità_ di una variabile aleatoria continua $X$ è una
funzione $f_X: \mathbb R \rightarrow \mathbb R^+$ che associa a ogni argomento
$x \in \mathbb R$ il valore

```{math}
f_X(x) =
\lim_{\Delta x \to 0}\frac{\mathbb P(X \in (x, x + \Delta x])}{\Delta x} \,,
```

che indica la densità della probabilità che $X$ assuma valori a destra di $x$.
````

Siccome

\begin{align*}
\mathbb P(X \in (x, x + \Delta x]) &= \mathbb P(x < X \leq x + \Delta x) \\
                                   &= F_X(x + \Delta x) - F(x) \,,
\end{align*}

si verifica facilmente che per ogni $x \in \mathbb R$ il valore $f_X(x)$
equivale al limite del rapporto incrementale di $F$ quando l'ampiezza del
relativo intervallo tende a zero, e quindi la funzione di densità di una
variabile aleatoria continua $X$ coincide con la derivata prima della sua
funzione di ripartizione.

````{prf:example}
Le funzioni di ripartizione e di densità della variabile aleatoria continua
$X$ introdotta nel paragrafo precedente sono definite rispettivamente nel
modo seguente:

```{math}
F_X(x) = x \mathrm I_{[0, 1]}(x) + \mathrm I_{(1, +\infty)}(x)
```

e

```{math}
f_X(x) = \mathrm I_{[0, 1]}(x) \,,
```

dunque si verifica facilmente che $F_X' =f_X$.

````

La funzione di ripartizione è quindi una primitiva della funzione di
densità, il teorema fondamentale del calcolo integrale [^tfci]
implica che per ogni $a, b \in \mathbb R$ tali che $a < b$ si ha

```{math}
\int_a^b f_X(x) \,\mathrm d x = F_X(b) - F_X(a) 
                              = \mathbb P(a \leq X \leq b) \,.
```

Considerando il limite per $b \rightarrow -\infty$ si ottiene, analogamente,
che $\mathbb P(X \leq x) = \int_{-\infty}^x f_X(x) \, \mathrm d x$. Più in
generale, dato un qualsiasi insieme $A$ esprimibile in termini di operazioni
fondamentali effettuate su intervalli, varrà dunque

```{math}
\mathrm P(X \in A) = \int_A f_X(x) \, \mathrm d x \,,
```

e quindi la probabilità $\mathbb P(X \in A)$ è interpretabile in termini
dell'area contenuta tra l'asse delle ascisse e il grafico della funzione di
densità di $X$ ristretta all'insieme $A$, come esemplificato in
{numref}`venn-symm-difference`.

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

import matplotlib.pyplot as plt
import numpy as np

from myst_nb import glue

plt.rcParams.update({
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

def pdf(x):
    return 1.2 * np.exp(-.1*(x)**2) + np.exp(-(x-3)**2)

fig, ax = plt.subplots()
x = np.linspace(-2, 5, 500)
y = pdf(x)

x_filled = np.linspace(1, 3, 500)
y_filled = pdf(x_filled)

ax.fill_between(x_filled, y_filled, alpha=0.5)
ax.plot(x, y)

ax.text(2, -.2, r'$A$')
ax.text(2, 1, '$\\mathbb P(X \\in A)$')

ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)

plt.xticks([])
plt.yticks([])

glue("pdf-interpretation", fig, display=False)
```

```{glue:figure} pdf-interpretation
:figwidth: 100%
:name: fig:pdf-interpretation

Un diagramma di Venn per descrivere la differenza tra l'insieme $S$ e
l'insieme $T$.
```

Il concetto di valore atteso di una variabile aleatoria continua o di una
sua funzione si ottiene estendendo la {prf:ref}`def:valore-atteso-discreto`.

```{margin}
Anche in questo caso non 
```
````{prf:definition} Valore atteso di una variabile aleatoria continua
:label: def:valore-atteso-continuo

Il _valore atteso_ di una variabile aleatoria continua $X$ è definito come

```{math}
\mathbb E(X) = \int_{-\infty}^{+\infty} x f_X(x) \, \mathrm d x \,,
```

nel caso in cui l'integrale converga, e risulta indefinito altrimenti.
Analogamente, il valore atteso di una funzione misurabile $g$ applicata a
una variabile aleatoria continua $X$ è uguale a

```{math}
\mathbb E(g(X)) = \int_{-\infty}^{+\infty} g(x) f_X(x) \, \mathrm d x
```

quando l'integrale converge ed è indefinito negli altri casi.
````



[^tfci]: Per la precisione, la versione del teorema fondamentale del calcolo
integrale che viene considerata in questo caso è formulabile nel modo che
segue: se $f_X$ è una funzione integrabile e ammette come primitiva una
funzione _assolutamente continua_ $F_X$ è, allora
$\int_a^b f_X(x) \,\mathrm dx = F_X(b) - F_X(a)$. Va sottolineato che,
nonostante l'ipotesi di assoluta continuità sia più restrittiva di quella di
continuità semplice che stiamo considerando, non ci addentreremo nel suo
approfondimento per evitare di complicare la trattazione. Rimarchiamo in ogni
caso che tutte le distribuzioni che considereremo soddisfano l'ipotesi di
assoluta continuità, rimandando a {cite}`mcdonald-2013` per una trattazione
rigorosa dei concetti collegati.

