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

(sec_statistique-science-donnees)=
# Statistique, science des données et autres étiquettes

Dans le passé, les données étaient souvent considérées comme un sous-produit de
procédures opérationnelles &mdash; parfois informatisées &mdash; principalement
destinées à l’archivage et rarement réutilisées. L’idée selon laquelle les
données constituent une ressource stratégique dans presque tous les domaines de
la connaissance humaine ne s’est imposée que depuis une vingtaine d’années.
Aujourd’hui, il est pleinement reconnu que, lorsqu’elles sont collectées,
stockées et traitées de manière systématique, elles deviennent des outils
essentiels pour analyser des processus complexes, nous aider à les comprendre
et soutenir des décisions dans des contextes critiques comme la médecine, la
politique ou la finance.

```{margin}
Après l’intervention de John Snow, les infections ont effectivement diminué.
Cette baisse doit toutefois être interprétée dans un contexte plus large : de
nombreuses personnes avaient déjà quitté le quartier pour se mettre à l’abri.
En tout état de cause, les découvertes médicales ultérieures ont confirmé
l’intuition de Snow sur la manière dont la maladie se transmettait.
```

Et pourtant, certains exemples remarquables montrent qu’une approche
_guidée par les données_ existait déjà au XIXe siècle, bien avant que le terme
ne soit forgé. L’un des plus célèbres remonte à 1854, lors d’une épidémie de
choléra à Londres. Le médecin John Snow, convaincu que la maladie ne se
transmettait pas par l’air &mdash; alors que les médecins de son époque
incriminaient les _miasmes_, ou le _mauvais air_ &mdash;, décida de rassembler
des preuves à l’appui d’une autre hypothèse : la contamination de l’eau. Pour
cela, il superposa sur une carte du quartier de Soho le nombre d’infections
enregistrées dans chaque maison[^cartographie]. Le résultat, visible dans la
{numref}`john-snow`, montra que les cas étaient concentrés près d’une pompe à
eau située sur Broad Street. Pour renforcer sa thèse, Snow observa aussi que
les brasseurs, qui buvaient davantage de bière que d’eau &mdash; et consommaient
donc un produit pasteurisé &mdash; étaient moins touchés par la maladie. Grâce
à ces éléments, il convainquit les autorités de désactiver la pompe, ce qui
contribua à endiguer l’épidémie.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/2/27/20201116211939%21Snow-cholera-map-1.jpg
:width: 60%
:name: john-snow

Carte du quartier de Soho dessinée par John Snow pendant l’épidémie de choléra
de 1854 : chaque barre noire horizontale indique une infection enregistrée dans
la maison adjacente. Image du domaine public. Réalisée par John Snow (1854).
Source : {extlink}`Wikimedia Commons </sds/short/cholera-map>`.
```

Fait plus curieux encore, le second exemple date lui aussi de 1854. Cette
année-là, Florence Nightingale part pour la Crimée, où une guerre oppose la
Russie et l’Empire ottoman, avec la participation de plusieurs puissances
européennes, dont le Royaume-Uni. Nightingale y arrive dans son rôle de
surintendante de l’Institute for Sick Gentlewomen, accompagnée d’autres
infirmières volontaires. Afin de documenter les carences dans la gestion des
soins médicaux, elle décide de recueillir des données sur l’état de santé des
soldats. En 1858, elle présente les résultats dans un rapport intitulé « Notes
on Matters Affecting the Health, Efficiency and Hospital Administration of the
British Army ». Ce document contient un _diagramme polaire_[^polaire],
reproduit en {numref}`florence-nightingale`, aujourd’hui considéré comme un
exemple classique de visualisation efficace des données. Le graphique se
compose de deux aires circulaires divisées en douze secteurs correspondant aux
mois d’avril 1854 à mars 1855 (à gauche) et d’avril 1855 à mars 1856 (à
droite). La surface de chaque secteur représente le nombre de décès, répartis
en trois catégories :

- blessures de guerre (rouge),
- maladies curables ou évitables (bleu),
- autres causes (noir).

L’effet visuel est immédiat : la plupart des décès n’étaient pas dus aux
combats. Nightingale s’appuya sur ce constat pour dénoncer l’inefficacité des
hôpitaux de campagne, dont les conditions insalubres entraînaient la diffusion,
chez les soldats, de maladies comme le choléra, le typhus ou la dysenterie. Ce
fut aussi grâce à cette intervention que le système de santé militaire fut plus
tard réformé.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/1/17/20201105141904%21Nightingale-mortality.jpg
:width: 100%
:name: florence-nightingale

Diagrammes polaires montrant les décès de soldats britanniques entre avril 1854
et mars 1856 dans l’hôpital militaire où Florence Nightingale exerçait. Chaque
secteur représente un mois, avec une aire proportionnelle au nombre de morts,
tandis que les couleurs indiquent la cause du décès : rouge pour les blessures
de guerre, bleu pour les maladies curables et noir pour les autres causes.
Image du domaine public. Réalisée par Florence Nightingale (1858). Source :
{extlink}`Wikimedia Commons <https://malchiodi.com/sds/short/nightingale-source>`.
```

Les cas de Snow et de Nightingale montrent très clairement une approche
descriptive de l’analyse des données : collecter et présenter l’information avec
précision permet de mettre en lumière des aspects pertinents d’un phénomène
&mdash; ici les causes des contagions de choléra et des décès de soldats
&mdash; et de fournir des bases solides pour prendre des décisions éclairées.
À partir de la fin du XIXe siècle, toutefois, la statistique s’est aussi
développée sur un plan plus théorique et quantitatif. Sans prétendre à
l’exhaustivité, citons deux figures fondamentales : Ronald A. Fisher, qui a
joué un rôle central dans l’élaboration des méthodes de la statistique moderne
et de leurs applications à la génétique et à la production agricole, et William
Gossett, qui a mis au point des techniques permettant de contrôler la qualité
de la bière Guinness sans compromettre l’ensemble de la production. Pour des
raisons de confidentialité, Gossett publia ses résultats sous le pseudonyme
« Student », afin que les concurrents de son employeur ne découvrent pas les
méthodes innovantes utilisées dans la brasserie.

Avec l’avènement des ordinateurs, à partir des années 1940, on s’est vite rendu
compte qu’ils pouvaient servir non seulement à mécaniser certaines opérations,
mais aussi à générer et à stocker de grandes quantités de données. Avec le
temps et le développement des technologies associées, la puissance de calcul a
augmenté, les coûts de stockage ont baissé et la diffusion d’internet a rendu
les données plus accessibles. Ces facteurs ont entraîné une augmentation
drastique de leur volume, ce qui en a accru la valeur.

À la charnière des XXe et XXIe siècles, le rôle de _data scientist_ a émergé :
une personne capable d’intégrer des compétences en informatique et en
mathématiques/statistique avec la connaissance d’un domaine spécifique, et de
transformer ainsi des données brutes en informations utiles, souvent dans une
optique de _business_. Mais qu’est-ce qui distingue vraiment une personne qui
travaille comme data scientist de quelqu’un qui travaille en statistique, en
informatique ou en mathématiques ? La réponse n’est pas immédiate.

Aujourd’hui, toutes ces personnes ont besoin d’une familiarité plus que
correcte avec des outils et des concepts relevant de l’informatique, en plus de
connaître au moins les bases de la statistique et des mathématiques. Pourtant,
ces profils restent distincts : les personnes qui travaillent en informatique
ne sont presque jamais les mêmes que celles qui travaillent en statistique ou
en mathématiques, et inversement. Par exemple, il existe des domaines de
l’informatique &mdash; comme les systèmes d’exploitation ou le développement
d’applications pour smartphones et terminaux mobiles &mdash; qui peuvent être
aisément ignorés dans des contextes typiques des mathématiques, de la
statistique ou de la science des données. De même, la plupart des informaticiens
ne s’aventurent pas dans des domaines comme la topologie ou les tests
d’hypothèses.

Je souligne également que, jusqu’ici, j’ai volontairement laissé de côté
l’intelligence artificielle. Il s’agit d’une discipline relativement récente,
mais qui exerce déjà un impact considérable sur la vie quotidienne. Bien qu’elle
croise souvent l’analyse de données, son objectif principal est l’étude et la
réplication automatique de processus qui, lorsqu’ils sont accomplis par des
êtres humains, requièrent une certaine forme d’intelligence. Dans certains cas,
ces processus reposent sur des raisonnements guidés par les données ; dans
d’autres, des approches complètement différentes sont nécessaires. C’est
précisément cette diversité d’objectifs et de méthodes qui fait de
l’intelligence artificielle une branche de l’informatique méritant un
traitement distinct des sujets abordés dans ce livre.

Ce livre vise à traiter des sujets allant de la programmation à l’analyse de
données, en passant par les probabilités et la statistique. C’est une
combinaison exigeante, mais cohérente avec le parcours d’études souvent
fragmenté des personnes qui étudient l’informatique. Le lire (et, ça va sans
dire, en comprendre le contenu) ne fera pas de vous des data scientists, ni
des spécialistes de statistique ou de mathématiques. À vrai dire, pas même des
spécialistes de l’informatique ou de l’intelligence artificielle. Mais il vous
donnera une base solide, l’une des briques nécessaires pour acquérir une
maîtrise aussi complète que possible de l’informatique et l’autonomie
professionnelle qui en découle &mdash; en bref, développer les compétences qui
font que l’on prend une personne au sérieux. En tout état de cause, je tiens à
souligner qu’au final, ce qui compte n’est pas l’étiquette professionnelle qui
nous est attribuée, mais ce que nous savons bien faire.

[^cartographie]: Bien que l’approche de Snow soit la plus célèbre, les
véritables pionniers de la _cartographie statistique_ furent les chercheurs
français André-Michel Guerry et Charles Dupin, qui utilisaient déjà, dans la
première moitié du XIXe siècle, des graphiques pour mettre en évidence des
différences entre les provinces de France en matière d’alphabétisation ou de
criminalité. Dupin fut le premier à introduire ce que nous appelons aujourd’hui
des {extlink}`cartes choroplèthes
<https://fr.wikipedia.org/wiki/Carte_choropl%C3%A8the>`, dans lesquelles les
régions d’une carte géographique sont colorées selon la valeur d’un indicateur
donné.

[^polaire]: Il convient de noter que les diagrammes polaires rendus célèbres
par Florence Nightingale avaient déjà été introduits en 1829 par André-Michel
Guerry (le même que dans la note précédente).
