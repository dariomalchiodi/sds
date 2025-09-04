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

(chap:statistica-inferenziale)=
# Statistica inferenziale

Nella prima parte di questo libro abbiamo visto come alcuni aspetti di un
insieme di dati, come per esempio la sua posizione o la sua dispersione
attorno a un valore centrale, possano essere valutati da particolari indici.
Questi indici permettono di considerare dati di dimensioni anche
ragguardevoli, e di descriverli in modo succinto estraendo da essi delle
informazioni rilevanti. In linea di principio, l'insieme di dati che viene
analizzato può coincidere con la popolazione, coinvolgendo quindi tutti gli
individui ai quali siamo interessati. In questo caso, le informazioni estratte
tramite la statistica descrittiva ci permettono di trarre delle conclusioni
_esatte_ sui dati. Non sempre, però, è possibile operare in questo modo, come
evidenziato di seguito.

- I dati dell'intera popolazione potrebbero non essere disponibili.
  Se per esempio si sta conducendo un sondaggio in vista di imminenti
  elezioni amministrative, non tutti i cittadini potrebbero essere propensi a
  dichiarare il proprio orientamento politico.
- Elaborare tutta la popolazione potrebbe richiedere troppe risorse.
  Continuando l'esempio precedente, anche ammettendo che tutti gli elettori
  siano disponibili a rispondere al sondaggio, intervistarli in modo esaustivo
  richiederebbe verosimilmente troppo tempo per avere dei risultati in tempo
  utile, richiedendo inoltre dei costi probabilmente proibitivi.
- La misurazione di un attributo potrebbe influire sull'individuo. Immaginiamo
  di voler vendere degli _hard disk_ dichiarando il loro tempo medio di
  funzionamento: per definizione, un _hard disk_ non sarà più funzionante
  dopo avere effettuato la misurazione del suo tempo di vita, pertanto se
  si calcolasse il tempo medio di funzionamento su tutti i dispositivi
  prodotti, non ne resterebbe alcuno da vendere.

In casi come questi, è possibile estrarre un campione dalla popolazione e
valutare un indice di interesse, che prenderà il nome di _stimatore_ o
_statistica_, assumendo che il risultato $\hat\tau$ non si discosti troppo
dal valore esatto $\tau$ che si sarebbe ottenuto lavorando su tutta la
popolazione. In tal senso, che $\hat\tau$ è una _stima_ di $\tau$, e pertanto
sarebbe auspicabile poter dire qualcosa relativamente alla bontà di questa
stima. Più in generale, questo tipo di procedimento ricade nell'ambito della
cosiddetta _inferenza induttiva_, nella quale l'informazione ottenuta
ragionando su alcuni casi particolari (quelli contenuti nel campione) viene
generalizzata a un insieme di casi più esteso (la popolazione). L'inferenza
induttiva rappresenta un processo di costruzione della conoscenza duale
rispetto ai procedimenti _deduttivi_ (utilizzati tipicamente nella
dimostrazione di teoremi, o, più semplicemente nel considerare proposizioni
vere per un insieme di individui e declinarle su di uno specifico individo).
A differenza di quanto accade con quest'ultima, però, le conclusioni alle
quali si arriva tramite l'inferenza induttiva non sono certe: come detto
prima, calcolare la media campionaria sugli elementi di un campione fornisce
un risultato diverso rispetto a quello che si otterrebbe effettuando il
medesimo calcolo sull'intera popolazione, e possiamo solo supporre che i due
risultati non differiscano troppo. La _statistica inferenziale_ studia questo
tipo di situazioni, definendo in modo formale l'incertezza insita nei
procedimenti basati su campionamento e fornendo degli strumenti che permettono
di quantificarla.

La statistica inferenziale rappresenta, sotto vari punti di vista, un punto di
incontro tra la statistica descrittiva e il calcolo delle probabilità.
Quest'ultimo considera per esempio molte delle proprietà studiate nella
statistica descrittiva per indicare analoghe proprietà di una variabile
aleatoria (o, meglio, della sua distribuzione), e non è un caso che gli indici
utilizzati per descrivere queste proprietà abbiano spesso lo stesso nome,
così che si aggiunge a questo nome l'aggettivo _campionario_ per distinguere
il contesto della statistica descrittiva (e, come vedremo, di quella
inferenziale) da quello del calcolo delle probabilità. La statistica
inferenziale, infatti, non solo utilizza il calcolo delle probabilità per
formalizzare in termini di variabili aleatorie i concetti di popolazione,
campione e stima, ma, valutando le sopra menzionate proprietà su queste
variabili aleatorie, permette di quantificare l'incertezza insita nel
processo di stima.

Inoltre, la statistica inferenziale approfondisce alcuni aspetti
che sono stati introdotti in modo relativamente informalme nell'ambito
descrittivo. Per esempio, la media campionaria indica il baricentro dei valori
osservati nel campione, e dunque risulta naturale utilizzarla per valutare la
centralità del campione stesso. Ma perché le viene data così tanta enfasi, a
discapito di altri indici di posizione, in virtù del fatto che essa non è
robusta rispetto ai valori fuori scala? Analogamente, consideriamo la
definizione non pienamente intuitiva della varianza campionaria: perché la
somma degli $n$ scarti quadratici rispetto al valore centrale viene divisa per
$n - 1$ e non per $n$, così da ottenere la media aritmetica degli scarti
stessi, che sembrerebbe più sensata per valutare la dispersione? Vedremo come
la statistica inferenziale permette di rispondere a queste domande, facendoci
considerare da un altro punto di vista alcuni degli indici che abbiamo
studiato, motivandone ulteriormente la validità.

Questo capitolo descrive in modo succinto le due principali branche della
statistica inferenziale, la _statistica parametrica_ (introducendo
separatamente due differenti modalità di stima, quella _puntuale_ e quella
_per intervalli_) e la _statistica non parametrica_ (si omette l'aggettivo
inferenziale, per non appesantire la trattazione). La prima branca è
approfondita nel {ref}`sec:stime-puntuali` e nel
{ref}`sec:stime-per-intervalli`, mentre la seconda viene accennata
nel {ref}`chap:statistica-non-parametrica`.


## La statistica parametrica

Nella statistica parametrica, l'incertezza è legata alla necessità di
utilizzare un campione per approssimare numericamente una quantità ignota,
indicata in modo generale come $\tau$, che dipende dalla popolazione.

```{margin}
L'uso del simbolo $\tau$ per indicare la quantità ignota è una convenzione
utilizzata soprattutto quando si vuole inquadrare il problema della stima
parametrica in modo generale. Quando si considerano dei casi specifici, è
ragionevole che vengano utilizzati simboli diversi, legati al particolare
contesto che viene di volta in volta considerato.
```
```{prf:example}
:label: ex:parametric-estimate

In un sondaggio demoscopico, $\tau$ può essere la percntuale di una
popolazione di riferimento che è favorevole (o sfavorevole) a un dato
argomento. Analogamente, uno studio clinico volto a determinare l'efficacia di
un farmaco nel curare una patologia può avere come scopo quello di stimare la
frazione $\tau$ dei casi nei quali si verifica una particolare
controindicazione.
```

L'approssimazione di queste quantità ignote può essere fatta procedendo
essenzialmente in due modi, brevemente descritti di seguito e approfonditi
rispettivamente nel {ref}`sec:stime-puntuali` e nel
{ref}`sec:stime-per-intervalli`.

- Il modo più semplice è  quello di fornire una _stima puntuale_, che non è
  altro che un singolo valore numerico $\hat\tau$ che si suppone non si
  discosti troppo da $\tau$. Questo viene fatto calcolando il valore di una
  funzione degli elementi del campione, che prende il nome di _stimatore_ o
  _statistica_.
```{margin}
Questa definizione nasconde delle sottigliezze, come spiegato in dettaglio nel
{ref}`sec:intervalli-fiduciari`.
```
- Un approccio alternativo consiste invece nell'indicare una
  _stima per intervalli_, nella quale l'approssimazione viene fornita
  specificando congiuntamente un _intervallo fiduciario_ e un
  _livello fiduciario_. Il primo è un intervallo di valori reale, mentre il
  secondo è un valore in $(0, 1)$, che indica la probabilità che l'intervallo
  specificato contenga $\tau$.

```{prf:example}
Con riferimento all'{prf:ref}`ex:parametric-estimate`, ogni valore
$\hat\tau \in [0..100]$ rappresenta una particolare stima puntuale per il
primo caso considerato, così come un qualsiasi valore in $[0, 1]$ è una stima
puntuale possibile per il secondo caso.

Considerando invece l'ambito della stima per intervalli, e focalizzandoci
solamente sul secondo caso considerato, $[0.001, 0.005]$ potrebbe essere un
intervallo fiduciario di livello $0.95$, così come potrebbe esserlo
$[0.01, 0.1]$.
```

L'esempio precedente mette in evidenza un fatto molto importante: di per sé,
il valore $\hat\tau$ di una stima puntuale non garantisce alcun livello sulla
bontà dell'approssimazione fornita per $\tau$. Vale la pena di fare un'altra
considerazione rilevante: anche qualora venga garantita, per esempio
utilizzando alcuni dei criteri che vedremo nel prossimo capitolo, la qualità
della procedura utilizzata per stimare $\tau$, non esiste un valore _giusto_
in assoluto per la stima puntuale fornita. È facile rendersene conto
ricordando che $\hat\tau$ è il valore restituito da una statistica che dipende
dal campione estratto, pertanto a ogni campione estraibile dalla popolazione
fissata corrisponderà una stima potenzialmente diversa. Vedremo che, in tal
senso, e come è ragionevole aspettarsi, la dimensione del campione considerato
può giocare un ruolo molto importante. Ma fissando questa dimensione si
ricade, in ogni caso, nella considerazione precedente: tutte le stime puntuali
sono affette da un insito errore dovuto alla procedura di campionamento che
le ha generate.

Considerazioni analoghe valgono per le stime per intervalli, sebbene in
questo caso la natura più complessa di un intervallo fiduciario veicoli anche
informazioni indirette sulla bontà della stima: intuitivamente, più è ampio
l'intervallo e meno precisa sarà la stima, e, indifferentemente dall'ampiezza,
più il livello fiduciario è elevato e più affidabile sarà il risultato
proposto. Ma, come già accennato, il ruolo del livello fiduciario va compreso
attentamente: infatti, come vedremo in dettaglio nel
{ref}`sec:intervalli-fiduciari`, il suo valore non indica
la probabilità che $\tau$ sia in generale compreso nell'intervallo fornito,
bensì l probabilità che la procedura di stima abbia fornito in _output_ un
intervallo fiduciario che contiene effettivamente il valore di $\tau$.


## La statistica non parametrica

Infine, vale la pena sottolineare che la statistica inferenziale
può essere declinata anche in senso _non parametrico_, nel caso in cui
l'incertezza non sia incentrata solo su uno o più parametri di una
distribuzione, bensì sia l'intera distribuzione a essere sconosciuta.
Affrontare questo argomento in modo dettagliato, però, è al di fuori della
trattazione data in questo libro. Il
{ref}`chap:statistica-non-parametrica` si limiterà a
introdurre alcuni aspetti di base di questa branca della statistica, legandoli
ad alcuni concetti a essi collegati che abbiamo già trattato nella parte sulla
statistica descrittiva.