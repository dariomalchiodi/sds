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

+++ {"header": true}

<div class="header">
D. Malchiodi, Superhero data science. Vol 1: probabilità e statistica: Calcolo combinatorio.
</div>
<hr style="width: 90%;" align="left" />

+++


<div id="h-0"></div>

# Calcolo combinatorio


<div id="h-1"></div>

## Principio fondamentale del calcolo combinatorio

_Principio fondamentale del calcolo combinatorio_: se ci sono $s_1$ modi per operare una scelta e, per ciascuno di essi, ci sono $s_2$ modi per operare una seconda scelta e, per ciascuno di essi ci sono $s_3$ modi per operare una terza scelta e così via fino a $s_t$ modi per operare la $t$-esima scelta, allora il numero delle sequenze di possibili scelte \`e  $s_1\cdot s_2\cdot s_3\dots s_t$.

Osserviamo che questo risultato corrisponde a calcolare il numero delle foglie di un albero di profondità $t$ il cui primo livello ha $s_1$ nodi, ciascuno dei quali ha $s_2$ figli, ciascuno dei quali ha $s_3$ figli e così via.

<div id="h-2"></div>

## Permutazioni


Consideriamo un insieme di $n$ oggetti $A= \{ a_1,\dots a_n\}$. Chiamiamo _permutazione_ degli $n$ oggetti una sequenza ordinata in cui compaiono tutti gli oggetti.

<div id="h-3"></div>

### Permutazioni semplici

Se gli $n$ oggetti di $A$ sono tutti distinguibili, allora si parla di _permutazione semplice_, o soltanto _permutazione_, degli $n$ oggetti. Ad esempio, se $A= \{ a,b,c \}$ allora tutte le permutazioni degli $n$ oggetti sono:

<table style="font-size: 1rem;">
  <tr>
    <td>a</td>
    <td>b</td>
    <td>c</td>
  </tr>
  <tr>
    <td>c</td>
    <td>a</td>
    <td>b</td>
  </tr>
  <tr>
    <td>b</td>
    <td>c</td>
    <td>a</td>
  </tr>
  <tr>
    <td>b</td>
    <td>a</td>
    <td>c</td>
  </tr>
  <tr>
    <td>c</td>
    <td>b</td>
    <td>a</td>
  </tr>
  <tr>
    <td>a</td>
    <td>c</td>
    <td>b</td>
  </tr>
</table>

Quante sono le permutazioni di $n$ oggetti? Per rispondere a questa domanda applichiamo il principio fondamentale del calcolo combinatorio:

- calcoliamo in quanti modi possiamo selezionare l'oggetto da inserire nella prima posizione: avendo a disposizione $n$ oggetti, abbiamo $n$ possibilità;
- per ciasuna delle $n$ possibili scelte fatte al punto precedente, calcoliamo in quanti modi possiamo selezionare l'oggetto da inserire nella seconda posizione: avendo a disposizione $n-1$ oggetti, abbiamo $n-1$ possibilità; in totale abbiamo $n\dot(n-1)$ modi differenti per scegliere il primo e il secondo elemento della sequenza;
- procediamo in modo analogo per tutte le altre posizioni, creando così un albero il cui livello $i$ corrisponde alla scelta per riempire la posizione $i$-esima; se osserviamo che per riempire la posizione $i$-esima sono rimasti $n-(i-1)$ elementi di $A$ tra cui scegliere, possiamo dire che esistono $n\cdot(n-1)\dots \cdot(n-(i-1))$ modi differenti per scegliere i primi $i$ elementi della sequenza;
- in particolare, arrivati all'ultima posizione, è rimasto un solo elemento di $A$ da scegliere, e abbiamo costruito un albero di profondità $n$ che ha un numero di foglie pari a $n(n-1)(n-2)\dots 1=n!$.

Quindi il numero di possibili permutazioni semplici di $n$ oggetti è $n!$. Nell'esempio visto poc'anzi abbiamo elencato tutte le possibili $3! = 6$ differenti permutazioni degli oggetti di $A$.

<div id="h-4"></div>

### Permutazioni di oggetti distinguibili a gruppi

Se gli $n$ oggetti di $A$ non sono tutti distinguibili, ma sono distinguibili a gruppi di numerosità $n_1, n_2,\dots n_k$ (ovviamente con $\sum_{i=1}^k n_i=n$), allora una sequenza ordinata di tali oggetti che sia distinguibile dalle altre è detta _permutazione di oggetti distinguibili a gruppi_.

Ad esempio, immaginiamo che l'insieme $A= \{ a_1, a_2, b_1, b_2, b_3 \}$ sia costituito da cinque caramelle di cui due (la $a_1$ e la $a_2$) sono al gusto arancia e le altre tre sono al gusto banana. Dal punto di vista del gusto della caramella possiamo identificare due gruppi distinti di oggetti, uno di numerosità $n_1=2$ e l'altro di numerosità  $n_2=3$.  Se ci interessa distinguere le sequenze di caramelle per i gusti che vi compaiono, allora la permutazione $a_1 a_2 b_1 b_2 b_3$ è diversa da $a_1 b_1 b_2 b_3 a_2$, perché nella prima abbiamo due caramelle all'arancia iniziali e poi tre alla banana e nella seconda abbiamo una caramella all'arancia all'inizio e una alla fine della sequenza e le caramelle centrali sono alla banana. Al contrario, la permutazione
$a_1 a_2 b_1 b_2 b_3$ è indistinguibile dalla $a_2 a_1 b_1 b_2 b_3$, perché in entrambe le prime due caramelle sono all'arancia e le restanti tre sono alla banana.

Quante sono dunque le permutazioni di $n$ oggetti distinguibili a gruppi di numerosità $n_1, n_2,\dots n_k$?
Torniamo al nostro esempio e fissiamo una configurazione di gusti, fissiamo cioè le posizioni in cui compare la caramella all'arancia e quelle in cui compare la caramella alla banana, per esempio la posizione 1 e la posizione 5 per l'arancia, la 2, la 3 e la 4 per la banana:

<p style="text-align: center">arancia banana banana banana arancia</p>

In questo caso abbiamo solo due gruppi e quindi, fissate le posizioni di elementi del primo gruppo, automaticamente sono anche fissate quelle degli  elementi del secondo gruppo. Le permutazioni semplici che corrispondono a questa configurazione sono:

<table style="font-size: 1rem;">
<tr><td>$a_1$</td><td>$b_1$</td><td>$b_2$</td><td>$b_3$</td><td>$a_2$</td></tr>
<tr><td>$a_1$</td><td>$b_3$</td><td>$b_1$</td><td>$b_2$</td><td>$a_2$</td></tr>
<tr><td>$a_1$</td><td>$b_2$</td><td>$b_3$</td><td>$b_1$</td><td>$a_2$</td></tr>
<tr><td>$a_1$</td><td>$b_3$</td><td>$b_2$</td><td>$b_1$</td><td>$a_2$</td></tr>
<tr><td>$a_1$</td><td>$b_2$</td><td>$b_1$</td><td>$b_3$</td><td>$a_2$</td></tr>
<tr><td>$a_1$</td><td>$b_1$</td><td>$b_3$</td><td>$b_2$</td><td>$a_2$</td></tr>
<tr><td>$a_2$</td><td>$b_1$</td><td>$b_2$</td><td>$b_3$</td><td>$a_1$</td></tr>
<tr><td>$a_2$</td><td>$b_3$</td><td>$b_1$</td><td>$b_2$</td><td>$a_1$</td></tr>
<tr><td>$a_2$</td><td>$b_2$</td><td>$b_3$</td><td>$b_1$</td><td>$a_1$</td></tr>
<tr><td>$a_2$</td><td>$b_3$</td><td>$b_2$</td><td>$b_1$</td><td>$a_1$</td></tr>
<tr><td>$a_2$</td><td>$b_2$</td><td>$b_1$</td><td>$b_3$</td><td>$a_1$</td></tr>
<tr><td>$a_2$</td><td>$b_1$</td><td>$b_3$</td><td>$b_2$</td><td>$a_1$</td></tr>
</table>

e le abbiamo ottenute lasciando fissati i gusti nelle posizioni scelte e permutando su tali posizioni le caramelle del gusto corrispondente. Utilizzando il principio fondamentale del calcolo combinatorio possiamo dire che alla singola configurazione

<p style="text-align: center;">arancia banana banana banana arancia</p>

corrispondono $n_1! \cdot n_2! = 2! \cdot 3! = 12$ permutazioni semplici.

Se chiamiamo $P_{n; n_1,\dots, n_k}$ il numero di configurazioni differenti e ricordiamo che il numero di permutazioni semplici è $n!$, possiamo scrivere:

\begin{equation}
n! = P_{n; n_1,\dots, n_k} \cdot n_1! \cdot n_2! \dots n_k!,
\end{equation}

da cui segue che il numero delle permutazioni di $n$ oggetti distinguibili a gruppi di numerosità $n_1, n_2,\dots n_k$ è

\begin{equation}
P_{n; n_1, \dots, n_k}=\frac{n!}{n_1!\cdot n_2! \dots n_k!}=\binom{n}{n_1!, n_2!, \dots, n_k!}.
\end{equation}

Questa quantità è detta anche _coefficiente multinomiale_.

+++

<div id="h-5"></div>

## Disposizioni e combinazioni

Consideriamo un insieme di $n$ oggetti distinti $A= \{ a_1,\dots a_n \}$ e selezioniamo $k$ oggetti di questo insieme. Le modalit\`a di selezione possono essere svariate.

- Se vogliamo distinguere le configurazioni contenenti gli stessi oggetti ma estratti in ordine differente allora pariamo di _disposizioni di $n$ oggetti su k posti_, che sono configurazioni in cui sono importanti sia l'oggetto selezionato che la sua posizione. Specifichiamo una disposizione indicando tra parentesi tonde gli oggetti estratti. Ad esempio, fissato $k=3$, la disposizione $(a_i, a_j, a_r)$ è diversa dalla disposizione $(a_r, a_j, a_i)$ perché, sebbene gli oggetti selezionati siano gli stessi, essi compaiono in ordine differente.

- Se invece siamo solo interessati a quali oggetti sono stati estratti e non alla loro posizione nella sequenza, allora pariamo di _combinazioni di $n$ oggetti presi $k$ alla volta_. Specifichiamo una combinazione indicando tra parentesi graffe gli oggetti estratti. Ad esempio, fissato $k=3$, $\{ a_i, a_j, a_r \}$ e $\{ a_r, a_j, a_i \}$ sono la stessa combinazione.

Inoltre:

- Se gli oggetti di $A$ possono essere usati una sola volta, allora parliamo di disposizioni o combinazioni _senza ripetizione_. Gli esempi di disposizioni o combinazioni visti sopra sono senza ripetizione.

- Se invece immaginiamo che nel selezionare ciascuno dei $k$ oggetti abbiamo a disposizione sempre l'insieme $A$ completo, e quindi il singolo oggetto $a_i$ può essere selezionato anche più di una volta, allora parliamo di disposizioni o combinazioni _con ripetizione_. Ad esempio, fissato $k=3$, la sequenza $(a_r, a_i, a_i)$ è una disposizione con ripetizione perché l'oggetto $a_i$ ricorre due volte, e analogamente  $\{a_r, a_i, a_i\}$ è una combinazione con ripetizione.

Abbiamo dunque quattro possibili modi di selezionare $k$ oggetti da un insieme di $n$ oggetti, che corrispondono a quattro tipi di configurazioni diverse:

- le _disposizioni senza ripetizione_, dette anche _disposizioni semplici_, che richiedono ovviamente che sia $k\leq n$,

- le _combinazioni senza ripetizione_, dette anche _combinazioni semplici_, con $k\leq n$,

- le _disposizioni con ripetizione_,

- le _combinazioni con ripetizione_.

Vediamo ora come calcolare, data una particolare modalità di selezione, il numero di possibili scelte distinte.

- Per calcolare il numero $d_{n, k}$ di possibili _disposizioni senza ripetizione di $n$ oggetti distinti su $k$ posti_ procediamo in modo analogo a quanto fatto per le permutazioni semplici, fermandoci però alla posizione $k$-esima. L'albero costruito ha profondità $k$ e un numero di foglie pari a:

\begin{align}
d_{n, k} &= n (n-1) (n-2) \dots (n-k+1) \\
         &= n (n-1) (n-2) \dots (n-k+1) \cdot \left(\frac{(n-k)(n-k-1)\dots1}{(n-k)(n-k-1)\dots1}\right) \\
         &=\frac{n!}{(n-k)!}.
\end{align}

- Si osservi che, per $k=n$, nella disposizione si utilizzano tutti gli elementi di $A$, quindi le permutazioni semplici sono un caso particolare di disposizioni semplici.

- Per calcolare il numero $c_{n, k}$ di possibili _combinazioni senza ripetizione di $n$ oggetti distinti presi $k$ alla volta_ osserviamo che, fissati $k$ oggetti, alla combinazione contenente quei $k$ oggetti corrispondono $k!$ distinte disposizioni contenenti gli stessi $k$ oggetti. Quindi il numero totale di disposizioni semplici è uguale al numero di combinazioni moltiplicato per $k!$, cioè $d_{n,k} = c_{n,k} \cdot k!$, da cui segue che

\begin{equation}
c_{n, k} = \frac{d_{n, k}}{k}! = \frac{n!}{(n-k)!k!} =\binom{n}{k}
\end{equation}

- Per calcolare il numero $D_{n, k}$ di possibili _disposizioni con ripetizione di $n$ oggetti distinti su $k$ posti_ procediamo in modo analogo a quanto fatto per le disposizioni senza ripetizione, tenendo presente però che in ciascun nodo dell'albero abbiamo sempre $n$ possibili oggetti tra i quali scegliere, mentre la profondità dell'albero è, come in quel caso, ancora $k$. Quindi avremo

\begin{equation}
D_{n, k} = \underbrace{n \cdot n \dots \cdot n}_{k \text{ volte}} = n^k.
\end{equation}

- Si potrebbe infine dimostrare (ma non lo faremo) che il numero  $C_{n,k}$ di _combinazioni con ripetizione di $n$ oggetti distinti presi $k$ alla volta_ è

\begin{equation}
C_{n, k} = \binom{n+k-1}{k}
\end{equation}

La Tabella seguente contiene uno schema riassuntivo dei casi considerati.

<table style="font-size: 1rem;">
    <tr>
        <th></th>
        <th>sequenze (ordinate)</th>
        <th>insiemi (non ordinati) </th>
    </tr>
    <tr>
        <th>senza ripetizione</th>
        <td>DISPOSIZIONI: $d_{n,k}=\frac{n!}{(n-k)!}$</td>
        <td>COMBINAZIONI: $c_{n,k}=\binom{n}{k}$</td>
    </tr>
    <tr>
        <th>con ripetizione </th>
        <td>DISPOSIZIONI: $D_{n,k}=n^k$</td>
        <td>COMBINAZIONI: $C_{n,k}=\binom{n+k-1}{k}$</td>
    </tr>
</table>
        


+++

<div id="h-6"></div>

## Esercizi

<div id="h-7"></div>

### Esercizio 1

Dato l'insieme $A = \{ a_1,\dots a_n\}$ e indicato con $\mathcal{P}(A)$ l'insieme delle parti di $A$, calcolare la cardinalità di $\mathcal{P}(A)$.

_Soluzione 1_

Ricordiamo che l'insieme delle parti $\mathcal{P}(A)$ è l'insieme di tutti i sottinsiemi propri e impropri di $A$: contiene l'insieme vuoto, tutti i sottinsiemi costituiti da un solo elemento di $A$, tutti i sottinsiemi costituiti da due soli elementi di $A$ e così via, e contiene anche $A$ stesso.

Siccome il numero di sottinsiemi costituiti da $k$ elementi è $c_{n,k}=\binom{n}{k}$, si ha  che la cardinalità di $\mathcal{P}(A)$ è $|\mathcal{P}(A)| = 1 + \sum_{k=1}^{n} \binom{n}{k}$, dove il primo addendo è dovuto alla presenza dell'insieme vuoto. Sfruttando le propriet\`a del coefficiente binomiale otteniamo

\begin{equation}
|\mathcal{P}(A)| = \sum_{k=0}^{n} \binom{n}{k} = \sum_{k=0}^{n}\binom{n}{k} 1^k 1^{n-k} = 2^n,
\end{equation}

dove nell'ultimo passaggio abbiamo utilizzato la formula del binomio di Newton: $(a+b)^n = \sum_{k=0}^{n}\binom{n}{k}a^k b^{n-k}$, ponendo $a=1$ e $b=1$.

_Soluzione 2_

Se rappresentiamo ogni sottinsieme $S$ di $A$ come una $n$-upla di elementi binari in cui nella posizione $i$-esima compare il simbolo $1$ se l'elemento $a_i$ appartiene a $S$  e il simbolo $0$ se l'elemento $a_i$ non  vi appartiene, allora l'insieme delle parti $\mathcal{P}(A)$ è l'insieme di tutte le $n$-uple che possiamo costruire a partire dai due simboli $0$ e $1$. Quindi

\begin{equation}
|\mathcal{P}(A)| = D_{n,2}=2^n.
\end{equation}

<div id="h-8"></div>

### Esercizio 2

Quanti numeri telefonici di 7 cifre tutte diverse si possono avere?

_Soluzione_: $d_{10,7} = 604800$.

<div id="h-9"></div>

### Esercizio 3

Quante combinazioni di numeri si posso ottenere lanciando 3 dadi?

_Soluzione_: $C_{6,3} = 56$.

<div id="h-10"></div>

### Esercizio 4

In quanti modi lanciando 3 dadi possono uscire facce tutte diverse?

_Soluzione_: $d_{6,3}=120$ se i dadi sono tra loro distinguibili e $c_{6,3}=20$ se questi non sono distinguibili.

<div id="h-11"></div>

### Esercizio 5

Quanti sono gli anagrammi della parola ROMA?

_Soluzione_: le permutazioni semplici $d_{4,4} = 24$.

<div id="h-12"></div>

### Esercizio 6

Quanti sono gli anagrammi della parola MATEMATICA?

_Soluzione_: le permutazioni di oggetti distinguibili a gruppi $P_{10; 3, 2, 2, 1, 1, 1} = 151200$.

<div id="h-13"></div>

### Esercizio 7

In quanti modi 3 persone possono occupare 4 posti numerati?

_Soluzione_: nel numero di modi in cui posso assegnare $4$ posti a $3$ persone: $d_{4, 3} = 24$.

+++

<div id="h-14"></div>

## Generazione di disposizioni, permutazioni e combinazioni

In python è abbastanza facile generare tutte le possibili disposizioni con ripetizione degli elementi in una lista in $k$ posti: basta eseguire una list comprehension per ottenere una lista i cui elementi sono $k$-ple, e gli elementi di queste $k$-ple si ottengono iterando $k$ volte sulla lista di partenza. Per esempio la cella seguente permette di generare tutte le $D'_{3, 2} = 9$ coppie con ripetizione a partire da una lista di tre elementi

```{code-cell} ipython3
l = range(3)

disp_rep = [(l1, l2) for l1 in l for l2 in l]
disp_rep
```

Le disposizioni senza ripetizione si ottengono facilmente a partire da quelle con ripetizione: è sufficiente effettuare un'ulteriore list comprehension che ha il solo scopo di eliminare tutte le disposizioni che contengono uno stesso elemento più volte. Tale controllo si può effettuare verificando che l'insieme ottenuto a partire da una disposizione abbia lo stesso numero di elementi della disposizione stessa. Nella cella seguente utilizziamo questa tecnica per ottenere tutte le $D_{3, 2} = 6$ coppie senza ripetizione a partire dalla stessa lista precedentemente considerata.

```{code-cell} ipython3
l = range(3)

disp_rep = [(l1, l2) for l1 in l for l2 in l]
disp_norep = [d for d in disp_rep if len(d)==len(set(d))]
disp_norep
```

Le permutazioni rappresentano un caso particolare delle disposizioni senza ripetizione, in cui il numero di posti è uguale al numero di oggetti. Pertanto si può adattare facilmente il codice della cella precedente per generare, per esempio, tutte le $P_3 = 6$ permutazioni della lista considerata.

```{code-cell} ipython3
l = range(3)

disp_rep = [(l1, l2, l3) for l1 in l for l2 in l for l3 in l]
perm = [d for d in disp_rep if len(d)==len(set(d))]
perm
```

La generazione di combinazioni è più complicata: si procede nello stesso modo visto per le disposizioni senza ripetizione, ma la seconda list comprehension non si limita a filtrare le coppie, bensì le trasforma anche in insiemi (tecnicamente, in istanze di `frozenset` che corrispondono a insiemi immutabili). Il risultato conterrà dei doppioni: per esempio le disposizioni $(a, b)$ e $(b, a)$ verrebbero trasformate nello stesso insieme. Per eliminare questi doppioni è sufficiente inserire tutti i risultati in un nuovo insieme. Già che ci siamo, possiamo trasformare tutti i `frozenset` ottenuti in normali insiemi, come nella cella seguente dove vengono costruite tutte le $C_{4, 2} = 6$ combinazioni di quattro elementi in due posti.

```{code-cell} ipython3
l = range(4)

disp_rep = [(l1, l2) for l1 in l for l2 in l]
comb = [frozenset(d) for d in disp_rep if len(d)==len(set(d))]
list(map(set, set(comb)))
```

<div class="alert alert-info">
L'uso di `frozenset` nella cella precedente è fondamentale per poter eseguire l'ultima istruzione. Gli elementi che si inseriscono in un insieme (ma lo stesso varrebbe per le chiavi di un dizionario) devono essere infatti immutabili: ciò è legato agli algoritmi che vengono utilizzati per inserire gli elementi di un insieme in un'opportuna struttura dati che permetta di verificare successivamente se un generico elemento appartiene oppure no all'insieme.
</div>

+++

Le generazioni di disposizioni, combinazioni e permutazioni fatte finora richiedono di fissare il numero di posti: non sarebbe altrimenti possibile scrivere le list comprehension alla base della costruzione delle disposizioni, che rappresentano il mattone fondamentale per ottenere tutti gli altri oggetti. Il modulo `itertools` contiene funzioni che permettono di superare questo ostacolo. Nella fattispecie:

- `product` permette di generare le disposizioni con ripetizione, specificando la lista dei valori come primo elemento e il numero di posti tramite l'argomento opzionale `repeat`:

```{code-cell} ipython3
import itertools
list(itertools.product(range(3), repeat=2))
```

- `permutations` genera le disposizioni senza ripetizioni e le permutazioni:

```{code-cell} ipython3
list(itertools.permutations(range(3), 2))
```

```{code-cell} ipython3
list(itertools.permutations(range(3), 3))
```

- `combinations` genera infine le combinazioni:

```{code-cell} ipython3
list(itertools.combinations(range(4), 2))
```

<div class="alert alert-info">
Le funzioni di `itertools` che abbiamo considerato non restituiscono delle liste, bensì degli speciali oggetti che è necessario convertire esplicitamente in liste utilizzando la funzione `list`.
</div>

+++

[try me!](Untitled5.ipynb#altra)

+++ {"footer": true}

<hr style="width: 90%;" align="left" />
<span style="font-size: 0.8rem;">D. Malchiodi, Superhero data science. Vol 1: probabilità e statistica: Calcolo combinatorio, 2017.</span>
<br>
<span style="font-size: 0.8rem;">Powered by <img src="img/jupyter-logo.png" style="height: 1rem; display: inline; margin-left: 0.5ex; margin-top: 0;" alt="Jupyter Notebook"></span>
<div style="float: left; margin-top: 1ex;">
<img src="http://mirrors.creativecommons.org/presskit/icons/cc.large.png" style="width: 1.5em; float: left; margin-right: 0.6ex; margin-top: 0;">
<img src="http://mirrors.creativecommons.org/presskit/icons/by.large.png" style="width: 1.5em; float: left; margin-right: 0.6ex; margin-top: 0;">
<img src="http://mirrors.creativecommons.org/presskit/icons/nc.large.png" style="width: 1.5em; float: left; margin-right: 0.6ex; margin-top: 0;">
<img src="http://mirrors.creativecommons.org/presskit/icons/nd.large.png" style="width: 1.5em; float: left; margin-right: 0.6ex; margin-top: 0;">
<span style="font-size: 0.7rem; line-height: 0.7rem; vertical-align: middle;">Quest'opera è distribuita con Licenza <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribuzione - Non commerciale - Non opere derivate 4.0 Internazionale</a></span>.
</div>
