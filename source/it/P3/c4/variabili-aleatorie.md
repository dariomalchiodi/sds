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

(sec_variabili-aleatorie)=
# Variabili aleatorie

Negli ultimi capitoli abbiamo lavorato con spazi di probabilità
$(\Omega, \mathsf A, \mathbb P)$ in cui gli esiti $\omega \in \Omega$ erano
oggetti anche piuttosto eterogenei: coppie di risultati, configurazioni di
componenti, supereroi estratti a caso. Lo spazio $\Omega$, d'altronde,
è un insieme, e in quanto tale agisce come un semplice _contenitore_ di
possibilità. In questo contesto, tutto ciò che $\mathbb P$ ci permette di fare
è pesare gli eventi che possiamo costruire a partire da $\Omega$. Quando è
possibile, però, piuttosto che fermarsi a un ragionamento basato sull'esito
_grezzo_ dell'esperimento è preferibile esprimerlo tramite un numero che ne
misura una sorta di _intensità_. Ci possiamo chiedere, ad esempio, quante
minacce abbia individuato una squadra in ricognizione, quanti dei dispositivi
montati su un'armatura stiano funzionando, o su quale piano sia stato
teletrasportato un personaggio. 

A volte, è l'esito stesso dell'esperimento casuale a essere rappresentato da un
numero &mdash; come quando si lancia un dado &mdash; ma più spesso capita che
sia necessario un vero e proprio passaggio dall'esito al numero &mdash; succede
quando si lanciano due dadi e si sommano i risultati, o quando si seleziona un
supereroe a caso e se ne misura l'altezza. Tutto ciò è molto più di una
comodità notazionale: si «trasporta» il problema da $\Omega$, che è un
generico insieme normalmente poco strutturato dal punto di vista matematico,
dentro $\mathbb R$, che è invece ricco di strutture algebriche e metriche e
topologiche: posso sommare, moltiplicare, confrontare, ordinare, misurare
distanze, passare al limite. Più in generale, entrano in gioco gli strumenti
dell'algebra e dell'analisi, che su $\Omega$ non avrebbero alcun significato. È
questo il vero guadagno: esprimere l'esito attraverso un numero non si limita a
codificarlo, bensì arricchisce i ragionamenti che possiamo fare su di esso. Va
però usata una certa cautela, perché non tutte le operazioni disponibili in
$\mathbb R$ sono legittime in ogni situazione: la matematica si applica _ove
ciò ha senso_. Se il numero che usiamo individua un'etichetta ordinata, come il
piano su cui ci si trova al termine del teletrasporto, avrebbe senso
confrontare due piani, ma non sommarli o sottrarli: il risultato non
corrisponderebbe necessariamente ad alcun piano in cui qualcuno sia mai
arrivato, o addirittura a un piano esistente. Quando invece il numero che
utilizziamo è il risultato di una procedura di conteggio &mdash; come le
minacce individuate, o i dispositivi funzionanti &mdash; possiamo usare
l'aritmetica, per esempio sommando il numero di minacce, e ottenere un
risultato al quale dare un significato. Ma anche in casi come questo, certe
operazioni restano prive di significato, come il prodotto di due conteggi.
Tenere a mente _quali_ manipolazioni siano sensate, e non soltanto quali siano
formalmente eseguibili, deve essere una preoccupazione ricorrente.

```{margin}
Non tutte le funzioni $X:\Omega \to \mathbb R$ rappresentano delle variabili
aleatorie, come vedremo più avanti.
```
L'oggetto naturale per formalizzare questa trasformazione da un esito a un
numero è una particolare funzione che ha $\Omega$ come dominio e $\mathbb R$
come codominio. Nella letteratura moderna, questa funzione viene tipicamente
indicata usando una lettera maiuscola (e $X$ è la scelta più ricorrente) e la
si chiama _variabile aleatoria_. Questo nome è in un certo senso fuorviante,
perché non si tratta né di una variabile nel senso dell'algebra o
dell'informatica, né di qualcosa di propriamente «aleatorio»: è infatti una
regola deterministica che traduce esiti in numeri. In effetti, l'aleatorietà
non sta nella funzione $X$ in sé, ma nel suo argomento $\omega$, che è l'esito
di un esperimento casuale formalizzato in uno spazio di probabilità $(\Omega,
\mathsf A, \mathbb P)$. Di conseguenza, ciò che diventa non deterministico è
l'immagine di $\omega$ attraverso $X$. Questo ha una conseguenza importante:
quasi sempre possiamo dimenticare $\Omega$ &mdash; e, in larga misura, anche il
fatto che $X$ sia una funzione. Nella pratica comune, infatti, si identifica
$X$ direttamente con i valori che essa assume: per esempio, si usa la notazione
$X \leq x$ per indicare l'evento $\{ \omega \in \Omega \mid X(\omega) \leq x
\}$, con estensioni analoghe ad altre espressioni che coinvolgono $X$. È
proprio qui che emerge il significato del termine «variabile aleatoria»: $X$ è
_variabile_, perché ogni volta che la si osserva (cioè ogni volta che si esegue
l'esperimento casuale e si trasforma l'esito ottenuto in un numero) si può
ottenere un risultato diverso. Ma varia in modo _aleatorio_, perché il valore
osservato dipende da una sorgente probabilistica &mdash; lo spazio $(\Omega,
\mathsf A, \mathbb P)$.

```{margin}
Nella pratica, una distribuzione viene descritta specificando quali sono i
valori che può assumere la variabile aleatoria, unitamente a una funzione che
permette di calcolare la probabilità degli eventi che la coinvolgono.
```
Una volta fatto questo passaggio concettuale, le risposte alle domande che ci
possiamo porre &mdash; per esempio quanto valga $X$ in media, quanto sia
probabile che superi una certa soglia o quanto siano dispersi i suoi valori
&mdash; dipendono soltanto dalla _distribuzione_ di $X$, che descrive come la
probabilità dello spazio originario si ripartisce sui valori numerici assunti
dalla variabile. È su questo oggetto, più che sullo spazio originario $\Omega$,
che si costruisce gran parte della teoria successiva.

Proprio guardando al modo in cui i valori si distribuiscono sui numeri reali,
si scopre che le variabili aleatorie non sono tutte dello stesso tipo: si
distinguono tradizionalmente tre grandi famiglie. Vi sono quelle _discrete_,
che assumono valori in un insieme al più numerabile (tipicamente conteggi, come
negli esempi visti fin qui)[^isolati], quelle _continue_, che possono variare
su insiemi continui di valori[^continue] e infine quelle _miste_, che combinano
i due comportamenti precedenti[^famiglie]. In questo capitolo introduco i
concetti fondamentali e le formalizzazioni matematiche che valgono in generale,
per qualunque tipo di variabile aleatoria, per poi concentrarmi sul caso
discreto e svilupparne in dettaglio gli strumenti. Ho fatto questa scelta
deliberatamente, in quanto permette di affrontare il
{ref}`chap_modelli-discreti`, dedicato ai modelli discreti, su basi già solide,
senza appesantire fin da subito il discorso con le variabili continue &mdash;
che richiedono un apparato analitico dedicato. Studieremo questo apparato nel
{ref}`chap_va-e-modelli-continui`, così da avere a disposizione gli strumenti
per trattare i modelli continui proprio quando ci serviranno.


[^isolati]: Un'incarnazione classica delle variabili aleatorie discrete è
quella che coinvolge osservazioni isolate (tipicamente i numeri interi). Ma la
proprietà essenziale delle distribuzioni corrispondenti è quella di assumere
valori in un insieme finito o infinito numerabile: ciò fa sì che esistano
variabili discrete i cui valori non sono affatto isolati, come accade quando
essi formano l'insieme dei numeri razionali.

[^continue]: In questo caso, la descrizione è volutamente intuitiva. Ciò che
caratterizza una variabile continua non è il fatto di assumere valori in un
insieme continuo, bensì l'esistenza di una funzione di densità che consente di
calcolare la probabilità degli eventi tramite un integrale. È sulla
distribuzione, e non sull'insieme dei valori assunti, che poggia la
definizione, come vedremo nel {ref}`chap_va-e-modelli-continui`.

[^famiglie]: La suddivisione in queste tre famiglie è quella convenzionale, ma
non è esaustiva, perché esistono distribuzioni che sfuggono a questa
tripartizione. Si tratta però di distribuzioni molto particolari, la cui
descrizione va decisamente al di là dello scopo di questo libro, e che in ogni
caso non compariranno nelle applicazioni che consideremo qui.