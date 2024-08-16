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

(sec:esempio-interattivo)=
# Un esempio interattivo

Come indicato nel Paragrafo @sec:approccio, nel testo farò riferimento a un
_dataset_ ottenuto modificando un opportuno sottoinsieme del
[Superhero database](http://www.superherodb.com). Gli esempi faranno quindi
riferimento al mondo dei supereroi, ognuno dei quali sarà descritto tramite
i dati indicati nella {numref}`tab:dataset`.

```{table} Descrizione del _dataset_ utilizzato negli esempi
:name: tab:dataset
:align: center
| Attributo        | Significato               | Contenuto                                                |
|------------------|---------------------------|----------------------------------------------------------|
| name             | Nome (univoco)            | stringa                                                  |
| full_name        | Nome completo             | stringa                                                  |
| identity         | Identità segreta          | stringa                                                  |
| alignment        | Inclinazione morale       | `'Good'`, `'Neutral'` o `'Bad'`                          |
| place_of_birth   | Luogo di nascita          | stringa                                                  |
| creator          | Editore/creatore          | stringa                                                  |
| universe         | Universo                  | stringa                                                  |
| first_appearance | Anno di prima apparizione | stringa                                                  |
| eye_color        | Colore degli occhi        | stringa                                                  |
| hair_color       | Colore dei capelli        | stringa                                                  |
| height           | Altezza in cm.            | intero                                                   |
| weight           | Peso  in kg.              | intero                                                   |
| strength         | Forza                     | intero, da `0` a `100`                                   |
| intelligence     | Intelligenza              | `'Low'`, `'Moderate'`, `'Average'`, `'Good'`, o `'High'` |
| speed            | Velocità                  | intero                                                   |
| durability       | Resistenza                | intero                                                   |
| combat           | Abilità nel combattimento | intero                                                   |
| powers           | Elenco dei superpoteri    | stringa                                                  |
```
```{margin}
Ho scelto di utilizzare la lingua inglese per indicare i nomi degli attributi
e i valori corrispondenti (quando questi sono descritti tramite stringhe),
per coerenza rispetto ai contenuti del dataset. Analogamente, il codice Python
sarà strutturato utilizzando nomi in inglese per variabili, funzioni e così via.
```

Il _dataset_ è memorizzato nel file `heroes.csv` contenuto nella directory
`data` del repository associato al libro. In questo file, i contenuti sono
rappresentati utilizzando il formato CSV (_comma separated values_): ogni
riga rappresenta un supereroe, in cui i valori degli attributi nella
{numref}`tab:dataset` sono indicati separandoli tramite virgole. L'unica
eccezione è costituita dalla prima riga del file, che contiene i nomi degli
attributi, sempre separati usando le virgole, come si può vedere visualizzando
la parte iniziale dei suoi contenuti.
```{margin}
Il formato CSV è uno standard altamente utilizzato per condividere dati
di dimensioni relativamente contenute.
```

```{code-cell} ipython3
!head data/heroes.csv
```

Nel Capitolo @cap:pandas vedremo come caricare in memoria i contenuti di
questo file e, soprattutto, come elaborarli. Per ora, concentriamoci su
due semplici esempi che, da una parte, mostrano come utilizzare le parti
interattive del libro, e, dall'altra, danno un'anteprima di alcuni concetti
spiegati nel seguito.

````{figure}
:name: fig:first-example

```{code-cell} ipython3
:tags: [remove-input]

import altair as alt
import pandas as pd
import numpy as np

heroes = pd.read_csv('data/heroes.csv', index_col=0).convert_dtypes()
filter = (heroes['creator'].isin(heroes.creator.value_counts()[:15].index))
filter &= (heroes['weight']<200)
filter &= (heroes['height']<250)
source = heroes[filter]
source = heroes[filter]
brush = alt.selection_interval()
points = alt.Chart(source).mark_point().encode(
    x='weight',
    y='height',
    size='strength',
    color=alt.condition(brush, 'creator', alt.value('lightgray')),
    tooltip='name'
).add_params(brush)

bars = alt.Chart(source).mark_bar().encode(
    y='creator',
    x='count(creator)',
    color='creator',
).transform_filter(brush)

points & bars
```

Un esempio di grafico interattivo. Il diagramma superiore mostra alcuni
supereroi, ognuno indicato da un cerchio. Le coordinate del centro corrispondono
a peso e altezza, il raggio indica la forza e il colore rappresenta l'editore.
Il diagramma inferiore riassume il numero di supereroi per ogni differente
editore. Quando viene selezionata un'area rettangolare nel primo diagramma, il
secondo viene automaticamente aggiornato in modo da considerare solo i
supereroi selezionati. Per tornare al grafico originale è possibile cliccare
in un punto qualsiasi al di fuori dell'area selezionata.
````