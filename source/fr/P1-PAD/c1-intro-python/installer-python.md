---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
nb_execution: false
---

(sec_installation)=
# Installation, configuration et premiers pas

Cette section explique comment installer Python et les bibliothèques auxquelles
je vais me référer tout au long du livre, tout en présentant un ensemble de
bonnes pratiques à adopter dès le début de tout projet logiciel d'analyse de
données&mdash;comme l'utilisation d'environnements virtuels et de gestionnaires
de paquets. Si vous êtes déjà familier avec Python et disposez d'une
installation opérationnelle, vous pouvez probablement passer à la section
suivante. Cependant, je recommande tout de même une lecture rapide pour vous
aligner sur la terminologie que j'utiliserai et vérifier qu'aucun problème de
compatibilité ne survienne avec votre version installée, et que toutes les
bibliothèques nécessaires soient disponibles.

(sec_langages-versions-implementations)=
## Langages, versions et implémentations

Les langages de programmation évoluent au fil du temps, à mesure que leurs
spécifications sont mises à jour. Ces changements se traduisent par une
succession de _versions_ du langage. Aujourd'hui, la manière la plus répandue
d'identifier une version spécifique d'un langage de programmation (mais aussi
d'une bibliothèque ou de tout produit logiciel) est le [versionnage
sémantique](https://semver.org/lang/fr/), qui, dans sa forme la plus simple,
décrit une version avec le format `X.Y.Z` &mdash; une suite de trois entiers
initialement définis à zéro et incrémentés lors des mises à jour :

- `X` indique une _version majeure_, augmentée lorsqu'il y a des changements
  incompatibles,
- `Y` est la _version mineure_, augmentée lorsqu'on ajoute des fonctionnalités
  compatibles avec les versions précédentes,
- `Z` correspond au _numéro de correctif_, lié à de petites modifications et
  corrections.

En général, sauf besoin d'une précision particulière, il suffit de se référer à
une version de Python en indiquant uniquement la version majeure et mineure.
Par exemple, même si le code de ce livre a été écrit avec Python 3.11.11, je
parlerai simplement de la version 3.11, puisque le code est exécutable quelle
que soit la version de correctif. De plus, utiliser une version mineure plus
récente ne devrait poser aucun problème, tandis qu'une version nettement plus
ancienne est à éviter.

Il pourrait sembler que connaître la version exacte d'un langage de
programmation suffise à en déterminer toutes les fonctionnalités, mais ce n'est
pas tout à fait vrai. La définition d'un langage inclut sa _syntaxe_ et sa
_sémantique_, mais la création des outils permettant d'exécuter les programmes
correspondants &mdash; interpréteurs et compilateur [^compilateurs] &mdash; est
une autre affaire. Ces outils peuvent être développés par des personnes
différentes, à des moments différents, et avec des technologies diverses. Il
existe donc plusieurs _implémentations_ d'un même langage, qui peuvent différer
malgré le respect d'une version identique, car les spécifications ne dictent
pas toujours exactement _comment_ certaines fonctionnalités doivent être
réalisées. Par exemple, le format d'encodage des chaînes de caractères peut
différer selon les implémentations. Dans le cas de Python, il existe <a
href="/sds/short/py-implementations" target="_blank">plusieurs
implémentations</a>, chacune reposant sur une technologie sous-jacente
différente : l'une utilise la machine virtuelle Java, une autre un moteur écrit
en C, une autre encore s'exécute dans les navigateurs web, etc.
L'implémentation la plus courante, généralement installée par défaut, s'appelle
_CPython_ et, comme son nom l'indique, est écrite en C.

(sec_telecharger-livre)=
## Télécharger le contenu du livre

Ce livre est conçu pour être utilisé via un serveur web. L'avantage est que les
composants interactifs sont accessibles sans installation ni configuration de
bibliothèques, mais cela nécessite une connexion internet permanente. Il est
aussi possible de télécharger le contenu du livre et de générer ses chapitres
sous forme de pages web servies depuis un serveur local, mais cela implique
d'abord d'installer tous les logiciels nécessaires à ce processus. Notez que
l'exécution des composants interactifs exige toujours une connexion internet.

```{margin}
Pour cloner le dépôt du livre, vous devez avoir installé un client git, 
disposer d'un compte GitHub et d'une clé SSH publique qui y est associée.
Alternativement, le clonage via HTTPS est possible, ce qui simplifie certaines
étapes (comme la clé SSH) mais en complique d'autres.
```

La méthode recommandée pour télécharger le livre est d'utiliser
[git](https://git-scm.com), un système de gestion de versions utilisé pour
gérer le code source dans les projets logiciels. Pour ce faire, ouvrez un
terminal, placez-vous dans l'emplacement souhaité de votre système de fichiers
et exécutez la commande suivante pour cloner le
[répertoire](https://github.com/dariomalchiodi/sds) du livre dans un nouveau
dossier `sds` :

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      Dans tous les exemples ci-dessous, le symbole ``$`` indique l'invite
      de la ligne de commande. Selon votre configuration, elle peut être
      différente. Dans l'exemple, ``my_parent_dir`` est un espace réservé
      pour le chemin où vous souhaitez sauvegarder le dossier du livre.

      .. code-block:: bash

         $ cd my_parent_dir
         $ git clone git@github.com:dariomalchiodi/sds.git
         $ cd sds

      Je supposerai, pour la suite, que cette session du terminal reste
      ouverte.

   .. group-tab_: Windows

      Dans les exemples suivants, ``C:>`` représente l'invite de
      PowerShell. Selon votre configuration, elle peut être différente. Dans
      l'exemple, ``my_parent_dir`` est un espace réservé pour le chemin du
      dossier où vous souhaitez sauvegarder le dossier du livre.

      .. code-block:: powershell

         C:> cd my_parent_dir
         C:> git clone git@github.com:dariomalchiodi/sds.git
         C:> cd sds

      Je supposerai, pour la suite, que cette session PowerShell reste ouverte.

```

```{margin}
Une connexion internet active est requise pour cette opération.
```

On peut aussi télécharger une archive ZIP. Cependant, avec git, il est facile
de mettre à jour le livre en exécutant simplement :

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         $ git pull

   .. group-tab_: Windows

      .. code-block:: powershell

         C:> git pull

```

depuis un terminal après s'être placé dans le dossier `sds` (ou l'un de ses
sous-dossiers). De plus, git est l'outil utilisé pour signaler des problèmes ou
proposer des modifications, via des _issues_ ou _pull requests_ comme expliqué
dans {ref}`chap_approche`. Enfin, se familiariser avec git est quelque chose
que je recommande à toute personne étudiant l'informatique ou, plus largement,
les disciplines liées à la science des données. En effet, git est utilisé dans
la grande majorité des projets logiciels, ce qui justifie de l'apprendre dès le
départ.

## Installer Python

L'installation de Python dépend fortement de votre système d'exploitation. Les
versions récentes de Linux et Mac OS incluent Python par défaut, tandis que
sur Windows il doit être installé manuellement. Cependant, il est possible que
votre ordinateur dispose déjà de Python. Pour vérifier, ouvrez un terminal et
exécutez :

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         $ python --version

   .. group-tab_: Windows

      .. code-block:: powershell

         C:> python --version

```

Trois résultats sont possibles :

1. La sortie est `Python 3.Y.Z`, ce qui signifie que Python 3 est installé, où
   `Y` et `Z` correspondent respectivement à la version mineure et au numéro de
   correctif, et `Y` est supérieur ou égal à $5$ ;
2. La sortie affiche une version commençant par `1` ou `2`, ou `3` mais avec
   une version mineure inférieure à $5$, ce qui signifie que Python est présent
   mais trop ancien pour exécuter le code de ce livre. Je me référerai à la
   version 3.11, largement adoptée au moment de l'écriture ;
```{margin}
Si la version majeure est `4` ou plus, alors vous lisez ce livre longtemps
après sa rédaction, et certains contenus relatifs à Python peuvent être
obsolètes. Vérifiez l'existence de versions plus récentes ou de
documentations mises à jour.
```
3. Un message d'erreur indique que `python` n'est pas une commande reconnue,
   ce qui signifie probablement que Python n'est pas installé.

Dans le premier cas, votre installation actuelle devrait suffire pour exécuter
le code de ce livre. Il est toutefois conseillé de vérifier que la version est
aussi proche que possible de celle que j'ai utilisée. Une version très
différente pourrait provoquer des problèmes de compatibilité, auquel cas il
vaut mieux installer la version indiquée sans supprimer l'existante.
```{margin}
Techniquement, remplacer le Python système est possible, mais cela risque de
casser d'autres logiciels. C'est donc déconseillé.
```

Dans le deuxième cas, il se peut qu'une version compatible soit installée, mais
que la commande `python` pointe vers une autre. Pour vérifier, tapez `python`
dans le terminal puis appuyez sur {kbd}`TAB` sans espace : si plusieurs
versions sont présentes, leurs commandes apparaîtront. Dans le troisième cas,
Python est peut-être installé mais mal configuré pour l'utiliser dans le
terminal&mdash;ce qui est rare.
```{margin}
En général, pour chaque version installée, il existe une commande du type
`pythonX.Y`, où `X` et `Y` sont respectivement les numéros de version majeure
et mineure. La commande `python` est un alias pointant vers l'une d'elles,
souvent la plus utilisée par le système.
```

Si Python doit être installé, consultez la documentation officielle, qui
fournit des guides pour
[Unix (comme Linux)](https://docs.python.org/3/using/unix.html),
[Mac OS](https://docs.python.org/3/using/mac.html) et
[Windows](https://docs.python.org/3/using/windows.html).


## Création d'un environnement d'exécution virtuel

Python est souvent utilisé avec de nombreuses bibliothèques, et je déconseille
vivement l'approche _monolithique_, où les bibliothèques sont ajoutées au fur
et à mesure des besoins. Avec le temps, cela augmente le risque
d'incompatibilités entre votre environnement et les bibliothèques nouvellement
ajoutées. Des problèmes similaires apparaissent lors des mises à jour. Pour
éviter ces soucis, il vaut mieux isoler l'installation des bibliothèques en
exécutant Python dans un espace dédié ne contenant que les paquets nécessaires
à un projet donné. Ces espaces, appelés _environnements virtuels_, sont activés
lorsque vous commencez à travailler sur un projet précis et désactivés lorsque
vous passez à un autre.

Il existe plusieurs façons de créer des environnements virtuels sous Linux ; ce
livre utilise _venv_[^environnement], inclus dans les versions récentes de
Python. Pour créer un environnement virtuel, utilisez la même session shell que
précédemment, placez-vous dans le répertoire sds et lancez :

```{margin}
Nommer le répertoire `.venv` est une pratique courante reconnue par de
nombreux IDE. Vous pouvez techniquement choisir un autre nom, mais ne le faites
que si vous avez une raison précise. L'option `--prompt sds` est facultative et
définit l'étiquette de l'invite ; sinon, le nom du répertoire sera utilisé.
```
```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         $ python3.11 -m venv .venv --prompt sds

   .. group-tab_: Windows

      .. code-block:: powershell

         C:> python3 -m venv .venv --prompt sds
```

Assurez-vous que python3.11 (sous Linux/Mac OS) ou python3 (sous Windows)
pointe vers la version souhaitée et qu'il est correctement installé. Cela crée
un répertoire .venv (caché sous Linux et Mac OS) avec les exécutables et les
futures bibliothèques de cet environnement. Pour l'activer, lancez :

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         $ source .venv/bin/activate

   .. group-tab_: Windows

      .. code-block:: powershell

         C:> .venv\Scripts\activate
```

Vous devez exécuter cette commande depuis le répertoire sds (ou utiliser un
chemin relatif/absolu vers le script activate). L'activation modifie aussi
l'invite, en ajoutant (sds) pour indiquer qu'un environnement virtuel est en
cours d'utilisation. La section suivante explique comment installer des
bibliothèques après activation. Pour désactiver l'environnement, tapez :

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         (sds) $ deactivate

   .. group-tab_: Windows

      .. code-block:: powershell

         (sds) C:> deactivate
```

Cela rétablit l'invite système dans son état initial.

(sec_lib-install)=
## Gestion des bibliothèques

En théorie, on peut installer une bibliothèque manuellement en téléchargeant
son exécutable ou en la générant à partir de son code source public. Mais cela
peut être délicat : la plupart des bibliothèques dépendent d'autres
bibliothèques, qui elles-mêmes peuvent en dépendre, et ainsi de suite.
Installer une bibliothèque à la main devient vite une expérience chronophage et
frustrante. Plus il y a de dépendances, plus le risque d'erreurs bloquant le
processus est élevé. Pour éviter ce problème, il est préférable d'utiliser un
_gestionnaire de paquets_&mdash;un outil qui détecte et gère automatiquement
les dépendances. C'est la bonne pratique en Python et, plus largement, en
développement logiciel. Comme pour les environnements virtuels, Python propose
plusieurs
[gestionnaires de paquets](https://packaging.python.org/en/latest/tutorials/installing-packages/#alternative-packaging-tools)[^package-manager].
Nous utiliserons [pip](https://pip.pypa.io), inclus dans les versions récentes
de Python.

L'installation de bibliothèques, généralement effectuée dans un environnement
virtuel actif, se fait avec la commande pip dans un shell, en précisant le nom
de la bibliothèque&mdash;éventuellement suivi de `==version` pour installer une
version précise. Par exemple, pour installer altair, la bibliothèque utilisée
dans {ref}`sec_apercu-general` pour les graphiques interactifs, on taperait :

```{margin}
Nous verrons bientôt comment installer toutes les bibliothèques requises en une
seule fois, il n'est donc pas nécessaire de lancer cette commande maintenant.
```

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         (sds) $ pip install altair

   .. group-tab_: Windows

      .. code-block:: powershell

         (sds) C:> pip install altair
```

Cela vérifie les dépendances d'altair, les installe si elles manquent ou les
met à jour si leurs versions sont incompatibles, et fait de même récursivement
pour les autres dépendances.

Les gestionnaires de paquets offrent aussi un autre avantage : on peut partager
un projet logiciel avec un fichier texte listant les bibliothèques requises et
les installer toutes d'un coup. Avec pip, cette liste est généralement placée
dans un fichier `requirements.txt`. Pour tout installer d'un coup, tapez :

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         (sds) $ pip install -r requirements.txt

   .. group-tab_: Windows

      .. code-block:: powershell

         (sds) C:> pip install -r requirements.txt
```

Le [dépôt](https://github.com/dariomalchiodi/sds) de ce livre inclut un fichier
`requirements.txt` listant toutes les bibliothèques nécessaires pour exécuter
le code des chapitres.

(sec_notebook)=
## Installation d'un gestionnaire de notebooks

Comme mentionné au début de ce chapitre, je présenterai le code Python de façon
à ce qu'il puisse être facilement exécuté dans des fichiers appelés
_notebooks_. Le contenu de ces fichiers est organisé en _cellules_, qui peuvent
être de trois types :
- cellules de code, composées d'une ou plusieurs lignes de code
  exécutable[^nb-lang],
- cellules de sortie, chacune associée à une cellule de code précise et
  contenant le résultat produit par son exécution,
- autres cellules, pouvant contenir du texte formaté, des graphiques ou des
  vidéos, éventuellement générés comme effets secondaires du code ou ajoutés
  manuellement par l'auteur.

```{margin}
Lorsque le nom d'une technologie Python contient la syllabe « py », elle se
prononce généralement comme le mot anglais « pie » (<a href="/sds/short/pie"
taget="_blank">ˈpī</a>). Jupyter fait exception, comme l'ont précisé ses
créateurs[^pronuncer-jupyter], et se prononce <a href="/sds/short/pee"
taget="_blank">ˈjü-pə-tər</a>, comme le nom anglais de la planète Jupiter.
```

Le standard _de facto_ des _notebook_ est celui introduit par le projet
[Jupyter](https://jupyter.org). Il existe <a href="/sds/short/jp-alternatives"
target="_blank">de nombreuses applications</a> permettant de créer, lire et
surtout exécuter des _notebook_. Les plus utilisées sont celle distribuée par
le projet Jupyter et l'IDE principal de Microsoft, [Visual Studio
Code](https://code.visualstudio.com).

Si vous avez installé les bibliothèques via le fichier requirements.txt selon
les instructions des sections précédentes, Jupyter est déjà disponible dans
l'environnement virtuel que vous avez créé. Pour le lancer, tapez simplement :

```{margin}
Un peu plus loin, vous trouverez aussi des instructions pour utiliser un
_notebook_ avec Visual Studio Code.
```
```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         (sds) $ jupyter notebook

   .. group-tab_: Windows

      .. code-block:: powershell

         (sds) C:> jupyter notebook
```
```{margin}
L'extension `.ipynb` identifie les _notebook_ Python.
```

Cela ouvrira automatiquement un navigateur sur une adresse locale, où un
serveur web attend les requêtes. La page affichera les fichiers du répertoire
d'où Jupyter a été lancé. Par exemple, la {numref}`jupyter-home` montre cette
page depuis la racine du dépôt de ce livre. En cliquant sur le dossier
`playground` et en ouvrant le fichier `first-notebook.ipynb`, vous verrez un
exemple simple, avec une seule cellule de code contenant l'expression `1 + 1`.
Si vous placez le curseur dans la cellule et appuyez sur {kbd}`Shift` +
{kbd}`⤶`, une cellule de sortie s'ajoute, affichant le résultat. Pour créer un
nouveau _notebook_, vous pouvez passer par _File > New > Notebook_ ou cliquer
sur « New » et choisir « Python 3 (ipykernel) ». Une nouvelle page s'ouvre avec
une cellule de code vide. L'avantage d'un _notebook_ est la forte
interactivité : les résultats d'exécution restent en mémoire tant qu'il reste
ouvert, et peuvent être réutilisés dans les cellules suivantes.

```{figure} ../../../_static/img/jupyter-home.png
:width: 100%
:name: jupyter-home

L'écran d'accueil de Jupyter, montrant les fichiers du répertoire du dépôt.
```

Utiliser un _notebook_ dans Visual Studio Code est encore plus simple, avec
l'extension correspondante : il suffit d'ouvrir le fichier dans l'IDE, et ses
cellules apparaissent dans un onglet. Là aussi, on peut écrire et exécuter du
code comme dans Jupyter. La seule différence est que lors de la première
exécution, il peut être nécessaire de choisir un environnement dans un menu
contextuel.

```{admonition} Avertissement
L'évaluation des cellules d'un _notebook_ est très flexible : il suffit de
placer le curseur sur une cellule et d'appuyer sur {kbd}`Shift` + {kbd}`⤶`
pour l'exécuter dans n'importe quel ordre &mdash; du début à la fin, de la fin
au début, sept fois la première puis la troisième, ou dans tout ordre
imaginable. Cela a ses avantages et ses inconvénients. D'un côté, on peut
analyser des données de façon très interactive, en exécutant de petites parties
de code et en décidant ensuite des étapes suivantes. De l'autre, l'absence d'un
ordre fixe peut introduire une part d'indétermination, limitant la
reproductibilité. En outre, bien que les _notebook_ soient des fichiers texte,
ils contiennent beaucoup de métadonnées qui compliquent leur gestion avec
git[^jupytext]. Enfin, les _notebook_ ne sont qu'un outil parmi d'autres pour
exécuter du code Python. Parmi les alternatives les plus répandues, deux se
distinguent. La première est le REPL (Read, Evaluate, Print, Loop), un
environnement purement textuel dans un shell, qui partage la même philosophie :
on entre une instruction, on l'exécute, on observe le résultat, puis on en
entre une autre. Mais ici, pour réexécuter une instruction précédente, il faut
la retaper. La seconde est l'utilisation d'un interpréteur Python pour exécuter
un programme, comme on le ferait avec d'autres langages tels que Go ou Java.
```


## Premiers pas avec Python

Comme discuté dans le {ref}`sec_apprendre-et-programmer`, je pars du principe
que vous êtes déjà familier avec au moins un langage de programmation. Dans
cette section, cependant, nous allons rapidement passer en revue quelques
opérations de base pour voir comment elles sont réalisées en Python. Cela me
permettra d'introduire immédiatement des exemples de code Python en parallèle
des concepts que j'expliquerai.

### Affectations
Attribuer une valeur à une variable utilise la même notation que dans la
plupart des autres langages, avec la syntaxe `variable = valeur`. Dans
{ref}`sec_typisation-dynamique`, nous verrons que Python ne demande pas de
déclaration de type : les variables sont créées automatiquement lors de la
première affectation, et cette valeur détermine implicitement leur type. Par
exemple :

```python
age = 42
```

est une affectation impliquant un entier.

### Afficher une valeur
Nous avons déjà vu qu'évaluer une cellule dans un _notebook_ peut produire un
résultat. Cependant, cette méthode a des limites (par exemple, elle n'affiche
que le résultat de la dernière expression évaluée dans la cellule), et elle ne
fonctionne pas du tout en dehors des _notebook_. Plus généralement, on peut
afficher une valeur ou le contenu d'une variable en les passant en argument à
la fonction `print` :

```python
print(age)
print(3.14)
```

### Exécution conditionnelle
Pour l'exécution conditionnelle, Python utilise une syntaxe probablement assez
proche de ce que vous connaissez déjà, mais pas identique. Considérons la
cellule suivante :

```python
if age >= 18:
  print('Ils sont majeurs, ils ont', age, 'ans.')
else:
  print('Ils ne sont pas majeurs.')
```

```{margin}
L'indentation peut se faire avec n'importe quel nombre d'espaces ou de
tabulations, tant qu'on ne mélange pas les deux et que l'on garde le même choix
dans tout le bloc. Il y a des arguments pour et contre chaque option, et c'est
un sujet qui divise fortement les développeurs &mdash; une vraie guerre de
préférences. Personnellement, je ne prends pas parti : cela relève souvent du
goût personnel, sauf si votre environnement de travail impose un choix. Quelle
que soit l'option retenue, la cohérence est essentielle.
```

La sélection se fait avec l'instruction `if`, suivie d'une condition et d'un
deux-points (`:`). Le bloc exécuté quand la condition est vraie doit être
indenté de manière cohérente. Le mot-clé `else` indique un bloc alternatif si
la condition est fausse, en utilisant la même syntaxe[^one-liner]. Notez que
l'exemple ci-dessus illustre que :

- il n'est pas nécessaire d'entourer la condition de parenthèses ;
- la fonction `print` permet d'afficher des messages sous forme de chaînes
  entre apostrophes ;
- on peut passer un nombre variable d'arguments à `print`, qui seront affichés
  séparés par des espaces.

### Définir des fonctions
La cellule suivante montre comment définir une fonction qui prend un argument
(interprété comme l'âge d'une personne) et renvoye un booléen indiquant si la
personne est majeure, après avoir affiché un message similaire à celui vu
précédemment :

```{margin}
Notez que l'exécution produit deux cellules, chacune ayant un but différent :
la première contient le message montré par `print`, la seconde contient la
valeur renvoyée par `check_age`. Mélanger ainsi sortie standard et valeur de
retour n'est __pas__ une bonne pratique[^bad-practice], mais ici cela me permet
d'introduire plusieurs notions importantes dans un exemple concis.
```

```python
def check_age(age):
  if age >= 18:
    print('Ils sont majeurs, ils ont', age, 'ans.')
    return True
  else:
    print('Ils ne sont pas majeurs.')
    return False

check_age(age)
```

Cet exemple montre aussi que :

- une définition de fonction commence par `def`, suivi du nom, d'une paire de
  parenthèses contenant les paramètres, et d'un deux-points ;
- les types d'arguments ne sont pas déclarés, en raison du typage dynamique ;
- le corps de la fonction est indenté, et les blocs `if` et `else` sont
  indentés davantage ;
- l'instruction `return` marque la fin d'exécution et précise la valeur
  renvoyée ;
- les constantes `True` et `False` représentent les deux valeurs booléennes.

L'avantage principal de définir une fonction est bien sûr de pouvoir la
réutiliser avec différents arguments, comme ici :

```python
check_age(13)
```

### Importer des modules
En Python, la réutilisation et les projets complexes reposent sur les
_modules_. Un module est un fichier définissant des variables, fonctions ou
classes. On peut importer tout un module ou seulement certains éléments. C'est
particulièrement utile avec les bibliothèques standard ou tierces. Prenons le
module `math`, distribué avec Python, qui définit par exemple `pi` (une
approximation de $\pi$) et `factorial` (factorielle d'un entier). On peut les
_importer_ avec la syntaxe `from <module> import <nom>` :

```{margin}
On peut aussi importer plusieurs éléments d'un module en une seule
instruction.
```

```python
from math import factorial, pi

print(pi)
print(factorial(10))
```

```{margin}
On peut définir des alias avec `from <module> import <element> as <alias>`.
```

Quand différents modules contiennent des éléments ayant le même nom, on peut
éviter les conflits grâce aux _espaces de noms_ : on importe le module entier
avec `import <module>` et on accède aux éléments avec la notation pointée.

```python
import math

print(math.pi)
print(math.factorial(10))
```

Ainsi, si `m1` et `m2` contiennent un élément `e`, il n'y a pas de conflit car
on les appelle `m1.e` et `m2.e`. Cependant, écrire le nom du module à chaque
fois peut rendre le code moins lisible. On peut alors utiliser un alias avec
`import <module> as <alias>`. C'est ce que j'utiliserai pour
[numpy](http://www.numpy.org){.external},
[pandas](http://pandas.pydata.org){.external} et
[matplotlib](http://matplotlib.org){.external} :

```{margin}
Comme dans la troisième ligne, certains modules (comme matplotlib) sont
structurés en paquets, un peu comme en Java.
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

```{admonition} Conventions de nommage
:class: naming
Importer numpy, pandas et `pyplot` avec `np`, `pd` et `plt` est une convention
universellement acceptée. Il est fortement recommandé de la suivre, pour que
les lecteurs identifient immédiatement le module.
```

### Erreurs et exceptions
Python gère les erreurs en levant des _exceptions_, comme en Java. L'exemple
ci-dessous montre une `NameError` levée lorsqu'on référence une variable non
initialisée :

```{margin}
La sortie d'erreur, ou _stack trace_, est détaillée : elle montre la portion
de code impliquée, liste éventuellement la séquence d'appels, et précise le
type d'exception et un message associé.
```

```python
print(uninitialized_variable)
```

Une exception interrompt normalement l'exécution, mais on peut écrire du code
qui s'exécute automatiquement lorsqu'une exception spécifique survient dans un
bloc. Je ne détaille pas cela ici ; je vous invite à consulter la
[documentation
officielle](https://docs.python.org/3/tutorial/errors.html){.external}, qui
fournit plus de détails à ce sujet.

Certaines erreurs ne peuvent pas être gérées par exceptions : par exemple, les
erreurs de syntaxe, lorsque l'analyseur ne reconnaît pas une ligne de code.

## Exercices

[^compilateurs]: On demande souvent si Python est interprété ou compilé. Cela
dépend de l'implémentation, mais la réponse la plus juste est : « ni l'un ni
l'autre ». Python compile en _bytecode_, comme Java, pour une _machine
virtuelle_. Avec CPython &mdash; l'implémentation visée par ce livre &mdash; la
compilation est automatique et transparente à l'import d'un module (voir
{ref}`sec_importer-modules`) : cela produit des fichiers `.pyc` dans un
répertoire `__pycache__`, créé s'il n'existe pas ou est plus vieux que le
source ; sinon, le bytecode est exécuté directement.
[^environnement]: Il existe plusieurs solutions pour créer et gérer des
environnements virtuels. À ce jour,
[Anaconda](https://docs.anaconda.com/anaconda/){.external} et
[Miniconda](https://docs.anaconda.com/miniconda/){.external} sont parmi les
plus utilisées avec `venv`.
[^package-manager]: Anaconda et Miniconda, cités ci-dessus, fournissent aussi
leur propre gestionnaire de paquets, utilisable à la place de pip.
[^nb-lang]: Les notebook ne sont pas liés à un langage spécifique. On peut y
installer un ou plusieurs _kernels_, chacun dédié à un langage. Je travaillerai
surtout en Python, mais nous verrons parfois comment exécuter des commandes
shell sans ouvrir de terminal.
[^prononcer-jupyter]: Fernando Perez, un des créateurs de Jupyter, le prononce
ainsi dans sa
[conférence](https://www.youtube.com/watch?v=cc2hHjARNTY){.external} à PLOTCON
2016.
[^jupytext]: Inclure directement des notebook dans un dépôt git est
déconseillé. On peut utiliser
[jupytext](https://jupytext.readthedocs.io/){.external} pour les synchroniser
automatiquement avec du code Python équivalent.
[^one-liner]: Il est possible d'écrire un `if` sur une seule ligne, mais cela
nuit souvent à la lisibilité.
[^bad-practice]: En principe, une fonction ne devrait pas afficher à l'écran,
sauf pour des avertissements ou erreurs. Même alors, il vaut mieux utiliser des
mécanismes comme la journalisation ou les exceptions, pour éviter de confondre
les lecteurs et faciliter les tests.
