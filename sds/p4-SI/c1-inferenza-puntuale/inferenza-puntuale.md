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

# Introduzione

Nella prima parte di questo libro abbiamo visto come alcuni aspetti di un
campione di dati, come per esempio la sua posizione o la sua dispersione
attorno a un valore centrale, possano essere valutati da particolari indici.
Questi indici sono stati introdotti motivando in modo relativamente informalme
la loro validità, a volte lasciando alcuni loro aspetti esplicitamente senza
spiegazione. Per esempio, la media campionaria corrisponde al baricentro dei
valori osservati nel campione, e dunque risulta naturale utilizzarla per
valutare la centralità del campione stesso. Ma perché si usa proprio questo
indice e non un altro? Per quanto riguarda la varianza campionaria, la
definizione non è nemmeno pienamente supportata dall'intuizione: perché la
somma degli $n$ scarti quadratici rispetto al valore centrale viene divisa per
$n - 1$ e non per $n$, così da ottenere come risultato la media aritmetica
degli scarti stessi, che sembrerebbe più sensata per cogliere l'informazione
cercata?


Nella parte sul calcolo delle probabilità, invece, gli stessi aspetti studiati
nella statistica descrittiva per indicare delle proprietà di un campione sono
stati utilizzati per descrivere una variabile aleatoria, o, meglio, la sua
distribuzione. Tutto questo non accade per caso, così come non è una
coincidenza il fatto che gli indici che si utilizzano per valutare queste
proprietà di una variabile aleatoria abbiano spesso nomi simili a quelli visti
nella statistica descrittiva: la mediana campionaria e la deviazione standard
campionaria hanno, per esempio, come controparte nel calcolo delle probabilità
i concetti di mediana e deviazione standard di una variabile aleatoria.

La _statistica inferenziale_ rappresenta, in un certo senso, il punto di
incontro tra la statistica descrittiva e il calcolo delle probabilità.
Più precisamente, questa branca della matematica utilizza il calcolo delle
probabilità per formalizzare i concetti di popolazione e campione
precedentemente introdotti nell'ambito della statistica descrittiva, e li
utilizza per valutare una qualche forma di _incertezza_ che grava sulla
popolazione. Per la precisione, ci concentreremo sulla _statistica
inferenziale parametrica_, caratterizzta dal fatto che questa incertezza è
legata al fatto di voler approssimare il valore numerico di parametri ignoti
di una particolare distribuzione di probabilità, oppure il valore di quantità
che dipendono da questi parametri. Questo capitolo, in particolare, si
concentra sulla _stastistica inferenziale parametrica puntuale_, nella quale
l'approssimazione di una quantità ignota viene fatta fornendo una _stima
puntuale_, che non è altro che un singolo valore numerico. Più precisamente,
viene introdotto il concetto generale di _stimatore_ per modellare un generico
indice utilizzato per approssimare una quantità ignota, in funzione di
un campione estratto da una popolazione. Questa modellizzazione permette di
introdurre delle proprietà desiderabili per gli stimatori, che si dimostrano
essere legate alla bontà delle approssimazioni precedentemente introdotte.
Vedremo, per esempio, che la media campionaria e la varianza campionaria
corrispondono a due stimatori che godono di particolari proprietà, ed è
proprio questo fatto a giustificare il loro utilizzo.

Il capitolo successivo è invece dedicato alla _statistica inferenziale
parametrica per intervalli_, che approssima un valore ignoto indicando un
intervallo nel quale questo valore è contenuto con un certo grado di
probabilità. Infine, vale la pena sottolineare che la statistica inferenziale
può essere declinata anche in senso _non parametrico_, nel caso in cui
l'incertezza non sia incentrata solo su uno o più parametri di una
distribuzione, bensì sia l'intera distribuzione a essere sconosciuta. Questo
argomento, però, è al di fuori della trattazione data in questo libro.