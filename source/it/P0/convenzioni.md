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

(sec:convenzioni)=
# Convenzioni e notazione

Per quanto detto nel paragrafo precedente, spesso inframmezzerò il testo con
del codice. Non sempre sarà pensato per essere eseguito: a volte lo userò a
scopo illustrativo, ad esempio per indicare `true` e `false` come gli unici
lettarli possibili per il tipo di dati `bool`. In questi casi, utilizzerò un
carattere tipografico non proporzionale con un colore diverso rispetto al testo
principale. Quando invece sarà necessario presentare del codice pensato per
essere eseguito, lo inserirà all'interno di un riquadro che ricorda una _cella
di codice_ in un _notebook_. Anche qui utilizzerò un carattere non
proporzionale, evidenziando con colori diversi particolari elementi nel codice
(come variabili, letterali o parole chiave) come accade nei moderni IDE.
Inoltre, il codice risulterà staccato rispetto al testo principale, come
nell'esempio seguente.
```{margin}
È pratica comune utilizzare un carattere non proporzionale, in cui ogni glifo
ha la stessa larghezza, per visualizzare codice, input e output. Questo
migliora la leggibilità del codice, facilitando l'indentazione delle
istruzioni e riducendo il rischio di confondere caratteri simili, come 1 e l
o come O e 0.
```

```python
age = 24
print(age <= 42)
```

Di norma, visualizzerò l'eventuale output dell'esecuzione all'interno di
un'apposita _cella di output_, posizionata subito dopo quella di codice, come mostrato di seguito, in modo da rendere chiaro il legame tra istruzioni e
risultati.

```python
print(age <= 42)
```

Per evidenziare nel testo alcune componenti particolari, utilizzerò blocchi
dedicati, ciascuno con uno stile specifico.

```{admonition} _
:class: naming
Aree di questo tipo contengono spiegazioni sui termini usati o su diciture
alternative.
```

```{prf:definition}
:label: segnaposto-definizione
:class: no-number
In quest'area vengono introdotti uno o più concetti in modo rigoroso.
```
```{margin}
Definizioni, esempi e così via saranno normalmente numerati, e spesso
accompagnati da un nome specifico racchiuso tra parentesi.
```

```{prf:example}
:label: segnaposto-esempio
:class: no-number
Gli esempi saranno racchiusi di riquadri di questo tipo.
```

````{prf:theorem}
:label: segnaposto-teorema
:nonumber:
:class: no-number
Questo tipo di blocco contiene la tesi di un teorema.
````

```{prf:corollary}
:label: segnaposto-corollario
:class: no-number
Le proposizioni di un corollario saranno inserite in aree come questa.
```

```{prf:lemma}
:class: no-number
:label: segnaposto-lemma
Questa area contiene la proposizione di un lemma.
```

```{admonition} _
:class: myproof
In questo blocco vengono inserite le dimostrazioni di teoremi, corollari o
lemma. Le ometterò ogni volta che sarà importante introdurre un risultato
teorico la cui dimostrazione richiede conoscenze matematiche avanzate.
```

```{note}
Questo tipo di riquadro contiene alcuni aspetti secondari che preferisco
mettere in evidenza nel testo, piuttosto che descriverli nelle note a pie' di
pagina.
```

Infine, la {numref}`tab-notazione` elenca le principali notazioni che
utilizzerò nelle formule matematiche.

```{table} Notazione utilizzata nel testo per le formule matematiche.
:name: tab-notazione
:align: center
:class: [full-width]

|  Simbolo                   | Significato                                                                    |
|:---------------------------|:-------------------------------------------------------------------------------|
| $\mathbb N$                | insieme dei numeri naturali                                                    |
| $\mathbb Z$                | insieme dei numeri interi                                                      |
| $[a..b]$                   | intervallo discreto dei numeri interi compresi tra $a$ e $b$ (estremi inclusi) |
| $\mathbb R$                | insieme dei numeri reali                                                       |
| $[a, b]$                   | intervallo chiuso dei numeri reali compresi tra $a$ e $b$                      |
| $(a, b)$                   | intervallo aperto dei numeri reali compresi tra $a$ e $b$                      |
| $[a, b)$, $(a, b]$         | intervalli semiaperti dei numeri reali compresi tra $a$ e $b$                  |
| $A = \\{ a_1, \dots a_n \\}$ | insieme/evento composto dagli elementi/esiti $a_1, \dots, a_n$                 |
| $a \in A$                  | elemento $a$ dell'insieme $A$                                                  |
| $(a_1, \dots, a_n)$        | disposizione o permutazione composta dagli elementi $a_1, \dots, a_n$          |
| $n!$                       | fattoriale del numero intero $n$                                               |
| $\binom{n}{k}$             | coefficiente binomiale («$n$ su $k$») di $n$ oggetti in $k$ posti              |
| $p_n$                      | numero di permutazioni semplici di $n$ elementi                                |
| $P_{n; n_1, \dots, n_k}$   | numero di permutazioni con ripetizione di $n$ elementi distinguibili a gruppi contenenti $n_1, \dots, n_k$ oggetti |
| $\\{ a_1, \dots, a_n \\}$    | combinazione composta dagli elementi $a_1, \dots, a_n$                         |
| $D_{n, k}$                 | disposizioni con ripetizione di $n$ oggetti in $k$ posti                       |
| $d_{n, k}$                 | disposizioni senza ripetizione di $n$ oggetti in $k$ posti                     |
| $c_{n, k}$                 | combinazioni semplici di $n$ oggetti in $k$ posti                              |
| $C_{n, k}$                 | combinazioni con ripetizione di $n$ oggetti in $k$ posti                       |
| $S \subseteq T$            | sottoinsieme/sottoevento $S$ di un insieme/evento $T$                          |
| $\Omega$                   | insieme universo / spazio degli esiti                                          |
| $A \rightarrow B$          | evento/proposizione $A$ implica evento/proposizione $B$                        |
| $A \leftrightarrow B$      | evento/proposizione $A$ coimplica evento/proposizione $B$                      |
| $S \cup T$                 | unione degli insiemi/eventi $S$ e $T$                                          |
| $S \cap T$                 | intersezione degli insiemi/eventi $S$ e $T$                                    |
| $S \backslash T$           | differenza tra l'insieme/evento $S$ e l'insieme/evento $T$                     |
| $S \ominus T$              | differenza simmetrica tra gli insiemi/eventi $S$ e $T$                         |
| $A \vee B$                 | disgiunzione logica tra le proposizioni $A$ e $B$                              |
| $A \wedge B$               | congiunzione logica tra le proposizioni $A$ e $B$                              |
| $\mathscr E$               | esperimento casuale                                                            |
| $\omega \in \Omega$        | esito di un esperimento casuale                                                |
| $\\{ \omega \\}$             | evento elementare                                                              |
| $\mathsf A$                | algebra degli eventi                                                           |
| $2^A$                      | insieme delle parti dell'insieme $A$                                           |
| $\mathbb P$                | funzione di probabilità                                                        |
| $\mathbb P(E)$             | probabilità dell'evento $E$                                                    |
| $\mathbb P(E\|F)$          | probabilità condizionata dell'evento $E$ dato l'evento $F$                     |
| $\mathbb E(X)$             | valore atteso della variabile aleatoria $X$                                    |
| $\mathbb E(g(X))$          | valore atteso della funzione $g$ della variabile aleatoria $X$                 |
| $\mathbb E(g(X, Y))$       | valore atteso della funzione $g$ delle variabili aleatorie $X$ e $Y$           |
| $a \triangleq b$           | $a$ è definito come uguale a $b$                                               |
```

