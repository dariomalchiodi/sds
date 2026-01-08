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

(chap_statistica-inferenziale)=
# Statistica inferenziale

Nella prima parte di questo libro abbiamo visto come alcuni aspetti di un
insieme di dati, come per esempio la sua posizione o la sua dispersione attorno
a un valore centrale, possano essere valutati da particolari indici. Questi
indici permettono di riassumere insiemi di dati anche molto grandi e di
descriverli in modo succinto, mettendone in evidenza alcuni aspetti rilevanti.
In linea di principio, l'insieme di dati che viene analizzato può coincidere
con la popolazione, coinvolgendo quindi tutti gli individui ai quali siamo
interessati. In questo caso, le informazioni estratte tramite la statistica
descrittiva ci permettono di trarre conclusioni esatte sui dati osservati. Non
sempre, però, è possibile operare in questo modo, come evidenziato di seguito.

- I dati dell'intera popolazione potrebbero non essere disponibili.
  Se per esempio si sta conducendo un sondaggio in vista di un imminente
  referendum, non tutti i cittadini potrebbero essere propensi a
  dichiarare il proprio orientamento politico.
- Elaborare tutta la popolazione potrebbe richiedere troppe risorse.
  Continuando l'esempio precedente, anche ammettendo che tutti gli elettori
  siano disponibili a rispondere al sondaggio, intervistarli in modo esaustivo
  richiederebbe verosimilmente troppo tempo per ottenere risultati utili, oltre
  a comportare costi probabilmente proibitivi.
- La misurazione di un attributo potrebbe influire sull'individuo. Immaginiamo
  di voler vendere degli _hard disk_ dichiarando il loro tempo medio di
  funzionamento: va da sé che, dopo averne misurato il tempo di vita, un _hard
  disk_ non sarà più funzionante. Se si calcolasse il tempo di funzionamento su
  tutti i dispositivi prodotti, quindi, non ne resterebbe alcuno da vendere.

In casi come questi, è possibile estrarre un campione dalla popolazione e
usarlo per ottenere una _stima_ del valore al quale siamo interessati. Dal
punto di vista logico, procedimenti di questo tipo rientrano nell’ambito della
cosiddetta _inferenza induttiva_, che consiste nel generalizzare a un insieme
più ampio di casi l’informazione ottenuta analizzando un numero limitato di
casi particolari. È proprio questo meccanismo che rende possibile la scoperta
di nuova conoscenza e che sostiene il progresso scientifico fondato sulla
sperimentazione. L’inferenza induttiva è, in questo senso, duale rispetto
all’_inferenza deduttiva_, tipicamente utilizzata nella dimostrazione di
teoremi o nel ragionare su proprietà valide per un insieme generale e
applicarle a un singolo individuo. A differenza di quanto accade con
quest'ultima, però, le conclusioni alle quali si arriva tramite l'inferenza
induttiva non sono certe, e in tal senso si parla di _stima_, intesa come
_approssimazione_. Nel seguito, ci concentreremo su una branca della matematica
che permette di formalizzare un ben specifico processo di inferenza induttiva:
quello che ho delineato qui sopra[^induzione], e che prende il nome di
_statistica inferenziale_. In questo processo, si continua a considerare la
popolazione come un insieme di individui (esattamente come nel
{ref}`chap_dati-e-informazione`), e ci si concentra su di un loro attributo
quantitativo. Il punto cardine della formalizzazione consiste nell'introdurre
una variabile aleatoria che individua indirettamente la popolazione stessa,
come dettagliato nella definizione seguente.

```{prf:definition} Variabile aleatoria indotta da una popolazione
:label: def_induced_population_va

Fissata una popolazione di interesse e un attributo quantitativo che può
essere individuato su ogni individuo di questa popolazione, si definisce la
_variabile aleatoria indotta dalla popolazione_ come la variabile aleatoria $X$
il cui supporto è l'insieme dei valori possibili per l'attributo considerato,
e la cui distribuzione è indotta dal campionamento di un individuo nella
popolazione e dalla successiva misurazione dell'attributo.
```

In altre parole, osservare una specificazione $x$ della variabile aleatoria
$X$ indotta dalla popolazione corrisponde a

1. selezionare un individuo da quest'ultima, secondo un meccanismo che assegna
   a tutti gli individui la stessa probabilità di essere selezionati, 
2. misrurare l'attributo in questione su tale individuo, ottenendo $x$ come
   risultato.

```{prf:example}
:label: ex_si_population

Nel caso del sondaggio demoscopico che ho menzionato sopra, la variabile
aleatoria indotta dalla popolazione è ragionevolmente distribuita all'interno
della famiglia di Bernoulli, supponendo di indicare con $1$ e $0$,
rispettivamente, il fatto di osservare un elettore favorevole o contrario al
quesito posto &mdash; o viceversa. Ciò è dovuto al fatto che l'osservazione di
un individuo nella popolazione ha due soli esiti possibili, e il modello di
Bernoulli è concepito proprio per descrivere situazioni di questo
tipo[^alt-bernoulli]. Pertanto, osservare una specificazione
$x \in \{ 0, 1 \}$ corrisponde ad aver intervistato un elettore che risulta
essere favorevole quando $x = 1$ e contrario altrimenti.


Per quanto riguarda invece il tempo di vita degli _hard disk_, la situazione è
più complicata, perché esistono svariati modelli di distribuzione che potremmo
prendere in considerazione: per essere coerenti con il fenomeno che stiamo
modellando, è naturale richiedere almeno che il supporto della distribuzione
contenga solo numeri non negativi[^normale-non-negativa]. Una scelta possibile,
e spesso utilizzata quando si modellano tempi di durata o di attesa, è quella
di considerare una distribuzione all'interno del modello esponenziale, che
assegna probabilità positive a tutti i valori $t \in \mathbb R^+$. Anche in
questo caso, una specificazione $x \in \mathbb R^+$ indica aver considerato
un _hard disk_ che ha funzionato $x$ unità di tempo prima di rompersi.
```

La variabile aleatoria indotta dalla popolazione permette di formalizzare e
studiare quantitativamente le caratteristiche della popolazione a partire da
osservazioni campionarie, senza dover considerare direttamente la popolazione
stessa, intesa come l'insieme degli individui originari. All'atto pratico,
vedremo che tale insieme non viene mai considerato, perché partiremo
direttamente dalla variabile aleatoria indotta. Come vedremo più avanti, questa
formalizzazione non solo introduce uno schema preciso per inquadrare gli
esperimenti che considereremo, ma soprattutto fornisce degli strumenti per
quantificare l’incertezza associata ai risultati ottenuti, permettendo di
valutare quanto le stime siano affidabili come approssimazioni di valori reali,
ma ignoti.

```{admonition} _
:class: naming

La dicitura «variabile aleatoria indotta dalla popolazione» è precisa, ma tende
ad appesantire la trattazione. Pertanto, nei testi scientifici si adotta spesso
una terminologia più chiara e concisa. In generale, io userò tendenzialmente la
parafrasi «popolazione descritta da una variabile aleatoria $X$», o espressioni
equivalenti. Può capitare però di imbattersi nell'uso ambivalente della parola
«popolazione», che in alcuni casi è riferita all'insieme di individui, e in
altri alla variabile aleatoria indotta. Confido di non avere fatto questo
errore nel libro, salvo rari casi in cui il contesto rende chiaro a quale dei
due significati mi sto riferendo. Quando la distinzione risulta sottile o
rilevante dal punto di vista concettuale, confido di aver precisato
esplicitamente il significato inteso.
```

```{margin}
L'uso dei simboli $X$ e $\tau$ per indicare rispettivamente la variabile
aleatoria indotta dalla popolazione e la quantità ignota è una convenzione,
adottata quando si vuole trattare il problema della stima in modo generale,
senza riferirsi a casi specifici. In situazioni particolari, è ragionevole
utilizzare simboli diversi, scelti in base al contesto.
```
Seguendo una notazione ampiamente diffusa, indicherò con $X$ la variabile
aleatoria che descrive la popolazione, e con $\tau$ la quantità sconosciuta che
vogliamo stimare.


```{prf:example}
:label: ex-parametric-estimate

Nel precedente esempio del sondaggio demoscopico, una scelta ragionevole per
$\tau$ è la frazione degli elettori favorevoli (o non favorevoli) al
quesito del referendum; in modo analogo, nel caso degli _hard disk_, $\tau$ è
un numero non negativo che rappresenta il tempo medio di vita, espresso in
un'unità di misura appropriata (ad esempio ore,  giorni, o numero di
letture/scritture).
```

La statistica inferenziale rappresenta, sotto vari punti di vista, un punto di
incontro tra la statistica descrittiva e il calcolo delle probabilità.
Quest'ultimo considera, per esempio, molte delle proprietà studiate nella
statistica descrittiva per indicare analoghe proprietà di una variabile
aleatoria (o, meglio, della sua distribuzione), e non è un caso che gli indici
utilizzati per descrivere queste proprietà abbiano spesso lo stesso nome. Per
distinguere le quantità calcolate su dati osservati, è quindi necessario
aggiungere l’aggettivo _campionario_. La statistica inferenziale permette di
comprendere appieno questo parallelo, oltre ad approfondire alcuni
concetti che ho introdotto nella statistica descrittiva soprattutto a scopo
operativo e in modo informale.


Per esempio, la media campionaria indica il baricentro dei valori osservati nel
campione, e dunque risulta naturale utilizzarla per valutarne la centralità. Ma
perché le viene data così tanta enfasi, a discapito di altri indici di
posizione? In particolare, perché utilizzarla nonostante la sua mancanza di
robustezza rispetto ai valori fuori scala? Analogamente, consideriamo la
definizione non pienamente intuitiva della varianza campionaria: perché la
somma degli $n$ scarti quadratici rispetto al valore centrale viene divisa per
$n - 1$ e non per $n$, così da ottenere la media aritmetica degli scarti
stessi, che sembrerebbe più sensata per valutare la dispersione? Vedremo come
la statistica inferenziale permette di rispondere a queste domande, facendoci
considerare da un altro punto di vista alcuni degli indici che abbiamo
studiato, e chiarendone il ruolo e le proprietà nel contesto inferenziale.

Come ho già accennato, una volta che è stata definita la variabile aleatoria
$X$ che descrive la popolazione, il punto di partenza per ogni procedura di
inferenza statistica è un _campione_, la cui definizione data nel
{ref}`chap_dati-e-informazione` deve essere riveduta, a fronte
dell'introduzione della variabile aleatoria indotta dalla popolazione.

```{prf:definition} Campione casuale
Data una popolazione descritta da una variabile aleatoria $X$ e un intero
$n \in \mathbb N$, un _campione casuale_ di _grandezza_ (o _taglia_) $n$ è una
sequenza $X_1, \dots X_n$ di variabili aleatorie i.i.d. che seguono la medesima
distribuzione di $X$.
```

Si dice che $X_1, \dots, X_n$ è _estratto_ da una popolazione descritta da $X$.
L'utilizzo di variabili aleatorie, in questo caso, può sembrare fuorviante:
dopo tutto, lo scopo di estrarre un campione è quello di utilizzare i relativi
valori numerici per ottenere una stima. Dunque, perché modellare il campione
come una collezione di variabili aleatorie e non direttamente come una sequenza
di numeri? La risposta a questa domanda è legata al fatto che, in questo modo,
possiamo considerare il campione da due diversi punti di vista:

1. quello che osserva la _realizzazione_ $x_1 , \dots, x_n$, cioè ciò che è
   stato effettivamente misurato, per ottenere una stima concreta di $\tau$;
2. quello che considera il _processo_ che ha portato all'ottenimento del
   campione &mdash; il quale, se ripetuto, può generare dei valori campionari
   differenti.

L'uso delle variabili aleatorie consente di modellare l'incertezza insita nel
secondo punto e di studiare le proprietà delle stime _indipendentemente_ dai
valori effettivamente osservati.


Questo capitolo descrive in modo succinto le due principali branche della
statistica inferenziale: quella _parametrica_, che introduce due modalità di
stima distinte &mdash; puntuale e per intervalli &mdash;, e quella _non
parametrica_. Entrambe sono brevemente descritte nei paragrafi che seguono.

## La statistica inferenziale parametrica

Nella statistica inferenziale parametrica, la distribuzione della variabile
aleatoria $X$ che descrive la popolazione si suppone nota, a meno di uno o più
parametri, e la quantità $\tau$ che vogliamo stimare dipende da questi
parametri.

```{prf:example}
:label: ex_possible_distr

Riprendiamo l’{prf:ref}`ex_si_population`, nel quale erano indicate soltanto le
famiglie delle distribuzioni per le popolazioni considerate: Bernoulli per il
sondaggio ed esponenziale per il tempo di vita. Se inquadriamo ora i due
problemi nell'ambito della statistica inferenziale parametrica, avremo
rispettivamente $X \sim \mathrm B(p)$ e $X \sim \mathrm E(\lambda)$, con
$p \in [0, 1]$ e $\lambda \in \mathbb R^+$ ignoti.

Consideriamo ora l’{prf:ref}`ex-parametric-estimate`: nel primo caso, la
quantità da stimare coincide con il parametro ignoto, ossia $\tau = p$, mentre
nel secondo caso vale $\tau = 1 / \lambda$: la quantità da stimare dipende
quindi dal parametro ignoto, ma non coincide con esso.
```

La stima può essere effettuata secondo due approcci principali,
brevemente descritti di seguito e approfonditi rispettivamente nel
{ref}`sec_stime-puntuali` e nel {ref}`chap_stime-per-intervalli`.

- Il modo più semplice consiste nel fornire una _stima puntuale_, ossia un
  singolo valore numerico $\hat\tau$, calcolato a partire dal campione estratto
  e che si suppone non si discosti eccessivamente da $\tau$.
```{margin}
Questa definizione nasconde delle sottigliezze, come spiegato in dettaglio nel
{ref}`sec_intervalli-fiduciari`.
```
- Un approccio alternativo consiste nell'indicare una
  _stima per intervalli_, nella quale l'approssimazione è fornita sempre
  partendo dal campione, ma   specificando congiuntamente un _intervallo
  fiduciario_ e un _livello fiduciario_. Il primo è un intervallo di valori
  reali, mentre il secondo è un valore in $(0, 1)$, che indica quanto sia
  affidabile affermare che l’intervallo contenga $\tau$.

```{prf:example}
:label: ex_possible_estimate

Con riferimento all’{prf:ref}`ex-parametric-estimate`, ogni valore
$\hat\tau \in [0, 1]$ rappresenta una stima puntuale formalmente possibile
per la percentuale di elettori, così come un qualsiasi valore in $\mathbb R^+$
lo è per il tempo di vita degli _hard disk_. 

Considerando invece l'ambito della stima per intervalli, e focalizzandoci
solamente sul secondo caso considerato, $[3, 7]$ potrebbe rappresentare
un intervallo fiduciario di livello $0.95$, così come potrebbe rappresentarlo
$[2.4, 9.1]$, supponendo di misurare il tempo in anni.
```

```{margin}
Vedremo che, come è intuitivo aspettarsi, la dimensione del campione
può giocare un ruolo molto importante nel governare l'errore
insito nella stima.
```
L'esempio precedente suggerisce un fatto fondamentale: il valore $\hat\tau$ di
una stima puntuale non garantisce, di per sé, alcun livello sulla bontà
dell'approssimazione fornita per $\tau$. Vale la pena aggiungere un'ulteriore
considerazione. Anche qualora venga garantita la qualità della procedura
utilizzata per stimare $\tau$ &mdash; per esempio mediante alcuni dei criteri
che vedremo nel prossimo capitolo &mdash; non esiste un valore _giusto_ in
senso assoluto per la stima puntuale fornita. Questo deriva dal fatto che
$\hat\tau$ è il valore restituito da una statistica che dipende dal campione
estratto. Perciò, a ogni campione estraibile dalla popolazione fissata
corrisponderà una stima potenzialmente diversa. In altre parole, con alcune
eccezioni trascurabili, tutte le stime puntuali contengono un errore intrinseco
dovuto al campionamento. 

Considerazioni analoghe valgono per le stime per intervalli, sebbene la natura
più complessa di un intervallo fiduciario veicoli anche informazioni indirette
sulla bontà della stima. Intuitivamente, più l'intervallo è ampio, meno precisa
sarà la stima. Inoltre, indipendentemente dall'ampiezza, un livello fiduciario
più elevato indica una stima più affidabile. Tuttavia, come già accennato, il
ruolo del livello fiduciario va compreso attentamente: infatti, come vedremo in
dettaglio nel {ref}`sec_intervalli-fiduciari`, il suo valore non indica la
probabilità che $\tau$ sia contenuto nell'intervallo, ma la probabilità che la
procedura di stima produca un intervallo che effettivamente contenga $\tau$.


## La statistica inferenziale non parametrica

Infine, vale la pena sottolineare che la statistica inferenziale può essere
declinata anche in senso _non parametrico_. Questo approccio è utile quando
l'incertezza non riguarda solo uno o più parametri, ma è l'intera distribuzione
della popolazione a essere sconosciuta. Tuttavia, un'analisi dettagliata di
questo argomento esula dalla trattazione di questo libro. Nel
{ref}`chap_statistica-non-parametrica` mi limiterò a introdurre alcuni aspetti
di base di questa branca, collegandoli ad alcuni concetti collegati che ho già
trattato nella parte sulla statistica descrittiva.



[^induzione]: Vale la pena sottolineare che l'inferenza induttiva si è
sviluppata in modo indipendente dalla statistica inferenziale, e in un contesto
diverso: quello dell'epistemologia, una branca della filosofia che si concentra
sulla conoscenza, e in particolare sulla conoscenza scientifica. La statistica
inferenziale formalizza un modo possibile di eseguire inferenze induttive con
la precisione tipica della matematica, ma esistono molti altri modi di fare
inferenza induttiva, dalle generalizzazioni alle analogie. Peraltro, gli
scienziati che hanno fondato la statistica inferenziale &mdash; come Fisher,
Neyman e Pearson &mdash; non avevano come obiettivo quello di replicare le
riflessioni epistemologiche sull’induzione; per loro, l’interesse principale
era quantificare l’incertezza e controllare il comportamento delle procedure di
stima, piuttosto che giustificare filosoficamente il passaggio dai casi
particolari alle conclusioni generali.

[^alt-bernoulli]: Naturalmente, esistono infinite distribuzioni di probabilità
il cui supporto contiene esattamente due valori distinti, e ognuna di queste
potrebbe essere utilizzata per modellare questo specifico caso. Da un punto
di vista formale, l'unica cosa che cambierebbe è il modo nel quale dovremmo
_codificare_ il fatto di essere favorevoli o contrari al quesito. Usare una
distribuzione di Bernoulli è però più vantaggioso, perché abbiamo già studiato
questo modello e conosciamo parecchie delle sue proprietà (come il valore
atteso, o la funzione di ripartizione), che per un'altra distribuzione con due
specificazioni dovrebbero invece essere ricavare ex novo.

[^normale-non-negativa]: In realtà, esistono situazioni nelle quali questo
vincolo può essere trascurato, scegliendo la distribuzione della popolazione
in modo tale che $\mathbb P(X < 0)$ sia abbastanza piccolo da rendere il
corrispondente evento, dal punto di vista pratico, paragonabile all'evento
impossibile.