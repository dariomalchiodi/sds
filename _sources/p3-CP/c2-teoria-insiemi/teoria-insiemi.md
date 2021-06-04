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
:tags: [remove-cell]

%matplotlib inline
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib_venn import venn2_circles, venn2
from myst_nb import glue

import matplotlib
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
matplotlib.rcParams['mathtext.fontset'] = 'cm'
font_size = 18
matplotlib.rcParams['font.size'] = str(font_size)

venn_set_color = '#cc0000'
venn_set_edge= '#333333'
```

# Teoria degli insiemi

Nel 1895 Georg Cantor ha proposto una definizione che coglie particolarmente bene il concetto intuitivo di insieme {cite}`cantor-1883`: "per molteplicità o insieme intendo ogni molti che si può pensare come uno" [^citazione-cantor]. Secondo questa definizione, un insieme è essenzialmente un raggruppamento di oggetti che, sebbene tra loro distinti, sono accomunati da una qualche proprietà. Nel 1895 lo stesso Cantor riformulò la sua definizione come segue: "per 'insieme' intendiamo qualsiasi combinazione $M$ di certi oggetti $m$ ben differenziati nella nostra visione o del nostro pensiero (che sono detti 'elementi' di $M$)" {cite}`cantor-1895`. Pochi anni dopo i matematici hanno scoperto che fornire una definizione formalmente corretta di insieme richede molta più attenzione, tipicamente appoggiandosi a un approccio assiomatico {cite}`suppes`. Nonostante ciò, nel seguito faremo riferimento alle definizioni sopra indicate, e in particolare alla seconda, al fine di rendere la trattazione più semplice e più focalizzata rispetto allo scopo di questo libro. D'altronde, come ricorda Rudy Rucker, è significativo che la parola _set_ abbia la definizione più lunga tra tutte le parole che compaiono nello Oxford English Dictionary {cite}`rucker`.
