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
:tags: [thebe-init, hide-input]

import ipywidgets as widgets

button = widgets.Button(
    description='Click me',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check' # (FontAwesome names without the `fa-` prefix)
)

def displ(e):
    print(e)

button.on_click(displ)

slider = widgets.IntSlider(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)
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

```{code-cell} ipython3
:tags: [hide-input, thebe-init]

import ipywidgets as widgets

button = widgets.Button(
    description='Click me',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check' # (FontAwesome names without the `fa-` prefix)
)

def displ(e):
    print("prova")

button.on_click(displ)

button
```

```{code-cell} ipython3
slider
```

```{code-cell} ipython3
:tags: [thebe-init, hide-input]

my_hidden_variable = 'wow, it worked!'
```

```{code-cell} ipython3
print(my_hidden_variable)
```

```{code-cell} ipython3

```
