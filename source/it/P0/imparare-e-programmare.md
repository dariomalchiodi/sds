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

(sec:imparare-e-programmare)=
# Imparare <span class="ast">\*</span>e<span class="ast">\*</span> programmare

Come descritto nel paragrafo precedente, introdurrò i concetti affiancandoli (o
facendoli precedere) da esempi. Dove possibile, mostrerò anche delle
_implementazioni_ utilizzando un linguaggio relativamente moderno: in
particolare, farò riferimento a [Python](https://www.python.org){.external} e
al relativo _data science stack_, costituito dai package che sono ampiamente
utilizzati, al tempo in cui scrivo, dalla comunità open source che fa
riferimento all'analisi dei dati[^librerie]. È quindi altamente consigliata una
competenza di base nella programmazione degli elaboratori.
```{margin}
Questo libro rappresenta l'evoluzione di una serie di dispense pensate per
studenti del secondo anno delle lauree triennali di area informatica, dunque
farò riferimento al livello di conoscenza di programmazione che si apprende al
primo anno nelle stesse lauree, o in lauree di aree affini.
```

Il {ref}`chap:intro-python` contiene una
descrizione a livello medio-alto delle funzionalità di Python che sono
utilizzate, e può essere utilizzato per mettersi in pari da chi sa già
programmare, ma non conosce questo linguaggio. Una lettura di questo capitolo è
comunque consigliata a tutti, al fine di familiarizzare con le convenzioni che
utilizzo per scrivere codice.

Questo libro è scritto utilizzando una tecnologia che permette di inserire dei
contenuti generati tramite l'esecuzione di codice python. Questo codice viene
mostrato esplicitamente ogni volta che il lettore viene guidato
nell’implementazione di uno o più concetti. Quando invece serve solo a produrre
elementi come tabelle o grafici, il codice viene mostrato, ma un link «Mostra
codice» consente al lettore di attivare o disattivare la visibilità del codice
nascosto. Invito tutti a sfruttare questa possibilità: così come leggere
passivamente un testo ha poco senso, eseguire questo codice senza riflettere è
inutile; al contrario, è importante analizzarlo, comprenderlo e modificarlo
(valgono anche le modifiche che permettono di capire meglio il
codice!)&mdash;insomma, _giocarci_ in un'ottica _hacker_, nel senso originale
del termine[^hacker]. In realtà è anche possibile giocare con il libro senza
necessariamente dover comprendere il codice ed eseguirlo: come mostrato nel
{ref}`chap:uno-sguardo-di-insieme`, una parte dei contenuti è interattiva, e la
sua manipolazione è pensata proprio per facilitare la comprensione dei concetti
introdotti.
```{margin}
Il libro è stato generato utilizzando [MyST](https://mystmd.org/){.external},
che comprende sia una variante del formato testuale
[Markdown](https://en.wikipedia.org/wiki/Markdown){.external}, sia il sofware
che permette di tradurre il codice corrispondente nelle pagine HTML che state
leggendo.

L'utilizzo delle componenti interattive è basato su alcune tecnologie (in
particolare,
[JupyterLite](https://github.com/jupyterlite/jupyterlite){.external}) che sono
al momento ancora in una fase preliminare di sviluppo, ma che hanno il grande
vantaggio di non richiedere alcuna installazione manuale. D'altro canto, è
spesso necessario armarsi di pazienza e assicurarsi di utilizzare uno
dei browser web supportati.
```


Molto spesso cerco di guidare il lettore in una vera e propria implementazione
degli strumenti fondamentali, soprattutto nella prima parte, relativa alla
statistica descrittiva. Il risultato al quale arrivo non è da considerarsi al
livello delle librerie professionali: da una parte, lo scopo è quello di
concentrarsi sugli aspetti fondamentali per facilitare l'apprendimento di uno o
più concetti. Dall'altro, queste implementazioni non sono pensate per essere
utilizzate in ambito lavorativo: esattamente come è ragionevole che uno
sviluppatore abbia imparato a scrivere da zero i principali algoritmi di
ordinamento (e, se dovesse servire, sia in grado di farlo), ma che faccia in
seguito riferimento alle loro implementazioni in una libreria, ottimizzate e
validate sicuramente meglio di quanto un singolo possa ragionevolmente fare in
autonomia. In quest'ottica, subito dopo le implementazioni  «fai da te», i
lettori sono indirizzati all'uso di librerie allo stato dell'arte.

In linea di principio, anche chi non sa programmare gli elaboratori può
leggere questo libro, saltando semplicemente le parti che contengono,
descrivono e discutono il codice. Ma in questo caso è opportuno valutare bene
il rischio di non apprendere i contenuti in modo ottimale, tenuto conto del
fatto che buona parte del libro è stata scritta alternando testo e codice.
A questo tipo di lettori consiglio di prendere in considerazione testi scritti
usando un approccio più tradizionale, come per esempio:

- Probabilità e Statistica per le scienze e l'ingegneria, di Sheldon Ross
  {cite:p}`ross`,
- Introduzione alla statistica di Marylin K. Pelosi, Theresa M. Sandifer,
  Paola Cerchiello e Paolo Giudici {cite:p}`pelosi`.


Va anche messo in guardia chi non sa programmare e si trova davanti alla
tentazione di leggere questo libro per apprendere a farlo, magari mentre in
contemporanea impara ad analizzare dati. Questo __non è__ un libro per imparare
a programmare, ma piuttosto un libro per imparare programmando, usando la
capacità di scrivere codice per arricchire il processo di apprendimento di
un'altra materia. Si dice che non si è veramente capita una cosa se non si è
in grado di spiegarla alla propria nonna[^cite-granny]: faccio mia questa
massima, sperando di non distorcerla troppo dicendo che non si è veramente
capito un concetto tecnico se non si è in grado di implementarlo scrivendo un
programma. Se si vuole però seguire questa filosofia, bisogna già
avere imparato a scrivere _software_, e questa è una competenza che richiede
tempo, energia e del materiale dedicato all'apprendimento della materia.
Anche in questo caso, ci sono parecchi libri che possono essere utilizzati
con profitto, per esempio:

- <a href="/sds/short/thinkpython-it" target="_blank">Pensare in Python</a>, di
  Allen B. Downey {cite:p}`downey`,
- Programmazione in C, di Kim N. King {cite:p}`king`,
- Programmare in Go, di Ivo Balbaert {cite:p}`balbaert`.

Ho volutamente messo nell'elenco precedente tre volumi più o meno recenti,
e soprattutto ognuno dedicato a un linguaggio diverso: lo scopo, in questo
caso, è infatti quello di imparare le basi della programmazione e non i
dettagli di un linguaggio specifico. Infine, questo paragrafo fa riferimento
solamente a libri scritti in italiano, ma è sempre da considerare la
possibilità di studiare sulla versione originale di un libro quando questa
è scritta in inglese, o quando esiste una versione in inglese specificamente
concepita per studenti di madre lingua non inglese.


````{margin}
```{figure} ../../_static/img/whistle.jpg
---
name: fig-whistle
height: 100px
---
Un fischietto Cap’n Crunch Bo’sun (immagine del Heinz Nixdorf MuseumsForum,
distribuita sotto licenza [CC BY-NC-SA
4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)){.external}
```
````

[^librerie]: Il [repository](https://github.com/dariomalchiodi/sds/){.external}
associato a questo libro contiene un file che elenca tutte le librerie
utilizzate per generare i contenuti, incluse quelle necessarie per eseguire il
codice.

[^hacker]: Il termine _hacker_ viene oggigiorno utilizzato nel linguaggio
comune dandogli un'accezione negativa, che essenzialmente lo accomuna a chi
persegue intenti dolosi scrivendo o modifcando _software_, o in generale
sfruttando delle falle di sicurezza al fine di utilizzare in modo improprio
delle tecnologie informatiche esistenti. In realtà, l'uso di questo termine
nell'inglese moderno viene fatto risalire intorno al 1960, conferendogli però
una connotazione più neutra, e non direttamente collegata all'informatica:
quella di indicare una persona con il talento di comprendere in profondità il
funzionamento di un sistema, e dunque di essere in grado di controllarlo al
punto di poterlo utilizzare in modo diverso rispetto agli scopi per cui il
sistema era stato progettato. Giusto per citare un esempio, uno dei primi
_hack_ famosi&mdash;peraltro illegale&mdash;riguardava l'uso del «Cap’n Crunch
Bo’sun Whistle» (un fischietto che si trovava in regalo nelle scatole di una
famosa marca di cereali, mostrato in @fig-whistle) per fare telefonate
interurbane o internazionali gratuite con alcuni telefoni pubblici negli Stati
Uniti. Uno degli ambienti nei quali la controcultura hacker ha iniziato a
svilupparsi è quello del Massachusetts Institute of Technology (MIT): la prima
traccia scritta del termine «hacking» fa riferimento al verbale di una riunione
del 1955 del [Tech Model Railroad Club](http://tmrc.mit.edu/){.external}, che
riuniva studenti appassionati di modellismo ferroviario. Solo più recentemente
è avvenuta un'identificazione rispetto al mondo informatico.

[^cite-granny]: Risulta complicato risalire all'autore di questa massima:
c'è chi la attribuisce ad Einstein, chi a Feynmann e chi a Rutherford (pare
dunque che ci sia consenso sul contesto delle scienze fisiche);
ci sono anche varianti in cui la nonna è sostituita da un bambino, o&mdash; per
qualche motivo&mdash;perfino da un barista.
