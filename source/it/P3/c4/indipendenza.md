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

(sec_indipendenza-va)=
# Indipendenza di variabili aleatorie


L'ultimo risultato riguarda le somme di variabili aleatorie indipendenti, ed è
il motivo principale per cui la funzione generatrice dei momenti è uno
strumento tanto usato: trasforma una somma di variabili aleatorie in un
prodotto di funzioni.

````{prf:theorem}
:label: teo-mgf-method

Siano date $n$ variabili aleatorie $X_1, \dots, X_n$ tra loro indipendenti e
ciascuna avente la stessa distribuzione di una variabile aleatoria $X$, della
quale $m_X$ indica la funzione generatrice dei momenti. Posto
$Y \triangleq \sum_{i=1}^n X_i$, si ha

```{math}
m_Y(t) = \left( m_X(t) \right)^n \enspace.
```
````
````{sds-proof}
La funzione generatrice dei momenti di $Y$ è tale che

```{math}
m_Y(t) = \mathbb E\left( \mathrm e^{tY} \right)
       = \mathbb E\left( \mathrm e^{t\sum_{i=1}^n X_i} \right)
       = \mathbb E\left( \prod_{i=1}^n \mathrm e^{t X_i} \right)
       = \prod_{i=1}^n \mathbb E\left( \mathrm e^{t X_i} \right)
       = \prod_{i=1}^n m_X(t)
       = \left( m_X(t) \right)^n \enspace,
```

dove il terzultimo passaggio è giustificato dall'indipendenza di
$X_1, \dots, X_n$.
````

Nell'{prf:ref}`ex-mom-multiple-man` avevamo già osservato una funzione
generatrice della forma $\left( m_X(t) \right)^n$: il numero di duplicati
riusciti è infatti la somma di due variabili indipendenti, ciascuna delle quali
vale $1$ o $0$ a seconda che il singolo tentativo riesca oppure no. Nel
prossimo capitolo useremo ripetutamente questo teorema per ricavare la
distribuzione di somme di variabili aleatorie con la stessa distribuzione.