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

(chap:approccio)=
# Approccio

Mi è sempre risultato facile apprendere nuovi concetti mettendoli in pratica
in un contesto che potesse essere facilmente esplorato e controllato. Quando,
anni fa, ho iniziato a insegnare, mi è sembrato naturale usare lo stesso
approccio, adottando in modo inconsapevole un metodo didattico che solo più
tardi ho scoperto essere codificato nella metodologia del _learning by doing_
{cite:p}`freire1982`. Questo libro cerca di seguire la stessa filosofia,
introducendo fin da subito&mdash;ove possibile&mdash;i singoli argomenti
all'interno di un contesto applicativo.

```{margin}
L'uso della fantascienza per introdurre concetti scientifici non è
particolarmente insolito: due esempi abbastanza noti sono «La Fisica
di Star Trek» {cite:p}`krauss` e «La Fisica dei Supereroi»
{cite:p}`kakalios`[^note].
```
Per dare coerenza alla trattazione, ho deciso di contestualizzare in uno stesso
dominio gli esempi da affiancare alle parti più teoriche.
Il perimetro nel quale ho scelto di muovermi è il multiverso dei supereroi.
Potrebbe sembrare un controsenso, vista la filosofia che ho appena dichiarato:
i supereroi sono personaggi di un ambito narrativo non reale&mdash;parecchio
_fiction_, peraltro. Poter applicare un concetto a un contesto, però, prescinde
dall'effettiva realizzabilità fisica di quest'ultimo: serve solo specificare in
modo chiaro, coerente e preciso le ipotesi che descrivono una data situazione.
Ciò permette di calarsi metaforicamente in questa stessa situazione, di usare
la matematica per modellarla e l'informatica per simularla, così da poterla
esplorare utilizzando il metodo scientifico e, sperabilmente, ricavare
informazioni, prendere decisioni e così via. Oltre a essere molto divertente,
riferirsi a un mondo inesistente ha anche un altro vantaggio: permette a chi
impara di non stabilire un collegamento diretto tra l'istanza di un problema e
i metodi risolutivi da utilizzare, favorendo un apprendimento incentrato
sull'uso _critico_ di metodi e strumenti.


Nonostante mi sia imbarcato in questa impresa, non sono un
esperto di supereroi. Chiedo quindi preventivamente scusa a chi ne sa più
di me per tutte le imperfezioni e gli errori che potrei avere inserito,
sperando che questi non pregiudichino la comprensione dei concetti e degli
esempi descritti. Nonostante io sia un po' più esperto di analisi dei dati,
di calcolo delle probabilità e di statistica, non posso escludere di
avere fatto errori in generale, anche se in questo caso sono confidente di non
averne fatti troppi.

Il lavoro di scrittura è comunuque _in progress_, e
verosimilmente lo sarà ancora per parecchio tempo: segnalatemi refusi ed
errori, e più in generale esempi e materiale che pensate possano arricchire
quanto ho scritto, tenendo presente che immagini, dati e così via possono
essere pubblicati solo se sono coerenti con la licenza _Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International_
([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en))
con la quale è distribuito questo libro.
Il modo più pratico per inviarmi queste segnalazioni è quello
di sottoporre _issue_ (per segnalare errori o suggerire miglioramenti)
o _pull request_ (per proporre modifiche ai contenuti) al
[repository](https://github.com/dariomalchiodi/sds) nel quale ho
organizzato i contenuti di questo libro. Ciò richiede
familiarità con [git](https://www.git-scm.org), lo strumento di _source
control management_ che utilizzo per i miei progetti _software_.


[^note]: Userò le note a margine per dei commenti che ritengo importanti
ma che non devono appesantire la lettura dei paragrafi corrispondenti.
Relegherò invece nelle note a fine testo tutti gli approfondimenti che
possono essere tralasciati a una prima lettura.
