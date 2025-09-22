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

(chap:uno-sguardo-di-insieme)=
# Uno sguardo di insieme

Lo scopo di questo capitolo è duplice: da una parte, mira a descrivere la
logica con cui ho organizzato i contenuti e a introdurre, in modo relativamente
informale, i concetti cardine. Dall'altra, spiega come utilizzare le componenti
interattive del libro. Come indicato nel {ref}`chap:approccio`, nel testo farò
riferimento a un _dataset_ ottenuto modificando un sottoinsieme del
{extlink}`Superhero database <http://www.superherodb.com>`. Gli esempi traggono
quindi spunto dal mondo dei supereroi, ciascuno dei quali è descritto tramite
gli _attributi_ indicati nella {numref}`tab:dataset`.

```{margin}
Ho scelto di mantenere l'inglese per i nomi degli attributi e per i loro valori
(quando sono descritti tramite stringhe), per coerenza con i contenuti del
_dataset_. Analogamente, nel codice Python utilizzerò nomi in inglese per
variabili, funzioni e altri identificatori.
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
L'estratto del _dataset_ viene generato dinamicamente, e può essere necessario
attendere alcuni secondi prima che compaia, sostituendo il messaggio `Attendere
il caricamento di PyScript...`. Lo stesso comportamento si verifica in tutti i
punti in cui il browser esegue codice Python.
```
Il _dataset_ è memorizzato nel file `heroes.csv` contenuto nella directory
`data` del {extlink}`repository <https://github.com/dariomalchiodi/sds>`
associato al libro. Nel codice interattivo, il file è accessibile come
`data/heroes.csv`. I suoi contenuti sono rappresentati utilizzando il formato
CSV (_comma separated values_), uno standard comunemente usato per condividere
dati di dimensioni relativamente ridotte: ogni riga corrisponde a un supereroe,
e in essa i valori degli attributi nella {numref}`tab:dataset` sono separati da
virgole. L'unica eccezione riguarda la prima riga del file, che contiene i nomi
degli attributi, anch'essi separati da virgole. La
{numref}`tab:dataset-excerpt` mostra un estratto del _dataset_, visualizzandone
i valori di alcuni attributi per dieci supereroi selezionati casualmente.

````{customfigure}
:name: tab:dataset-excerpt
:class: full-width

```{code-block} python
:class: toggle-code
import pandas as pd

heroes = pd.read_csv('data/heroes.csv', index_col=0).convert_dtypes()
    
source = heroes.sample(10).loc[:,'name':'combat']
source.index.name = None
source
```

Valori degli attributi `name`, `identity`, `intelligence`, `strength`, `speed`,
`durability`, `power` e `control` per dieci elementi estratti casualmente dal
_dataset_ di riferimento.

````

Nel {ref}`chap:pandas` vedremo come caricare in memoria e analizzare i
contenuti di questo file. Per ora, ci concentreremo su alcuni esempi
preliminari. Quello contenuto nella {numref}`fig:altair-example` è un primo
esempio di grafico interattivo. Nel diagramma in alto, alcuni supereroi sono
rappresentati tramite cerchi in un piano cartesiano: le coordinate del centro
indicano peso e altezza, mentre il raggio esprime la forza. Il colore varia in
base all'editore, utilizzando diverse sfumature di blu. Posizionando il
puntatore su un cercio viene visualizzato il nome del supereroe corrispondente.
Il diagramma inferiore mostra invece delle barre orizzontali che indicano il
numero di supereroi per ciascun editore o creatore. È possibile selezionare un
sottoinsieme di supereroi tracciando un rettangolo nel diagramma superiore: gli
altri elementi del _dataset_ vengono disattivati, colorandoli in grigio, e il
grafico inferiore viene aggiornato per riflettere la distribuzione del gruppo
selezionato. La selezione può essere spostata, e facendo clic al suo esterno si
ripristina la visualizzazione originale.
```{margin}
Il grafico in {numref}`fig:altair-example` è stato realizzato con
{extlink}`Altair <https://altair-viz.github.io/>`, una libreria Python
per la creazione di grafici interattivi in pagine web. Un segno distintivo dei
grafici Altair è la presenza, in alto a destra, di un pulsante rotondo con tre
punti: questo attiva un menu che consente, tra le altre funzioni, di scaricare
il grafico.
```

````{customfigure}
:name: fig:altair-example

```{code-block} python
:class: toggle-code

import altair as alt

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

Un esempio di grafico interattivo basato su altair.

````

Interagendo con il grafico è possibile effettuare un’_analisi esplorativa_ dei
dati, per esempio per rispondere alle domande seguenti.

1. Qual è l'editore/creatore con più supereroi in assoluto?
2. Quale editore ha il maggior numero di supereroi alti meno di un metro?
3. Quale editore ha il maggior numero di supereroi con un peso compreso tra 80
   e 100 kg.?
4. Qual è il supereroe più alto?

Molti aspetti possono essere analizzati anche senza interagire con il grafico,
semplicemente osservandolo nella sua forma iniziale, come per le due domande
qui sotto.

5. Esiste una relazione tendenziale tra peso e altezza dei supereroi?
6. Questa relazione cambia se consideriamo solo i supereroi di un determinato
   editore/creatore?

```{margin}
Se tutto questo sembra complicato, non vi preoccupate: i prossimi capitoli
spiegheranno questi concetti partendo dalle basi.
```
Domande come queste si affrontano con gli strumenti della _statistica
descrittiva_, introdotta nei capitoli
{numref}`chap:dati-e-informazione`&ndash;{numref}`sec:analizzare-relazioni`. Il
suo obiettivo è estrarre informazioni da un _dataset_ che descrive un insieme
di individui, in tutto o in parte. Le tecniche impiegate possono essere di due
tipi: _qualitative_ o _quantitative_.

- L'analisi qualitativa cerca di determinare la natura di un certo fenomeno (ad
  esempio, per rispondere alle domande 5 e 6 nell'elenco precedente). Spesso si
  basa su strumenti grafici, i cui risultati devono essere interpretati,
  introducendo un certo grado di soggettività.
- L'analisi quantitativa, invece, ha come risultato uno o più valori numerici,
  che possono essere confrontate in modo oggettivo con altre misure (come i
  risultati di altre analisi).

Per semplicità, concentriamoci ora sul peso dei supereroi. Il grafico
precedente è piuttosto affolalto: se da un lato è facile individuare le altezze
minima e massima, dall'altro non è immediato capire se prevalgano i supereroi
«leggeri» o quelli più «pesanti». Per chiarire questo aspetto, si può ricorrere
a un _istogramma_, un grafico che evidenzia le frequenze con cui i diversi
valori del peso compaiono nel _dataset_.

````{customfigure}
:name: fig:histogram

```{code-block} python
:class: toggle-code

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
data = heroes.weight[heroes.weight < 200]

ax.hist(data, bins=30, density=True)
fig.show()
```

Un istogramma per il peso dei supereroi.
````

```{margin}
Non sempre l'istogramma è la scelta giusta per esplorare i dati. È utile quando
abbiamo molte osservazioni numeriche di un attributo continuo; in altri casi,
può essere fuorviante (ne parleremo nel {ref}`chap:dati-e-informazione`).
```

```{margin}
L'esplorazione dei dati non implica sempre l'uso di metodi grafici: più avanti
vedremo che spesso si fonda su strumenti quantitativi.
```
Gli istogrammi sono spiegati in dettaglio nel {ref}`chap:dati-e-informazione`,
ma per ora su come leggerne uno. Il grafico è composto da tanti rettangoli:
ognuno di essi ha come base un intervallo $I$ di possibili valori per il peso,
e l'altezza è legata alla frazione di supereroi il cui peso rientra in
quell'intervallo[^histogram]. Guardando l'istogramma, notiamo due cose
interessanti:

- i supereroi che pesano più di 125 kg. sono più numerosi di quelli sotto i
  quaranta chili;
- se escludiamo i pesi estremi, la distribuzione è grossomodo simmetrica, con
  le altezze dei rettangoli che crescono fino a circa 70 kg. e poi calano.

Questa è una prima forma di analisi esplorativa, anche senza grafici
interattivi.

```{margin}
Guardando l'asse delle ordinate, vediamo che i valori non sono interi,
pertanto l'altezza dei rettangoli non può rappresentare il numero di supereroi.
In questo istogramma è l'area del rettangolo a essere proporzionale alla
frequenza. Questa scelta, che ha implicazioni importanti, è spiegata in
dettaglio nel {ref}`chap:dati-e-informazione`.
```

Dopo aver raccolto informazioni a partire dai dati, il passo successivo è
provare a _modellare_ matematicamente il processo che li ha generati. Per farlo
dobbiamo cambiare: non ragioniamo sull'intero _dataset_, ma immaginiamo di
poter osservare uno qualsiasi dei suoi elementi, senza sapere in anticipo quale
sarà (ricordatevi della [Legge di Franklin](#par:franklin-law)). Assumiamo
semplicemente che ogni supereroe abbia la stessa possibilità di essere
osservato rispetto a tutti gli altri. Nei capitoli
{numref}`chap:calcolo-combinatorio`&ndash;{numref}`chap:va-e-modelli-continui`
entreremo nella _Teoria della Probabilità_, che ci fornisce strumenti per
gestire in modo rigoroso l'incertezza dovuta al non sapere quale supereroe
osserveremo di verrà di volta. Ci concentreremo su degli _eventi_, cioè
affermazioni che riguardano ciò che potremmo osservare. Per esempio, sono
eventi le seguenti affermazioni:

1. osserveremo un supereroe cattivo (nell'ipotesi che l'inclinazione morale
   sia fissa, definita a priori e indicata dall'attributo `alignement` del
   _dataset_);
2. se osserviamo un supereroe Marvel e un supereroe DC, il primo è più veloce
   del secondo;
3. se osserviamo due supereroi apparsi per la prima volta nello stesso anno,
   questi hanno lo stesso indice di intelligenza;
4. se osserviamo dieci supereroi, almeno uno di essi è collocato in uno degli
   universi di _Star Wars_.

Non sappiamo se queste affermazioni siano vere o false (tecnicamente, se i
relativi eventi si verificano oppure no): dipende da cosa osserveremo. Qui
entra in gioco la _probabilità_, che assegna un numero $p \in [0, 1]$ per
quantificare questa incertezza. Senza entrare, per ora, nei dettagli,
l'incertezza è massima quando $p$ si avvicina a $\frac{1}{2}$ e diminuisce
quando $p$ tende ai suoi estremi. In particolare, più $p$ è vicino a zero, meno
possiamo ritenere veritiera l'affermazione, e se $p = 0$ siamo sicuri che sia
falsa; analogamente, man mano che $p$ si avvicina a $1$ cresce la confidenza
che l'affermazione sia vera, cosa che diventa certa quando $p = 1$. Vedremo che
questa formalizzare ci permetterà di calcolare la probabilità di eventi
complessi a partire da eventi più semplici. Ad esempio, per calcolare la
probabilità dell'ultimo evento nell'elenco precedente basta conoscere la
probabilità di osservare un supereroe proveniente da un universo _Star Wars_.

Molto spesso, gli eventi considerati fanno riferimento a una o più quantità
numeriche. Pensate, per esempio, alla resistenza di un supereroe o alla sua
altezza: ha senso chiedersi se sia massima o se rientri in un certo intervallo.
È importante sottolineare che il fatto che ogni supereroe abbia le stesse
_chance_ degli altri di essere osservato non implica affatto che lo stesso
valga per i valori che queste quantità possono assumere. Potete facilmente
rendervene conto riguardando il precedente istogramma: un peso tra $50$ e $100$
kg. è molto più frequente rispetto a uno superiore ai cento chili. Diventa
quindi necessario modellare anche queste quantità casuali. A tal fine, si
introduce il concetto di _variabile aleatoria_ e la relativa formalizzazione
matematica. Per ora, concentriamoci sul caso specifico del peso dei supereroi,
ricordando che in generale il procedimento può essere più complicato o
semplicemente diverso. L'idea alla base della formalizzazione è quella di
individuare una funzione $f$, detta _densità di probabilità_, il cui grafico
_idealizza_ l'istogramma dei valori osservati, producendo una curva continua
che ne mantiene le proprietà principali. Per il nostro esempio, queste
proprietà sono la simmetria rispetto a un asse centrale l'andamento _unimodale_
(cioè crescente fino a un valore massimo e decrescente da lì in avanti). Ci
sono infinite funzioni che esibiscono queste due proprietà, ma per motivi
troppo complessi da spiegare&mdash;ma che chiarirò più avanti&mdash;mi
concentrerò su quella definita da:

```{margin}
In questa formula, $\exp(x)$ indica l'elevamento della costante $\mathrm e$
alla potenza $x$. Preferisco questa forma a $\mathrm e^x$ per evitare la
presenza di un esponente frazionario, che risulterebbe meno leggibile.   
```
```{math}
:label: eq:weight_normal
f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2 \pi}} \;
       \mathrm{exp}\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right) \enspace,
```

```{margin}
La curva che stiamo considerando è informalmente chiamata _campana gaussiana_,
e il modello che ne deriva è detto _normale_. Come vedremo, questo modello avrà
un ruolo fondamentale nelle ultime due parti del libro.
```
dove $x$ indica un generico peso e $f(x; \mu, \sigma)$ restituisce l'altezza
corrispondente nell'istogramma idealizzato. È importante evidenziare che $f$ ha
un solo argomento, denotato da $x$, mentre $\mu \in \mathbb R$ e $\sigma \in
\mathbb R^+$ sono due _parametri_ che devono essere fissati per definire
completamente la funzione. Il punto e virgola serve proprio a distinguere
l'argomento dai parametri. Per la precisione, al variare di $\mu$ e $\sigma$
{eq}`eq:weight_normal` definisce una _famiglia_ di funzioni: ciascuna
corrisponde a una variabile aleatoria, e noi ci riferiamo a questa è una
famiglia come a un _modello_ di variabile aleatoria. Nella
{numref}`fig:normal-model` potete osservare come cambia il grafico di $f$ al
variare dei suoi parametri. Agendo sui due selettori, associati a $\mu$ e
$\sigma$, vedrete immediatamente come il grafico di $f$ si aggiorna in base
alle nuove impostazioni.

````{customfigure}
:name: fig:normal-model

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
    ax.set_xlabel(r'$x$', fontsize=12, ha='right')
    ax.set_ylabel(r'$f$', fontsize=12, rotation=0)
    label = ax.yaxis.label
    label.set_verticalalignment('bottom')
    bbox = ax.get_position()
    y_label_x = bbox.x0 + bbox.width / 2
    label.set_position((y_label_x, 1.02))


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
    
    target_element = document.getElementById("pdf-output")
    if target_element:
        target_element.innerHTML = img_html
    
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
        <label for="mean-slider">\(\mu\): </label>
        <input type="range" id="mean-slider"
               min="-5" max="5" value="0" step="0.1" />
        <span id="mean-value">0</span>
    </div>

    <div class="slider-container" style="float: right;">
        <label for="std-slider">\(\sigma\): </label>
        <input type="range" id="std-slider"
               min="0.1" max="5" value="1" step="0.1" />
        <span id="std-value">1.0</span>
    </div>

    <div id="pdf-output" class="no-mathjax"
            style="clear: both; display: flex;
            justify-content: center; margin-bottom: 2em;">
    </div>
</div>
```

Grafico della densità di probabilità descritta da {eq}`eq:weight_normal`.
````


Uno dei motivi per i quali si parla di «modello» di variabile aleatoria è
legato al fatto che è possibile scegliere i valori dei suoi parametri in modo
da _adattare_ la funzione di densità di probabilità, e più in generale la
corrispondente variabile aleatoria, a dati precedentemente osservati. Nel caso
appena visto, ciò equivale a scegliere dei valori opportuni per $\mu$ e
$\sigma$, facendo sì che il grafico di $f$ si sovrapponga qualitativamente con
quello dell'istogramma inizialmente ottenuto per il peso. Il grafico
interattivo in {numref}`fig:adapt-model` vi permette di eseguire manualmente
questa operazione, agendo sui selettori al fine di trovare un allineamento
qualitativo tra i due grafici.

````{customfigure}
:name: fig:adapt-model

```{code-block} python
:class:  toggle-code

import base64
import io

def model_plot_pdf(mu, sigma):
    x = np.linspace(0, 200, 400)
    y = (1 / (sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
    
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, density=True, alpha=0.3, color='tab:blue')
    ax.fill_between(x, 0, y, alpha=0.5, color='tab:blue')

    # Use plain text for axis labels to avoid MathJax interference
    ax.set_xlabel(r'$x$', fontsize=12, ha='right')
    ax.set_ylabel(r'$f$', fontsize=12, rotation=0)
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
    <div class="no-mathjax"
         style="display: flex; justify-content: center; margin-bottom: 2em;">
        <img src="data:image/png;base64,{img_base64}"
        alt="Model Plot" style="max-width: 100%; height: auto;">
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
        <label for="model-mean-slider">\(\mu\): </label>
        <input type="range" id="model-mean-slider"
               min="10" max="200" value="150" step="0.1" />
        <span id="model-mean-value">150</span>
    </div>

    <div class="model-slider-container" style="float: right;">
        <label for="model-std-slider">\(\sigma\): </label>
        <input type="range" id="model-std-slider"
               min="0.1" max="50" value="33" step="0.1" />
        <span id="model-std-value">33.0</span>
    </div>

    <div id="model-output"
         style="clear: both; display: flex;
                justify-content: center; margin-bottom: 2em;">
    </div>
</div>
```

Sovrapposizione del grafico della densità descritta da {eq}`eq:weight_normal`
all'istogramma di {numref}`fig:histogram`. Agendo sui selettori è possibile
trovare dei valori per i parametri che adattano il modello all'istogramma.
````

Nell'ultima parte del libro, vedremo che esistono vari metodi per determinare
automaticamente i parametri di un modello, in modo da adattarlo a un insieme di
dati. Questo è uno degli scopi della _statistica inferenziale_, illustrata nei
capitoli
{ref}`chap:statistica-inferenziale`&ndash;{ref}`chap:statistica-non-parametrica`.
Il punto di partenza è sempre un _dataset_, che in questo contesto rappresenta
un _campione_ di osservazioni effettuate su una _popolazione_ più ampia. Su
questa popolazione vogliamo fare delle ipotesi o trarre conclusioni, anche se
non possiamo osservarla nella sua interezza. In altre parole, useremo il
campione per ottenere informazioni su ciò che non sappiamo della popolazione.
Il caso più semplice &mdash; e anche quello su cui ci concentreremo
maggiormente &mdash; è quello in cui la popolazione è descritta da una variabile
aleatoria, associata a un modello che dipende da uno o più parametri
sconosciuti. L'obiettivo è quello di approssimare questi parametri, o altre
quantità che dipendono da essi. Per esempio, consideriamo la popolazione dei
supereroi nel nostro _dataset_ e supponiamo di essere interessati al loro peso
medio $p$. Se abbiamo a disposizione solo un campione di cento supereroi, il
buon senso suggerisce di usare la media del loro peso come approssimazione di
$p$. In generale, chiamiamo _stimatore_ la funzione che viene applicata al
campione per ottenere questo tipo di approssimazioni. Nel nostro esempio, lo
stimatore utilizzato è la media aritmetica dei valori del campione, detta
_media campionaria_. La {numref}`fig:statistics-variability` mostra come
variano i valori di questo stimatore in seguito all'estrazione di dieci
campioni differenti.

````{customfigure}
:name: fig:statistics-variability

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

Valore della media campionaria per il peso dei supereroi, calcolato su dieci
diversi campioni estratti dalla popolazione.
````

È natuarale che le medie campionarie ottenute dai dieci campioni siano diverse
tra loro, dal momento che ogni campione è diverso. Tuttavia, i risultati
ottenuti non variano drasticamente e tendono a concentrarsi attorno a $79$, che
è una buona approssimazione del valore  corretto per il peso medio di tutti i
supereroi (come potete verificare osservando il precedente istogramma). Ma
possiamo essere certi che la media campionaria sia davvero il miglior stimatore
possibile? E, più in generale, come possiamo valutare la bontà di uno
stimatore, considerando anche la variabilità intrinseca che abbiamo appena
evidenziato? Queste domande troveranno risposta nella parte dedicata alla
statistica inferenziale. Questa parte, in un certo senso, mi permette di
terminare il libro «chiudendo il cerchio»: sia perché mette in pratica in
maniera sinergica quello che abbiamo visto nelle parti sulla statistica
descrittiva e sul calcolo delle probabilità, sia perché permette di comprendere
più a fondo la potenza di alcuni dei concetti e degli strumenti già
incontrati&mdash;magari in modo relativamente informale&mdash;nelle parti
precedenti.

Prima però di iniziare con la statistica descrittiva, è importante rivedere
alcuni concetti fondamentali di programmazione degli elaboratori, e
soprattutto prendere dimestichezza con gli strumenti computazionali che
userò in tutto il libro. È questo lo scopo dei capitoli
{numref}`chap:intro-python` e {numref}`chap:pandas`, che aprono la trattazione.

## Esercizi

Al termine di ogni capitolo sono proposti alcuni esercizi, la cui difficoltà
di risoluzione è indicata dal numero di pallini racchuso tra parentesi.

```{exercise} •
Scaricate il _dataset_ dei supereroi dal
[repository](https://github.com/dariomalchiodi/sds) del libro e
importatelo in un qualsiasi programma che gestisce fogli elettronici (tutti
quelli più diffusi hanno la capacità di importare file CSV), in modo che ogni
colonna contenga un diverso attributo. Focalizzatevi, diciamo, sulle prime
trenta righe e considerate separatamente le varie colonne, al fine di farvi
un'idea di come varino i valori associati ai singoli attributi.
```

```{margin}
Essere _data scientist_ significa non solo combinare competenze in
probabilità, statistica e programmazione, ma anche
padroneggiare vari strumenti di _scripting_ per convertire,
adattare e ripulire i dati. Spesso l'uso di questi strumenti avviene tramite
un terminale e la relativa _shell_. A seconda dell'ambito professionale,
i dati possono essere disponibili in forma più o meno strutturata, e la loro
gestione può richiedere procedure complesse, anche tramite formati di
rappresentazione diversi dal CSV o basi di dati articolate.
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
Formulate altre domande relative al _dataset_ alle quali si possa trovare
risposta utilizzando il primo grafico interattivo. Anche in questo caso,
verbalizzate il ragionamento che va fatto per rispondere a queste domande.
```

````{exercise} •
Considerate i seguenti valori

```{math}
\{13, 8, 7, 4, 9, 8, 4, 4, 19, 2, 5, 3, 3, 1, 12 \}
```

e disegnate a mano il corrispondente istogramma, calcolando l'altezza di ogni
rettangolo come il numero di valori che ricadono nell'intervallo
corrispondente, e utilizzando i seguenti intervalli di riferimento:
$[0, 5)$, $[5, 10)$, $[10, 15)$, $[15, 20)$.
Confrontate la forma del grafico ottenuto con quanto mostrato nel testo,
mettendo in luce le principali differenze.
````

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
ricoprono tutti i valori possibili per il peso. A seconda dei casi, può
essere sensato utilizzare un numero maggiore (o minore) di siffatti intervalli,
oppure usare intervalli di ampiezza diversa.
