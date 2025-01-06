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
numbering:
  heading_1: true
  heading_2: false
  enumerator: 2.2.%s

title: 2.2. Dati strutturati
---

Come indicato nel Paragrafo @sec:tipi-semplici-e-strutturati, ho deciso di
definire un tipo di dati come strutturato se i corrispondenti valori
costituiscono un'aggregazione di più tipi di dati __ed__ è possibile iterare
automaticamente sui loro contenuti. Dopo aver spiegato meglio questo concetto,
in questo paragrafo elencherò i tipi strutturati usati maggiormente in Python, 
descrivendo le corrispondenti classi e alcuni aspetti speciali della sintassi
che permettono di accedere ai loro contenuti.

```{admonition} Nomenclatura
Il generico valore di un tipo di dati strutturato è memorizzato appoggiandosi
su di una _struttura dati_, intesa come metodo che permette di organizzare
un particolare tipo di informazione all'interno di un computer. Questo tende
a creare confusione nella terminologia, anche perché sebbene a volte i due
concetti si sovrappongono (come capita per esempio con gli _array_),
normalmente questo non succede. Anzi, di norma è possibile costruire un
medesimo tipo di dati strutturato usando strutture dati diverse: per esempio,
un insieme è un tipo di dati strutturato che può essere basato su un _array_
così come su un albero (sebbene la scelta tra queste due strutture dati abbia
un impatto sull'_efficienza_ delle operazioni che si possono eseguire
sull'insieme). Siccome questo libro non parla delle strutture dati, e tenuto
conto del fatto che la dicitura «generico valore di un tipo di dati
strutturato» è decisamente prolissa, al suo posto userò occasionalmente il
termine _struttura_, confidando che questo non causi confusione in chi
legge.
```

I tipi di dati strutturati che descrivo nei prossimi paragrafi, elencati
nella @tab:caratteristiche-dati-strutturati, sono:
```{margin}
Python supporta gli _array_ in un package omonimo, che non supporta però la
corrispondente aritmetica. È per questo motivo che per analizzare dati vengono
quasi sempre usati gli _array_ implementati in numpy.
```

- le stringhe, che abbiamo già parzialmente utilizzato e che descrivono
  sequenze di caratteri;
- gli _array_, che contengono sequenze omogenee di oggetti;
- le liste e le tuple, che implementano sequenze di generici oggetti;
- gli insiemi, che fanno riferimento all'omonimo concetto in matematica;
- i dizionari, che permettono di costruire mappe tra oggetti.

Classificherò questi tipi di dati in funzione di vari criteri, che descrivo
qui sotto.

- La modalità di accesso: quando l'aggregazione viene fatta in modo
  sequenziale, il modo più naturale per riferirsi a un elemento della
  struttura è quello di utilizzare un _indice_ che descrive la sua posizione.
  È questo il caso delle stringhe, delle liste, degli _array_ e delle tuple.
  L'accesso a insiemi e i dizionari, che organizzano i dati in un modo non
  necessariamente ordinato, viene invece fatto in modo differente.

- La staticità/dinamicità della struttura: ci sono dei tipi di dati strutturati
  che non permettono di aggiungere o rimuovere elementi a una struttura dopo
  che questa è stata creata (come le stringhe e le tuple), e altri tipi che
  invece lo consentono (come le liste, gli insiemi e i dizionari).

- La mutabilità degli elementi della struttura: alcuni tipi sono _immutabili_,
  nel senso che gli elementi che aggregano non possono essere modificati,
  mentre altri sono _mutabili_. Tra i tipi che considererò, le stringhe e le
  tuple sono immutabili, mentre tutti gli altri sono mutabili.

```{table} Proprietà dei tipi di dati strutturati
:name: tab:caratteristiche-dati-strutturati
:align: center
| Tipo strutturato | Classe     | Posizionale | Dinamico | Mutabile |
|:-----------------|:-----------|:-----------:|:--------:|:--------:|
| stringhe         | `str`      | ✓           | ✕       | ✕        |
| array            | `np.array` | ✓           | ✕       | ✓        |
| liste            | `list`     | ✓           | ✓       | ✓        |
| tuple            | `tuple`    | ✓           | ✕       | ✕        |
| insiemi          | `set`      | ✕           | ✓       | ✓        |
| dizionari        | `dict`     | ✕           | ✓       | ✓        |
```
```{margin}
Ricordate che `np` è l'_alias_ che viene usato per importare numpy.
```

(sec:iterare)=
## Accedere a una struttura
Pur facendo riferimento a concetti altamente diversi tra loro, i tipi di dato
strutturati che considererò supportano delle modalità comuni di accesso, e
Python introduce una sintassi unificata per queste operazioni.
La prima di queste modalità riguarda l'aspetto che ho scelto per definire i
dati di tipo strutturato, ed è quella di supportare in modo automatico
l'iterazione sui contenuti di una struttura.

Molti dei linguaggi di programmazione che si rifanno al paradigma imperativo
prevedono tra le strutture di controllo il cosiddetto _ciclo enumerativo_, noto
ai più come «ciclo for» a causa della parola chiave corrispondente. Questa
particolare forma di iterazione è caratterizzata dal fatto di specificare a
priori il numero di volte che il corpo del ciclo deve essere eseguito.
Normalmente, il numero di iterazioni viene indicato in modo più o meno
esplicito, lavorando su una _variabile di ciclo_[^i] che deve assumere tutti i
valori in una sequenza predefinita, e normalmente&mdash;ma non
sempre&mdash;questa sequenza contempla tutti gli interi da $0$ a un valore $n$
prefissato[^for-caveats].
```{margin}
A complicare ulteriormente la nomenclatura, notate come il termine «struttura
di controllo» si riferisca a un ulteriore concetto che è completamente diverso
sia da «tipo di dati strutturato» che da «struttura dati».
```

Python si comporta in un modo completamente diverso:
nella sua forma più semplice, un ciclo for viene introdotto dall'idioma
`for <variabile> in <struttura>:`, dove `<variabile>` è il nome scelto per la
variabile di ciclo e `<struttura>` è il valore di un tipo di dati strutturato.
Le righe di codice che compongono il corpo del ciclo vengono scritte subito
dopo, aumentando il livello di indentazione. L'esecuzione del ciclo avviene nel
modo seguente: tutti gli elementi contenuti in `<struttura>` vengono
considerati separatamente, una e una sola volta, assegnandoli alla variabile
del ciclo ed eseguendo il suo corpo. La differenza fondamentale rispetto al
ciclo enumerativo classico è che in quest'ultimo la variabile di ciclo contiene
di volta in volta un _indice_ da usare per ottenere l'elemento da
elaborare[^foreach], per esempio estraendolo da un _array_, mentre in Python la
variabile di ciclo contiene direttamente l'elemento in questione.

````{prf:example}
L'unico tipo di dati strutturato al quale ho accennato finora sono le stringhe:
eseguire un ciclo for su una di esse equivale a considerare tutti i caratteri
contenuti, dal primo all'ultimo:

```{code-cell} ipython
for c in 'Wasp':
    print(c)
```
````

Il nome per la variabile di ciclo viene generalmente scelto in modo da
rispettare due requisiti: deve essere corto e deve ricordare il significato
dei valori che saranno contenuti nella variabile. Nell'esempio precedente
ho usato `c`, in quanto l'iterazione è fatta sui caratteri.

Nonostante la sua semantica diversa, `for` in Python ricade a pieno titolo
nella categoria dei cicli enumerativi: anche in questo caso, la variabile di
ciclo assume i valori di una particolare sequenza, che sono poi i valori
contenuti nella struttura sulla quale viene organizzata l'iterazione. La
descrizione che ho dato di questa semantica, però, non specifica
_in quale ordine_ vengono considerati i vari elementi, perché questo dipende
fortemente dal particolare tipo di dati strutturato che si utilizza di volta
in volta: in alcuni casi, come nell'esempio precedente, questo ordine è
noto a priori, mentre in altri no.

Le altre modalità di accesso comuni ai tipi di dati strutturati sono riassunte
nel seguente elenco, e verranno dettagliate nei paragrafi che seguono.

- La funzione `len` restituisce sempre il numero di elementi contenuti nella
  struttura[^data-model]. Nel gergo informatico, ci si riferisce a questo
  numero come alla sua _lunghezza_, anche nel caso in cui questa denominazione
  possa risulta impropria (per esempio, si parla della _cardinalità_ di un
  insieme e non della sua lunghezza).

- È sempre disponibile un operatore di _accesso_ che permette di fare
  riferimento a uno specifico elemento contenuto nella struttura. La sintassi
  corrispondente dipende dal particolare tipo di dati, ma è comunque basata
  sull'uso delle parentesi quadre, mutuata, estendendola, da quella
  dall'analogo operatore che permette di estrarre le componenti in un _array_
  nella maggior parte dei  linguaggi che mettono a disposizione questo tipo di
  dato. Se la struttura è mutabile, l'accesso permetterà anche di modificarne
  il contenuto, altrimenti sarà possibile solamente leggere il valore
  corrispondente.

- L'operatore `in` permette di verificare se una struttura contiene o meno un
  dato elemento.


(sec:stringhe)=
## Le stringhe

```{margin}
A differenza di altri linguaggi, come per esempio C, in Python non esiste
un tipo di dato che corrisponde a un singolo carattere.
```
Le stringhe sono implementate come oggetti della classe `str`, i cui
letterali si costruiscono facendo precedere e seguire i caratteri della
stringa in questione da un delimitatore. Esistono tre tipi di delimitatori:
gli apici singoli, doppi e tripli. L'uso degli apici singoli (`'`) o doppi
(`"`) ricalca la classica sintassi per indicare le stringhe nei linguaggi di
programmazione più diffusi, con la differenza che in Python è possibile
scegliere tra due diversi delimitatori: in altre parole, `'Robin'` e `"Robin"`
identificano la stessa stringa. Questo facilita la creazione di stringhe che
devono contenere apici doppi o singoli, come nella cella seguente:


```{code-cell} ipython3
:tags: remove-output

'Superman proviene da un pianeta chiamato "Krypton".'
"L'altro nome di Superman è Kal-El."
```
```{margin}
Volendo, apici singoli e doppi si possono comunque inserire in un letterale
stringa usando la tecnica di _escaping_, utilizzando rispettivamente le
sequenze `\'` e `\"`.
```

È però necessario chiudere una stringa usando lo stesso tipo di delimitatore
con il quale si è iniziato: sempre due apici singoli, o due doppi apici.
Gli apici tripli permettono di definire delle stringhe che contengono più
righe, senza dover inserire sequenze di _escape_ per i corrispondenti caratteri
di «a capo». Per esempio, il letterale

```{code-cell} ipython3
:tags: remove-output

'''Il primo fumetto che ha Storm come protagonista
compare nel numero uno di "Giant-size X-men"
ed è stato pubblicato nel 1977.
'''
```

fa riferimento a una stringa di tre righe. I tre apici per delimitare le
stringhe su più righe possono essere sia singoli che doppi. Anche in questo
caso, è necessaria coerenza tra il delimitatore iniziale e quello finale.

Abbiamo già visto che l'iterazione su di una stringa avviene carattere per
carattere, nell'esatto ordine con cui questi appaiono. E non dovrebbe stupire
nessuno il fatto che `len(s)` restituisca il numero di caratteri della stringa
`s`, né che i letterali `''` e `""` denotino la stringa vuota (la cui
lunghezza è uguale a zero).

L'operatore di accesso richiede un po' più di dettaglio. Risulta naturale
accedere in modo posizionale ai singoli caratteri di una stringa,
specificandone la posizione, pertanto basta specificare dopo una variabile
che la referenzia (ma ovviamente si potrebbe utilizzare anche un letterale)
una coppia di parentesi quadre contenente la posizione, conteggiata a partire
partire da `0`[^start-from-zero]. In altre parole, si può utilizzare
l'operatore di accesso con la stessa semantica degli _array_. Ma in Python
la sintassi è più estesa: se si specifica un valore negativo per la posizione,
a questo viene automaticamente sommata la lunghezza della lista. Pertanto `-1`
identifica l'ultimo elemento della lista, `-2` il penultimo e così via.

È anche possibile indicare un intervallo di posizioni consecutive per
riferirsi a una sottostringa: questa modalità, che prende il nome
di _slicing_, si effettua indicando tra parentesi quadre la posizione del
primo carattere da includere nella sottostringa, seguita da un carattere di due
punti e dalla posizione del primo carattere da escludere[^substring]. Gli
_slicing_ si possono fare anche usando due indici positivi, oppure due
negativi, o ancora mischiando un indice positivo e uno negativo: la cosa
importante è che la prima posizione preceda la seconda, altrimenti l'operazione
restituisce la stringa vuota.
```{margin}
La sottostringa estratta partirà dal primo carattere della stringa ogni volta
che nello slicing si omette la posizione iniziale, e procederà fino a fine
stringa ogni volta che si omette la posizione finale.
```

In linea di principio, l'operatore `in` dovrebbe permettere di verificare
se un carattere occorre da qualche parte in una stringa oppure no. In realtà
questo comportamento si estende alle sottostringhe: `s in t` restituisce `True`
quando la stringa `s` (che può contenere uno o più caratteri) è una
sottostringa della stringa `t`, e `False` altrimenti.

```{prf:example}
TODO: esempio sulle stringhe.
```


Come già indicato precdentemente, in Python le stringhe sono immutabili, il
che significa che non è possibile cambiarne i contenuti, per esempio
rimpiazzando un carattere con un altro, oppure appendendo uno o più caratteri.
Per effettuare operazioni di questo tipo è sempre necessario creare una nuova
stringa che vada a rimpiazzare quella di partenza.

Il tipo `str` implementa vari metodi e operatori specifici per le stringhe;
in particolare vale la pena segnalare che:

- l'operatore `+` concatena due stringhe,
- l'esito della moltiplicazione tra una stringa `s` e un numero intero `i` è
  una nuova stringa ottenuta concatenando `s` con se stessa per `i` volte;
- `s.find(t)` restituisce la posizione a partire dalla quale la sottostringa
  `t` è contenuta nella stringa `s`, se ciò accade, e `-1` negli altri casi.


Per un elenco completo si può consultare la sezione relativa alle stringhe nella
[documentazione ufficiale](https://docs.python.org/3/library/stdtypes.html#string-methods).

### Stringhe raw e stringhe formattate

(liste)=
## Le liste

Una lista è una struttura dati che permette di memorizzare una sequenza di
elementi. Questi elementi, che sono aggiungibili ed eliminabili dalla lista
dopo che questa è stata creata, possono essere di tipo diverso, e a ognuno di
essi si può accedere in modo diretto specificandone la posizione all'interno
della sequenza. Si dice quindi che una lista è una struttura dati _dinamica_,
_eterogenea_ e ad _accesso posizionale_).

```{admonition} Nomenclatura
:class: naming
Le liste non vanno confuse con gli _array_ (o _vettori_), che sono invece delle
strutture dati _omogenee_ ad accesso posizionale: in altre parole, anche in
questo caso vengono memorizzate delle sequenze di valori, ma questi valori
devono essere tutti dello stesso tipo. Sebbene gli _array_ non siano
direttamente messi a disposizione in Python, è possibile utilizzarli facendo
riferimento al _modulo_ `numpy`, descritto in @importare-moduli.
```

```{margin}
Vedremo che esiste anche la possibilità di utilizzare un particolare
formalismo, chiamato _list comprehension_, per definire una lista in termini di
una _trasformazione_ degli elementi di un'altra struttura dati.
```
Una lista si può indicare in modo _estensivo_, cioè elencando i suoi elementi
dal primo all'ultimo, separandoli tramite virgole e racchiudendo il tutto tra
parentesi quadre. Ciò vale anche per la _lista vuota_, che si può descrivere
scrivendo semplicemente l'espressione `[]`. La proprietà di eterogeneità ci
permette per esempio di usare una lista per aggregare le informazioni che
descrivono un supereroe:

```{code-cell} ipython3
iron_man = ['Iron Man',
            'Tony Stark',
            'Long Island, New York',
            'Marvel Comics',
            198.51,
            191.85,
            'M',
            1963,
            'Blue',
            'Black',
            85,
           'high']
```

```{margin}
Quando però una lista è utilizzata per dati di tipo omogeneo, vale la pena
considerare di sostituirla con un _array_ per diminuire i tempi di esecuzione
e ridurre la possibilità di introdurre _bug_ nel codice.
```
In effetti vedremo che ci sono modi molto più interessanti di codificare un
_record_ di informazioni, così come ci renderemo conto che nei fatti le liste
contengono di norma valori di tipo omogeneo, ma per ora quello che ci interessa
è semplicemente vedere quali sono le modalità principali di utilizzo di questo
tipo di struttura dati.

Per accedere a un elemento in una lista, basta specificare dopo una variabile
che la referenzia (ma ovviamente si potrebbe utilizzare anche la lista stessa)
una coppia di parentesi quadre contenente la posizione dell'elemento,
conteggiata a partire da `0`, pertanto

```{code-cell} ipython3
iron_man[1]
```

permette di accedere al secondo elemento della lista memorizzata in `iron_man`.
Se si specifica un valore negativo per la posizione, a questo viene
automaticamente sommata la lunghezza della lista. Pertanto la posizione `-1`
identifica l'ultimo elemento della lista, la posizione `-2` corrisponde al
penultimo e così via:

```{code-cell} ipython3
iron_man[-2]
```

È anche possibile indicare un intervallo di posizioni consecutive per
recuperare la sottolista corrispondente: questa operazione, che prende il nome
di _list slicing_, si effettua indicando tra parentesi quadre la posizione del
primo elemento da inserire, seguita da un carattere di due punti e dalla
posizione del primo elemento da escludere. Pertanto

```{code-cell} ipython3
iron_man[4:6]
```

permette di accedere alla sottolista che contiene il peso e l'altezza di Tony
Stark, essendo queste informazioni memorizzate in quinta e sesta posizione
nella lista di partenza (ricordando che gli indici delle posizioni partono da
zero). Il riferimento a un _list slicing_ si può fare anche utilizzando indici
negativi (o mescolando indici positivi e negativi):

```{code-cell} ipython3
iron_man[-4:-2]
```

```{margin}
Un'altra differenza tra liste e _array_ è legata al fatto che questi ultimi
rappresentano strutture dati _statiche_, nelle quali non è possibile aggiungere
o rimuovere elementi, ma solo modificare quelli esistenti.
```
Dover specificare la posizione del primo elemento da escludere sembra
controintuitivo rispetto alla scelta più naturale di indicare la posizione
dell'ultimo elemento da includere. In realtà in questo modo risulta più facile
scrivere codice che elabora porzioni successive in una lista. Infine, come già
detto le liste sono strutture dati _dinamiche_, nel senso che oltre a
modificare gli elementi in essa contenuti è anche possibile rimuovere uno o più
di tali elementi, oppure aggiungerne di nuovi.

Sono a disposizione varie operazioni che agiscono sulle liste, e queste
operazioni sono implementate utilizzando diversi elementi del linguaggio:
gli operatori, le funzioni e i metodi. I paragrafi che seguono, lungi
dall'essere esaustivi, introducono alcuni esempi: il loro scopo è
principalmente quello di sottolineare la differenza tra i concetti di
operatore, funzione e metodo in Python. Per degli approfondimenti è possibile
consultare la documentazione ufficiale, che contiene un [documento
introduttivo](https://docs.python.org/3/tutorial/introduction.html#lists) e uno
[più dettagliato](https://docs.python.org/3/tutorial/datastructures.html#)
sull'uso delle liste. Per esemplificare l'uso di questi tre tipi di strumenti
conviene ragionare in termini di una lista utilizzata come se fosse un _array_,
memorizzando dunque una successione di valori dello stesso tipo, per esempio i
nomi di alcuni supereroi:

```{code-cell} ipython3
names = ['Aquaman', 'Ant-Man', 'Batman', 'Black Widow',
         'Captain America', 'Daredavil', 'Elektra', 'Flash',
         'Green Arrow', 'Human Torch', 'Hancock', 'Iron Man',
         'Mystique', 'Professor X', 'Rogue', 'Superman',
         'Spider-Man', 'Thor', 'Northstar']
```

Questo esempio introduce, tra l'altro, l'uso delle stringhe, che saranno approfondite in
@stringhe.


### Operatori

Alcuni degli operatori descritti in @dati-semplici mantengono la loro semantica quando vengono usate delle liste come operatori: per esempio `==` permette di verificare se due liste abbiano uguali contenuti (cioè contengano lo stesso numero di elementi, e gli elementi in una stessa posizione siano uguali). Altri tra questi operatori assumono invece una semantica diversa: in particolare

- l'operatore `+` permette di concatenare due liste, creando una nuova lista che contiene un numero di elementi pari alla somma dei numeri di elementi contenuti nelle due liste usate come operando: in particolare, questa nuova lista conterrà tutti gli elementi del primo operando in testa e tutti quelli del secondo operando in coda;
- per mantenere coerente la relazione tra gli operatori `+` e `*`, se `l` è una lista e `n` è un valore intero la valutazione dell'espressione `l * n` ha l'effetto di creare una nuova lista ottenuta concatenando `l` con se stessa esattamente `n` volte.

```{margin}
Vedremo che `in` e `del` mantengono la loro semantica anche quando vengono usati con altri tipi di strutture dati.
```
Sempre in @dati-semplici sono stati introdotti gli operatori speciali `in` e `del`.
Il primo implementa essenzialmente la relazione di appartenenza: se `e` è un'espressione e `l` una lista, l'espressione `e in l` viene valutata come logicamente vera se il valore dell'espressione occorre in una posizione qualsiasi della lista, e come logicamente falsa altrimenti:

```{code-cell} ipython3
'Thing' in names
```

```{code-cell} ipython3
'Human Torch' in names
```

L'operatore `del` permette invece di eliminare un elemento da una lista, indicandone la relativa posizione: per esempio, eseguendo la cella seguente viene cancellata la stringa contenuta nella prima posizione di `names`:

```{code-cell} ipython3
del names[0]
```

Va sottolineato che `del` è un operatore dal comportamento quantomeno particolare, in quanto esso non restituisce alcun valore; la sua esecuzione ha però l'_effetto collaterale_ di eliminare l'elemento nella posizione specificata della lista usata come operando [^del-behaviour]. Come conseguenza di questo effetto collaterale, nell'esempio precedente viene eliminato il primo elemento della lista, così che quello che prima era il secondo elemento diventa ora il primo, e così via, come si può facilmente verificare:

```{code-cell} ipython3
names[0]
```

```{admonition} Nota
:class: note
In realtà `del` è un operatore che può essere applicato a una vasta gamma di operandi, e che permette di eliminare il riferimento a un oggetto, liberando la memoria che questo occupa quando non ci sono più riferimenti che puntano a esso. Il fatto che le varie componenti di Python accessibili durante l'esecuzione di un programma siano più o meno esplicitamente associate a degli oggetti permette ad esempio di eliminare variabili, parti di strutture dati, ma anche altri elementi del linguaggio che vedremo più avanti, come funzioni e moduli.
```

+++

### Funzioni

Alcune delle funzioni nel linguaggio base di Python sono pensate per elaborare liste. Per esempio `len` restituisce la _lunghezza_ della lista specificata come argomento, dove per lunghezza si intende il numero di elementi contenuti nella lista:

```{code-cell} ipython3
len(names)
```

Anche in questo caso, `len` è una funzione di carattere generale pensata per calcolare la lunghezza delle varie strutture dati implementate in Python.

### Metodi

Python è un linguaggio di programmazione che implementa (anche) il paradigma orientato a oggetti, e come abbiamo già visto le liste (così come gli altri tipi di dati) sono a tutti gli effetti oggetti, e quindi su di esse è possibile invocare dei metodi. Supponiamo per esempio di voler mettere in ordine alfabetico i nomi dei supereroi contenuti in `names` (la lista è quasi in ordine, l'unico elemento fuori posto è l'ultimo): uno dei modi in cui è possibile eseguire questa operazione è quella di invocare sulla lista il metodo `sort` (usando la _dot notation tipica_ della programmazione orientata agli oggetti).

```{code-cell} ipython3
names.sort()
```

Così come l'operatore `del`, questo metodo non restituisce alcun valore, in quanto l'ordinamento è eseguito _in place_ [^sorted]: l'invocazione di `sort` ha come effetto collaterale il riposizionamento degli elementi all'interno della lista in modo da riflettere l'ordinamento [^ordinamento-eterogeneo]. Possiamo convincercene facilmente visualizzando per esempio gli ultimi cinque elementi di `names`:

```{code-cell} ipython3
names[-5:]
```

In Python è possibile specificare valori per argomenti _opzionali_ quando si invoca un metodo (o una funzione): si tratta di argomenti identificati da un nome, che _possono_ essere omessi, e in tal caso assumono un valore predefinito [^argomenti-opzionali]. Per poter specificare un valore diverso da quello predefinito è necessario indicare, dopo _tutti_ gli eventuali argomenti non opzionali, un'espressione del tipo `<nome>=<valore>`, dove `<nome>` indica il nome dell'argomento opzionale in questione e `<valore>` è il relativo valore. Per esempio, il metodo `sort` effettua l'ordinamento in verso non decrescente, e l'argomento opzionale `reversed` permette di invertire tale verso:

```{code-cell} ipython3
names.sort(reverse=True)
```

Un'altra caratteristica di python è quella di poter specificare una funzione come argomento di un metodo (o di un'altra funzione) [^first-class]; ciò si può fare indicando il nome della funzione, oppure usando una _funzione anonima_ (vedi @funzioni-anonime). Consideriamo ad esempio l'argomento opzionale `key` del metodo `sort`: esso permette di indicare un criterio alternativo per eseguire l'ordinamento, specificando come valore una funzione che trasforma gli elementi della lista in quantità numeriche su cui basare l'ordinamento (nel senso che elementi trasformati in numeri più bassi compariranno prima nella lista ordinata rispetto ad altri elementi trasformati in numeri più alti). Dunque è necessario fornire come valore di questo argomento opzionale il nome di una funzione che trasforma stringhe in numeri. Possiamo quindi utilizzare la funzione `len` precedentemente introdotta:

```{code-cell} ipython3
names.sort(key=len)
```

Invocare in questo modo il metodo `sort` equivale quindi a:

- associare ogni nome di supereroe alla sua lunghezza,
- ordinare le coppie ottenute in base alla lunghezza,
- considerare solo i nomi, mantenendo questo nuovo ordinamento.

In parole povere, abbiamo ordinato i nomi dal più breve al più lungo, come si può facilmente verificare:

```{code-cell} ipython3
names
```

Nel caso in cui si volessero specificare due o più argomenti opzionali all'atto dell'invocazione di un metodo, basta separarli usando le virgole esattamente come si procede per gli argomenti non opzionali. Per esempio

```{code-cell} ipython3
names.sort(key=lambda n:len(n), reverse=True)
```

riordina le stringhe contenute in `names` dalla più lunga alla più corta. Va anche notato che essendo gli argomenti opzionali univocamente individuati dal loro nome, non è necessario specificarli seguendo un ordine prefissato: pertanto si potrebbero scambiare le posizioni di `key` e `reverse` nell'invocazione precedente senza modificare la semantica dell'istruzione.


(sec:tuple)=
## Le tuple

```{margin}
La sintassi per la descrizione delle tuple diventa problematica quando si vuole indicare una tupla contenente un unico elemento, in quanto per esempio l'espressione `(1)` viene interpretata come il valore intero `1` racchiuso tra parentesi tonde, ottenendo dunque il medesimo intero come risultato della valutazione. In casi come questo la soluzione è quella di fare seguire l'unico elemento della tupla da una virgola, scrivendo per esempio `(1,)`. Come regola generale, infatti, è sempre possibile aggiungere una virgola alla fine di una tupla (o di una lista) senza che ciò ne alteri i contenuti. È invece possibile utilizzare l'espressione `()` per indicare una tupla vuota.
```
Una tupla è in tutto e per tutto una lista immutabile, nel senso che una volta che essa è stata creata non è possibile modificare i suoi contenuti. Un letterale di tipo tupla viene indicato con una sintassi analoga a quella per le liste, con l'unica differenza che i suoi contenuti sono delimitati da parentesi tonde.

```{code-cell} ipython3
rogue = ('Rogue',
         'Anna Marie',
         'Caldecott County, Mississippi',
         'Marvel Comics',
         173.1,
         54.39,
         'F',
         1981,
         'Green',
         'Brown / White',
         10,
        'good')
```

L'accesso a un elemento di una tupla viene fatto in modo posizionale usando la medesima sintassi introdotta per le liste, e anche in questo caso è possibile estrarre delle sotto-tuple utilizzando degli _slicing_. Quando però si tenta di modificare un elemento contenuto in una tupla, l'esecuzione verrà bloccata emettendo un errore:

```{code-cell} ipython3
try:
    rogue[-2] = 70
except TypeError:
    print('Non si possono modificare gli elementi di una tupla')
```

Notiamo _en passant_ che in Python gli errori di esecuzione sono basati sul meccanismo delle eccezioni, che nella cella precedente vengono gestite in modo analogo a quanto succede per esempio in Java: il blocco di istruzioni coinvolto è quello che segue la parola chiave `try`, e se durante l'esecuzione di tale blocco viene lanciata un eccezione del tipo `TypeError`, quest'ultima viene gestita eseguendo le istruzioni dopo la linea di codice contenente la parola-chiave `except` (andrebbe anche specificato che l'indentazione del codice è obbligatoria, ma di questo ci occuperemo nel Paragrafo @cap:funzioni).

A seguito di questo errore, la tupla manterrà i suoi valori originali, restando quindi effettivamente invariata:

```{code-cell} ipython3
rogue
```

Una tupla può essere utilizzata facendo ri ferimento agli stessi operatori e alle stesse funzioni messi a disposizione per le liste (come per esempio `in` e `len`), escludendo ovviamente le operazioni che modificano la tupla stessa (come `sort`).

+++

L'immutabilità delle tuple le rende da preferire rispetto alle liste in tutti i casi in cui si vuole impedire che dei dati vengano modificati, per esempio a causa di un bug; inoltre la loro elaborazione è in molti casi più efficiente di quella delle liste.


## Gli insiemi
Python implementa direttamente un tipo di dato per gli insiemi, intesi come collezione finita di elementi tra loro distinguibili e non memorizzati in un ordine particolare. A differenza delle liste e delle tuple, gli elementi non sono quindi associati a una posizione e non è possibile che un insieme contenga più di un'istanza di un medesimo elemento. La descrizione di questo tipo di dato è posticipata al Paragrafo @insiemi-in-python, dopo avere richiamato le proprietà matematiche di base degli insiemi.

+++

##  I dizionari
I dizionari servono a memorizzare delle associazioni tra oggetti, in analogia con il concetto matematico di funzione. È quindi possibile pensare a essi come a insiemi di coppie (chiave, valore), dove una data chiave non occorre più di una volta, e a ogni chiave corrisponde un unico valore.

Un letterale di tipo dizionario viene descritto indicando ogni coppia separando chiave e valore con il carattere di due punti, separando le coppie con delle virgole e racchiudendo l'intero letterale tra parentesi graffe. Possiamo per esempio usare un dizionario per rappresentare un _record_ in modo più elegante rispetto a quanto fatto nel Paragrafo @liste utilizzando le liste:

```{code-cell} ipython3
rogue = {'name': 'Rogue',
         'identity': 'Anna Marie',
         'birth_place': 'Caldecott County, Mississippi',
         'publisher': 'Marvel Comics',
         'height': 173.1,
         'weight': 54.39,
         'gender': 'F',
         'first_appearance': 1981,
         'eye_color': 'Green',
         'hair_color': 'Brown / White',
         'strength': 10,
         'intelligence': 'good'}
```

L'accesso, in lettura o scrittura, agli elementi di un dizionario viene fatto con una notazione che ricorda quella di liste e tuple: si specifica all'interno di parentesi quadre la chiave per ottenere o modificare il valore corrispondente:

```{code-cell} ipython3
rogue['identity']
```

È proprio questa modalità di accesso che fa sì che i dizionari rappresentino una scelta più elegante per memorizzare un record: `rogue['identity']` è sicuramente più leggibile di `rogue[1]`. Va notato che il prezzo da pagare per la leggibilità è un'efficienza potenzialmente minore nelle operazioni di accesso (normalmente le liste sono implementate con una logica simile a quella degli array e dunque hanno un tempo di accesso costante ai loro elementi, mentre i dizionari sono implementati tramite tabelle di hash, pertanto l'accesso è a tempo costante solo se non avvengono collisioni).

Se si tenta di accedere in lettura a un dizionario specificando una chiave inesistente viene lanciata un'eccezione (`KeyError`), mentre accedendovi in scrittura la specificazione di una chiave inesistente comporterà l'aggiunta della corrispondente coppia (chiave, valore) al dizionario.

L'operatore `in` introdotto per le liste può anche essere utilizzato per i dizionari: più precisamente, l'espressione `k in d` restituisce `True` se `k` è una chiave valida per il dizionario `d`.

Anche nel caso dei dizionari il linguaggio mette a disposizione una serie di funzioni specifiche, e si può fare riferimento alla [documentazione ufficiale](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) di python per approfondire l'argomento.

[^i]: Nel tempo si è consolidato l'uso dei nomi `i`, `j` e `k` per le variabili
usate nei cicli enumerativi. C'è chi sostiene (ma è uno scherzo) che ciò sia un
omaggio dovuto a [Edsger Dijkstra](wiki:Edsger_Dijkstra), uno dei pionieri
dell'informatica, ma l'origine di questi nomi va fatta risalire a uno dei primi
linguaggi di programmazione: il [Fortran](wiki:fortran), che utilizzava una
dichiarazione di tipo _implicita_, nella quale la lettera iniziale nel nome di
una variabile ne determinava anche il tipo, e il tipo era intero per le 
variabili nelle quali questa iniziale era compresa tra I e N. Per brevità, e
anche per ricordare la classica notazione usata in matematica per gli indici
muti nelle sommatorie o nelle successioni, venivano quindi usate `I`, `J` e `K`
come variabili di ciclo, e `N` o `M` per indicare eventualmente il valore
finale di queste ultime (notate l'uso delle maiuscole: quando è stato
introdotto il Fortran, si usavano solo quelle per scrivere il codice!). Questa
convenzione viene ampiamente usata anche oggi: qualunque programmatore associa
istintivamente nomi come `i` e `j` alle variabili di ciclo. È per questo che
il loro uso è consigliato anche in Python, anche se vedremo che è relativamente
rara la necessità di dover introdurre variabili di questo tipo.

[^for-caveats]: In realtà è possibile modificare dinamicamente il numero di
iterazioni in un ciclo enumerativo, sia forzandone l'uscita anticipata, sia
modificando alcune informazioni contestuali, come il valore della varaibile di
ciclo nei linguaggi come C o Java, o la modifica del dato strutturato sul quale
si esegue l'iterazione in Python.  Quest'ultima pratica è però decisamente
sconsigliata, perché complica la comprensione del codice ed è normalmente
rimpiazzabile con degli idiomi di programmazione più eleganti, come la sopra
menzionata uscita anticipata.

[^foreach]: Per completezza di informazione, molti altri linguaggi di
programmazione affiancano al ciclo enumerativo (inteso in senso classico) una
struttura di controllo con la semantica analoga a quella di `for` in Python,
usando parole chiave dedicate come `foreach` o `forall`, oppure introducendo
una sintassi alternativa.

[^data-model]: Se avete già studiato un linguaggio di programmazione orientato
agli oggetti, vi starete probabilmente chiedendo perché la lunghezza di una
struttura non si ottenga invocando un metodo su di essa. Questo è in effetti
quello che succede dietro le quinte: tutte le occorrenze di `len(o)` vengono
automaticamente convertite nell'invocazione `o.__len__()`, dove `__len__` è
un metodo implementato in tutti i tipi strutturati (il doppio _underscore_
all'inizio e alla fine del nome del metodo sancisce il fatto che quest'ultimo è
per certi versi speciale, ed è alla base della regola di stile che richiede di
non usare `_` all'inizio e alla fine degli identificatori). Questo permette
agli sviluppatori di scrivere nuove classi i cui oggetti possono essere usati
in modo trasparente come argomenti di `len`. Procedendo in modo analogo si
riesce ad agire praticamente su tutti gli aspetti del linguaggio, costruendo
delle classi i cui oggetti possono venire usati come operandi in espressioni
matematiche, o che possono essere invocati come delle funzioni, o ancora che
supportano l'equivalente degli operatori di accesso. L'idea di base è quella
di usare sempre la stessa sintassi per effettuare una particolare azione,
indipendentemente dallo specifico tipo di dato che viene elaborato (ricordate
uno dei principi esposti nello zen di Python: «There should be one&mdash;and
preferably only one&mdash;obvious way to do it»). Il cosiddetto
[Python data model](https://docs.python.org/3/reference/datamodel.html)
formalizza in modo dettagliato la corrispondenza tra i vari componenti del
linguaggio e i metodi che le classi devono implementare. Un
buon punto di partenza per studiare il Python data model è il primo capitolo
di {cite:p}`ramalho`, sebbene sarebbe prima importante imparare come si
definisce una nuova classe.

[^start-from-zero]: Gli informatici iniziano a contare da zero. Se aveste
qualche dubbio sull'utilità di questa pratica, un breve ma particolarmente
efficace
[manoscritto](https://www.cs.utexas.edu/~EWD/ewd08xx/EWD831.PDF) di Edsger
Dijkstra (vedi anche la precedente nota[^i]) descrive i suoi vantaggi.

[^substring]: Dover specificare la posizione del primo carattere da
escludere sembra controintuitivo rispetto a indicare la posizione dell'ultimo
carattere nella sottostringa. In realtà in questo modo risulta più facile
scrivere codice che elabora porzioni successive in una stringa.

[^del-behaviour]: I lettori attenti potrebbero avere notato un apparente incoerenza tra il modo in cui vengono valutate le espressioni e la semantica appena introdotta per l'operatore `del`. Consideriamo l'espressione `del names[0]` dell'esempio precedente: se questa fosse valutata in modo ususale, verrebbe innanzitutto valutato l'operando, dunque l'espressione `names[0]`. L'operatore `del` verrebbe quindi applicato al valore ottenuto, che nel nostro caso sarebbe la stringa `'Aquaman'`. Ora, l'istruzione `del 'Aquaman'` genererebbe un errore, perché `del` si può applicare solo a riferimenti e non a letterali. In realtà la valutazione di espressioni di questo tipo viene fatta in un modo diverso, perché `del names[0]` viene implicitamente convertita in un'altra espressione che equivale a invocare un particolare metodo dell'oggetto referenziato da `names`, passando il valore `0` come argomento. 

[^sorted]: In realtà è disponibile anche la funzione `sorted`, che non modifica l'argomento e restituisce una nuova lista.

[^ordinamento-eterogeneo]: Tenuto conto del fatto che le liste sono una struttura dati eterogenea ci si potrebbe chiedere quale sia la relazione d'ordine a cui fa riferimento Python quando viene invocato il metodo `sort`. Non approfondiremo questo aspetto: per quanto riguarda gli argomenti qui trattati è sufficiente dire che quando gli elementi della lista sono tutti dello stesso tipo viene sfruttata una relazione d'ordine canonica per questo tipo. Per esempio i valori numerici sono ordinati in modo non decrescente e per le stringhe viene utilizzato l'ordinamento lessicografico.

[^argomenti-opzionali]: Gli argomenti opzionali vengono tipicamente utilizzati quando si ha a che fare con metodi o funzioni che implementano operazioni che prevedono svariate opzioni, sebbene nella maggior parte dei casi ognuna di queste opzioni venga usata sempre nello stesso modo, modificandone al più una oppure due. Si pensi al caso della produzione di grafici: sebbene in teoria sia possibile cambiare il colore o lo spessore degli assi cartesiani, o il corpo dei caratteri usati per etichettare questi ultimi, difficilmente si ricorre a tale possibilità. E anche quando si decide di modificare l'aspetto di un grafico, si agisce di norma solo su alcune delle molteplici possibilità. In assenza di argomenti opzionali, sarebbe quindi necessario specificare obbligatoriamente un elevato numero di valori (uno per ogni elemento stilistico personalizzabile), quasi sempre uguali e ricordandone l'ordine esatto. Vedremo nel Paragrafo @disegnare-grafici che le librerie che useremo per produrre grafici sfruttano proprio gli argomenti opzionali per permettere di specificare solo le eventuali modifiche da apportare rispetto a uno stile predefinito per il risultato che si vuole ottenere.

[^first-class]: Nel gergo tecnico in lingua inglese si dice che i nomi di funzione sono _first-class citizen_ per enfatizzare che vengono trattate in modo analogo ai nomi delle altre variabili: è possibile per esempio usarli per specificare argomenti, o come destinazione di un'operazione di assegnamento.
