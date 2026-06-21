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

(sec_principio-fondamentale-combinatorica)=
# Principio fondamentale

```{figure} https://static.wikia.nocookie.net/marvel_dc/images/8/8c/Detective_Comics_241.jpg/revision/latest?cb=20081218152007
---
figclass: margin
name: fig_dc-241
width: 200px
align: left
---
Copertina del numero 241 di Detective Comics (marzo 1957). Trademarks & Copyright © 1935–2026 DC Comics, Inc.. Fonte: [DC Database, Fandom](https://dc.fandom.com/wiki/Detective_Comics_Vol_1_241).
```
Può sembrare strano, ma in alcune storie Batman ha indossato costumi molto più
vivaci rispetto al classico grigio dei fumetti originali o al nero dei film più
recenti. Nel numero 241 di _Detective Comics_ compare infatti la storia
intitolata «The Rainbow Batman». In questa versione, l'uomo pipistrello alterna
anche tenute arancioni, verdi e rosa, con l'obiettivo di attirare l'attenzione
su di sé invece che su una ferita al braccio di Robin, che avrebbe potuto
destare sospetti perché uguale a quella riportata da Dick Grayson {cite}`robb`.
Modifichiamo leggermente lo scenario: immaginiamo che Batman abbia in
guardaroba quattro mantelli (rosa, verde, rosso e marrone) e tre costumi
(giallo, azzurro e nero). In quanti modi diversi può abbinare un mantello e un
costume? La {numref}`fig_principio-fondamentale` mostra la risposta: per
ciascuno dei quattro mantelli ci sono tre costumi possibili, quindi gli
abbinamenti totali sono $4 \times 3 = 12$.

```{figure} ../../_static/img/superhero-grid.png
:width: 50%
:name: fig_principio-fondamentale

Una semplice illustrazione del principio fondamentale del calcolo combinatorio:
avendo quattro opzioni possibili per una prima scelta e tre opzioni per una
seconda scelta, si hanno dodici scelte combinate in tutto
(immagine creata ex novo dall'autore tramite IA (ChatGPT) e post-produzione
grafica).
```

Generalizzando, otteniamo il cosiddetto _principio fondamentale del calcolo
combinatorio_: dovendo fare $t$ scelte, se la prima può essere effettuata in
$s_1$ modi, la seconda in $s_2$ modi, la terza in $s_3$ modi, e così via,
allora il numero totale delle sequenze di scelta è pari a

```{math}
:label: eq-pf-comb

s_1 \cdot \ldots \cdot s_t = \prod_{i=1}^t s_i \enspace.
```

Possiamo ottenere lo stesso risultato anche costruendo un albero di decisione:
il numero di modi possibili di fare le $t$ scelte è uguale al numero delle
foglie di un albero di profondità $t$ in cui il primo livello ha $s_1$ nodi,
ciascuno con $s_2$ figli, dove ciascun figlio ha a sua volta $s_3$ figli, e
così via, come evidenziato nella {numref}`fig_tree`.


```{figure} ../../_static/img/superhero-tree.png
:width: 100%
:name: fig_tree

L'albero che corrisponde alle scelte possibili nella
{numref}`fig_principio-fondamentale` (immagine creata ex novo dall'autore
tramite IA (ChatGPT) e post-produzione grafica).
```

Come ho sottolineato all'inizio del capitolo, l'applicazione del principio
fondamentale del calcolo combinatorio non dipende dalla natura degli oggetti
considerati, siano essi mantelli, costumi, verdure o strumenti finanziari. Se,
nell'esempio precedente, avessimo abbinato tre colori a quattro modelli di
bat-mobile, avremmo ottenuto lo stesso risultato numerico. Questo fatto è vero
in generale: i risultati del calcolo combinatorio dipendono dalla numerosità
degli oggetti e, quando serve, dal numero di posti considerati. Per questo
parliamo, ad esempio, delle _permutazioni_ di $n$ oggetti o delle
_combinazioni_ di $n$ oggetti in $k$ posti, utilizzando astrattamente i termini
«oggetto» e «posto». Nei paragrafi che seguono, in ogni caso, farò spesso
riferimento a degli oggetti specifici, per esemplificare i concetti che
verranno via via esposti.


## Vero o falso?

Analizzate ciascuna delle seguenti affermazioni, che riguardano il principio
fondamentale del calcolo combinatorio, e dite se è vera o falsa, motivando il
vostro ragionamento. Cliccate su di essa per visualizzare la risposta corretta.

````{tf-item}
Il principio fondamentale si applica solo a sequenze di esattamente due scelte.
+++
**Falsa**. Il principio si generalizza a qualsiasi numero $t$ di scelte, come
formalizzato in {eq}`eq-pf-comb`. Vedremo due esempi specifici negli Esercizi
{numref}`%s <ex-pfc-xmen-pericolo>`  e {numref}`%s <ex-pfc-avengers-turni>`.
````

````{tf-item}
Abbinando un elemento di un insieme da $m$ oggetti a uno di un insieme da $n$,
si ottengono $m + n$ abbinamenti possibili.
+++
**Falsa**. Il principio fondamentale prescrive di moltiplicare, non di sommare:
gli abbinamenti possibili sono $m \times n$. Nel testo, $4$ mantelli e
$3$ costumi producono $4 \times 3 = 12$ abbinamenti, non $4 + 3 = 7$.
La somma si userebbe se le due scelte fossero alternative (o un mantello o un
costume), mentre qui si fanno entrambe in sequenza.
````

````{tf-item}
Il principio fondamentale vale anche quando il numero di opzioni è diverso da
una fase all'altra.
+++
**Vera**. Nell'esempio del testo le due fasi hanno un numero diverso di opzioni
($s_1 = 4$ mantelli, $s_2 = 3$ costumi), eppure il principio si applica
direttamente: $4 \times 3 = 12$. La formula $\prod_{i=1}^t s_i$ ammette un
numero $s_i$ di valori distinti a ogni scelta, senza alcuna restrizione.
````

````{tf-item}
In un albero di decisione, il numero di foglie corrisponde al numero totale di
sequenze di scelta.
+++
**Vera**. Il testo afferma esplicitamente che «il numero di modi possibili di
fare le $t$ scelte è uguale al numero delle foglie di un albero di profondità
$t$». Ogni percorso dalla radice a una foglia rappresenta una specifica
sequenza di scelte, e le foglie sono in tutto $\prod_{i=1}^t s_i$, quante le
sequenze calcolate dal principio fondamentale.
````

````{tf-item}
Invertire l'ordine delle scelte (prima il costume, poi il mantello) cambia il
numero totale di abbinamenti.
+++
**Falsa**. Per la commutatività della moltiplicazione, $s_1 \times s_2 =
s_2 \times s_1$: l'ordine in cui si effettuano le scelte non influisce sul
prodotto. Riprendendo l'esempio del testo, scegliere prima il costume ($3$
modi) e poi il mantello ($4$ modi) dà $3 \times 4 = 12$, lo stesso di
$4 \times 3 = 12$.
````

````{tf-item}
Il numero di abbinamenti dipende dalla natura degli oggetti (mantelli, costumi,
bat-mobili...) e non solo dalla loro numerosità.
+++
**Falsa**. Nel calcolo combinatorio ciò che conta è solo la numerosità degli
insiemi, non la natura dei loro elementi. Abbinare $4$ mantelli a $3$ costumi
porta allo stesso numero di scelte che abbinare $4$ colori a $3$ modelli di
bat-mobile.
````

## Esercizi

````{exercise} •••
:label: ex-disp-justice-society-categorie

La [Justice Society of
America](https://dc.fandom.com/wiki/Justice_Society_of_America_(New_Earth))
invia in missione tre membri in sequenza (il primo apre le ostilità, il secondo
interviene nel vivo dello scontro, il terzo copre la ritirata), scegliendo tra
quattro supereroi con poteri sovrannaturali (Lanterna Verde, Flash, Dottor Fate
e Hourman) e tre vigilanti senza superpoteri (Sandman, Wildcat e Starman).
Quante sequenze sono possibili se la prima posizione deve essere ricoperta da
un supereroe e l'ultima da un vigilante?
````
````{solution} ex-disp-justice-society-categorie
:class: dropdown

I tre posti devono essere riempiti rispettando i vincoli di categoria:

- il primo posto va a uno dei quattro supereroi con poteri sovrannaturali;
- l'ultimo posto va a uno dei tre vigilanti;
- la posizione centrale può essere occupata da uno qualsiasi dei cinque eroi
  rimasti.

Per il principio fondamentale del calcolo combinatorio, il numero di sequenze
valide è $4 \cdot 5 \cdot 3 = 60$.
````

````{exercise} ••
:label: ex-pfc-xmen-pericolo

Per classificare una missione degli X-Men, Cerebro assegna:

- un livello di minaccia tra $6$ possibili;
- una priorità tra $4$ possibili;
- un settore operativo tra $5$ possibili.

Quanti codici di missione distinti può produrre?
````
````{solution} ex-pfc-xmen-pericolo
:class: dropdown

Ogni codice è ottenuto scegliendo in sequenza una voce per ciascuna delle tre
categorie. Per il principio fondamentale del calcolo combinatorio, i codici
possibili sono quindi $6 \cdot 4 \cdot 5 = 120$.
````

````{exercise} ••
:label: ex-pfc-avengers-turni

Gli Avengers devono coprire tre turni (mattina, pomeriggio, notte) scegliendo
sempre un membro diverso tra otto disponibili. In quanti modi si può compilare
la turnazione giornaliera?
````
````{solution} ex-pfc-avengers-turni
:class: dropdown

Per il turno del mattino ci sono otto scelte, per il pomeriggio ce ne sono
sette (perché il membro scelto al mattino non può essere riutilizzato), e per
la notte sei (per considerazioni analoghe a quella precednte). Per il principio
fondamentale del calcolo combinatorio, i modi possibili di scegliere i turni
sono $8 \cdot 7 \cdot 6 = 336$.
````

````{exercise} •••
:label: ex-pfc-defenders-vincolo-capo

I [Defenders](https://marvel.fandom.com/wiki/Defenders_(Earth-616)) devono
scegliere tre ruoli distinti: capo squadra, analista tattico e supporto
operativo, partendo da sette candidati. Jessica Jones, se selezionata, può
ricoprire solo il ruolo di capo squadra. Quante assegnazioni sono possibili?
````
````{solution} ex-pfc-defenders-vincolo-capo
:class: dropdown

Consideriamo separatamente i casi nei quali Jessica Jones è selezionata oppure
no. Nel primo, il ruolo di capo è fissato, e i due ruoli rimanenti possono
essere assegnati ai restanti sei candidati. Ciò può essere fatto in $d_{6, 2}$
modi diversi. Nel secondo caso, vi sono solo sei candidati per i tre ruoli,
per cui ci sono $d_{6, 3}$ modi di procedere. Sommando i due risultati, le
assegnalzioni possibili sono quindi $d_{6, 2} + d_{6, 3} = 6 \cdot 5 + 6 \cdot
5 \cdot 4 = 30 + 120 = 150$.
````

## Concetti fondamentali

Pensate ai concetti fondamentali illustrati in questo paragrafo ed elencateli.
Nella lista qui sotto sono già presenti gli stessi concetti, ma nascosti.
Cliccate sul pulsante per mostrarli sotto forma di parole chiave, quindi
confrontateli con la vostra lista. Provate infine a descrivere ciascun concetto
con parole vostre.

````{sds-wordcloud}
Calcolo combinatorio
Numerosità
Albero di decisione
Principio fondamentale
Scelte
Sequenze
````