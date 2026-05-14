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

(sec_apercu-general)=
# Vue d'ensemble

Le but de ce chapitre est double : d’une part, il vise à décrire la logique
selon laquelle j’ai organisé les contenus et à introduire les concepts clés de
manière relativement informelle. D’autre part, il explique comment utiliser les
composants interactifs du livre. Comme indiqué dans {ref}`chap_approche`, tout
au long du texte, je ferai référence à un jeu de données obtenu en modifiant
un sous-ensemble du {extlink}`Superhero database <http://www.superherodb.com>`.
Les exemples s’appuient donc sur l’univers des super-héros, chacun étant décrit
au moyen des _attributs_ indiqués dans la {numref}`tab_dataset`.

```{margin}
J’ai choisi d’utiliser l’anglais pour désigner les noms des attributs ainsi que
les valeurs correspondantes (lorsqu’elles sont exprimées sous forme de chaînes
de caractères), afin de rester cohérent avec le contenu du jeu de données. De
la même manière, le code Python suivra une convention de nommage en anglais
pour les variables, les fonctions, etc.
```
```{table} Description du jeu de données utilisé dans les exemples.
:name: tab_dataset
:align: center
| Attribut           | Signification            | Contenu                                                  |
|--------------------|--------------------------|----------------------------------------------------------|
| `name`             | identifiant unique       | chaîne de caractères                                     |
| `full_name`        | nom complet              | chaîne de caractères                                     |
| `identity`         | identité secrète         | chaîne de caractères                                     |
| `alignment`        | alignement moral         | `'Good'`, `'Neutral'` ou `'Bad'`                         |
| `place_of_birth`   | lieu de naissance        | chaîne de caractères                                     |
| `creator`          | éditeur/créateur         | chaîne de caractères                                     |
| `universe`         | univers                  | chaîne de caractères                                     |
| `first_appearance` | année de première apparition | entier                                               |
| `eye_color`        | couleur des yeux         | chaîne de caractères                                     |
| `hair_color`       | couleur des cheveux      | chaîne de caractères                                     |
| `height`           | taille en cm             | nombre à virgule flottante                               |
| `weight`           | poids en kg              | nombre à virgule flottante                               |
| `strength`         | force                    | entier (de `0` à `100`)                                  |
| `intelligence`     | intelligence             | `'Low'`, `'Moderate'`, `'Average'`, `'Good'`, ou `'High'`|
| `speed`            | vitesse                  | entier (de `0` à `100`)                                  |
| `durability`       | endurance                | entier (de `0` à `100`)                                  |
| `combat`           | aptitude au combat       | entier (de `0` à `100`)                                  |
| `power`            | liste des super-pouvoirs | chaîne de caractères                                     |
```

```{margin}
L’extrait du jeu de données est généré dynamiquement, et il peut être
nécessaire d’attendre quelques secondes avant qu’il n’apparaisse, en
remplaçant le message `Please wait, loading PyScript...`. Le même comportement
se produit partout où le navigateur exécute du code Python.
```

Le jeu de données est stocké dans le fichier `heroes.csv`, situé dans le
répertoire `data` du {extlink}`dépôt GitHub
<https://github.com/dariomalchiodi/sds>` associé au livre. Dans le code
interactif, ce fichier est accessible sous le chemin `data/heroes.csv`. Son
contenu est représenté au format CSV (_comma separated values_), un format
standard couramment utilisé pour partager des jeux de données de taille
relativement modeste : chaque ligne correspond à un super-héros, et les valeurs
des attributs de la {numref}`tab_dataset` y sont séparées par des virgules. La
seule exception est la première ligne du fichier, qui contient les noms des
attributs, eux aussi séparés par des virgules. La {numref}`tab_dataset-excerpt`
montre un extrait du jeu de données, en affichant les valeurs de certains
attributs pour dix super-héros choisis aléatoirement.


````{customtable}
:name: tab_dataset-excerpt
:class: full-width, left-align


```{interactive-code} python
:height: 300px
:class: toggle-code

import pandas as pd

heroes = pd.read_csv('data/heroes.csv', index_col=0)
    
source = heroes.sample(10).loc[:,'name':'combat']
source.index.name = None
source

```

Extrait du jeu de données de référence.

````

Dans le {numref}`chap_pandas`, nous verrons comment charger le contenu de ce fichier
en mémoire et l’analyser. Pour l’instant, concentrons-nous sur quelques
exemples préliminaires. Celui de la {numref}`fig_altair-example` constitue un
premier exemple de graphique interactif. Dans le diagramme supérieur, certains
super-héros sont représentés par des cercles dans un plan cartésien : les
coordonnées de chaque centre indiquent le poids et la taille, tandis que le
rayon exprime la force. La couleur varie selon l’éditeur, à l’aide de
différentes nuances de bleu. En déplaçant le pointeur sur un cercle, on fait
apparaître le nom du super-héros correspondant. Le diagramme inférieur montre,
quant à lui, des barres horizontales indiquant le nombre de super-héros pour
chaque éditeur/créateur. Il est possible de sélectionner un sous-ensemble de
super-héros en traçant un rectangle dans le diagramme supérieur : les autres
éléments du jeu de données sont désactivés et affichés en gris, tandis que le
diagramme inférieur est mis à jour afin de refléter la distribution du groupe
sélectionné. La sélection peut être déplacée, et un clic en dehors de celle-ci
rétablit la vue initiale.
```{margin}
Le graphique de la {numref}`fig_altair-example` a été réalisé avec
{extlink}`Altair <https://altair-viz.github.io/>`, un paquet Python pour
créer des graphiques interactifs dans des pages web. Un signe distinctif des
graphiques Altair est le bouton rond à trois points dans le coin supérieur
droit : il ouvre un menu qui permet, entre autres, de télécharger le graphique.
```

```{code-cell} python
:tags: [remove-cell]

import matplotlib.pyplot as plt
plt.style.use('../_static/sds.mplstyle')
%matplotlib inline
plt.ioff()
```

```{code-cell} python
:height: 600px
:tags: [hide-input]

import altair as alt
import pandas as pd

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
            alt.X('count:Q', title='N. of superheroes'),
            alt.Color('creator:N', title='Creator').scale(scheme="blues"),
        ).transform_filter(
            brush
        ).transform_aggregate(
            count='count()',
            groupby=['creator']
        )
# Create the final interactive chart
chart = (points & bars).configure(background='#eaf3f5')
chart
```

````{customfigure}
:name: fig_altair-example
:class: left-align

Un exemple de graphique interactif basé sur Altair.

````

En interagissant avec ce graphique, on peut effectuer une _analyse
exploratoire_ des données, par exemple pour répondre aux questions suivantes.

1. Quel éditeur/créateur compte le plus grand nombre total de super-héros ?
2. Quel éditeur compte le plus grand nombre de super-héros mesurant moins d’un
   mètre ?
3. Quel éditeur compte le plus grand nombre de super-héros pesant entre $80$ et
   $100$ kg ?
4. Quel est le super-héros le plus grand ?

De nombreux aspects peuvent aussi être analysés sans interagir avec le
graphique, simplement en l’observant dans sa forme initiale, comme pour les
deux questions suivantes.

5. Existe-t-il une tendance ou une relation entre le poids et la taille des
   super-héros ?
6. Cette relation change-t-elle si l’on se concentre sur les super-héros d’un
   éditeur/créateur particulier ?

```{margin}
Si tout cela vous paraît compliqué, ne vous inquiétez pas : les chapitres
suivants expliqueront ces concepts en partant des bases.
```
De telles questions se traitent à l’aide des outils de la _statistique
descriptive_, introduits dans les chapitres
{numref}`chap_dati-e-informazione`–{numref}`chap_analizzare-le-relazioni-tra-i-dati`. Leur but
est d’extraire de l’information à partir d’un jeu de données décrivant un
ensemble d’individus, en tout ou en partie. Les techniques employées peuvent
être de deux types : _qualitatives_ ou _quantitatives_.

- Une analyse qualitative cherche à déterminer la nature d’un phénomène donné
  (par exemple pour répondre aux questions 5 et 6 de la liste ci-dessus). Elle
  s’appuie souvent sur des outils graphiques dont les résultats doivent être
  interprétés, ce qui introduit une certaine part de subjectivité.
- Une analyse quantitative, en revanche, produit une ou plusieurs valeurs
  numériques, qui peuvent être comparées de manière objective à d’autres
  mesures, comme les résultats d’autres analyses.

Pour simplifier, concentrons-nous maintenant sur le poids des super-héros. Le
graphique précédent est assez chargé : d’un côté, il est facile d’identifier
les tailles minimale et maximale, mais de l’autre, il n’est pas immédiat de
savoir si les super-héros « légers » sont plus nombreux que les plus « lourds ».
Pour clarifier ce point, nous pouvons utiliser un _histogramme_, c’est-à-dire
un graphique qui met en évidence les fréquences avec lesquelles les différentes
valeurs du poids apparaissent dans le jeu de données.


```{code-cell} python
:height: 400px
:tags: [hide-input]

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
data = heroes.weight[heroes.weight < 200]

ax.hist(data, bins=30, density=True)
fig
```

````{customfigure}
:name: fig_histogram

Un histogramme des poids des super-héros.
````

```{margin}
L’histogramme n’est pas toujours le bon choix pour explorer des données. Il est
utile lorsque l’on dispose de nombreuses valeurs numériques associées à un
attribut continu ; dans d’autres cas, il peut être trompeur (comme nous le
verrons dans le {ref}`chap_dati-e-informazione).
```

```{margin}
L’exploration des données n’implique pas toujours l’utilisation de méthodes
graphiques : nous verrons également qu’elle repose souvent sur des outils
quantitatifs.
```

```{margin}
En regardant l’axe des ordonnées, on constate que les valeurs ne sont pas
entières, de sorte que la hauteur des rectangles ne peut pas représenter le
nombre de super-héros. Dans cet histogramme, c’est l’aire de chaque rectangle
qui est proportionnelle à la fréquence. Ce choix, qui a des implications
importantes, sera expliqué plus en détail par la suite.
```

Les histogrammes seront expliqués de manière détaillée dans le {ref}`sec_histogrammes`,
mais pour le moment ce qui importe est de savoir comment les lire. Le graphique
est constitué de nombreux rectangles : la base de chacun correspond à un
intervalle $I$ de valeurs possibles du poids, et sa hauteur est liée à la
fraction de super-héros dont le poids tombe dans cet intervalle[^histogram]. En
observant cet histogramme, on remarque deux éléments intéressants :

- les super-héros qui pèsent plus de $125$ kg sont plus nombreux que ceux qui
  pèsent moins de $40$ kg ;
- si l’on exclut les poids extrêmes, la distribution est approximativement
  symétrique, les hauteurs des rectangles augmentant jusqu’à environ $70$ kg
  avant de décroître.

Il s’agit déjà d’une première forme d’analyse exploratoire, même sans
graphiques interactifs.

```{margin}
Si vous êtes attentif, vous aurez remarqué que la hauteur d’un rectangle ne
peut pas correspondre directement au nombre de super-héros ayant un certain
poids, car les valeurs indiquées sur l’axe des ordonnées ne sont pas entières.
Dans cet histogramme, en effet, le nombre de super-héros est représenté par
l’aire du rectangle, ce qui nous permettra de comparer cette répresentation à
une autre un peu plus loin. Le choix de cette représentation est éxpliqué dans
le {ref}`sec_histogrammes`.
```
Une fois que l’on a accumulé suffisamment d’informations sur les données
disponibles, l’étape suivante consiste à tenter de _modéliser_ de manière
mathématique le processus qui les a engendrées. Pour cela, il faut changer de
perspective : au lieu de raisonner sur l’ensemble du jeu de données, imaginons
que nous puissions observer n’importe lequel de ses éléments sans savoir à
l’avance lequel ce sera (rappelons-nous de la [loi de Franklin](#sec_franklin-law)).
Supposons simplement que chaque super-héros ait autant de chances d’être
observé que n’importe quel autre. À partir du {ref}`chap_combinatoire`, les
chapitres consacrés à la _théorie des probabilités_ fournissent des outils
rigoureux pour traiter l’incertitude due au fait que nous ne savons pas quel
super-héros sera observé à chaque fois. Nous nous intéresserons aux
_événements_, c’est-à-dire aux énoncés portant sur ce que nous pourrions
observer. Par exemple, les affirmations suivantes sont des événements :

1. nous observerons un super-héros malveillant (en supposant que l’alignement
   moral soit fixé à l’avance et indiqué par l’attribut `alignment` du jeu de
   données) ;
2. si nous observons un super-héros Marvel et un super-héros DC, le premier est
   plus rapide que le second ;
3. si nous observons deux super-héros apparus pour la première fois la même
   année, ils ont le même niveau d’intelligence ;
4. si nous observons dix super-héros, au moins l’un d’eux appartient à l’un des
   univers _Star Wars_.

Nous ne savons pas si ces affirmations sont vraies ou fausses (techniquement,
si les événements correspondants se réalisent ou non) : tout dépend de ce que
nous observons. C’est ici qu’intervient la _probabilité_. Elle attribue un
nombre $p \in [0, 1]$ pour quantifier cette incertitude. Sans entrer pour le
moment dans les détails, l’incertitude est maximale lorsque $p$ se rapproche de
$\frac{1}{2}$, et elle diminue lorsque $p$ tend vers les extrêmes. En
particulier, plus $p$ est proche de zéro, moins il est raisonnable de croire à
la véracité de l’affirmation, et si $p = 0$, on sait qu’elle est fausse avec
certitude. De même, lorsque $p$ se rapproche de $1$, la confiance dans la
vérité de l’affirmation augmente, et si $p = 1$, elle devient certaine. Nous
verrons que cette formalisation permet de calculer la probabilité d’événements
complexes à partir d’événements plus simples. Par exemple, pour calculer la
probabilité du dernier événement de la liste ci-dessus, il suffit de connaître
la probabilité d’observer un super-héros issu d’un univers _Star Wars_.

Très souvent, les événements que nous considérons font référence à une ou
plusieurs quantités numériques (pensons, par exemple, à l’endurance ou à la
taille d’un super-héros : il est naturel de se demander si elle est maximale ou
si elle appartient à un certain intervalle). Il est important de souligner que
le fait que chaque super-héros ait la même probabilité d’être observé ne
signifie pas que la même chose soit vraie pour les valeurs que ces quantités
peuvent prendre. On s’en rend facilement compte en regardant à nouveau
l’histogramme précédent : les poids compris entre $50$ et $100$ kg sont bien
plus fréquents que ceux qui dépassent cent kilos. Il devient donc nécessaire de
modéliser également ces quantités aléatoires. Pour cela, on introduit le
concept de _variable aléatoire_ et sa formalisation mathématique. Pour le
moment, concentrons-nous sur le cas particulier du poids des super-héros, en
gardant à l’esprit que, de manière générale, la procédure peut être plus
complexe, ou simplement différente. L’idée à la base de cette formalisation
consiste à identifier une fonction $f$, appelée _densité de probabilité_, dont
le graphique _idéalise_ l’histogramme des valeurs observées, en produisant une
courbe continue qui en conserve les propriétés essentielles. Dans notre
exemple, ces propriétés sont la symétrie par rapport à un axe central et une
forme _unimodale_ (c’est-à-dire croissante jusqu’à une valeur maximale puis
décroissante). Il existe une infinité de fonctions possédant ces deux
propriétés, mais pour des raisons trop complexes à expliquer à ce stade &mdash;
que j’éclaircirai toutefois plus tard &mdash; je me concentrerai sur celle qui
est définie par :

```{margin}
Dans cette formule, $\exp(x)$ désigne la constante $\mathrm e$ élevée à la
puissance $x$. Je préfère cette notation à $\mathrm e^x$ afin d’éviter un
exposant fractionnaire, qui serait moins lisible.
```
```{math}
:label: eq_weight_normal
f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2 \pi}} \;
       \mathrm{exp}\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right) \enspace,
```

```{margin}
La courbe que nous considérons est souvent appelée, de manière informelle, une
_courbe en cloche gaussienne_, et le modèle correspondant est qualifié de
_normal_. Comme nous le verrons, il jouera un rôle fondamental dans les deux
dernières parties du livre.
```
où $x$ désigne un poids quelconque et où $f(x; \mu, \sigma)$ renvoie la hauteur
correspondante dans l’histogramme idéalisé. Il est important de souligner que
$f$ n’a qu’un seul argument, noté $x$, tandis que $\mu \in \mathbb R$ et
$\sigma \in \mathbb R^+$ sont deux _paramètres_ qu’il faut fixer pour définir
complètement la fonction. Le point-virgule sert précisément à distinguer
l’argument des paramètres. Plus précisément, lorsque $\mu$ et $\sigma$ varient,
{eq}`eq_weight_normal` définit une _famille_ de fonctions : chacune correspond
à une variable aléatoire, et l’on parle alors d’un _modèle de variable
aléatoire_. Dans {numref}`fig_normal-model`, on peut observer comment le
graphique de $f$ évolue lorsque ses paramètres changent. En déplaçant les deux
curseurs associés à $\mu$ et à $\sigma$, on voit immédiatement comment la
visualisation de $f$ se met à jour.


````{customfigure}
:name: fig_normal-model
:class: left-align


```{interactive-code} python
:tags: [toggle-code]

import asyncio
import matplotlib.pyplot as plt
import numpy as np
from js import document
from pyscript import display
from pyscript.web import page, when

mu = float(page['#pdf-mu-slider'][0].value)
sigma = float(page['#pdf-sigma-slider'][0].value)

x = np.linspace(0, 200, 400)
y = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

fig_pdf, ax_pdf = plt.subplots()
curve_pdf, = ax_pdf.plot(x, y, alpha=0.5, color='tab:blue')


ax_pdf.set_xlabel('$x$', fontsize=12, ha='right')
#ax.xaxis.set_label_coords(1.07, 0.03)
ax_pdf.set_ylabel('$f$', fontsize=12, rotation=0)
#ax.yaxis.set_label_coords(0., 1.09)
ax_pdf.set_xlim(0, 200)
ax_pdf.set_ylim(0, 0.02)

@when("input", "#pdf-mu-slider, #pdf-sigma-slider")
def pdf_plot(event):

    mu = float(page['#pdf-mu-slider'][0].value)
    sigma = float(page['#pdf-sigma-slider'][0].value)
    page['#pdf-mu-value'][0].innerHTML = f'{mu:.1f}'
    page['#pdf-sigma-value'][0].innerHTML = f'{sigma:.1f}'

    y = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) /
        sigma) ** 2)
    curve_pdf.set_data(x, y)
    display(fig_pdf, target='graph-%this%', append=False)

display(fig_pdf, target='graph-%this%', append=False)
```

```{raw} html
<div class="plot-container">
    <div class="model-slider-container">
        <label for="pdf-mu-slider">\(\mu\): </label>
        <input type="range" id="pdf-mu-slider"
               min="10" max="200" value="150" step="0.1" />
        <span id="pdf-mu-value">150</span>
    </div>

    <div class="model-slider-container">
        <label for="pdf-sigma-slider">\(\sigma\): </label>
        <input type="range" id="pdf-sigma-slider"
               min="0.1" max="50" value="33" step="0.1" />
        <span id="pdf-sigma-value">33.0</span>
    </div>
</div>
```

Graphique de la densité de probabilité décrite par {eq}`eq_weight_normal`.
````

L’une des raisons pour lesquelles on parle de « modèle de variable aléatoire »
est qu’il est possible de choisir les valeurs de ses paramètres afin
d’_adapter_ la densité de probabilité, et plus généralement la variable
aléatoire correspondante, à des données déjà observées. Dans le cas que nous
venons de voir, cela revient à choisir des valeurs appropriées pour $\mu$ et
$\sigma$ de sorte que le graphique de $f$ se superpose qualitativement à
l’histogramme initialement obtenu pour le poids. Le graphique interactif de
{numref}`fig_adapt-model` vous permet d’effectuer cette opération manuellement,
en déplaçant les curseurs afin de trouver un ajustement qualitatif entre les
deux visualisations.

```{interactive-code} python
:height: 0px
:class: no-output

data = heroes['weight'][heroes['weight'] < 200].dropna()
```

````{customfigure}
:name: fig_adapt-model
:class: left-align

```{interactive-code} python
:height: 400px
:class: toggle-code

mu = float(page['#model-mu-slider'][0].value)
sigma = float(page['#model-sigma-slider'][0].value)

x = np.linspace(0, 200, 400)
y = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

fig, ax = plt.subplots()
ax.hist(data, bins=30, density=True, alpha=0.3, color='tab:blue')
curve, = ax.plot(x, y, alpha=0.5, color='tab:blue')

ax.set_xlabel(r'$x$', fontsize=12, ha='right')
ax.xaxis.set_label_coords(1.07, 0.03)
ax.set_ylabel(r'$f$', fontsize=12, rotation=0)
ax.yaxis.set_label_coords(0., 1.09)
ax.set_xlim(0, 200)
ax.set_ylim(0, 0.02)

@when("input", "#model-mu-slider, #model-sigma-slider")
def model_plot(event):

    mu = float(page['#model-mu-slider'][0].value)
    sigma = float(page['#model-sigma-slider'][0].value)
    page['#model-mu-value'][0].innerHTML = f'{mu:.1f}'
    page['#model-sigma-value'][0].innerHTML = f'{sigma:.1f}'

    y = (1 / (sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
    curve.set_data(x, y)
    display(fig, target='graph-%this%', append=False)

display(fig, target='graph-%this%', append=False)
    
```

```{raw} html
<div class="plot-container">
    <div class="model-slider-container">
        <label for="model-mu-slider">\(\mu\): </label>
        <input type="range" id="model-mu-slider"
               min="10" max="200" value="150" step="0.1" />
        <span id="model-mu-value">150</span>
    </div>

    <div class="model-slider-container">
        <label for="model-sigma-slider">\(\sigma\): </label>
        <input type="range" id="model-sigma-slider"
               min="0.1" max="50" value="33" step="0.1" />
        <span id="model-sigma-value">33.0</span>
    </div>
</div>
```

Superposition du graphique de la densité décrite par {eq}`eq_weight_normal` à
l’histogramme de {numref}`fig_histogram`. En déplaçant les curseurs, il est
possible de trouver des valeurs de paramètres qui ajustent le modèle à
l’histogramme.
````

Dans la dernière partie du livre, nous verrons qu’il existe plusieurs méthodes
permettant de déterminer automatiquement les paramètres d’un modèle afin de
l’adapter à un ensemble de données. C’est l’un des objectifs de la _statistique
inférentielle_. Le point de départ est toujours un _jeu de données_, qui, dans
ce contexte, représente un _échantillon_ d’observations issues d’une
_population_ plus large. Nous voulons formuler des hypothèses sur cette
population ou tirer des conclusions à son sujet, même si nous ne pouvons pas
l’observer dans son intégralité. En d’autres termes, nous utilisons
l’échantillon pour obtenir des informations sur ce que nous ignorons de la
population. Le cas le plus simple &mdash; et aussi celui sur lequel nous nous
attarderons le plus &mdash; est celui où la population est décrite par une
variable aléatoire associée à un modèle dépendant d’un ou de plusieurs
paramètres inconnus. L’objectif consiste à approximer ces paramètres, ou
d’autres quantités qui en dépendent. Par exemple, considérons la population des
super-héros de notre jeu de données et supposons que nous nous intéressions à
leur poids moyen $p$. Si nous n’avons à disposition qu’un échantillon de cent
super-héros, le bon sens suggère d’utiliser la moyenne de leurs poids comme une
approximation de $p$. En général, on appelle _estimateur_ la fonction appliquée
à l’échantillon pour obtenir ce type d’approximation. Dans notre exemple,
l’estimateur est simplement la moyenne arithmétique des valeurs de
l’échantillon, appelée _moyenne d’échantillon_. La
{numref}`fig_statistics-variability` montre comment les valeurs de cet
estimateur varient lorsque l’on tire dix échantillons différents.

````{customtable}
:name: fig_statistics-variability
:class: left-align

```{interactive-code} python
:height: 100px
:class: toggle-code

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

Valeur de la moyenne d’échantillon du poids des super-héros, calculée sur dix
échantillons différents tirés dans la population.
````

Il est naturel que les moyennes obtenues à partir des dix échantillons
diffèrent les unes des autres, puisque chaque échantillon est différent.
Néanmoins, les résultats ne varient pas de façon drastique et ont tendance à se
regrouper autour de $79$, qui constitue une bonne approximation de la valeur
correcte du poids moyen de l’ensemble des super-héros (comme on peut le
vérifier en observant l’histogramme précédent). Mais peut-on être certain que
la moyenne d’échantillon soit réellement le meilleur estimateur possible ? Et,
plus généralement, comment évaluer la qualité d’un estimateur en tenant compte
de la variabilité intrinsèque que nous venons de mettre en évidence ? Ces
questions trouveront leur réponse dans la partie consacrée à la statistique
inférentielle. D’une certaine manière, cette partie me permet de terminer le
livre en « bouclant la boucle » : non seulement parce qu’elle met en pratique,
de manière synergique, ce que nous avons vu en statistique descriptive et en
théorie des probabilités, mais aussi parce qu’elle permet de comprendre plus en
profondeur la puissance de certains concepts et outils déjà rencontrés &mdash;
peut-être de façon relativement informelle &mdash; dans les parties précédentes.

Avant de commencer avec la statistique descriptive, il est toutefois important
de revoir quelques concepts fondamentaux de programmation et, surtout, de se
familiariser avec les outils computationnels que j’utiliserai dans tout le
livre. C’est l’objet des chapitres {numref}`chap_intro-python` et
{numref}`chap_pandas`, qui ouvrent le parcours.

## Exercices

À la fin de presque chaque paragraphe, quelques exercices sont proposés. Leur
difficulté est indiquée par le nombre de points entre parenthèses.

```{exercise} •
Téléchargez le jeu de données des super-héros depuis le
{extlink}`dépôt <https://github.com/dariomalchiodi/sds>` du livre et
importez-le dans un tableur quelconque (les plus répandus savent importer des
fichiers CSV), de façon à ce que chaque colonne contienne un attribut
différent. Concentrez-vous, par exemple, sur les trente premières lignes et
considérez les colonnes séparément afin de vous faire une idée de la manière
dont varient les valeurs associées aux différents attributs.
```

```{margin}
Être _data scientist_, ce n’est pas seulement combiner des compétences en
probabilités, en statistique et en programmation : c’est aussi maîtriser divers
outils de _scripting_ permettant de convertir, adapter et nettoyer les données.
Ces outils sont souvent utilisés via un terminal et son _shell_. Selon le
contexte professionnel, les données peuvent être disponibles sous des formes
plus ou moins structurées, et leur traitement peut exiger des procédures
complexes, faisant parfois intervenir des représentations autres que le CSV ou
des bases de données élaborées.
```
````{exercise} •••
Reprenez l’exercice précédent en examinant le contenu de chaque colonne du
fichier CSV sans utiliser de tableur, mais uniquement un terminal et des
commandes de _shell_.
````

```{exercise} ••
À partir de l’idée que vous vous êtes faite du jeu de données des super-héros
en résolvant les exercices précédents, essayez de répartir les attributs en
groupes homogènes en vous fondant non sur le type de donnée utilisé pour
représenter les valeurs correspondantes (indiqué dans la colonne « Contenu » de
la {numref}`tab_dataset`), mais sur la _nature_ même des attributs.
```

```{exercise} •
Répondez aux questions 1 à 4 de la liste qui suit le premier graphique
interactif.
```

```{exercise} ••
Répondez aux questions 5 et 6 de la liste qui suit le premier graphique
interactif. Mettez par écrit le raisonnement que vous avez suivi.
```

```{exercise} ••
Formulez d’autres questions sur le jeu de données auxquelles on peut répondre
à l’aide du premier graphique interactif. Là encore, mettez par écrit le
raisonnement nécessaire pour y répondre.
```

````{exercise} •
Considérez les valeurs suivantes

```{math}
\{13, 8, 7, 4, 9, 8, 4, 4, 19, 2, 5, 3, 3, 1, 12 \}
```

et tracez à la main l’histogramme correspondant, en calculant la hauteur de
chaque rectangle comme le nombre de valeurs qui tombent dans l’intervalle
considéré, et en utilisant les intervalles de référence suivants : $[0, 5)$,
$[5, 10)$, $[10, 15)$, $[15, 20)$. Comparez la forme du graphique obtenu avec
celui présenté dans le texte, en mettant en évidence les principales
différences.
````

```{exercise} •
Écrivez dix événements possibles concernant le jeu de données des super-héros.
```

```{exercise} ••
Écrivez un événement dont la probabilité est nulle. Puis écrivez-en un autre
dont la probabilité vaut $1$.
```

```{exercise} ••
Posez $\mu = \sigma = 1$ et étudiez la fonction décrite dans
{eq}`eq_weight_normal`, en traçant à la main le graphe correspondant et en
vérifiant que sa forme correspond à celle qui apparaît dans le second graphique
interactif.
```

```{exercise} •
À partir du résultat de l’exercice précédent, et en tenant compte de ce que
vous avez observé en utilisant le second graphique interactif, quel est le rôle
des paramètres $\mu$ et $\sigma$ dans le graphe de $f$ définie par
{eq}`eq_weight_normal` ?
```

```{exercise} •
À l’aide du second graphique interactif, déterminez des valeurs de $\mu$ et
$\sigma$ qui permettent de superposer raisonnablement le graphe de $f$ à
l’histogramme des poids des super-héros.
```

```{exercise} ••
Mettez par écrit le raisonnement qui vous a convaincu que $79$ est une bonne
approximation du poids moyen des super-héros.
```

[^histogram]: Les intervalles définissant les bases des rectangles d’un
histogramme peuvent être choisis avec une certaine liberté. Par souci de
simplicité, l’histogramme du texte a été généré à l’aide de trente intervalles
de même largeur couvrant toutes les valeurs possibles du poids. Selon le
contexte, il peut être pertinent d’en utiliser davantage (ou moins), ou même
d’employer des intervalles de largeurs différentes.