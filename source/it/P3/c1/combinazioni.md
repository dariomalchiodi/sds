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

(sec:combinazioni)=
# Combinazioni

Analogamente alle disposizioni, anche le combinazioni descrivono delle
sequenze di lunghezza prefissata costituite da oggetti scelti da un insieme di
partenza. In questo caso, però, le sequenze _non sono ordinate_, e in effetti
è più corretto parlare della costruzione di un _sottoinsieme_ dell'insieme di
partenza. Pertanto nel raggruppamento che corrisponde alle combinazioni
non è rilevante l'ordine, ma possiamo scegliere di potere ripetere gli
oggetti oppure no. Le due categorie di combinazioni risultanti sono descritte
nei paragrafi che seguono.

## Combinazioni semplici

```{margin}
È anche possibile parlare della costruzione di _insiemi_ a partire da un
_universo_ che contiene gli oggetti considerati.
```
Quando non è possibile inserire nella sequenza non ordinata uno stesso oggetto
più di una volta, possiamo a tutti gli effetti dire che vi è corrispondenza
tra le combinazioni, che vengono dette _semplici_, e i sottoinsiemi
dell'insieme di partenza.

````{prf:definition}
:label: def-combinazioni
Consideriamo un insieme $A = \{ a_1, \ldots, a_n \}$ di $n$ oggetti e
fissiamo un numero naturale $k \leq n$. Una _combinazione semplice_ (o più
semplicemente _combinazione_) degli $n$ oggetti in $k$ posti è una sequenza
di questi oggetti che individua un sottoinsieme $B \subseteq A$ di cardinalità
uguale a $k$. Indicheremo con $c_{n, k}$ il numero di differenti combinazioni
semplici di $n$ oggetti in $k$ posti.
````

```{margin}
L'uso delle parentesi graffe è anche direttamente collegato alla sintassi
utilizzata per descrivere gli insiemi in modo estensivo.
```
Indicheremo le combinazioni utilizzando una sintassi simile a quella delle
permutazioni e delle disposizioni, ma in questo caso useremo le parentesi
graffe come delimitatori, per sottolineare che si tratta di sequenze non
ordinate.

````{prf:example} Peter Petrelli
:label: ex-peter-petrelli
Peter Petrelli è uno dei protagonisti della serie Heroes, dotato di una
straordinaria forma di _empatia_ che gli permette di riprodurre i poteri
degli altri supereroi che si trovano nelle sue vicinanze.
Ipotizziamo che questo meta-potere sia limitato, e che Peter sia in grado
di replicare tre superpoteri alla volta: le terne
$\{ \text{psicocinesi}, \text{telepatia}, \text{invisibilità} \}$ e
$\{ \text{telepatia}, \text{invisibilità}, \text{psicocines} \}$ indicano una
medesima sequenza ordinata, e dunque uno stesso sottoinsiemi e
una sola combinazione semplice di $k = 3$ superpoteri. In questo caso l'insieme
da cui estraiamo gli oggetti è l'insieme di tutti i superpoteri, ed è poco
rilevante determinarne la cardinalità $n$.
````

Per calcolare $c_{n, k}$ possiamo utilizzare un ragionamento analogo a quello
seguito per calcolare il numero di permutazioni con ripetizione: basta
osservare che l'insieme delle dispozioni senza ripetizione di $n$ oggetti in
$k$ posti contiene anche tutte le corrispondenti combinazioni, ma ognuna di
queste $c_{n, k}$ combinazioni sarà rappresentata tante volte.
Più precisamente, per ognuna delle combinazioni troveremo $k!$ disposizioni
ottenute permutando i $k$ oggetti coinvolti. Pertanto
$d_{n, k} = c_{n, k} \cdot k!$, da cui si ricava

```{math}
c_{n, k} = \frac{d_{n, k}}{k}! = \frac{n!}{(n-k)!k!} =\binom{n}{k} \enspace.
```

```{margin}
Come indicato in [superherodb](https://www.superherodb.com/powers/).
```
Riprendendo l'esempio precedente, immaginiamo che vi siano in tutto $n = 477$
possibili superpoteri, e che Peter Petrelli sia potenzialmente in grado di
riprodurli tutti.
In un dato istante sarà in grado di «ricordarsi» $\binom{477}{3} = \\;$
<span style="word-spacing: -0.1rem">17 974 950</span>
diverse configurazioni di tre superpoteri.


## Combinazioni con ripetizione

Quando è possibile inserire uno stesso oggetto più volte in una combinazione,
si dice che quest'ultima è una _combinazione con ripetizione_. In questo
caso la costruzione di una combinazione è analogo alla costruzione di un
multiinsieme

````{prf:definition} Combinazione con ripetizione
:label: def-combinazione-con-ripetizione
Consideriamo un insieme $A = \{ a_1, \ldots, a_n \}$ contenente $n$ oggetti, e
fissiamo un numero intero $k \in \mathbb N$. Una _combinazione con ripetizione_
di questi oggetti in $k$ posti è una sequenza non ordinata di $k$ elementi
(non necessariamente distinti) appartenenti ad $A$. Indicheremo con $C_{n, k}$
il numero di combinazioni con ripetizione distinte di $n$ oggetti in $k$ posti.
````

Indicheremo le combinazioni con ripetizione usando la stessa sintassi adottata
per quelle semplici, con la differenza che in questo caso la sequenza tra
parentesi graffe potrà contenere degli elementi ripetuti.

````{prf:example}
:label: ex-combinazioni-con-ripetizione
Immaginiamo che una stanza che
può contenere fisicamente quattro persone sia piena di cloni di Dupli-Kate e
Multi-Paul (vedi {prf:ref}`dupli-kate-multi-paul`), senza che entrambi i
gemelli debbano necessariamente essere presenti. La
{numref}`tab-combinazioni-DK-MP` elenca tutti i modi in cui
la stanza può essere riempita, che corrispondono a tutte le combinazioni con
ripetizione dei due oggetti $k$ e $p$ (Kate e Paul) in quattro posti.

````

```{table} Possibili combinazioni con ripetizione di Dupli-Kate e Multi-Paul in quattro posti
:name: tab-combinazioni-DK-MP
:align: center

|    Combinazione    |
| :----------------: |
| $\{ k, k, k, k \}$ |
| $\{ k, k, k, p \}$ |
| $\{ k, k, p, p \}$ |
| $\{ k, p, p, p \}$ |
| $\{ p, p, p, p \}$ |
```


Un modo possibile per calcolare $C_{n, k}$ è quello di mettere in
corrispondenza biunivoca le combinazioni con ripetizione e degli opportuni
sottoinsiemi di $\mathbb N$. Più precisamente, iniziamo mettendo in
corrispondenza biunivoca gli $n$ oggetti a disposizione con l'insieme dei
primi numeri naturali da $1$ a $n$, ovvero costruiamo una funzione biunivoca
$r: A \rightarrow \{ 1, \ldots, n \}$, dove $A$ indica l'insieme degli
oggetti da combinare. Fissato $k$, una qualunque combinazione con ripetizione
equivale a una sequenza non ordinata $\sigma_A = \{ e_1, \ldots, e_k \}$ tale
che $\forall i = 1, \ldots, k \quad e_i \in A$. Consideriamo ora la sequenza di
numeri interi $\sigma_N = \{r(e_1), \ldots, r(e_k) \}$ ottenuta scambiando ogni
elemento con la sua rappresentazione numerica attraverso $r$ e ordiniamola in
senso non decrescente. In questo modo siamo certi che:
- $\sigma_N$ non dipende dal particolare ordine in cui sono elencato gli
  elementi di $\sigma_A$;
- i $k$ elementi di $\sigma_N$ sono valori interi compresi tra $1$ e $n$,
  estremi inclusi, ed è possibile che questa sequenza contenga valori contigui
  che sono identici.

Infine, indichiamo con $\sigma_N[i]$ l’$i$-esimo elemento di $\sigma_N$ e
costruiamo un'ultima sequenza

```{math}
\sigma_M = \{ \sigma_N[1] + 0, \sigma_N[1] + 1, \ldots, \sigma_N[k] + k - 1 \}.
```


Anche $\sigma_M$ conterrà $k$ elementi, ma essi risultano ordinati in senso
crescente, perché sono stati ottenuti incrementando di una quantità via via più
grande gli elementi di $\sigma_N$, che è una sequenza non decrescente. Inoltre
$\sigma_M$ conterrà valori interi compresi tra $1$ e $n + k - 1$, dunque essa
può essere messa in corrispondenza biunivoca con un sottoinsieme di
$M = \{ 1, \ldots, n + k - 1 \}$ che contiene $k$ elementi.
Ricapitolando, ogni combinazione con ripetizione di $n$ oggetti in $k$ posti
può essere messa in relazione con un sottoinsieme di $M$ di cardinalità $k$.

D'altro canto, un generico sottoinsieme di $M$ di cardinalità $k$ può essere
descritto scrivendo i suoi elementi ordinandoli in senso crescente, ottenendo
dunque una sequenza $\sigma_M$. Se ora decrementiamo gli elementi di questa
sequenza sottraendo zero al primo elemento, uno al secondo elemento, due al
terzo elemento e così via, otteniamo una nuova sequenza $\sigma_N$ ordinata in
verso non decrescente e i cui valori (che possono essere ripetuti), sono
compresi tra $1$ e $n$ (estremi inclusi). Considerando quindi le preimmagini di
questi valori attraverso $r$ si ottiene una combinazione con ripetizione di $k$
oggetti di $A$. Dunque ogni sottoinsieme di $M$ di $k$ elementi può essere
messo in relazione con una combinazione con ripetizione di $n$ oggetti in $k$
posti.

````{prf:example}
:label: combinazioni-DK-MP-2
Riprendendo l’{prf:ref}`ex-combinazioni-con-ripetizione`, abbiamo che l'insieme
degli oggetti di partenza è $A = \{ k, p \}$, dove $k$ e $p$ indicano
rispettivamente Kate e Paul, può essere messo in corrispondenza biunivoca con
l'insieme $N = \{ 1, 2 \}$ per esempio ponendo $r(k) = 2$ e $r(p) = 1$. La
{numref}`tab-combinazioni-DK-MP-2` mostra la corrispondenza tra tutte le
combinazioni con ripetizione dei due oggetti in $A$ in quattro posizioni e le
sequenze $\sigma_N$ e $\sigma_M$.
````

```{table} Corrispondenza tra le combinazioni con ripetizione di Dupli-Kate e Multi-Paul in tre posti
:name: tab-combinazioni-DK-MP-2
:align: center

|    Combinazione    |     $\sigma_N$     |     $\sigma_M$     |
| :----------------: | :----------------: | :----------------: |
| $\{ k, k, k, k \}$ | $\{ 2, 2, 2, 2 \}$ | $\{ 2, 3, 4, 5 \}$ |
| $\{ k, k, k, p \}$ | $\{ 1, 2, 2, 2 \}$ | $\{ 1, 3, 4, 5 \}$ |
| $\{ k, k, p, p \}$ | $\{ 1, 1, 2, 2 \}$ | $\{ 1, 2, 4, 5 \}$ |
| $\{ k, p, p, p \}$ | $\{ 1, 1, 1, 2 \}$ | $\{ 1, 2, 3, 5 \}$ |
| $\{ p, p, p, p \}$ | $\{ 1, 1, 1, 1 \}$ | $\{ 1, 2, 3, 4 \}$ |
```

Pertanto, le combinazioni con ripetizione di $n$ oggetti in $k$ posti sono
in corrispondenza biunivoca con i sottoinsiemi di $M$ di cardinalità $k$, e
siccome il numero di questi sottoinsiemi è uguale al numero di combinazioni
senza ripetizione di $n + k - 1$ oggetti in $k$ posti, possiamo concludere che

```{math}
C_{n, k} = c_{n + k - 1, k} = \binom{n+k-1}{k} \enspace.
```
