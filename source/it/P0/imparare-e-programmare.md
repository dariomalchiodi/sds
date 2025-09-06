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

Come descritto nel paragrafo precedente, introdurrò i concetti affiancandoli, o
talvolta precedoli, con esempi pratici. Quando possibile, mostrerò anche delle
_implementazioni_ utilizzando un linguaggio relativamente moderno. Userò
{extlink}`Python <https://www.python.org>` e il relativo _data science stack_,
costituito dalle librerie principalmente utilizzate dalla comunità open source
che si concentra sull'analisi dei dati[^librerie] (nel momento in cui questo
libro è stato scritto). Per seguire efficacemente il libro, è quindi altamente
consigliata una conoscenza di base della programmazione.
```{margin}
Questo libro nasce dall'evoluzione di una serie di dispense pensate per
studenti del secondo anno dei corsi di laurea triennale in area informatica.
Pertanto presuppone come acquisite le competenze di programmazione che vengono
acquisite generalmente al primo anno di queste lauree, o in percorsi affini.
```
Il {ref}`chap:intro-python` fornisce una panoramica a livello medio-alto delle
funzionalità di Python che utilizzo nel libro, pensata per consentire a chi sa
già programmare, ma non conosce questo linguaggio, di mettersi in pari. La
lettura di questo capitolo è comunque consigliata, perché permette di
familiarizzare fin da subito con le convenzioni che utilizzo nel codice.

```{margin}
Le componenti interattive si basano su {extlink}`PyScript
<https://pyscript.net/>`, una tecnologia che consente di eseguire codice Python
nei moderni browser web. Questa tecnologia ha il vantaggio di non richiedere
alcuna installazione o configurazione manuale, ma richiede una connessione
internet attiva e l'utilizzo di un _browser_ compatibile con WebAssembly (come
Chrome, Firefox, Edge, Safari e i navigatori basati su
Chromium).
```
Il libro è scritto utilizzando una tecnologia che permette di inserire
contenuti generati dall'esecuzione di codice Python. Ogni volta che guido chi
legge a implementare uno o più concetti, il codice viene mostrato
esplicitamente. È invece nascosto quando serve solo a produrre elementi come
tabelle o grafici, ma un link «Mostra codice» consente di
visualizzarlo[^hidden-code]. Invito caldamente lettrici e lettori a sfruttare
questa possibilità: così come leggere passivamente un testo ha poco senso,
eseguire questo codice senza riflettere è poco utile. Al contrario, è
importante analizzarlo, comprenderlo e modificarlo per capirne meglio il
funzionamento&mdash;insomma, _giocarci_ in un'ottica _hacker_, nel senso
originale del termine[^hacker]. In ogni caso, alcuni dei contenuti sono
interattivi, come mostrato per esempio nel {ref}`chap:uno-sguardo-di-insieme`:
la loro manipolazione, che non richiede di analizzare del codice, è pensata
proprio per facilitare la comprensione dei concetti introdotti.

Molto spesso guiderò chi legge nell'implementazione pratica degli strumenti
fondamentali, soprattutto nella prima parte dedicata alla statistica
descrittiva. È importante sottolineare che queste implementazioni non mirano a
sostituire le librerie professionali, bensì a permettere di concentrarsi sugli
aspetti essenziali di uno o più concetti, al fine di facilitarne
la comprensione. Il ragionamento alla base di questo modo di procedere è
analogo a quello che prevede che chi sviluppa software abbia imparato a
scrivere da zero i principali algoritmi di ordinamento (e, se necessario, sia
in grado di farlo), ma che in ambito lavorativo utilizzi le implementazioni
disponibili in librerie ottimizzate e rigorosamente validate, in misura
difficilmente ottenibile individualmente. In quest'ottica, subito dopo le
implementazioni  «fai da te», proporrò l'uso di librerie allo stato dell'arte.

Chi non ha esperienza di programmazione può comunque leggere questo libro,
saltando semplicemente le parti che contengono, descrivono e discutono il
codice. In questo caso, è opportuno essere consapevoli del rischio di non
apprendere pienamente i contenuti, dal momento che buona parte della
trattazione alterna spiegazioni e codice. In tale situazione, consiglio di
prendere in considerazione libri che seguono un approccio più tradizionale,
come:

- Probabilità e Statistica per le scienze e l'ingegneria, di Sheldon Ross
  {cite:p}`ross`,
- Introduzione alla statistica di Marylin K. Pelosi, Theresa M. Sandifer,
  Paola Cerchiello e Paolo Giudici {cite:p}`pelosi`.


Voglio mettere in guardia chi pensa di usare questo libro per imparare a
programmare mentre, nello stesso tempo, impara ad analizzare dati. Questo
__non è__ un libro per imparare a programmare, ma piuttosto un libro per
imparare __usando__ la programmazione, scrivendo cioè codice per rendere più
solido il processo di apprendimento di un'altra materia. Si dice che si è
compreso veramente qualcosa solo quando si è in grado di spiegarla alla
propria nonna[^cite-granny]. Io rilancio, dicendo che non si padroneggia
davvero un concetto tecnico se non si è in grado di implementarlo scrivendo un
programma. Per seguire questa filosofia, però, bisogna già saper scrivere
_software_, e questa è una competenza che richiede tempo, energia e materiali
didattici dedicati per essere acquisita. Per chi parte da zero, consiglio
alcuni testi di riferimento, più o meno recenti:

- {extlink}`Pensare in Python </sds/short/thinkpython-it>`, di Allen B. Downey
  {cite:p}`downey`,
- Programmazione in C, di Kim N. King {cite:p}`king`,
- Programmare in Go, di Ivo Balbaert {cite:p}`balbaert`.

Ho scelto libri dedicati a linguaggi diversi, per sottolineare come non conti
tanto conoscere i dettagli di un linguaggio in particolare, ma capire bene le
basi della programmazione come disciplina a sé stante. Infine, anche se ho
citato testi in italiano, vale sempre la pena valutare la versione originale in
inglese: spesso è più aggiornata e scritta pensando anche a chi non è
madrelingua. Questo aiuta a familiarizzare con il gergo tecnico e a comunicare
facilmente sui canali online dedicati alla programmazione, che sono una risorsa
preziosa per risolvere problemi.


````{margin}
```{figure} ../../_static/img/whistle.jpg
---
name: fig-whistle
height: 100px
---
Un fischietto Cap’n Crunch Bo’sun (immagine del Heinz Nixdorf MuseumsForum,
distribuita sotto licenza {extlink}`CC BY-NC-SA 4.0
<https://creativecommons.org/licenses/by-nc-sa/4.0/>`)
```
````

[^librerie]: Il {extlink}`repository <https://github.com/dariomalchiodi/sds>`
associato a questo libro contiene un file che elenca tutte le librerie
utilizzate per generare i contenuti, incluse quelle necessarie per eseguire il
codice.

[^hidden-code]: È importante tenere presente che il codice nascosto può
contenere dettagli tecnici legati alla generazione di contenuti da visualizzare
nelle pagine web (ad esempio, elementi HTML o stili CSS). Di conseguenza, non è
scritto nello stesso modo in cui lo si scriverebbe per analizzare dati in un
ambiente di lavoro tradizionali: la sua struttura risponde a esigenze di
presentazione e interattività, più che di analisi.

[^hacker]: Il termine _hacker_ è usato nel linguaggio di tutti i giorni con
un'accezione negativa, riferita a chi persegue intenti dolosi scrivendo o
modifcando _software_, o sfruttando falle di sicurezza per utilizzare in modo
improprio delle tecnologie informatiche. In origine, però, non era così.
Nell'inglese moderno questo termine compare intorno al 1960 con una
connotazione più neutra, non necessariamente collegata all'informatica:
indicava una persona capace di capire in profondità il funzionamento di un
sistema, al punto di saperlo controllare e adattare a scopi diversi da quelli
previsti da chi lo aveva progettato. Uno dei primi _hack_ famosi&mdash;per
quanto illegale&mdash;riguardava l'uso del «Cap’n Crunch Bo’sun Whistle» (un
fischietto che si trovava in regalo nelle scatole di una famosa marca di
cereali, mostrato in {numref}`fig-whistle`) per effettuare chiamate interurbane
e internazionali gratuite da alcuni telefoni pubblici negli Stati Uniti. Uno
degli ambienti nei quali la controcultura hacker iniziò a svilupparsi fu il
Massachusetts Institute of Technology (MIT): la prima traccia scritta del
termine «hacking» fa riferimento al verbale di una riunione del 1955 del
{extlink}`Tech Model Railroad Club <http://tmrc.mit.edu/>`,un
gruppo di studenti appassionati di modellismo ferroviario. L'associazione
diretta con mondo informatico è arrivata solo più tardi.

[^cite-granny]: Risulta difficile risalire all'autore di questa massima: c'è
chi la attribuisce a Einstein, chi a Feynmann e chi a Rutherford (pare dunque
che ci sia consenso sul contesto delle scienze fisiche). Inoltre, nella sua
versione più nota, il detto appare decisamente stereotipato nei confronti delle
nonne, e questo è probabilmente legato al fatto che ha iniziato a circolare
parecchio tempo fa. Esistono in effetti diverse varianti: alcune altrettanto
discutibili, in cui la nonna è rimpiazzata per qualche motivo da un barista, e
altre nelle quali al suo posto compare un bambino.
