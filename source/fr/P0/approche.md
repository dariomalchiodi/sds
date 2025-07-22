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

(chap:apprach)=
# Approche

J'ai toujours eu facilité à apprendre de nouveaux concepts en les mettant en
pratique dans un contexte facile à explorer et à contrôler. Lorsque, il y a
un moment, j'ai commencé à enseigner, il m'a paru naturel d'adopter la même
approche, adoptant inconsciemment une méthode d'enseignement que seulement plus
tard j'ai découverte comme codifiée dans la méthodologie du _learning by doing_
{cite:p}`freire1982`. Ce livre essaie de suivre la même philosophie, en
introduisant les sujets dès le départ&mdash;lorsque c'est possible&mdash;dans
un contexte orienté application.

```{margin}
L'utilisation de la science-fiction pour introduire des concepts scientifiques
n'est pas   particulièrement inhabituelle : deux exemples assez connus sont
« La Physique de Star Trek »   {cite:p}`krauss` et « La Physique des
Super-héros » {cite:p}`kakalios`[^note].
```

Pour assurer la cohérence dans le développement, j'ai décidé d'encadrer les
exemples utilisés en parallèle aux parties plus théoriques dans un seul
domaine. Le champ que j'ai choisi est le multivers des super-héros. Cela peut
sembler paradoxal, étant donné la philosophie que je viens d'énoncer : les
super-héros sont des personnages d'une histoire fictive—hautement fictive,
même. Cependant, la capacité d'appliquer un concept à un contexte ne dépend  
pas de sa réalisabilité physique : il suffit que les hypothèses décrivant une  
situation donnée soient énoncés clairement, de façon cohérente et précisément.
Cela permet de se plonger métaphoriquement dans cette situation, d'utiliser les
mathématiques pour la modéliser et l'informatique pour la simuler, permettant
ainsi son exploration par la méthode scientifique, dans l'espoir d'en tirer des
informations utiles, de prendre des décisions, etc. En plus du côté ludique,
se référer à un monde inexistant présente un autre avantage : cela aide les  
apprenants à éviter d'établir un lien direct entre un problème donné et les
méthodes résolutives à utiliser, favorisant un apprentissage centré sur
l'utilisation _critique_ des méthodes et outils.

Bien que je me sois lancé dans cette entreprise, je ne suis pas un expert en
super-héros. Je m'excuse d'avant auprès de ceux qui en savent plus que moi pour
toutes les imperfections ou erreurs que j'aurais pu inclure, en espérant que
celles-ci ne rendent pas   plus difficile la compréhension des concepts et des
exemples présentés. Bien que j'aie un peu plus d'expérience en analyse de
données, probabilité et statistiques, je ne peux garantir qu'il n'y ait aucune
inexactitude dans l'ensemble, même si dans ce cas je suis confiant qu'il  
n'y en a pas trop.

Le travail d'écriture est encore _en cours_, et le restera probablement pendant
un certain temps : merci de signaler les coquilles et les erreurs, et plus
généralement tout exemple ou matériel que vous pensez pouvoir enrichir ce que
j'ai écrit, en gardant à l'esprit que les images, données, etc., ne peuvent
être publiés que s'ils sont compatibles avec la licence  
_Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International_  
([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en))
sous laquelle ce livre est distribué. La façon la plus pratique de m'envoyer
ces indications est de soumettre des _issues_ (pour mettre en évidence erreurs
ou suggérer des améliorations) ou des _pull requests_ (pour proposer des
modifications de contenu) au 
[référentiel](https://github.com/dariomalchiodi/sds) dans lequel j'ai organisé
le contenu de ce livre. Cela nécessite une certaine familiarité avec  
[git](https://www.git-scm.org), l'outil de _gestion de contrôle de version_ que
j'utilise pour   mes projets logiciels.


[^note]: J'utiliserai les notes en marge pour des commentaires que je
considère importants mais qui ne doivent pas alourdir la lecture principale des
paragraphes correspondants. Je reporterai en revanche en notes de fin toutes
les discussions approfondies pouvant être ignorées lors d'une première lecture.
