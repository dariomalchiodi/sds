---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  name: python3
  display_name: Python 3
---

(sec:notazione)=
# Notazione

La {numref}`tab-notazione` elenca le principali notazioni che utilizzerò nelle
formule matematiche.

```{table} Notazione utilizzata nel testo per le formule matematiche.
:name: tab-notazione
:align: center
:class: [full-width]

|  Simbolo                      | Significato |
|:------------------------------|:------------|
| $\mathbb N$                   | insieme dei numeri naturali                                        |
| $\mathbb Z$                   | insieme dei numeri interi                                        |
| $[a..b]$                      | intervallo discreto dei numeri interi compresi tra $a$ e $b$ (estremi inclusi) |
| $\mathbb R$                   | insieme dei numeri reali                                        |
| $[a, b]$                      | intervallo chiuso dei numeri reali compresi tra $a$ e $b$ |
| $(a, b)$                      | intervallo aperto dei numeri reali compresi tra $a$ e $b$ |
| $[a, b)$, $(a, b]$            | intervalli semiaperti dei numeri reali compresi tra $a$ e $b$ |
| $A = \{ a_1, \dots a_n \}$    | insieme/evento composto dagli elementi/esiti $a_1, \dots, a_n$ |
| $a \in A$                     | elemento $a$ dell'insieme $A$                                      |
| $(a_1, \dots, a_n)$           | disposizione o permutazione composta dagli elementi $a_1, \dots, a_n$ |
| $n!$                          | fattoriale del numero intero $n$                                   |
| $\binom{n}{k}$                | coefficiente binomiale («$n$ su $k$») di $n$ oggetti in $k$ posti              |
| $p_n$                         | numero di permutazioni semplici di $n$ elementi                    |
| $P_{n; n_1, \dots, n_k}$      | numero di permutazioni con ripetizione di $n$ elementi distinguibili a gruppi contenenti $n_1, \dots, n_k$ oggetti |
| $\{ a_1, \dots, a_n \}$       | combinazione composta dagli elementi $a_1, \dots, a_n$             |
| $D_{n, k}$                    | disposizioni con ripetizione di $n$ oggetti in $k$ posti           |
| $d_{n, k}$                    | disposizioni senza ripetizione di $n$ oggetti in $k$ posti         |
| $c_{n, k}$                    | combinazioni semplici di $n$ oggetti in $k$ posti                  |
| $C_{n, k}$                    | combinazioni con ripetizione di $n$ oggetti in $k$ posti           |
| $S \subseteq T$               | sottoinsieme/sottoevento $S$ di un insieme/evento $T$          |
| $\Omega$                      | insieme universo / spazio degli esiti                              |
| $A \rightarrow B$             | evento/proposizione $A$ implica evento/proposizione $B$    |
| $A \leftrightarrow B$         | evento/proposizione $A$ coimplica evento/proposizione $B$  |
| $S \cup T$                    | unione degli insiemi/eventi $S$ e $T$                            |
| $S \cap T$                    | intersezione degli insiemi/eventi $S$ e $T$                      |
| $S \backslash T$              | differenza tra l'insieme/evento $S$ e l'insieme/evento $T$     |
| $S \ominus T$                 | differenza simmetrica tra gli insiemi/eventi $S$ e $T$            |
| $A \vee B$                    | disgiunzione logica tra le proposizioni $A$ e $B$                  |
| $A \wedge B$                  | congiunzione logica tra le proposizioni $A$ e $B$                  |
| $\mathscr E$                  | esperimento casuale                                                |
| $\omega \in \Omega$           | esito di un esperimento casuale                                    |
| $\{ \omega \}$                | evento elementare                                                  |
| $\mathsf A$                   | algebra degli eventi                                               |
| $2^A$                         | insieme delle parti dell'insieme $A$                               |
| $\mathbb P$                   | funzione di probabilità                                            |
| $\mathbb P(E)$                | probabilità dell'evento $E$                                        |
| $\mathbb P(E\|F)$             | probabilità condizionata dell'evento $E$ dato l'evento $F$         |
| $\mathbb E(X)$                | valore atteso della variabile aleatoria $X$                        |
| $\mathbb E(g(X))$             | valore atteso della funzione $g$ della variabile aleatoria $X$     |
| $\mathbb E(g(X, Y))$           | valore atteso della funzione $g$ delle variabili aleatorie $X$ e $Y$ |
| $a \triangleq b$              | $a$ è definito come uguale a $b$                                   |
```

