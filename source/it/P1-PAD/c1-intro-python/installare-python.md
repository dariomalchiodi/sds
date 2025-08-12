---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
nb_execution: false
---

(sec:installazione)=
# Installazione, configurazione e primi passi

Questo paragrafo descrive come installare Python e le librerie utilizzate nel
libro. Nel contempo, introdurrò alcune buone abitudini che è opportuno imparare
fin da subito a utilizzare per tutti i progetti software legati all'analisi dei
dati, come l'utilizzo degli ambienti virtuali di esecuzione e dei _package
manager_. Chi ha già dimestichezza con Python e ha a disposizione
un'installazione funzionante può probabilmente saltare direttamente al
paragrafo successivo, sebbene anche in questo caso consiglio una rapida
lettura, sia per allinearsi con la terminologia che utilizzerò, sia per
sincerarsi che non vi siano problemi di incompatibilità della versione già
disponibile e che tutte le librerie necessarie siano già installate.

(sec:linguaggi-versioni-implementazioni)=
## Linguaggi, versioni e implementazioni
I linguaggi di programmazione evolvono nel tempo, perché con il passare degli
anni le loro specifiche vengono aggiornate. Il risultato di questi cambiamenti
è una serie di _versioni_ del linguaggio. A oggi, per individuare le specifica
versione di un linguaggio di programmazione (ma anche di una libreria o in
generale di un prodotto software), è ampiamente utilizzato il cosiddetto schema
di [versionamento semantico](https://semver.org/lang/it){.external} che, nella
sua incarnazione più semplice, descrive una versione tramite una sequenza
`X.Y.Z` formata da tre numeri interi, inizialmente fissati a zero e
incrementati ogni volta che vengono effettuati degli aggiornamenti:

- `X` indica la _major release_, e viene aumentato quando si introducono
  cambiamenti non compatibili con le versioni precedenti,
- `Y` rappresenta la _minor release_, e si incrementa quando vengono aggiunte
  nuove funzionalità che sono comunque retrocompatibili,
- `Z` denota un numero di _patch_, legato a modifiche di carattere minore.

In generale, a meno che non sia necessario riferirsi a un'implementazione
con un elevato grado di precisione, per indicare una versione specifica di
Python ci si limita a specirifarne la _major_ e la _minor release_. Per
esempio, nonostante il codice di questo libro sia stato scritto utilizzando la
versione 3.11.11 di Python, io farò riferimento più in generale alla versione
3.11, perché il codice risulta eseguibile indipendentemente dal particolare
numero di _patch_. Inoltre non dovrebbero esserci, verosimilmente, problemi
a utilizzare _minor release_ differenti: in particolare, _minor_ più recenti
dovrebbero essere utilizzabili senza alcun problema, mentre è opportuno evitare
l'uso di _minor_ particolarmente meno recenti.

Potrebbe dunque sembrare che stabilire con precisione la versione di un
linguaggio di programmazione permetta di individuarne rigorosamente tutte le
funzionalità, ma non è così. Infatti, definire un linguaggio significa definire
una serie di _specifiche_, ma una cosa è definire il linguaggio in termini
della sua sintassi e della sua semantica, e un'altra è costruire gli strumenti
che permettono di eseguire i corrispondenti programmi, come gli interpreti e i
compilatori[^compilatori]. Questi strumenti possono essere realizzati in
momenti differenti, da persone diverse e usando di volta in volta specifiche
tecnologie. Il risultato sono diverse _implementazioni_ del linguaggio. Anche
quando si riferiscono allo stesso numero di versione, non sono necessariamente
identiche: le specifiche del linguaggio, infatti, non sempre entrano nel
dettaglio specifico di come certe funzionalità debbano essere realizzate. Per
esempio, potrebbe essere dipendente dalla particolare implementazione il
formato di codifica da utilizzare per le stringhe. Per quanto riguarda Python,
esistono <a href="/sds/short/py-implementations" target="_blank">varie
implementazioni</a> che differiscono nella particolare tecnologia usata per
eseguire i programmi: una è basata sulla _Java virtual machine_, un'altra su
uno strumento analogo basato sul linguaggio C, un'altra ancora è pensata per
l'esecuzione in un browser Web, e così via. L'implementazione più diffusa (che
tipicamente viene installata per _default_) viene chiamata _CPython_ e, come
suggerito dal nome, è stata scritta usando il linguaggio C.

(sec:download-book)=
## Scaricare i contenuti del libro
Questo libro è pensato per essere fruito tramite la mediazione di un server
web. Il lato positivo è che le parti interattive possono essere utilizzate
senza che sia necessario installare o configurare librerie, ma d'altro canto
ciò richiede una connessione dati permanentemente attiva. Volendo, è possibile
scaricare i contenuti del libro e generare i suoi paragrafi come pagine gestite
da un server web locale. Questa opzione richiede però l'installazione
preventiva del software che gestisce il processo di generazione. Va notato che
per esecguire le parti interattive è comuqnue necessario essere collegati a
internet.

```{margin}
Per poter clonare il _repository_ del libro è necessario avere un _client_ git
installato sul proprio sistema, disporre di un account GitHub e aver associato
a quest'ultimo una chiave SSH pubblica. In alternativa, è possibile effettuare
la clonazione usando il protocollo HTTPS, semplificando alcuni passi (per
esempio, non è richiesta la chiave SSH) ma complicandone altri.
```
Il modo consigliato per scaricare il libro è basato sull'utilizzo di
[git](https://git-scm.com){.external}, un sistema di _source control
management_ usato per per organizzare il codice sorgente in un progetto
software. Per fare questo è sufficiente aprire un terminale, posizionarsi in un
punto del _file system_ nel quale si vogliono salvare i contenuti ed eseguire
il comando che segue, che clona localmente il
[repository](https://github.com/dariomalchiodi/sds){.external} del libro
inserendolo in una directory `sds` creata appositamente.

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      Negli esempi seguenti, il simbolo ``$`` indica il _prompt_ di una
      _shell_, che nel sistema che usate potrebbe essere visualizzato
      diversamente. Solo nell'esempio qui sotto, invece, ``my_parent_dir`` è un
      nome fittizio da sostituire con il percorso nel quale intendete salvare
      la directory del libro.

      .. code-block:: bash

         $ cd my_parent_dir
         $ git clone git@github.com:dariomalchiodi/sds.git
         $ cd sds

      Nel seguito del paragrafo supporrò che la _shell_ nella quale sono stati
      inseriti questi comandi sia rimasta aperta.

   .. group-tab:: Windows

      Negli esempi seguenti, la dicitura ``C:>`` indica il _prompt_ di
      una _PowerShell_, che nel sistema che usate potrebbe essere visualizzato
      diversamente. Solo nell'esempio qui sotto, invece, ``my_parent_dir`` è un
      nome fittizio da sostituire con il percorso nel quale intendete salvare
      la directory del libro.

      .. code-block:: powershell

         C:> cd my_parent_dir
         C:> git clone git@github.com:dariomalchiodi/sds.git
         C:> cd sds

      Nel seguito del paragrafo supporrò che la *PowerShell* nella quale sono
      stati inseriti questi comandi sia rimasta aperta.

```
```{margin}
Per poter eseguire questa operazione è necessaria una connessione internet
attiva.
```

Volendo, è anche possibile scaricare un unico archivio ZIP, ma usare git
permette di allineare facilmente il libro con la sua versione più recente, nel
momento in cui vengono pubblicati degli aggiornamenti dei contenuti, eseguendo
il comando

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         $ git pull

   .. group-tab:: Windows

      .. code-block:: powershell

         C:> git pull

```

da un terminale, posizionandosi preventivmente nella directory `sds` creata
quando è stato clonato il _repository_ del libro (o in una sua sotto-directory).
Inoltre, git è lo strumento da utilizzare anche per segnalare errori o proporre
modifiche, inviando _issue_ o _pull request_ come già indicato nel
{ref}`chap:approccio`. Infine, imparare a usare git è una cosa che raccomando a
chiunque approcci lo studio non solo dell'informatica, ma anche di
tutte le discipline che in qualche modo afferiscono alla _data science_. Di
fatto, git è lo strumento più utilizzato per la gestione dei progetti software:
imparare a usarlo fin da subito è un investimento utile.


## Installare Python

L'installazione di Python è fortemente dipendente dal sistema operativo
utilizzato. Nelle distribuzioni recenti di Linux e di Mac OS Python è già
preinstallato, mentre in Windows è necessario installarlo manualmente. In ogni
caso, il computer che state utilizzando potrebbe già disporre di una
distribuzione di Python: per verificare se sia così, è possibile lanciare un
terminale, eseguire il comando

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         $ python --version

   .. group-tab:: Windows

      .. code-block:: powershell

         C:> python --version

```

e notare che tipo di output si ottiene. Sono possibili tre casi:

1. l'esecuzione ha come effetto quello di stampare a video la stringa
   `Python 3.Y.Z`, a indicare che è disponibile la _major release_ 3 di
   Python, e `Y` e `Z` indicano i rispettivi numeri di _minor release_ e di
   _patch_, dove `Y` è maggiore o uguale a $5$;
2. viene stampata una sigla simile, ma la major release è `1` oppure `2`, o
   in alternativa la major release è `3` ma la minor release è inferiore a $5$,
   a indicare che è disponibile una versione di Python, ma questa
   è troppo vecchia per eseguire tutto il codice che troverete nel resto del
   libro: io farò riferimento alla versione 3.11, che è ampiamente diffusa nel
   momento in cui sto scrivendo questo paragrafo;
```{margin}
Se la _major release_ è `4` o superiore, allora state leggendo questo libro
parecchio tempo dopo che l'ho scritto, ed è probabile che parte del contenuto
sia obsoleta. In questo caso, verificate se è disponibile una versione
aggiornata del libro o consultate della documentazione più recente.
``` 
3. si ottiene un errore che indica che `python` non è tra i comandi
   disponibili: questo è indice del fatto che probabilmente non è installata
   alcuna versione di Python.

Nella prima ipotesi, molto probabilmente è possibile utilizzare la versione
di Python già installata per eseguire tutto il codice contenuto in questo
libro. Vale però la pena sincerarsi del fatto che la versione installata sia
il più possibile allineata a quella che ho usato io. Se il numero di versione è
sensibilmente diverso potrebbero verificarsi dei problemi di compatibilità:
se ciò dovesse succedere, sarà necessario installare la versione  alla quale
faccio riferimento, affiancandola a quella già presente.
```{margin}
In teoria è possibile rimpiazzare la versione preesistente di Python, ma ciò
espone al rischio che altro software basato su di essa smetta di funzionare
correttamente. Pertanto sconsiglio di procedere in tal senso.
```

Nel secondo caso, potrebbe comunque esistere un'installazione del
linguaggio in una versione compatibile, ma il comando `python` fa riferimento
a un'altra versione. Per sincerarsene, è possibile scrivere `python`
nel terminale e premere il tasto {kbd}`TAB`, senza aggiungere spazi: in
presenza di più installazioni, i nomi dei corrispondenti comandi vengono 
automaticamente stampati. Anche nel terzo caso, Python potrebbe essere
installato senza che il vostro terminale risulti configurato per eseguirlo, ma
si tratta di un'eventualità abbastanza remota.
```{margin}
Normalmente, per ogni versione installata è disponibile un comando, e il
nome corrispondente di questo comando è `pythonX.Y`, dove `X` e `Y`
corrispondono ai numeri di _major_ e _minor release_. Il comando `python` è un
_alias_ a uno di questi comandi, tipicamente alla versione che viene
maggiormente utilizzata dal software di sistema.
```

Se dovesse risultare necessario installare Python, è possibile fare riferimento
alla documentazione ufficiale, che prevede guide separate per sistemi basati su
[Unix (come Linux)](https://docs.python.org/3/using/unix.html){.external},
[Mac OS](https://docs.python.org/3/using/mac.html){.external} e
[Windows](https://docs.python.org/3/using/windows.html){.external}.


## Creare un ambiente virtuale di esecuzione

Python viene normalmente utilizzato insieme a varie librerie. Sconsiglio però
di adottare un approccio _monolitico_, aggiungendo librerie ogni volta che
servono: man mano che il tempo passa, aumenta il numero di librerie utilizzate
e cresce il rischio di incompatibilità tra il sistema esistente e una nuova
libreria della quale potreste avere bisogno. Considerazioni analoghe si possono
fare nel momento in cui una o più librerie vengono aggiornate a una versione
più recente. Per aggirare questo tipo di rischi, è altamente consigliabile
compartimentare l'installazione delle librerie: eseguire cioè Python in uno
spazio logicamente isolato nel quale aggiungere tutte e sole le librerie
necessarie per uno specifico progetto software. Questi spazi isolati vengono
chiamati _environment virtuali_, o _ambienti virtuali di esecuzione_ (nel
seguito parlerò per brevità di _environment_ o di ambienti virtuali). Un
ambiente virtuale viene attivato ogni volta che si inizia a lavorare su un
progetto, e si disattiva prima di passare a lavorare su altro.

Esistono diverse implementazioni del concetto di _environment_ virtuale in
Linux: in questo libro farò riferimento a _venv_[^environment], che è
automaticamente installato insieme alle versioni recenti di Python. Per creare
un ambiente virtuale si procede usualmente nel modo che segue: usando la stessa
_shell_ del paragrafo precedente, controllando di risultare posizionati nella
directory `sds`, si esegue il comando

```{margin}
Scegliere `.venv` come nome della directory per l'_environment_ rappresenta un
uso consolidato, del quale tengono conto per esempio gli IDE. In teoria si può
usare un nome qualunque, ma è meglio farlo solo se sussistono motivi specifici. 
L'uso di `--prompt sds` è facoltativo, e quando questa parte di comando viene
omessa, verrà usato il nome della directory come _prompt_.
```
```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         $ python3.11 -m venv .venv --prompt sds

   .. group-tab:: Windows

      .. code-block:: powershell

         C:> python3 -m venv .venv --prompt sds

```

avendo cura di verificare preventivamente che il comando `python3.11` (in Linux
o Mac OS) o `python3` (in Windows) faccia riferimento alla versione che volete
utilizzare, e che questa versione risulti installata e accessibile.
L'esecuzione ha l'effetto di creare una directory `.venv` (che risulterà
nascosta in Linux e Mac OS), nella quale verranno copiati i file relativi agli
eseguibili e alle librerie da installare nell'ambiente virtuale. Per poter
utilizzare l'ambiente è necessario attivarlo, eseguendo il comando

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         $ source .venv/bin/activate

   .. group-tab:: Windows

      .. code-block:: powershell

         C:> .venv\Scripts\activate

```

sempre nella directory `sds` (anche se è possibile posizionarsi in un altro
punto del _file system_ e fare riferimento a un opportuno _pathname_ assoluto o
relativo per lo _script_ `activate` che è stato creato dal comando precedente).
L'attivazione ha, tra le altre cose, l'effetto di modificare il _prompt_,
aggiungendo al suo inizio la stringa `(sds)`: in questo modo viene reso
esplicito l'utilizzo di un ambiente virtuale a chi inserisce comandi nella
_shell_. Nel paragrafo che segue vedremo come installare delle librerie una
volta che l'ambiente è stato attivato. Eseguendo invece il comando

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         (sds) $ deactivate

   .. group-tab:: Windows

      .. code-block:: powershell

         (sds) C:> deactivate

```

si disattiva l'_environment_ attivato, e conseguentemente il _prompt_ di
sistema torna a essere quello originario.


(sec:lib-install)=
## Gestire le librerie
In teoria, si può installare manualmente una libreria, scaricando il
corrispondente eseguibile o partendo dal codice sorgente disponibile su fonti
pubbliche. Tuttavia, questo approccio può nascondere delle insidie: quasi ogni
libreria dipende da altre librerie. Procedere in questo modo richiede di
installare innanzitutto queste ultime librerie, che a loro volta potrebbero
dipendere da altro software, e così via. In altre parole, l'installazione
manualme di una libreria può rivelarsi un'esperienza particolarmente
impegnativa, quando non decisamente frustrante: con il crescere del numero di
installazioni necessarie, diventa più verosimile che qualche tipo di errore
complichi ulteriormente il processo, quando non lo blocchi completamente. Per
mitigare questo problema, le _best practice_ per l'installazione di una
libreria Python (ma anche per l'installazione di software in senso generale)
prevedono l'utilizzo di un _package manager_, che è uno strumento pensato per
rilevare e gestire in modo trasparente le dipendenze tra librerie. Come per gli
ambienti virtuali, esistono differenti _package manager_ associati a
Python[^package-manager]. Io farò riferimento a
[pip](https://pip.pypa.io){.external}, che è installato automaticamente insieme
alle versioni recenti di Python.

L'installazione di una libreria, che normalmente viene fatta all'interno di
un _environment_ virtuale attivato, viene fatta eseguendo il comando `pip`
in una _shell_, specificando il nome della libreria stessa&mdash;aggiungendo
eventualmente i caratteri `==` seguiti da uno specifico numero di versione. Se
volessimo per esempio installare _altair_, la libreria che ho usato nel
{ref}`sec:uno-sguardo-di-insieme` per produrre grafici interattivi, sarà
sufficiente eseguire il comando

```{margin}
Tra breve vedremo come effettuare tramite un unico comando le installazioni di
tutte le librerie che utilizzeremo; pertanto non è necessario che eseguiate
questo comando nel vostro sistema.
```
```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         $ pip install altair

   .. group-tab:: Windows

      .. code-block:: powershell

         C:> pip install altair

```

il cui effetto è quello di verificare quali siano le librerie dalle quali
_altair_ dipende, installando quelle che non sono attualmente disponibili, o
gestendo gli eventuali aggiornamenti di librerie installate la cui versione
è incompatibile, ripetendo poi il processo a ritroso per gestire tutte le
dipendenze.

Utilizzare dei _package manager_ presenta anche un ulteriore vantaggio: è
possibile distribuire un progetto software insieme a una descrizione testuale
di tutte le librerie che questo richiede, ed effettuare tutte le installazioni
relative in un colpo solo. Se si utilizza pip, questa descrizione testuale è
tipicamente inserita in un file il cui nome è `requirements.txt`, e tutte le
installazioni si possono effettuare eseguendo il comando

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         $ pip install -r requirements.txt

   .. group-tab:: Windows

      .. code-block:: powershell

         C:> pip install -r requirements.txt

```

Il [repository](https://github.com/dariomalchiodi/sds){.external} associato a
questo libro include il file `requirements.txt` che contiene tutti i
riferimenti alle librerie necessarie per poter eseguire il codice che troverete
nei vari capitoli.


(sec:notebook)=
## Installare un notebook manager

Come indicato all'inizio di questo capitolo, presenterò il codice Python in
modo da eseguirlo agevolmente all'interno di particolari file chiamati
_notebook_. Il contenuto di questi file è organizzato in _celle_, che possono
essere di tre tipi differenti:
- le celle di codice, costituite da una o più righe di codice
  eseguibile[^linguaggio-notebook],
- le celle di output, ognuna delle quali è associata a una specifica cella di
  codice, e contiene output prodotto dall'esecuzione di quest'ultima,
- le celle restanti, nelle quali si possono trovare testo formattato, grafici e
  video che possono essere stati generati dal codice eseguito nel _notebook_,
  come effetto collaterae, ma che possono anche essere stati inseriti
  direttamente da chi ha realizzato quest'ultimo.

```{margin}
Quando nel nome di una tecnologia basata su python è contenuta la sillaba «py»,
questa sillaba è normalmente pronunciata nello stesso modo della parola parola
«pie», cioè <a href="/sds/short/pie" target="_blank">ˈpī</a>. Jupyter fa
eccezione, come dichiarato dai suoi creatori[^pronuncia-jupyter], e si
pronuncia <a href="/sds/short/pee" target="_blank">ˈjü-pə-tər</a>, come il nome
inglese del pianeta Giove (Jupiter).
```
Lo standard _de facto_ per i _notebook_ è quello introdotto dal progetto
[Jupyter](https://jupyter.org). Esiste <a href="/sds/short/py-implementations"
target="_blank">una pletora di applicazioni</a> che permettono di scrivere,
leggere e soprattutto eseguire  _notebook_, e tra queste le più comunemente
utilizzate sono quella distribuita direttamente dal progetto Jupyter e l'IDE
flagship di Microsoft ([Visual Studio
Code](https://code.visualstudio.com){.external}). Se avete installato le
librerie utilizzando il file `requirements.txt` seguendo le istruzioni indicate
nei paragrafi precedenti, nell'ambiente virtuale che avete creato è già
disponibile Jupyter, e per lanciarlo è sufficiente eseguire da terminale il
comando

```{margin}
Poco più avanti trovate anche le istruzioni per visualizzare ed eseguire
un _notebook_ usando Visual Studio Code.
```
```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         (sds) $ jupyter notebook

   .. group-tab:: Windows

      .. code-block:: powershell

         (sds) C:> jupyter notebook
```

```{margin}
{margin} L’estensione .ipynb` identifica i notebook Python.
```
che ha l'effetto di aprire un browser e di collegarlo a un indirizzo locale,
sul quale è in ascolto un server web appositamente eseguito. La pagina caricata
mostrerà i file contenuti nella directory dalla quale è stato lanciato Jupyter.
Per esempio, la {numref}`jupyter-home` mostra come appare questa pagina quando
si esegue Jupyter dalla directory principale del _repository_ di questo libro.
Cliccando sulla directory _playground_ e selezionando l'unico file presente,
_first-notebook.ipynb_, viene visualizzato un semplice esempio di _notebook_,
contenente un'unica cella di codice nella quale è già presente l'espressione
`1 + 1`. Se vi posizionate nella cella e premete la combinazione di tasti
{kbd}`Shift` + {kbd}`⤶`, verrà automaticamente aggiunta una cella di output,
che conterrà il valore dell'espressione. Per creare un nuovo _notebook_ è
possibile selezionare la voce di menu _File/New/Notebook_, oppure tornare alla
vista che elenca i file, cliccare sul pulsante «New» e selezionare «Python 3
(ipykernel)». Verrà visualizzata una nuova pagina, contenente un'unica cella di
codice, vuota. Il vantaggio di usare un _notebook_ consiste in un'elevata
interattività nell'esecuzione del codice, perché i risultati dell'esecuzione di
una cella sono mantenuti in memoria per tutto il tempo nel quale il _notebook_
resta aperto, così da poter usare questi risultati come base per l'esecuzione
di altre celle.

```{figure} ../../../_static/img/jupyter-home.png
:width: 100%
:name: jupyter-home

La schermata iniziale di Jupyter, con l'elenco dei file presenti nella
directory che corrisponde al _repository_ del libro.
```

Usare un _notebook_ con le versioni recenti di Visual Studio Code è ancora più
semplice, a patto di avere installato l'omonima estensione: basta selezionare
il file corrispondente dall'IDE, e le sue celle verranno mostrate in un tab.
Anche in questo caso, è possibile aggiungere codice ed esguirlo esattamente
come nel caso di Jupyter: l'unica differenza sta nel fatto che la prima volta
che si esegue una cella potrebbe essere necessario specificare l'_environment_
di riferimento, selezionandolo da un men contestuale.

```{admonition} Avvertenza
Vi è una notevole flessibilità nel modo in cui si possono valutare le celle di
codice contenute in un _notebook_: è sufficiente posizionarsi in una di essa e
premere la combinazione {kbd}`Shift` + {kbd}`⤶`, cosa che permette di
eseguirle in un ordine qualsiasi: dalla prima all'ultima, dall'ultima alla
prima, sette volte la prima per poi passare alla terza e così via. Questo
comporta aspetti positivi quanto negativi. La flessibilità dell'esecuzione
consente un'analisi altamente interattiva: si può eseguire una parte di celle,
osservare i risultati, e decidere in base a questi come procedere. Tuttavia,
questa libertà comporta dei rischi. Non potendo imporre un ordine di
esecuzione, il risutato finale può variare, e questo limita la riproducibilità
dei risultati. Inoltre, i _notebook_ siano salvati come file di testo che
contengono un'elevata quantità di meta-informazioni, che ne complicano la
gestione con strumenti come git[^jupytext].

Va anche sottolineato che i _notebook_ sono solo uno degli strumenti che è
possibile usare per eseguire codice Python: tra quelli rimanenti, ve ne sono
due che vengono ampiamente utilizzati: il primo riguarda l'uso del cosiddetto
REPL (Read, Evaluate, Print, Loop), un ambiente semplificato che si esegue in
una _shell_ e che segue per certi versi la filosofia alla base dei _notebook_:
si inserisce un'istruzione e la si esegue, osservandone i risultati, e
successivamente è possibile eseguire una seconda istruzione e così via, ma in
questo caso per ri-eseguire un'istruzione precedentemente inserita è necessario
inserirla nuovamente a mano; il secondo è invece l'uso di un interprete Python
per eseguire un programma, in modo molto simile a quanto fatto con altri
linguaggi come Go o Java. 
```

## Primi passi con Python

Come motivato nel {ref}`sec:imparare-e-programmare`, suppongo che chi
legge questo libro abbia già imparato a usare un linguaggio di programmazione.
In questo paragrafo considererò alcuni concetti di base di programmazione,
mostrandone la sintassi in Python. Questo mi permetterà di introdurre fin da
subito esempi di codice che accompagneranno i concetti che spiegherò man mano
nel testo.

### Assegnamenti
L'assegnamento di un valore a una variabile viene fatto utilizzando la stessa
notazione che si riscontra nella maggior paerte dei linguaggi di
programmazione, utilizzando l'idioma `variabile = valore`. Nel Paragrafo
{ref}`sec:tipizzazione-dinamica` vedremo che Python non richiede la
_dichiarazione_ delle variabili: queste ultime sono create automaticamente la
prima volta che viene assegnato loro un valore, che determina implicitamente
il tipo della variabile. Per esempio

```python
age = 42
```

è un esempio di assegnamento che coinvolge un tipo intero.

### Stampare un valore
Abbiamo visto che la valutazione di una cella in un _notebook_ può produrre
un output. Tuttavia, questo modo di procedere presenta delle limitazioni: per
esempio viene visualizzatio solo il risultato dell'ultima istruzione eseguita
nella cella di input. Inoltre, questo approccio non è utilizzabile quando
scriviamo codice senza utilizzare i _notebook_. In generale, è possibile
stampare esplicitamente un valore o il contenuto di una variabile, passandoli
come argomento alla funzione `print`:

```python
print(age)
print(3.14)
```

### Esecuzione condizionata
Anche le selezioni (anche note come istruzioni condizionali) si scrivono in
Python usando una sintassi simile a quella di molti altri linguaggio, sebbene
con alcune differenze. Considerate per esempio la cella che segue:

```python
if age >= 18:
  print('È maggiorenne, ha', age, 'anni.')
else:
  print('È minorenne.')
```

```{margin}
L'indentazione può essere fatta usando un numero qualsiasi di spazi o di
tabulazioni, a condizione di non mescolarli e di mantenere la scelta effettuata
per tutto il blocco di codice. Esistono argomentazioni sia a favore degli spazi
che delle tabulazioni, così come critiche per entrambi. È una questione che
divide profondamente gli sviluppatori&mdash;una vera e propria guerra di
preferenze. Personalmente, non intendo schierarmi: usate quella che
preferite (quando ve lo potete permettere: a volte la scelta è imposta
dall’ambiente di lavoro), ma siate coerenti.
```
La selezione è fatta utilizzando l'istruzione `if`, seguita da una condizione e
terminata da un carattere di due punti (`:`). Il blocco di codice da eseguire
se la condizione è vera è indentato. La parola chiave `else` permette di
specificare un blocco da eseguire in caso contrario, usando la stessa
sintassi[^one-liner]. Notate che l'esempio precedente mette in luce che:

- non è necessario racchiudere la condizione tra parentesi tonde,
- la funzione `print` permette di stampare dei messaggi sotto forma di una
  stringa prefissata, che in questo caso è stata delimitata da due caratteri di
  apice singolo,
- `print` accetta una sequenza di argomenti da stampare, separandoli
   automaticamente con degli spazi.

### Scrivere funzioni
La cella seguente mostra come definire una funzione che accetta un argomento,
che interpreta come l'età di una persona, stampa un messaggio e restituisce
un valore booleano che indica se la persona è maggiorenne:

```{margin}
Notate che l'esecuzione ha prodotto due celle, i cui ruoli sono
fondamentalmente diversi: la prima contiene il testo prodotto da `print`, la
il valore restituito da `check_age`. In generale, mescolare standard output e
valori restituiti __non__ è una buona pratica di programmazione[^bad-practice];
in questo caso, tuttavia, lo faccio per introdurre più concetti importanti con
un singolo esempio.
```

```python
def check_age(age):
  if age >= 18:
    print('È maggiorenne, ha', age, 'anni.')
    return True
  else:
    print('È minorenne.')
    return False

check_age(age)
```

Questo esempio ci permette di osservare che

- la definizione di una funzione viene fatta dall'istruzione `def`,
  seguita dal nome della funzione e dagli argomenti racchiusi tra parentesi
  tonde, terminando con un carattere di due punti;
- non si indicano i tipi degli argomenti, né del valore restituito, per via
  della tipizzazione dinamica;
- il corpo della funzione è indentato rispetto alla definizione, e i blocchi
  per `if` ed `else` sono ulteriormente indentati;
- l'istruzione `return` determina il termine dell'esecuzione della funzione e
  specifica il valore da restituire,
- le costanti `True` e `False` rappresentano i due valori booleani.

Chiaramente, il vantaggio di una funzione è quello di poterla invocare
più volte, passando diversi argomenti, come nell'esempio che segue:

```python
check_age(13)
```

### Importare moduli
Il meccanismo con cui in Python si organizzano progetti software complessi e si
riutilizza il codice è basato sul concetto di _modulo_. In pratica un modulo è
un file che contiene la definizione di una o più variabili, funzioni o classi.
L'importazione può riguardare un intero modulo oppure solo uno (o alcuni) dei
suoi elementi. Tramite i moduli è inoltre possibile utilizzare librerie
standard o sviluppate da terze parti. Consideriamo per esempio il modulo
`math`, che definisce, tra gli altri, la variabile `pi` che contiene
un'approssimazione di $\pi$ e la funzione `factorial` che restituisce il
fattoriale di un intero. Questi due elementi possono essere _importati_ in
modo da utilizzarli nel codice, esattamente come se li avessimo definiti noi,
usando la sintassi `from <module> import <name>`:
```{margin}
Va notato come sia possibile usare `import` per importare più elementi da un
medesimo modulo utilizzando una sola istruzione.
```

```python
from math import factorial, pi

print(pi)
print(factorial(10))
```

Quando è necessario importare molti elementi da uno o più moduli, potrebbe
capitare che due o più elementi in moduli diversi abbiano lo stesso nome. In
casi come questi, per evitare degli adombramenti (cioè conflitti tra i nomi)
è opportuno utilizzare i cosiddetti _namespace_: si importa l'intero modulo,
usando l'istruzione `import <module>`, e si accede poi ai suoi generici
elementi usando una variante della _dot notation_: si scrive il nome del
modulo, seguito da un punto e dal nome dell'elemento in questione.

```python
import math

print(math.pi)
print(math.factorial(10))
```

In casi come questo, se due moduli `m1` e `m2` dovessero entrambi contenere un
elemento `e`, non può avvenire alcun adombramento, perché per riferirsi ad
esso si utilizzerebbero le denominazioni differenti `m1.e` e `m2.e`.

Indicare il nome di un modulo per accedere ai suoi elementi ha spesso l'effetto
di allungare il codice, diminuendone al contempo la leggibilità. È per questo
motivo che è possibile importare un modulo specificando un nome alternativo,
più corto detto _alias_, usando la sintassi `import <modulo> as <alias>`. Userò
questo approccio per le librerie che utilizzo più frequentemente nel libro, che
sono [numpy](http://www.numpy.org){.external},
[pandas](http://pandas.pydata.org){.external} e
[matplotlib](http://matplotlib.org){.external}, che permettono di lavorare
rispettivamente con gli _array_, i _dataset_ e i grafici. Farò sempre
l'importazione nel modo seguente:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
```{margin}
Come mostrato nella terza riga, alcuni moduli (come matplotlib) sono
organizzati in strutture gerarchiche chiamate _package_, in modo non dissimile
a quanto avviene per esempio in Java.
```

```{admonition} Nomenclatura
:class: naming
Questo modo di importare numpy, pandas e il modulo `pyplot` di matplotlib
usando gli _alias_ `np`, `pd` e `plt` fa riferimento a una convenzione
universalmente accettata tra gli sviluppatori. È consigliabile mantenere sempre
questa convenzione, così che chi legge il codice possa capire a colpo d'occhio
a quale modulo si fa riferimento.
```

### Errori ed eccezioni
Python gestisce le situazioni di errore emettendo delle _eccezioni_ in modo
non dissimile, per esempio, da Java. Nell'esempio seguente si può vedere in
che modo viene notificata all'utente un'eccezione di tipo `NameError`, dovuta
al riferimento a una variabile che non è mai stata inizializzata:

```python
print(uninitialized_variable)
```

Un aspetto importante delle eccezioni è rappresentato dal fatto che normalmente
l'emissione di un'eccezione causa l'arresto del programma (o della valutazione
di una cella in un _notebook_), ma il programmatore può scrivere del codice che
sarà eseguito automaticamente ogni volta che si verifica una specifica
eccezione all'interno di un dato blocco di codice. Per approfondire questo
argomento, che non tratterò nel libro, è possibile per esempio fare riferimento
alla [documentazione
ufficiale](https://docs.python.org/3/tutorial/errors.html){.external}. Detto
questo, esistono delle particolari situazioni di errore che non sono gestibili
usando le eccezioni: un classico esempio è quello degli errori di sintassi, che
vengono emessi quando il _parser_ che analizza il codice sorgente non è in
grado di riconoscere una riga del programma.

## Esercizi


[^compilatori]: Una domanda che ricorre spesso è quella che chiede se Python
sia un linguaggio interpretato oppure compilato. Anche questo è un aspetto che
dipende dalla particolare implementazione utilizzata, sebbene quasi sempre la
risposta alla domanda è: «né l'uno, né l'altro», perché normalmente l'approccio
utilizzato per trasformare il sorgente in codice eseguibile è basato su una
compilazione intermedia in _bytecode_. Esattamente come avviene con Java, questo
_bytecode_ è l'equivalente del codice binario, ma per una _macchina virtuale_.
Uno specifico software provvede poi a eseguirlo, trasformandolo a sua volta nel
codice macchina dello specifico computer utilizzato. Quando si utilizza
CPython, l'implementazione di Python alla quale faccio qui riferimento, il
processo di compilazione è trasparente, e avviene in modo automatico solo
quando vengono importati dei moduli (vedi il {ref}`sec:importare-moduli`): in
questo caso, il risultato della compilazione sono file dall'estensione `.pyc`
salvati in una directory `__pycache__`, che vengono creati solo se non esistono
o se sono meno recenti del relativo sorgente; negli altri casi, il _bytecode_
già esistente viene direttamente eseguito.
[^environment]: In realtà esistono alcune alternative per creare e utilizzare
ambienti virtuali: al momento nel quale scrivo,
[Anaconda](https://docs.anaconda.com/anaconda/){.external} e
[Miniconda](https://docs.anaconda.com/miniconda/){.external} rappresentano
quelle più utilizzate insieme a `venv`.
[^package-manager]: Anaconda e miniconda, citati nella nota
precedente, mettono a disposizione anche i relativi _package
manager_, che possono essere utilizzati al posto di pip.
[^linguaggio-notebook]: Va notato che i _notebook_ non sono vincolati a un
particolare linguaggio di programmazione. I _notebook manager_ permettono
l'installazione di uno o più _kernel_, moduli dedicati a specifici linguaggi di
programmazione. Io lavorerò quasi esclusivamente con codice Python, ma
occasionalmente vedremo come lanciare dei comandi di _shell_ senza dover aprire
un terminale dedicato.
[^pronuncia-jupyter]: Fernando Perez, uno degli artefici del progetto Jupyter,
lo pronuncia in questo modo, per esempio, in una sua
[presentazione](https://www.youtube.com/watch?v=cc2hHjARNTY){.external} alla
conferenza PLOTCON 2016.
[^jupytext]: Per questo motivo, inserire dei _notebook_ all'interno di un
_repository_ git è sconsigliato. Piuttosto, si possono usare tencologie come
[jupytext](https://jupytext.readthedocs.io/){.external} che sincronizzano
automaticamente i _notebook_ con del codice Python equivalente, e provvedono a
versionare quest'ultimo.
[^one-liner]: In realtà è possibile usare una sintassi che permette di scrivere
una selezione su di una sola riga, ma sconsiglio di utilizzarla, perché
diminuisce la leggibilità del codice.
[^bad-practice]: In linea di principio, una funzione non dovrebbe produrre
stampe a schermo, a meno che non si tratti di emissione di _warning_ o di
errori. Anche in questi casi, è tuttavia preferibile utilizzare le funzionalità
specifiche del linguaggio, come il _logging_ o le eccezioni, piuttosto che
ricorrere a `print`. Questo approccio aiuta a non confondere chi osserva
l'esecuzione del programma, distinguendo chiaramente tra messaggi e valori
restituiti, oltre a semplificare il processo di verifica del software.