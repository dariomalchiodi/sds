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

(sec_tipi-di-dati)=
# Tipi di dati

```{margin}
Nel {ref}`chap_dati-e-informazione` vedremo che non bisogna confondere il _tipo
di un attributo_ in un dataset con il _tipo di dato_ usato per memorizzare i
valori di quell’attributo.
```
Nella programmazione dei calcolatori, il termine _tipo_ indica normalmente la
categoria a cui appartiene un _dato_ che può essere associato a una variabile,
a un'espressione, a un parametro, al valore restituito da una funzione e così
via. Associare ogni dato a un tipo è fondamentale, perché ci dice quali
operazioni si possono effettuare su di esso. Per esempio, l'elevamento a
potenza ha senso quando l'esponente è un numero, ma non quando è una stringa.
Anche Python assegna un tipo a ogni dato, ma lo fa con un meccanismo molto
diverso rispetto ai linguaggi che si incontrano di solito quando si inizia a
stuidare programmazione. Tra poco vedremo come funziona questo sistema,
distinguendo alcune macro-categorie di tipi che analizzeremo in dettaglio nei
paragrafi successivi. Questo ci permetterà anche di introdurre alcuni aspetti
della programmazione orientata agli oggetti, indispensabili per usare parte
delle librerie che incontreremo. Non sempre chi inizia a studiare i fondamenti
della _data science_ ha già familiarità con questi concetti, quindi li
tratteremo con la gradualità necessaria.

(sec_tipizzazione-dinamica)=
## Tipizzazione dinamica

Nella maggior parte dei linguaggi che si incontrano quando siinizia a
programmare (come C, Java o Go), il tipo di un dato deve essere indicato in
modo esplicito, mediante una _dichiarazione_. Questo permette di analizzare il
codice e intercettare in anticipo eventuali errori, come il già citato
tentativo di elevare una lettera a potenza. L’analisi viene normalmente
eseguita da un compilatore, che se tutto è corretto tradue il codice di
partenza in un programma eseguibile. Si parla quindi di _type checking
statico_, o _tipizzazione statica_, perché la verifica della coerenza dei tipi
avviene «a bocce ferme», fissando una volta per tutte il tipo di ciascun dato,
indipendentemente da ciò che accade durante l’esecuzione.

Python segue invece un approccio diverso. Non obbliga a dichiarare i tipi in
anticipo, ma si affida a un _type checking dinamico_, che avviene durante
l’esecuzione del programma. In pratica, prima di eseguire ogni operazione viene
controllata la coerenza dei tipi di dati coinvolti. Se emergono incongruenze,
viene sollevata un’eccezione; altrimenti l’esecuzione prosegue normalmente.

È utile sottolineare che Python è un linguaggio _fortemente tipizzato_: non
esegue mai _coercizioni implicite_ tra tipi fondamentalmente diversi, come
stringhe e interi. Trasformazioni di questo tipo devono essere fatte in modo
esplicito. Diverso è il caso delle _promozioni_, che avvengono automaticamente
quando un tipo meno rappresentativo viene convertito in uno più
rappresentativo. Un esempio classico è la somma tra un intero e un numero
decimale: in questo caso l’intero viene automaticamente promosso a decimale.

Il _type checking_ dinamico semplifica notevolmente la struttura del
linguaggio: si usano semplicemente dei _nomi_ per indicare variabili, parametri
formali di funzioni e così via, senza dover specificare i tipi. In particolare:

- una variabile viene creata automaticamente la prima volta che le viene
  assegnato un valore, e ciò determina il suo tipo iniziale; quest'ultimo può
  successivamente cambiare, a seconda di come verrà modificata la variabile;
- i parametri formali di metodi e funzioni assumono i tipi dei parametri
  effettivi specificati a ogni invocazione;  
- il tipo restituito da una funzione è quello dell’espressione effettivamente
  restituita di volta in volta.

Di conseguenza, non ha più senso parlare del tipo di una variabile, di un
parametro o del valore restituito da una funzione come se fosse qualcosa di
immutabile. Al contrario, in Python il concetto di tipo è relativo: una
funzione può restituire tipi diversi a seconda dei parametri ricevuti; allo
stesso modo, una variabile può contenere valori di tipi differenti in momenti
diversi dell’esecuzione.

A complicare il quadro, dalla versione 3.5 di Python è possibile effettuare una
sorta di dichiarazione, utilizzando un formalismo chiamato _type hinting_, che
permette di indicare nel codice il tipo di alcuni elementi del linguaggio. Per
esempio, è possibile indicare un tipo per i parametri formali di una funzione,
o per il valore che essa restituisce. È però importante chiarire che la
tipizzazione rimane comunque dinamica: il _type hinting_ non modifica il
comportamento del linguaggio. Tuttavia, apre la porta a strumenti esterni che
possono effettuare un _type checking_ statico, basato su ciò che è scritto
nel codice. Per esempio, _editor_ e IDE possono proporre
suggerimenti per il completamento del codice o segnalare _warning_.  
Infine, il _type hinting_ rende più leggibile il codice e permette di scrivere
documentazione più concisa. Per questo lo utilizzerò quando aumenterà la
chiarezza del testo, evitando però di introdurlo nei casi in cui
rappresenterebbe solo un inutile appesantimento.


(sec_tipi_classi_oggetti)=
## Tipi, classi e oggetti

Python supporta pienamente il paradigma di programmazione orientato agli
oggetti, basato sui concetti di _classe_ e _oggetto_ per rappresentare ed
elaborare i dati. In parole semplici, per _classe_ si intende un’_astrazione_
rispetto a tutti i dati di un certo tipo, che considerati singolarmente ne
costituiscono un _oggetto_, o _istanza_. Più precisamente, una classe definisce
non solo che cosa è necessario memorizzare affinché esista un dato (le
informazioni che sono descritte dalle sue _variabili di istanza_), ma anche
quali sono le operazioni che si possono eseguire sull'oggetto corrispondente (i
suoi _metodi_). Per esempio, un'ipotetica classe `Superhero` potrebbe prevedere

```{margin}
In alcuni linguaggi orientati agli oggetti, i metodi rimpiazzano completamente
le funzioni. Come vedremo più avanti, in Python i due concetti coesistono.
```
- due variabili di istanza `name` e `secret_identity`, contenenti due stringhe
  che indicano il nome di un supereroe e la sua identità segreta;
- due metodi `fly` e `run` che implementano le azioni che corrispondono,
  rispettivamente, a farlo volare e correre.

Se tutto quello che ci interessa fare con un supereroe è riferirsi al suo nome
e alla sua identità segreta, nonché farlo volare o correre, la classe
`Superhero` racchiude tutto quello di cui necessitiamo. Per ragionare nei
termini di uno specifico supereroe, diciamo Superman, dobbiamo creare l'oggetto
corrispondente invocando un metodo speciale che prende il nome di _costruttore_
della classe [^costruttore]. Questo riceve come parametri le informazioni
necessarie a inizializzare l'oggetto stesso (spesso, ma non sempre, si tratta
dei valori per tutte o alcune delle variabili di istanza). Il costruttore
restituisce un _riferimento_ all'oggetto creato, che di norma viene memorizzato
in una variabile, così da poterlo succesivamente utilizzare nel codice. In
Python, il costruttore si invoca facendo riferimento allo stesso nome della
classe, così che la creazione dell'oggetto che corrisponde a Superman e la
memorizzazione del corrispondente riferimento si possono fare come nella cella
seguente.

```{code}
# Questo codice è riportato per esemplificare i concetti di classe,
# costruttore, riferimento e oggetto. Non eseguitelo, perché non funzionerebbe!

# Notate anche che tutto il testo che segue un carattere di cancelletto (#)
# viene ignorato durante l'esecuzione, perché rappresenta un commento.

hero = Superhero('Superman', 'Clark Kent')
``` 


In questo caso,

```{margin}
Come vedremo nel Paragrafo {ref}`sec_stringhe`, in Python esistono diversi
delimitatori per le stringhe, uno dei quali è l'apice singolo.
```
- `Superhero` indica la classe, e di conseguenza viene utilizzato come
  costruttore;  
- `'Superman'` e `'Clark Kent'` sono le stringhe utilizzate per inizializzare
  le due variabili di istanza;  
- `hero` è la variabile che conterrà il riferimento all'oggetto creato.

```{margin}
In teoria, la _dot notation_ può essere applicata direttamente al riferimento
restituito dal costruttore, o perfino ai _letterali_ della classe[^letterali],
anche se questo è raramente necessario.
```
Memorizzare il riferimento restituito in una variabile è importante per poter
successivamente interagire con l'oggetto. Nella maggior parte dei casi, ciò
richiede l'utilizzo di una specifica sintassi detta _dot notation_: si scrive
il nome della variabile, seguito da un punto e dal nome di una variabile di
istanza o di un metodo. Nel primo caso si ottiene un'espressione il cui valore
è quello della variabile di istanza, e nel secondo il risultato si può usare
per invocare il metodo, specificando eventuali parametri effettivi. Tornando
all’esempio, valutando `hero.name` si ottiene `'Superman'`, mentre `hero.fly()`
invoca sull'oggetto il metodo `fly` (senza specificare parametri). Anche qui,
Python applica il _type checking_ dinamico: a _runtime_, se il riferimento
memorizzato in `hero` punta a un oggetto che contiene la variabile di istanza o
il metodo indicati, l’esecuzione procede senza problemi. Altrimenti, viene
sollevata un’eccezione `AttributeError`. Questo comportamento implica che,
indipendentemente dalla classe, se un oggetto permette di accedere a `name` e
`secret_identity` e di invocare i metodi `fly` e `run`, esso può essere
trattato come un oggetto della classe `Superhero`, usandolo in tutti i contesti
pensati per tale classe[^duck-typing].

```{admonition} Approfondimento: identificatori e regole di stile
:name: adm:regole-di-stile

Il termine _identificatore_ indica il nome scelto per riferirsi in modo univoco
ad alcuni elementi inun programma, come variabili, variabili di istanza,
classi, funzioni, metodi e parametri. In questo libro userò i termini «nome» e
«identificatore» in modo intercambiabile, anche se il primo può comparire in
altri contesti con un significato differente, ad esempio per riferirsi al
nome di un file.

In Python, per formare un identificatore si possono usare i caratteri che
corrispondono alle lettere maiuscole e minuscole (il linguaggio è _case
sensitive_: `superman` e `Superman` sono considerati identificatori diversi),
all'_underscore_ (`_`) e alle cifre (a patto di non iniziare l'identificatore
con una di esse). 

Rispettare la sintassi è obbligatorio, ma è anche buona pratica seguire in
modo coerente possibile delle _regole di stile_, che descrivono anche come
formare gli identificatori. Non esiste uno standard unico: io farò riferimento
alla [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) e
in particolare al paragrafo [Naming
conventions](https://peps.python.org/pep-0008/#naming-conventions). Per
variabili (di istanza e non), funzioni e metodi, queste regole prevedono
l'impiego dello _snake case_: si usano solo le lettere minuscole, più
l'_underscore_ come separatore per gli identficatori che contengono più
parole (come in `secret_identity` nell'esempio di prima). L'uso di uno o più
_underscore_ iniziali o finali va evitato, perché può conferire un significato
particolare al codice. Non approfondiremo questo aspetto, dunque mi limito a
specificare due eccezioni rilevanti a questa regola:

- quando una parola chiave del linguaggio è particolarmente significativa come
  identificatore (per esempio `lamdba`, che utilizzeremo nel Paragrafo
  {ref}`sec_funzioni-anonime`, e che può comparire come simbolo in formule
  matematiche), si può aggiungere a questa parola un _underscore_ finale
  (ottenendo, nel caso precedente, l'identificatore `lambda_`);
- se è necessario riferirsi esplicitamente a una variabile temporanea, o che
  non viene utilizzata affatto, usare un unico _underscore_ come identificatore
  evita di dover pensare a un nome significativo.

Gli identificatori delle classi dovrebbero invece adottare l'_upper camel
case_, che si deriva dallo _snake case_ eliminando l'_underscore_ e usando le
lettere maiuscole per indicare l'inizio di ogni parola (come in `Superhero`).
Infine, nonostante Python non implementi le _costanti_, è possibile usare lo
_screaming snake case_ &mdash; la variante dello _snake case_ che utilizza solo
lettere &mdash; per segnalare che il contenuto di una variabile non muterà dopo
il primo assegnamento che la riguarda (ma ribadisco che si tratta di una mera
convenzione stilistica: come detto sopra, Python non prevede le costanti e
dunque è possibile modificare una siffatta variabile senza che questo causi
errori a _runtime_[^costanti-type-hint]).

Anche tenendo conto della sintassi e delle regole di stile, vi è ampia
discrezionalità nella scelta per un identificatore: per esempio, al posto di
`hero` si potrebbero utilizzare `clark_kent`, `superman`, `s`, `s1` o sequenze
più o meno intelligibili di caratteri. Per aumentare la leggibilità del codice,
è però consigliabile scegliere nomi significativi, che riflettano il ruolo
dell'identificatore.
```

Va sottolineato che, in Python, l’unico modo per riferirsi a un tipo di dato è
attraverso le classi. A differenza di quanto accade con altri linguaggi, come
Java, non esistono «tipi primitivi» separati che memorizzano interi, decimali o
altri valori come mere sequenze di byte. I tipi intero e decimale corrispondono
infatti alle classi `int` e `float`[^first-letter], ciascuna dotata dei propri
metodi.

Ricapitolando, quando parliamo di una variabile in Python, non ha molto senso
parlare del suo tipo. È più corretto ragionare in termini di un _nome_ (o
identificatore) che è associato a un riferimento, che a sua volta individua
&mdash; temporaneamente, a causa della tipizzazione dinamica &mdash; un oggetto
di una certa classe. La classe, infine, determina il tipo dello specifico dato
memorizzato in quella variabile. Nel gergo inglese si usa spesso il verbo
_to bind_ («legare») per sottolineare questa associazione tra nome e oggetto.
Per parametri formali di funzioni o metodi si può fare un discorso analogo.
Questa terminologia risulta spesso pesante, e infatti nella pratica comune si
tende a fare un abuso di linguaggio, senza distinguere formalmente tra nome,
riferimento e oggetto. Più semplicemente, ci si riferisce a una variabile (o a
un parametro) e all’oggetto, quando non al valore, in essa contenuto. 


```{admonition} Avvertenza
La programmazione orientata agli oggetti è un argomento molto complesso, e qui
ne ho solo scalfito la superficie, accennando ai suoi aspetti essenziali. Mi
sono concentrato su ciò che serve conoscere per comprendere il codice che
che presenterò nel seguito, e per imparare a scrivere programmi che
automatizzano le tecniche di analisi dei dati descritte nei capitoli seguenti.
In particolare, non ho trattato la creazione di classi personalizzate, né 
concetti come ereditarietà e polimorfismo, perché non sono necessari per
seguire il resto della trattazione. Padroneggiare questi concetti è però una
competenza attesa per ogni professionista dell'informatica, e auspicabile anche
per chi si occupa di _data science_, ma è al di fuori dello scopo di questo
libro. Per approfondire questi argomenti si può fare riferimento alla
[documentazione ufficiale di
Python](https://docs.python.org/3/tutorial/classes.html), o alla parte IV in
{cite:p}`ramalho`.
```

(sec_tipi-semplici-e-strutturati)=
## Tipi semplici e strutturati

Semplificando, possiamo dividere i tipi di dati che utilizzeremo in due grandi
categorie:

- i tipi di dati _semplici_, che rappresentano un'informazione atomica, che
  ha poco senso suddividere ulteriormente, come un numero intero o decimale;  
- i tipi di dati _strutturati_, che aggregano insieme più tipi di dati
  (semplici o strutturati), come _array_ o insiemi.

Nei due paragrafi successivi descriverò, rispettivamente, i tipi di dati
semplici e strutturati che utilizzerò nel libro. Anche considerando i soli tipi
_builtin_, Python offre molti tipi di dati (la [documentazione
ufficiale](https://docs.python.org/3/library/datatypes.html) ne riporta un
elenco), ai quali vanno aggiunti i tipi implementati da librerie di terze
parti. Pertanto non proporrò una trattazione esaustiva. Anche se lo fosse,
questa sarebbe lungi dall'essere perfetta: non sarebbe completa, perché alcune
classi implementano tipi che non rientrano naturalmente in nessuna delle due
categorie (come le classi che si riferiscono a funzioni, iteratori o concetti
complessi che non corrispondono a un tipo di dato così come lo si intende in
senso classico). Inoltre, l’assegnazione di alcuni tipi a una categoria può
essere opinabile: ad esempio, le stringhe possono essere considerate un tipo
sia semplice che strutturato, perché sono sequenze di caratteri. Per decidere
se un tipo di dato è semplice o strutturato, adotterò un criterio pratico:
considero un tipo strutturato se Python permette di _iterare_ nativamente sui
suoi elementi usando l’idioma `for` (vedi il Paragrafo {ref}`sec_iterare`); in
tutti gli altri casi, considererò il tipo di dato come semplice.


## Esercizi

```{exercise} •
In riferimento alle caratteristiche del _type checking_ dinamico, dite quali
delle seguenti affermazioni sono vere e quali sono false:

- in momenti diversi dell'esecuzione di un programma, una stessa variabile
  può contenere valori di tipo differente;
- il nome di una variabile può mutare durante l'esecuzione;
- è possibile assegnare un valore a una variabile prima della sua definizione;
- una funzione può in alcuni casi restituire un valore e in altri no;
```

```{exercise} •
Considerate l'ipotetica classe `Superhero` definita nel Paragrafo
{ref}`sec_tipi_classi_oggetti`, indicando ulteriori variabili di istanza e
metodi che è sensato considerare per i relativi oggetti.
```

```{exercise} ••
Stabilite quali delle seguenti affermazioni sui costruttori in Python sono vere
e quali sono false:

- per ottenere l'oggetto di una classe può essere necessario invocare il
  corrispondente costruttore per più volte;
- l'invocazione di un costruttore non richiede mai di dovere specificare
  valori per dei parametri;
- a ogni variabile di istanza in una classe corrisponde un parametro nel
  costruttore;
- l'invocazione di un costruttore è l'unico modo per creare un oggetto;
- il nome di una classe è anche l'identificatore da utilizzare per invocare
  il corrispondente costruttore.
```

```{margin}
Il fatto che una funzione restituisca una classe potrebbe sembrarvi quantomeno
strano: risolvendo questo esercizio, riflettete sul significato di questo
comportamento e sulle sue possibili implicazioni. Più avanti, spiegherò un po'
più in dettaglio questa particolarità del linguaggio.
```
```{exercise} ••
La funzione `type` restituisce la classe del valore specificato come argomento.
Utilizzate questa funzione per capire di che tipo siano le seguenti
espressioni:

- `42`;
- `42.`;  
- `'foo'`;
- `None`;
- `int`.

```

```{exercise} ••
Considerate le seguenti sequenze di caratteri, e per ognuna di esse stabilite
se rappresentano un identificatori valido in Python oppure no. Per ogni
identificatore valido, indicate anche se esso rispetta le regole di stile
introdotte nel testo.

- `velocita`;
- `velocità`;
- `speed`;
- `Speed`;
- `CarSpeed`;
- `CArSPeED`;
- `Car_Speed`
- `SPEED`
- `CAR_SPEED`
- `_speed`;
- `speed_`;
- `__speed`;
- `speed__`;
- `__speed__`;
- `__init__`;
- `set_level`;
- `set__level`;
- `set__level__`;
- `int`;
- `int_`;
- `i`;
- `i1`;
- `1i`;
- `_`;
- `black&white`;
- `jfellfsef`.
```

```{exercise} ••
Considerate i tipi di dati che già conoscete (per esempio, quelli che avete
studiato nei corsi di programmazione), e per ognuno di essi specificate se
ricade nella categoria dei tipi semplici o di quelli strutturati, motivando
la vostra scelta.
```


[^costruttore]: In realtà, la costruzione di un oggetto avviene in due fasi
successive: la _creazione_, intesa come allocazione della memoria necessaria
per contenerlo, e l'_inizializzazione_, che imposta i valori che definiscono
l'oggetto nel suo stato iniziale. Se studierete Python in modo più
approfondito, scoprirete che queste due azioni corrispondono rispettivamente
ai metodi `__new__` e `__init__`, e comunemente ci si riferisce a quest'ultimo
come al costruttore della classe, anche se tecnicamente questo è incorretto.

[^letterali]: Se non ricordate (o non sapete) che cosa si intende per
letterale, pazientate fino al prossimo paragrafo.

[^duck-typing]: Il termine _duck typing_ descrive questo aspetto della
tipizzazione dinamica. Il nome trae ispirazione da un detto attribuito al poeta
americano James Whitcomb Riley: «when I see a bird that walks like a duck and
swims like a duck and quacks like a duck, I call that bird a duck».

[^costanti-type-hint]: Per la precisione, esistono strumenti che si
avvantaggiano del _type hinting_ per segnalare che un identificatore deve
essere trattato come una costante, così come tecniche speciali di
programmazione che evitano che un identificatore venga modificato, ma si tratta
di aspetti decisamente avanzati rispetto a quanto affronto in questo libro.

[^first-letter]: Se siete stati attenti, dovreste avere notato una
contraddizione: nel riquadro [Regole di stile](#adm:regole-di-stile) ho scritto
che i nomi delle classi dovrebbero utilizzare l'_upper camel case_, ma ciò non
è vero per `int` e `float`, né per gran parte delle classi dei tipi accessibili
in Python senza ricorrere a librerie (quelli che vengono chiamati tipi
_builtin_). Questi tipi usano uno stile separato (come anche specificato nella
PEP8) per molteplici ragioni, tra cui semplificare il codice, o evidenziare la
differenza tra le classi _builtin_ e quelle definite dagli utenti. 
