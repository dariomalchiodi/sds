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

(sec:modello-bernoulliano)=
# Il modello bernoulliano

 Tenuto conto del fatto che un esperimento bernoulliano di
parametro $p$ si può simulare estraendo un numero pseudocasuale uniformemente
distribuito in $[0, 1]$ (compito effettuato per esempio dalla funzione `random`
nel modulo omonimo) e decretando un successo se il risultato è inferiore a
$p$ e un fallimento altrimenti

