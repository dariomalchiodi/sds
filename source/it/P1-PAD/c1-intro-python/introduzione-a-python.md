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

(chap:intro-python)=
# Elaborare i dati con Python

> <span title="Man mano che progredirete nella programmazione, svilupperete una
sorta di senso estetico che vi aiuterà a riconoscere quando il codice è scritto
in modo elegante. E realizzerete che leggerlo è più facile, così come diventa
immediato capirne lo scopo. Inoltre, se un programma è ben scritto diminuisce
il rischio di introdurre errori quando lo si modifica o lo si estende.
Pensate sempre che scrivere codice «bello» è soprattutto un atto di cortesia
verso chi in futuro dovrà metterci mano &mdash; e molto spesso saremo noi a
doverlo fare. Allo stesso modo, apprezzerete immensamente il fatto di lavorare
con codice altrui che è scritto bene, perché vi semplificherà la vita. Le
regole che seguono rapresentano delle indicazioni pratiche per scrivere codice
Python elegante: quello che in gergo si chiama «codice pythonico».">Beautiful
is better than ugly.</span><br/>
> <span title="Il codice dovrebbe sempre riflettere chiaramente l'intento
originale di chi lo ha scritto: meglio prendersi il tempo di renderlo
esplicito una sola volta, quando si scrive un programma, che doversi
scervellare per «scoprirlo» ogni volta che lo si legge.">Explicit is better
than implicit.</span><br/>
> <span title="Il punto non è mostrare la propria maestrìa nelle tecniche Jedi
di programmazione: soluzioni semplici sono sempre da preferire a costrutti
complessi, perché oltre a essere più leggibili sono anche più a prova di
bug.">Simple is better than complex.</span><br/>
> <span title="Ci sono problemi difficili, che non si possono risolvere se non
scrivendo codice complesso. Ma complesso non vuole dire complicato, nel senso
di mal organizzato o disordinato (quello che in gergo anglofono viene
scherzosamente chiamato «spaghetti code»).">Complex is better than
complicated.</span><br/>
> <span title="Il modo migliore di scrivere codice elegante è quello di
organizzare la sua logica in modo lineare, limitando allo stretto necessario
l'uso di strutture dati annidate, che «spostano» rapidamente il codice a destra
(la tabulazione è obbligatoria in Python) e aumentano lo sforzo mentale
necessario per ricordare la particolare combinazione di condizioni in cui ci si
trova quando si legge una porzione di programma. Meglio ragionare «per casi»,
con uscite di funzione anticipate, e usare le comprehension al posto dei
cicli espliciti.">Flat is better than nested.</span><br/>
> <span title="Meglio organizzare il codice in più linee, sfruttando spazi,
tabulazioni e righe vuote per aumentarne la leggibilità.">Sparse is better
than dense.</span><br/>
> <span title="Una riga di codice viene scritta o modificata poche volte
rispetto a quanto viene letta. Scrivere codice facile da leggere è dunque un
investimento per un futuro più semplice da gestire.">Readability
counts.</span><br/>
> <span title="Lo stile di programmazione è personale, ma non va adattato
ogni volta ai casi particolari che emergono quando si risolve un problema.
Anche la coerenza nel modo di scrivere codice è uno degli aspetti che
contribuiscono &mdash; non poco! &mdash; a renderlo leggibile.">Special cases
aren't special enough to break the rules.</span><br>
> <span title="Ci sono comunque delle eccezioni alla regola precedente, nelle
quali infrangere una regola di stile è decisamente più efficace rispetto a
rispettarla «piegando» la soluzione a un problema. Insomma: quando ci vuole,
ci vuole!">Although practicality beats purity.</span><br/>
> <span title="Le condizioni di errore vanno comunicate in modo esplicito,
e non appena si verificano, altrimenti correggere i bug può diventare parecchio
complicato..">Errors should never pass silently.</span><br/>
> <span title="Ci sono però dei casi nei quali le eccezioni si possono
silenziare, per esempio perché sappiamo che sono innocue o perché ci permettono
di isolare casi speciali da trattare separatamente. La cosa importante è che
il codice indichi chiaramente qual è la strategia di programmazione
operata.">Unless explicitly silenced.</span><br/>
> <span title="Quando qualcosa non funziona, procedere per tentativi non si
rivela quasi mai una strategia efficace. Meglio armarsi di pazienza e capire
bene quali sono le cause del problema.">In the face of ambiguity, refuse the
temptation to guess.</span><br/>
> <span title="Ogni linguaggio di programmazione promuove i propri pattern
di codice: costrutti da usare per eseguire compiti che 
tendono a ripetersi molto spesso quando si scrive codice. Sicuramente esistono
modi alternativi per risolvere lo stesso problema, ma adeguarsi a questi
pattern facilita agli altri la lettura di quel che scriviamo. E in genere porta
anche a soluzioni più efficienti.">There should be one&mdash;and preferably
only one&mdash;obvious way to do it.</span><br/>
> <span title="Python non fa eccezione alla regola precedente, ma chi già
conosce altri linguaggi può dover faticare un po' prima di adattarsi a
scrivere codice pythonico. Il riferimento scherzoso è legatto alle origini di
Guido van Rossum, il creatore di Python.">Although that way may not be obvious
at first unless you're Dutch.</span><br/>
> <span title="Meglio scrivere un'implementazione subottimale che attendere
di aver trovato quella ideale, cosa che potrebbe non succedere mai. Questo
vale non solo per la creazione di nuovo codice (Python è particolarmente
indicato per scrivere codice prototipale), ma anche per migliorare quello già
esistente.">Now is better than never.</span><br/>
> <span title="D'altro canto, è importante evitare di cadere nella tentazione
di produrre una soluzione in tempi rapidissimi: la fretta tende a portare
errori, e a volte è saggio sapere quando è meglio aspettare.">Although never is
often better than \*right\* now.</span><br/>
> <span title="Se non siete in grado di spiegare che cosa succede quando viene
eseguito il vostro codice, probabilmente questo è basato su una logica
complicata. Ciò è tipicamente sintomo di qualche errore concettuale.">If the
implementation is hard to explain, it's a bad idea.</span><br/>
> <span title="Al contrario, quando la logica dietro al codice è facile da
spiegare significa che la soluzione implementata è probabilmente solida.">If
the implementation is easy to explain, it may be a good idea.</span><br/>
> <span title="Usare i namespace (tipicamente a livello di modulo) permette
di non incorrere in collisioni tra i nomi, di evitare un elevato numero di
importazioni e di ottenere del codice più ordinato.">Namespaces are one honking
great idea &mdash; let's do more of those!</span><br/>
>
> --- The Zen of Python, by Tim Peters


Questo capitolo descrive brevemente i principali strumenti che permettono di
analizzare dati in modo esplorativo usando [Python](https://www.python.org)
come linguaggio di programmazione, i
[notebook](https://en.wikipedia.org/wiki/Notebook_interface) per scrivere ed
eseguire il codice e le principali librerie del cosiddetto _Python data science
stack_, che saranno introdotte via via che queste si riveleranno necessarie.
```{margin}
I _notebook_ possono essere eseguiti in vari ambienti di sviluppo: al
momento in cui questo libro è stato scritto tra quelli più diffusi ci sono
[Jupyter](https://jupyter.org/) e [Visual Studio
Code](https://code.visualstudio.com/), che hanno anche il vantaggio
di essere gratuiti, sebbene esistano altre alternative.
```

Tutti gli strumenti a cui farò riferimento ricadono nella categoria del
[FLOSS](https://it.wikipedia.org/wiki/Free_and_Open_Source_Software),
e sono pertanto distribuiti con licenze che ne permettono, tra le altre cose,
il libero utilizzo.
```{margin}
L'acronimo FLOSS sta per «Free/Libre Open Source Software»
```

La trattazione è pensata per studenti che hanno già familiarità con la
programmazione degli elaboratori e, in particolare, sono fluenti con almeno un
linguaggio di programmazione che adotta l'approccio imperativo e procedurale.
Introdurrò invece alcune conoscenze di base del paradigma di programmazione
orientato agli oggetti, necessarie per utilizzare il _data science stack_ di
Python e che non sempre sono alla portata di chi si appresta a studiare la
materia.


La citazione riportata all'inizio del capitolo elenca $19$ linee guida da
seguire per scrivere codice in modo da sfruttare l'eleganza e le strutture
sintattiche di Python, piuttosto che mimare in modo pedissequo la sintassi di
altri linguaggi: quello che in gergo si chiama «scrivere codice pythonico».
Queste linee guida, di pubblico dominio, sono state scritte nel 1999 da Tim
Peters, uno dei principali contributori di Python. Oltre a essere pubblicate in
un’[apposita sezione](https://peps.python.org/pep-0020/) dei _Python
Enhancement Proposals_, vengono automaticamente visualizzate eseguendo la linea
di codice Python `import this`. Se posizionate il cursore sopra ogni riga,
apparirà un mio breve commento che ne spiega il significato.