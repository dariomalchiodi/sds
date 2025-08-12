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

(sec:uno-sguardo-di-insieme)=
# Uno sguardo di insieme

Lo scopo di questo capitolo è duplice: da una parte, serve a descrivere per
sommi capi il filo logico che è dietro all'organizzazione dei contenuti e a
introdurre, in modo relativamente informale, i concetti cardine; dall'altra,
spiega come utilizzare le componenti interattive del libro. Come indicato nel
{ref}`chap:approccio`, nel testo farò riferimento a un _dataset_ ottenuto
modificando un opportuno sottoinsieme del [Superhero
database](http://www.superherodb.com){.external}. Gli esempi faranno quindi
riferimento al mondo dei supereroi, ognuno dei quali sarà descritto tramite gli
_attributi_ indicati nella {numref}`tab:dataset`.

```{margin}
Ho scelto di utilizzare la lingua inglese per indicare i nomi degli attributi
e i valori corrispondenti (quando questi sono descritti tramite stringhe),
per coerenza rispetto ai contenuti del dataset. Analogamente, il codice Python
sarà strutturato utilizzando nomi in inglese per variabili, funzioni e così via.
```

```{table} Descrizione del _dataset_ utilizzato negli esempi.
:name: tab:dataset
:align: center
| Attributo          | Significato               | Contenuto                                                |
|--------------------|---------------------------|----------------------------------------------------------|
| `name`             | identificativo univoco    | stringa                                                  |
| `full_name`        | nome completo             | stringa                                                  |
| `identity`         | identità segreta          | stringa                                                  |
| `alignment`        | inclinazione morale       | `'Good'`, `'Neutral'` o `'Bad'`                          |
| `place_of_birth`   | luogo di nascita          | stringa                                                  |
| `creator`          | editore/creatore          | stringa                                                  |
| `universe`         | universo                  | stringa                                                  |
| `first_appearance` | anno di prima apparizione | numero intero                                            |
| `eye_color`        | colore degli occhi        | stringa                                                  |
| `hair_color`       | colore dei capelli        | stringa                                                  |
| `height`           | altezza in cm.            | numero in virgola mobile                                 |
| `weight`           | peso  in kg.              | numero in virgola mobile                                 |
| `strength`         | forza                     | numero intero (da `0` a `100`)                           |
| `intelligence`     | intelligenza              | `'Low'`, `'Moderate'`, `'Average'`, `'Good'`, o `'High'` |
| `speed`            | velocità                  | numero intero (da `0` a `100`)                           |
| `durability`       | resistenza                | numero intero (da `0` a `100`)                           |
| `combat`           | abilità nel combattimento | numero intero (da `0` a `100`)                           |
| `powers`           | elenco dei superpoteri    | stringa                                                  |
```

```{margin}
L'estratto del _dataset_ viene prodotto dinamicamente, e può essere necessario
attendere alcuni secondi prima che questo venga visualizzato, rimpiazzando
la scritta `Please wait, loading PyScript... Lo stesso vale per
tutti i punti nei quali il browser deve eseguire del codice Python.
```
Il _dataset_ è memorizzato nel file `heroes.csv` contenuto nella directory
`data` del [repository](https://github.com/dariomalchiodi/sds){.external}
associato al libro. Nel codice interattivo, il file è accessibile come
`data/heroes.csv`. In questo file, i contenuti sono rappresentati utilizzando
il formato CSV (_comma separated values_), uno degli standard impiegati per
condividere dati di dimensioni relativamente contenute: ogni riga rappresenta
un supereroe, e in essa i valori degli attributi nella {numref}`tab:dataset`
sono indicati separandoli tramite virgole. L'unica eccezione è costituita dalla
prima riga del file, che contiene i nomi degli attributi, sempre separati
usando le virgole, come si può vedere visualizzando la parte iniziale del file
stesso. Qui sotto potete vedere la descrizione di alcuni degli attributi per
dieci supereroi del _dataset_ considerati a caso.

```{code-block} python
:class: toggle-code
import pandas as pd

# Load heroes data only once and persist it
if 'heroes' not in globals():
    heroes = pd.read_csv('data/heroes.csv', index_col=0).convert_dtypes()
    
source = heroes.sample(10).loc[:,'name':'combat']
source.index.name = None
source
```

Nel {ref}`chap:pandas` vedremo come caricare in memoria i contenuti di
questo file e, soprattutto, come elaborarli. Per ora, concentriamoci su
alcuni semplici esempi che, da una parte, mostrano come utilizzare le parti
interattive del libro, e, dall'altra, forniscono una panoramica di quelli che
saranno i concetti che illustrerò.

Quello che segue è un primo esempio di grafico interattivo. Nel diagramma in
alto sono rappresentati alcuni supereroi, utilizzando dei cerchi in un piano
cartesiano: le coordinate del centro indicano il peso e l'altezza, mentre il
raggio esprime la forza. Ogni cerchio è colorato con una sfumatura di
blu scelta in funzione dell'editore, e posizionandosi sopra di esso viene
automaticamente visualizzato il nome del supereroe corrispondente. Il
diagramma in basso mostra invece il numero di supereroi per ogni
editore/creatore, usando delle barre orizzontali. Selezionando un'area
rettangolare nel diagramma superiore è possibile concentrarsi su un
sottoinsieme di supereroi (con l'effetto di colorare in grigio i cerchi
che indicano i supereroi esclusi): in modo automatico, il diagramma inferiore
viene rigenerato in modo da riflettere la distribuzione del gruppo selezioato.
Una volta effettuata, la selezione può essere spostata, e cliccando
in un punto qualsiasi al di fuori di essa viene ripristinato il grafico
originale.
```{margin}
Il grafico qui accanto è stato realizzato utilizzando
[altair](https://altair-viz.github.io/){.external}, una libreria che permette
di utilizzare Python per visualizzare grafici complessi all'interno di pagine
web, in una forma interattiva che è automaticamente attivata nel momento in cui
una pagina viene caricata. Per riconoscere se un grafico è stato generato
tramite altair, è sufficiente controllare se in alto a destra è presente un
pulsante rotondo che contiene tre punti. Questo pulsante attiva un menu che
permette, tra le altre cose, di scaricare il grafico.
```

```{code-block} python
:class: toggle-code

import altair as alt

# Use cached heroes data if available
if 'heroes' not in globals():
    heroes = pd.read_csv('data/heroes.csv', index_col=0).convert_dtypes()

filter = (heroes['creator'].isin(heroes.creator.value_counts()[:15].index))
filter &= (heroes['weight']<200)
filter &= (heroes['height']<250)
source = heroes[filter].sample(1500)

# Create the selection for brushing
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
            alt.Color('creator', title='Creator').scale(scheme="blues"),
        ).transform_filter(brush)

# Create the final interactive chart
chart = (points & bars).configure(background='#eaf3f5')
chart
```

Interagendo con il grafico è possibile effettuare un'_analisi esplorativa_ dei
dati, per esempio per rispondere alle domande seguenti.

1. Qual è l'editore/creatore con più supereroi in assoluto?
2. Quale editore ha il maggior numero di supereroi alti meno di un metro?
3. Quale editore ha il maggior numero di supereroi che pesano tra 80 e 100 kg.?
4. Qual è il supererore più alto in assoluto?

```{margin}
In generale, solo una piccola parte dei grafici che vedremo saranno
interattivi.
```
Ci sono ovviamente tanti aspetti che possono essere analizzati preliminarmente
semplicemente guardando il grafico così come è stato prodotto (cioè senza
utilizzare le componenti interattive), come per esempio i due indicati
di seguito.

5. Esiste una relazione di qualche tipo che lega tendenzialmente il peso e
   l'altezza dei supereroi?
6. Questa relazione cambia se ci concentriamo sui supereroi che corrispondono
   a un particolare editore/creatore?

La _statistica descrittiva_, introdotta dal {ref}`chap:dati-e-informazione`
al {ref}`chap:analizzare-le-relazioni-tra-i-dati`, fornisce degli strumenti che
permettono di rispondere a domande come quelle appena considerate. In generale,
lo scopo è quello di estrarre informazioni da un _dataset_ che descrive,
globalmente o parzialmente, un insieme di individui di riferimento, e le
tecniche utilizzate possono avere una natura sia _qualitativa_, sia
_quantitativa_. Si parla di analisi qualitativa quando lo scopo è quello di
determinare la natura di un certo fenomeno (per esempio, per rispondere alle
domande ai punti 5 o 6 nell'elenco qui sopra). Questo richiede spesso di
utilizzare degli strumenti, come il grafico precedentemente visualizzato, i cui
risultati devono essere interpretati, introducendo un certo grado di
soggettività. Si parla invece di analisi quantitativa quando l'esito
di quest'ultima è espresso da una o più quantità numeriche, che possono essere
quindi messe a confronto in modo oggettivo con altre quantità (tipicamente,
i risultati di altre analisi).
```{margin}
Se tutto questo suona complicato, non vi preoccupate: i concetti diventeranno
più chiari nei capitoli successivi.
```

Supponiamo ora di volerci concentrare, per semplicità, sul peso dei
supereroi: il grafico precedente è decisamente pieno di cerchi, e
mentre è relativamente facile farsi un'idea dell'altezza più piccola e di
quella più grande, diventa poco chiaro, per esempio, capire se ci sono più
supereroi «leggeri» che «pesanti». Per capire meglio, riporto qui sotto un
particolare grafico, chiamato _istogramma_, che evidenzia le frequenze con le
quali i valori diversi del peso sono presenti nel _dataset_.

```{code-block} python
:class: toggle-code

import matplotlib.pyplot as plt

# Use cached heroes data if available
if 'heroes' not in globals():
    heroes = pd.read_csv('data/heroes.csv', index_col=0).convert_dtypes()

fig, ax = plt.subplots()
data = heroes.weight[heroes.weight < 200]

ax.hist(data, bins=30, density=True)
fig.show()
```

```{margin}
Non sempre ha senso utilizzare un istogramma per esplorare dei valori in un
_dataset_, come vedremo nel {ref}`chap:dati-e-informazione`.
```

```{margin}
Vedremo altresì che il processo di esplorazione non deve
necessariamente (o esclusivamente) coinvolgere l'uso di metodi grafici, ma può
essere basato anche sull'utilizzo di strumenti quantitativi (e tipicamente lo
è).
```
Gli istogrammi sono definiti in dettaglio nel {ref}`sec:istogrammi`, ma per il
momento ci basta sapere come leggere il risultato ottenuto: in ognuno dei
rettangoli mostrati, la base individua un intervallo $I$ di possibili valori
per il peso dei supereroi, e l'altezza è legata alla frazione di supereroi che
hanno un peso contenuto in $I$ [^histogram]. Il grafico ottenuto mette in
evidenza alcune cose interessanti: per esempio si vede che i supereroi con un
peso superiore a 125 kg. sono presenti in numero maggiore rispetto a quelli con
un peso inferiore a quaranta chili. D'altro canto, se non consideriamo i pesi
molto grandi o molto piccoli, emerge un'approssimativa simmetria nei valori
rispetto a un asse centrale, unitamente al fatto che le altezze dei rettangoli
tendono a crescere, approssimativamente fino ai $70$ kg, per poi diminuire.
Anche questa è un'esplorazione dei dati, che in questo caso non richiede
l'utilizzo di grafici interattivi.

```{margin}
Se siete attenti avrete notato che l'altezza di un rettangolo non può essere
uguale al numero di supereroi che hanno un certo peso, perché i valori mostrati
sull'asse delle ordinate non sono numeri interi. In questo istogramma, infatti,
il numero di supereroi è legato all'area del rettangolo, cosa che ci
permetterà tra poco di confrontare il risultato ottenuto con un altro grafico.
Il motivo di questa scelta è approfondito nel {ref}`sec:istogrammi`.
```

Una volta accumulata conoscenza sui dati a disposizione, il passo successivo
richiede normalmente di _modellare_ il processo che li ha generati, e per fare
ciò è necessario cambiare in modo radicale la nostra prospettiva, immaginando
non in termini dell'intero _dataset_, ma piuttosto ponendoci domande relative
all'osservazione di uno qualsiasi dei suoi elementi, o di un insieme di
elementi, nell'ipotesi di non sapere a priori che cosa osserveremo (ricordatevi
della [Legge di Franklin](#par:franklin-law)), ma assumendo che ogni supereroe
abbia la stessa possibilità di tutti gli altri di essere osservato. A partire
dal {ref}`{chap:calcolo-combinatorio}` e fino al
{ref}`chap:va-e-modelli-continui`, il libro descrive la _Teoria della
Probabilità_, fornendo alcuni strumenti formali per gestire
l'incertezza dovuta al non sapere che cosa verrà di volta in volta osservato.
Più precisamente, ci concentreremo su degli _eventi_, intesi come affermazioni
che riguardano l'esito delle osservazioni. Sempre pensando ai supereroi, sono
ad esempio eventi le seguenti affermazioni:

1. un supereroe è cattivo (nell'ipotesi che ogni supereroe abbia
   un'inclinazione morale definita a priori, come misurato nell'attributo
   `alignement` del _dataset_ che utilizziamo);
2. un supereroe Marvel è più veloce di un supereroe DC;
3. due supereroi apparsi per la prima volta nello stesso anno hanno lo stesso
   indice di intelligenza;
4. almeno un supereroe in un gruppo di dieci è collocato in uno degli
   universi di _Star Wars_.

Chiaramente, non è noto a priori se l'affermazione che costituisce un evento
è vera o falsa, perché il valore di verità dipende da quelle che saranno le
effettive osservazioni. Per questo motivo, viene introdotto il concetto
cardine di _probabilità_, intesa come quantificazione numerica di questa
incertezza, utilizzando un numero $p \in [0, 1]$. Senza entrare per ora nei
dettagli, più tale numero è prossimo a $\frac{1}{2}$ e più l'incertezza è
elevata; dualmente, quanto più $p$ si avvicina agli estremi, tanto più si
riduce questa incertezza: al tendere di $p$ a zero, si riduce sempre di
più la confidenza che l'affermazione sia vera, al punto che, quando la
probabilità è nulla, l'affermazione diventa sicuramente falsa; analogamente,
la confidenza aumenta al crescere di $p$, e l'affermazione sarà sicuramente
vera quando $p = 1$. Come vedremo, il vantaggio di formalizzare matematicamente
il concetto di probabilità ci permetterà di sviluppare tecniche che consentono
di calcolare la probabilità di eventi complessi a partire da quella di eventi
semplici: è questo il caso del punto 4 nell'elenco qui sopra, nel quale la
probabilità cercata si può ottenere una volta che è nota la probabilità che un
singolo eroe provenga da un universo _Star Wars_.

Molto spesso, gli eventi che vengono considerati fanno riferimento a una o
più quantità numeriche (come ad esempio negli esempi ai punti 2 e 3 nel
precedente elenco): ha senso, per esempio, chiedersi se la resistenza di un
supereroe è massima, o se la sua altezza è compresa in un dato intervallo.
È importante sottolineare che il fatto che ogni supereroe abbia le stesse
_chance_ degli altri di essere osservato non implica assolutamente che la
stessa cosa valga per i valori che queste quantità possono assumere. Potete
facilmente rendervene conto riguardando il precedente istogramma: un peso tra
$50$ e $100$ kg. è molto più frequente rispetto a un peso superiore ai cento
chili. Diventa quindi importante modellare anche queste quantità casuali, e in
tal senso si introduce il concetto di _variabile aleatoria_ e la relativa
formalizzazione matematica. Senza entrare per ora nei dettagli, concentriamoci
sul caso specifico del peso dei supereroi, mettendo in chiaro che in generale
il procedimento può essere più complicato o semplicemente diverso. L'idea alla 
base della formalizzazione è quella di individuare una funzione $f$, detta
_densità di probabilità_, il cui grafico _idealizza_ l'istogramma dei valori
osservati, pur continuando a rispettarne le proprietà fondamentali. Per
l'esempio in questione, possiamo identificare queste proprietà come essere
simmetrico rispetto a un asse centrale e avere un andamento _unimodale_ (cioè
crescente fino a un valore massimo e decrescente da lì in avanti). Ci sono
infinite funzioni che esibiscono queste due proprietà, ma per motivi che al
momento sono troppo difficili da giustificare&mdash;ma che dovrebbero risultare
chiari una volta letto il resto del libro&mdash;vale la pena concentrarci su
quella definita da:

```{margin}
In questa formula, $\exp(x)$ indica l'elevamento della costante $\mathrm e$
alla potenza $x$: questa forma è preferibile a $\mathrm e^x$ per evitare la
presenza di un esponente frazionario, che risulterebbe meno leggibile.   
```
```{math}
:label: eq:weight_normal
f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2 \pi}} \;
       \mathrm{exp}\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right) \enspace,
```

dove $x$ indica un generico peso e $f(x; \mu, \sigma)$ individua il valore
dell'altezza corrispondente nell'istogramma idealizzato. È importante
evidenziare che $f$ ha un solo argomento, denotato da $x$, mentre
$\mu \in \mathbb R$ e $\sigma \in \mathbb R^+$ vanno intesi come due
_parametri_: la funzione risulta completamente definita solo quando il loro
valore è stato fissato. Il punto e virgola nella definizione di $f$ ha appunto
lo scopo di evidenziare il ruolo differente che hanno l'argomento, da una
parte, e i parametri, dall'altra. Per la precisione, {eq}`eq:weight_normal`
definisce, al variare di $\mu$ e $\sigma$, una _famiglia_ di funzioni, ognuna
delle quali è associata a una variabile aleatoria. Il risultato è una famiglia
di variabili aleatorie, alla quale ci si riferisce come a un _modello_ di
variabile aleatoria. Nel diagramma interattivo riportato qui sotto è possibile
vedere come cambia il grafico di $f$ al variare dei suoi due parametri. Agendo
sui due selettori, associati rispettivamente a $\mu$ e $\sigma$, è possibile
cambiare i valori dei parametri corrispondenti e simultaneamente vedere come
varia il grafico di $f$.

```{code-block} python
:class: toggle-code 
import numpy as np
from js import document
from pyodide.ffi import create_proxy
import pyscript as pys
import io
import base64

def plot_pdf(mu, sigma):
    x = np.linspace(-10, 10, 400)
    y = (1 / (sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
    
    fig, ax = plt.subplots()
    ax.fill_between(x, 0, y, alpha=0.5, color='tab:blue')

    # Use plain text label to avoid MathJax processing
    ax.set_xlabel('x', fontsize=12, ha='right')
    ax.xaxis.set_label_coords(1.07, 0.03)
    ax.set_xlim(-10, 10)
    ax.set_ylim(0, 1)
    
    # Manual rendering to avoid MathJax processing
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format='png', bbox_inches='tight', dpi=100)
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    img_buffer.close()
    
    # Display in protected div
    img_html = '<div class="no-mathjax"><img src="data:image/png;base64,' + \
               img_base64 + '" style="max-width: 100%; height: auto;" /></div>'
    Element("pdf-output").write(img_html)
    
    plt.close(fig)

def update_plot(event=None):
    mu = float(document.getElementById("mean-slider").value)
    sigma = float(document.getElementById("std-slider").value)
    document.getElementById("mean-value").innerText = f"{mu:.1f}"
    document.getElementById("std-value").innerText = f"{sigma:.1f}"
    plot_pdf(mu, sigma)


mean_slider = document.getElementById("mean-slider")
std_slider = document.getElementById("std-slider")

mean_slider.addEventListener("input", create_proxy(update_plot))
std_slider.addEventListener("input", create_proxy(update_plot))

# Initial plot
plot_pdf(0, 1)
```
```{raw} html

<div id="plot-container" style="visibility: none;">
    <div class="slider-container" style="float: left;">
        <label for="mean-slider">$\mu$: </label>
        <input type="range" id="mean-slider"
               min="-5" max="5" value="0" step="0.1" />
        <span id="mean-value">0</span>
    </div>

    <div class="slider-container" style="float: right;">
        <label for="std-slider">$\sigma$: </label>
        <input type="range" id="std-slider"
               min="0.1" max="5" value="1" step="0.1" />
        <span id="std-value">1.0</span>
    </div>

    <div id="pdf-output" class="no-mathjax"
            style="clear: both; display: flex; justify-content: center; margin-bottom: 2em;">
        <div class="splash"></div>
    </div>
</div>
```

Uno dei motivi per i quali si parla di «modello» di variabile aleatoria è
legato al fatto che è possibile scegliere i valori dei suoi parametri in modo
da _adattare_ il grafico di $f$, e più in generale la corrispondente variabile
aleatoria, a dati precedentemente osservati. Nel caso appena visto, ciò
equivale a scegliere dei valori opportuni per $\mu$ e $\sigma$, facendo sì che
il grafico di $f$ si sovrapponga qualitativamente con quello dell'istogramma
inizialmente ottenuto per il peso. Il seguente diagramma interattivo permette
di eseguire manualmente questa operazione: potete quindi agire sui selettori in
modo da ottenere una buona sovrapposizione tra l'istogramma e la funzione di
densità di probabilità.

```{code-block} python
:class:  toggle-code

import base64
import io

# Use variable persistence - check if heroes/data is already loaded
if 'heroes' not in builtins.__dict__:
    # Load heroes data only once per session
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Check if heroes.csv exists and download if needed
    from pathlib import Path
    heroes_path = Path("data/heroes.csv")
    if not heroes_path.exists():
        # Ensure directory exists
        heroes_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Download the file
        from urllib.request import urlretrieve
        url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-04-23/week4_powerlifting.csv"
        try:
            urlretrieve(url, heroes_path)
            print("Downloaded heroes.csv")
        except Exception as e:
            print(f"Error downloading heroes.csv: {e}")
    
    # Load the data
    try:
        heroes = pd.read_csv(heroes_path)
        print(f"Loaded heroes data with {len(heroes)} rows")
    except Exception as e:
        print(f"Error loading heroes.csv: {e}")
        heroes = pd.DataFrame()
    
    # Store in builtins for persistence
    builtins.heroes = heroes
    builtins.data = heroes.weight[heroes.weight < 200]
    print("Variables stored in builtins for persistence")
else:
    # Use existing data
    heroes = builtins.heroes
    data = builtins.data
    print("Using existing heroes and data from builtins")

def model_plot_pdf(mu, sigma):
    x = np.linspace(0, 200, 400)
    y = (1 / (sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
    
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, density=True, alpha=0.3, color='tab:blue')
    ax.fill_between(x, 0, y, alpha=0.5, color='tab:blue')

    # Use plain text for axis labels to avoid MathJax interference
    ax.set_xlabel('x', fontsize=12, ha='right')
    ax.xaxis.set_label_coords(1.07, 0.03)
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 0.02)
    
    # Convert plot to base64 string for display
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', dpi=100)
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode()
    plt.close(fig)
    
    # Display in no-mathjax container
    output_html = f'''
    <div class="no-mathjax" style="display: flex; justify-content: center; margin-bottom: 2em;">
        <img src="data:image/png;base64,{img_base64}" alt="Model Plot" style="max-width: 100%; height: auto;">
    </div>
    '''
    
    target_element = document.getElementById("model-output")
    if target_element:
        target_element.innerHTML = output_html
    else:
        print("Target element 'model-output' not found")

def model_update_plot(event=None):
    try:
        mu = float(document.getElementById("model-mean-slider").value)
        sigma = float(document.getElementById("model-std-slider").value)
        document.getElementById("model-mean-value").innerText = f"{mu:.1f}"
        document.getElementById("model-std-value").innerText = f"{sigma:.1f}"
        model_plot_pdf(mu, sigma)
    except Exception as e:
        print(f"Error updating plot: {e}")

# Wait for DOM to be ready
def setup_model_sliders():
    try:
        model_mean_slider = document.getElementById("model-mean-slider")
        model_std_slider = document.getElementById("model-std-slider")
        
        if model_mean_slider and model_std_slider:
            model_mean_slider.addEventListener("input", create_proxy(model_update_plot))
            model_std_slider.addEventListener("input", create_proxy(model_update_plot))
            
            # Initial plot
            model_plot_pdf(150, 33)
            print("Model sliders setup complete")
        else:
            print("Model slider elements not found, retrying in 100ms...")
            import asyncio
            asyncio.get_event_loop().call_later(0.1, setup_model_sliders)
    except Exception as e:
        print(f"Error setting up model sliders: {e}")

# Setup sliders when DOM is ready
setup_model_sliders()
```
```{raw} html

<div id="plot-container" style="visibility: none;">
    <div class="model-slider-container" style="float: left;">
        <label for="model-mean-slider">Mean ($\mu$): </label>
        <input type="range" id="model-mean-slider"
               min="10" max="200" value="150" step="0.1" />
        <span id="model-mean-value">150</span>
    </div>

    <div class="model-slider-container" style="float: right;">
        <label for="model-std-slider">Standard Deviation ($\sigma$): </label>
        <input type="range" id="model-std-slider"
               min="0.1" max="50" value="33" step="0.1" />
        <span id="model-std-value">33.0</span>
    </div>

    <div id="model-output" style="clear: both; display: flex; justify-content: center; margin-bottom: 2em;">
        <div class="splash"></div>
    </div>
</div>
```

Nell'ultima parte del libro, vedremo che esistono vari metodi che permettono di
determinare in modo automatico i parametri di un modello, al fine di adattarlo
a un insieme di dati. È questo, tra gli altri, lo scopo della _statistica
inferenziale_, illustrata a partire dal {ref}`chap:inferential_statistics` e
fino al {ref}`chap:statistica-non-parametrica`. Il punto di partenza è sempre
un _dataset_, che in questo contesto rappresenta un _campione_ di osservazioni
effettuate su una _popolazione_ più ampia. Su questa popolazione vogliamo fare
delle ipotesi o trarre delle conclusioni, anche se non possiamo osservarla
direttamente nella sua interezza. In altre parole, useremo il campione per
ottenere informazioni su ciò che non sappiamo della popolazione. Il caso più
semplice&mdash;e anche quello su cui ci concentreremo maggiormente&mdash; è
quello nel quale la popolazione è descritta da una variabile aleatoria,
associata a un modello che dipende da uno o più parametri sconosciuti.
L'obiettivo è quello di approssimare questi parametri, o altre quantità di che
dipendono da essi. Per esempio, immaginiamo che la popolazione sia composta da
di tutti i supereroi nel nostro _dataset_, e che la quantità che ci interessa
sia il loro peso medio $p$. Se abbiamo a disposizione solo un campione di
cento supereroi, il buon senso suggerisce di usare la media del loro peso come
approssimazione di $p$. Si usa in generale il termine _stimatore_ per indicare
la funzione che viene applicata al campione per ottenere questo tipo di
approssimazioni. Nel nostro esempio, lo stimatore utilizzato è la media
aritmetica dei valori del campione, e viene chiamata _media campionaria_. La
tabella seguente mostra come variano i valori di questo stimatore in seguito
all'estrazione di dieci campioni differenti.

```{code-block} python
:class:  toggle-code

weights = heroes['weight'][heroes['weight']<200].dropna()

def sample_mean(weights, n=100):
    sample = weights.sample(n)
    return sample.mean().round(2)

num_samples = 10
means = [sample_mean(weights) for _ in range(num_samples)]
pd.DataFrame([means],
             columns=[f'#{i}' for i in range(1, num_samples+1)],
             index=['Mean weight'])

```

Come si può osservare, le medie campionarie ottenute dai dieci campioni sono
diverse tra loro, e non potrebbe essere altrimenti, dal momento che ogni
campione è diverso. Tuttavia, i risultati ottenuti non variano drasticamente e
tendono a concentrarsi attorno a $79$, che è una buona approssimazione del
valore  corretto per il peso medio di tutti i supereroi (come potete verificare
osservando il precedente istogramma). Ma possiamo essere certi che la media
campionaria sia davvero il miglior stimatore possibile? E, più in generale,
come possiamo valutare la bontà di uno stimatore, tenendo in conto anche della
variabilità intrinseca che abbiamo appena evidenziato? Queste domande
troveranno risposta nella parte dedicata alla statistica inferenziale. Questa
parte, in un certo senso, mi permette di terminare il libro «chiudendo il
cerchio»: sia perché mette in pratica in maniera sinergica
quello che abbiamo visto nelle parti sulla statistica descrittiva e sul calcolo
delle probabilità, sia perché permette di comprendere più a fondo la potenza di
alcuni dei concetti e degli strumenti già incontrati&mdash;magari in modo
relativamente informale&mdash;nelle parti precedenti.

Prima però di iniziare con la statistica descrittiva, è importante rivedere
alcuni concetti fondamentali di programmazione degli elaboratori, e
soprattutto prendere dimestichezza con gli strumenti computazionali che
userò in tutto il libro. È questo lo scopo del {ref}`chap:intro-python` e del
{ref}`chap:pandas`, che aprono la trattazione.

## Esercizi

Al termine di ogni paragrafo sono proposti alcuni esercizi, la cui difficoltà
di risoluzione è indicata dal numero di pallini racchuso tra parentesi.

```{exercise} •
Scaricate il _dataset_ dei supereroi dal
[repository](https://github.com/dariomalchiodi/sds){.external} del libro e
importatelo in un qualsiasi programma che gestisce fogli elettronici (tutti
quelli più diffusi hanno la capacità di importare file CSV), in modo che ogni
colonna contenga un diverso attributo. Focalizzatevi, diciamo, sulle prime
trenta righe e considerate separatamente le varie colonne, al fine di farvi
un'idea di come varino i valori associati ai singoli attributi.
```

```{margin}
Essere _data scientist_ significa non solo sapere coniugare le competenze in
probabilità, statistica e programmazione degli elaboratori, ma anche
padroneggiare vari strumenti di _scripting_ che permettono di convertire,
adattare e ripulire i dati: molto spesso, l'uso di questi strumenti è mediato
da un terminale e dalla relativa _shell_. 
```
```{exercise} •••
Riconsiderate l'esercizio precedente, guardando i contenuti
di ogni singola colonna del file CSV senza utilizzare un elaboratore di fogli
elettronici, ma usando solamente un terminale e i comandi di _shell_.
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

$$ \\{13, 8, 7, 4, 9, 8, 4, 4, 19, 2, 5, 3, 3, 1, 12 \\} $$

e disegnate a mano il corrispondente istogramma, calcolando l'altezza di ogni
rettangolo come il numero di valori che ricadono nell'intervallo
corrispondente, e utilizzando i seguenti intervalli di riferimento:
$[0, 5)$, $[5, 10)$, $[10, 15)$, $[15, 20)$.
Confrontate la forma del grafico ottenuto con quanto mostrato nel testo,
mettendo in luce le principali differenze.
```

```{exercise} •
Scrivete dieci possibili eventi che riguardano il _dataset_ dei supereroi.
```

```{exercise} ••
Scrivete un evento la cui probabilità è uguale a zero. Scrivete poi un
evento avente $1$ come probabilità.
```

```{exercise} ••
Ponete $\mu = \sigma = 1$ ed effettuate lo studio della funzione descritta in
{eq}`eq:weight_normal`, disegnando a mano il grafico corrispondente e
verificando che questo grafico abbia la stessa forma visualizzata nel secondo
grafico interattivo.
```

```{exercise} •
Sulla base del risultato dell'esercizio precedente, e tenuto conto di quanto
avete sperimentato lavorando sul secondo grafico interattivo, che ruolo hanno i
parametri $\mu$ e $\sigma$ sul grafico di $f$ definita in
{eq}`eq:weight_normal`?
```

```{exercise} •
Utilizzando il secondo grafico interattivo, determinate dei valori per $\mu$ e
$\sigma$ che permettono di sovrapporre in modo ragionevole il grafico di $f$
all'istogramma del peso dei supereroi.
```

```{exercise} ••
Verbalizzate il ragionamento che avete fatto per convincervi che $79$ è
approssimativamente il valore medio del peso dei supereroi.
```

[^histogram]: È possibile scegliere gli intervalli che individuano le basi dei
rettangoli con un certo grado di libertà. Per semplicità, l'istogramma nel
testo è stato generato  considerando venticinque intervalli equiampi che
ricoprono tutti i valori possibili per il peso, ma a seconda dei casi può
essere sensato utilizzare un numero maggiore (o minore) di siffatti intervalli,
oppure considerare un insieme di intervalli di ampiezze diverse.
