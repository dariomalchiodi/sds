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
numbering:
  heading_1: true
  heading_2: false
  enumerator: 2.1.%s

title: 2.1. Installazione e configurazione 
---

```{admonition}
Questo paragrafo descrive come installare Python e le librerie alle quali
farò riferimento nel libro. Chi ha già dimestichezza con questo linguaggio
e ha a disposizione un'installazione funzionante può probabilmente saltare
direttamente al paragrafo successivo, sebbene anche in questo caso consiglio
una rapida lettura, per sincerarsi che non vi siano problemi di
incompatibilità della versione già disponibile e che tutte le librerie
necessarie siano già installate.
```

## Installare Python

L'installazione di Python è fortemente dipendente dal sistema operativo
utilizzato. Le distribuzioni recenti di Linux e di Mac OS sono già equipaggiate
con Python: per verificare che sia così, è possibile lanciare un terminale ed
eseguire il comando

    $ python --version

e notando che tipo di output si ottiene. Sono possibili tre casi:

1. l'esecuzione ha come effetto quello di stampare a video la stringa
   `Python 3.YY.ZZ`, a indicare che è disponibile la _major release_ 3 di
   Python, e `YY` e `ZZ` indicano i rispettivi numeri di _minor release_ e di
   _patch_;
2. viene stampata una sigla simile, ma la major release è `1` oppure `2`,
   a indicare che è disponibile una versione di Python, ma questa
   è troppo vecchia per eseguire gran parte del codice di questo libro: al
   momento in cui sto scrivendo questo paragrafo, è distribuita la versione
   3.12.5 di Python, che è quella alla quale farò riferimento;
```{margin}
Se la _major release_ è `4` o superiore, allora state leggendo questo libro
parecchio tempo dopo che l'ho scritto, ed è fortemente probabile che una
parte più o meno grande dei contenuti che riguardnao l'uso di Python sia
diventata obsoleta. In questo caso, controllate se non esiste un aggiornamento
del libro, e in caso negativo cercate della documentazione più aggiornata.
``` 
3. si ottiene un errore che indica che `python` non è tra i comandi disponibili:
   questo è indice del fatto che probabilmente non è installata alcuna versione
   di Python.

Nella prima ipotesi, molto probabilmente è possibile utilizzare la versione
di Python già installata per eseguire tutto il codice contenuto in questo
libro. Vale però la pena sincerarsi del fatto che la versione installata sia
il più possibile allineata a quella che ho usato io. Al momento in cui scrivo,
è distribuita la versione 3.12.5. Se il numero di versione è sensibilmente
inferiore o molto superiore, potrebbero verificarsi dei problemi di
compatibilità: se ciò dovesse succedere, sarà necessario installare la versione 
alla quale faccio riferimento, affiancandola a quella già presente.
```{margin}
In teoria è possibile rimpiazzare la versione di Python già presente, ma ciò
espone al rischio che altro software basato su di essa smetta di funzionare
correttamente. Pertanto sconsiglio di procedere in tal senso.
```

Nel secondo caso, potrebbe comunque esistere un'installazione del
linguaggio in una versione compatibile, ma il comando `python` fa riferimento
a un'altra versione. Per sincerarsene, è possibile scrivere `python`
nel terminale e (senza aggiungere alcuno spazio) premere il tasto {kbd}`TAB`:
in presenza di più installazioni, il nome dei corrispondenti comandi viene 
automaticamente stampato. Anche nel terzo caso, Python potrebbe essere
installato senza che il vostro terminale risulti configurato per eseguirlo, ma
si tratta di un'eventualità abbastanza remota.
```{margin}
Normalmente, per ogni versione installata è disponibile un comando, e il
nome corrispondente di questo comando è `pythonX.YY`, dove `X` e `YY`
corrispondono ai numeri di _major_ e _minor release_. Il comando `python` è un
_alias_ a uno di questi comandi, tipicamente alla versione che viene
maggiormente utilizzata.
```

Se dovesse risultare necessario installare Python, è possibile fare riferimento
alla documentazione ufficiale, che prevede guide separate per sistemi basati su
[Unix (come Linux)](https://docs.python.org/3/using/unix.html),
[Mac OS](https://docs.python.org/3/using/mac.html) e
[Windows](https://docs.python.org/3/using/windows.html).


## Creare un ambiente virtuale di esecuzione

Python viene normalmente utilizzato insieme a varie librerie, ed è
decisamente sconsigliabile installarle adottando un approccio _monolitico_,
nel quale semplicemente si aggiunge una libreria ogni volta che ci si rende
conto di averne bisogno: man mano che il tempo passa, e che il numero di
librerie utilizzate aumenta, cresce anche il rischio di incompatibilità tra
il sistema esistente e una nuova libreria della quale potreste avere bisogno.
Considerazioni analoghe si possono fare nel momento in cui una o più librerie
vengono aggiornate a una versione più recente.
Per aggirare questo tipo di rischi, è altamente consigliabile compartimentare
l'installazione delle librerie: eseguire cioè Python in uno spazio logicamente
isolato nel quale aggiungere tutte e sole le librerie necessarie per uno
specifico progetto software. Questi spazi isolati prendono il nome di
_environment virtuali_, o _ambienti virtuali di esecuzione_ (nel seguito
parlerò per brevita di _environment_ o di ambienti virtuali), e vengono
opportunamente attivati ogni volta che si inizia a lavorare sul corrispondente
progetto, disattivandoli prima di passare a un altro progetto.

Esistono diverse implementazioni del concetto di _environment_ virtuale in
Linux: in questo libro farò riferimento a _venv_[^environment], che è
automaticamente installato insieme alle versioni recenti di Python. Per creare
un ambiente virtuale si procede usualmente nel modo che segue: usando un
terminale, ci si posiziona nella directory principale del progetto e si
esegue il comando

```bash
$ python -m venv .venv
``` 

avendo cura di verificare preventivamente che il comando `python` faccia
riferimento alla versione corretta. L'esecuzione ha l'effetto di creare una
sotto-directory `.venv` (che sarà quindi nascosta), nella quale verranno
copiati i file relativi alle librerie da installare nell'ambiente virtuale.
L'ambiente non risulta però automaticamente attivato: per farlo è necessario
eseguire il comando
```{margin}
Se fosse necessario creare un ambiente virtuale che utilizza una versione di
Python diversa da quella individuata dal comando `python`, è sufficiente
utilizzare il comando che fa riferimento in modo esplicito alla versione
richiesta.
```
```bash
$ source .venv/bin/activate
```

sempre nella directory principale del progetto (anche se è possibile
posizionarsi in un altro punto del _file system_ e fare riferimento a un
opportuno _pathname_ assoluto o relativo per lo _script_ `activate` che è stato
creato dal comando precedente). L'attivazione ha, tra le altre cose, l'effetto
di modificare il _prompt_, aggiungendovi la stringa `(.venv)`: in questo
modo viene reso esplicito l'utilizzo di un ambiente virtuale a chi utilizza
il terminale.
```{margin}
In realtà è possibile modificare sia il nome e la posizione della directory
da creare per l'_environment_, sia la stringa visualizzata quando questo viene
attivato, modificando gli argomenti del comando utilizzato per crearlo.
```

Nel paragrafo che segue vedremo come installare delle librerie una volta che
l'ambiente è stato attivato. Eseguendo invece il comando

```bash
(.venv) $ deactivate
```

si disattiva l'_environment_ attivato, e conseguentemente il _prompt_ di
sistema torna a essere quello originario.

## Gestire le librerie
In teoria l'installazione di una libreria può essere fatta in modo
autonomo, scaricando ed eseguendo il corrispondente eseguibile, o perfino
a partire dal relativo codice sorgente scaricabile da fonti pubbliche. Questo
modo di procedere può però nascondere delle insidie, e quella che classicamente
si verifica è legata al fatto che quasi tutte le librerie sono state
realizzate utilizzando _altre_ librerie, e dunque è necessario installare
preventivamente queste ultime. Chiaramente, anche queste installazioni
preventive dipenderanno verosimilmente da altre librerie ancora, che dovranno
essere installate prima di procedere, e così via. In altre parole, procedere
in modo manuale all'installazione di una libreria può rivelarsi un'esperienza
particolarmente impegnativa, se non stressante (con il crescere del numero di
installazioni necessarie diventa più verosimile che intervenga qualche tipo di
errore che complichi ulteriormente il processo). Per mitigare questo problema,
le _best practice_ per l'installazione di una libreria Python (ma anche per
l'installazione di software in generale) prevedono l'utilizzo di un _package
manager_, che è uno strumento pensato per rilevare e gestire in modo
trasparente le dipendenze tra librerie. Come per la gestione degli ambienti
virtuali, esistono differenti _package manager_ associati a
Python[^package-manager]. Io farò riferimento a [pip](https://pip.pypa.io),
che è installato automaticamente insieme alle versioni recenti di Python.

L'installazione di una libreria, che normalmente viene fatta all'interno di
un _environment_ virtuale attivato, viene fatta eseguendo il comando `pip`
in un terminale, specificando il nome della libreria stessa&mdash;aggiungendo
eventualmente i caratteri `==` seguiti da uno specifico numero di versione
della libreria. Se volessimo per esempio installare _altair_, la libreria che
ho usato nel Paragrafo [Uno sguardo di insieme](uno-sguardo-di-insieme) per
produrre grafici interattivi, sarà sufficiente eseguire il comando

```bash
(.venv) $ pip install altair
```
```{margin}
Sconsiglio di eseguire questo comando, perché tra breve vedremo come effettuare
simultaneamente le installazioni di più librerie.
```

il cui effetto è quello di verificare quali siano le librerie dalle quali
_altair_ dipende, installando quelle che non sono attualmente disponibili, o
gestendo gli eventuali aggiornamenti di librerie installate la cui versione
è incompatibile, ripetendo il processo a ritroso per gestire tutte le
dipendenze.

Utilizzare dei _package manager_ presenta anche un ulteriore vantaggio: è
possibile distribuire un progetto software insieme a una descrizione testuale
di tutte le librerie che questo richiede, ed effettuare tutte le installazioni
relative in un colpo solo. Se si utilizza pip, questa descrizione testuale è
tipicamente inserita in un file il cui nome è `requirements.txt`, e tutte le
installazioni si possono effettuare eseguendo il comando

```bash
(.venv) $ pip install -r requirements.txt
```

Il [repository](https://github.com/dariomalchiodi/sds) associato a questo
libro include il file `requirements.txt` che contiene tutti i riferimenti
alle librerie necessarie per poter eseguire il codice che troverete nei vari
capitoli.


## Installare un notebook manager

Come indicato all'inizio di questo capitolo, presenterò il codice Python in
modo da eseguirlo agevolmente all'interno di particolari file chiamati
_notebook_. Il contenuto di questi file è organizzato in _celle_, che possono
essere di tre tipi differenti:
- le celle di codice, costituite da una o più righe di codice
  eseguibile[^linguaggio-notebook],
- le celle di output, ognuna delle quali è associata a una specifica cella di
  codice, e contiene l'output prodotto dall'esecuzione di quest'ultima,
- le celle restanti, nelle quali si trova testo formattato, grafici e
  video che non sono generati dal codice eseguito nel notebook, bensì sono
  stati inseriti direttamente da chi ha scritto il notebook.

Lo standard _de facto_ per i _notebook_ è quello introdotto dal progetto
[Jupyter](https://jupyter.org). Esiste una pletora di applicazioni che
permettono di scrivere, leggere e soprattutto eseguire __notebook_, e tra
queste le più comunemente utilizzate sono quella distribuita direttamente
dal progetto Jupyter e l'IDE flagship di Microsoft (Visual Studio Code).
```{margin}
Quando nel nome di una tecnologia basata su python è contenuta la sillaba «py»,
questa sillaba è normalmente pronunciata nello stesso modo della parola
inglese "pie", cioè [ˈpī](https://www.merriam-webster.com/dictionary/pie?pronunciation&lang=en_us&dir=p&file=pie00001).
Jupyter fa eccezione, come dichiarato dai suoi creatori[^pronuncia-jupyter],
e si pronuncia [ˈjü-pə-tər](https://www.merriam-webster.com/dictionary/Jupiter?pronunciation&lang=en_us&dir=gg&file=ggjupi01),
come il pianeta "Jupiter".
```


[^environment]: In realtà esistono alcune alternative per creare e
utilizzare ambienti virtuali: al momento nel quale scrivo,
[Anaconda](https://docs.anaconda.com/anaconda/) e
[Miniconda](https://docs.anaconda.com/miniconda/) rappresentano quelle più
utilizzate insieme a `venv`.
[^package-manager]: Anaconda e miniconda, citati nella nota
precedente[^environment], mettono a disposizione anche i relativi _package
manager_, che possono essere utilizzati al posto di pip.
[^linguaggio-notebook]: Va notato che i _notebook_ che useremo non sono
vincolati a un particolare linguaggio di programmazione: noi li utilizzeremo
per eseguire quasi esclusivamente codice Python, ma occasionalmente vedremo
come lanciare dei comandi di _shell_ senza dover aprire un terminale.
[^pronuncia-jupyter]: Fernando Perez, uno degli artefici del progetto Jupyter,
lo pronuncia in questo modo, per esempio, in una sua
[presentazione](https://www.youtube.com/watch?v=cc2hHjARNTY) alla conferenza
PLOTCON 2016.