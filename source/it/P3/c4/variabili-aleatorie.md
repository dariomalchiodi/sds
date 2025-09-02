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

(sec:variabili-aleatorie)=
# Variabili aleatorie

````{prf:definition} Variabile aleatoria
:label: def:variabile-aleatoria
Fissato uno spazio di probabilità $(\Omega, \mathsf A, \mathbb P)$, una
_variabile aleatoria_ è definita come una funzione $X: \Omega \rightarrow
\mathbb R$ tale che, per ogni $a \in \mathbb R$, l'evento
```{math}
X^{-1}((-\infty, a]) = \{ w \in \Omega \text{ tale che } X(\omega) \leq a \}
```
è contenuto in $\mathsf A$.
````

````{prf:definition} Dominio di una variabile aleatoria
:label: def:dominio
Il dominio di una variabile aleatoria $X$ è l'insieme delle specificazioni che
quest'ultima può assumere, e viene normalmente indicato usando il simbolo
$D_X$.
````

La probabilità che una variabile aleatoria $X$ assuma valori in un intervallo
è direttamente legata alla funzione di distribuzione cumulativa di
quest'ultima:

```{math}
:label: eq:cdf-e-intervalli

\mathbb P(a < X \leq b) = F_X(b) - F_X(a).
```

````{prf:theorem} Proprietà delle funzioni di distribuzione cumulativa
:label: teo:proprieta-F

Data una qualsiasi variabile aleatoria discreta $X$, la sua funzione di
distribuzione cumulativa $F_X$ soddisfa le tre seguenti proprietà:

1. $F_X$ è monotona non decrescente;
2. $F_X$ è continua da destra;
3. $\lim_{x \to +\infty} F_X(x) = 1$.

Viceversa, se una qualsiasi funzione $F: \mathbb R \to [0, 1]$ soddisfa le tre
proprietà precedenti, allora esiste una variabile aleatoria $X$ di cui $F$
rappresenta la funzione di distribuzione cumulativa.
````
