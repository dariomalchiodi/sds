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

(sec_combinazioni)=
# Combinazioni

Analogamente alle disposizioni, anche le combinazioni descrivono delle tuple di
lunghezza prefissata nelle quali occorrono oggetti scelti da un insieme. In
questo caso, però, le tuple _non sono ordinate_: non si tratta di sequenze,
bensì di _sottoinsiemi_ dell'insieme di partenza. Pertanto, nel raggruppamento
che corrisponde alle combinazioni non è rilevante l'ordine, ma rimane la
possibilità di decidere se gli oggetti si possano ripetere oppure no. Le due
categorie di combinazioni risultanti sono descritte nei paragrafi che seguono.

## Combinazioni semplici

```{margin}
È anche possibile parlare della costruzione di _insiemi_ a partire da un
_universo_ che contiene gli oggetti considerati.
```
Quando un oggetto può essere considerato al più una volta, possiamo a tutti gli
effetti dire che vi è corrispondenza tra le combinazioni, che vengono dette
_semplici_, e i sottoinsiemi dell'insieme di partenza.

````{prf:definition}
:label: def-combinazioni
Consideriamo un insieme $A = \{ a_1, \ldots, a_n \}$ di $n$ oggetti e
fissiamo un numero naturale $k \leq n$. Una _combinazione semplice_ (o più
semplicemente _combinazione_) degli $n$ oggetti in $k$ posti è una tupla non
ordinata $\{ a_{i_1}, \dots, a_{i_k} \}$ tale che per ogni $j = 1, \dots, k$ si
ha $a_{i_j} \in A$, e $a_{i_j} \neq a_{i_l}$ per ogni
$j, l = 1, \dots, k$ con $j \neq l$. Indichiamo il numero di possibili
combinazioni semplici di $n$ oggetti in $k$ posti con $c_{n, k}$.
````

Indicherò le combinazioni usando le parentesi graffe come delimitatori delle
tuple, per sottolineare che l'ordine non è rilevante; inoltre, questa
notazione è coerente con il fatto che una combinazione semplice individua un
sottoinsieme $\{ a_{i_1}, \dots, a_{i_k} \}\subseteq A$, così che le
descrizioni del sottoinsieme &mdash; fatta in modo estensivo &mdash; e della
combinazione coincidono.

````{prf:example} Peter Petrelli
:label: ex-peter-petrelli
[Peter Petrelli](https://comicvine.gamespot.com/peter-petrelli/4005-47678/) è
uno dei protagonisti di
[Heroes](https://comicvine.gamespot.com/heroes/4050-19509/), dotato di una
straordinaria forma di _empatia_ che gli permette di riprodurre i poteri
degli altri supereroi che si trovano nelle sue vicinanze.
Ipotizziamo che questo meta-potere sia limitato, e che Peter sia in grado
di replicare tre superpoteri alla volta:
$\{ \text{psicocinesi}, \text{telepatia}, \text{invisibilità} \}$ e
$\{ \text{telepatia}, \text{invisibilità}, \text{psicocinesi} \}$ indicano una
medesima terna non ordinata, e dunque uno stesso sottoinsieme e
una sola combinazione semplice di $k = 3$ superpoteri. In questo caso,
l'insieme da cui estraiamo gli oggetti è l'insieme di tutti i superpoteri, ed è
poco rilevante determinarne la cardinalità $n$.
````

Per calcolare il numero $c_{n, k}$ di possibili combinazioni semplici di $n$
oggetti in $k$ posti si può sfruttare il legame tra queste e le disposizioni
semplici: 
- ogni combinazione semplice corrisponde a più disposizioni: permutando in
  tutti i modi possibili i $k$ oggetti che la compongono si ottengono $k!$
  disposizioni distinte;
- di conseguenza, ogni combinazione compare esattamente $k!$ volte nell'insieme
  delle $d_{n, k}$ disposizioni semplici di $n$ oggetti in $k$ posti, da cui
  $d_{n, k} = c_{n, k} \cdot k!$;
- invertendo quetsa relazione si ricava $c_{n, k} = \frac{d_{n, k}}{k!}$.

Applicando la formula per il calcolo di $d_{n, k}$ si ottiene infine

```{math}
c_{n, k} = \frac{d_{n, k}}{k!} = \frac{n!}{(n-k)!k!} =\binom{n}{k} \enspace.
```

````{prf:example} Peter Petrelli
:label: ex-peter-petrelli-2

Immaginiamo che vi siano in tutto $n = 477$ possibili
superpoteri[^superpoteri], e che Peter Petrelli (vedi
l’{prf:ref}`ex-peter-petrelli`) sia in grado di riprodurli tutti.
Ciò significa che, a un dato istante, sarà in grado di «ricordarsi»
$c_{477, 3} = \binom{477}{3} = \;$
<span style="word-spacing: -0.1rem">17 974 950</span>
diverse configurazioni di tre superpoteri.
````

## Combinazioni con ripetizione

Quando è possibile inserire uno stesso oggetto più volte in una combinazione,
si dice che quest'ultima è una _combinazione con ripetizione_. In questo caso,
la costruzione di una combinazione è analoga a quella di un _multiinsieme_, una
generalizzazione del concetto di insieme nella cui descrizione in forma
estensiva gli oggetti possono comparire più volte, così che ogni elemento nel
multiinsieme ha anche una _molteplicità_, intesa come il numero di volte che
occorre.

````{prf:definition} Combinazione con ripetizione
:label: def-combinazione-con-ripetizione

Consideriamo un insieme $A = \{ a_1, \ldots, a_n \}$ di $n$ oggetti e
fissiamo un numero naturale $k \in \mathbb N$. Una _combinazione semplice_ (o,
più semplicemente, _combinazione_) degli $n$ oggetti in $k$ posti è una tupla
non ordinata $\{ a_{i_1}, \dots, a_{i_k} \}$ tale che per ogni
$j = 1, \dots, k$ si ha $a_{i_j} \in A$. Indichiamo il numero di tutte le
possibili combinazioni con ripetizione di $n$ oggett in $k$ posti con
$c_{n, k}$.
````

Descriverò le combinazioni con ripetizione usando la stessa notazione di quelle
semplici, con la differenza che in questo caso la tupla tra parentesi graffe
potrà contenere dei doppioni.

````{prf:example}
:label: ex-combinazioni-con-ripetizione

Immaginiamo un ascensore con capienza di quattro persone, pieno di cloni di
Dupli-Kate e Multi-Paul (vedi l’{prf:ref}`dupli-kate-multi-paul`), senza che
entrambi i gemelli debbano necessariamente essere presenti. La
{numref}`tab-combinazioni-DK-MP` elenca tutti i modi in cui si possono
inserire quattro cloni nell'ascensore, dove ogni configurazione corrisponde
a una combinazione con ripetizione dei due oggetti $k$ e $p$ (Kate e Paul) in
quattro posti.
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


Un modo possibile per calcolare il numero $C_{n, k}$ di combinazioni con
ripetizione di $n$ oggetti di un insieme $A$ in $k$ posti consiste
nell'associarle univocamente a degli opportuni sottoinsiemi di $\mathbb N$.
Fissata una funzione biunivoca $r: A \rightarrow \{ 1, \ldots, n \}$, ogni
possibile combinazione con ripetizione $\{ a_{i_1}, \ldots, a_{i_k} \}$ può
essere trasformata nell'insieme numerico $\{r(a_{i_1}), \ldots, r(a_{i_k}) \}$,
scambiando ogni elemento con la sua rappresentazione numerica attraverso $r$.
Se indichiamo con $\sigma^r$ la sequenza ottenuta ordinando quest'ultimo
insieme in senso non decrescente, segue che:

- $\sigma^r$ non dipende dal particolare ordine in cui sono elencati gli
  elementi della combinazione di partenza;
- i $k$ elementi di $\sigma^r$ sono valori interi compresi tra $1$ e $n$,
  estremi inclusi, ed è possibile che questa sequenza contenga valori contigui
  che sono identici.

Infine, indichiamo con $\sigma^r_i$ l’$i$-esimo elemento di $\sigma^r$ e
costruiamo un'ultima sequenza

```{math}
\rho = \{ \sigma^r_1 + 0, \sigma^r_2 + 1, \ldots, \sigma^r_k + k - 1 \}.
```


Anche $\rho$ conterrà $k$ elementi, ma essi saranno automaticamente ordinati in
senso strettamente crescente, perché sono stati ottenuti incrementando di una
quantità via via più grande gli elementi di $\sigma^r$, che è non decrescente.
Inoltre, $\rho$ conterrà valori interi compresi tra $1$ e $n + k - 1$, dunque
essa può essere messa in corrispondenza biunivoca con un sottoinsieme di
$M = \{ 1, \ldots, n + k - 1 \}$ che contiene $k$ elementi.
Ricapitolando, ogni combinazione con ripetizione di $n$ oggetti in $k$ posti
può essere messa in relazione con un sottoinsieme di $M$ di cardinalità $k$.

D'altro canto, un generico sottoinsieme di $M$ di cardinalità $k$ può essere
descritto scrivendo i suoi elementi ordinandoli in senso crescente, ottenendo
dunque una sequenza $\rho$. Se ora decrementiamo gli elementi di questa
sequenza sottraendo zero al primo elemento, uno al secondo elemento, due al
terzo elemento e così via, otteniamo una nuova sequenza $\sigma^r$ ordinata in
senso non decrescente e i cui valori (che possono essere ripetuti), sono
compresi tra $1$ e $n$ (estremi inclusi). Considerando quindi le preimmagini di
questi valori attraverso $r$ si ottiene una combinazione con ripetizione di $k$
oggetti di $A$. Dunque ogni sottoinsieme di $M$ di $k$ elementi può essere
messo in relazione con una combinazione con ripetizione di $n$ oggetti in $k$
posti.

````{prf:example}
:label: combinazioni-DK-MP-2
Riprendendo l’{prf:ref}`ex-combinazioni-con-ripetizione`, abbiamo che l'insieme
degli oggetti di partenza $A = \{ k, p \}$, dove $k$ e $p$ indicano
rispettivamente Kate e Paul, può essere messo in corrispondenza biunivoca con
l'insieme $N = \{ 1, 2 \}$ per esempio ponendo $r(k) = 2$ e $r(p) = 1$. La
{numref}`tab-combinazioni-DK-MP-2` mostra la corrispondenza tra tutte le
combinazioni con ripetizione dei due oggetti in $A$ in quattro posizioni e le
sequenze $\sigma^r$ e $\rho$.
````

```{table} Corrispondenza tra le combinazioni con ripetizione di Dupli-Kate e Multi-Paul in quattro posti.
:name: tab-combinazioni-DK-MP-2
:align: center

|    Combinazione    |     $\sigma^r$     |     $\rho$     |
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


[^superpoteri]: Come indicato ad esempio in
[superherodb](https://www.superherodb.com/powers/).


## Esercizi

````{exercise} ••
:label: ex-insieme-parti

Dato l'insieme $A = \{ a_1,\dots a_n \}$ e indicato con $\mathcal{P}(A)$
l'insieme delle parti di $A$, calcolare la cardinalità di $\mathcal{P}(A)$.
````
````{solution} ex-insieme-parti
:class: dropdown

Ricordiamo che l'insieme delle parti $\mathcal{P}(A)$ è l'insieme di tutti i
sottinsiemi propri e impropri di $A$: contiene l'insieme vuoto, tutti i
sottinsiemi costituiti da un solo elemento di $A$, tutti i sottinsiemi
costituiti da due soli elementi di $A$ e così via, e contiene anche $A$
stesso.

Siccome il numero di sottinsiemi costituiti da $k$ elementi è
$c_{n,k}=\binom{n}{k}$, si ha che la cardinalità di $\mathcal{P}(A)$ è
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

Questo esercizio si può risolvere anche nel modo seguente: se rappresentiamo
ogni sottinsieme $S$ di $A$ come una $n$-upla di elementi binari, in cui nella
posizione $i$-esima compare il simbolo $1$ se l'elemento $a_i$ appartiene a
$S$  e il simbolo $0$ se l'elemento $a_i$ non vi appartiene, allora l'insieme
delle parti $\mathcal{P}(A)$ è l'insieme di tutte le $n$-uple che 
costruire a partire dai due simboli $0$ e $1$. Quindi

```{math}
|\mathcal{P}(A)| = D_{n,2}=2^n.
```

````

````{exercise} ••
:label: ex-comb-justice-league-squadra

La [Justice League](https://dc.fandom.com/wiki/Justice_League_(Prime_Earth))
deve selezionare una squadra di intervento rapido composta da quattro membri,
scegliendoli tra dieci candidati. In quanti modi distinti si può formare la
squadra?
````
````{solution} ex-comb-justice-league-squadra
:class: dropdown

Si tratta di scegliere quattro eroi tra dieci, senza ordine e senza
ripetizione. Ciò si può fare in $c_{10,4} = \binom{10}{4} = 210$ modi.
````

````{exercise} ••
:label: ex-comb-xmen-professore-x

Gli [X-Men](https://marvel.fandom.com/wiki/X-Men) devono formare un team di
cinque membri su dodici disponibili. Il Professor X deve essere necessariamente
incluso. Quante squadre diverse sono possibili?
````
````{solution} ex-comb-xmen-professore-x
:class: dropdown

Se il Professor X non può mancare, vanno scelti quattro membri tra i
rimanenti undici. Il numero di squadre è quindi $c_{11,4} = \binom{11}{4} =
330$.
````

````{exercise} •••
:label: ex-comb-defenders-non-insieme

I [Defenders](https://marvel.fandom.com/wiki/Defenders_(Earth-616)) hanno
nove candidati per una missione alla quale devono partecipare quattro elementi.
In quanti modi si può formare la squadra se Daredevil e Jessica Jones non
possono comparire insieme?
````
````{solution} ex-comb-defenders-non-insieme
:class: dropdown

Senza vincoli, le squadre possibili sarebbero $c_{9, 4} = \binom{9}{4} = 126$.
D'altro canto, le squadre in cui sono presenti sia Daredevil che Jessica Jones
si contano nel modo seguente: fissata la coppia, vanno scelti altri due membri
tra i restanti sette, e questo si può fare in $c_{7,2} = \binom{7}{2} = 21$
modi. Le squadre valide sono quindi $126 - 21 = 105$.
````

````{exercise} ••
:label: ex-comb-legione-risorse

I [Guardiani della
Galassia](https://marvel.fandom.com/wiki/Guardians_of_the_Galaxy_(Earth-616))
stanno equipaggiando la [Milano](https://marvel.fandom.com/wiki/Milano) (la loro astronave) per una missione. A bordo ci sono cinque alloggiamenti
disponibili, ognuno dei quali può essere occupato da uno tra quattro
tipi di dispositivo: cannoni laser, scudi energetici, sensori di rilevamento e
moduli di supporto vitale. Calcolate il numero di modi diversi per configurare
la Milano, tenendo conto che ogni dispositivo può essere installato più volte
e che interessa solo quanti dispositivi di ciascun tipo vengono installati
(non in quali alloggiamenti specifici).
````
````{solution} ex-comb-legione-risorse
:class: dropdown

A ogni configurazione corrisponde una e una sola combinazione con ripetizione
di quattro oggetti (i tipi di dispositivi) in cinque posti (gli alloggiamenti),
per un totale di $C_{4,5} = \binom{4+5-1}{5} = \binom{8}{5} = 56$
configurazioni possibili.
````

````{exercise} •
:label: ex-comb-avengers-gemme

Gli [Avengers](https://marvel.fandom.com/wiki/Avengers_(Earth-616)) vogliono
scegliere quattro [Gemme
dell'Infinito](https://marvel.fandom.com/wiki/Infinity_Stones) tra le sei
disponibili, per studiarne il comportamento. Tuttavia, le gemme del Tempo e
della Realtà devono essere studiate insieme, perché modificare la sequenza
degli eventi senza aggiornare lo stato della realtà può generare incoerenze
logiche e paradossi. Quindi queste due gemme devono essere entrambe
selezionate, oppure escluse dal gruppo. Calcolate il numero di configurazioni
diverse di gemme che possono venire prese in considerazione.
````
````{solution} ex-comb-avengers-gemme
:class: dropdown

Siccome le gemme del Tempo e della Realtà devono essere considerate insieme,
oppure completamente escluse, possiamo considerare separatamente i due casi,
calcolando il numero di scelte possibili e poi sommando.

- Ci sono $c_{4, 2} = \binom{4}{2} = 6$ configurazioni che contengono le due
  gemme, perché una volta fissate quelle del Tempo e della Realtà, per
  completare il gruppo bisogna selezionare un sottoinsieme di due elementi
  dalle quattro gemme rimanenti.
- Intuitivamente, se si escludono le due gemme in questione, ne rimangono
  esattamente quattro, che quindi dovranno essere tutte selezionate. Infatti,
  in questo caso vanno considerate le combinazioni di queste quattro gemme in
  quattro posti, che sono $c_{4, 4} = 1$.

Concludendo, ci sono sette modi possibili di selezionare le gemme per
studiarle.
````

````{exercise} •••
:label: ex-comb-batman-gadget-vincolo

Batman deve preparare una cintura scegliendo quattro gadget da un elenco di
otto, ma due gadget (la granata accecante e il visore notturno) sono
incompatibili e non possono essere inclusi insieme. In quanti modi può
scegliere la dotazione?
````
````{solution} ex-comb-batman-gadget-vincolo
:class: dropdown

Se non ci fosse il vincolo di incompatibilità, le dotazioni sarebbero
descritte dalle combinazioni di otto gadget in gruppi di quattro,
per un totale di $c_{8, 4} = \binom{8}{4} = 70$ casi. Da questi dobbiamo
sottrarre le configurazioni non permesse. In tali configurazioni, due scelte
sono già occupate dalla granata e dal visore, quindi il loro numero coincide
con il numero di combinazioni dei sei gadget residui in gruppi di due, cioè
$c_{6, 2} = \binom{6}{2} = 15$. Il totale valido è quindi $70 - 15 = 55$.
````
