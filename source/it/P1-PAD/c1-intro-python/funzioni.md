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

(sec:funzioni)=
# Funzioni

Il calcolo delle frequenze è un'operazione che viene fatta molto spesso, quindi
conviene scrivere una funzione che ci eviti di dover ricopiare ogni volta la
decina di linee che abbiamo scritto (in realtà è solo una scusa per vedere come
si definiscono le funzioni in python: più avanti vedremo come usare delle
librerie per calcolare le frequenze). La definizione di una funzione in python
(a parte il caso delle funzioni anonime) viene fatta utilizzando la parola
chiave `def` seguita dal nome del metodo e dai nomi simbolici per i suoi
argomenti, separati da virgole e racchiusi tra parentesi (fanno eccezione gli
eventuali argomenti opzionali, ma di questo non parleremo). La definizione
procede con un carattere di due punti e dal corpo della funzione le cui
istruzioni devono essere indentate di un livello.

La cella seguente riporta un esempio di semplice definizione di funzione che
mette insieme il codice scritto finora in modo da accettare una generica lista
e di restituirne le frequenze assolute ordinate dalla più grande alla più
piccola.

```python
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

## Parametri opzionali

(sec:funzioni-anonime)=
## Funzioni anonime

Un'altra caratteristica di python è quella di poter specificare una funzione
come argomento di un metodo (o di un'altra funzione); ciò si può fare o
indicando il nome della funzione, oppure usando una _lambda function_ o
_funzione anonima_: una funzione che viene definita senza darle un nome ma
definendo direttamente come i suoi argomenti devono essere trasformati nel
valore da restituire. Più precisamente, la sintassi `lambda x: <espressione>`
definisce una funzione che ha un argomento il cui nome simbolico è `x` e che
restituisce l'espressione dopo il carattere di due punti (che di norma
dipenderà da `x`).

Un esempio che mette insieme l'uso di argomenti opzionali e di funzioni anonime
si trova nella cella seguente, in cui la lista dei nomi viene ordinata non in
modo alfabetico, bensì in funzione della lunghezza dei nomi stessi,
specificando tramite l'argomento opzionale `key` una funzione anonima che
trasformerà ogni elemento della lista in un valore su cui basare l'ordinamento.
