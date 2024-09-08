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
  enumerator: 2.1.%s

title: 2.2. Tipi di dati
---

Nell'ambito della programmazione dei calcolatori, si utilizza normalmente
il termine _tipo_ per identificare a quale categoria appartiene un particolare
_dato_ che può essere associato a una variabile, a un'espressione, a un
parametro, al valore restituito da una funzione e così via. Associare ogni
dato a un tipo è importante perché ciò permette di identificare quelle che
sono le operazioni che si possono effettuare su di esso: per esempio,
l'elevamento a potenza può avere senso quando l'esponente è un numero, ma
non, per dire, una stringa. Sebbene Python non faccia eccezione, il meccanismo
che utilizza per identificare i tipi è decisamente diverso da quello adottato
dai linguaggi che normalmente si studiano quando ci si avvicina alla
programmazione degli elaboratori. Di seguito vedremo in dettaglio come funziona
questo meccanismo, specificando alcune macro-categorie di tipi che
saranno analizzate in dettaglio nei paragrafi successivi. Questo mi permetterà
anche di introdurre alcuni accenni alla _programmazione orientata agli
oggetti_, necessari per poter utilizzare una parte delle librerie alle quali
farò riferimento, tenuto conto del fatto che non sempre questo argomento è noto
a chi si appresta a imparare i fondamenti della _data science_.
```{margin}
Nel Paragrafo @attributi vedremo che è importante non confondere il _tipo di un
attributo_ all'interno di un _dataset_ con il _tipo di dato_ utilizzato per
memorizzare i valori dell'attributo stesso.
```

(tipizzazione-dinamica)=
## Tipizzazione dinamica

Nella gran parte dei linguaggi che si studiano quando si impara a programmare
gli elaboratori (come C, o Java, o Go), l'associazione di un dato al tipo
corrispondente deve essere fatta in modo esplicito tramite un'opportuna
_dichiarazione_, che determina che cosa si può fare con il dato in questione. 
Ciò permette di rilevare eventuali operazioni improprie, come il sopra citato 
elevamento alla potenza di una lettera, effettuando una preventiva analisi
lessicale dei contenuti di un programma, e trasformando quest'ultimo in codice
eseguibile solo se tale analisi ha esito positivo. Si parla quindi di _type
checking statico_, o di _tipizzazione statica_, riferendosi al fatto che la
verifica della congruità dei tipi viene fatta «a bocce ferme», leggendo il
codice prima che questo venga eseguito e dunque stabilendo il tipo di ogni dato
una volta per tutte.

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
le promozioni) tra tipi di operandi fondamentalmente diversi.
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
memorizzato, e così via. In sintesi, la definizione del concetto stesso di
_tipo_ diventa in un certo senso indiretta, perché le operazioni che è
possibile effettuare su una variabile, su un parametro e così via dipendono dai
loro contenti in un dato momento dell'esecuzione.

A complicare il tutto, a partire dalla versione 3.5 di Python è possibile
effettuare una sorta di dichiarazione, utilizzando un formalismo
chiamato _type hinting_ che permette di indicare nel codice il
tipo di alcuni elementi del linguaggio (come ad esempio i parametri formali di
una funzione, o il valore da essa restituito). Va sottlineato che la
tipizzazione resta comunque dinamica, ma in questo modo è possibile utilizzare
degli strumenti esterni per effettuare il cosiddetto _type checking_, che
consiste nel verificare _staticamente_ (cioè sulla base di quanto scritto nel
codice) che le variabili vengano utilizzate correttamente. _Editor_ e IDE 
possono per esempio trarre vantaggio dal _type hinting_ per suggerire come
completare il codice o per segnalare dei _warning_. Infine, l'uso del _type
hinting_ rappresenta anche un modo per alleggerire la documentazione del
software prodotto, pertanto tenderò a utilizzarla ove questo aiuterà a leggere
meglio il codice, evitando nel contempo di adottarla quando ciò comporti
un'inutile appesantimento.


## Tipi, classi e oggetti
Python è un linguaggio che supporta pienamente il paradigma di programmazione
orientato agli oggetti, che mette in evidenza i concetti di _classe_ e
_oggetto_ per rappresentare ed elaborare i dati. Semplificando non poco la
trattazione, una classe identifica un'_astrazione_ rispetto a tutti i dati di
un certo tipo, definendo non solo che cosa è necessario memorizzare per creare
un dato (le informazioni che sono chiamate _variabili di istanza_ o membri
della classe), ma soprattutto quali operazioni è lecito eseguire su di esso (i
cosiddetti _metodi_ della classe). In un certo senso, una classe può essere
vista come l'insieme di tutti i dati di un certo tipo, e si utilizza il termine
_oggetto_ per indicare uno di questi specifici dati. Per esempio, una ipotetica
classe `Superhero` potrebbe includere

- una variabile di istanza `secret_identity`, contenente una stringa che
  descrive l'identità segreta;
- due metodi `fly` e `run` che implementano le corrispondenti azioni.
```{margin}
In alcuni linguaggi orientati agli oggetti, i metodi rimpiazzano completamente
le funzioni. Come vedremo più avanti, in Python i due concetti coesistono.
```

Nell'ipotesi che tutto quello che ci interessa relativamente a un supereroe
qualsiasi sia conoscerne l'identità segreta e permettergli di volare o correre,
la classe `Superhero` racchiude tutto quello di cui necessitiamo. Quando
vorremo ragionare in termini di uno specifico supereroe, diciamo Superman,
possiamo creare l'oggetto corrispondente invocando una particolare funzione
che prende il nome di _costruttore_ della classe, che accetta come parametri
i valori per le variabili di istanza e che restituisce un _riferimento_
all'oggetto creato, che è opportuno memorizzare in una variabile. Spesso, il
costruttore ha lo stesso nome della classe stessa, così che la creazione
dell'oggetto verrebbe fatta (ipoteticamente) nel modo seguente, notando che
l'operazione di assegnamento di un valore a una variabile  viene fatto usando
la stessa sintassi di parecchi linguaggi di programmazione:

```python
superman = Superhero('Clark Kent')
```
```{margin}
Questo codice è riportato per esemplificare i concetti di classe, costruttore,
riferimento e oggetto. Non eseguitelo, perché non funzionerebbe!
```

e, in questo caso,

- `Superhero` indica sia la classe, sia il costruttore;
- `'Clark Kent'` rappresenta la stringa utilizzata per la variabile di istanza
  `secret_identity`;
- `superman` è il nome della variabile che conterrà il riferimento all'oggetto
   della classe `Superhero` che modella Superman.

La memorizzazione del riferimento restituito dal costruttore in una variabile
è necessaria perché rappresenta quasi sempre l'unico modo di utilizzare
l'oggetto creato. Ciò viene fatto utilizzando una specifica sintassi alla
quale ci si riferisce con il termine inglese di _dot notation_, perché
richiede di scrivere il riferimento all'oggetto (o, più spesso, la variabile
che lo contiene) seguito dal carattere di punto e dal nome di una variabile
di istanza o di un metodo. Nel primo caso si ottiene un'espressione il cui
valore corrisponde al contenuto della variabile di istanza, e nel secondo
il risultato è l'equivalente di un nome di funzione che è possibile invocare,
specificando eventuali parametri previsti. Tornando all'esempio precedente,
`superman.secret_identity` corrisponde a `'Clark Kent'`, ed è possibile
effettuare l'invocazione `superman.fly()` (nell'ipotesi che il metodo sia
invocabile senza specificare alcun parametro). Anche in questo contesto, il
linguaggio è basato su un _type checking_ dinamico: indipendentemente dalla sua
classe, se a partire da un oggetto è possibile usare la _dot notation_ per
accedere alla variabile d'istanza `secret_identity` e invocare i metodi `fly` e
`run`, questo oggetto è funzionalmente equivalente a un oggetto della classe
`Superhero`, e lo si potrà utilizzare in tutti i contesti pensati per tale
classe[^duck-typing].

```{admonition} Approfondimento: identificatori e regole di stile
Si utilizza il termine _identificatore_ per indicare un nome scelto per
riferirsi univocamente a specifiche entità in un programma, come variabili,
variabili di istanza, classi, funzioni, metodi, parametri e così via. Nel
libro, userò «nome» e «identificatore» in modo intercambiabile, sebbene il
primo termine si possa utilizzare anche per indicare concetti differenti (come
ad esempio il nome di un file).

Da un punto di vista sintattico, per formare un identificatore in Python si
possono utilizzare i caratteri alfabetici maiuscoli e minuscoli (tenendo conto
del fatto che il linguaggio è _case sensitive_: `superman` e `Superman`
rappresentano due identificatori differenti), le cifre e il carattere di
_underscore_ (`_`), con l'unico vincolo di non usare una cifra come carattere
iniziale.

Rispettare la sintassi è obbligatorio, ma è anche buona pratica seguire il più
coerentemente possibile delle _regole di stile_, che di norma stabiliscono
anche come scegliere gli identificatori. Non esiste però uno _standard_ unico:
io farò riferimento alla
[Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/), che
contiene anche un paragrafo
[Naming conventions](https://peps.python.org/pep-0008/#naming-conventions).

Per variabili (di istanza e non), funzioni e metodi, le regole di stile
prevedono il cosiddetto _snake case_: si usano unicamente i caratteri minuscoli
e l'_underscore_, impiegando quest'ultimo solo come separatore in un
identificatore composto da più parole (come in `secret_identity` nel precedente
esempio). L'uso di uno o più _underscore_ all'inizio o alla fine di un nome è
da evitare, perché in contesti specifici conferisce un significato specifico al
codice: nel libro non affronterò situazioni di questo tipo, ma è meglio essere
particolarmente attenti a questo aspetto già quando si imparano le basi del
linguaggio. Questa regola ha comunque delle eccezioni, che metterò in risalto
quando sarà necessario applicarle.

Gli identificatori delle classi andrebbero invece costruiti adottando il
cosiddetto _upper camel case_, e cioè utilizzando solo caratteri alfabetici,
dove le maiuscole servono esclusivamente per marcare l'inizio di ogni parola
(come in `Superhero`). Infine, nonostante Python non preveda il concetto di
_costante_, è possibile usare la variante dello _snake case_ che utilizza
esclusivamente lettere maiuscole (il cosiddetto _screaming snake case_) per
indicare che il contenuto di una variabile non muterà dopo il primo (e unico)
assegnamento che la riguarda.

Anche tenendo conto della sintassi e delle regole di stile, vi è ampia
discrezionalità nella scelta per un identificatore: per esempio, al posto di
`superman` si sarebbero potuti utilizzare `clark_kent`, `hero`, `s`, `s1` o
accozzaglie più o meno intelligibili di caratteri. È però altamente
consigliabile scegliere un nome che aumenti la leggibilità del codice.
```

In realtà, l'unico modo di riferirsi a un tipo di dato in Python è attraverso
l'utilizzo delle classi: non esistono «tipi primitivi», ai quali corrispondono
mere sequenze di byte usate per rappresentare interi, decimali e così via, che
si trovano per esempio in Java. Per esempio, i tipi interi e decimale
fanno riferimento alle classi `int`[^maxint] e `float`, ognuna caratterizzata
dai suoi metodi.
```{margin}
Le classi `int` e `float` rappresentano un esempio di eccezione alla regola
di stile che ho precedentemente menzionato.
```

Ricapitolando, quando si parla di una variabile all'interno di codice scritto
in Python, invece di dire che una variabile contiene un valore di un dato
tipo, sarebbe più corretto parlare di un _nome_ associato a un _riferimento_
che individua univocamente l'oggetto di una classe: la seconda individua
(temporaneamente, a causa della tipizzazione dinamica) il tipo e il primo il
particolare dato che corrisponde alla variabile (in inglese si usa il
verbo _to bind_, che significa «legare», per indicare in modo ancora più forte
questa associazione tra il nome e l'oggetto). Un discorso analogo si può fare
per esempio per i parametri formali di una funzione o di un metodo.
Oggettivamente, questa nomenclatura tende a essere pesante, e infatti nel
gergo comune è diffusa l'abitudine di riferirsi a una variabile (o un
parametro) e all'oggetto&mdash;quando non al valore&mdash;in essa contenuto.


```{admonition} Avvertenza
La programmazione orientata agli oggetti è un argomento molto complesso, e in
questo paragrafo ne ho solo scalfito la superficie, trattando esclusivamente
alcuni aspetti di base che è necessario conoscere per poter comprendere il
codice che presenterò nel seguito e imparare a scrivere in modo autonomo
programmi relativamente semplici che automatizzino le tecniche di analisi dei
dati che introdurrò nei capitoli seguenti. In particolare, non ho parlato di
come sia possibile creare delle classi per riferirsi a tipi di dati
personalizzati, perché questo è un aspetto che non è necessario conoscere per
comprendere con profitto il resto dei contenuti. Padroneggiare questo aspetto
rappresenta una competenza decisamente attesa per un informatico, e auspicabile
anche per un _data scientist_, ma tutto questo è ampiamente al di fuori dello
scopo di questo libro. Per approfondire questi argomenti si può fare
riferimento alla
[specifica parte](https://docs.python.org/3/tutorial/classes.html) della
documentazione ufficiale di Python o alla parte IV in {cite:p}`ramalho`.
```

## Tipi semplici e strutturati

Semplificando un po' il discorso, possiamo suddividere i tipi di dati che
Python mette a disposizione in due grandi categorie:

- i tipi di dati _semplici_, che servono a definire un'informazione di tipo
  atomico, che ha poco senso suddividere ulteriormente, come ad esempio un
  dato numerico intero o decimale;
- i tipi di dati _strutturati_, che vengono utilizzati per aggregare insieme
  più tipi di dati (semplici o strutturati che siano), come gli _array_ o
  gli insiemi.

Nel Paragrafo [Dati semplici](dati-semplici) mi soffermerò sui tipi di dati semplici,
mentre il Paragrafo [Dati strutturati](dati-strutturati) si concentrerà sui principali tipi di
dati strutturati che utilizzerò in seguito. Come accennato poco sopra, la
categorizzazione che descriverò è lungi dall'essere perfetta: da una parte, non
è completa perché Python supporta alcuni tipi di dati, come quelli che
descrivono le funzioni o le classi, che non ricadono naturalmente in nessuna
delle due categorie; dall'altra, è opinabile piazzare alcuni tipi in una
categoria piuttosto che nell'altra: ciò capita per esempio con le stringhe, che
vedremo annoverate tra i tipi semplici ma che possono essere pensate (e
accedute) come una particolare aggregazione di caratteri.



[^duck-typing]: Spesso si utilizza
il termine _duck typing_ per descrivere questo tipo di tipizzazione dinamica,
facendo riferimento a una frase attribuita al poeta americano James Whitcomb
Riley: «when I see a bird that walks like a duck and swims like a duck and
quacks like a duck, I call that bird a duck».

[^maxint]: È interessante notare che l'implementazione della classe `int`
adotta un approccio ad aritmetica con _precisione arbitraria_: il numero di bit
necessari per memorizzare un valore intero non è prefissato, bensì stabilito
dinamicamente in funzione dei valori di volta in volta assegnati. Ciò implica
che non esiste un «più grande» o un «più piccolo» intero memorizzabile, come
in altri linguaggi.