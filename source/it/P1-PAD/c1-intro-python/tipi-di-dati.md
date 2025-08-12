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

(sec:tipi-di-dati)=
# Tipi di dati

Nell'ambito della programmazione dei calcolatori, si utilizza normalmente
il termine _tipo_ per identificare a quale categoria appartiene un particolare
_dato_ che può essere associato a una variabile, a un'espressione, a un
parametro, al valore restituito da una funzione e così via. Associare ogni
dato a un tipo è importante perché ciò permette di capire quali operazioni si
possono effettuare su di esso: per esempio, l'elevamento a potenza può avere
senso quando l'esponente è un numero, ma non, per dire, una stringa. Anche
Python associa ogni dato a un tipo, ma il meccanismo che utilizza è molto
diverso da quello dei linguaggi che di solito si incontrano quando si inizia a
studiare programmazione. Vedremo tra poco come funziona questo meccanismo,
specificando alcune macro-categorie di tipi che analizzeremo in dettaglio nei
paragrafi successivi. Questo mi permetterà anche di introdurre alcuni accenni
alla _programmazione orientata agli oggetti_, necessari per poter utilizzare
una parte delle librerie alle quali farò riferimento, visto che non sempre
questo argomento è noto a chi si appresta a imparare i fondamenti della
_data science_.
```{margin}
Nel {ref}`sec:attributi` vedremo che è importante non confondere
il _tipo di un attributo_ all'interno di un _dataset_ con il _tipo di dato_
utilizzato per memorizzare i valori dell'attributo stesso.
```

(sec:tipizzazione-dinamica)=
## Tipizzazione dinamica

Nella gran parte dei linguaggi che si studiano quando si impara a programmare
gli elaboratori (come C, o Java, o Go), l'associazione di un dato al tipo
corrispondente deve essere fatta in modo esplicito tramite un'opportuna
_dichiarazione_, che determina che cosa si può fare con quel dato. Ciò permette
di rilevare eventuali operazioni improprie, come il sopra citato  elevamento
alla potenza di una lettera, effettuando una preventiva analisi lessicale dei
contenuti di un programma, e trasformando quest'ultimo in codice eseguibile
solo se tale analisi ha esito positivo. Si parla quindi di _type checking
statico_, o di _tipizzazione statica_, riferendosi al fatto che la verifica
della congruità dei tipi viene fatta «a bocce ferme», leggendo il codice prima
che questo venga eseguito e dunque stabilendo il tipo di ogni dato una volta
per tutte.

In Python si segue invece un approccio differente, eliminando dal linguaggio
l'obbligo di rendere esplicite le dichiarazioni e affidandosi a
un _type checking dinamico_ che viene effettuato durante l'esecuzione del
codice. Senza entrare troppo nei dettagli, prima di effettuare una singola
operazione si verifica che questa sia possibile in funzione dei valori degli
operandi coinvolti. Se vengono rilevate delle incongruenze, viene lanciata
un'eccezione, altrimenti l'esecuzione procede.
```{margin}
È interessante sottolineare che Python è un linguaggio _fortemente tipizzato_,
nel senso che non vengono mai eseguite conversioni implicite (come per esempio
le promozioni) tra tipi di operandi fondamentalmente diversi, come stringhe
e interi.
```

L'utilizzo del _type checking_ dinamico semplifica notevolmente la struttura
del linguaggio di programmazione, che utilizza dei _nomi_ da associare a
variabili e a parametri formali di funzioni, senza alcuna indicazione dei
tipi coinvolti. In particolare:

- una variabile viene automaticamente creata in corrispondenza del primo
  assegnamento che la coinvolge, e il suo tipo è quello del valore assegnato;
- i parametri formali di metodi e funzioni vengono associati ai tipi che
  corrispondono ai valori attuali di volta in volta specificati durante le
  relative invocazioni;
- il tipo restituito da una funzione è quello dell'espressione di volta in
  volta restituita al termine dell'invocazione della funzione stessa.

Ciò significa che tecnicamente non ha più senso parlare del tipo di una
variabile, o di un parametro, o del valore restituito da una funzione come
di qualcosa di immutabile. La funzione potrebbe ad esempio restituire tipi
differenti a seconda dei parametri attuali specificati durante la sua
invocazione; analogamente, è possibile assegnare a una variabile un valore il
cui tipo è completamente diverso rispetto al valore precedentemente
memorizzato, e così via. In sintesi, il concetto di tipo in Python è relativo:
ciò che puoi fare con una variabile o un parametro dipende dal valore che
contiene in quel momento. A complicare il tutto, a partire dalla versione 3.5
di Python è possibile effettuare una sorta di dichiarazione, utilizzando un
formalismo chiamato _type hinting_ che permette di indicare nel codice il
tipo di alcuni elementi del linguaggio (come ad esempio i parametri formali di
una funzione, o il valore da essa restituito). Va sottolineato che la
tipizzazione resta comunque dinamica, ma in questo modo è possibile utilizzare
degli strumenti esterni per effettuare il cosiddetto _type checking_, che
consiste nel verificare _staticamente_ (cioè sulla base di quanto scritto nel
codice) che le variabili vengano utilizzate correttamente. _Editor_ e IDE 
possono per esempio trarre vantaggio dal _type hinting_ per suggerire come
completare il codice o per segnalare dei _warning_. Infine, l'uso del _type
hinting_ rappresenta anche un modo per alleggerire la documentazione del
software prodotto, pertanto tenderò a utilizzarla ove questo aiuterà a leggere
meglio il codice, evitando nel contempo di adottarla quando ciò comporti
un inutile appesantimento.

(sec:tipi_classi_oggetti)=
## Tipi, classi e oggetti
Python è un linguaggio che supporta pienamente il paradigma di programmazione
orientato agli oggetti, che mette in evidenza i concetti di _classe_ e
_oggetto_ per rappresentare ed elaborare i dati. Semplificando non poco la
trattazione, una classe identifica un'_astrazione_ rispetto a tutti i dati di
un certo tipo. Una classe è, in pratica, l’insieme di tutti i dati di un certo
tipo. Un singolo elemento di quell’insieme è detto _oggetto_, o _istanza_.
Entrando un poco più nel dettaglio, una classe definisce non solo che cosa è
necessario memorizzare affinché esista un dato (le informazioni che sono
descritte dalle sue _variabili di istanza_), ma anche quali sono le operazioni
che si possono eseguire sull'oggetto corrispondente (i suoi _metodi_) Per
esempio, un'ipotetica classe `Superhero` potrebbe prevedere

- due variabili di istanza `name` e `secret_identity`, contenenti due stringhe
  che indicano il nome di un supereroe e la sua identità segreta;
- due metodi `fly` e `run` che implementano le azioni che corrispondono,
  rispettivamente, a farlo volare e correre.
```{margin}
In alcuni linguaggi orientati agli oggetti, i metodi rimpiazzano completamente
le funzioni. Come vedremo più avanti, in Python i due concetti coesistono.
```

Se tutto quello che ci interessa fare con un supereroe è riferirsi al suo nome
e alla sua identità segreta, nonché farlo volare o correre, la classe
`Superhero` racchiude tutto quello di cui necessitiamo. Quando vorremo
ragionare in termini di uno specifico supereroe, diciamo Superman, possiamo
creare l'oggetto corrispondente invocando un particolare metodo che prende il
nome di _costruttore_ della classe, e che accetta come parametri le
informazioni necessarie a inizializzare l'oggetto stesso (spesso, ma non
sempre, si tratta dei valori per tutte o alcune delle variabili di istanza). Il
costruttore restituisce un _riferimento_ all'oggetto creato, che di norma viene
memorizzato in una variabile. In Python, il costruttore si invoca facendo 
riferimento allo stesso nome della classe, così che la creazione dell'oggetto
che corrisponde a Superman e la memorizzazione del corrispondente riferimento
si potrebbe ipoteticamente fare nel modo descritto nella cella seguente.

```{code}
# Questo codice è riportato per esemplificare i concetti di classe, costruttore,
# riferimento e oggetto. Non eseguitelo, perché non funzionerebbe!

# Notate anche che tutto il testo che segue un carattere di cancelletto (#)
# viene ignorato durante l'esecuzione rappresenta dunque un commento.

hero = Superhero('Superman', 'Clark Kent')
``` 

In questo caso,

```{margin}
Come vedremo nel Paragrafo @sec:stringhe, in Python esistono diversi
delimitatori per le stringhe, e uno di questi è l'apice singolo.
```

- `Superhero` indica la classe, dunque anche il costruttore;
- `'Superman'` e`'Clark Kent'` rappresentano le stringhe utilizzate per
  inizilizzare le due variabili di istanza;
- `hero` è il nome della variabile che conterrà il riferimento all'oggetto
   della classe `Superhero` che modella Superman.

La memorizzazione del riferimento restituito dal costruttore in una variabile
è necessaria perché nella maggior parte dei casi l'interazione con l'oggetto
avviene utilizzando una specifica sintassi detta _dot notation_: si fa seguire
il nome della variabile da un carattere di punto e dal nome di una variabile
di istanza o di un metodo. Nel primo caso si ottiene un'espressione il cui
valore corrisponde al contenuto della variabile di istanza, e nel secondo
il risultato si può usare per invocare il metodo, specificando i valori degli
eventuali parametri previsti.
```{margin}
In teoria la _dot notation_ si può applicare direttamente al riferimento
restituito dal costruttore, o perfino ai _letterali_ della classe[^letterali],
anche se è estremamente raro che questo si renda necessario.
```
Tornando all'esempio precedente, `hero.name` corrisponde a `'Superman'`, ed è
possibile effettuare l'invocazione `hero.fly()` (se per invocare il metodo non
è richiesta la specificazione del valore di alcun parametro). Anche in
questo contesto, il linguaggio è basato su un _type checking_ dinamico:
indipendentemente dalla classe in gioco,  quando a _runtime_ viene analizzata
una _dot notation_, se il riferimento individua un oggetto che prevede la
variabile di istanza o il metodo specificati, l'esecuzione procede senza
problemi. Negli altri casi viene lanciata un'eccezione `AttributeError`. Questo
significa che, indipendentemente dalla sua classe, se a partire da un oggetto è
possibile accedere alle variabili di istanza `name` e `secret_identity`, nonché
invocare i metodi `fly` e `run`, questo è in tutto e per tutto equivalente a un
oggetto della classe `Superhero`, e lo si potrà utilizzare in tutti i contesti
pensati per tale classe[^duck-typing].

(sec:regole-di-stile)=
```{admonition} Approfondimento: identificatori e regole di stile
Il termine _identificatore_ indica il nome scelto per riferirsi in modo univoco
a specifiche entità in un programma, come variabili, variabili di istanza,
classi, funzioni, metodi, parametri e così via. Io utilizzerò i termini «nome»
e «identificatore» in modo intercambiabile, sebbene il primo termine si possa
utilizzare anche in contesti differenti (pensate per esempio al nome di un
file).

Da un punto di vista sintattico, per formare un identificatore in Python si
possono utilizzare i caratteri alfabetici maiuscoli e minuscoli (tenendo conto
del fatto che il linguaggio è _case sensitive_: `superman` e `Superman`
rappresentano due identificatori differenti), le cifre e il carattere di
_underscore_ (`_`), con l'unico vincolo di non usare una cifra come carattere
iniziale.

Rispettare la sintassi è obbligatorio, ma è anche buona pratica seguire nel
modo più coerente possibile delle _regole di stile_, che tra le altre cose
prevedono delle convenzioni specifiche su come debbano essere formati gli
identificatori. Non esiste però uno standard unico: io farò riferimento alla
[Style Guide for Python
Code](https://www.python.org/dev/peps/pep-0008/){.external}, che contiene anche
un paragrafo [Naming
conventions](https://peps.python.org/pep-0008/#naming-conventions){.external}.
Per variabili (di istanza e non), funzioni e metodi, queste regole di stile
prevedono il cosiddetto _snake case_: si usano unicamente i caratteri minuscoli
e l'_underscore_, impiegando quest'ultimo solo come separatore in un
identificatore composto da più parole (come in `secret_identity` nel precedente
esempio). L'uso di uno o più _underscore_ all'inizio o alla fine di un nome è
da evitare, perché può conferire un significato specifico al codice che
emerge solo in particolari occasioni. Nel libro non affronterò situazioni di
questo tipo, ma è meglio essere particolarmente attenti a questo aspetto già
quando si imparano le basi del linguaggio. Ci sono comunque delle eccezioni
da considerare: tra queste, solo due sono rilevanti per i nostri scopi:

- quando risulta particolarmente significativo utilizzare come identificatore
  una parola chiave del linguaggio (come per esempio `lambda`, che utilizzeremo
  nel Paragrafo @sec:funzioni-anonime, per esprimere concetti matematici o
  fisici), è   accettabile aggiungere un underscore al suo termine (ottenendo,
  nel caso precedente, l'identificatore `lambda_`);
- se è necessario riferirsi esplicitamente a una variabile che viene utilizzata
  in una parte particolarmente limitata del codice, o che non viene utilizzata
  affatto, al posto di inventare un nome significativo si può usare un unico
  _underscore_ come identificatore.

Gli identificatori delle classi andrebbero invece costruiti adottando il
cosiddetto _upper camel case_, che prevede di utilizzare esclusivamente
caratteri alfabetici, servendosi delle maiuscole per marcare l'inizio di ogni
parola (come in `Superhero`). Infine, nonostante Python non preveda il concetto
di _costante_, è possibile usare la variante dello _snake case_ che utilizza
solo lettere maiuscole (il cosiddetto _screaming snake case_) per
suggerire che il contenuto di una variabile non muterà dopo il primo (e unico)
assegnamento che la riguarda.

Anche tenendo conto della sintassi e delle regole di stile, vi è ampia
discrezionalità nella scelta per un identificatore: per esempio, al posto di
`hero` si sarebbero potuti utilizzare `clark_kent`, `superman`, `s`, `s1` o
accozzaglie più o meno intelligibili di caratteri. Per aumentare la leggibilità
del codice è però altamente consigliabile scegliere un nome che sia legato
al significato dell'identificatore stesso.
```

Va infine sottolineato che l'unico modo di riferirsi a un tipo di dato in
Python è attraverso l'utilizzo delle classi: a differenza di Java, non esistono
«tipi primitivi» che memorizzano interi, decimali e così via come mere sequenze
di byte. Al contrario, i tipi intero e decimale fanno riferimento alle classi
`int`[^maxint] e `float`, ognuna caratterizzata dai suoi metodi.
```{margin}
Gran parte delle classi che implementano tipi introdotti fin dalle prime
versioni di Python, come `int` e `float`, sono delle eccezioni alla regola di
stile che ho precedentemente menzionato: per una serie di motivi legati anche
alla retrocompatibilità del linguaggio, i loro nomi non iniziano con una
lettera maiuscola.
```

Ricapitolando, quando si parla di una variabile all'interno di codice scritto
in Python, invece di dire che una variabile contiene un valore di un dato
tipo, sarebbe più corretto parlare di un _nome_ (o identificatore) associato a
un _riferimento_ che a sua volta individua univocamente l'oggetto di una
classe: la seconda individua (temporaneamente, a causa della tipizzazione
dinamica) il tipo del particolare dato che corrisponde alla variabile (nel
gergo informatico inglese si usa il verbo _to bind_, che significa «legare»,
per indicare in modo ancora più forte questa associazione tra il nome e
l'oggetto). Un discorso analogo si può fare per esempio per i parametri formali
di una funzione o di un metodo. Oggettivamente, questa nomenclatura tende a
essere pesante, e infatti nel gergo comune è diffusa l'abitudine di riferirsi a
una variabile (o un parametro) e all'oggetto&mdash;quando non al
valore&mdash;in essa contenuto.


```{admonition} Avvertenza
La programmazione orientata agli oggetti è un argomento molto complesso, e in
questo paragrafo ne ho solo scalfito la superficie. Mi sono limitato a
introdurre ciò che è necessario conoscere per poter comprendere il codice che
che presenterò nel seguito, e imparare a scrivere programmi che automatizzano
le tecniche di analisi dei dati che introdurrò nei capitoli seguenti. Non ho
descritto come sia possibile creare delle classi per riferirsi a tipi di dati
personalizzati, né introdotto argomenti specifici come l'ereditarietà e il
polimorfismo, perché non è necessario conoscere questi aspetti del linguaggio
per poter comprendere con profitto il resto di quello che scriverò.
Padroneggiare questi concetti, però, è una competenza decisamente attesa per
ogni professionista dell'informatica, e auspicabile anche per un
_data scientist_, ma tutto questo è ampiamente al di fuori dello scopo di
questo libro. Per approfondire questi argomenti si può fare riferimento alla
[specifica parte](https://docs.python.org/3/tutorial/classes.html){.external}
della documentazione ufficiale di Python o alla parte IV in {cite:p}`ramalho`.
```

(sec:tipi-semplici-e-strutturati)=
## Tipi semplici e strutturati

Semplificando un po' il discorso, possiamo suddividere i tipi di dati che
utilizzeremo in due grandi categorie:

- i tipi di dati _semplici_, che servono a definire un'informazione atomica,
  che ha poco senso suddividere ulteriormente, come ad esempio un
  dato numerico intero o decimale;
- i tipi di dati _strutturati_, che vengono utilizzati per aggregare insieme
  più tipi di dati (semplici o strutturati che siano), come gli _array_ o
  gli insiemi.

I due paragrafi che seguono descriveranno, rispettivamente, i tipi di dati
semplici e strutturati che utilizzerò nel libro. Già solo considerando il
linguaggio base, Python contempla svariati tipi di dati (la documentazione
ufficiale ne riporta un
[elenco](https://docs.python.org/3/library/datatypes.html){.external}), ai
quali vanno aggiunti i tipi implementati dalle librerie di terze parti. La
trattazione che farò non è sicuramente esaustiva, e, anche se lo fosse, sarebbe
lungi dall'essere perfetta. Da una parte, non è completa, perché vi sono classi
che implementano tipi che non ricadono naturalmente in nessuna delle due
categorie introdotte (come quelle che descrivono le funzioni, o gli iteratori,
o concetti complessi che non corrispondono ad alcun tipo di dati così come lo
si intende in senso classico); dall'altra, è opinabile associare alcuni tipi a
una delle due categorie: per esempio, le stringhe possono essere pensate come
un tipo semplice, ma anche annoverate tra i tipi strutturati, essendo esse
costituite da una sequenza di caratteri. Per decidere se un tipo di dato è
semplice oppure strutturato, io mi baserò sul seguente criterio: un dato è di
tipo strutturato se Python permette di _iterare_ nativamente sui suoi elementi
usando l'idioma `for` (vedi {ref}`sec:iterare`); in tutti gli altri casi,
considererò il tipo di dato come semplice.


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
@sec:tipi_classi_oggetti, indicando ulteriori variabili di istanza e metodi
che è sensato considerare per i relativi oggetti.
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

```{exercise} ••
La funzione `type` restituisce la classe del valore specificato come argomento.
Utilizzate questa funzione per capire di che tipo siano le seguenti espressioni:

- `42`;
- `42.`;  
- `'foo'`;
- `None`;
- `int`.

```

```{exercise} ••
Considerate le seguenti sequenze di caratteri, e per ognuna di esse stabilite
se rappresenta un identificatori valido in Python oppure no. Per ogni
identificatore valido, indicate se esso rispetta oppure no le convenzioni
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

[^letterali]: Se non sapete (o non ricordate) che cosa si intende per letterale,
pazientate fino al prossimo paragrafo.

[^duck-typing]: Spesso si utilizza
il termine _duck typing_ per descrivere questo aspetto della tipizzazione
dinamica, facendo riferimento a una frase attribuita al poeta americano James
Whitcomb Riley: «when I see a bird that walks like a duck and swims like a duck
and quacks like a duck, I call that bird a duck».

[^maxint]: È anche interessante notare che l'implementazione della classe `int`
adotta un approccio ad aritmetica con _precisione arbitraria_: il numero di bit
necessari per memorizzare un valore intero non è prefissato, bensì allocato
dinamicamente in funzione dei valori di volta in volta assegnati. Ciò implica
che non esiste un «più grande» o un «più piccolo» intero memorizzabile, come
in altri linguaggi.
