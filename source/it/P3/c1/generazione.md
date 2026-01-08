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

(sec_generazione-combinatoria)=
# Generazione di disposizioni, permutazioni e combinazioni

In Python è abbastanza facile generare tutte le possibili disposizioni con
ripetizione degli elementi in una lista in $k$ posti: basta eseguire una list
comprehension per ottenere una lista i cui elementi sono $k$-ple, e gli
elementi di queste $k$-ple si ottengono iterando $k$ volte sulla lista di
partenza. Per esempio la cella seguente permette di generare tutte le
$D'_{3, 2} = 9$ coppie con ripetizione a partire da una lista di tre elementi

```{code-cell} python
l = range(3)

disp_rep = [(l1, l2) for l1 in l for l2 in l]
disp_rep
```

Le disposizioni senza ripetizione si ottengono facilmente a partire da quelle
con ripetizione: è sufficiente effettuare un'ulteriore list comprehension che
ha il solo scopo di eliminare tutte le disposizioni che contengono uno stesso
elemento più volte. Tale controllo si può effettuare verificando che
l'insieme ottenuto a partire da una disposizione abbia lo stesso numero di
elementi della disposizione stessa. Nella cella seguente utilizziamo questa
tecnica per ottenere tutte le $D_{3, 2} = 6$ coppie senza ripetizione a
partire dalla stessa lista precedentemente considerata.

```{code-cell} python
l = range(3)

disp_rep = [(l1, l2) for l1 in l for l2 in l]
disp_norep = [d for d in disp_rep if len(d)==len(set(d))]
disp_norep
```

Le permutazioni rappresentano un caso particolare delle disposizioni senza
ripetizione, in cui il numero di posti è uguale al numero di oggetti.
Pertanto si può adattare facilmente il codice della cella precedente per
generare, per esempio, tutte le $P_3 = 6$ permutazioni della lista
considerata.

```{code-cell} python
l = range(3)

disp_rep = [(l1, l2, l3) for l1 in l for l2 in l for l3 in l]
perm = [d for d in disp_rep if len(d)==len(set(d))]
perm
```

La generazione di combinazioni è più complicata: si procede nello stesso modo
visto per le disposizioni senza ripetizione, ma la seconda list comprehension
non si limita a filtrare le coppie, bensì le trasforma anche in insiemi
(tecnicamente, in istanze di `frozenset` che corrispondono a insiemi
  immutabili). Il risultato conterrà dei doppioni: per esempio le
  disposizioni $(a, b)$ e $(b, a)$ verrebbero trasformate nello stesso
  insieme. Per eliminare questi doppioni è sufficiente inserire tutti i
  risultati in un nuovo insieme. Già che ci siamo, possiamo trasformare tutti
  i `frozenset` ottenuti in normali insiemi, come nella cella seguente dove
  vengono costruite tutte le $C_{4, 2} = 6$ combinazioni di quattro elementi
  in due posti.

```{code-cell} python
l = range(4)

disp_rep = [(l1, l2) for l1 in l for l2 in l]
comb = [frozenset(d) for d in disp_rep if len(d)==len(set(d))]
list(map(set, set(comb)))
```

```{admonition} Nomenclatura
:class: naming
L'uso di `frozenset` nella cella precedente è fondamentale per poter eseguire
l'ultima istruzione. Gli elementi che si inseriscono in un insieme (ma lo
stesso varrebbe per le chiavi di un dizionario) devono essere infatti
immutabili: ciò è legato agli algoritmi che vengono utilizzati per inserire
gli elementi di un insieme in un'opportuna struttura dati che permetta di
verificare successivamente se un generico elemento appartiene oppure no
all'insieme.
```

Le generazioni di disposizioni, combinazioni e permutazioni fatte finora
richiedono di fissare il numero di posti: non sarebbe altrimenti possibile
scrivere le list comprehension alla base della costruzione delle
disposizioni, che rappresentano il mattone fondamentale per ottenere tutti
gli altri oggetti. Il modulo `itertools` contiene funzioni che permettono di
superare questo ostacolo. Nella fattispecie:

- `product` permette di generare le disposizioni con ripetizione,
  specificando la lista dei valori come primo elemento e il numero di posti
  tramite l'argomento opzionale `repeat`:

```{code-cell} python
import itertools
list(itertools.product(range(3), repeat=2))
```

- `permutations` genera le disposizioni senza ripetizioni e le permutazioni:

```{code-cell} python
list(itertools.permutations(range(3), 2))
```

```{code-cell} python
list(itertools.permutations(range(3), 3))
```

- `combinations` genera infine le combinazioni:

```{code-cell} python
list(itertools.combinations(range(4), 2))
```

```{admonition} Nomenclatura
:class: naming
Le funzioni di `itertools` che abbiamo considerato non restituiscono delle
liste, bensì degli speciali oggetti che è necessario convertire
esplicitamente in liste utilizzando la funzione `list`.
```
