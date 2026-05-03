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

(sec_disposizioni)=
# Disposizioni

Per disposizione di $n$ oggetti distinti in $k$ posti si intende una qualsiasi
sequenza di $k$ simboli, ognuno rappresentante uno degli oggetti. Pertanto, il
tipo di raggruppamento che corrisponde alle disposizioni dipende dall'ordine
utilizzato, e gli oggetti devono essere tra loro distinguibili. Si parla di
disposizioni con ripetizione quando un simbolo può apparire più volte nella
sequenza, e di disposizioni semplici altrimenti.

## Disposizioni con ripetizione

Nelle disposizioni con ripetizione è possibile utilizzare uno stesso oggetto
più di una volta, come specificato dalla definizione che segue.

```{margin}
In questo caso il significato di _ripetizione_ è diverso da quello visto per
le permutazioni, nelle quali siamo obbligati a inserire ogni oggetto
esattamente tante volte quanto questo occorre nel multiinsieme di partenza;
nelle disposizioni possiamo invece ripetere uno stesso oggetto quante volte
vogliamo, o escluderlo completamente.
```
```{prf:definition} Disposizione con ripetizione
:label: def-disposizioni-con-ripetizione
Fissato un insieme di $n$ oggetti $A = \{ a_1,\dots a_n \}$ e un
numero $k \in \mathbb N$, una _disposizione con ripetizione_ è una sequenza
$(a_{i_1}, \dots, a_{i_k})$, dove per ogni $j = 1, \dots, k$ si ha
$i_j \in \{1, \dots, n\}$ e $a_{i_j} \in A$. Indichiamo con $D_{n, k}$ il
numero di possibili disposizioni con ripetizione di $n$ oggetti in $k$ posti.
```


```{prf:example} un esempio di disposizione con ripetizione
:label: ex-disposizioni-con-ripetizione-1

Il [Dipartimento H](https://marvel.fandom.com/wiki/Department_H_(Earth-616))
deve pianificare una sequenza di tre missioni giornaliere, rispettivamente la
mattina, il pomeriggio e la sera. Per ogni missione può essere inviato uno
qualsiasi dei quattro membri degli [Alpha
Flight](https://marvel.fandom.com/wiki/Alpha_Flight_(Earth-616)): Guardian,
Sasquatch, Northstar e Aurora, che indicheremo rispettivamente con le
iniziali $G$, $S$, $N$ e $A$. Se ogni membro può essere dispiegato in più
missioni nella stessa giornata, a ogni pianificazione corrisponde una
disposizione con ripetizione degli $n = 4$ oggetti nell'insieme
$\{G, S, N, A  \}$ (i membri della squadra) in $k = 3$ posti (i turni
giornalieri). Per esempio, le tre seguenti situazioni descrivono pianificazioni
(e disposizioni) differenti:
- $(G, S, N)$ indica che Guardian, Sasquatch e Northstar svolgono
  rispettivamente i turni mattutino, pomeridiano e serale;
- $(S, N, G)$, inverte i turni del mattino e del pomeriggio rispetto al
  punto precedente;
- $(A, G, G)$ coinvolge Aurora al mattino e Guardian nei due turni successivi.
```

Calcolare il numero $D_{n, k}$ di possibili disposizioni con ripetizione
è abbastanza facile, considerando il numero di scelte possibili per ognuno dei
$k$ posti:
- l'oggetto da inserire nel primo posto può essere scelto in $n$ modi diversi;
- il numero di scelte continua a essere uguale a $n$ anche per il secondo
  posto, dal momento che è possibile riutilizzare l'oggetto selezionato per la
  prima posizione;
- chiaramente, vi saranno $n$ scelte possibili per tutti i rimanenti posti.

Applicando il principio fondamentale del calcolo combinatorio si ottiene
pertanto che

$$
D_{n, k} = \underbrace{n \cdot n \dots \cdot n}_{k \text{ volte}} = n^k \enspace.
$$

Lo stesso risultato si ottiene notando che l'insieme di tutte le
disposizioni è il prodotto cartesiano $A^k$ di $A$ con se stesso, calcolato
$k$ volte, e ricordando che $| A^k | = |A|^k = n^k$.

```{prf:example} un esempio di disposizione con ripetizione
:label: ex-disposizioni-con-ripetizione-2

Riprendendo l’{prf:ref}`ex-disposizioni-con-ripetizione-1`, il numero totale di
pianificazioni giornaliere distinte è uguale a $D_{4,3} = 4^3 = 64$, come
evidenziato nella {numref}`tab-disposizioni-con-ripetizione`, dove le colonne
M, P ed S fanno riferimento ai turni del mattino, del pomeriggio e della sera,
rispettivamente.
```

````{table} Le possibili disposizioni con ripetizione di $4$ oggetti in $3$ posti che descrivono i turni degli Alpha Flight; le corrispondenti disposizioni semplici sono evidenziate in grassetto.
:name: tab-disposizioni-con-ripetizione
:align: center

|  # | M   | P   | S   |  # | M   | P   | S   |  # | M   | P   | S   |
|----|-----|-----|-----|----|-----|-----|-----|----|-----|-----|-----|
|  1 | $G$ | $G$ | $G$ |  2 | $G$ | $G$ | $S$ |  3 | $G$ | $G$ | $N$ |
|  4 | $G$ | $G$ | $A$ |  5 | $G$ | $S$ | $G$ |  6 | $G$ | $S$ | $S$ |
| **7** | $\boldsymbol{G}$ | $\boldsymbol{S}$ | $\boldsymbol{N}$ | **8** | $\boldsymbol{G}$ | $\boldsymbol{S}$ | $\boldsymbol{A}$ |  9 | $G$ | $N$ | $G$ |
| **10** | $\boldsymbol{G}$ | $\boldsymbol{N}$ | $\boldsymbol{S}$ | 11 | $G$ | $N$ | $N$ | **12** | $\boldsymbol{G}$ | $\boldsymbol{N}$ | $\boldsymbol{A}$ |
| 13 | $G$ | $A$ | $G$ | **14** | $\boldsymbol{G}$ | $\boldsymbol{A}$ | $\boldsymbol{S}$ | **15** | $\boldsymbol{G}$ | $\boldsymbol{A}$ | $\boldsymbol{N}$ |
| 16 | $G$ | $A$ | $A$ | 17 | $S$ | $G$ | $G$ | 18 | $S$ | $G$ | $S$ |
| **19** | $\boldsymbol{S}$ | $\boldsymbol{G}$ | $\boldsymbol{N}$ | **20** | $\boldsymbol{S}$ | $\boldsymbol{G}$ | $\boldsymbol{A}$ | 21 | $S$ | $S$ | $G$ |
| 22 | $S$ | $S$ | $S$ | 23 | $S$ | $S$ | $N$ | 24 | $S$ | $S$ | $A$ |
| **25** | $\boldsymbol{S}$ | $\boldsymbol{N}$ | $\boldsymbol{G}$ | 26 | $S$ | $N$ | $S$ | 27 | $S$ | $N$ | $N$ |
| **28** | $\boldsymbol{S}$ | $\boldsymbol{N}$ | $\boldsymbol{A}$ | **29** | $\boldsymbol{S}$ | $\boldsymbol{A}$ | $\boldsymbol{G}$ | 30 | $S$ | $A$ | $S$ |
| **31** | $\boldsymbol{S}$ | $\boldsymbol{A}$ | $\boldsymbol{N}$ | 32 | $S$ | $A$ | $A$ | 33 | $N$ | $G$ | $G$ |
| **34** | $\boldsymbol{N}$ | $\boldsymbol{G}$ | $\boldsymbol{S}$ | 35 | $N$ | $G$ | $N$ | **36** | $\boldsymbol{N}$ | $\boldsymbol{G}$ | $\boldsymbol{A}$ |
| **37** | $\boldsymbol{N}$ | $\boldsymbol{S}$ | $\boldsymbol{G}$ | 38 | $N$ | $S$ | $S$ | 39 | $N$ | $S$ | $N$ |
| **40** | $\boldsymbol{N}$ | $\boldsymbol{S}$ | $\boldsymbol{A}$ | 41 | $N$ | $N$ | $G$ | 42 | $N$ | $N$ | $S$ |
| 43 | $N$ | $N$ | $N$ | 44 | $N$ | $N$ | $A$ | **45** | $\boldsymbol{N}$ | $\boldsymbol{A}$ | $\boldsymbol{G}$ |
| **46** | $\boldsymbol{N}$ | $\boldsymbol{A}$ | $\boldsymbol{S}$ | 47 | $N$ | $A$ | $N$ | 48 | $N$ | $A$ | $A$ |
| 49 | $A$ | $G$ | $G$ | **50** | $\boldsymbol{A}$ | $\boldsymbol{G}$ | $\boldsymbol{S}$ | **51** | $\boldsymbol{A}$ | $\boldsymbol{G}$ | $\boldsymbol{N}$ |
| 52 | $A$ | $G$ | $A$ | **53** | $\boldsymbol{A}$ | $\boldsymbol{S}$ | $\boldsymbol{G}$ | 54 | $A$ | $S$ | $S$ |
| **55** | $\boldsymbol{A}$ | $\boldsymbol{S}$ | $\boldsymbol{N}$ | 56 | $A$ | $S$ | $A$ | **57** | $\boldsymbol{A}$ | $\boldsymbol{N}$ | $\boldsymbol{G}$ |
| **58** | $\boldsymbol{A}$ | $\boldsymbol{N}$ | $\boldsymbol{S}$ | 59 | $A$ | $N$ | $N$ | 60 | $A$ | $N$ | $A$ |
| 61 | $A$ | $A$ | $G$ | 62 | $A$ | $A$ | $S$ | 63 | $A$ | $A$ | $N$ |
| 64 | $A$ | $A$ | $A$ |    |     |     |     |    |     |     |     |

````

## Disposizioni semplici

Nelle disposizioni con ripetizione, ogni oggetto può comparire più volte nella
sequenza. Quando invece ogni oggetto può essere inserito in una sola posizione,
si parla di _disposizioni semplici_, o _disposizioni senza ripetizione_.
In questo caso è quindi necessario imporre $k \leq n$, perché dopo che tutti
gli $n$ oggetti sono stati inseriti in una sequenza non ve ne sono altri
che possono essere scelti ulteriormente.

```{prf:definition} Disposizione semplice
:label: def-disposizioni-semplici

Fissato un insieme di $n$ oggetti $A = \{ a_1,\dots a_n \}$ e un
numero $k \in \mathbb N$, con $k \leq n$, una _disposizione semplice_ è una
sequenza $(a_{i_1}, \dots, a_{i_k})$, dove per ogni $j = 1, \dots, k$ si ha
$i_j \in \{1, \dots, n\}$ e $a_{i_j} \in A$, e per ogni $j, l = 1, \dots, k$
con $j \neq l$ si ha $a_{i_j} \neq a_{i_l}$. Indichiamo con $d_{n, k}$ il
numero di possibili disposizioni semplici di $n$ oggetti in $k$ posti.
```

````{prf:example}
:label: ex-disposizioni-semplici-1

Se nell’{prf:ref}`ex-disposizioni-con-ripetizione-1` non fosse possibile
assegnare più di un turno giornaliero a una stessa persona, le sequenze come
$(A, G, G)$ non sarebbero più ammesse, e a ogni turnazione corrisponderebbe una
e una sola disposizione semplice di quattro oggetti in tre posti.
````

Per calcolare il numero $d_{n, k}$ di disposizioni semplici di $n$ oggetti in
$k$ posti, possiamo seguire un ragionamento analogo a quello delle
permutazioni semplici:

- l'oggetto da inserire nel primo posto può esere scelto in $n$ modi diversi;
- il secondo posto può essere riempito in $n - 1$ modi possibili, non potendo
  più riusare l'oggetto selezionato per la prima posizione;
- la terza scelta può essere fatta in $n - 2$ modi, e così via fino all'ultimo
  posto, che sarà riempibile scegliendo tra $n - k + 1$ oggetti.

Applicando il principio fondamentale del calcolo combinatorio si ottiene che

```{math}
d_{n, k} = n (n-1) \ldots (n-k+1) =
n (n-1) \ldots (n-k+1) \cdot \frac{(n-k)!}{(n-k)!} =
\frac{n!}{(n-k)!} \enspace.
```

````{prf:example}
:label: ex-disposizioni-semplici-2

La {numref}`tab-disposizioni-con-ripetizione` evidenzia in grassetto le
pianificazioni dell’{prf:ref}`ex-disposizioni-semplici-1`, il cui numero è
uguale a $d_{4, 3} = 4 \cdot 3 \cdot 2 = 24$.
````

Quando $k=n$, per formare una disposizione bisogna utilizzare tutti gli
elementi di $A$, quindi le permutazioni semplici sono un caso particolare di
disposizioni semplici. Coerentemente, si ha che $d_{n, n} = n!/0! = n! = p_n$.

## Esercizi

```{exercise} •
:label: ex-disp-shield-codici

Il sistema informatico dello
[S.H.I.E.L.D.](https://marvel.fandom.com/wiki/S.H.I.E.L.D.) genera codici di
accesso formati da cinque caratteri, ognuno scelto tra otto simboli speciali,
con possibilità di ripetizione. Quanti codici distinti è possibile generare?
```
```{solution} ex-disp-shield-codici
:class: dropdown

Ogni codice è una disposizione con ripetizione di $8$ simboli in $5$ posti,
quindi il numero di codici distinti è $D_{8,5} = 8^5 = 32\,768$.
```

````{exercise} ••
:label: ex-disp-pattuglie-wakanda

La Guardia Reale del [Wakanda](https://marvel.fandom.com/wiki/Wakanda) deve
pianificare le ronde dei prossimi tre giorni, selezionando per ogni giorno un
guerriero diverso tra i sei disponibili. In quanti modi si può organizzare il calendario?
````
````{solution} ex-disp-pattuglie-wakanda
:class: dropdown

Ogni calendario è una disposizione semplice dei sei guerrieri nei tre giorni,
per cui si può organizzare il calendario in $d_{6,3} = 6 \cdot 5 \cdot 4 = 120$
modi diversi.
````

````{exercise} ••
:label: ex-disp-defenders-turni

I [Defenders](https://marvel.fandom.com/wiki/Defenders_(Earth-616))
devono coprire quattro turni distinti in una giornata (alba, mattina,
pomeriggio, notte), scegliendo ogni volta un membro diverso tra nove candidati.
In quanti modi si può compilare la turnazione?
````
````{solution} ex-disp-defenders-turni
:class: dropdown

Si tratta di disposizioni semplici di $9$ oggetti in $4$ posti:

```{math}
d_{9,4} = 9 \cdot 8 \cdot 7 \cdot 6 = 3024.
```
````

````{exercise} ••
:label: ex-disp-portavoce

I membri dei [Guardiani della
galassia](https://marvel.fandom.com/wiki/Guardians_of_the_Galaxy_(Earth-616))
&mdash; Star-Lord, Gamora, Drax, Rocket e Groot &mdash; devono assegnare tre
ruoli distinti: portavoce, vice-portavoce e archivista. Quante assegnazioni
sono possibili, sapendo che Groot non può ricoprire il ruolo di portavoce,
essendo il suo linguaggio limitato all’espressione «Io sono Groot»?
````
````{solution} ex-disp-portavoce
:class: dropdown

Se non vi fossero vincoli, ogni assegnazione sarebbe in corrispondenza con una
delle $d_{5, 3} = 5 \cdot 4 \cdot 3 = 60$ disposizioni senza ripetizione
degli eroi rispetto ai ruoli. Siccome fissare uno dei ruoli riduce il numero di
diverse configurazioni a $d_{4, 2} = 4 \cdot 3 = 12$ &mdash; in quanto restano
due ruoli e quattro persone &mdash; le assegnazioni nelle quali Groot non è
portavoce saranno $60 - 12 = 48$.
````

````{exercise} ••
:label: ex-disp-young-avengers-vincolo

Per una missione degli
[Young Avengers](https://marvel.fandom.com/wiki/Young_Avengers_(Earth-616))
si devono assegnare tre ruoli distinti (comando, ricognizione, supporto) a
sette eroi. In quanti modi si possono assegnare i ruoli se Patriot e Wiccan non
possono essere entrambi selezionati?
````
````{solution} ex-disp-young-avengers-vincolo
:class: dropdown

Se non vi fossero vincoli, ci sarebbero $d_{7, 3} = 7 \cdot 6 \cdot 5 = 210$
modi possibili di procedere. Partendo da questo numero, possiamo sottrarre i
casi non ammessi, nei quali Patriot e Wiccan compaiono entrambi. Essendo i tre
ruoli distinti, i due eroi ne possono occupare due in $3 \cdot 2 = 6$ modi
diversi (si tratta delle disposizioni $d_{3, 2}$ dei tre ruoli in due eroi, o
alternativamente si sceglie prima il ruolo di Patriot, poi quello di Wiccan).
Il terzo ruolo può essere assegnato a uno dei restanti $5$ eroi. I casi da
escludere sono quindi $6 \cdot 5 = 30$, e il numero di configurazioni
valide è $210 - 30 = 180$.
````

````{exercise} •••
:label: ex-disp-avengers-prima-ultima

Gli [Avengers](https://marvel.fandom.com/wiki/Avengers) devono pianificare una
sequenza di quattro missioni consecutive, scegliendo ogni volta un membro
diverso tra Iron Man, Thor, Capitan America, Vedova Nera e Occhio di Falco.
Iron Man deve partecipare alla prima o all'ultima missione. Quante
pianificazioni sono possibili?
````
````{solution} ex-disp-avengers-prima-ultima
:class: dropdown

Contiamo separatamente i casi in cui Iron Man è assegnato alla prima o
all'ultima missione. I due insiemi sono disgiunti, perché ogni eroe
partecipa al più a una missione e non può quindi occupare entrambe le
posizioni.

- Quando Iron Man è coinvolto nella prima missione, le tre restanti si
  possono assegnari ai quattro Avengers rimanenti in
  $d_{4,3} = 4 \cdot 3 \cdot 2 = 24$ modi diveri.
- Il ragionamento al punto precedente non cambia quando Iron Man viene
  assegnato all'ultima missione.

Pertanto, le pianificazioni valide sono $24 + 24 = 48$.
````