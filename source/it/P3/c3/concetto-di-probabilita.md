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

(sec_concetto-probabilita)=
# Il concetto di probabilità


Come ho scritto all'inizio del libro, citando la [legge di
Franklin](par_franklin-law), quasi nulla è certo. Le decisioni che prendiamo
&mdash; nella vita quotidiana così come nello studio e nel lavoro &mdash; si
basano quasi sempre su informazioni incomplete. Decidere se portare con noi un
ombrello, stimare quanto tempo servirà per trovare un _bug_ o capire se
conviene rifare un esercizio prima dell’esame: in tutti questi casi dobbiamo
fare i conti con qualcosa che non sappiamo, o che non possiamo sapere con
precisione. Diventa dunque importante saper _gestire_ questo tipo di
situazioni.

Il termine «incertezza» è in realtà piuttosto generico e copre casistiche molto
diverse tra loro. Alcuni concetti, per esempio, sono definiti in modo _vago_:
che cosa significa dire che una persona è «alta», che un esame è «facile», o
che un supereroe è «forte»? In altri casi l'incertezza è di natura
_epistemica_: il fenomeno è ben definito, ma non si dispone di tutte le
informazioni necessarie per conoscerne l'esito &mdash; un'incertezza che, in
linea di principio, potrebbe essere eliminata. Per esempio, le domande di un
tema d'esame sono determinate giorni prima della prova, ma gli studenti non le
conoscono finché non si presentano allo scritto. Io mi concentrerò qui su un
terzo tipo di incertezza, detta _aleatoria_. In questi casi, anche supponendo
di ripetere un’osservazione più volte nelle stesse condizioni, il risultato può
cambiare in modo imprevedibile. Per esempio, non possiamo sapere a priori quale
canzone parte quando si attiva la riproduzione casuale di una _playlist_, o se
in un fumetto pescato a caso da uno scatolone comparirà Visione. Situazioni di
questo tipo vengono descritte e analizzate attraverso il concetto di
_probabilità_, che è basato su due entità fondamentali, che per il momento
introduco in modo informale:

- _esperimento casuale_, che individua una procedura che, pur essendo
  eseguita sempre nelle stesse condizioni, può produrre risultati diversi (come
  l'ascolto della playlist o la scelta di un fumetto negli esempi precedenti);
- _evento_, inteso come proprietà che può essere verificata o meno in seguito
  all’esecuzione di un esperimento aleatorio (il fatto che la prima canzone
  sia di un dato genere, o il fatto che Visione compaia nel fumetto). 

Intuitivamente, la probabilità quantifica quanto sia _verosimile_ che un certo
evento si verifichi, utilizzando un numero compreso tra $0$ e $1$. Zero
significa «impossibile», uno significa «certo», e tutto il resto sta nel mezzo.
Risulta invece decisamente meno facile chiarire quale sia il senso di questo
numero, cioè  esprimere _che cosa significa_ attribuire una probabilità a un
evento. In merito a ciò, come è ragionevole aspettarsi, ci sono diverse
scuole di pensiero. Senza alcuna pretesa di esaustività, accenno di seguito
a due delle più conosciute.

- Secondo l’interpretazione _frequentista_, la probabilità di un evento è il
  limite della frequenza relativa con cui esso si verifica in una lunga serie
  di esperimenti identici ed eseguiti in modo indipendente. Per esempio, la
  probabilità di ottenere «testa» lanciando una moneta si approssima
  effettuando molti lanci e osservando la proporzione di volte in cui
  effettivamente si ottiene «testa» come risultato.
- Nell’interpretazione _soggettivista_, la probabilità rappresenta invece il
  grado di _fiducia_ che un soggetto attribuisce al verificarsi di un evento,
  sulla base delle informazioni a sua disposizione in un dato istante. Secondo
  questa accezione, uno sviluppatore potrebbe ritenere che una libreria scritta
  da un collega sia esente da _bug_ con probabilità $0.7$; se analizzando la
  _test suite_ distribuita con il codice scoprisse che questa è particolarmente
  scarna, lo sviluppatore potrebbe rivedere al ribasso questo valore di
  probabilità.

Chiaramente, ogni interpretazione ha i suoi limiti e i suoi punti di forza, che
in questa sede non è il caso di approfondire. Peraltro, in molte situazioni
pratiche le due interpretazioni sopra elencate portano agli stessi risultati
quantitativi. Conoscerle è in ogni caso utile, perché aiutano a comprendere
come si possa dare senso ai numeri che vengono calcolati, così come a
inquadrare meglio i risultati teorici e le metodologie del calcolo delle
probabilità.

Dal punto di vista matematico, esistono molti modi diversi di formalizzare il
concetto di probabilità, ciascuno motivato da esigenze teoriche o applicative
specifiche. Alcune formalizzazioni mettono l’accento sulla ripetizione di
esperimenti, altre sull’aggiornamento dell’informazione, altre ancora sulla
struttura logica degli eventi. Di fatto, però, per introdurre didatticamente il
calcolo delle probabilità si utilizza quasi sempre una formalizzazione
assiomatica, proposta all’inizio del secolo scorso. Questo libro non fa
eccezione, perché si tratta di un approccio che fornisce una base matematica
solida ed elegante, che oltretutto non dipende da una delle particolari
interpretazioni precedentemente introdotte. In altre parole, la formalizzazione
non entra nel merito del _significato_ della probabilità, ma ne descrive il
comportamento matematico. Ed è proprio questa separazione tra significato e
struttura formale che rende il calcolo delle probabilità uno strumento potente
e applicabile in contesti molto diversi tra loro.
