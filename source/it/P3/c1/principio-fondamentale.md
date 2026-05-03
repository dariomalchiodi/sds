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