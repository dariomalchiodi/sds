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

(sec:disposizioni)=
# Disposizioni

Per disposizione di $n$ oggetti distinti in $k$ posti si intende una qualsiasi
sequenza ordinata di $k$ simboli, ognuno rappresentante uno degli oggetti.
Pertanto il tipo di raggruppamento che corrisponde alle disposizioni dipende
dall'ordine utilizzato e gli oggetti sono tra loro distinguibili. In funzione
del fatto che in una stessa sequenza vi possano essere due o più simboli che
si riferiscono a un medesimo oggetto oppure no, ha senso parlare di due
diverse categorie di disposizioni, a cui ci riferisce rispettivamente
chiamandole disposizioni con e senza ripetizione.

## Disposizioni con ripetizione

Nelle disposizioni con ripetizione è possibile utilizzare uno stesso oggetto
più di una volta, come specificato dalla definizione che segue.

```{margin}
In questo caso il significato di _ripetizione_ è diverso da quello visto per
le permutazioni, nelle quali siamo obbligati a ripetere ogni oggetto
esattamente tante volte quanto questo occorre nel multiiniseme di partenza;
nelle disposizioni possiamo invece ripetere uno stesso oggetto quante volte
vogliamo.
```
```{prf:definition} Disposizione con ripetizione
:label: def-disposizioni-con-ripetizione
Consideriamo un insieme di $n$ oggetti $A = \{ a_1,\dots a_n \}$. Fissato un
numero $k \in \mathbb N$, una _disposizione con ripetizione_ di questi oggetti
in $k$ posti è una sequenza ordinata di $k$ elementi distinti appartenenti ad
$A$. Indicheremo con il simbolo $D_{n, k}$ il numero di differenti
disposizioni con ripetizione di $n$ oggetti in $k$ posti.
```

Indicheremo le disposizioni usando la stessa sintassi delle permutazioni.

```{prf:example} un esempio di disposizione con ripetizione
:label: ex-disposizioni-con-ripetizione
TODO
Ad esempio, fissato
$k=3$, la disposizione $(a_i, a_j, a_r)$ è diversa dalla disposizione
$(a_r, a_j, a_i)$ perché, sebbene gli oggetti selezionati siano gli stessi,
essi compaiono in ordine differente.

Ad esempio, fissato $k=3$,
la sequenza $(a_r, a_i, a_i)$ è una disposizione con ripetizione perché
l'oggetto $a_i$ ricorre due volte, e analogamente  $\{a_r, a_i, a_i\}$ è
una combinazione con ripetizione.
```

Calcolare il numero $D_{n, k}$ di possibili disposizioni con ripetizione
è abbastanza facile, considerando il numero di scelte possibili per ognuno dei
$k$ posti:
- per selezionare l'oggetto da inserire nel primo posto abbiamo $n$ scelte
  a disposizione;
- il numero di scelte continua a essere uguale a $n$ anche per il secondo
  posto, tenuto conto del fatto che è eventualmente possibile riutilizzare
  l'oggetto scelto per la prima posizione;
- chiaramente, vi saranno $n$ scelte possibili per tutti i rimanenti posti.

Applicando il principio fondamentale del calcolo combinatorio si ottiene
pertanto che

$$
D_{n, k} = \underbrace{n \cdot n \dots \cdot n}_{k \text{ volte}} = n^k \enspace.
$$



## Disposizioni senza ripetizione

Nelle disposizioni con ripetizione ogni oggetto può essere scelto un
numero illimitato di volte per formare una sequenza. Quando invece la
scelta di un oggetto può essere fatta al massimo per una volta, si parla
di _disposizioni senza ripetizione_, dette anche _disposizioni semplici_.
In questo caso è pertanto richiesto che $k \leq n$, perché dopo che tutti
gli $n$ oggetti sono stati inseriti in una sequenza non ve ne sono altri
che possono essere scelti ulteriormente.

```{prf:definition} Disposizione semplice
:label: def-disposizioni-semplici
Consideriamo un insieme $A \{ a_1, \ldots, a_n \}$ di $n$ oggetti. Fissato
un numero intero $k \leq n$, una _disposizione semplice_ (detta anche
_disposizione senza ripetizione_) è una sequenza di $k$ degli oggetti di $A$
nella quale non occorrono ripetizioni. Indicheremo con il simbolo $d_{n, k}$
il numero di differenti disposizioni semplici di $n$ oggetti in $k$ posti.
```

```{margin}
Si osservi che, per $k=n$, nella disposizione si utilizzano tutti gli
elementi di $A$, quindi le permutazioni semplici sono un caso particolare
di disposizioni semplici.
```
La sintassi che useremo per indicare le disposizioni semplici è la stessa
utilizzata per quelle con ripetizione, e dunque è identica a quella utilizzata
per le permutazioni.

````{prf:example}
:label: ex:disposizioni-semplici
TODO Esempio sulle disposizioni semplici
````

```{margin}
Notate che $d_{n, n} = n!/0! = n! = p_n$, in coerenza con la nota precedente.
``` 
Per calcolare $d_{n, k}$ possiamo seguire lo stesso ragionamento fatto per le
permutazioni semplici, fermandoci però dopo avere scelto $k$ oggetti.
Applicando il principio fondamentale del calcolo combinatorio si ottiene che

```{math}
d_{n, k} = n (n-1) \ldots (n-k+1) =
n (n-1) \ldots (n-k+1) \cdot \frac{(n-k)!}{(n-k)!} =
\frac{n!}{(n-k)!} \enspace.
```