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

(sec_esercizi-combinatorica)=
# Esercizi

```{exercise} •

Dato l'insieme $A = \{ a_1,\dots a_n \}$ e indicato con $\mathcal{P}(A)$
l'insieme delle parti di $A$, calcolare la cardinalità di $\mathcal{P}(A)$.
```

````{admonition} Soluzione 1

Ricordiamo che l'insieme delle parti $\mathcal{P}(A)$ è l'insieme di tutti i
sottinsiemi propri e impropri di $A$: contiene l'insieme vuoto, tutti i
sottinsiemi costituiti da un solo elemento di $A$, tutti i sottinsiemi
costituiti da due soli elementi di $A$ e così via, e contiene anche $A$
stesso.

Siccome il numero di sottinsiemi costituiti da $k$ elementi è
$c_{n,k}=\binom{n}{k}$, si ha  che la cardinalità di $\mathcal{P}(A)$ è
$|\mathcal{P}(A)| = 1 + \sum_{k=1}^{n} \binom{n}{k}$, dove il primo addendo
è dovuto alla presenza dell'insieme vuoto. Sfruttando le proprietà del
coefficiente binomiale otteniamo

```{math}
|\mathcal{P}(A)| = \sum_{k=0}^{n} \binom{n}{k}
                 = \sum_{k=0}^{n}\binom{n}{k} 1^k 1^{n-k} = 2^n,
```

dove nell'ultimo passaggio abbiamo utilizzato la formula del binomio di
Newton: $(a+b)^n = \sum_{k=0}^{n}\binom{n}{k}a^k b^{n-k}$, ponendo $a=1$ e
$b=1$.
````
````{admonition} Soluzione 2
:class: dropdown

Se rappresentiamo ogni sottinsieme $S$ di $A$ come una $n$-upla di elementi
binari in cui nella posizione $i$-esima compare il simbolo $1$ se l'elemento
$a_i$ appartiene a $S$  e il simbolo $0$ se l'elemento $a_i$ non vi
appartiene, allora l'insieme delle parti $\mathcal{P}(A)$ è l'insieme di
tutte le $n$-uple che possiamo costruire a partire dai due simboli $0$ e $1$.
Quindi

```{math}
|\mathcal{P}(A)| = D_{n,2}=2^n.
```
````

```{exercise} •
Quanti numeri telefonici di 7 cifre tutte diverse si possono avere?

_Soluzione_: $d_{10,7} = 604800$.
```

```{exercise} •
Quante combinazioni di numeri si posso ottenere lanciando 3 dadi?

_Soluzione_: $C_{6,3} = 56$.
```

```{exercise} •
In quanti modi lanciando 3 dadi possono uscire facce tutte diverse?

_Soluzione_: $d_{6,3}=120$ se i dadi sono tra loro distinguibili e
$c_{6,3}=20$ se questi non sono distinguibili.
```

```{exercise} •
Quanti sono gli anagrammi della parola ROMA?

_Soluzione_: le permutazioni semplici $d_{4,4} = 24$.
```

```{exercise} •
Quanti sono gli anagrammi della parola MATEMATICA?

_Soluzione_: le permutazioni di oggetti distinguibili a gruppi
$P_{10; 3, 2, 2, 1, 1, 1} = 151200$.
```

```{exercise} •
In quanti modi 3 persone possono occupare 4 posti numerati?

_Soluzione_: nel numero di modi in cui posso assegnare $4$ posti a $3$
persone: $d_{4, 3} = 24$.
```

