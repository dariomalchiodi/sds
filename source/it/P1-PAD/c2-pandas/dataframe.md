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

(sec:dataframe)=
# Dataframe

Un _dataframe_ è una collezione di serie che hanno lo stesso indice, ed è
quindi un insieme di osservazioni di vari _caratteri_ per una popolazione di
individui. Tra i vari modi che sono disponibili in pandas per creare un
_dataframe_, noi faremo riferimento al metodo `read_csv` della classe
`pd.DataFrame`, che permette di leggere i contenuti di un file in formato CSV e
convertirli automaticamente in un _dataframe_.

```{code-block} python
import pandas as pd

heroes = (pd.read_csv('data/heroes.csv', index_col=0)
            .drop(columns=['powers', 'creator', 'universe', 'name',
                           'place_of_birth', 'full_name']))
```

Usando lo stesso file a cui abbiamo fatto riferimento nei paragrafi precedenti,
è stato necessario utilizzare l'argomento opzionale `sep` per indicare il
carattere usato per separare i campi in ogni record. La visualizzazione dei
dataframe viene automaticamente formattata in un formato tabellare facile da
leggere se si utilizza jupyter:

```{code-block} python
:class: full_width
heroes.head()
```

Ci riferiremo spesso alle righe e alle colonne di un _dataframe_ per indicare
rispettivamente le osservazioni e i caratteri. Per esempio la prima riga si
riferisce all'osservazione relativa ad "A-Bomb", mentre la prima colonna
corrisponde al carattere "identity". Vi sono molti modi per interagire con un
_dataframe_:

- l'insieme degli indici, dei caratteri e dei valori si ottengono, nell'ordine,
  alle proprietà `index`, `columns` e `values`;
- una serie corrispondente a una colonna/carattere può essere selezionata
  usando una sintassi simile a quella dei dizionari, specificando il nome del
  carattere come chiave:

```{code-block} python
heroes['eye_color']
```

```{admonition} Nomenclatura
:class: naming
In alternativa è possibile usare una sintassi basata su _dot notation_ in cui
il nome della colonna, senza essere racchiuso tra apici, segue il _dataframe_.
In altre parole, `heroes['Gender']` e `heroes.Gender` sono equivalenti. Questa
seconda notazione è però utilizzabile solamente se non vi sono spazi nei nomi
delle colonne. Nel seguito utilizzeremo quindi sempre la prima delle due
notazioni.
```

- tramite uno _slicing_ sulle posizioni o sui valori dell'indice è possibile
  selezionare un sottoinsieme delle righe del _dataframe_ (e come nel caso
  delle serie, l'estremo superiore è incluse se si usano gli indici ed escluso
  se si usano le posizioni):

```{code-block} python
:class: full-width
heroes['Agent 13':'Agent 711']
```

Queste modalità di accesso possono effettivamente creare confusione: usando una
sintassi molto simile, specificando un valore si accede a una colonna e
specificando uno _slice_ si accede a un insieme di righe. Per scrivere codice
più chiaro è meglio selezionare le righe utilizzando le proprietà `loc` e
`iloc` nello stesso modo in cui queste funzionano per le serie, con la
differenza che quando queste sono usate specificando un solo valore, viene
restituita una serie, e quando sono utilizzate con uno _slice_ o con una lista
viene restituito un _dataframe_.

```{code-block} python
heroes.loc['Professor X']
```

```{code-block} python
:class: full-width
heroes.iloc[42:46]
```

È inoltre possibile selezionare una o più righe e visualizzare solo un
sottoinsieme dei caratteri, passando a `loc` o `iloc` un secondo argomento in
cui si specificano i caratteri da mostrare, utilizzando anche in questo caso un
valore, una lista di valori oppure uno _slice_:

```{code-block} python
heroes.loc['Professor X', 'height':'weight']
```

Va notato che `loc` accetta solo valori simbolici, mentre `iloc` solamente
posizioni, e ciò riguarda anche il loro secondo argomento:

```{code-block} python
heroes.iloc[[106, 103], [3, 4]]
```

Volendo accedere direttamente a un elemento è possibile utilizzare le proprietà `at` e `iat`:

```{code-block} python
heroes.at['Superman', 'strength']
```

```{code-block} python
heroes.iat[500, -1]
```

```{admonition} Nomenclatura
:class: naming
È anche possibile utilizzare `loc` e `iloc` per estrarre un singolo elemento:
per esempio, `heroes.loc['Superman', 'strength']` equivale alla prima delle due
istruzioni appena elencate. Tuttavia, `at` e `iat` sono implementate in modo da
essere più efficienti.
```

È infine possibile riordinare le righe di un dataframe invocando i metodi
`sort_values` e `sort_index`: il primo basa l'ordinamento sul valore di una
colonna, il cui nome va specificato tramite l'argomento `by` e il secondo è
invece basato sui valori dell'indice. È inoltre possibile indicare un valore
booleano per l'argomento `ascending` che permette di ordinare in verso
crescente o decrescente.

```{code-block} python
:class: full-width
heroes.sort_values(by='weight', ascending=False)[:5]
```

```{code-block} python
:class: full-width
heroes.sort_index()[-5:]
```

Va notato che entrambi i metodi restituiscono una copia del _dataframe_. Anche
per i _dataframe_ è possibile utilizzare una lista di valori booleani che
identificano le righe da selezionare, e tale lista può essere prodotta
effettuando una query. In questo caso però le condizioni possono riguardare le
varie colonne, ognuna delle quali va specificata usando una delle due sintassi
precedentemente introdotte (quella analoga ai dizionari oppure quella basata
su _dot notation_). Per esempio possiamo selezionare gli eroi per cui l'anno
di apparizione esiste e rappresenta un valore non fuori scala nel modo seguente:

```{code-block} python
:class: full-width
heroes_with_year = heroes[heroes['first_appearance'] > 1900]
heroes_with_year.head()
```
