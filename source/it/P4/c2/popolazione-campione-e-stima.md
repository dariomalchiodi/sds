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

(sec:problema-stima-parametrica)=
# Il problema della stima parametrica

## La popolazione

```{margin}
In linea di principio è possibile definire una popolazione utilizzando
variabili aleatorie multivariate, che equivale a considerare individui
descritti da più attributi, ma questo è un argomento avanzato che va oltre lo
scopo di questo libro.
```
La parte di questo libro dedicata alla statistica descrittiva ha introdotto il
concetto di popolazione definendolo come un insieme di individui, ognuno
rappresentato dall'esito delle misurazioni di uno o più attributi. Quando si
introduce la statistica inferenziale, il punto di partenza è lo stesso (un
insieme di individui), ma per semplificare la trattazione ci si concentra su
di un unico attributo $\mathcal A$. In questo modo è possibile identificare
ogni individuo con il valore che si ottiene misurando l'attributo
$\mathcal A$, e le variabili aleatorie emergono come strumento ideale per
modellare questo processo.

In modo più preciso, e nella sua accezione più semplice, la statistica
inferenziale considera uno spazio di probabilità
$(\Omega, \mathsf A, \mathrm P)$ nel quale $\Omega$ rappresenta l'insieme
degli individui e $\mathrm P$ è la funzione di probabilità che
corrisponde a selezionare gli individui in modo uniforme da $\Omega$. Infine,
si introduce una variabile aleatoria $X$ che formalizza la misurazione di
$\mathcal A$ (in altre parole, $X$ è definita da una funzione che ha come
codominio l'insieme dei valori di $\mathcal A$).

Osservare una specificazione
di $X$ equivale dunque a estrarre a caso un elemento della popolazione e
misurare su di esso il valore dell'attributo al quale siamo interessati.
Per evitare di appesantire la nomenclatura, si preferisce fare un abuso di
linguaggio e riferire il termine _popolazione_ non agli _individui_, bensì
direttamente alle _misurazioni_ dell'attributo $\mathcal A$. In tal senso,
si identifica la variabile aleatoria $X$ direttamente con la popolazione.



```{margin}
Nel {ref}`sec:massima-verosimiglianza` considererò
brevemente un caso particolare nel quale la distribuzione della popolazione
coinvolge due parametri ignoti.
```
Come indicato nell'introduzione, la statistica inferenziale parametrica si
basa sul fatto di conoscere la distribuzione della popolazione, a meno di uno
o più parametri. Più precisamente, considereremo una _famiglia_ di
distribuzioni di probabilità, come introdotto nel
{ref}`sec:famiglie-di-distribuzioni`, e nell'ottica di
semplificare il problema che stiamo studiando, questa famiglia sarà
caratterizzata da uno e un solo parametro. La distribuzione della popolazione
apparterrà a questa famiglia, e individuare il corrispondente valore del
parametro, che considereremo ignoto, equivarrà a individuare completamente la
distribuzione. Grazie alla formalizzazione introdotta, diventa relativamente
semplice definire in modo formale una popolazione.


````{prf:definition} Popolazione
:label: def:population-is

Sia $\mathcal F = \{F_\theta, \theta \in \Theta \subseteq \mathbb R \}$ una
famiglia di distribuzioni di probabilità indicizzata rispetto a un parametro.
In un problema di statistica inferenziale parametrica, la _popolazione_ è
definita come una variabile aleatoria univariata $X$, la cui distribuzione
appartiene a $\mathcal F$.
````

````{admonition} Nomenclatura
:class: naming

Quando si vuole modellare in modo generale il problema della statistica
inferenziale parametrica puntuale, in letteratura si utilizzano i simboli $X$
e $\theta$ per indicare, rispettivamente, la popolazione e il parametro
ignoto. C'è invece meno uniformità quando si tratta di denotare formalmente la
distribuzione della popolazione. A questo scopo, io ho scelto di usare la
notazione $X \sim F_\theta$, evidenziando così il parametro ignoto.
````

È importante sottolineare che le definizioni date in questo paragrafo e in
quelli che seguono, così come la notazione introdotta, hanno lo scopo di
formalizzare i concetti chiave del problema che stiamo studiando. Ogni volta
che affronteremo un'istanza specifica di questo problema, i simboli come
$\theta$ e $F_\theta$ verranno sostituiti opportunamente.


```{prf:example}
:label: ex:population-bernoulli

Supponiamo che la popolazione considerata coinvolga tutti i supereroi,
che l'osservazione di un suo individuo corrisponda a valutare l'attributo che
descrive l'editore, e che il risultato della misurazione sia $1$ nel caso di
un supereroe Marvel e $0$ altirmenti. Se assumiamo di non conoscere quale
sia la frazione dei supereroi Marvel rispetto al totale, allora possiamo dire
che la popolazione ha una distribuzione di Bernoulli di parametro $p$, fissato
ma sconosciuto. Dunque, in termini della modellazione appena introdotta:

- il parametro ignoto $\theta$ si può indicare in modo più adeguato usando
  $p$, e i suoi valori possibili appartengono all'insieme $\Theta = [0, 1]$;
- la popolazione è descritta da una variabile aleatoria $X \sim \mathrm B(p)$,
  la cui distribuzione appartiene alla famiglia
  $\mathcal F = \{ F_p, p \in [0, 1] \}$, dove $F_p$ indica la funzione di
  ripartizione della distribuzione di Bernoulli di parametro $p$.
```

È importante notare che è possibile fare riferimento a distribuzioni per la
popolazione che dipendono da più parametri, dei quali solo uno è ignoto, come
illustrato nell'esempio che segue.

```{prf:example}
:label: ex:population-normal

Come nell'{prf:ref}`ex:population-bernoulli`, consideriamo tutti i supereroi,
ma in questo caso concentriamoci sull'attributo relativo all'altezza, misurata
in centimetri. Supponiamo che la popolazione sia descritta da una
distribuzione normale il cui valore atteso è ignoto e la cui deviazione
standard è pari a $2\, \mathrm{cm}$. In questo caso avremo
$X \sim \mathrm N(\mu, 2)$, e pertanto

- è più descrittivo utilizzare $\mu$ (rispetto a $\theta$) come simbolo per
  descrivere il parametro ignoto, e $\Theta = \mathbb R^+$ (in generale, il
  valore atteso di una distribuzione normale può essere qualsiasi numero
  reale, ma nel caso specifico che stiamo considerando $\mu$ descrive
  l'altezza, che è una quantità sempre positiva);
- la famiglia di distribuzioni che stiamo considerando è
  $\mathcal F = \{ F_\mu, \mu \in \mathbb R^+ \}$, dove $F_\mu$ indica la
  funzione di ripartizione della distribuzione normale di valore atteso $\mu$
  e deviazione standard uguale a 2.
```

La formalizzazione finora introdotta permette di definire in modo preciso
il concetto di popolazione, al prezzo di una certa complessità nella notazione
e, più in generale, imponendo un certo grado di verbosità nella descrizione
dei problemi. Quando il contesto lo permette, la terminologia utilizzata si
può però semplificare: nell'{prf:ref}`ex:population-bernoulli` si può dire che
la popolazione $X$ ha una distribuzione di Bernoulli il cui parametro $p$ è
ignoto; analogamente, la popolazione dell'{prf:ref}`ex:population-normal` si
può descrivere più semplicemente dicendo che la sua distribuzione è normale,
con valore atteso ignoto e deviazione standard uguale a $2$.

L'uso di una variabile aleatoria per modellare la popolazione è intuitivamente
legato al fatto che l'estrazione di un campione si lega in modo naturale
all'osservazione della variabile aleatoria stessa, come dettagliato nel
paragrafo seguente.

(sec:il-campione)=
## Il campione

```{margin}
Negli esempi citati, le popolazioni sono descritte come variabili aleatorie,
mentre qui eseguiamo un campionamento direttamente dal _dataset_,
soffermandoci su attributi che sono ben descritti da queste variabili
aleatorie.
```
La modellizzazione del concetto di campione all'interno della statistica
inferenziale è un argomento delicato: da un lato, come informalmente indicato
alla fine del paragrafo precedente, è naturale pensare a un campione come
a un insieme $\{ x_1, \dots, x_n \}$ di osservazioni della popolazione $X$.
Questa definizione avrebbe l'innegabile vantaggio di essere molto simile a
quella vista nella parte sulla statistica descrittiva. Bisogna però tener
conto di un aspetto importante: consideriamo per esempio il codice che segue,
che sfrutta il metodo `DataFrame.sample` per estrarre dal _dataset_
dei supereroi dieci diversi possibili campioni, ognuno di $n = 6$ elementi,
separatamente per le due popolazioni descritte
nell'{prf:ref}`ex:population-bernoulli` e
nell'{prf:ref}`ex:population-normal` e considerando solamente le
supereroine.

```{admonition} Note al codice
:class: dropdown, code-note, full-width

- La funzione `get_sample` accetta come argomento, rispettivamente, un
  _dataframe_, una stringa contenente il nome di un attributo $\mathcal A$ e
  un numero intero $n$. Dopo avere eliminato tutti i valori mancanti, il
  _dataframe_ viene campionato estraendo $n$ casi ed estraendo dal risultato
  la colonna corrispndente ad $\mathcal A$, restituendola. Questa funzione
  viene utilizzata per ottenere 10 campioni per i due attributi selezionati,
  salvandoli nelle variabili `height_samples` e `publisher_samples`, che
  utilizzeremo anche più avanti.
- La funzione `show_sample` accetta come argomento un campione restituito da
  `get_sample` e una funzione di conversione, che applica a tutti gli elementi
  del campione al fine di ottenerne una descrizione testuale. Le descrizioni
  vengono poi concatenate separandole con virgole, restituendo il risultato
  prodotto dopo averlo delimitato con una coppia di parentesi graffe, così da
  ottenere una descrizione testuale per l'intero campione che si rifà alla
  notazione matematica che abbiamo utilizzato.
- Il valore predefinito per l'argomento della funzione di conversione in
  `show_sample` è `str`, e permette di trasformare in stringa i valori degli
  attributi numerici, al fine di concatenarli. Nel caso di attributi
  categorici o ordinali, per poter ragionare in termini numerici è necessario
  modificare il valore di questo argomento. È quello che viene fatto
  introducendo `publisher_conversion` per convertire i valori dell'attributo
  _Publisher_ in stringhe che corrispondono alle specificazioni di una
  variabile aleatoria di Bernoulli.
- Le descrizioni testuali dei vari campioni vengono utilizzati come colonne
  per creare un nuovo _dataframe_, il cui scopo è meramente quello di
  mostrare questi campioni in forma tabulare.
```
```{code-block} python
:class: toggle-code

import pandas as pd

heroes = pd.read_csv('data/heroes.csv')

def get_sample(dataset, attribute, n):
    return dataset[attribute].dropna().sample(n)

def show_sample(sample, conversion=str):
    return '{' + ', '.join(map(conversion, sample)) + '}'

n = 6
num_samples = 10

height_samples = [get_sample(heroes, 'height', n) for _ in range(num_samples)]
publisher_samples = [get_sample(heroes, 'creator', n)
                     for _ in range(num_samples)]

publisher_conversion = lambda s: '1' if s == 'Marvel Comics' else '0'

show_publisher_smaple = lambda s: show_sample(s,
                                              conversion=publisher_conversion)
pd.DataFrame({'Altezza': map(show_sample, height_samples),
              'Editore': map(show_publisher_smaple,
                             publisher_samples)})
```

I risultati ottenuti mettono in evidenza una differenza molto importante tra
la statistica descrittiva e quella inferenziale. Nella prima, il campione
viene inteso come una sequenza di numeri fornita a priori. Nella seconda,
d'altro canto, una volta che il numero di elementi è stato fissato, i campioni
che è _possibile_ osservare sono di solito sensibilmente diversi l'uno
dall'altro, e quindi anche le conclusioni che se ne possono ricavare saranno
differenti da un punto di vista numerico. Risulta però desiderabile valutare
la bontà di queste conclusioni indipendentemente dal _particolare_ campione
che è stato osservato. Ipotizziamo, come è naturale pensare, che il nostro
scopo sia quello di fornire un'approssimazione per il valore del parametro
sconosciuto $\theta$ (ma vedremo nel
Paragrafo {ref}`sec:stimatori-e-stime` che questo è solo uno dei
possibili obiettivi da perseguire). Chiaramente, saremo interessati a fornire
un'approssimazione numerica per $\theta$, ma vorremo anche poter dire
qualcosa, indipendentemente dal particolare campione che abbiamo osservato,
sulla bontà di questa approssimazione, fornendo per esempio un'indicazione di
quanto essa sia accurata. È per questo motivo che, nell'ambito della statistca
inferenziale, il concetto di campione viene formalizzato utilizzando una
successione di variabili aleatorie, come nella definizione seguente.

```{prf:definition}
:label: def:sample-is

Data una popolazione descritta da una variabile aleatoria
$X$ e un numero intero $n \in \mathbb N$, si definisce
un _campione aleatorio_ di dimensione $n$ come una sequenza $X_1, \dots, X_n$
di $n$ variabili aleatorie i.i.d., la cui distribuzione coincide con quella
di $X$. Ognuna delle $n$ variabili aleatorie è detta _elemento_ del campione.
```

Identificare ogni elemento del campione con una variabile aleatoria
modella in modo naturale il processo di campionamento: abbandonando per un
attimo l'abuso di linguaggio che ho inizialmente introdotto, osservare una
specificazione $x_i$ di un generico elemento $X_i$ equivale a selezionare
casualmente un individuo della popolazione e misurarne il valore di un
attributo. All'atto pratico, a seconda dei casi descriveremo un campione in
due modi diversi:

- quando vorremo fare riferimento a _uno specifico campione estratto_, per
  esempio perché vogliamo ottenere un'approssimazione numerica di $\theta$,
  lo descriveremo come una sequenza $x_1, \dots, x_n$ di specificazioni
  della variabile aleatoria $X$ che descrive la popolazione;
- quando vorremo studiare le _proprietà_ delle conclusioni alle quali
  arriviamo, per esempio nel valutare la bontà dell'approssimazione numerica
  del punto precedente, utilizzeremo una sequenza $X_1, \dots, X_n$ di
  variabili aleatorie.

La {prf:ref}`def:sample-is` impone tre requisiti alle variabili aleatorie
utilizzate per desrivere un campione: queste variabili devono

- essere tra loro indipendenti,
- avere un'identica distribuzione,
- avere la stessa distribuzione della variabile aleatoria che descrive la
  popolazione.

Questi requisiti hanno un ruolo fondamentale nelle dimostrazioni dei teoremi
legati alla statistica inferenziale, ma è facile convincersi della loro
importanza anche ragionando in modo informale. L'indipendenza tra gli
elementi del campione garantisce che questo sia il più possibile
rappresentativo della distribuzione dalla quale è stato estratto: i risultati
dell'inferenza sarebbero verosimilmente falsati nel caso in cui due o più
elementi del campione fossero in qualche modo dipendenti tra loro. Se per
esempio lo scopo fosse quello di valutare l'efficacia di un farmaco nel
ridurre il tasso di colesterolo nel sangue, sarebbe scorretto considerare, tra
le altre, più misurazioni del colesterolo fatte a uno stesso individuo in
istanti differenti. Infatti, se questo individuo fosse stato molto più
ricettivo al farmaco rispetto alle altre persone considerate, e il farmaco
avesse avuto un effetto duraturo, è ragionevole immaginare che tutte le
misurazioni effettuate sull'individuo sarebbero sensibilmente più basse
rispetto alle altre, e dunque si introdurrebbe una distorsione nei risultati
dello studio. D'atra parte, la richiesta che tutte le variabili aleatorie che
descrivono i singoli elementi del campione debbano avere un'identica
distribuzione è ovviamente legata alla necessità di campionare sempre la
medesima popolazione: se lo studio precedente fosse focalizzato sull'effetto
congiunto del farmaco e di un particolare stile di vita, non avrebbe senso
includere nel campione tutti i pazienti e le pazienti di un ospedale che
hanno usufruito di quel farmaco in un dato periodo, perché solo una parte di
questi pazienti condurrebbe verosimilmente lo stile di vita considerato.
Infine, la distribuzione comune di tutte le variabili che definiscono il
campione deve ovviamente essere la stessa che descrive la popolazione: se
il campionamento consistesse nel selezionare a caso le persone che
frequentano un edificio e domandare loro di valutare l'efficacia dei lavori
di manutenzione, sarebbe errato posizionarsi all'ultimo piano e
intervistare le prime cento persone che escono dall'ascensore dopo le 8:30,
perché tutte queste persone non descrivono la popolazione alla quale siamo
interessati, bensì una precisa sotto-popolazione: quella delle persone che
frequentano un piano dell'edificio al mattino presto. Anche in questo caso,
vi è un concreto rischio che i risultati dello studio siano falsati, perché
per esempio vi sono delle falle nel sistema di manutenzione che coinvolgono
piani diversi dall'ultimo, o che si verificano durante le ore più calde
della giornata.

## Oggetto della stima

Come specificato nella {prf:ref}`def:population-is`, la distribuzione della
popolazione è nota a meno del valore di un parametro $\theta \in \Theta$.
La quantità $\tau$ che si vuole stimare coincide a volte con il parametro
ignoto. In questi casi avremo dunque $\tau = \theta$, ma più semplicemente
useremo fin da subito $\theta$ (o, meglio, un simbolo specifico) per denotare
la quantità che siamo interessati ad approssimare. Nei casi rimanenti, quello
che si vuole stimare è una quantità che dipende dal parametro ignoto, che
sarà necessariamente anch'essa sconosciuta, ed è opportuno modificare
leggermente la notazione introdotta per esplicitare questa dipendenza. In
generale, scriverò $\tau(\theta)$ per denotare la quantità ignota, adattando
questa formalizzazione ai singoli esempi specifici, utilizzando i simboli in
essi adottati.

```{prf:example}
:label: ex:populations

Concentriamoci sulla popolazione dei professionisti in una fissata categoria
che operano in una certa regione, e supponiamo di essere interessati a stimare
il loro reddito medio. Se questa popolazione è descritta da una variabile
aleatoria $X$ con distribuzione normale il cui valore atteso $\mu$ è ignoto e
la cui deviazione standard è fissata, allora il parametro ignoto e la quantità
da stimare coincidono, e potremo dire direttamente che siamo interessati a
stimare $\mu$. Potremmo essere molto pedanti, e scrivere che vogliamo
approssimare la quantità $\tau = \mu$, ma complicheremmo inutilmente la nostra
descrizione del problema.

Se la stessa popolazione $X$ fosse invece distribuita secondo una legge
esponenziale di parametro ignoto $\lambda$, ricordando che
$\mathbb E(X) = \frac{1}{\lambda}$, la quantità da stimare dipenderebbe dal
parametro ignoto, ma non sarebbe uguale a quest'ultimo. Diremo quindi che ciò
che vogliamo stimare è $\frac{1}{\lambda}$. Anche in questo caso, potremmo
seguire alla lettera la notazione introdotta, e fare riferimento a
$\tau(\lambda) = \frac{1}{\lambda}$, o addirittura scrivere $\theta = \lambda$
e $\tau(\theta) = \tau(\lambda) = \frac{1}{\lambda}$. Ma introdurremmo, anche
più marcatamente rispetto al caso precedente, delle complicazioni inutili.
```


(sec:stimatori-e-stime)=
## Stimatori e stime

Nei problemi di stima puntuale, il campione estratto dalla popolazione viene
utilizzato per ricavare un'approssimazione per la quantità ignota che si è
interessati a valutare. Questo viene fatto usando il campione come argomento
di una funzione, detta _statistica_.

```{prf:definition}
:label: def:statistics-is

Una _statistica_ è una funzione $t$ a valori reali i cui argomenti sono
gli elementi di un campione, e che non dipende da alcun parametro ignoto.
```

Formalizzare il concetto di statistica introdotto nella precedente definizione
richiede un po' di attenzione, perché la definizione di una funzione richiede
di fissare il relativo numero di argomenti, mentre un campione può avere un
generico numero di elementi. Sebbene nella {prf:ref}`def:sample-is` un
campione di dimensione $n \in \mathbb N$ sia stato introdotto come una
sequenza $X_1, \dots, X_n$ di variabili aleatorie, concentriamoci inizialmente
sulle specificazioni $x_1, \dots, x_n$ di queste variabili aleatorie. Fissato
il valore di $n$, la definizione precedente ci dice che una generica funzione
$t: \mathbb R^n \to \mathbb R$ che non dipende da alcun parametro ignoto è
una statistica. L'esempio che segue mostra però che, in generale, le
statistiche che considereremo sono in un certo senso indipendenti dalla taglia
del campione che elaborano.

````{prf:example}
:label: ex:statistic

Fondamentalmente, tutti gli indici che abbiamo visto nella parte sulla
statistica descrittiva vengono calcolati utilizzando una statistica. Pertanto,
fissato $n \in \mathbb N$, sono esempi di statistica la media campionaria,
definita da

```{math}
:label: eq:sample-mean
t(x_1, \dots, x_n) = \frac{1}{n} \sum_{i=1}^n x_i \enspace, 
```

ma anche la la varianza campionaria e la deviazione standard campionaria, per
le quali la funzione $t$ è definita in modo analogo, e così via.
````

Emerge chiaramente da {eq}`eq:sample-mean` che la definizione analitica della
media campionaria è fondamentalmente indipendente dal particolare valore di
$n$, ed è possibile commutare l'ordine degli argomenti senza che cambi il
valore restituito dalla statistica. Questa situazione si verificherà sempre
nei casi che considereremo, come d'altronde è ragionevole aspettarsi: nei
problemi che analizzeremo, la scelta della statistica non dovrebbe dipendere
dal particolare ordine nel quale sono stati osservati gli elementi del
campione. Pertanto, risulta possibile formalizzare il concetto di statistica
tramite una _famiglia_ di funzioni, indicizzata rispetto al relativo numero di
argomenti. Ove opportuno, espliciterò questo indice indicando $n$ come pedice
nel nome della funzione. Per esempio, la media campionaria può essere
collegata alla famiglia $\{ t_n: \mathbb R^n \to \mathbb R \}$, dove ogni
$t_n$ è definita esattamente come in {eq}`eq:sample-mean`.

La {prf:ref}`def:statistics-is` richiede esplicitamente che la funzione alla
base di una statistica non dipenda da alcun parametro ignoto. In questo caso,
il termine _parametro_ si riferisce a eventuali argomenti il cui valore non
è conosciuto, includendo ovviamente il parametro sconosciuto per la
distribuzione di una popolazione. Questo requisito richiede essenzialmente
che una statistica dipenda _solamente_ da un campione e che, quando
quest'ultimo viene specificato, il valore della statistica sia calcolabile
e sia un numero reale. In altre parole, ragionando in termini informatici una
statistica è un _algoritmo_ che accetta come argomenti tutti e soli gli
elementi di un campione e che restituisce come valore un numero reale. Questo
aspetto è cruciale quando questo valore viene utilizzato per approssimare la
quantità ignota $\tau(\theta)$ alla base del problema di stima puntuale che si
sta affrontando. Si dice, in questo caso, che la statistica $t$ è uno
_stimatore_ per $\tau(\theta)$, e che il valore
$\hat\tau = t (x_1, \dots, x_n)$ da essa calcolato è una _stima_ per la
quantità ignota. Idealmente, $\hat\tau$ e $\tau(\theta)$ non sono troppo
diversi tra loro, al punto che ci si può spingere a dire che sono
approssimativamente uguali, scrivendo $\hat\tau \approx \tau(\theta)$.

Abbandoniamo ora la semplificazione che abbiamo introdotto e ripetiamo il
ragionamento precedente considerando, correttamente, il campione come una
sequenza $X_1, \dots, X_n$ di variabili aleatorie. È facile rendersi conto
che nulla cambia nella definizione e nel significato di una statistica, intesa
come funzione o algoritmo. Quello che cambia è che adesso gli argomenti di
questa funzione sono delle variabili aleatorie, e dunque anche il valore
restituito è una variabile aleatoria $t(X_1, \dots, X_n)$. Qualora il
campione sia chiaro dal contesto, per semplificare la notazione e i conti
introdurrò una variabile aleatoria specifica $T$ per modellare direttamente il
valore restituito dalla statistica. Analogamente a quanto esposto sopra, a
volte sostituirò a $T$ un simbolo legato allo specifico caso trattato, e ove
opportuno aggiungerò un pedice per evidenziare la dipendenza implicita della
statistica rispetto alla dimensione del campione.

````{prf:example}
:label: ex:statistics-rv

Riprendendo l'{prf:ref}`ex:statistic`, il valore della media campionaria
sarà descritto dalla variabile aleatoria

```{math}
\overline X = \frac{1}{n} \sum_{i=1}^n X_i \enspace,
```

e vedremo nel {ref}`sec:media-campionaria` che questa
statistica viene tipicamente utilizzata come stimatore per il valore atteso
di una popolazione, o alternativamente che la sua generica specificazione
$\overline x$ rappresenta una stima per la medesima quantità.
````

La definizione di una statistica in termini di una variabile aleatoria
modella il fatto che ogni volta che si estrae dalla popolazione un campione
di dimensione fissata, quest'ultimo contiene valori potenzialmente differenti,
e quindi anche la statistica può assumere un insieme di differenti valori.
Riprendendo l'esempio fatto all'inizio del
Paragrafo {ref}`sec:il-campione`, possiamo evidenziare questo fatto
considerando tutti i campioni per le altezze e calcolando per ognuno la media
campionaria.

```{admonition} Note al codice
:class: dropdown, code-note

- Ho utilizzato una _list comprehension_ per calcolare la media di ogni
  campione in `height_samples` e arrotondare i risultati alla seconda cifra
  decimale.
- La conversione della lista ottenuta in un array e la stampa di quest'ultimo
  è un "trucco" che evita che l'output della cella venga suddiviso su più
  righe.
```
```{code-block} python
:class: toggle-code

import numpy as np

print(np.array([round(np.mean(s), 2) for s in height_samples]))
```

```{margin}
L'uso del condizionale in questa frase è dovuto al fatto che i valori
dell'esempio sono stati generati sulla base del campionamento effettuato
all'inizio del Paragrafo {ref}`sec:il-campione`, pertanto potrebbe
capitare che alcuni dei valori della media campionaria si discostino in modo
anche sensibile rispetto agli altri. Se questo succede, controllate i valori
numerici contenuti nei campioni corrispondenti, e provate a determinare la
causa di questi discostamenti rilevanti.
```
Le stime ottenute dovrebbero essere tra loro diversi ma non in modo eccessivo,
oscillando intorno a 185 cm, e ognuna rappresenta una possibile
approssimazione per la quantità $\mu$ che vogliamo stimare, che in questo caso
rappresenta l'altezza media di tutti i supereroi nella popolazione del nostro
_dataset_. Questo però non ci dice nulla sull'_errore_ introdotto da queste
approssimaioni. Più in generale, emergono le seguenti domande relative al
comportamento degli stimatori.

- Che strumenti abbiamo per valutare quanto è buona l'approssimazione fatta
  utilizzando una stima?
- Lo stimatore da utilizzare dipende di volta in volta dal particolare caso
  che stiamo considerando oppure esistono degli stimatori generici che possono
  essere utilizzate in più di una situazione?
- Esistono dei metodi che permettono di ricavare uno stimatore adatto per
  risolvere un problema di stima puntuale?

Nei prossimi paragrafi utilizzeremo la formalizzazione che abbiamo introdotto
per dare una risposta a queste domande.