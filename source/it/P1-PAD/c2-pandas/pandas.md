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

(chap_pandas)=
# Pandas

Vedremo come la libreria pandas faciliti le operazioni viste finora per
caricare dati, organizzarli in opportune strutture e analizzarli. Per poter
procedere dobbiamo ricaricare le librerie usate finora, nonché il file
`heroes.csv`.

```{code-cell} python
import pandas as pd
```

Va notato come pandas (così come, in generale, gran parte del software open
source dedicato all'analisi dei dati) sia caratterizzato da una comunità di
sviluppatori molto attiva. Ciò significa che il tempo tra il rilascio di due
release successive sia di norma breve: se avete effettuato l'installazione in
modo autonomo è quindi possibile che stiate utilizzando una versione più (o
meno) recente di quella più aggiornata quando è stato scritto questo documento.
Per verificare quale sia la versione installata è sufficiente accedere alla
proprietà `pd.__version__`:

```{code-cell} python
pd.__version__
```

Utilizzando una versione diversa da questa, può capitare che il risultato
ottenuto eseguendo alcune celle sia diverso da quello indicato. Alcune
funzionalità potrebbero anche non essere implementate, deprecate o perfino
rimosse. Se state invece utilizzando l'ambiente fornito tramite immagine Docker
o tramite mybinder non dovreste avere problemi di questo genere.