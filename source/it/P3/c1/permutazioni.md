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

(sec:permutazioni)=
# Permutazioni

Una permutazione di $n$ oggetti rappresenta un modo possibile di elencare
questi oggetti in qualche ordine. Pertanto, nel raggruppamento che
corrisponde alle permutazioni risulta rilevante l'ordine utilizzato, e non è
possibile utilizzare uno stesso oggetto più di una volta. La costruzione di una
permutazione equivale all'applicazione di queste regole per inserire gli $n$
oggetti in altrettanti posti, perché per definizione tutti gli oggetti devono
essere utilizzati. Come vedremo nei due paragrafi che seguono, il ragionamento
alla base del calcolo del numero di permutazioni dipende dal fatto che gli
oggetti siano tra loro distinguibili oppure no.


## Permutazioni semplici

Quando gli oggetti da permutare sono gli elementi di un insieme, per
definizione devono essere tutti diversi (o in altre parole distinguibili) tra
tra loro, e si parla di _permutazione semplice_, o soltanto di _permutazione_,
come descritto dalla seguente definizione.

````{prf:definition} Permutazione semplice
:label: def-permutazione-semplice
Consideriamo un insieme $A = \\{ a_1,\dots a_n \\}$ contenente $n$ oggetti.
Chiamiamo _permutazione semplice_ (o più brevemente _permutazione_) di questi
oggetti una qualsiasi sequenza ordinata in cui compaiono tutti e soli gli $n$
elementi di $A$.
````

In generale, descriveremo una permutazione elencando i suoi elementi nel
corrispondente ordine, separandoli con delle virgole e delimitando l'elenco
con delle parentesi tonde.

````{prf:example} I Fantastici 4
:label: ex-fantastic-4
Consideriamo l'insieme $Q = \\{ f, i, t, c \\}$ dei Fantastici 4: mister
fantastic ($f$), la donna invisibile ($i$), la torcia umana ($t$) e la cosa
($c$): le possibili permutazioni semplici dei suoi oggetti sono elencate nella
{numref}`permutazioni-fantastici-quattro`.
````

```{table} Possibili permutazioni semplici dei membri dei Fantastici 4
:name: permutazioni-fantastici-quattro
:align: center

|  Permutazione  |  Permutazione  |
| :------------: | :------------: |
| $(f, i, t, c)$ | $(t, f, i, c)$ |
| $(f, i, c, t)$ | $(t, f, c, i)$ |
| $(f, t, i, c)$ | $(t, i, f, c)$ |
| $(f, t, c, i)$ | $(t, i, c, f)$ |
| $(f, c, i, t)$ | $(t, c, f, i)$ |
| $(f, c, t, i)$ | $(t, c, i, f)$ |
| $(i, f, t, c)$ | $(c, f, i, t)$ |
| $(i, f, c, t)$ | $(c, f, t, i)$ |
| $(i, t, f, c)$ | $(c, i, f, t)$ |
| $(i, t, c, f)$ | $(c, i, t, f)$ |
| $(i, c, f, t)$ | $(c, t, f, i)$ |
| $(i, c, t, f)$ | $(c, t, i, f)$ |
```

Per calcolare in generale il numero $p_n$ di differenti permutazioni di $n$
oggetti possiamo applicare il principio fondamentale del calcolo combinatorio:

- calcoliamo in quanti modi possiamo selezionare l'oggetto da inserire nella
  prima posizione: avendo a disposizione $n$ oggetti, abbiamo $n$
  possibilità;
- per ciascuna delle $n$ possibili scelte fatte al punto precedente,
  calcoliamo in quanti modi possiamo selezionare l'oggetto da inserire nella
  seconda posizione: avendo a disposizione $n-1$ oggetti, abbiamo $n-1$
  possibilità; in totale abbiamo dunque $n \cdot (n-1)$ modi differenti per
  scegliere i primi due elementi della sequenza;
- procediamo in modo analogo per tutte le altre posizioni, creando così un
  albero il cui livello $i$ corrisponde alla scelta per riempire l’$i$‑esima
  posizione; se osserviamo che per riempire la posizione $i$-esima sono
  rimasti $n-(i-1)$ elementi di $A$ tra cui scegliere, possiamo dire che
  esistono $n\cdot(n-1) \cdot \ldots \cdot(n-(i-1))$ modi differenti per
  scegliere i primi $i$ elementi della sequenza;
- in particolare, arrivati all'ultima posizione, è rimasto un solo elemento
  di $A$ da scegliere, e abbiamo costruito un albero di profondità $n$ che ha
  un numero di foglie pari a $n(n-1)(n-2)\ldots 1=n!$.

Quindi il numero di possibili permutazioni semplici di $n$ oggetti è
$p_n = n!$. Guardando ad esempio la {numref}`permutazioni-fantastici-quattro`,
potete verificare molto facilmente che essa contiene tutte le possibili
$4! = 24$ permutazioni dei 4 oggetti di $Q$.


## Permutazioni con ripetizione

Quando gli $n$ oggetti da permutare non sono tutti diversi tra loro, non
possiamo più dire che essi fanno parte di un insieme. In casi come questo
si parla piuttosto di un _multiinsieme_, inteso come sequenza non ordinata
in cui ogni elemento può comparire una o più volte. In altre parole, gli $n$
oggetti non sono a due a due distinguibili, bensì esistono $r \in \mathbb N$
diversi oggetti, che possiamo indicare come $a_1, \ldots, a_r$, ognuno dei
quali può occorrere anche più di una volta nella sequenza. Questi oggetti sono
pertant _distinguibili a gruppi_: indichiamo con $n_1, n_2,\ldots n_k$ le
numerosità di questi gruppi, a significare che nel multiinsieme vi sono $n_1$
occorrenze dell'elemento $a_1$, $n_2$ occorrenze di $a_2$ e così via
(ovviamente con $\sum_{i=1}^k n_i=n$). In altre parole possiamo scrivere gli
elementi del multiinsieme uno dopo l'altro ottenendo la sequenza

```{math}
\underbrace{a_1, \ldots, a_1}_{n_1 \text{volte}},
\underbrace{a_2, \ldots, a_2}_{n_2 \text{volte}}, \ldots,
\underbrace{a_r, \ldots, a_r}_{n_r \text{volte}} \enspace.
```

Se cambiamo l'ordine degli elementi, non è detto che otterremo una sequenza
diversa da quella di partenza: potremmo per esempio scambiare tra di loro
due occorrenze di uno stesso simbolo, ottenendo una sequenza invariata. In
casi come questo il concetto di permutazione, descritto dalla definizione che
segue, prende in considerazione solamente le sequenze che sono diverse tra
loro.

````{prf:definition} Permutazione con ripetizione
:label: def-permutation-repetition
Consideriamo un multiinsieme $A = \\{ a_1,\dots a_n \\}$ contenente $n$ oggetti
distinguibili a gruppi di numerosità $n_1, \ldots, n_k$.
Chiamiamo _permutazione di oggetti distinguibili a gruppi_ (più semplicemente
_permutazione con ripetizione_) di questi oggetti una qualsiasi loro sequenza
ordinata che sia distinguibile dalle altre, e indichiamo con
$P_{n; n_1, \ldots, n_k}$ il numero di possibili permutazioni con ripetizione.
````

Indicheremo le permutazioni con ripetizione usando la medesima sintassi di
quelle semplici, separando dunque i loro elementi con virgole e usando delle
parentesi tonde come delimitatori.

````{prf:example} Dupli-Kate e Multi-Paul
:label: dupli-kate-multi-paul
Consideriamo i gemelli Kate e Paul Cha di _Invincible Universe_,
entrambi dotati del potere di autoreplicarsi a piacimento e noti come
Dupli-Kate e Multi-Paul. In particolare, ogni versione di Dupli-Kate è
contrassegnata da un numero intero progressivo che compare sul suo costume,
così che possiamo indicare con $k_1$, $k_2$ e così via le sue varianti
esistenti in un dato momento. Immaginiamo che lo stesso valga per Multi-Paul,
le cui repliche indicheremo con $p_1, p_2, \ldots$, e che di fronte a noi ci
siano due versioni di Kate e tre di Paul, così che il quintetto risultante
possa essere descritto dal multiinsieme $A= \\{ k_1, k_2, p_1, p_2, p_3 \\}$.

Se volessimo calcolare in quanti modi possibili si possono mettere in fila
queste cinque versioni di Kate e Paul, senza tenere conto del loro numero
progressivo, ci troveremmo di fronte al calcolo del numero di permutazioni con
ripetizione di $n = 5$ oggetti divisi in due gruppi distinti, rispettivamente
di numerosità $n_1 = 2$ (quello di Kate) e $n_2 = 3$ (quello di Paul). In
questo contesto, $(k_1, k_2, p_1, p_2, p_3)$ e $(k_2, k_1, p_1, p_2, p_3)$
indicano due diverse permutazioni semplici a cui corrisponde però la stessa
permutazione con ripetizione, in cui le prime due posizioni rappresentano
varianti di Kate e le ultime tre rappresentano repliche di Paul; al contrario,
$(k_1, k_2, p_1, p_2, p_3)$ e $(k_1, p_1, k_2, p_2, p_3)$ indicano permutazioni
con ripetizione differenti (e dunque anche permutazioni semplici differenti)
nelle quali la seconda e terza posizione sono occupate rispettivamente da Kate
e Paul nel primo caso e da Paul e Kate nel secondo.
````

Prima di calcolare il numero totale di permutazioni con ripetizione di $n$
oggetti distinguibili a gruppi di numerosità $n_1, n_2,\dots n_k$, analizziamo
preliminarmente il caso speciale dell’{prf:ref}`dupli-kate-multi-paul`.
```{margin}
in questo caso, avendo solo due gruppi, quando si fissano le posizioni degli
elementi del primo si determinano automaticamente anche quelle degli elementi
del secondo gruppo
```
Concentriamoci su di una possibile permutazione con ripetizione, fissando
le posizioni in cui compare Kate e quelle in cui si trova Paul. Per esempio,
ipotizziamo che la prima e l'ultima posizione siano dedicate a Kate e quelle
rimamenti a Paul:

<p style="text-align: center">Kate Paul Paul Paul Kate</p>

Ora, a questa permutazione con ripetizione corrispondono varie permutazioni
semplici dei cinque oggetti che stiamo considerando (le due copie di Kate e le
tre di Paul): più precisamente, la
{numref}`permutazioni-oggetti-indistinguibili` elenca tutti i modi possibili di
mettere in fila due Kate e tre Paul (le varie permutazioni semplici) in modo
che Kate si trovi agli estremi della fila (la fissata permutazione con
  ripetizione).

```{table} Possibili permutazioni semplici di oggetti in due gruppi distinguibili contenenti rispettivamente due duplicati $k_1$ e $k_2$ di Kate e tre duplicati $p_1$, $p_2$ e $p_3$ di Paul, in modo che Kate si trovi nella prima e nell'ultima posizione
:name: permutazioni-oggetti-indistinguibili
:align: center

|         Permutazione        |
| :-------------------------: |
| $(k_1, p_1, p_2, p_3, k_2)$ |
| $(k_1, p_3, p_1, p_2, k_2)$ |
| $(k_1, p_2, p_3, p_1, k_2)$ |
| $(k_1, p_3, p_2, p_1, k_2)$ |
| $(k_1, p_2, p_1, p_3, k_2)$ |
| $(k_1, p_1, p_3, p_2, k_2)$ |
| $(k_2, p_1, p_2, p_3, k_1)$ |
| $(k_2, p_3, p_1, p_2, k_1)$ |
| $(k_2, p_2, p_3, p_1, k_1)$ |
| $(k_2, p_3, p_2, p_1, k_1)$ |
| $(k_2, p_2, p_1, p_3, k_1)$ |
| $(k_2, p_1, p_3, p_2, k_1)$ |
```

Le righe della {numref}`permutazioni-oggetti-indistinguibili` sono state
ottenute permutando le due copie di Kate nella prima e nell'ultima posizione e
le tre copie di Paul nelle posizioni restanti. Se consideriamo Kate, abbiamo
solo due possibilità: $k_1$ e $k_2$ rispettivamente in prima e ultima
posizione, o viceversa, e queste due possibilità corrispondono alle $2!$
permutazioni semplici delle due versioni di Kate. In altre parole, avremmo
potuto considerare tutte le permutazioni semplici di queste due versioni e per
ognuna di esse prendere il primo elemento e posizionarlo nella prima colonna
della tabella, per poi inserire nell'ultima colonna il secondo elemento. In
questo modo avremmo ottenuto due _template_ per le righe della tabella,
rispettivamente per quelle dalla prima alla sesta e per quelle dalla settima
alla dodicesima. In entrambi i casi, le righe si possono completare effettuando
un ragionamento analogo che coinvolge le $3!$ possibili permutazioni semplici
delle versioni di Paul. Possiamo ora applicare il principio fondamentale del
calcolo combinatorio: siccome abbiamo $2!$ modi di riempire le posizioni in
testa e in coda e $3!$ modi per riempire le posizioni centrali, alla singola
configurazione considerata corrispondono $n_1! \cdot n_2! = 2! \cdot 3! = 12$
permutazioni semplici dei cinque oggetti a disposizione.

Il ragionamento che abbiamo fatto non dipende dalla particolare permutazione
con ripetizione che abbiamo analizzato, pertanto a ognuna delle
$P_{5; 2,3}$ permutazioni con ripetizione corrispondono $2! \cdot 3! = 12$
permutazioni semplici, e se consideriamo tutte queste permutazioni con
ripetizione è facile vedere che esse individuano globalmente tutte le
permutazioni semplici. Pertanto deve valere l'uguaglianza
$P_{5; 2,3} \cdot 2! \cdot 3! = 5!$, il che ci permette di ricavare

$$ P_{5; 2,3} = \frac{5!}{2! \cdot 3!} = 10 \enspace. $$

Va notato che $P_{5; 2,3} = \binom{5}{2}$, e in effetti il numero di
permutazioni con ripetizione coincide con il numero di modi in cui si
possono selezionare le due posizioni in cui inserire Kate tra le cinque a
disposizione.

Nel caso generale, avremo $n$ oggetti divisi in $k$ gruppi di numerosità
$n_1, \ldots, n_k$, e ripetendo il ragionamento precedente si ottiene
$n! = P_{n; n_1,\dots, n_k} \cdot n_1! \cdot n_2! \cdot \ldots \cdot n_k!$, che
implica

$$
P_{n; n_1, \dots, n_k} = \frac{n!}{n_1!\cdot n_2! \cdot \ldots \cdot n_k!} \enspace.
$$

La quantità $P_{n; n_1, \dots, n_k}$ è anche detta _coefficiente multinomiale_
e indicata come

$$
P_{n; n_1, \dots, n_k} = \frac{n!}{n_1!\cdot n_2! \cdot \ldots \cdot n_k!}
                       =: \binom{n}{n_1, n_2, \ldots, n_k} \enspace,
$$

in quanto essa rappresenta una generalizzazione del coefficiente binomiale:
in effetti, $\binom{n}{k} = \binom{n}{k, n-k}$ indica in quanti modi è
possibile suddividere $n$ oggetti in due gruppi, rispettivamente contenenti
$k$ e $n-k$ elementi; analogamente $\binom{n}{n_1, \ldots, n_k}$ indica in
quanti modi è possibile suddividere $n$ oggetti in $k$ gruppi nei quali il
primo contiene $n_1$ elementi, il secondo ne contiene $n_2$ e così via.
