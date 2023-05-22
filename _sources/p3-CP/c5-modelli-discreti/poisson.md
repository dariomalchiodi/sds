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

# Le distribuzioni di Poisson

Immaginiamo di rieseguire il codice del {numref}`sec:binomial-quantiles`
per il calcolo dei quantili di una distribuzione binomiale nella quale il
parametro $n$ assume un valore elevato, diciamo dell'ordine delle decine di
migliaia. In quel codice, una delle prime operazioni consiste nel calcolare
$(1 - p)^n$, e per valori così alti dell'esponente, indipendentemente dalla
base che consideriamo, è ragionevole che il valore della potenza venga
memorizzato come $0$, tenendo conto della precisione dei numeri in virgola
mobile. Analoghe considerazioni valgono per esempio per il calcolo della
funzione di massa di probabilità. In casi come questi, è possibile introdurre
una nuova famiglia di distribuzioni che rappresenta il risultato della
convergenza 
