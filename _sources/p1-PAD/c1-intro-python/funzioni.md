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

# Funzioni
Il calcolo delle frequenze è un'operazione che viene fatta molto spesso, quindi conviene scrivere una funzione che ci eviti di dover ricopiare ogni volta la decina di linee che abbiamo scritto (in realtà è solo una scusa per vedere come si definiscono le funzioni in python: più avanti vedremo come usare delle librerie per calcolare le frequenze). La definizione di una funzione in python (a parte il caso delle funzioni anonime) viene fatta utilizzando la parola chiave `def` seguita dal nome del metodo e dai nomi simbolici per i suoi argomenti, separati da virgole e racchiusi tra parentesi (fanno eccezione gli eventuali argomenti opzionali, ma di questo non parleremo). La definizione procede con un carattere di due punti e dal corpo della funzione le cui istruzioni devono essere indentate di un livello.

La cella seguente riporta un esempio di semplice definizione di funzione che mette insieme il codice scritto finora in modo da accettare una generica lista e di restituirne le frequenze assolute ordinate dalla più grande alla più piccola.

```{code-cell} ipython3
def get_sorted_counts(sequence):
    counts = {}

    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    pairs = counts.items()
    return sorted(pairs, key=lambda p:p[1], reverse=True)

years = [1941, 1962, None, None, 1941,
         1964, None, 1940, 1941, 1961,
         None, 1963, None, 1963, 1981,
         None, None, 1962, 1979]

get_sorted_counts(years)
```
