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

# Il problema della stima parametrica

# La popolazione

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
modellare questo processo. In modo più preciso, si considera uno spazio di
probabilità $(\Omega, \mathsf A, \mathrm P)$ nel quale $\Omega$ rappresenta
l'insieme degli individui e $\mathrm P$ è la funzione di probabilità che
corrisponde a selezionare gli individui in modo uniforme da $\Omega$. Infine,
si introduce una variabile aleatoria $X$ che formalizza la misurazione di
$\mathcal A$ (in altre parole, $X$ è definita da una funzione che ha come
codominio l'insieme dei valori di $\mathcal A$). Osservare una specificazione
di $X$ equivale dunque a estrarre a caso un elemento della popolazione e
misurare su di esso il valore dell'attributo al quale siamo interessati.
Per evitare di appesantire la nomenclatura, si preferisce fare un abuso di
linguaggio e riferire il termine _popolazione_ non agli _individui_, bensì
direttamente alle _misurazioni_ dell'attributo $\mathcal A$. In tal senso,
si identifica la variabile aleatoria $X$ direttamente con la popolazione.



```{margin}
Nel {numref}`Paragrafo %s <sec:inferenza-di-due-parametri>` considererò
brevemente un caso particolare nel quale la distribuzione della popolazione
coinvolge due parametri ignoti.
```
Come indicato nell'introduzione, la statistica inferenziale parametrica si
basa sul fatto di conoscere la distribuzione della popolazione, a meno di uno
o più parametri. Più precisamente, considereremo una _famiglia_ di
distribuzioni di probabilità, come introdotto nel
{numref}`Paragrafo %s <sec-famiglie-di-distribuzioni>`, e nell'ottica di
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

L'uso di una variabile aleatoria per modellare la popolazione è intuitivamente
legato al fatto che l'estrazione di un campione si lega in modo naturale
all'osservazione della variabile aleatoria stessa, come dettagliato nel
paragrafo seguente.

# Il campione

La modellizzazione del concetto di campione all'interno della statistica
inferenziale è un argomento delicato: da un lato, come informalmente indicato
alla fine del paragrafo precedente, è naturale pensare a un campione come
a un insieme $\{ x_1, \dots, x_n \}$ di osservazioni della popolazione $X$.
Questa definizione avrebbe l'innegabile vantaggio di essere molto simile a
quella vista nella parte sulla statistica descrittiva. Bisogna però tener
conto di un aspetto importante, evidenzito nell'esempio che segue.

```{code-cell} ipython3
:tags: [remove-cell]

from myst_nb import glue
import scipy.stats as st

import scipy.stats as st

E = st.bernoulli(0.7)
A = st.norm(197, 2)

def publisher_sample(n):
    return r'{' + ', '.join(map(str, E.rvs(n))) + r'}'

def height_sample(n):
    return '{' + ', '.join(map(lambda f: str(round(f, 2)), A.rvs(n))) + '}'

for i in range(10):
  glue(f'publ_sample_{i}', publisher_sample(7))
  glue(f'height_sample_{i}', height_sample(7))
```



````{prf:example}
:label: ex:multiple-samples

Consideriamo le popolazioni descritte nell'{prf:ref}`ex:population-bernoulli`
e nell'{prf:ref}`ex:population-normal`, e fissiamo $n = 10$. La
{numref}`tab:possible-samples` mostra dieci diversi possibili campioni di
$n$ elementi estratti da queste due popolazioni.
````


```{table} Dieci possibili campioni di dimensione $n=7$ estratti da popolazioni definite rispettivamente da una distribuzione di Bernoulli (prima colonna) e normale (seconda colonna, con valori arrotondati alla seconda cifra dopo la virgola per non appesantire la visualizzazione).
:name: tab:possible-samples
:align: center
| Editore                    | Altezza                      |
|----------------------------|------------------------------|
| {glue:text}`publ_sample_0` | {glue:text}`height_sample_0` |
| {glue:text}`publ_sample_1` | {glue:text}`height_sample_1` |
| {glue:text}`publ_sample_2` | {glue:text}`height_sample_2` |
| {glue:text}`publ_sample_3` | {glue:text}`height_sample_3` |
| {glue:text}`publ_sample_4` | {glue:text}`height_sample_4` |
| {glue:text}`publ_sample_5` | {glue:text}`height_sample_5` |
| {glue:text}`publ_sample_6` | {glue:text}`height_sample_6` |
| {glue:text}`publ_sample_7` | {glue:text}`height_sample_7` |
| {glue:text}`publ_sample_8` | {glue:text}`height_sample_8` |
| {glue:text}`publ_sample_9` | {glue:text}`height_sample_9` |
```

L'esempio precedente mette in evidenza una differenza molto importante tra
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
{numref}`Paragrafo %s <sec:stimatori-e-stime>` che questo è solo uno dei
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

(sec:stimatori-e-stime)=
# Stimatori e stime