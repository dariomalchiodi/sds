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


# Variabili aleatorie

````{prf:definition} Variabile aleatoria
:label: def:variabile-aleatoria
Una _variabile aleatoria_ ...
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
```
