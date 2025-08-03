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

(sec:vista-de-conjunto)=
# Una vista de conjunto

El objetivo de este apartado es doble: por un lado, sirve para describir a
grandes rasgos el hilo lógico que está detrás de la organización de los
contenidos e introducir, de manera relativamente informal, los conceptos clave;
por otro lado, explica cómo utilizar los componentes interactivos del libro.
Como se indica en el {ref}`chap:enfoque`, en el texto haré referencia a un
{ref}`sec:installacion` conjunto de datos obtenido modificando un subconjunto
adecuado del [Superhero database](http://www.superherodb.com). Los ejemplos
harán referencia al mundo de los superhéroes, cada uno de los cuales será
descrito mediante los _atributos_ indicados en la {numref}`tab:dataset`.

```{margin}
He optado por utilizar el idioma inglés para indicar los nombres de los
atributos y sus valores correspondientes (cuando están representados como
cadenas), por coherencia con el contenido del conjunto de datos. De manera
análoga, el código Python está estructurado utilizando nombres en inglés para
variables, funciones y demás.
```

```{table} Descripción del conjunto de datos utilizado en los ejemplos.
:name: tab:dataset
:align: center
| Atributo           | Significado                | Contenido                       |
|--------------------|----------------------------|---------------------------------|
| `name`             | Identificador único        | cadena                          |
| `full_name`        | Nombre completo            | cadena                          |
| `identity`         | Identidad secreta          | cadena                          |
| `alignment`        | Tendencia moral            | `'Good'`, `'Neutral'` o `'Bad'` |
| `place_of_birth`   | Lugar de nacimiento        | cadena                          |
| `creator`          | Editorial/creador          | cadena                          |
| `universe`         | Universo                   | cadena                          |
| `first_appearance` | Año de primera aparición   | número entero                   |
| `eye_color`        | Color de ojos              | cadena                          |
| `hair_color`       | Color de cabello           | cadena                          |
| `height`           | Altura en cm               | número de coma flotante         |
| `weight`           | Peso en kg                 | número de coma flotante         |
| `strength`         | Fuerza                     | número entero (de `0` a `100`)  |
| `intelligence`     | Inteligencia               | `'Low'`, `'Moderate'`, `'Average'`, `'Good'` o `'High'`  |
| `speed`            | Velocidad                  | número entero (de `0` a `100`)  |
| `durability`       | Resistencia                | número entero (de `0` a `100`)  |
| `combat`           | Habilidad de combate       | número entero (de `0` a `100`)  |
| `powers`           | Lista de superpoderes      | cadena                          |
```


```{margin}
El extracto del conjunto de datos se genera dinámicamente, y puede ser
necesario esperar algunos segundos antes de que se visualice, reemplazando el
mensaje `Esperar a que se cargue PyScript...` [^pyscript].
```

El conjunto de datos está almacenado en el archivo `heroes.csv`, ubicado en el
directorio `data` del [repositorio](https://github.com/dariomalchiodi/sds)
asociado al libro. En el código interactivo, el archivo es accesible como
`data/heroes.csv`. En este archivo, los contenidos están representados
utilizando el formato CSV (_comma separated values_), uno de los estándares
utilizados para compartir datos de tamaño relativamente reducido: cada línea
representa un superhéroe, y en ella los valores de los atributos indicados en
la {numref}`tab:dataset` están separados por comas. La única excepción es la
primera línea del archivo, que contiene los nombres de los atributos, también
separados por comas, como se puede ver visualizando el inicio del archivo
mismo. A continuación se muestra la descripción de algunos de los atributos
correspondientes a diez superhéroes del conjunto de datos seleccionados al
azar.

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

En el {ref}`chap:pandas` veremos cómo cargar en memoria los contenidos de este
archivo y, sobre todo, cómo procesarlos. Por ahora, centrémonos en algunos
ejemplos sencillos que, por un lado, muestran cómo utilizar las partes
interactivas del libro y, por otro, ofrecen una vista de conjunto de los
conceptos que iré presentando.

Lo que sigue es un primer ejemplo de gráfico interactivo. En el diagrama
superior se representan algunos superhéroes mediante círculos en un plano
cartesiano: las coordenadas del centro indican el peso y la altura, mientras
que el radio representa la fuerza. Cada círculo está coloreado con una
tonalidad de azul elegida en función del editor, y al situarse sobre él se
visualiza automáticamente el nombre del superhéroe correspondiente. El diagrama
inferior muestra en cambio el número de superhéroes por cada editor/creador,
utilizando barras horizontales. Al seleccionar un área rectangular en el
diagrama superior es posible enfocarse en un subconjunto de superhéroes (lo que
tiene como efecto colorear de gris los círculos correspondientes a los
superhéroes excluidos); de forma automática, el diagrama inferior se actualiza
para reflejar la distribución del grupo seleccionado. Una vez realizada la
selección, esta puede moverse, y al hacer clic en cualquier punto fuera de
ella se restablece el gráfico original.

```{margin}
El gráfico que aparece aquí al lado se ha generado utilizando
[altair](https://altair-viz.github.io/), una biblioteca que permite utilizar
Python para visualizar gráficos complejos dentro de páginas web, en una forma
interactiva que se activa automáticamente en el momento en que se carga la
página. Para saber si un gráfico ha sido generado con altair, basta con
comprobar si en la esquina superior derecha hay un botón redondo con tres
puntos. Este botón activa un menú que permite, entre otras cosas, descargar el
gráfico.
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

Interactuando con el gráfico es posible realizar un _análisis exploratorio_ de
los datos, por ejemplo para responder a las siguientes preguntas.

1. ¿Cuál es el editor/creador con más superhéroes en total?
2. ¿Qué editor tiene el mayor número de superhéroes que miden menos de un
   metro?
3. ¿Qué editor tiene el mayor número de superhéroes que pesan entre 80 y 100
   kg?
4. ¿Cuál es el superhéroe más alto de todos?

```{margin}
En general, solo una pequeña parte de los gráficos que veremos serán
interactivos.
```

Obviamente, hay muchos aspectos que pueden analizarse de forma preliminar
simplemente observando el gráfico tal como fue generado (es decir, sin utilizar
los componentes interactivos), como por ejemplo los dos que se indican a
continuación.

5. ¿Existe algún tipo de relación entre el peso y la altura de los superhéroes?
6. ¿Cambia esta relación si nos enfocamos en los superhéroes de un
   editor/creador en particular?

La _estadística descriptiva_, introducida desde el
{ref}`chap:dati-e-informazione` hasta el
{ref}`chap:analizzare-le-relazioni-tra-i-dati`, proporciona herramientas que
permiten responder a preguntas como las que acabamos de considerar. En general,
su objetivo es extraer información de un conjunto de datos que describe,
globalmente o parcialmente, un conjunto de individuos de referencia, y las
técnicas utilizadas pueden ser tanto de naturaleza _cualitativa_ como
_cuantitativa_. Se habla de análisis cualitativo cuando el objetivo es
determinar la naturaleza de un fenómeno determinado (por ejemplo, para
responder a las preguntas 5 o 6 del listado anterior). Esto requiere a menudo
el uso de herramientas, como el gráfico visualizado anteriormente, cuyos
resultados deben ser interpretados, introduciendo un cierto grado de
subjetividad. En cambio, hablamos de análisis cuantitativo cuando el resultado
se expresa en una o más cantidades numéricas, que pueden compararse
objetivamente con otras cantidades (típicamente, los resultados de otros
análisis).

```{margin}
Si todo esto suena complicado, no se preocupen: los conceptos se irán aclarando
en los próximos capítulos.
```

Supongamos ahora que queremos concentrarnos, por simplicidad, en el peso de los
superhéroes: el gráfico anterior está claramente lleno de círculos, y si bien
es relativamente fácil hacerse una idea de la altura mínima y máxima, se vuelve
poco claro, por ejemplo, saber si hay más superhéroes «ligeros» que «pesados».
Para entenderlo mejor, presento a continuación un gráfico particular, llamado
_histograma_, que muestra las frecuencias con las que aparecen los distintos
valores del peso en el conjunto de datos.

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
No siempre tiene sentido usar un histograma para explorar valores en un 
conjunto de datos, como veremos en el {ref}`chap:dati-e-informazione`.
```

```{margin}
También veremos que el proceso de exploración no debe involucrar necesariamente
(ni exclusivamente) el uso de métodos gráficos, sino que puede basarse también
en herramientas cuantitativas (y típicamente así es).
```

Los histogramas se definen en detalle en el {ref}`sec:histogramas`, pero por
ahora basta saber cómo interpretar el resultado obtenido: en cada uno de los
rectángulos mostrados, la base identifica un intervalo $I$ de posibles valores
para el peso de los superhéroes, y la altura está relacionada con la fracción
de superhéroes cuyo peso se encuentra dentro de $I$ [^histogram]. El gráfico
resultante pone en evidencia algunas cosas interesantes: por ejemplo, se
observa que los superhéroes con un peso superior a 125 kg están presentes en
número mayor que aquellos con un peso inferior a cuarenta kilos. Por otro lado,
si no consideramos los pesos muy grandes o muy pequeños, emerge una simetría
aproximada en los valores respecto a un eje central, junto con el hecho de que
las alturas de los rectángulos tienden a crecer aproximadamente hasta los
$70$ kg, para luego disminuir. Esta también es una exploración de los datos,
que en este caso no requiere el uso de gráficos interactivos.

```{margin}
Si han estado atentos, habrán notado que la altura de un rectángulo no puede
ser igual al número de superhéroes con cierto peso, porque los valores
mostrados en el eje vertical no son números enteros. En este histograma, de
hecho, el número de superhéroes está relacionado con el área del rectángulo, lo
que nos permitirá pronto comparar este resultado con otro gráfico. La razón de
esta elección se explica en el {ref}`sec:histogramas`.
```

Una vez acumulado conocimiento sobre los datos disponibles, el siguiente paso
normalmente requiere _modelizar_ el proceso que los generó, y para ello es
necesario cambiar radicalmente nuestra perspectiva, imaginando no en términos
del conjunto de datos completo, sino planteándonos preguntas relativas a la
observación de cualquiera de sus elementos, o de un conjunto de elementos, bajo
la hipótesis de no saber de antemano qué observaremos (recuerden la
[Ley de Franklin](#par:franklin-law)), pero asumiendo que cada superhéroe tiene
la misma probabilidad que los demás de ser observado. Desde el
{ref}`{chap:calcolo-combinatorio}` hasta el {ref}`chap:va-e-modelli-continui`,
el libro describe la _Teoría de la Probabilidad_, proporcionando algunas
herramientas formales para manejar la incertidumbre derivada de no saber qué
será observado en cada caso. Más concretamente, nos centraremos en _sucesos_,
entendidos como afirmaciones sobre el resultado de las observaciones. Siguiendo
con los superhéroes, son sucesos, por ejemplo, las siguientes afirmaciones:

1. un superhéroe es malo (bajo la hipótesis de que cada superhéroe tenga una
   inclinación moral definida a priori, como se mide en el atributo `alignment`
   del conjunto de datos que usamos);
2. un superhéroe de Marvel es más rápido que uno de DC;
3. dos superhéroes que aparecieron por primera vez el mismo año tienen el mismo
   índice de inteligencia;
4. al menos un superhéroe en un grupo de diez pertenece a uno de los universos
   de _Star Wars_.

Claramente, no se sabe a priori si la afirmación que constituye un evento es
verdadera o falsa, porque el valor de verdad depende de las observaciones
efectivas. Por este motivo, se introduce el concepto clave de _probabilidad_,
entendida como cuantificación numérica de esta incertidumbre mediante un número
$p \in [0, 1]$. Sin entrar por ahora en detalles, cuanto más próximo esté este
número a $\frac{1}{2}$, mayor será la incertidumbre; de forma dual, cuanto más
se acerque $p$ a los extremos, menor será esta incertidumbre: cuando $p$ tiende
a cero, disminuye cada vez más la confianza en que la afirmación sea verdadera,
hasta el punto en que, cuando la probabilidad es nula, la afirmación será
definitivamente falsa; análogamente, la confianza aumenta al crecer $p$, y la
afirmación será definitivamente verdadera cuando $p = 1$. Como veremos, la
ventaja de formalizar matemáticamente el concepto de probabilidad nos
permitirá desarrollar técnicas que permiten calcular la probabilidad de eventos
complejos a partir de la de eventos simples: es el caso del punto 4 en la lista
anterior, donde la probabilidad buscada puede obtenerse una vez que se conoce
la probabilidad de que un solo héroe provenga de un universo _Star Wars_.

Muy a menudo, los eventos considerados hacen referencia a una o más cantidades
numéricas (como, por ejemplo, en los puntos 2 y 3 del listado anterior): tiene
sentido, por ejemplo, preguntarse si la resistencia de un superhéroe es máxima,
o si su altura está dentro de un cierto intervalo. Es importante destacar que
el hecho de que cada superhéroe tenga las mismas _chances_ que los demás de ser
observado no implica en absoluto que esto valga para los valores que estas
cantidades pueden tomar. Pueden darse cuenta fácilmente revisando el histograma
anterior: un peso entre $50$ y $100$ kg es mucho más frecuente que un peso
superior a los cien kilos. Por lo tanto, se vuelve importante modelar también
estas cantidades aleatorias, y en este sentido se introduce el concepto de
_variable aleatoria_ y su correspondiente formalización matemática. Sin entrar
aún en detalles, nos centraremos en el caso específico del peso de los
superhéroes, aclarando que en general el procedimiento puede ser más complicado
o simplemente diferente. La idea detrás de la formalización es identificar una
función $f$, llamada _densidad de probabilidad_, cuyo gráfico _idealiza_ el
histograma de los valores observados, respetando aún sus propiedades
fundamentales. Para el ejemplo en cuestión, podemos identificar estas
propiedades como la simetría respecto a un eje central y un comportamiento
_unimodal_ (es decir, creciente hasta un valor máximo y decreciente a partir de
ahí). Existen infinitas funciones que exhiben estas dos propiedades, pero por
razones que ahora son demasiado difíciles de justificar&mdash;pero que deberían
quedar claras una vez leído el resto del libro&mdash;vale la pena centrarse en
la función definida por:


```{margin}
En esta fórmula, $\exp(x)$ indica la elevación de la constante $\mathrm e$ a
la potencia $x$: esta forma es preferible a $\mathrm e^x$ para evitar la
presencia de un exponente fraccionario, que resultaría menos legible.
 
```
```{math}
:label: eq:weight_normal
f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2 \pi}} \;
       \mathrm{exp}\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right) \enspace,
```

donde $x$ indica un peso genérico y $f(x; \mu, \sigma)$ identifica el valor de
la altura correspondiente en el histograma idealizado. Es importante destacar
que $f$ tiene un solo argumento, denotado por $x$, mientras que
$\mu \in \mathbb{R}$ y $\sigma \in \mathbb{R}^+$ se entienden como dos
_parámetros_: la función está completamente definida solo cuando sus valores
han sido fijados. El punto y coma en la definición de $f$ sirve precisamente
para destacar el rol diferente que tienen el argumento, por un lado, y los
parámetros, por otro. Con precisión, {eq}`eq:weight_normal` define, al variar
$\mu$ y $\sigma$, una _familia_ de funciones, cada una de las cuales está
asociada a una variable aleatoria. El resultado es una familia de variables
aleatorias, a la cual se refiere como un _modelo_ de variable aleatoria.
En el diagrama interactivo que se muestra a continuación es posible ver cómo
cambia el gráfico de $f$ al variar sus dos parámetros. Actuando sobre los dos
selectores, asociados respectivamente a $\mu$ y $\sigma$, es posible cambiar
los valores de los parámetros correspondientes y simultáneamente ver cómo varía
el gráfico de $f$.

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
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
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
    img_html = '<div class="no-mathjax"><img src="data:image/png;base64,' + img_base64 + '" style="max-width: 100%; height: auto;" /></div>'
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

Una de las razones por las que se habla de «modelo» de variable aleatoria está
relacionada con el hecho de que es posible elegir los valores de sus parámetros
para _adaptar_ el gráfico de $f$, y más en general la variable aleatoria
correspondiente, a datos previamente observados. En el caso recién visto, esto
equivale a elegir valores adecuados para $\mu$ y $\sigma$, de modo que el
gráfico de $f$ se superponga cualitativamente con el del histograma
inicialmente obtenido para el peso. El siguiente diagrama interactivo permite
realizar esta operación manualmente: por lo tanto, pueden actuar sobre los
selectores para obtener una buena superposición entre el histograma y la
función de densidad de probabilidad.

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
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
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

En la última parte del libro, exploraremos varios métodos que permiten
determinar automáticamente los parámetros de un modelo con el fin de ajustarlo
a un conjunto de datos. Este es uno de los objetivos de la _estadística
inferencial_, que se ilustra desde el {ref}`chap:inferential_statistics` hasta
el {ref}`chap:statistica-non-parametrica`. El punto de partida es siempre un
conjunto de datos, que en este contexto representa una _muestra_ de
observaciones tomadas de una _población_ más grande. Nuestro objetivo es
formular hipótesis o sacar conclusiones sobre esa población, aunque no podamos
observarla en su totalidad. En otras palabras, usaremos la muestra para
aprender algo sobre lo que no sabemos de la población. El caso más
simple&mdash;y también el que más nos interesará&mdash;es aquel en el que la
población está descrita por una variable aleatoria, asociada a un modelo que
depende de uno o más parámetros desconocidos. El objetivo es aproximar estos
parámetros, u otras cantidades que dependen de ellos. Por ejemplo, imaginemos
que la población está formada por todos los superhéroes de nuestro conjunto de
datos, y que la cantidad que nos interesa es su peso medio $p$. Si solo
tenemos una muestra de cien superhéroes, lo razonable es utilizar el peso
medio de las observaciones como una aproximación de $p$. En general, usamos el
término _estimador_ para referirnos a la función que se aplica a la muestra
para obtener este tipo de aproximaciones. En nuestro ejemplo, el estimador es
simplemente la media aritmética de los valores de la muestra &mdash; lo que
llamamos la _media muestral_. La tabla siguiente muestra cómo varían los
valores de este estimador en diez muestras distintas.


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

Como puedes ver, las medias muestrales varían de una muestra a otra, lo cual es
esperable &mdash; al fin y al cabo, cada muestra es diferente. Aun así, los
resultados no están completamente dispersos: tienden a agruparse alrededor de
$79$, que es una estimación bastante buena del valor medio real del peso de
todos los superhéroes (como puedes comprobar mirando el histograma anterior).
Pero, &iquest;podemos estar seguros de que la media muestral es realmente el
mejor estimador posible? Y, más en general, &iquest;cómo evaluamos qué tan
bueno es un estimador, teniendo en cuenta también la variabilidad que acabamos
de observar? Responderemos a este tipo de preguntas en la parte dedicada a la
estadística inferencial. En cierto sentido, esta sección me permite cerrar el
libro «cerrando el círculo»: no solo conecta lo que hemos visto sobre estadística
descriptiva y teoría de la probabilidad, sino que también nos permite apreciar
mejor el poder de algunos conceptos y herramientas que ya encontramos &mdash;
tal vez de manera más informal &mdash; en las partes anteriores.

Antes, sin embargo, de comenzar con la estadística descriptiva, es importante
revisar algunos conceptos calve de programación, y sobre todo familiarizarse
con las herramientas computacionales que usaré a lo largo del libro. Este es
justamente el propósito del {ref}`chap:intro-python` y del {ref}`chap:pandas`,
que abren el tratamiento.

## Ejercicios

Al final de cada párrafo se proponen algunos ejercicios, cuya dificultad de
resolución está indicada por el número de puntos encerrados entre paréntesis.

```{exercise} •
Descarguen el conjunto de datos de superhéroes desde el
[repositorio](https://github.com/dariomalchiodi/sds) del libro e impórtenlo en
cualquier programa que maneje hojas de cálculo (todos los más comunes tienen la
capacidad de importar archivos CSV), de modo que cada columna contenga un
atributo diferente. Concéntrense, digamos, en las primeras treinta filas y
consideren por separado las diversas columnas, para hacerse una idea de cómo
varían los valores asociados a los atributos individuales.
```

```{margin}
Ser _data scientist_ significa no solo saber conjugar las competencias en
probabilidad, estadística y programación informática, sino también
dominar varias herramientas de _scripting_ que permiten convertir,
adaptar y limpiar los datos: muy a menudo, el uso de estas herramientas es
mediado por una terminal y su correspondiente _shell_.
```

```{exercise} •••
Reconsideren el ejercicio anterior, observando el contenido de cada columna
del archivo CSV sin utilizar un procesador de hojas de cálculo, sino usando
solo una terminal y los comandos de _shell_.
```

```{exercise} ••
Basándose en la idea que se han hecho sobre el conjunto de datos de superhéroes
resolviendo los ejercicios anteriores, intenten dividir los atributos en
grupos homogéneos basándose no en el tipo de dato que se usa para representar
los valores correspondientes (indicado en la columna «Contenido» de la
{numref}`tab:dataset`), sino en la _naturaleza_ de los propios atributos.
```

```{exercise} •
Respondan las preguntas numeradas del 1 al 4 en la lista que sigue al primer
gráfico interactivo.
```

```{exercise} ••
Respondan las preguntas 5 y 6 en la lista que sigue al primer gráfico
interactivo. Verbalicen el razonamiento que hicieron y escríbanlo.
```

```{exercise} ••
Piensen en otras preguntas relacionadas con el conjunto de datos a las que se
pueda encontrar respuesta usando el primer gráfico interactivo. También en este
caso, verbalicen el razonamiento que se debe hacer para responder a estas
preguntas.
```

```{exercise} •
Consideren los siguientes valores

$$ \\{13, 8, 7, 4, 9, 8, 4, 4, 19, 2, 5, 3, 3, 1, 12 \\} $$

y dibujen a mano el correspondiente histograma, calculando la altura de cada
rectángulo como el número de valores que caen en el intervalo
correspondiente, y usando los siguientes intervalos de referencia:
$[0, 5)$, $[5, 10)$, $[10, 15)$, $[15, 20)$.
Comparen la forma del gráfico obtenido con lo mostrado en el texto,
destacando las principales diferencias.
```

```{exercise} •
Escriban diez posibles sucesos que se refieran al conjunto de datos de
superhéroes.
```

```{exercise} ••
Escriban un suceso cuya probabilidad sea igual a cero. Luego escriban un
suceso con probabilidad $1$.
```

```{exercise} ••
Fijen $\mu = \sigma = 1$ y realicen el estudio de la función descrita en
{eq}`eq:weight_normal`, dibujando a mano su gráfico y comprobando que tenga una
forma similar al resultado que se muestra en el segundo diagrama interactivo.
```

```{exercise} •
Basándose en el resultado del ejercicio anterior, y teniendo en cuenta lo que
han experimentado trabajando con el segundo gráfico interactivo, ¿qué rol
juegan los parámetros $\mu$ y $\sigma$ en el gráfico de $f$ definido en
{eq}`eq:weight_normal`?
```

```{exercise} •
Usando el segundo gráfico interactivo, determinen valores para $\mu$ y
$\sigma$ que permitan superponer de modo razonable el gráfico de $f$
al histograma del peso de los superhéroes.

```{exercise} ••
Escribid el razonamiento que os llevó a convenceros de que $79$ es una buena
aproximación del valor medio del peso de los superhéroes.
```

[^histogram]: Es posible elegir los intervalos que definen las bases de los
rectángulos con cierto grado de libertad. Para simplificar, el histograma en
el texto se generó considerando veinticinco intervalos equiespaciados que
cubren todos los valores posibles para el peso, pero según los casos puede
ser sensato utilizar un número mayor (o menor) de dichos intervalos,
o bien considerar un conjunto de intervalos de diferentes anchos.

