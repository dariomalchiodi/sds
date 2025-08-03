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

(sec:apercu-general)=
# Vue d’ensemble

Ce chapitre a un double objectif : d’un côté, il sert à décrire à grands traits
la logique suivie dans l’organisation des contenus et à introduire, de façon
relativement informelle, les concepts fondamentaux ; de l’autre, il explique
comment utiliser les composants interactifs du livre. Comme indiqué dans le
{ref}`chap:approche`, je vais faire référence à un jeu de données obtenu en
modifiant un sous-ensemble approprié du
[Superhero database](http://www.superherodb.com). Les exemples se rapporteront
donc à l’univers des super-héros, chacun étant décrit par les _attributs_
listés dans la {numref}`tab:dataset`.

```{margin}
J’ai choisi d’utiliser l’anglais pour indiquer les noms des attributs et les
valeurs correspondantes (lorsqu’elles sont exprimées sous forme de chaînes),
afin de rester cohérent avec le contenu du dataset. De la même manière, le code
Python suivra une convention de nommage en anglais pour les variables,
fonctions, etc.
```

```{table} Description du jeu de données utilisé dans les exemples.
:name: tab:dataset
:align: center
| Attribut            | Signification             | Contenu                                                  |
|---------------------|---------------------------|----------------------------------------------------------|
| `name`              | identifiant unique        | chaîne                                     |
| `full_name`         | nom complet               | chaîne                                     |
| `identity`          | identité secrète          | chaîne                                     |
| `alignment`         | alignement moral          | `'Good'`, `'Neutral'` ou `'Bad'`                         |
| `place_of_birth`    | lieu de naissance         | chaîne                                     |
| `creator`           | éditeur/créateur          | chaîne                                     |
| `universe`          | univers                   | chaîne                                     |
| `first_appearance`  | année de première apparition | entier                                                 |
| `eye_color`         | couleur des yeux          | chaîne                                     |
| `hair_color`        | couleur des cheveux       | chaîne                                     |
| `height`            | taille en cm              | nombre flottant                              |
| `weight`            | poids en kg               | nombre flottante                             |
| `strength`          | force                     | entier (de `0` à `100`)                                  |
| `intelligence`      | intelligence              | `'Low'`, `'Moderate'`, `'Average'`, `'Good'` ou `'High'` |
| `speed`             | vitesse                   | entier (de `0` à `100`)                                  |
| `durability`        | endurance                 | entier (de `0` à `100`)                                  |
| `combat`            | aptitude au combat        | entier (de `0` à `100`)                                  |
| `powers`            | liste des super-pouvoirs  | chaîne                                     |
```

```{margin}
L’extrait du jeu de données est généré dynamiquement, et il peut être
nécessaire d’attendre quelques secondes avant qu’il n’apparaisse à l’écran,
remplaçant le message `Attendre le chargement de PyScript`. Il en va de même
pour tous les points où le navigateur exécute du code Python.
```

Le jeu de données est stocké dans le fichier `heroes.csv`, situé dans le
répertoire `data` du [répertoire GitHub](https://github.com/dariomalchiodi/sds)
associé au livre. Dans le code interactif, le fichier est accessible via le
chemin `data/heroes.csv`. Le contenu de ce fichier est représenté au format CSV
(_comma separated values_), un des standards utilisés pour l’échange de données
de taille modérée : chaque ligne représente un super-héros, et les valeurs des
attributs listés dans la {numref}`tab:dataset` y sont séparées par des
virgules. La seule exception est la première ligne, qui contient les noms des
attributs, eux aussi séparés par des virgules, comme on peut le voir en
affichant le début du fichier.

Ci-dessous, vous pouvez voir la description de certains des attributs pour dix
super-héros du jeu de données, choisis au hasard.  


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

Dans le {ref}`chap:pandas`, nous verrons comment charger en mémoire le contenu
de ce fichier et, surtout, comment le manipuler. Pour l’instant,
concentrons-nous sur quelques exemples simples qui, d’un côté, montrent comment
utiliser les parties interactives du livre, et de l’autre, donnent un aperçu
des concepts que je vais présenter.

Ce qui suit est un premier exemple de graphique interactif. Dans le diagramme
du haut, certains super-héros sont représentés à l’aide de cercles placés sur
un plan cartésien : les coordonnées du centre indiquent le poids et la taille,
tandis que le rayon représente la force. Chaque cercle est coloré avec une
nuance de bleu choisie en fonction de l’éditeur, et en passant la souris
au-dessus, le nom du super-héros correspondant s’affiche automatiquement. Le
diagramme du bas montre quant à lui le nombre de super-héros par
éditeur/créateur, à l’aide de barres horizontales. En sélectionnant une zone
rectangulaire dans le diagramme supérieur, on peut se concentrer sur un
sous-ensemble de super-héros (ce qui grise automatiquement les cercles des
super-héros exclus) : le diagramme inférieur est alors mis à jour
automatiquement pour refléter la distribution du groupe sélectionné. Une fois
la sélection effectuée, on peut la déplacer, et un simple clic en dehors de
cette zone permet de rétablir le graphique initial.

```{margin}
Le graphique ci-contre a été généré avec
[altair](https://altair-viz.github.io/), un paquet qui permet d’utiliser Python
pour créer des visualisations complexes dans des pages web, avec un
comportement interactif automatiquement activé dès le chargement de la page.
Pour savoir si un graphique a été généré avec altair, il suffit de vérifier si
un petit bouton rond contenant trois points est visible en haut à droite. Ce
bouton ouvre un menu qui permet, entre autres, de télécharger le graphique.
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

En interagissant avec le graphique, on peut effectuer une _analyse
exploratoire_ des données, par exemple pour répondre aux questions suivantes.

1. Quel est l’éditeur/créateur qui compte le plus grand nombre de super-héros ?
2. Quel éditeur compte le plus de super-héros mesurant moins d’un mètre ?
3. Quel éditeur a le plus de super-héros pesant entre 80 et 100 kg ?
4. Quel est le super-héros le plus grand de tous ?

```{margin}
En général, seule une petite partie des graphiques que nous verrons seront
interactifs.
```

Il y a évidemment de nombreux aspects que l’on peut analyser de manière
préliminaire simplement en observant le graphique tel qu’il a été généré
(c’est-à-dire sans utiliser les composants interactifs), comme par exemple les
deux suivants.

5. Existe-t-il une relation quelconque entre le poids et la taille des
   super-héros ?
6. Cette relation change-t-elle si l’on se concentre sur les super-héros d’un
   éditeur/créateur en particulier ?

La _statistique descriptive_, introduite du {ref}`chap:dati-e-informazione` au
{ref}`chap:analizzare-le-relazioni-tra-i-dati`, fournit des outils permettant
de répondre à des questions comme celles que l’on vient de considérer. En
général, l’objectif est d’extraire de l’information à partir d’un jeu de
données qui décrit, totalement ou partiellement, un ensemble d’individus de
référence. Les techniques employées peuvent être de nature _qualitative_ ou
_quantitative_. On parle d’analyse qualitative lorsque l’objectif est de
comprendre la nature d’un certain phénomène (comme dans les questions 5 ou 6
ci-dessus). Cela implique souvent l’utilisation d’outils, comme le graphique
présenté précédemment, dont les résultats doivent être interprétés, ce qui
introduit une certaine part de subjectivité. On parle au contraire d’analyse
quantitative lorsque le résultat s’exprime par une ou plusieurs valeurs
numériques, que l’on peut alors comparer objectivement à d’autres (typiquement,
les résultats d’autres analyses).

```{margin}
Si tout cela vous semble compliqué, ne vous inquiétez pas : les concepts
deviendront plus clairs dans les chapitres suivants.
```

Supposons maintenant que nous voulions nous concentrer, pour faire simple, sur
le poids des super-héros : le graphique précédent est clairement chargé en
cercles, et même s’il est relativement facile d’estimer les tailles minimale et
maximale, il est plus difficile de déterminer, par exemple, s’il y a plus de
super-héros « légers » que « lourds ». Pour mieux comprendre cela, voici un
graphique particulier, appelé _histogramme_, qui met en évidence les fréquences
auxquelles apparaissent les différentes valeurs de poids dans le jeu de données.

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
Il n’est pas toujours pertinent d’utiliser un histogramme pour explorer les
valeurs d’un jeu de données, comme nous le verrons dans le
{ref}`chap:dati-e-informazione`.
```

```{margin}
Nous verrons également que l’exploration des données ne passe pas
nécessairement (ou exclusivement) par des méthodes graphiques, mais peut aussi,
et souvent doit, reposer sur des outils quantitatifs.
```

Les histogrammes sont définis en détail dans le {ref}`sec:histogrammes`, mais
pour le moment, il suffit de savoir comment en lire le résultat : dans chacun
des rectangles affichés, la base identifie un intervalle $I$ de valeurs
possibles pour le poids des super-héros, et la hauteur est liée à la fraction
de super-héros dont le poids appartient à $I$ [^histogramme]. Le graphique
obtenu met en lumière quelques éléments intéressants : par exemple, on remarque
que les super-héros pesant plus de 125 kg sont plus nombreux que ceux pesant
moins de quarante kilos. D’un autre côté, si l’on exclut les poids très grands
ou très petits, on observe une certaine symétrie approximative des valeurs par
rapport à un axe central, et les hauteurs des rectangles ont tendance à
augmenter jusqu’à environ $70$ kg, puis à diminuer. C’est aussi une forme
d’exploration des données, qui ici ne nécessite pas de graphiques interactifs.

```{margin}
Si vous êtes attentif, vous aurez remarqué que la hauteur d’un rectangle ne
peut pas correspondre simplement au nombre de super-héros ayant un certain
poids, car les valeurs indiquées sur l’axe des ordonnées ne sont pas entières.
Dans cet histogramme, en effet, le nombre de super-héros est lié à l’aire du
rectangle, ce qui nous permettra de comparer ce résultat à un autre graphique
un peu plus loin. Le choix de cette représentation est détaillé dans le
{ref}`sec:histogrammes`.
```

Une fois que l’on a acquis une certaine connaissance sur les données
disponibles, l’étape suivante consiste généralement à _modéliser_ le processus
qui les a générées. Pour cela, il faut changer radicalement de perspective : il
ne s’agit plus de considérer le jeu de données dans son ensemble, mais plutôt
de se poser des questions relatives à l’observation d’un de ses éléments (ou
d’un groupe d’éléments), sans savoir à l’avance ce que l’on va observer
(rappelez-vous la [Loi de Franklin](#sec:franklin-law)), tout en supposant que
chaque super-héros a autant de chances que les autres d’être observé. À partir
du {ref}`{chap:calcolo-combinatorio}` et jusqu’au
{ref}`chap:va-e-modelli-continui`, ce livre introduit la _Théorie des
Probabilités_, en fournissant des outils formels pour gérer l’incertitude liée
à cette absence de connaissance préalable sur ce qui sera observé.

Plus précisément, nous nous concentrerons sur les _événements_, entendus comme
des affirmations portant sur les résultats des observations. En restant dans le
thème des super-héros, on peut par exemple considérer les événements suivants :

1. un super-héros est mauvais (en supposant que chaque super-héros ait une
   inclination morale bien définie à l’avance, comme mesuré par l’attribut
   `alignment` dans notre _dataset_) ;
2. un super-héros Marvel est plus rapide qu’un super-héros DC ;
3. deux super-héros apparus pour la première fois la même année ont le même
   indice d’intelligence ;
4. au moins un super-héros dans un groupe de dix appartient à l’un des univers
   de _Star Wars_.

Bien entendu, on ne sait pas à l’avance si ces affirmations sont vraies ou
fausses, car leur valeur dépend des observations effectives. C’est pourquoi on
introduit la notion centrale de _probabilité_, entendue comme une
quantification numérique de cette incertitude, au moyen d’un nombre
$p \in [0, 1]$. Sans entrer dans les détails pour l’instant, plus ce nombre est
proche de $\frac{1}{2}$, plus l’incertitude est grande ; inversement, plus $p$
se rapproche de l’un des deux extrêmes, plus l’incertitude diminue : quand $p$
tend vers zéro, on est de moins en moins enclin à croire que l’affirmation est
vraie, et si la probabilité est nulle, elle est forcément fausse ; à l’inverse,
plus $p$ croît, plus la confiance en la plausibilité de l’affirmation augmente,
et l’affirmation est sûrement vraie lorsque $p = 1$. Comme nous le verrons, le
fait de formaliser mathématiquement le concept de probabilité nous permettra de
développer des techniques qui permettent de calculer la probabilité
d’événements complexes à partir de celle d’événements plus simples : c’est le
cas du point 4 ci-dessus, où la probabilité cherchée peut être obtenue dès que
l’on connaît la probabilité qu’un héros donné provienne d’un univers
_Star Wars_.

Très souvent, les événements que l’on considère font référence à une ou
plusieurs quantités numériques (comme dans les exemples aux points 2 et 3
ci-dessus) : on peut par exemple se demander si la résistance d’un super-héros
est maximale, ou si sa taille se trouve dans un certain intervalle. Il est
important de souligner que le fait que chaque super-héros ait la même _chance_
d’être observé que les autres ne signifie absolument pas que cela vaut aussi
pour les valeurs que peuvent prendre ces quantités. Vous pouvez facilement vous
en rendre compte en regardant à nouveau l’histogramme précédent : un poids
entre $50$ et $100$ kg est beaucoup plus fréquent qu’un poids supérieur à cent
kilos. Il devient donc important de modéliser aussi ces quantités aléatoires,
ce qui nous conduit à introduire la notion de _variable aléatoire_ et sa
formalisation mathématique. Sans entrer encore dans les détails,
concentrons-nous sur le cas spécifique du poids des super-héros, en gardant
bien à l’esprit que, en général, la démarche peut être plus complexe ou
simplement différente. L’idée à la base de cette formalisation est de définir
une fonction $f$, appelée _densité de probabilité_, dont le graphique
_idéalise_ l’histogramme des valeurs observées, tout en respectant ses
propriétés fondamentales. Pour l’exemple qui nous intéresse ici, on peut
résumer ces propriétés comme suit : symétrie par rapport à un axe central et
comportement _unimodal_ (c’est-à-dire croissant jusqu’à un maximum, puis
décroissant). Il existe une infinité de fonctions vérifiant ces deux
propriétés, mais pour des raisons qui seraient trop complexes à justifier à ce
stade&mdash;mais qui devraient devenir claires à la lecture du reste du
livre&mdash;, il vaut la peine de se concentrer sur celle définie par :

```{margin}
Dans cette formule, $\exp(x)$ désigne l’exponentielle de la constante
$\mathrm e$ à la puissance $x$ : cette notation est préférée à $\mathrm e^x$
afin d’éviter les exposants fractionnaires, moins lisibles.
```

```{math}
:label: eq:weight_normal
f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2 \pi}} \;
       \mathrm{exp}\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right) \enspace,
```

où $x$ représente un poids quelconque et $f(x; \mu, \sigma)$ donne la valeur de
la hauteur correspondante dans l’histogramme idéalisé. Il est important de
souligner que $f$ a un seul argument, noté $x$, tandis que $\mu \in \mathbb R$
et $\sigma \in \mathbb R^+$ doivent être considérés comme deux _paramètres_ :
la fonction est entièrement définie uniquement lorsque leurs valeurs ont été
fixées. Le point-virgule dans la définition de $f$ sert justement à mettre en
évidence le rôle différent de l’argument d’une part, et des paramètres d’autre
part. Plus précisément, l’{eq}`eq:weight_normal` définit, en faisant varier
$\mu$ et $\sigma$, une _famille_ de fonctions, chacune étant associée à une
variable aléatoire. Le résultat est une famille de variables aléatoires, à
laquelle on fait référence comme à un _modèle_ de variable aléatoire. Dans le
diagramme interactif ci-dessous, vous pouvez voir comment le graphique de $f$
évolue en fonction de ses deux paramètres. En manipulant les deux curseurs,
associés respectivement à $\mu$ et $\sigma$, il est possible de modifier les
valeurs des paramètres et de visualiser en temps réel la manière dont la courbe
de $f$ change.

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

L’une des raisons pour lesquelles on parle de « modèle » de variable aléatoire
réside dans le fait qu’il est possible de choisir les valeurs de ses paramètres
de manière à _adapter_ le graphique de $f$, et plus généralement la variable
aléatoire correspondante, à des données précédemment observées. Dans le cas que
nous venons de voir, cela revient à choisir des valeurs appropriées pour $\mu$
et $\sigma$, de façon à ce que le graphique de $f$ se superpose de façon
qualitative à celui de l’histogramme initialement obtenu pour le poids. Le
graphique interactif suivant permet de réaliser manuellement cette opération,
en affichant à la fois l’histogramme et la courbe (variable) de $f$. Vous
pouvez donc manipuler les curseurs afin d’obtenir une bonne superposition.

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

Dans la dernière partie du livre, nous verrons qu’il existe plusieurs méthodes
permettant de déterminer automatiquement les paramètres d’un modèle afin de
l’adapter à un ensemble de données. C’est là, entre autres, l’objectif de la
_statistique inférentielle_, présentée du {ref}`chap:inferential_statistics` au
{ref}`chap:statistica-non-parametrica`. Le point de départ est toujours un jeu
de données, qui représente ici un _échantillon_ d’observations effectuées
sur une _population_ plus large. Notre objectif est de formuler des hypothèses
ou de tirer des conclusions sur cette population &mdash; même si nous ne
pouvons pas l'observer directement dans son ensemble. En d'autres termes, nous
allons utiliser l'échantillon pour apprendre quelque chose sur ce que nous
ignorons dans la population. Le cas le plus simple&mdash;et celui que nous
étudierons plus en détail&mdash;est celui où la population est décrite par une
variable aléatoire associée à un modèle dont un ou plusieurs paramètres sont
inconnus. Le but est et d'approximer ces paramètres, ou d’autres quantités
qui en dépendent. Par exemple, imaginons que la population soit constituée de
tous les super-héros présents dans notre jeu de données, et que la quantité qui
nous intéresse soit leur poids moyen $p$. Si nous ne disposons que d'un
échantillon de cent super-héros, le bon sens nous pousse à utiliser la moyenne
de leur poids comme approximation de $p$. De manière générale, on utilise le
terme _estimateur_ pour désigner la fonction qu'on applique à l'échantillon
pour produire ce genre d'approximation. Dans notre exemple, l'estimateur
utilisé est simplement la moyenne arithmétique des valeurs de l'échantillon
&mdash; ce qu'on appelle la _moyenne empirique_. Le tableau ci-dessous
montre comment les valeurs de cet estimateur varient pour dix échantillons
tirés au hasard.

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

Comme on peut le voir, les moyennes empiriques varient d'un échantillon à
l'autre, ce qui est tout à fait normal &mdash; chaque échantillon étant
différent. Cela dit, les résultats ne varient pas de manière extrême : ils ont
tendance à se regrouper autour de $79$, qui est une bonne estimation du vrai
poids moyen de tous les super-héros (comme vous pouvez le vérifier en
observant l'histogramme précédent). Mais peut-on vraiment être sûrs que la
moyenne échantillonnale est le meilleur estimateur possible ? Et plus
généralement, comment évaluer si un estimateur est « bon », en tenant compte
de la variabilité qu'on vient de constater ? Nous répondrons à ce genre de
questions dans la partie consacrée à la statistique inférentielle. D'une
certaine manière, cette partie me permet de conclure le livre en « bouclant la
boucle » : à la fois parce qu’elle met en &oelig;uvre de manière synergique ce
que nous avons vu dans les parties sur la statistique descriptive et la théorie
des probabilités, et parce qu’elle permet aussi de mieux comprendre toute la
puissance de certains concepts et outils que nous avions rencontrés auparavant
&mdash; parfois de manière relativement informelle.

Mais avant de commencer avec la statistique descriptive, il est important de
revoir certains concepts de base liés à la programmation, et surtout de se
familiariser avec les outils computationnels que j’utiliserai tout au long du
livre. C’est justement l’objectif du {ref}`chap:intro-python` et du
{ref}`chap:pandas`, qui ouvrent notre parcours.

## Exercices

À la fin de chaque paragraphe, quelques exercices sont proposés, dont le niveau
de difficulté est indiqué par le nombre de points entre parenthèses.

```{exercise} •
Téléchargez le jeu de données des super-héros depuis le
[dépôt](https://github.com/dariomalchiodi/sds) du livre et importez-le dans
n’importe quel programme de tableur (tous les plus courants peuvent importer
des fichiers CSV), de façon à ce que chaque colonne contienne un attribut
différent. Concentrez-vous, disons, sur les trente premières lignes et examinez
les différentes colonnes séparément, pour vous faire une idée de la manière
dont varient les valeurs associées aux différents attributs.
```

```{margin}
Être _data scientist_ ne signifie pas seulement savoir combiner les compétences
en probabilités, statistiques et programmation, mais aussi maîtriser différents
outils de _scripting_ permettant de convertir, adapter et nettoyer les
données : très souvent, l’utilisation de ces outils passe par un terminal et
une _shell_.
```

```{exercise} •••
Reprenez l’exercice précédent, en inspectant le contenu de chaque colonne du
fichier CSV sans utiliser de tableur, mais uniquement un terminal et des
commandes _shell_.
```

```{exercise} ••
Sur la base de l’idée que vous vous êtes faite du jeu de données des
super-héros en résolvant les exercices précédents, essayez de regrouper les
attributs par similarité, non pas en fonction du type de données utilisé pour
représenter les valeurs (indiqué dans la colonne « Contenu » de la
{numref}`tab:dataset`), mais selon la _nature_ des attributs eux-mêmes.
```

```{exercise} •
Répondez aux questions numérotées de 1 à 4 dans la liste qui suit le premier
graphique interactif.
```

```{exercise} ••
Répondez aux questions 5 et 6 dans la liste qui suit le premier graphique
interactif. Rédigez le raisonnement que vous avez suivi et mettez-le par écrit.
```

```{exercise} ••
Formulez d’autres questions relatives au jeu de données auxquelles il serait
possible de répondre en utilisant le premier graphique interactif. Là aussi,
expliquez par écrit le raisonnement qui permet d’y répondre.
```

```{exercise} •
Considérez les valeurs suivantes :

$$ \\{13, 8, 7, 4, 9, 8, 4, 4, 19, 2, 5, 3, 3, 1, 12 \\} $$

et tracez à la main l’histogramme correspondant, en calculant la hauteur de
chaque rectangle comme le nombre de valeurs qui tombent dans l’intervalle
correspondant, et en utilisant les intervalles suivants :
$[0, 5)$, $[5, 10)$, $[10, 15)$, $[15, 20)$.
Comparez la forme du graphique obtenu à celle montrée dans le texte, en mettant
en évidence les principales différences.
```

```{exercise} •
Écrivez dix événements possibles concernant le jeu de données des super-héros.
```

```{exercise} ••
Écrivez un événement dont la probabilité est égale à zéro. Puis un autre dont
la probabilité est égale à $1$.
```

```{exercise} ••
Fixez $\mu = \sigma = 1$ et étudiez la fonction décrite dans
{eq}`eq:weight_normal`, en dessinant à la main le graphique correspondant et en
vérifiant que celui-ci a la même forme que celle affichée dans le second
graphique interactif.
```

```{exercise} •
Sur la base du résultat de l’exercice précédent et en tenant compte de ce que
vous avez expérimenté avec le second graphique interactif, quel est le rôle des
paramètres $\mu$ et $\sigma$ sur le graphique de $f$ défini dans
{eq}`eq:weight_normal` ?
```

```{exercise} •
À l’aide du second graphique interactif, trouvez des valeurs pour $\mu$ et
$\sigma$ qui permettent de superposer de manière raisonnable le graphique de
$f$ à l’histogramme du poids des super-héros.
```

```{exercise} ••
Expliquez par écrit le raisonnement qui vous a permis de conclure que $79$ est
une bonne approximation du poids moyen des super-héros.
```

[^histogramme]: Il est possible de choisir librement les intervalles définissant
les bases des rectangles. Pour simplifier, l’histogramme dans le texte a été
généré en considérant vingt-cinq intervalles de largeur égale couvrant toutes
les valeurs possibles du poids, mais selon les cas, il peut être pertinent
d’utiliser un nombre plus (ou moins) élevé d’intervalles, ou encore de
considérer un ensemble d’intervalles de largeurs différentes.

