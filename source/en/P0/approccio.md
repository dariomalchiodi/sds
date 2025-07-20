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
  heading: true
  heading_1: true
  heading_2: false

  figure:
    template: Figura 1.%s
  table:
    template: Tabella 1.%s
title: 1.2. Approccio
---

(sec:approccio)=
Mi è sempre risultato facile apprendere nuovi concetti mettendoli in pratica
in un contesto che potesse essere facilmente esplorato e controllato. Quando,
anni fa, ho iniziato a insegnare, mi è sembrato naturale usare lo stesso
approccio, adottando in modo inconsapevole un metodo didattico che solo più
tardi ho scoperto essere codificato nella metodologia del _learning by doing_
{cite:p}`freire1982`. Questo libro cerca di seguire la stessa filosofia,
introducendo fin da subito&mdash;ove possibile&mdash;i singoli argomenti
all'interno di un contesto applicativo.

```{margin}
L'uso della fantascienza per introdurre concetti scientifici non è
particolarmente insolito: due esempi abbastanza noti sono «La Fisica
di Star Trek» {cite:p}`krauss` e «La Fisica dei Supereroi»
{cite:p}`kakalios`[^note].
```
Per dare coerenza alla trattazione, ho deciso di contestualizzare in uno stesso
dominio gli esempi da affiancare alle parti più teoriche.
Il perimetro nel quale ho scelto di muovermi è il multiverso dei supereroi.
Potrebbe sembrare un controsenso, vista la filosofia che ho appena dichiarato:
i supereroi sono personaggi di un ambito narrativo non reale&mdash;parecchio
_fiction_, peraltro. Poter applicare un concetto a un contesto, però, prescinde
dall'effettiva realizzabilità fisica di quest'ultimo: serve solo specificare in
modo chiaro, coerente e preciso le ipotesi che descrivono una data situazione.
Ciò permette di calarsi metaforicamente in questa stessa situazione, di usare
la matematica per modellarla e l'informatica per simularla, così da poterla
esplorare utilizzando il metodo scientifico e, sperabilmente, ricavare
informazioni, prendere decisioni e così via. Oltre a essere molto divertente,
riferirsi a un mondo inesistente ha anche un altro vantaggio: permette a chi
impara di non stabilire un collegamento diretto tra l'istanza di un problema e
i metodi risolutivi da utilizzare, favorendo un apprendimento incentrato
sull'uso _critico_ di metodi e strumenti.


Nonostante mi sia imbarcato in questa impresa, non sono un
esperto di supereroi. Chiedo quindi preventivamente scusa a chi ne sa più
di me per tutte le imperfezioni e gli errori che potrei avere inserito,
sperando che questi non pregiudichino la comprensione dei concetti e degli
esempi descritti. Nonostante io sia un po' più esperto di analisi dei dati,
di calcolo delle probabilità e di statistica, non posso escludere di
avere fatto errori in generale, anche se in questo caso sono confidente di non
averne fatti troppi.

Il lavoro di scrittura è comunuque _in progress_, e
verosimilmente lo sarà ancora per parecchio tempo: segnalatemi refusi ed
errori, e più in generale esempi e materiale che pensate possano arricchire
quanto ho scritto, tenendo presente che immagini, dati e così via possono
essere pubblicati solo se sono coerenti con la licenza _Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International_
([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en))
con la quale è distribuito questo libro.
```{margin}
Il modo più pratico per inviarmi queste segnalazioni è quello
di sottoporre _issue_ (per segnalare errori o suggerire miglioramenti)
o _pull request_ (per proporre modifiche ai contenuti) al
[repository](https://github.com/dariomalchiodi/sds) nel quale ho
organizzato i contenuti di questo libro. Ciò richiede
familiarità con [git](https://www.git-scm.org), lo strumento di _source
control management_ che utilizzo per i miei progetti _software_.
```


### Ringraziamenti

Alcune persone hanno letto e commentato quello che ho scritto, contribuendo
in modo fondamentale al risultato finale: Alessandro Di Giorgi mi ha aiutato
a limare la trattazione matematica in alcuni punti. Nicola Ludwig ha
impreziosito una mia incursione nel mondo della fisica. Marco De Petri, Matteo
Princisgh e Nicolò Rosati hanno accuratamente letto le bozze e trovato
tante imperfezioni alle quali spero di avere rimediato. Ringrazio tutte e tutti
per avere dedicato un po' del loro tempo e delle loro energie a questo lavoro,
puntualizzando che che errori e imprecisioni che dovessero essere rimasti sono
da attirbuirsi interamente a me.

È poi doveroso ringraziare Laura Ripamonti, che tanti anni fa ha instillato in
me l'idea di usare i supereroi come esempio didattico, Serena Paolo e Paolo
Boldi, che per primi e per motivi diversissimi (ma non così diversi) sono
venuti a conoscenza della mia idea di scrivere un libro, e per motivi uguali
(ma non così uguali) mi hanno spronato a farlo. A tutte queste persone, e a chi
inevitabilmente sto dimenticando, voglio esprimere la mia riconoscenza per il
supporto che hanno saputo darmi.

(sec:imparare-e-programmare)=
## Imparare \*e\* programmare

Come descritto nel paragrafo precedente, introdurrò i concetti affiancandoli
(o facendoli precedere) da esempi. Dove possibile, mostrerò anche delle
_implementazioni_ utilizzando un linguaggio relativamente moderno: in
particolare, farò riferimento a [Python](https://www.python.org) e al
relativo _data science stack_, costituito dai package che sono ampiamente
utilizzati, al tempo in cui scrivo, dalla comunità open source che fa
riferimento all'analisi dei dati[^librerie]. È quindi altamente consigliata una
competenza di base nella programmazione degli elaboratori.
```{margin}
Questo libro rappresenta l'evoluzione di una serie di dispense pensate per
studenti del secondo anno delle lauree triennali di area informatica, dunque
farò riferimento al livello di conoscenza di programmazione che si apprende al
primo anno nelle stesse lauree, o in lauree di aree affini.
```

Il Capitolo [Elaborare i dati con Python](introduzione-a-python) contiene una
descrizione a livello medio-alto delle funzionalità di Python che sono
utilizzate, e può essere utilizzato per mettersi in pari da chi sa già
programmare, ma non conosce questo linguaggio. Una lettura di questo capitolo è
comunque consigliata a tutti, al fine di familiarizzare con le convenzioni che
utilizzo per scrivere codice.

Questo libro è scritto utilizzando una tecnologia che permette di inserire
dei contenuti generati tramite l'esecuzione di codice python. Questo codice
è nascosto quando serve a produrre per esempio tabelle o grafici, mentre è
esplicitamente mostrato in tutti i casi nei quali chi legge viene guidato
nell'implementazione di uno o più concetti spiegati nel testo. In ogni caso,
l'intero codice sorgente che ho scritto per produrre il libro è scaricabile
sia dal [repository](https://github.com/dariomalchiodi/sds) associato, sia
cliccando l'icona ![download icon](images/download.svg) a inizio pagina. Va
notato che, in entrambi i casi, quello che viene scaricato sono dei file che
alternano il codice Markdown che specifica i contenuti testuali con il codice
python, ed è quindi necessario separare quest'ultimo per poterlo eseguire.
Nonostante questo modo di procedere sia un po' macchinoso, incoraggio tutti a
usufruire di questa opportunità, non limitandosi a leggere passivamente il
testo, e nemmeno a eseguire il codice in modo pedissequo, ma ad analizzarlo,
comprenderlo, modificarlo (valgono anche le modifiche che permettono di capire
meglio il codice!)&mdash;insomma, _giocarci_ in un'ottica _hacker_, nel senso
originale del termine [^hacker]. In realtà è anche possibile giocare con il
libro senza necessariamente dover comprendere il codice ed eseguirlo: come
mostrato nel Paragrafo [Uno sguardo d'insieme](uno-sguardo-di-insieme), una
parte dei contenuti è interattiva, e la sua manipolazione è pensata proprio per
facilitare la comprensione dei concetti introdotti.
```{margin}
Il libro è stato generato utilizzando [MyST](https://mystmd.org/), che
comprende sia una variante del formato testuale <wiki:Markdown>, sia il sofware
che permette di tradurre il codice corrispondente nelle pagine HTML che
state leggendo.

L'utilizzo delle componenti interattive è basato su alcune tecnologie (in
particolare, [JupyterLite](https://github.com/jupyterlite/jupyterlite))
che sono al momento ancora in una fase preliminare di sviluppo, ma che hanno
il grande vantaggio di non richiedere alcuna installazione manuale. D'altro
canto, è spesso necessario armarsi di pazienza e assicurarsi di utilizzare uno
dei browser web supportati.
```


Molto spesso cerco di guidare il lettore in una vera e propria implementazione
degli strumenti fondamentali, soprattutto nella prima parte, relativa alla
statistica descrittiva. Il risultato al quale arrivo non è da considerarsi al
livello delle librerie professionali: da una parte, lo scopo è quello di
concentrarsi sugli aspetti fondamentali per facilitare l'apprendimento di uno o
più concetti. Dall'altro, queste implementazioni non sono pensate per essere
utilizzate in ambito lavorativo: esattamente come è ragionevole che uno
sviluppatore abbia imparato a scrivere da zero i principali algoritmi di
ordinamento (e, se dovesse servire, sia in grado di farlo), ma che faccia in
seguito riferimento alle loro implementazioni in una libreria, ottimizzate e
validate sicuramente meglio di quanto un singolo possa ragionevolmente fare in
autonomia. In quest'ottica, subito dopo le implementazioni  «fai da te», i
lettori sono indirizzati all'uso di librerie allo stato dell'arte.

In linea di principio, anche chi non sa programmare gli elaboratori può
leggere questo libro, saltando semplicemente le parti che contengono,
descrivono e discutono il codice. Ma in questo caso è opportuno valutare bene
il rischio di non apprendere i contenuti in modo ottimale, tenuto conto del
fatto che buona parte del libro è stata scritta alternando testo e codice.
A questo tipo di lettori consiglio di prendere in considerazione testi scritti
usando un approccio più tradizionale, come per esempio:

- Probabilità e Statistica per le scienze e l'ingegneria, di Sheldon Ross
  {cite:p}`ross`,
- Introduzione alla statistica di Marylin K. Pelosi, Theresa M. Sandifer,
  Paola Cerchiello e Paolo Giudici {cite:p}`pelosi`.


Va anche messo in guardia chi non sa programmare e si trova davanti alla
tentazione di leggere questo libro per apprendere a farlo, magari mentre in
contemporanea impara ad analizzare dati. Questo __non è__ un libro per imparare
a programmare, ma piuttosto un libro per imparare programmando, usando la
capacità di scrivere codice per arricchire il processo di apprendimento di
un'altra materia. Si dice che non si è veramente capita una cosa se non si è
in grado di spiegarla alla propria nonna[^cite-granny]: faccio mia questa
massima, sperando di non distorcerla troppo dicendo che non si è veramente
capito un concetto tecnico se non si è in grado di implementarlo scrivendo un
programma. Se si vuole però seguire questa filosofia, bisogna già
avere imparato a scrivere _software_, e questa è una competenza che richiede
tempo, energia e del materiale dedicato all'apprendimento della materia.
Anche in questo caso, ci sono parecchi libri che possono essere utilizzati
con profitto, per esempio:

- [Pensare in Python](https://github.com/AllenDowney/ThinkPythonItalian/blob/master/thinkpython_italian.pdf), di Allen B. Downey {cite:p}`downey`.
- Programmazione in C, di Kim N. King {cite:p}`king`,
- Programmare in Go, di Ivo Balbaert {cite:p}`balbaert`.

Ho volutamente messo nell'elenco precedente tre volumi più o meno recenti,
e soprattutto ognuno dedicato a un linguaggio diverso: lo scopo, in questo
caso, è infatti quello di imparare le basi della programmazione e non i
dettagli di un linguaggio specifico. Infine, questo paragrafo fa riferimento
solamente a libri scritti in italiano, ma è sempre da considerare la
possibilità di studiare sulla versione originale di un libro quando questa
è scritta in inglese, o quando esiste una versione in inglese specificamente
concepita per studenti di madre lingua non inglese.

## Convenzioni

Per quanto detto nel paragrafo precedente, spesso inframmezzerò il testo con
del codice, non tanto al fine di eseguirlo, ma più per uno scopo illustrativo
(per esempio, per indicare i letterali `true` e `false` come unici valori
possibili per il tipo di dati `bool`). In questo caso, utilizzerò un carattere
tipografico non proporzionale con un colore diverso da quello del
testo principale. Quando invece sarà necessario mostrare una o più righe di
codice pensate per essere eseguite da chi legge, mostrerò queste righe 
all'interno di un riquadro che ricorda la tipica _cella di codice_ in un
_notebook_. Anche in questo caso utilizzerò un carattere tipografico non
proporzionale, ma la colorazione del testo sarà fatta in modo da evidenziare
dei particolari elementi nel codice (come variabili, letterali, parole chiave
e così via, analogamente a quanto normalmente fatto dai moderni IDE). Inoltre,
il codice risulterà staccato rispetto al testo principale, come nell'esempio
che segue.
```{margin}
È pratica comune utilizzare un carattere tipografico non proporzionale (nel
quale cioè tutti i glifi utilizzati per rappresentare una lettera hanno la
stessa larghezza) per visualizzare codice, input e output, per una serie di
motivi che ottimizzano la leggibilità del codice stesso, come la maggiore
facilità di indentare le istruzioni, il minor rischio di non distinguere tra
caratteri simili come 1 e l.
```

```{code-cell} ipython3
:tags: [remove-input]
age = 24
```

```{code-cell} ipython3
:tags: [remove-output]
print(age <= 42)
```

Di norma, visualizzerò l'eventuale output dell'esecuzione all'interno di
un'apposita _cella di output_, accodata a quella di codice e mostrata come
di seguito.

```{code-cell} ipython3
print(age <= 42)
```

Infine, utilizzerò uno stile specifico per evidenziare nel testo alcune
componenti particolari, come esemplificato qui sotto.

```{admonition} Nomenclatura
:class: naming
Questo tipo di area contiene delle note relative alla nomenclatura utilizzata
in un particolare ambito, o alla descrizione di diciture alternative rispetto
a quelle introdotte.
```

```{prf:definition}
:label: segnaposto-definizione
:nonumber: true
In questa area vengono definiti in modo formale uno o più concetti.
```
```{margin}
Definizioni, esempi e così via saranno normalmente numerati, e spesso
accompagnati da un nome specifico racchiuso tra parentesi.
```

```{prf:example}
:label: segnaposto-esempio
:nonumber: true
Questa area racchiude un esempio.
```
```{margin}
Le diciture «Definizione», «Esempio», «Teorema» e così via non sono al momento
localizzate dal _software_ che uso per generare le pagine HTML. Portate
pazienza.
```

````{prf:theorem}
:label: segnaposto-teorema
:nonumber: true
Questa area contiene la tesi di un teorema.
````

```{prf:corollary}
:label: segnaposto-corollario
:nonumber: true
Questa area contiene la definizione di un corollario.
```

```{prf:lemma}
:label: segnaposto-lemma
:nonumber: true
Questa area contiene la definizione di un lemma.
```

````{prf:proof}
:nonumber: true
In questa area viene inserita la dimostrazione di un teorema, di un corollario
o di un lemma.
````
```{margin}
Per alcuni dei teoremi ometterò la relativa dimostrazione. Ciò capiterà quando
sarà importante introdurre un risultato teorico rilevante, sebbene la sua
dimostrazione richieda conoscenze matematiche avanzate.
```


## Notazione

La {numref}`tab-notazione` elenca le principali notazioni che utilizzerò nelle
formule matematiche.

```{table} Notazione utilizzata nel testo per le formule matematiche.
:name: tab-notazione
:align: center
:class: [full-width]

|  Simbolo                      | Significato |
|:------------------------------|:------------|
| $\mathbb N$                   | insieme dei numeri naturali                                        |
| $\mathbb Z$                   | insieme dei numeri interi                                        |
| $[a..b]$                      | intervallo discreto dei numeri interi compresi tra $a$ e $b$ (estremi inclusi) |
| $\mathbb R$                   | insieme dei numeri reali                                        |
| $[a, b]$                      | intervallo chiuso dei numeri reali compresi tra $a$ e $b$ |
| $(a, b)$                      | intervallo aperto dei numeri reali compresi tra $a$ e $b$ |
| $[a, b)$, $(a, b]$            | intervalli semiaperti dei numeri reali compresi tra $a$ e $b$ |
| $A = \{ a_1, \dots a_n \}$    | insieme/evento composto dagli elementi/esiti $a_1, \dots, a_n$ |
| $a \in A$                     | elemento $a$ dell'insieme $A$                                      |
| $(a_1, \dots, a_n)$           | disposizione o permutazione composta dagli elementi $a_1, \dots, a_n$ |
| $n!$                          | fattoriale del numero intero $n$                                   |
| $\binom{n}{k}$                | coefficiente binomiale («$n$ su $k$») di $n$ oggetti in $k$ posti              |
| $p_n$                         | numero di permutazioni semplici di $n$ elementi                    |
| $P_{n; n_1, \dots, n_k}$      | numero di permutazioni con ripetizione di $n$ elementi distinguibili a gruppi contenenti $n_1, \dots, n_k$ oggetti |
| $\{ a_1, \dots, a_n \}$       | combinazione composta dagli elementi $a_1, \dots, a_n$             |
| $D_{n, k}$                    | disposizioni con ripetizione di $n$ oggetti in $k$ posti           |
| $d_{n, k}$                    | disposizioni senza ripetizione di $n$ oggetti in $k$ posti         |
| $c_{n, k}$                    | combinazioni semplici di $n$ oggetti in $k$ posti                  |
| $C_{n, k}$                    | combinazioni con ripetizione di $n$ oggetti in $k$ posti           |
| $S \subseteq T$               | sottoinsieme/sottoevento $S$ di un insieme/evento $T$          |
| $\Omega$                      | insieme universo / spazio degli esiti                              |
| $A \rightarrow B$             | evento/proposizione $A$ implica evento/proposizione $B$    |
| $A \leftrightarrow B$         | evento/proposizione $A$ coimplica evento/proposizione $B$  |
| $S \cup T$                    | unione degli insiemi/eventi $S$ e $T$                            |
| $S \cap T$                    | intersezione degli insiemi/eventi $S$ e $T$                      |
| $S \backslash T$              | differenza tra l'insieme/evento $S$ e l'insieme/evento $T$     |
| $S \ominus T$                 | differenza simmetrica tra gli insiemi/eventi $S$ e $T$            |
| $A \vee B$                    | disgiunzione logica tra le proposizioni $A$ e $B$                  |
| $A \wedge B$                  | congiunzione logica tra le proposizioni $A$ e $B$                  |
| $\mathscr E$                  | esperimento casuale                                                |
| $\omega \in \Omega$           | esito di un esperimento casuale                                    |
| $\{ \omega \}$                | evento elementare                                                  |
| $\mathsf A$                   | algebra degli eventi                                               |
| $2^A$                         | insieme delle parti dell'insieme $A$                               |
| $\mathbb P$                   | funzione di probabilità                                            |
| $\mathbb P(E)$                | probabilità dell'evento $E$                                        |
| $\mathbb P(E\|F)$             | probabilità condizionata dell'evento $E$ dato l'evento $F$         |
| $\mathbb E(X)$                | valore atteso della variabile aleatoria $X$                        |
| $\mathbb E(g(X))$             | valore atteso della funzione $g$ della variabile aleatoria $X$     |
| $\mathbb E(g(X, Y))$           | valore atteso della funzione $g$ delle variabili aleatorie $X$ e $Y$ |
| $a \coloneqq b$              | $a$ è definito come uguale a $b$                                   |
```

## Utilizzo all'interno di un insegnamento

Questo libro nasce dall'evoluzione di una serie di dispense che ho utilizzato
negli ultimi anni a corredo dei libri di testo che ho adottato per
l'insegnamento di «Statistica e analisi dei dati» per il corso di Laurea in
Informatica erogato dall'Università degli Studi di Milano. Queste dispense
trattavano sia gli aspetti più _computazionali_ delle lezioni, dunque quelle
direttamente incentrate sulla comprensione e sulla scrittura di codice, sia
alcuni argomenti che non trovano posto nella trattazione fatta nei libri di
testo che avevo adottato.

Nei corsi di Laurea in area informatica, l'insegnamento delle tematiche alla
base dell'analisi dei dati è tipicamente affidato a un unico insegnamento
fondamentale del secondo anno, nel quale si abbracciano sia gli aspetti teorici
del calcolo della probabilità e della statistica matematica, sia quelli più
pratici legati alla statistica descrittiva. Risulta quindi difficile reperire
materiale bibliografico, perché queste discipline sono spesso oggetto di
insegnamenti differenti nell'ambito, per esempio, dei corsi in area matematica.
Coerentemente, il panorama dei libri di testo vede spesso ottimi volumi, ma
dedicati a una sola di queste discipline, o opere che focalizzano l'interesse
su una di esse, sacrificando la trattazione delle altre. Non sono invece
ancora riuscito a trovare un libro di testo che desse a queste tre aree
il peso relativo che io assegno loro nelle mie lezioni.
È per questo motivo che ho deciso, via via che la «massa critica» delle
dispense cresceva, di scrivere un libro che evitasse l'adozione di due o più
testi differenti, da affiancare in ogni caso a dispense che colmassero le lacune
risultanti.

I contenuti sono organizzati secondo il filo logico che seguo durante le mie
lezioni. La prima parte si concentra sulle basi computazionali, introducendo
Python e le relative librerie utilizzate all'interno del libro. Nella seconda
parte, dedicata all'analisi dei dati nel senso più pratico del termine,
introduco i principali argomenti della statistica descrittiva e i relativi
strumenti nell'ottica di un loro utilizzo diretto, scrivendo codice Python e
analizzando un _dataset_ di riferimento. Segue una parte sul calcolo delle
probabilità, dedicata a esporre i principali concetti legati alla modellazione
dell'incertezza in senso probabilistico. L'ultima parte espone infine le basi
della statistica inferenziale, focalizzandosi sull'inferenza parametrica. Nella
trattazione ho cercato di limitare l'uso del formalismo matematico allo stretto
necessario per introdurre gli argomenti in modo rigoroso. I paragrafi il cui
titolo è contrassegnato da un asterisco includono approfondimenti e materiale
addizionale che possono essere trascurati&mdash;fondamentalmente, tutti gli
argomenti che per limiti di tempo non riesco a spiegare in aula ma che
consiglio vivamente agli studenti che volessero approfondire la conoscenza
della disciplina, soprattutto nell'ottica di un proseguimento degli studi a
livello magistrale.


````{aside}
```{figure} ../images/whistle.jpg
---
name: fig-whistle
height: 100px
---
Un fischietto Cap’n Crunch Bo’sun (immagine del Heinz Nixdorf
MuseumsForum, distribuita sotto licenza
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/))
```
````
[^note]: Userò le note a margine per dei commenti che ritengo importanti
ma che non devono appesantire la lettura dei paragrafi corrispondenti.
Relegherò invece nelle note a fine testo tutti gli approfondimenti che
possono essere tralasciati a una prima lettura.
[^librerie]: Il repository associato a questo libro contiene un
[file](https://github.com/dariomalchiodi/sds/blob/main/requirements.in)
che elenca tutte le librerie utilizzate per generare i contenuti, incluse
quelle necessarie per eseguire il codice.

[^hacker]: Il termine _hacker_ viene oggigiorno utilizzato nel linguaggio
comune dandogli un'accezione negativa, che essenzialmente lo accomuna a chi
persegue intenti dolosi scrivendo o modifcando _software_, o in generale
sfruttando delle falle di sicurezza al fine di utilizzare in modo improprio
delle tecnologie informatiche esistenti. In realtà, l'uso di questo termine
nell'inglese moderno viene fatto risalire intorno al 1960, conferendogli
però una connotazione più neutra, e non direttamente collegata all'informatica:
quella di indicare una persona con il talento di comprendere in profondità il
funzionamento di un sistema, e dunque di essere in grado di controllarlo al
punto di poterlo utilizzare in modo diverso rispetto agli scopi per cui il
sistema era stato progettato. Giusto per citare un esempio, uno dei primi
_hack_ famosi&mdash;peraltro illegale&mdash;riguardava l'uso del
«Cap’n Crunch Bo’sun Whistle» (un fischietto che si trovava in regalo nelle
scatole di una famosa marca di cereali, mostrato in @fig-whistle) per fare
telefonate interurbane o internazionali gratuite con alcuni telefoni pubblici
negli Stati Uniti. Uno degli ambienti nei quali la controcultura hacker ha
iniziato a svilupparsi è quello del Massachusetts Institute of Technology
(MIT): la prima traccia scritta del termine «hacking» fa riferimento al verbale
di una riunione del 1955 del [Tech Model Railroad Club](http://tmrc.mit.edu/),
che riuniva studenti appassionati di modellismo ferroviario. Solo più
recentemente è avvenuta un'identificazione rispetto al mondo informatico.

[^cite-granny]: Risulta complicato risalire all'autore di questa massima:
c'è chi la attribuisce ad Einstein, chi a Feynmann e chi a Rutherford (pare
dunque che ci sia consenso sul contesto delle scienze fisiche);
ci sono anche varianti in cui la nonna è sostituita da un bambino, o&mdash; per
qualche motivo&mdash;perfino da un barista.
