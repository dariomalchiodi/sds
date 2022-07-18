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

# Organizzazione del libro

## Convenzioni

Spesso risulta necessario inframmezzare il testo principale con del codice,
non al fine di eseguirlo ma per scopo illustrativo (per esempio per indicare
i letterali `true` e `false` per il tipo di dati `bool`). In questo caso il
codice viene indicato utilizzando un carattere tipografico non proporzionale
(Fira Code) che sfrutta le cosiddette _legature_ per abbellire il modo in cui
vengono visualizzati alcuni elementi del linguaggio di programmazione.

```{margin}
Il software normalmente impiegato per scrivere codice (editor, IDE, e così
via) utilizza normalmente un tipo di carattere predefinito che non è in grado
di gestire le legature, dunque le sequenze di questo tipo rimarranno invariate
quando vengono inserite. È però abbastanza facile cambiare il tipo di
carattere.
```
Per esempio, l'operatore logico di «maggiore o uguale» è descritto dalla
sequenza dei due simboli
<code style="font-family: monospace !important;">>=</code>,
che una volta digitata viene automaticamente convertita nel simbolo `>=`, più
simile a quello utilizzato in ambito matematico.


Quando invece è necessario mostrare una o più righe di codice intese per
essere eseguite, queste verranno organizzate in una _cella di codice_
all'interno di un notebook, visualizzata nel modo che segue.

```{code-cell} ipython3
:tags: [remove-input]
age = 24
```

```{code-cell} ipython3
:tags: [remove-output]
print(age <= 42)
```

Di norma, l'esito dell'esecuzione di codice sarà visualizzato all'interno di
un'apposita _cella di output_, accodata a quella di codice e mostrata come
di seguito.

```{code-cell} ipython3
:tags: [remove-input]
print(age <= 42)
```

Va notato come le celle di output siano leggermente diverse da quelle di
codice, in quanto queste ultime hanno il bordo sinistro evidenziato con un
colore diverso. Questa convenzione è leggermente diversa da quella utilizzata
normalmente nei notebook, in cui il colore delle celle di input cambia quando
queste vengono selezionate per eseguirle o per modificarne i contenuti.

```{admonition} Nomenclatura
:class: naming
Questo tipo di area contiene delle note relative alla nomenclatura utilizzata
in un particolare ambito, o alla descrizione di diciture alternative rispetto
a quelle introdotte.
```

```{prf:definition} Definizione
:label: segnaposto-definizione
In questa area vengono definiti in modo formale uno o più concetti.
```

```{prf:example} Esempio
:label: segnaposto-esempio
Questa area racchiude un esempio.
```

```{prf:theorem}
:label: segnaposto-teorema
Questa area contiene la tesi di un teorema.
```

```{prf:proof}
In questa area viene inserita la dimostrazione di un teorema.
```

```{prf:corollary}
:label: segnaposto-corollario
Questa area contiene la definizione di un corollario e la sua dimostrazione.
```

## Notazione

La {numref}`tab-notazione` elenca le principali notazioni utilizzate nel
testo.

```{table} Notazione utilizzata nel testo
:name: tab-notazione
:align: center
|  Simbolo                      | Significato |
|:-----------------------------:|:-----------:|
| $\mathbb N$                   | insieme dei numeri naturali                                        |
| $\mathbb R$                   | insieme dei numeri reali                                        |
| $A = \{ a_1, \dots a_n \}$    | insieme / evento composto dagli elementi / esiti $a_1, \dots, a_n$ |
| $a \in A$                     | elemento $a$ dell'insieme $A$                                      |
| $(a_1, \dots, a_n)$           | disposizione o permutazione composta dagli elementi $a_1, \dots, a_n$ |
| $n!$                          | fattoriale del numero intero $n$                                   |
| $\binom{n}{k}$                | coefficiente binomiale («$n$ su $k$»)                              |
| $p_n$                         | numero di permutazioni semplici di $n$ elementi                    |
| $P_{n; n_1, \dots, n_k}$      | numero di permutazioni con ripetizione di $n$ elementi distinguibili a gruppi contenenti $n_1, \dots, n_k$ oggetti |
| $\{ a_1, \dots, a_n \}$       | combinazione composta dagli elementi $a_1, \dots, a_n$             |
| $D_{n, k}$                    | disposizioni con ripetizione di $n$ oggetti in $k$ posti           |
| $d_{n, k}$                    | disposizioni senza ripetizione di $n$ oggetti in $k$ posti         |
| $c_{n, k}$                    | combinazioni semplici di $n$ oggetti in $k$ posti                  |
| $C_{n, k}$                    | combinazioni con ripetizione di $n$ oggetti in $k$ posti           |
| $S \subseteq T$               | sottoinsieme / sottoevento $S$ di un insieme / evento $T$          |
| $\Omega$                      | insieme universo / spazio degli esiti                              |
| $A \rightarrow B$             | (evento o proposizione) $A$ implica (evento o proposizione) $B$    |
| $A \leftrightarrow B$         | (evento o proposizione) $A$ coimplica (evento o proposizione) $B$  |
| $S \cup T$                    | unione degli insiemi / eventi $S$ e $T$                            |
| $S \cap T$                    | intersezione degli insiemi / eventi $S$ e $T$                      |
| $S \backslash T$              | differenza tra l'insieme / eventi $S$ e l'insieme / evento $T$     |
| $S \ominus T$                 | differenza simmetrica tra gli insiemi /eventi $S$ e $T$            |
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
| $a \triangleq b$              | $a$ è definito come uguale a $b$                                   |
```