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

```{code-cell} ipython3
:tags: [remove-input]

import altair as alt
import pandas as pd
import numpy as np

heroes = pd.read_csv('data/heroes.csv', index_col=0)
filter = (heroes['universe'].isin(heroes.universe.value_counts()[:10].index))
filter &= (heroes['weight']<600)
filter &= (heroes['height']<400)
source = heroes[filter]
brush = alt.selection_interval(encodings=['x'])
points = alt.Chart(source).mark_point().encode(
    x='height:Q',
    y='weight:Q',
    size='strength',
    color=alt.condition(brush, 'universe:N', alt.value('lightgray'))
).add_params(brush)

bars = alt.Chart(source).mark_bar().encode(
    y='count(universe)',
    color='universe',
    x='universe'
).transform_filter(brush)

points & bars
```

# Un esempio

Facciamo finta che...

+++

Nei nostri esperimento faremo riferimento a un _dataset_ ottenuto modificando
un opportuno sottoinsieme del [Superhero database](http://www.superherodb.com).
Gli esempi faranno quindi riferimento al mondo dei supereroi, ognuno dei quali
sarà descritto tramite:

- il suo nome,
- la sua identità,
- il luogo in cui è nato,
- l'editore dei corrispondenti fumetti/film/serie tv,
- l'altezza in cm.,
- il peso in kg.,
- il genere,
- l'anno della prima apparizione,
- il colore degli occhi,
- il colore dei capelli,
- un indice di forza (in una scala quantitativa da 0 a 100),
- un indice di intelligenza (in una scala qualitativa i cui valori sono _low_,
  _moderate_, _average_, _good_, e _high_).


