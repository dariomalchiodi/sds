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

## La popolazione

La parte di questo libro dedicata alla statistica descrittiva ha introdotto il
concetto di popolazione definendolo come un insieme di individui, ognuno
rappresentato dall'esito delle misurazioni di uno o più attributi. Nell'ambito
della statistica inferenziale, la definizione di popolazione cambia in modo da
poterla inquadrare nell'ambito del calcolo delle probabilità: quello che era
l'insieme degli individui diventa ora legato al supporto di una variabile
aleatoria, le cui specificazioni corrisopndono ai possibili valori della
misurazione di un attributo. Anche in questo caso, per semplificare la
trattazione si fa un abuso di linguaggio, riferendo il termine _popolazione_
direttamente alle _misurazioni_ e non agli _individui_.

```{margin}
Nella statistica descrittiva, ogni individuo della popolazione è associato
tipicamente a più attributi, mentre in questa definizione si
fa implicitamente riferimento a una variabile aleatoria univariata. In linea
di principio è possibile definire una popolazione utilizzanto delle variabili
aleatorie multivariate, ma questo è un argomento avanzato che va oltre lo
scopo di questo libro.
```
````{prf:definition} Popolazione
:label: def:population-is

In un problema di statistica inferenziale, la _popolazione_ è definita come
una variabile aleatoria $X$, la cui distribuzione dipende da un parametro
$\theta$ il cui valore è fissato ma al contempo ignoto.
````

```{margin}
In altre parole, $\mathrm D$ indica una particolare famiglia di distribuzione,
dipendente esclusivamente dal parametro ignoto.
```
Nella letteratura c'è ampio accordo sul fatto di utilizzare i simboli $X$ e
$\theta$ per indicare, rispettivamente, la popolazione e il relativo parametro
ignoto. Non c'è invece accordo relativamente al simbolo da usare per
la distribuzione stessa. In questo libro adotterò la notazione
$X \sim \mathrm D(\theta)$, evidenziando così il parametro ignoto. Utilizzerò
la stessa notazione anche nel caso in cui la distribuzione della popolazione
coinvolge due o più parametri, ma solamente uno di essi è sconosciuto, e
ovviamente $\theta$ farà riferimento a questo parametro. È possibile estendere
questa notazione per il caso nel quale non si conoscono due o più parametri
della distribuzione, scrivendo $X \sim \mathrm D(\boldsymbol \theta)$, dove
$\boldsymbol\theta$ è un vettore le cui componenti individuano i parametri
ignoti. Questo caso particolare sarà però trattato solo marginalmente.
Chiaramente, questa notazione viene introdotta solo per poter formalizzare i
concetti chiave della statistica inferenziale parametrica puntuale
indipendentemente dall'effettiva distribuzione della popolazione. Nel caso in
cui questa sia specificata, i simboli $D$ e $\theta$ verranno sostituiti
opportunamente.

```{margin}
In alcuni degli esempi preferirò in realtà scrivere simbolicamente tutti i
parametri della distribuzione della popolazione, anche nel caso in cui alcuni
siano noti, così che la soluzione si possa applicare indipendentemente dal
particolare valore che i parametri noti assumono.
```
```{prf:example}
:label: ex:population

Se la popolazione coincide con l'insieme di tutti i supereroi, e
l'osservazione di un suo individuo ha come esito $1$ nel caso in cui esso
sia un supereroe Marvel e $0$ altirmenti, la popolazione è
naturalmente descritta da una variabile aleatoria $X \sim \mathrm B(p)$,
pertanto si dice che la popolazione ha una distribuzione di Bernoulli il cui
parametro $p$ è ignoto. Dunque, $\mathrm D$ è sostituito dalla distribuzione
di Bernoulli e $\theta = p$.

Se invece l'osservazione corrisponde a misurare l'altezza del supereroe,
esprimendola in centrimetri, supponiamo che la popolazione sia descritta da
una distribuzione normale il cui valore atteso è ignoto e la cui deviazione
standard è pari a $2 \mathrm{cm}$. In questo caso avremo
$X \sim \mathrm N(\mu, 2)$, il che vuol dire che
- $\mathrm D$ corrisponde a una particolare sottofamiglia del modello normale,
  precisamente quella nella quale il valore atteso può assumere qualsiasi
  valore in $\mathbb R$ ma la deviazione standard è sempre uguale a $2$;
- $\theta = \mu$.


Va notato che, in linea di principio, sarebbe possibile introdurre il simbolo
$\sigma = 2$ e scrivere $X \sim \mathrm N(\mu, \sigma)$, ma in questo modo
la notazione non permette di capire immediatamente quale sia il parametro
ignoto.

Infine, supponiamo che nel caso precedente sia il valore atteso, sia la
deviazione standard della popolazione siano sconosciute. Avremo pertanto
$X \sim \mathrm N(\mu, \sigma)$, che corrisponde a far coincidere $\mathrm D$
con la famiglia delle distribuzioni normali e
$\boldsymbol \theta = (\mu, \sigma)$.
```

L'uso di una variabile aleatoria per modellare la popolazione è intuitivamente
legato al fatto che il campionamento da essa si lega in modo naturale
all'osservazione della variabile aleatoria stessa, come dettagliato nel
paragrafo seguente.

## Il campione

La modellizzazione del concetto di campione all'interno della statistica
inferenziale è un argomento delicato: da un lato, come informalmente indicato
alla fine del paragrafo precedente, è naturale pensare a un campione come
a un insieme $\{ x_1, \dots, x_n \}$ di osservazioni della popolazione $X$.
Questa definizione avrebbe l'innegabile vantaggio di essere molto simile a
quella vista nella parte sulla statistica descrittiva. Bisogna però tener
conto di un aspetto importante: nella statistica descrittiva il campione,
inteso come sequenza di numeri, è dato, mentre la modellazione fatta
nell'ambito della statistica inferenziale deve essere indipendente dal
_particolare_ campione osservato.

```{prf:example}
:label: ex:multiple-samples

ESEMPIO SULL'ESTRAZIONE DI DIVERSI CAMPIONI DA UNA STESSA POPOLAZIONE.
```

```{prf:definition}
:label: def:sample-is

Data una popolazione descritta da una variabile aleatoria
$X \sim \mathrm D(\theta)$ e un numero intero $n \in \mathbb N$, si definisce
un _campione aleatorio_ di dimensione $n$ come una sequenza $X_1, \dots, X_n$
di $n$ variabili aleatorie i.i.d., la cui distribuzione coincide con quella
di $X$.
```
