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

  figure:
    template: Figura 1.%s
  table:
    template: Tabella 1.%s

title: 1.3. Uno sguardo d'insieme
---

Lo scopo di questo paragrafo è duplice: da una parte, serve a descrivere per
sommi capi il filo logico che è dietro all'organizzazione dei contenuti e
a introdurre, in modo relativamente informale, i concetti cardine; dall'altra,
spiega come utilizzare le componenti interattive del libro.
Come indicato nel Paragrafo [Approccio](approccio), nel testo farò riferimento a un
_dataset_ ottenuto modificando un opportuno sottoinsieme del
[Superhero database](http://www.superherodb.com). Gli esempi faranno quindi
riferimento al mondo dei supereroi, ognuno dei quali sarà descritto tramite
gli _attributi_ indicati nella {numref}`tab:dataset`.

```{table} Descrizione del _dataset_ utilizzato negli esempi
:name: tab:dataset
:align: center
| Attributo          | Significato               | Contenuto                                                |
|--------------------|---------------------------|----------------------------------------------------------|
| `name`             | Identificativo univoco    | stringa                                                  |
| `full_name`        | Nome completo             | stringa                                                  |
| `identity`         | Identità segreta          | stringa                                                  |
| `alignment`        | Inclinazione morale       | `'Good'`, `'Neutral'` o `'Bad'`                          |
| `place_of_birth`   | Luogo di nascita          | stringa                                                  |
| `creator`          | Editore/creatore          | stringa                                                  |
| `universe`         | Universo                  | stringa                                                  |
| `first_appearance` | Anno di prima apparizione | numero intero                                            |
| `eye_color`        | Colore degli occhi        | stringa                                                  |
| `hair_color`       | Colore dei capelli        | stringa                                                  |
| `height`           | Altezza in cm.            | numero in virgola mobile                                 |
| `weight`           | Peso  in kg.              | numero in virgola mobile                                 |
| `strength`         | Forza                     | numero intero (da `0` a `100`)                           |
| `intelligence`     | Intelligenza              | `'Low'`, `'Moderate'`, `'Average'`, `'Good'`, o `'High'` |
| `speed`            | Velocità                  | numero intero (da `0` a `100`)                           |
| `durability`       | Resistenza                | numero intero (da `0` a `100`)                           |
| `combat`           | Abilità nel combattimento | numero intero (da `0` a `100`)                           |
| `powers`           | Elenco dei superpoteri    | stringa                                                  |
```
```{margin}
Ho scelto di utilizzare la lingua inglese per indicare i nomi degli attributi
e i valori corrispondenti (quando questi sono descritti tramite stringhe),
per coerenza rispetto ai contenuti del dataset. Analogamente, il codice Python
sarà strutturato utilizzando nomi in inglese per variabili, funzioni e così via.
```

Il _dataset_ è memorizzato nel file `heroes.csv` contenuto nella directory
`data` del [repository](https://github.com/dariomalchiodi/sds) associato al
libro. In questo file, i contenuti sono rappresentati utilizzando il formato
CSV (_comma separated values_): ogni riga rappresenta un supereroe, in cui i
valori degli attributi nella {numref}`tab:dataset` sono indicati separandoli
tramite virgole. L'unica eccezione è costituita dalla prima riga del file, che
contiene i nomi degli attributi, sempre separati usando le virgole, come si può
vedere visualizzando la parte iniziale del file stesso.
```{margin}
Il formato CSV è uno standard altamente utilizzato per condividere dati
di dimensioni relativamente contenute.
```

```{margin}
Le righe di codice precedute dal punto esclamativo indicano dei comandi di
_shell_.
```
```{code-cell} ipython3
!head data/heroes.csv
```

Nel Capitolo [Pandas](pandas) vedremo come caricare in memoria i contenuti di
questo file e, soprattutto, come elaborarli. Per ora, concentriamoci su
alcuni semplici esempi che, da una parte, mostrano come utilizzare le parti
interattive del libro, e, dall'altra, forniscono una panoramica di quelli che
saranno i concetti spiegati nel libro.

Quello che segue è un primo esempio di grafico interattivo. Nel diagramma in
alto sono rappresentati alcuni supereroi utilizzando dei cerchi in un
piano cartesiano, usando peso e altezza rispettivamente come ascissa e ordinata
del centro, e forza come raggio. Ogni cerchio è colorato in funzione
dell'editore del supereroe, e posizionandosi sopra di esso viene visualizzato
il nome corrispondente. Il secondo diagramma (in basso) mostra il numero di
supereroi per ogni editore/creatore, usando delle barre orizzontali.
Selezionando un'area rettangolare nel diagramma in alto è possibile concentrarsi
su un sottoinsieme di supereroi (i cerchi relativi a quelli esclusi vengono
automaticamente colorati in grigio): in modo automatico, il diagramma inferiore
viene rigenerato in modo da riflettere la distribuzione dei soli supereroi
selezionati. Una volta effettuata, la selezione può essere spostata, e cliccando
in un punto qualsiasi al di fuori di essa viene ripristinato il grafico
originale.
```{margin}
Il grafico qui sotto è stato realizzato utilizzando
[altair](https://altair-viz.github.io/), una libreria che permette di
utilizzare Python per visualizzare all'interno di pagine web grafici complessi 
a partire da _dataset_ di dimensioni ridotte, in una forma interattiva che è
automaticamente attivata nel momento in cui queste pagine sono caricate. Per
riconoscere se un grafico è stato generato tramite altair, è sufficiente
controllare se nella sua parte in alto a destra è presente un pulsante rotondo
che contiene tre punti. Questo pulsante attiva un menu che permette, tra le
altre cose, di scaricare il grafico.
```

```{code-cell} ipython3
:tags: [remove-input]

import altair as alt
import pandas as pd
import numpy as np

heroes = pd.read_csv('data/heroes.csv', index_col=0).convert_dtypes()
filter = (heroes['creator'].isin(heroes.creator.value_counts()[:15].index))
filter &= (heroes['weight']<200)
filter &= (heroes['height']<250)
source = heroes[filter]
source = heroes[filter].sample(1500)
brush = alt.selection_interval()
points = alt.Chart(source).mark_point().encode(
    alt.X('weight', title='Weight'),
    alt.Y('height', title='Height'),
    alt.Size('strength', title='Strength'),
    color=alt.condition(brush, 'creator', alt.value('lightgray')),
    tooltip='name'
).add_params(brush)

bars = alt.Chart(source).mark_bar().encode(
    alt.Y('creator', title='Creator'),
    alt.X('count(creator)', title='N. of superheroes'),
    alt.Color('creator', title='Creator'),
).transform_filter(brush)

points & bars
```

Interagendo con questo grafico è possibile _esplorare_ i dati visualizzati, per
esempio per rispondere alle domande seguenti.

1. Qual è l'editore/creatore con più supereroi in assoluto?
2. Quale editore ha il maggior numero di supereroi alti meno di un metro?
3. Quale editore ha il maggior numero di supereroi che pesano tra 80 e 100 kg.?
4. Qual è il supererore più alto in assoluto?

Ci sono ovviamente tanti aspetti dei dati che possono essere analizzati in
prima battuta semplicemente guardando il grafico, come per esempio i due
indicati qui sotto.
```{margin}
In generale, solo una piccola parte dei grafici che vedremo saranno
interattivi.
```
(pt:relation-general)=
5. Esiste una relazione di qualche tipo che lega tendenzialmente il peso e
   l'altezza dei supereroi?
(pt:relation-particular)=
6. Questa relazione cambia se ci concentriamo sui supereroi che corrispondono
   a un particolare editore/creatore?

La _statistica descrittiva_, introdotta nei Capitoli da @cap:dati-e-informazione
a @cap:analizzare-le-relazioni-tra-i-dati, fornisce degli strumenti che
permettono di rispondere a domande come quelle appena considerate. In generale,
lo scopo è quello di estrarre informazioni da un _dataset_ che descrive,
globalmente o parzialmente, un insieme di individui di riferimento, e le
tecniche utilizzate possono avere una natura sia _qualitativa_, sia
_quantitativa_. Si parla di analisi qualitativa quando lo scopo è quello di
determinare la natura di un certo fenomeno (per esempio, per rispondere alle
domande ai punti {numref}`5 <pt:relation-general>` o
{numref}`6 <pt:relation-particular>` nell'elenco qui sopra). Questo richiede
spesso di utilizzare degli strumenti, come il grafico precedentemente
visualizzato, i cui risultati devono essere interpretati, introducendo un certo
grado di soggettività. Si parla invece di analisi quantitativa quando l'esito
di quest'ultima è espresso da una o più quantità numeriche, che possono essere
quindi messe a confronto in modo oggettivo con altre quantità (tipicamente,
i risultati di altre analisi).
```{margin}
Se tutto questo suona complicato, non vi preoccupate: i concetti diventeranno
più chiari nei capitoli successivi.
```

Supponiamo ora di volerci concentrare, per semplicità, sul peso dei
supereroi: il grafico precedente è decisamente sovraffollato di cerchi, e
mentre è relativamente facile farsi un'idea dell'altezza più piccola e di
quella più grande, diventa poco chiaro, per esempio, capire se ci sono più
supereroi «leggeri» che «pesanti». Per capire meglio, generiamo un particolare
grafico chiamato _istogramma_ che evidenzia le frequenze con le quali i valori
diversi del peso sono presenti nel nostro dataset. La @fig:histogram mostra il
risultato ottenuto.

````{figure}
:name: fig:histogram

```{code-cell} ipython3
:tags: [remove-input]

import matplotlib.pyplot as plt
import pandas as pd

import pyodide_http

pyodide_http.patch_all()

source = 'https://raw.githubusercontent.com/dariomalchiodi/' + \
         'sds/main/content/data/heroes.csv'

heroes = pd.read_csv(source, index_col=0)
data = heroes.weight[heroes.weight < 200]

plt.hist(data, bins=25, density=True, color='tab:blue')
plt.show()
```

Istogramma del peso di un insieme di supereroi: in ogni rettangolo, la base
individua un intervallo di valori per il peso, mentre l'area è legata al
numero totale di supereroi il cui peso è contenuto nell'intervallo.
````
```{margin}
Non sempre ha senso utilizzare un istogramma per esplorare dei valori in un
_dataset_, come vedremo nel Capitolo @cap:dati-e-informazione.
```

Gli istogrammi sono definiti in dettaglio nel Paragrafo @istogrammi, ma per il
momento ci basta sapere come leggere il risultato ottenuto: in ognuno dei
rettangoli mostrati, la base individua un intervallo $I$ di possibili valori
per il peso dei supereroi, e l'altezza indica quanti supereroi hanno un peso
contenuto in $I$ [^histogram]. Il grafico ottenuto mette in evidenza alcune
cose interessanti: per esempio si vede che i supereroi con un peso
superiore a 125 kg. sono presenti in numero maggiore rispetto a quelli con un
peso inferiore a quaranta chili. D'altro canto, se non consideriamo i pesi
molto grandi o molto piccoli, emerge un'approssimativa simmetria nei valori
rispetto a un asse centrale, unitamente al fatto che le altezze dei rettangoli
tendono a crescere, approssimativamente fino ai $70$ kg, per poi diminuire.
Anche questa è un'esplorazione dei dati, che in questo caso non richiede
l'utilizzo di grafici interattivi. Vedremo altresì che il processo di
esplorazione non deve necessariamente (o esclusivamente) coinvolgere l'uso
di metodi grafici, ma può essere basato anche sull'utilizzo di strumenti
quantitativi (e tipicamente lo è).
```{margin}
Se siete attenti avrete notato che l'altezza di un rettangolo non può essere
uguale al numero di supereroi che hanno un certo peso, perché i valori mostrati
sull'asse delle ascisse non sono numeri interi. In questo istogramma, infatti,
il numero di supereroi è legato all'_area_ del rettangolo, cosa che ci
permetterà tra poco di confrontare il risultato ottenuto con un altro grafico.
Il motivo di questa scelta è approfondito nel Paragrafo @istogrammi.
```

Una volta accumulata conoscenza sui dati a disposizione, il passo successivo
richiede normalmente di _modellare_ il processo che li ha generati, e questo
richiede di cambiare in modo radicale la nostra prospettiva, immaginando non
in termini dell'intero _dataset_, ma piuttosto ponendoci domande relative
all'osservazione di uno qualsiasi dei suoi elementi, o di un insieme di
elementi, nell'ipotesi di non sapere a priori che cosa osserveremo (ricordatevi
della [Legge di Franklin](#par:franklin-law)), ma assumendo che ogni elemento
abbia la stessa possibilità di tutti gli altri di essere osservato. I capitoli
da @cap:calcolo-combinatorio a @cap:va-e-modelli-continui affrontano il
_Calcolo delle Probabilità_, fornendo alcuni strumenti di base per gestire
l'incertezza dovuta al non conoscere quale sarà l'elemento che di volta in
volta verrà osservato. Più precisamente, ci concentreremo su delle affermazioni
che riguardano questo elemento, che chiameremo _eventi_. Tornando ai supereroi,
sono ad esempio eventi le seguenti affermazioni:

1. un supereroe è cattivo;
(par:faster-hero)=
2. un supereroe Marvel è più veloce di un supereroe DC;
(par:same-intelligence)=
3. due supereroi apparsi per la prima volta nello stesso anno hanno lo stesso
   indice di intelligenza;
(par:ten-heroes)=
4. almeno un supereroe in un gruppo di dieci è collocato in uno degli
   universi di _Star Wars_.

Chiaramente, non è noto a priori se l'affermazione che costituisce un evento
è vera o falsa, perché il valore di verità dipende da quella che sarà
l'effettiva osservazione. Per questo motivo, viene introdotto il concetto
cardine di _probabilità_, intesa come quantificazione numerica di questa
incertezza utilizzando un numero $p \in [0, 1]$. Senza entrare per ora nei
dettagli, più tale numero è prossimo a $\frac{1}{2}$ e più l'incertezza è
elevata; dualmente, quanto più $p$ si avvicina agli estremi, tanto più si
riduce questa incertezza: quando $p$ si avvicina a zero oppure a uno, aumenta
rispettivamente la confidenza che l'affermazione sia falsa oppure vera, al
punto che l'affermazione risulta essere sicuramente falsa quando la probabilità
è nulla e sicuramente vera quando la probabilità è uguale a $1$.
Se la probabilità diventa uguale a uno di questi valori estremi
Vedremo come il vantaggio di formalizzare matematicamente il concetto di
probabilità ci permetterà di sviluppare tecniche che consentono di calcolare
la probabilità di eventi complessi a partire da quella di eventi semplici:
è questo il caso del punto {numref}`4 <par:ten-heroes>` nell'elenco qui sopra,
nel quale la probabilità cercata si può ottenere una volta che è nota la
probabilità che un singolo eroe provenga da un universo _Star Wars_.

Molto spesso, gli eventi che vengono considerati fanno riferimento a una o
più quantità numeriche (come ad esempio negli esempi ai punti
{numref}`2 <par:faster-hero>` e {numref}`3 <par:same-intelligence>`) nel
precedente elenco: ha senso, per esempio, chiedersi se la resistenza di un
supereroe è massima, o se la sua altezza è compresa in un dato intervallo.
È importante sottolineare che il fatto che ogni supereroe abbia le stesse
_chance_ degli altri di essere osservato non implica assolutamente che la
stessa cosa valga per i valori che queste quantità possono assumere. Potete
facilmente rendervene conto riguardando l'istogramma in @fig:histogram:
un peso tra $50$ e $100$ kg. occorre molto di più di un peso superiore ai
cento chili. Diventa quindi importante modellare anche queste quantità
casuali, e in tal senso si introduce il concetto di _variabile aleatoria_ e la
relativa formalizzazione matematica. Senza entrare per ora nei dettagli, e
concentrandosi sempre sul peso dei supereroi, l'idea alla base di
questa formalizzazione è quella di _idealizzare_ l'istogramma dei valori
osservati, sostituendolo con il grafico di una funzione che rispetti le
proprietà fondamentali messe in luce dall'istogramma stesso. Focalizziamoci sempre
sulla @fig:histogram: ci sono infinite funzioni che esibiscono simmetria
rispetto a un asse centrale e andamento _unimodale_ (cioè crescente fino a
un valore massimo e poi decrescente), ma per motivi che al momento sono troppo
difficili da giustificare&mdash;ma che saranno chiari se una volta letto il
resto del libro&mdash;vale la pena concentrarci su questa:

```{math}
:label: eq:weight_normal
f(x) = \frac{1}{\sigma \sqrt{2 \pi}}
       \mathrm{exp}\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right) \enspace,
```

dove $x$ indica un generico peso e $f(x)$ la corrispondente altezza
nell'istogramma, mentre $\mu \in \mathbb R$ e $\sigma \in \mathbb R^+$ sono due
_parametri_ che cambiano la forma del grafico di $f$. Per la precisione,
@eq:weight_normal definisce una _famiglia_ di funzioni, che come vedremo
definisce a sua volta una famiglia di variabili aleatorie, o _modello_ di
variabile aleatoria.

Nel grafico interattivo riportato qui sotto è possibile vedere come cambia il
grafico di $f$ al variare dei suoi due parametri. In questo caso, è
però necessario attivare manualmente le funzionalità interattive cliccando
inizialmente sul pulsante ![jupyterlite on icon](images/jupyterlite.svg)
visualizzato nella parte alta della pagina web (operazione che è sufficiente
eseguire una sola volta per ogni pagina web del libro). Successivamente è
possibile attivare il grafico grafico cliccando sul pulsante
![jupyterlite run icon](images/run.svg) che compare a destra del grafico stesso
(questa operazione va ripetuta per ogni grafico interattivo presente nella
pagina): l'immagine sparirà, per ricomparire dopo circa un minuto, ora
arricchita con l'interfaccia che permette di interagire con la visualizzazione.
Nel caso che stiamo considerando compaiono due selettori, rispettivamente per
$\mu$ e $\sigma$: agendo su di essi è possibile cambiare i valori dei parametri
e simultaneamente vedere come varia il grafico della corrispondente versione di
$f$.
```{margin}
Questo secondo tipo di grafici interattivi è basato su
[jupyterlite](https://jupyterlite.readthedocs.io/), una tecnologia recentemente
sviluppata che permette di eseguire codice python direttamente all'interno di
un browser web. I grafici di questo tipo si riconoscono facilmente perché sotto
di essi è riportata la dicitura `a Jupyter kernel connection is required to
fully display this output`. Questa dicitura scompare una volta attivato il
grafico.
```

```{code-cell} ipython3
:tags: [remove-input]

%pip install -q ipywidgets

import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as st

mu_slider = widgets.FloatSlider(value=150,
                                        min=10,
                                        max=200,
                                        step=1,
                                        description=r'\(\mu\)',
                                        continuous_update=True,
                                        readout=False,
                                        orientation='horizontal')
sigma_slider = widgets.FloatSlider(value=12,
                                   min=5,
                                   max=40,
                                   step=0.1,
                                   description=r'\(\sigma\)',
                                   continuous_update=True,
                                   readout=False,
                                   orientation='horizontal')

def normal_pdf(mu, sigma):
    X = st.norm(mu, sigma)
    x = np.linspace(0, 200, 200)
    plt.fill_between(x, 0, X.pdf(x), alpha=0.5, color='tab:orange')
    plt.plot(x, X.pdf(x), lw=2, color='tab:orange')
    plt.ylim(0, 0.035)
    plt.show()

widgets.interactive(normal_pdf, mu=mu_slider, sigma=sigma_slider)
```

Uno dei motivi per i quali si parla di «modello» di variabile aleatoria sta nel
fatto che è possibile scegliere i valori dei suoi parametri in modo da
_adattare_ il modello ai dati che abbiamo osservato, che nel caso appena visto
consiste nello scegliere degli opportuni valori di $\mu$ e $\sigma$ in modo che
il grafico di $f$ si sovrapponga qualitativamente con quello dell'istogramma
inizialmente ottenuto per il peso. Il grafico interattivo
che segue permette di eseguire manualmente questa operazione, visualizzando
sia l'istogramma sia il grafico (variabile) di $f$. Dopo avere attivato il
grafico, agite sui selettori in modo da ottenere una buona sovrapposizione.

```{code-cell} ipython3
:tags: [remove-input]
%pip install -q ipywidgets

import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats as st

import pyodide_http

pyodide_http.patch_all()

source = 'https://raw.githubusercontent.com/dariomalchiodi/' + \
         'sds/main/content/data/heroes.csv'
heroes = pd.read_csv(source, index_col=0)

data = heroes.weight[heroes.weight < 200]

mu_slider = widgets.FloatSlider(value=150,
                                        min=10,
                                        max=200,
                                        step=1,
                                        description=r'\(\mu\)',
                                        continuous_update=True,
                                        readout=True,
                                        orientation='horizontal')
sigma_slider = widgets.FloatSlider(value=12,
                                   min=5,
                                   max=40,
                                   step=0.1,
                                   description=r'\(\sigma\)',
                                   continuous_update=True,
                                   readout=True,
                                   orientation='horizontal')

def normal_fit(mu, sigma):
    X = st.norm(mu, sigma)
    x = np.linspace(min(data), max(data), 200)
    plt.fill_between(x, 0, X.pdf(x), alpha=0.5, color='tab:orange')
    plt.plot(x, X.pdf(x), lw=2, color='tab:orange')
    plt.ylim(0, 0.035)

    plt.hist(data, bins=25, density=True, color='tab:blue')

    plt.show()

widgets.interactive(normal_fit, mu=mu_slider, sigma=sigma_slider)
```

Nell'ultima parte del libro, vedremo che in pratica esistono una serie di
metodi che permettono di determinare in modo automatico i parametri che
meglio si adattano a un insieme di dati. È questo, tra gli altri, lo scopo
della _statistica inferenziale_, illustrata nei Capitoli da
@cap:inferential_statistics a @cap:statistica-non-parametrica. Il punto di partenza
è sempre un _dataset_, che rappresenta ora un _campione_ di osservazioni
effettuate su una _popolazione_ che presenta alcuni aspetti ignoti sui quali
vogliamo gettare luce. Il caso più semplice&mdash;e quello che studieremo più a
fondo&mdash; è quello nel quale la popolazione è descritta da una variabile
aleatoria descritta da un modello nel quale uno o più parametri sono incogniti,
e lo scopo è quello di approssimare questi parametri, o altre quantità di
interesse che dipendono da questi ultimi. La statistica inferenziale, in un
certo senso, ci permette di «chiudere il cerchio»: sia perché mette in
pratica in maniera sinergica quello che abbiamo visto nelle parti sulla
statistica descrittiva e sul calcolo delle probabilità, sia perché permette di
comprendere a fondo la potenza di alcuni degli strumenti visti proprio
nell'ambito della statistica descrittiva, e le cui proprietà erano state
introdotte in modo relativamente informale.

Prima però di iniziare con la statistica descrittiva, è importante rivedere
alcuni concetti fondamentali di programmazione degli elaboratori, e
soprattutto prendere dimestichezza con gli strumenti computazionali che
userò in tutto il libro. È questo lo scopo dei capitoli
[Elaborare i dati con Python](introduzione-a-python) e [Pandas](pandas), che
aprono la trattazione.

### Esercizi

Al termine di ogni paragrafo sono proposti alcuni esercizi, la cui difficoltà
di risoluzione è indicata dal numero di pallini racchuso tra parentesi.

```{exercise} •
Scaricate il dataset dei supereroi dal
[repository](https://github.com/dariomalchiodi/sds) del libro e importatelo in
un qualsiasi programma che gestisce fogli elettronici (tutti quelli più diffusi
hanno la capacità di importare file CSV), in modo che ogni colonna contenga
un diverso attributo (vedi ). Focalizzatevi, diciamo, sulle prime trenta righe
e considerate separatamente le varie colonne, al fine di farvi un'idea di come
varino i valori associati ai singoli attributi.
```

```{exercise} •••
Riconsiderate l'esercizio precedente, guardando i contenuti
di ogni singola colonna del file CSV senza utilizzare un elaboratore di fogli
elettronici, ma usando solamente un terminale e i comandi di _shell_.
```
```{margin}
Essere _data scientist_ significa non solo sapere coniugare le competenze in
probabilità, statistica e programmazione degli elaboratori, ma anche
padroneggiare vari strumenti di _scripting_ che permettono di convertire,
adattare e ripulire i dati: molto spesso, l'uso di questi strumenti è mediato
da un terminale e dalla relativa _shell_. 
```

```{exercise} ••
Sulla base dell'idea che vi siete fatti in merito dal _dataset_ dei supereroi
risolvendo gli esercizi precedenti, provate a suddividere gli attributi in
gruppi omogenei basandovi non sul tipo di dato che viene utilizzato per
rappresentare i valori corrispondenti (indicato nella colonna «Contenuto» della
{numref}`tab:dataset`), bensì sulla _natura_ degli attributi stessi.
```

```{exercise} •
Rispondete alle domande numerate da 1 a 4 nell'elenco che segue il primo
grafico interattivo.
```

```{exercise} ••
Rispondete alle domande 5 e 6 nell'elenco che segue il primo grafico
interattivo. Verbalizzate il ragionamento che avete fatto e scrivetelo.
```

```{exercise} ••
Pensate ad altre domande relative al _dataset_ alle quali si possa trovare
risposta utilizzando il primo grafico interattivo. Anche in questo caso,
verbalizzate il ragionamento che va fatto per rispondere a queste domande.
```

```{exercise} •
Considerate i seguenti valori

$$ \{13, 8, 7, 4, 9, 8, 4, 4, 19, 2, 5, 3, 3, 1, 12 \} $$

e disegnate a mano il corrispondente istogramma, utilizzando i seguenti
intervalli di riferimento: $[0, 5)$, $[5, 10)$, $[10, 15)$, $[15, 20)$.
Confrontate la forma del grafico ottenuto con quanto mostrato nella
@fig:histogram, mettendo in luce le principali differenze.
```

```{exercise} •
Scrivete dieci possibili eventi che riguardano il _dataset_ dei supereroi.
```

```{exercise} ••
Scrivete un evento la cui probabilità è uguale a zero. Scrivete poi un
evento avente $1$ come probabilità.
```

```{exercise} ••
Ponete $\mu = \sigma = 1$ ed effettuate lo studio della funzione descritta
in @eq:weight_normal, disegnando a mano il grafico corrispondente e verificando
che questo grafico abbia la stessa forma visualizzata nel secondo grafico
interattivo.
```

```{exercise} •
Sulla base del risultato dell'esercizio precedente, e tenuto conto di quanto
avete sperimentato lavorando sul secondo grafico interattivo, che ruolo hanno i
parametri $\mu$ e $\sigma$ sul grafico di $f$ definita in @eq:weight_normal?
```

```{exercise} •
Utilizzando il secondo grafico interattivo, determinate dei valori per $\mu$ e
$\sigma$ che permettono di sovrapporre in modo ragionevole il grafico di $f$
all'istogramma della @fig:histogram.
```


[^histogram]: È possibile scegliere gli intervalli che individuano le basi dei
rettangoli con un certo grado di libertà. Per semplicità, nella @fig:histogram
l'istogramma è stato generato  considerando venticinque intervalli equiampi che
ricoprono tutti i valori possibili per il peso, ma a seconda dei casi può
essere sensato utilizzare un numero maggiore (o minore) di siffatti intervalli,
oppure considerare un insieme di intervalli di ampiezze diverse.

# Test Toggle Code

```{code-block} python
:class: toggle-code

print("Hello from English version!")
```