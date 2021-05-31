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

(dati-strutturati)=
# I tipi di dati strutturati

I tipi di dati strutturati, o più brevemente _strutture dati,_ permettono di aggregare più valori.
Python supporta nativamente i seguenti tipi strutturati: le liste, le tuple, le stringhe, gli insiemi e i dizionari. A ognuno di questi tipi corrisponde una diversa classe, esattamente come per i tipi semplici. Come descritto nei paragrafi seguenti, la sintassi per accedere ai contenuti di una struttura dati è relativamente uniforme, mentre ovviamente il modo in cui viene effettuato l'accesso dipende dallo specifico tipo di struttura dati.

In Python è possibile sia usare gli oggetti che corrispondono ai tipi di dati strutturati (ma anche gli altri tipi di dati descritti più avanti) come argomenti di operatori o funzioni, sia invocare metodi sugli oggetti stessi. Anche in questo caso vi sono operazioni di carattere più generale, effettuate utilizzando una sintassi comune, e operazioni specifiche che hanno una sintassi propria. Nel resto di questo paragrafo, senza pretesa di essere esaustivi, descrive le modalità di accesso e le operazioni principali per i tipi strutturati sopra elencati e fornisce dei puntatori alla documentazione ufficiale per chi volesse approfondire alcuni argomenti.

+++

## Le liste

Una lista è una struttura dati che permette di memorizzare una sequenza di elementi. Questi elementi possono essere di tipo diverso, e a ognuno di questi si può accedere in modo diretto specificandone la posizione all'interno della sequenza (si dice quindi che una lista è una struttura dati _eterogenea_ e ad _accesso posizionale_).

```{admonition} Attenzione!
:class: warning
Le liste non vanno confuse con gli _array_ (o _vettori_), che sono invece delle strutture dati _omogenee_ ad accesso posizionale: in altre parole, anche in questo caso vengono memorizzate delle sequenze di valori, ma questi valori devono essere tutti dello stesso tipo. Sebbene gli _array_ non siano direttamente messi a disposizione in Python, è possibile utilizzarli facendo riferimento al _package_ `numpy`, descritto nel {numref}`Paragrafo %s <importare-moduli>`
```


Una lista si può indicare in modo _estensivo_ separando i suoi elementi tramite virgola e racchiudendo il tutto tra parentesi quadre. La proprietà di eterogeneità ci permette per esempio di usare una lista per aggregare le informazioni che descrivono un supereroe:

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
Quando però una lista è utilizzata per dati di tipo omogeneo, vale la pena considerare di sostituirla con un _array_ per diminuire il tempo di esecuzione.
```
In effetti vedremo che ci sono modi molto più interessanti di codificare un _record_ di informazioni, così come ci renderemo conto che nei fatti le liste contengono di norma valori di tipo omogeneo, ma per ora quello che ci interessa è semplicemente vedere quali sono le modalità principali di utilizzo di questo tipo di struttura dati.

Per accedere a un elemento in una lista, basta specificare dopo una variabile che la referenzia (ma ovviamente si potrebbe utilizzare anche la lista stessa) una coppia di parentesi quadre contenente la posizione dell'elemento, conteggiata a partire da `0`, pertanto

```{code-cell} ipython3
iron_man[1]
```

permette di accedere al secondo elemento della lista memorizzata in `iron_man`. Se si specifica un valore negativo per la posizione, a questo viene automaticamente sommata la lunghezza della lista. Pertanto la posizione `-1` identifica l'ultimo elemento della lista, la posizione `-2` corrisponde al penultimo e così via:

```{code-cell} ipython3
iron_man[-2]
```

È anche possibile indicare un intervallo di posizioni consecutive per recuperare la sottolista corrispondente: questa operazione, che prende il nome di *list slicing*, si effettua indicando tra parentesi quadre la posizione del primo elemento da inserire, seguita da un carattere di due punti e dalla posizione del primo elemento da escludere. Pertanto

```{code-cell} ipython3
iron_man[4:6]
```

permette di accedere alla sottolista che contiene il peso e l'altezza di Tony Stark, essendo queste informazioni memorizzate in quinta e sesta posizione nella lista di partenza (ricordando che gli indici delle posizioni partono da zero). Il riferimento a un _list slicing_ si può fare anche utilizzando indici negativi (o mescolando indici positivi e negativi):

```{code-cell} ipython3
iron_man[-4:-2]
```

```{margin}
Un'altra differenza tra liste e _array_ è legata al fatto che questi ultimi rappresentano strutture dati _statiche_, nelle quali non è possibile aggiungere o rimuovere elementi, ma solo modificare quelli esistenti.
```
Dover specificare la posizione del primo elemento da escludere sembra controintuitivo rispetto alla scelta più naturale di indicare la posizione dell'ultimo elemento da includere. In realtà in questo modo risulta più facile scrivere codice che elabora porzioni successive in una lista. Le liste sono, infine, una struttura dati *dinamica*, nel senso che oltre a modificare gli elementi in essa contenuti è anche possibile rimuovere uno o più di tali elementi, oppure aggiungerne di nuovi.

Python mette a dipsosizione varie operazioni che agiscono sulle liste: i paragrafi che seguono introducono alcuni esempi, ma il loro scopo è più quello di sottolineare la differenza tra i concetti di operatore, funzione e metodo. Per degli approfondimenti è possibile consultare la documentazione ufficiale, che contiene un [documento introudttivo](https://docs.python.org/3/tutorial/introduction.html#lists) e uno [più dettagliato](https://docs.python.org/3/tutorial/datastructures.html#) sull'uso delle liste in Python. Per esemplificare l'uso di questi tre tipi di strumenti conviene ragionare in termini di una lista utilizzata come se fosse un _array_, memorizzando dunque una successione di valori dello stesso tipo, per esempio i nomi di alcuni supereroi:

```{code-cell} ipython3
names = ['Aquaman', 'Ant-Man', 'Batman', 'Black Widow',
         'Captain America', 'Daredavil', 'Elektra', 'Flash',
         'Green Arrow', 'Human Torch', 'Hancock', 'Iron Man',
         'Mystique', 'Professor X', 'Rogue', 'Superman',
         'Spider-Man', 'Thor', 'Northstar']
```

Questo esempio introduce, tra l'altro, l'uso delle stringhe, che saranno approfondite nel {numref}`Paragrafo %s <stringhe>`.


```{rubric} Operatori
```
Alcuni degli operatori descritti nel {numref}`Paragrafo %s <dati-semplici>` mantengono la loro semantica quando vengono usate delle liste come operatori: per esempio `==` permette di verificare se due liste abbiano uguali contenuti (cioè contengano lo stesso numero di elementi, e gli elementi in una stessa posizione siano uguali). Altri tra questi operatori assumono invece una semantica diversa: in particolare

- l'operatore `+` permette di concatenare due liste, creando una nuova lista che contiene un numero di elementi pari alla somma dei numeri di elementi contenuti nelle due liste usate come operando: in particolare, questa nuova lista conterrà tutti gli elementi del primo operando in testa e tutti quelli del secondo operando in coda;
- per mantenere coerente la relazione tra gli operatori `+` e `*`, se `l` è una lista e `n` è un valore intero la valutazione dell'espressione `l * n` ha l'effetto di creare una nuova lista ottenuta concatenando `l` con se stessa esattamente `n` volte.

```{margin}
Vedremo che `in` e `del` mantengono la loro semantica anche quando vengono usati con altri tipi di strutture dati.
```
Sempre nel {numref}`Paragrafo %s <dati-semplici>` sono stati introdotti gli operatori speciali `in` e `del`.
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

Va sottolineato che `del` è un operatore dal comportamento quantomeno particolare, in quanto esso non restituisce alcun valore; la sua esecuzione ha però l'_effetto collaterale_ di eliminare l'elemento nella posizione specificata della lista usata come operando [^data-model]. Come conseguenza di questo effetto collaterale, nell'esempio precedente viene eliminato il primo elemento della lista, così che quello che prima era il secondo elemento diventa ora il primo, e così via, come si può facilmente verificare:

```{code-cell} ipython3
names[0]
```

```{admonition} Nota
:class: note
In realtà `del` è un operatore che può essere applicato a una vasta gamma di operandi, e che permette di eliminare il riferimento a un oggetto, liberando la memoria che questo occupa quando non ci sono più riferimenti che puntano a esso. Il fatto che le varie componenti di Python accessibili durante l'esecuzione di un programma siano più o meno esplicitamente associate a degli oggetti permette ad esempio di eliminare variabili, parti di strutture dati, ma anche altri elementi del linguaggio che vedremo più avanti, come funzioni e moduli.
```

+++

```{rubric} Funzioni
```
Alcune delle funzioni nel linguaggio base di Python sono pensate per elaborare liste. Per esempio `len` restituisce la _lunghezza_ della lista specificata come argomento, dove per lunghezza si intende il numero di elementi contenuti nella lista:

```{code-cell} ipython3
len(names)
```

Anche in questo caso, `len` è una funzione di carattere generale pensata per calcolare la lunghezza delle varie strutture dati implementate in Python.

```{rubric} Metodi
```
Python è un linguaggio di programmazione che implementa (anche) il paradigma orientato a oggetti, e come abbiamo già visto le liste (così come gli altri tipi di dati) sono a tutti gli effetti oggetti, e quindi su di esse è possibile invocare dei metodi. Supponiamo per esempio di voler mettere in ordine alfabetico i nomi dei supereroi contenuti in `names` (la lista è quasi in ordine, l'unico elemento fuori posto è l'ultimo): uno dei modi in cui è possibile eseguire questa operazione è quella di invocare sulla lista il metodo `sort` (usando la _dot notation tipica_ della programmazione orientata agli oggetti).

```{code-cell} ipython3
names.sort()
```

Così come l'operatore `del`, questo metodo non restituisce alcun valore, in quanto l'ordinamento è eseguito _in place_ [^sorted]: l'invocazione di `sort` ha come effetto collaterale il riposizionamento degli elementi all'interno della lista in modo da riflettere l'ordinamento [^ordinamento-eterogeneo]. Possiamo convincercene facilmente visualizzando per esempio gli ultimi cinque elementi di `names`:

```{code-cell} ipython3
names[-5:]
```

L'invocazione di metodi (e di funzioni) prevede in python anche la possibilità di specificare degli argomenti _opzionali_: si tratta di argomenti, identificati da un nome, che possono essere omessi, e in tal caso assumono un valore predefinito all'atto dell'invocazione. Per poterne specificare un valore diverso da quello predefinito è sufficiente indicare, dopo gli eventuali altri argomenti, un'espressione del tipo `<nome>=<valore>`, separando tramite virgola la specificazione di più argomenti opzionali. Per esempio il metodo `sort` effettua l'ordinamento in verso non decrescente, e l'argomento opzionale `reversed` permette di invertire tale verso:

```{code-cell} ipython3
names.sort(reverse=True)
```

Un'altra caratteristica di python è quella di poter specificare una funzione come argomento di un metodo (o di un'altra funzione); ciò si può fare o indicando il nome della funzione, oppure usando una _lambda function_ o _funzione anonima_: una funzione che viene definita senza darle un nome ma definendo direttamente come i suoi argomenti devono essere trasformati nel valore da restituire. Più precisamente, la sintassi `lambda x: <espressione>` definisce una funzione che ha un argomento il cui nome simbolico è `x` e che restituisce l'espressione dopo il carattere di due punti (che di norma dipenderà da `x`).

Un esempio che mette insieme l'uso di argomenti opzionali e di funzioni anonime si trova nella cella seguente, in cui la lista dei nomi viene ordinata non in modo alfabetico, bensì in funzione della lunghezza dei nomi stessi, specificando tramite l'argomento opzionale `key` una funzione anonima che trasformerà ogni elemento della lista in un valore su cui basare l'ordinamento.

```{code-cell} ipython3
successore = lambda n: n+1
successore(9)
```

```{code-cell} ipython3
names.sort(key=lambda n:len(n))
names
```

Un altro metodo invocabile su una lista è `insert`, che permette di aggiungere un elemento a una lista esistente, specificando rispettivamente come secondo e primo argomento l'elemento da aggiungere e la posizione in cui inserirlo: per esempio nella cella seguente viene re-inserito Aquaman in modo da mantenere `names` in orine

```{code-cell} ipython3
names.insert(4, 'Aquaman')
names[:6]
```

## Le tuple

+++

Una tupla è una lista immutabile: una volta creata non è possibile modificare i suoi contenuti. Una tupla viene indicata in modo analogo a una lista, con l'unica differenza che i suoi contenuti sono delimitati da parentesi tonde.

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

L'accesso a un elemento di una tupla viene fatto in modo posizionale usando la medesima sintassi introdotta per le liste:

+++

Qualora si tenti di modificare un elemento in una tupla, l'esecuzione verrà però bloccata emettendo un errore:

```{code-cell} ipython3
try:
    rogue[-2] = 70
except TypeError:
    print('Non si possono modificare gli elementi di una tupla')
```

Va notato che in python gli errori di esecuzione vengono emessi utilizzando il meccanismo delle eccezioni, che nella cella precedente vengono gestite in modo analogo a quanto succede per esempio in Java: il blocco di istruzioni coinvolto è quello che segue la parola chiave `try`, e le istruzioni dopo `except` vengono eseguite solo se viene lanciata un eccezione del tipo specificato. A seguito di questo errore, la tupla manterrà i suoi valori originali, restando quindi effettivamente invariata:

```{code-cell} ipython3
rogue
```

Una tupla può essere utilizzata facendo ri ferimento agli stessi operatori e alle stesse funzioni messi a disposizione per le liste (come per esempio `in` e `len`), escludendo ovviamente le operazioni che modificano la tupla stessa (come `sort`).

+++

L'immutabilità delle tuple le rende da preferire rispetto alle liste in tutti i casi in cui si vuole impedire che dei dati vengano modificati, per esempio a causa di un bug; inoltre la loro elaborazione è in molti casi più efficiente di quella delle liste.

+++

<div class="alert alert-info">
Va notato che la sintassi per la descrizione delle tuple diventa problematica quando si vuole indicare una tupla contenente un unico elemento, in quanto per esempio `(1)` viene interpretato come valore `1` tra parentesi tonde. La soluzione in casi come questi è quella di fare seguire l'unico elemento della tupla da una virgola, scrivendo per esempio `(1,)`. Come regola generale, infatti, è possibile aggiungere una virgola alla fine di una tupla (o di una lista) senza variarne i contenuti.
</div>

+++

(stringhe)=
## Le stringhe

Le stringhe sono implementate come tuple di caratteri, e quindi su di esse è possibile eseguire tutte le operazioni che si eseguono sulle tuple:

```{code-cell} ipython3
name = rogue[1]
name[3]
```

Si verifica facilmente come si tratti di tuple e non di liste, in quanto i contenuti non sono modificabili:

```{code-cell} ipython3
try:
    name[3] = 'A'
except TypeError:
    print('Non si possono modificare i contenuti di una stringa')
```

Anche per quanto riguarda le liste è possibile approfondire l'argomento consultando la [documentazione ufficiale](https://docs.python.org/3/library/stdtypes.html#string-methods).

+++

## Gli insiemi
Python implementa direttamente un tipo di dato per gli insiemi, intesi come collezione finita di elementi tra loro distinguibili e non memorizzati in un ordine particolare. A differenza delle liste e delle tuple, gli elementi non sono quindi associati a una posizione e non è possibile che un insieme contenga più di un'istanza di un medesimo elemento. Non utilizzeremo questo tipo di dato, quindi si rimanda alla [documentazione ufficiale](https://docs.python.org/2/library/stdtypes.html#set) per un approfondimento.

+++

##  I dizionari
I dizionari servono a memorizzare delle associazioni tra oggetti, in analogica con il concetto matematico di funzione. È quindi possibile pensare a essi come a insiemi di coppie (chiave, valore), dove una data chiave non occorre più di una volta.

Un dizionario viene descritto indicando ogni coppia separando chiave e valore con il carattere di due punti, separando le varie coppie con delle virgole e racchiudendo il tutto tra parentesi graffe. Possiamo per esempio usare un dizionario per rappresentare un record in modo più elegante rispetto alla precedente scelta basata sulle liste:

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

+++

[^data-model]: I lettori attenti potrebbero avere notato un apparente incoerenza tra il modo in cui vengono valutate le espressioni e la semantica appena introdotta per l'operatore `del`. Consideriamo l'espressione `del names[0]` dell'esempio precedente: se questa fosse valutata in modo ususale, verrebbe innanzitutto valutato l'operando, dunque l'espressione `names[0]`. L'operatore `del` verrebbe quindi applicato al valore ottenuto, che nel nostro caso sarebbe la stringa `'Aquaman'`. Ora, l'istruzione `del 'Aquaman'` genererebbe un errore, perché `del` si può applicare solo a riferimenti e non a letterali. In realtà la valutazione di espressioni di questo tipo viene fatta in un modo diverso, perché `del names[0]` viene implicitamente convertita in un'altra espressione che equivale a invocare un particolare metodo dell'oggetto referenziato da `names`, passando il valore `0` come argomento. Senza addentrarsi in dettagli, è importante segnalare che Python è permeato da tecniche di questo tipo, che permettono tra l'altro di estendere l'uso della sintassi per i tipi _builtin_ anche a oggetti di classi definite dagli sviluppatori. Chi volesse approfondire questo spetto può studiare il cosiddeto [data model](https://docs.python.org/3/reference/datamodel.html) di Python (sebbene sarebbe prima importante imparare come definire e utilizzare nuove classi).

[^sorted]: In realtà è disponibile anche la funzione `sorted`, che non modifica l'argomento e restituisce una nuova lista.

[^ordinamento-eterogeneo]: Tenuto conto del fatto che le liste sono una struttura dati eterogenea ci si potrebbe chiedere quale sia la relazione d'ordine a cui fa riferimento Python quando viene invocato il metodo `sort`. Non approfondiremo questo aspetto: per quanto riguarda gli argomenti qui trattati è sufficiente dire che quando gli elementi della lista sono tutti dello stesso tipo viene sfruttata una relazione d'ordine canonica per questo tipo. Per esempio i valori numerici sono ordinati in modo non decrescente e per le stringhe viene utilizzato l'ordinamento lessicografico.

```{code-cell} ipython3

```
