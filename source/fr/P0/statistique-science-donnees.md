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

(sec_statistiques-science-donnees)=
# Statistiques, science des données et autres étiquettes

Dans le passé, les données étaient généralement considérées comme un
sous-produit des procédures opérationnelles (parfois automatisées)
principalement destinées à l'archivage, et rarement réutilisées dans les
processus de production. L'idée que les données constituent une ressource
cruciale dans presque tous les domaines de la connaissance humaine n’a été
largement acceptée que depuis une vingtaine d’années. On a alors pleinement
reconnu que, lorsqu'elles sont collectées, stockées et traitées de manière
systématique, les données deviennent des outils essentiels pour analyser des
processus complexes et appuyer la prise de décision éclairée dans des domaines
critiques comme la médecine, la politique ou la finance.

```{margin}
Il convient de noter qu'après l'intervention de John Snow, une baisse des
infections a effectivement été observée. Toutefois, ce déclin doit être
replacé dans un contexte plus large, notamment parce qu’une partie importante
de la population avait quitté le quartier pour se mettre en sécurité. Quoi
qu'il en soit, les découvertes ultérieures de la recherche médicale
confirmeront la validité de l’hypothèse de Snow sur les modes de transmission
de la maladie.
```

Il existe néanmoins des exemples historiques qui montrent que l'approche
_guidée par les données_ était déjà présente à la fin du XIXᵉ siècle. En 1854,
lors d'une épidémie de choléra à Londres, le médecin John Snow superposa à une
carte du quartier de Soho les informations relatives au nombre d’infections
dans chaque maison[^cartografie]. Le graphique obtenu, visible en
{numref}`john-snow`, met en évidence la concentration des cas autour d'une
pompe à eau située sur Broad Street. L’objectif de Snow était de contredire le
consensus médical de l'époque, selon lequel la maladie se transmettait par
l'air (on parlait de _miasmes_ ou d’_air vicié_), et d'appuyer plutôt
l'hypothèse selon laquelle la véritable cause était la contamination de l'eau.
Pour étayer son raisonnement, il observa également que les brasseurs&mdash;qui
consommaient plus de bière (pasteurisée) que d’eau&mdash;étaient moins touchés
par la maladie. Grâce à ces éléments, il réussit à convaincre les autorités de
désactiver la pompe, contribuant ainsi à contenir l'épidémie.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/2/27/20201116211939%21Snow-cholera-map-1.jpg
:width: 60%
:name: john-snow

Carte du quartier de Soho, à Londres, montrant le nombre d'infections dans
chaque maison (barres noires horizontales) pendant l'épidémie de choléra de
1854. Image du domaine public. Réalisée par John Snow (1854). Source :
[Wikimedia Commons](https://en.wikipedia.org/wiki/File:Snow-cholera-map-1.jpg).
```

Fait intéressant, le deuxième exemple remonte également à la même année. En
1854, Florence Nightingale se rend en mission en Crimée, où se déroule une
guerre entre la Russie et l'Empire ottoman, avec la participation de plusieurs 
uissances européennes, dont le Royaume-Uni. Nightingale, alors surintendante de
l'Institute for Sick Gentlewoman, y arrive avec un groupe d'infirmières
bénévoles. Constatant le manque d'organisation dans les soins médicaux apportés
aux soldats, elle collecte des données qu'elle présentera plus tard, en 1858,
dans un rapport intitulé _Notes on Matters Affecting the Health, Efficiency and
Hospital Administration of the British Army_. Ce document contient un célèbre
_diagramme polaire_[^polaire], reproduit en {numref}`florence-nightingale`,
souvent cité comme un exemple de visualisation efficace des données. Le
diagramme est composé de deux cercles, chacun divisé en douze secteurs
correspondant aux mois d’avril 1854 à mars 1855 et d’avril 1855 à mars 1856. La
surface de chaque secteur représente le nombre de décès mensuels parmi les
soldats, répartis en trois catégories :

- blessures de guerre (rouge),
- maladies évitables ou soignables (bleu),
- autres causes (noir).

Sans entrer dans les détails techniques, on constate que la majorité des décès
n'étaient pas liés aux combats. Nightingale utilisa ce constat pour dénoncer
l’état désorganisé des hôpitaux de campagne, dont les conditions sanitaires
déplorables favorisaient la propagation de maladies comme le choléra, le typhus
ou la dysenterie parmi les soldats. Cette intervention joua un rôle important
dans les réformes ultérieures du système de santé militaire.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/1/17/20201105141904%21Nightingale-mortality.jpg
:width: 100%
:name: florence-nightingale

Diagrammes polaires montrant les décès parmi les soldats britanniques entre
avril 1854 et mars 1856 à l’hôpital militaire où exerçait Florence Nightingale.
La surface de chaque secteur représente le nombre de morts, et les couleurs
indiquent la cause : rouge pour les blessures de guerre, bleu pour les maladies
évitables, et noir pour les autres causes. Image du domaine public. Réalisée
par Florence Nightingale (1858). Source :
<a href="/sds/short/nightingale-source" target="_blank">Wikimedia commons</a>.
```

Les cas de Snow et de Nightingale illustrent une approche descriptive de
l'analyse de données : une bonne collecte et présentation des informations
permet de mettre en évidence des aspects importants d'un phénomène (ici, les
causes des épidémies de choléra et de la majorité des décès de soldats), ce qui
aide à prendre des décisions éclairées. Parallèlement, dès la fin du XIXᵉ 
iècle, la statistique s'est développée dans une direction plus quantitative et
théorique. Sans prétendre à l'exhaustivité, on peut citer Ronald A. Fisher, qui
a joué un rôle central dans la définition des méthodes statistiques modernes et
dans leur application à la génétique et à l'agriculture, ainsi que William
Gossett, qui a développé des techniques statistiques pour contrôler la qualité
de la bière Guinness sans gaspiller toute la production. Il publia ses
résultats sous le pseudonyme « Student » pour éviter que les concurrents de son
employeur ne découvrent les méthodes innovantes utilisées dans la brasserie.

Avec l'arrivée des ordinateurs, utilisés dès les années 1940 pour automatiser
les tâches répétitives, on s'est vite aperçu qu'il était non seulement possible
de mécaniser des opérations, mais aussi de générer et stocker d’énormes
quantités de données. La montée en puissance des capacités de calcul, la baisse
des coûts de stockage et la diffusion d’internet ont rendu ces données plus
accessibles et en ont considérablement augmenté le volume&mdash;et donc la
valeur.

Vers le début du XXIᵉ siècle, le rôle de _data scientist_ émerge : un profil
capable de combiner des compétences en informatique et en statistique avec une
connaissance d'un domaine spécifique, pour transformer des données brutes en
informations utiles&mdash;souvent à visée commerciale. Mais qu'est-ce qui
distingue vraiment un data scientist d’un statisticien ou d’un informaticien ?

Il n'y a pas de réponse simple. Aujourd'hui, un statisticien doit maîtriser des
outils et concepts informatiques, tout comme un informaticien doit comprendre
certains fondements de la statistique et des mathématiques. Mais ces trois
rôles ne sont pas équivalents : un informaticien n'est presque jamais
statisticien ou mathématicien, et inversement. Il existe des domaines de
l'informatique, comme le développement de systèmes d’exploitation ou
d'applications mobiles, qu'un mathématicien peut totalement ignorer ; de même,
de nombreux informaticiens ne gardent qu'un souvenir flou de notions de
probabilités ou de statistiques, et ne s'aventureraient pas volontiers sur des
terrains comme la topologie ou les tests d'hypothèses.

Jusqu'ici, j'ai volontairement évité de parler d'intelligence artificielle
(IA), discipline relativement récente mais qui a un impact croissant dans
notre quotidien. Elle est souvent liée à l'analyse de données, mais son
objectif principal est d'étudier et de reproduire automatiquement des processus
qui, chez l'humain, mobilisent une forme d'intelligence. Dans certains cas, ces
processus s'appuient sur des raisonnements guidés par les données ; dans
d’autres, il faut recourir à des approches complètement différentes. C'est
justement cette diversité d’objectifs et de méthodes qui fait de l’IA un champ
distinct de l’informatique, méritant un traitement séparé de celui des sujets
abordés dans ce livre.

Ce volume traite de sujets allant de la programmation à l'analyse de données,
en passant par les probabilités et la statistique. Une combinaison ambitieuse,
mais cohérente avec le parcours souvent fragmenté des étudiants en
informatique. Le lire (et, ça va sans dire, en comprendre le contenu) ne fera
pas de vous un data scientist&mdash;ni un statisticien ou un mathématicien
d'ailleurs. Et pour être honnête, pas non plus un informaticien accompli ou un
expert en IA. Mais cela vous donnera une base solide, un des fondements
nécessaires pour devenir un informaticien compétent et bien formé&mdash;bref,
quelqu'un qu'on prend au sérieux. Au final, ce qui compte vraiment, ce n'est
pas l'étiquette qu'on vous colle, mais ce que vous savez bien faire.

[^cartografie]: Bien que l'approche de Snow soit la plus connue, les véritables
pionniers de la _cartographie statistique_ ont été les Français André-Michel
Guerry et Charles Dupin. Dès la première moitié du XIXᵉ siècle, ils ont utilisé
des graphiques pour mettre en évidence des différences entre les départements
français, par exemple en matière d’alphabétisation ou de criminalité. Dupin a
été le premier à introduire ce que nous appelons aujourd’hui les
[cartes choroplèthes](https://fr.wikipedia.org/wiki/Carte_choropl%C3%A8the), où
les régions d'une carte géographique sont colorées en fonction de la valeur
d'un indicateur donné.

[^polaire]: Il convient de noter que les diagrammes polaires rendus célèbres
par Florence Nightingale avaient déjà été introduits en 1829 par André-Michel
Guerry (le même que dans la note précédente).
