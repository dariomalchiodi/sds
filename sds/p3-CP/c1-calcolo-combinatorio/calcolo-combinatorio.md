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

# Calcolo combinatorio

Il _calcolo combinatorio_ è una branca della matematica che descrive come
contare il numero di raggruppamenti di elementi scelti all'interno di un
insieme finito. Le formule che descrivono i numeri di raggruppamenti possibili
non dipendono dalla particolare natura degli elementi, che possono essere sia
tangibili (come abiti, frutti o biciclette), sia intangibili (come supereroi,
scelte delle abilità di un personaggio creato all'inizio di un video gioco
oppure software da installare su un computer). Invece è necessario tenere in
considerazione i seguenti aspetti.

- Gli elementi sono tutti diversi tra loro oppure ve ne sono alcuni che
  risultano _indistinguibili_?
- È possibile inserire in un raggruppamento un elemento che è gia stato scelto?
- Il raggruppamento dipende oppure no dall'ordine in cui si elencano gli
  elementi che lo compongono?

Una volta data risposta a queste domande, il numero di raggruppamenti
dipende solamente da pochi parametri. Nella maggior parte dei casi che vedremo
ne basteranno due: il numero $n$ di elementi che si possono scegliere e la
lunghezza $k$ del raggruppamento, intesa come numero totale di elementi che
questo contiene. Normalmente si utilizza la metafora secondo cui gli $n$
elementi sono degli _oggetti_ (indipendentemente dalla loro effettiva
tangibilità) da inserire in $k$ _posti_. Nei paragrafi che seguono vedremo
quali sono le principali modalità che si possono seguire per effettuare questi
"inserimenti" ottenendo i vari tipi di raggruppamenti, e deriveremo le
corrispondenti formule per contare quanti siano i possibili raggruppamento di
ogni tipo.
