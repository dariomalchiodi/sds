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

(sec:importare-moduli)=
# Importare moduli

Il meccanismo con cui in python si organizzano progetti software complessi e si
riutilizza il codice è basato sul concetto di _modulo_. In pratica un modulo è
un file che contiene la definizione di una o più funzioni o classi.
L'importazione può riguardare un intero modulo oppure solo uno (o più) dei suoi
elementi. Tramite i moduli è inoltre possibile utilizzare librerie standard o
sviluppate da terze parti. Consideriamo per esempio la funzione
`get_sorted_counts` che abbiamo appena scritto: se esistesse un dizionario in
cui le chiavi inesistenti venissero automaticamente associate a un valore
nullo, si potrebbe semplificare notevolmente il corpo della funzione, rendendo
corretto il primo tentativo di implementazione che avevamo fatto. In effetti,
una tale variante di dizionario esiste: si chiama `defaultdict` ed è
disponibile nel modulo `collections` (uno dei moduli standard di python). La
cella seguente importa questo nuovo tipo di dato:

```python
from collections import defaultdict
```

e lo mette a disposizione: l'espressione `defaultdict(<tipo>)` crea un
dizionario vuoto e il tipo indicato come argomento determina quale sarà il
valore predefinito per le chiavi. Nel nostro caso, l'argomento `int` fa sì che
tale valore predefinito sia `0`. Ciò permette di riscrivere la funzione
`get_sorted_counts` in modo che non sia più necessario verificare
preventivamente l'esistenza dei contatori.

```python
def get_sorted_counts(sequence):
    counts = defaultdict(int)

    for x in sequence:
        counts[x] += 1

    pairs = counts.items()
    return sorted(pairs, key=lambda p:p[1], reverse=True)
```

Quando è necessario importare molti elementi da uno o più moduli, potrebbe
capitare che due o più elementi in moduli diversi abbiano lo stesso nome. Per
evitare situazioni di questo genere, è opportuno importare un intero modulo:
per esempio, l'istruzione

```python
import numpy
```

importa il modulo corrispondente alla libreria [numpy](http://www.numpy.org),
che mette a disposizione una struttura dati simile agli array (in cui
  l'omogeneità dei dati ivi contenuti permette di effettuare calcoli in modo
  più efficiente rispetto all'uso delle liste o delle tuple). Dopo che un
  modulo è stato importato, è possibile accedere a un suo generico elemento
  usando il nome del modulo, seguito da un punto e dal nome dell'elemento in
  questione. Per esempio, la cella successiva calcola il cosiddetto _argmax_
  della lista `index` (dopo averla modificata eliminando i valori `None` in
    essa presenti), e cioè l'indice in cui si trova un suo elemento massimo.

```python
years = [1941, 1962, None, None, 1941,
         1964, None, 1940, 1941, 1961,
         None, 1963, None, 1963, 1981,
         None, None, 1962, 1979]

years = [y for y in years if y]
numpy.argmax(years)
```

Indicare il nome di un modulo per poter accedere ai suoi elementi ha spesso
l'effetto di allungare il codice, diminuendone al contempo la leggibilità. È
per questo motivo che è possibile importare un modulo specificando un nome
alternativo, più corto. È quello che succede nella seguente cella, che importa
`numpy` e [pandas](http://pandas.pydata.org), un modulo che mette a
disposizione delle classi per gestire i dati organizzandoli in serie e in
tabelle.

```python
import numpy as np
import pandas as pd
```

```{admonition} Nomenclatura
:class: naming
Questo modo di importare numpy e pandas usando i nomi alternativi `np` e `pd`
fa riferimento a una convenzione molto diffusa tra gli sviluppatori. Vale la
pena mantenre questa convenzione, così che chi legge il codice possa capire a
colpo d'occhio a quale modulo si fa riferimento.
```

I moduli più complessi sono organizzati in strutture gerarchiche chiamate
_package_, in modo non dissimile a quanto avviene per esempio in Java. La
seguente cella importa il modulo `pyplot` che è contenuto nel modulo
`matplotlib` ([matplotlib](http://matplotlib.org) è la libreria di riferimento
in python per la creazione di grafici).

```python
import matplotlib.pyplot as plt
```
