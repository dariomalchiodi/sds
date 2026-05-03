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

(sec_permutazioni)=
# Permutazioni

Una _permutazione_ di $n$ oggetti è, in sostanza, un elenco ordinato che
contiene ognuno di essi una e una sola volta. In italiano, d'altronde,
_permutare_ è sinonimo di _scambiare_, o _riordinare_. In questo contesto, le
configurazioni considerate dipendono strettamente dall'ordine degli elementi, e
non è permesso il riutilizzo di uno stesso oggetto. In altri termini, si tratta
di disporre $n$ oggetti in altrettanti posti disponibili. Ciò equivale a
fissare un criterio per ordinare gli oggetti, per poi elencarli dal «più
piccolo» al «più grande».

Per calcolare il numero di permutazioni possibili dobbiamo distinguere tra due
situazioni:

- nella prima, gli oggetti sono tutti diversi,
- nella seconda, esistono oggetti differenti che sono però indistinguibili tra
  loro.

A seconda dei due casi, si parla di permutazioni _semplici_ o _con 
ipetizione_, che approfondiamo di seguito.

## Permutazioni semplici

Quando gli oggetti da permutare sono gli elementi di un insieme, per
definizione sono tutti diversi, cioè distinguibili tra loro. In questo caso si
parla di _permutazione semplice_ (o più brevemente di _permutazione_) come
descritto dalla seguente definizione.

````{prf:definition} Permutazione semplice
:label: def-permutazione-semplice

Consideriamo un insieme $A = \{ a_1,\dots a_n \}$ contenente $n$ oggetti.
Chiamiamo _permutazione semplice_ (_permutazione_) di questi oggetti una
qualsiasi sequenza ordinata

```{math}
(a_{i_1}, \dots, a_{i_n}), \quad
1 \leq i_j \leq n \ \forall j \in \{1, \dots, n \}, \quad
i_h \neq i_k \ \forall h \neq k
```

in cui compaiono tutti e soli gli $n$ elementi di $A$. Indichiamo con
$p_n$ il numero di tali permutazioni semplici.
````

In generale, descriverò una permutazione elencando i suoi elementi nell'ordine
corrispondente, separati da virgole e racchiundendo l'elenco tra parentesi
tonde. Vale la pena osservare che, partendo da una permutazione semplice, è
sufficiente scambiare tra loro due elementi qualsiasi per ottenerne una nuova.

````{prf:example} I Fantastici 4
:label: ex-fantastic-4
Consideriamo l'insieme $Q = \{ f, i, t, c \}$ dei Fantastici 4: mister
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

Il principio fondamentale del calcolo combinatorio ci aiuta a calcolare
facilmente il numero $p_n$ di differenti permutazioni di $n$ oggetti:

- l'oggetto da mettere nella prima posizione dell'elenco si può selezionare in
  $n$ modi diversi, potendo scegliere tra tutti gli oggetti disponibili;
- la seconda posizione può essere occupata da $n-1$ oggetti distinti, in
  quanto non è possibile considerare quello utilizzato al punto precedente,
  così che esistono $n \cdot (n-1)$ modi differenti per scegliere i primi due
  elementi della sequenza;
- procedendo analogamente per ogni posizione successiva, il numero di opzioni
  diminuisce di un'unità a ogni passo, creando così un albero in cui il livello
  $i$ è associato alla $i$-esima posizione; per riempire questa posizione, sono
  rimasti $n-(i-1)$ elementi di $A$ tra cui scegliere, dunque vi sono
  $n\cdot(n-1) \cdot \ldots \cdot(n-(i-1))$ modi possibili per elencare i
  primi $i$ elementi della sequenza;
- arrivati all'ultima posizione, va obbliagatoriamente scelto l'unico elemento
  di $A$ rimasto disponibile.
  
Si può quindi costruire un albero di profondità $n$ che ha un numero di
foglie pari a $n(n-1)(n-2)\ldots 1=n!$, ognuna delle quali corrisponde a una
delle possibili permutazioni semplici. Riassumendo, il numero di permutazioni
di $n$ oggetti è uguale a $p_n = n!$. Guardando ad esempio la
{numref}`permutazioni-fantastici-quattro`, si verifica facilmente che essa
contiene tutte le possibili $4! = 24$ permutazioni dei quattro oggetti
dell'insieme $Q$ introdotto nell’{prf:ref}`ex-fantastic-4`.


## Permutazioni con ripetizione

Consideriamo ora il caso in cui alcuni degli oggetti da permutare siano
indistinguibili, ma restino _distinguibili a gruppi_. Più precisamente,

- esistono $r \in \mathbb N$ versioni possibili per gli oggetti, che possiamo
  indicare come $a_1, \ldots, a_r$, e
- per ogni $j = 1, \dots, r$, la versione $a_j$ è ripetuta $n_j$ volte (il che
  implica $\sum_{j=1}^r n_j = n$).

Per ogni versione $a_j$ esiste dunque un gruppo di oggetti indistinguibili la
cui numerosità è $n_j$. Questi oggetti formano un
_multiinsieme_ (una collezione non ordinata in cui ogni elemento può comparire
una o più volte) che contiene $n_1$ occorrenze della versione $a_1$, $n_2$
occorrenze di $a_2$ e così via. Riassumendo, possiamo scrivere gli elementi di
questo multiinsieme uno dopo l'altro ottenendo la sequenza

```{math}
\underbrace{a_1, \ldots, a_1}_{n_1 \text{volte}},
\underbrace{a_2, \ldots, a_2}_{n_2 \text{volte}}, \ldots,
\underbrace{a_r, \ldots, a_r}_{n_r \text{volte}} \enspace.
```

Cambiando l'ordine degli elementi, non sempre si ottiene una sequenza
diversa: infatti, se si scambiasse la posizione di due oggetti indistinguibili
la sequenza resterebbe invariata. In queste situazioni si considerano solo le
permutazioni che producono sequenze effettivamente distinguibili, come
descritto dalla definizione che segue.

````{prf:definition} Permutazione con ripetizione
:label: def-permutation-repetition

Consideriamo un multiinsieme $A = \{ a_1,\dots a_n \}$ contenente $n$ oggetti
distinguibili a gruppi di numerosità $n_1, \ldots, n_r$. Una _permutazione di
oggetti distinguibili a gruppi_ (più semplicemente, _permutazione con
ripetizione_) di questi oggetti una qualsiasi loro sequenza ordinata che sia
distinguibile dalle altre, e indichiamo con $P_{n; n_1, \ldots, n_r}$ il numero
di tali configurazioni.
````

Indicherò le permutazioni con ripetizione usando la medesima sintassi di
quelle semplici, separando dunque i loro elementi con virgole e usando delle
parentesi tonde come delimitatori.

````{prf:example} Dupli-Kate e Multi-Paul
:label: dupli-kate-multi-paul
Consideriamo i gemelli
[Kate](https://comicvine.gamespot.com/dupli-kate/4005-41136/) e
[Paul Cha](https://comicvine.gamespot.com/multi-paul/4005-48737/) che appaiono
in [Invincible](https://comicvine.gamespot.com/invincible/4050-150390/).
Entrambi sono dotati del potere di autoreplicarsi a piacimento e noti come
Dupli-Kate e Multi-Paul. In particolare, ogni versione di Dupli-Kate è
contrassegnata da un numero intero progressivo che compare sul suo costume,
così che possiamo indicare con $k_1$, $k_2$ e così via i suoi cloni presenti
in un dato momento. Immaginiamo che lo stesso valga per Multi-Paul,
le cui repliche indicheremo con $p_1, p_2, \ldots$, e che di fronte a noi ci
siano due versioni di Kate e tre di Paul, così che il quintetto risultante
sia descritto dal multiinsieme $A= \{ k_1, k_2, p_1, p_2, p_3 \}$.

Per calcolare in quanti modi si possano mettere in fila queste cinque
versioni di Kate e Paul senza tenere conto del loro numero progressivo, bisogna
ricavare il numero di permutazioni con ripetizione di $n = 5$ oggetti divisi in
due gruppi distinti: uno che comprende le $n_1 = 2$ copie di Kate e un altro
con $n_2 = 3$ cloni Paul. In questo contesto,
$(k_1, k_2, p_1, p_2, p_3)$ e $(k_2, k_1, p_1, p_2, p_3)$ indicano due
diverse permutazioni semplici a cui corrisponde però la stessa permutazione
con ripetizione: nelle prime due posizioni compare Kate, nelle ultime tre
compare Paul. Al contrario, $(k_1, k_2, p_1, p_2, p_3)$ e $(k_1, p_1, k_2,
p_2, p_3)$ indicano permutazioni con ripetizione differenti, perché nel primo
caso la seconda posizione è occupata da Kate e la terza da Paul, mentre nel
secondo accade il contrario.
````

Prima di calcolare il numero totale di permutazioni con ripetizione di $n$
oggetti distinguibili a gruppi di numerosità $n_1, n_2,\dots n_r$, analizziamo
preliminarmente il caso particolare dell’{prf:ref}`dupli-kate-multi-paul`.
```{margin}
Fissare le posizioni delle copie di Kate determina in questo caso anche quelle
delle copie di Paul.
```
Concentriamoci su di una possibile permutazione con ripetizione, stabilendo
le posizioni di Kate e quelle di Paul. Per esempio, ipotizziamo che la prima e 
'ultima posizione siano dedicate a Kate e quelle rimanenti a Paul:

<p style="text-align: center">Kate Paul Paul Paul Kate</p>

Ora, a questa permutazione con ripetizione corrispondono varie permutazioni
semplici di cinque oggetti (le due copie di Kate e le tre di Paul). La
{numref}`permutazioni-oggetti-indistinguibili` elenca tutti le permutazioni in
cui Kate si trova agli estremi della fila, cioè nella permutazione con
ripetizione che abbiamo fissato.

```{table} Possibili permutazioni semplici di oggetti in due gruppi distinguibili contenenti rispettivamente due duplicati $k_1$ e $k_2$ di Kate e tre duplicati $p_1$, $p_2$ e $p_3$ di Paul, in modo che Kate si trovi nella prima e nell'ultima posizione.
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
alla dodicesima. In entrambi i casi, le righe si completano con un
ragionamento analogo che coinvolge le $3!$ possibili permutazioni semplici
delle versioni di Paul. Possiamo allora applicare il principio fondamentale
del calcolo combinatorio: siccome abbiamo $2!$ modi di riempire le posizioni
in testa e in coda e $3!$ modi per riempire le posizioni centrali, alla
singola configurazione considerata corrispondono $n_1! \cdot n_2! = 2! \cdot
3! = 12$ permutazioni semplici dei cinque oggetti a disposizione.

Questo ragionamento non dipende dalla particolare permutazione con
ripetizione che abbiamo analizzato: a ognuna delle $P_{5; 2,3}$ permutazioni
con ripetizione corrispondono $2! \cdot 3! = 12$ permutazioni semplici, e se
le consideriamo tutte è facile vedere che, nel loro insieme, individuano la
totalità delle permutazioni semplici. Pertanto deve valere l'uguaglianza
$P_{5; 2,3} \cdot 2! \cdot 3! = 5!$, il che ci permette di ricavare

```{math}
P_{5; 2,3} = \frac{5!}{2! \cdot 3!} = 10 \enspace.
```

Va notato che $P_{5; 2,3} = \binom{5}{2}$, e in effetti il numero di
permutazioni con ripetizione coincide con il numero di modi in cui si
possono selezionare le due posizioni in cui inserire Kate tra le cinque a
disposizione.

Nel caso generale, avremo $n$ oggetti divisi in $r$ gruppi di numerosità
$n_1, \ldots, n_r$, e ripetendo il ragionamento precedente si ottiene
$n! = P_{n; n_1,\dots, n_r} \cdot n_1! \cdot n_2! \cdot \ldots \cdot n_r!$, che
implica

```{math}
:label: eq-permutazioni-ripetizione

P_{n; n_1, \dots, n_r} = \frac{n!}{n_1!\cdot n_2! \cdot \ldots \cdot n_r!}
\enspace.
```

La quantità $P_{n; n_1, \dots, n_r}$ è anche detta _coefficiente multinomiale_
e indicata come

```{math}
P_{n; n_1, \dots, n_r} = \frac{n!}{n_1!\cdot n_2! \cdot \ldots \cdot n_r!}
                       \triangleq \binom{n}{n_1, n_2, \ldots, n_r} \enspace,
```

perché rappresenta una generalizzazione del coefficiente binomiale:
in effetti, $\binom{n}{k} = \binom{n}{k, n-k}$ indica in quanti modi è
possibile suddividere $n$ oggetti in due gruppi, rispettivamente contenenti
$k$ e $n-k$ elementi; analogamente $\binom{n}{n_1, \ldots, n_r}$ indica in
quanti modi è possibile suddividere $n$ oggetti in $r$ gruppi nei quali il
primo contiene $n_1$ elementi, il secondo ne contiene $n_2$ e così via.

## Esercizi

````{exercise} ••
:label: ex-perm-xmen-storico

Gli [X-Men](https://marvel.fandom.com/wiki/X-Men) nella formazione originale
sono cinque: Ciclope, Marvel Girl, Bestia, Angelo e Uomo Ghiaccio. In quanti
modi si possono disporre in fila in modo che Ciclope sia sempre in testa (come
leader della squadra)?
````
````{solution} ex-perm-xmen-storico
:class: dropdown

Se Ciclope deve stare in prima posizione, i rimanenti quattro eroi possono
occupare le restanti quattro posizioni in $p_4 = 4! = 24$ modi.
````

````{exercise} ••
:label: ex-perm-thunderbolts

I [Thunderbolts](https://marvel.fandom.com/wiki/Thunderbolts) originali sono
stati formati da Citizen V, criminale sotto falso nome che aveva convinto altri
cinque cattivi a cambiare identità e fingere di essere degli eroi. Al gruppo
si era poi aggiunta Jolt, ignara di questo inganno. In quanti modi si possono
disporre in fila tutti i membri del gruppo, in modo che i cinque ex cattivi
originariamente convocati occupino le prime posizioni?
````
````{solution} ex-perm-thunderbolts
:class: dropdown

I cinque ex cattivi possono occupare le prime posizioni in
$p_5 = 5! = 120$ modi, e &mdsh; per ognuno di questi ordinamenti &mdash; i due
membri rimasti possono occupare le ultime posizioni in $p_2 = 2! = 2$ modi. Per
il principio fondamentale, il numero di configurazioni possibili è
$120 \cdot 2 = 240$.
````

````{exercise} ••
:label: ex-perm-sinistri-sei

In quanti modi i [Sinistri Sei](https://marvel.fandom.com/wiki/Sinister_Six)
(Doctor Octopus, Avvoltoio, Electro, Mysterio, Kraven il Cacciatore e Uomo
Sabbia) possono occupare altrettante sedie, in modo che Doctor Octopus ed
Electro non siano mai uno accanto all'altro?
````
````{solution} ex-perm-sinistri-sei
:class: dropdown

A ogni abbinamento dei personaggi alle sedie corrisponde una particolare
permutazione dei Sei Sinistri, ma non tutte le permutazioni sono da
considerare. Per risolvere questo problema, conviene ragionare in modo
complementare, sottraendo dalle $p_6 = 6! = 720$ permutazioni tutte quelle in
cui Doctor Octopus ed Electro sono vicini. Il conteggio di queste ultime si
effettua considerando i due cattivi come un blocco unico, ottenendo cinque
oggetti (quattro personaggi, più la coppia) da permutare in $p_5 = 5! = 120$
modi; bisogna però tener conto del fatto che scambiando i due elementi della
coppia si ottengono due diverse permutazioni tra quelle originali, quindi ci
sono $240$ modi di piazzare Doctor Octopus ed Electro uno accanto all'altro.
Concludendo, ci sono $720 - 240 = 480$ disposizioni accettabili.
````

````{exercise} ••
:label: ex-perm-legione-dei-sostituti

La [Legione degli Eroi
Sostituiti](https://malchiodi.com/sds/short/sustitute-heroes) comprende Polar
Boy, Night Girl, Fire Lad, Stone Boy e Chlorophyll Kid. Le loro classifiche
settimanali di potenza vengono stilate nel modo seguente: Night Girl e Polar
Boy si trovano sempre nelle prime due posizioni (in un ordine qualsiasi),
mentre Stone Boy è sempre l'ultimo. In quanti modi distinti può essere
compilata una classifica?
````
````{solution} ex-perm-legione-dei-sostituti
:class: dropdown

Stone Boy deve apparire sempre all'ultimo posto, quindi il numero di
classifiche si ottiene applicando il principio fondamentale del
calcolo combinatorio, moltiplicando:

- i $p_2 = 2! = 2$ modi nei quali Night Girl e Polar Boy possono occupare le
  prime due posizioni, e
- i $p_2 = 2$ modi possiili di distribuire Fire Lad e Chlorophyll Kid nelle
  nelle rimanenti posizioni centrali.

Risulta perciò possibile stilare la classifica in quattro modi distinti.
````

````{exercise} ••
:label: ex-perm-invincible-multiinsieme

Iron Man, Capitan America e la Donna Invisibile hanno un'identità che è nota a
tutti; al contrario, Daredavil, Spider-Man e Ant-Man operano nell'anonimato.
Se consideriamo indistinguibili tra loro i supereroi con identità pubblica, e analogamente quelli con identità segreta, in quanti modi distinti è possibile ordinarli?
````
````{solution} ex-perm-invincible-multiinsieme
:class: dropdown

In questo caso, bisogna considerare le permutazioni di sette oggetti,
organizzati in due gruppi di tre e quattro eroi indistinguibili. Applicando
la formula {eq}`eq-permutazioni-ripetizione`, si ottiene

```{math}
P_{7;\,3,4} = \frac{7!}{3!\cdot 4!} = \binom{7}{3} = 35 \enspace.
```
````

````{exercise} ••
:label: ex-perm-anagrammi-superman

In quanti modi si possono formare gli anagrammi della parola
SUPERMAN, intendendo per anagramma una qualunque riorganizzazione delle
lettere della parola di partenza, anche quando il risultato ottenuto non
ha significato?
````
````{solution} ex-perm-anagrammi-superman
:class: dropdown

SUPERMAN è una parola che contiene otto lettere, tutte diverse tra loro. Il
numero di anagrammi coincide quindi con il numero di permutazioni semplici di
$8$ oggetti, che è uguale a $p_8 = 8! = 40\,320$.
````

````{exercise} ••
:label: ex-perm-anagrammi-antman

In quanti modi si possono formare gli anagrammi della parola ANTMAN, nella
stessa accezione dell'esercizio precedente?
````
````{solution} ex-perm-anagrammi-antman
:class: dropdown

La parola ANTMAN contiene sei lettere, due delle quali occorrono in due
diverse posizioni. Il numero di anagrammi distinti è quindi una permutazione
con ripetizione: più precisamente, T e M appartengono ognuna a un gruppo con
molteplicità $1$, mentre A ed N fanno riferimento a due gruppi con molteplicità
$2$. Pertanto il numero di anagrammi distinti è

```{math}
P_{6;\,2,2,1,1} = \frac{6!}{2!\cdot 2!\cdot 1!\cdot 1!} = \frac{720}{4} = 180
\enspace.
```
````

````{exercise} •••
:label: ex-perm-justice-society

Nella sua formazione originale, la [Justice Society of
America](https://dc.fandom.com/wiki/Justice_Society_of_America_(New_Earth))
schiera una formazione di otto eroi: tre con poteri magici o alieni (Lanterna
Verde, Spettro e Dottor Fate), tre che utilizzano tecnologie segrete (Atomo,
Hourman e Flash) e due che fanno uso di tecnologie note e facilmente
riconoscibili (Sandman e Hawkman). In quanti modi possono intervenire uno dopo
l’altro in battaglia, mantenendo sempre consecutivi gli eroi della stessa
categoria?
````
````{solution} ex-perm-justice-society
:class: dropdown

Immaginiamo di fare intervenire prima tutti gli eroi con poteri magici, poi
quelli che usano tecnologie segrete e infine quelli rimanenti. Siccome i primi
due gruppi possono essere permutati in $p_3 = 3!$ modi e il terzo si può
ordinare in $p_2 = 2!$ configurazioni, Per il principio fondamentale del
calcolo combinatorio, esistono quindi $6 \cdot 6 \cdot 2 = 72$ modi di
interventire. Se modificassimo l'ordine dei gruppi, il risultato sarebbe lo
stesso. Quindi il risultato si ottiene moltiplicando $72$ per il numero di
permutazioni dei gruppi, che è $p_3 = 3!$. Concludendo, vi saranno $432$
diversi modi di fare intervenire i membri della Justice Society, uno dopo
l'altro.
````




