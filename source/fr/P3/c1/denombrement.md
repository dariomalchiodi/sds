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

(sec_denombrement-combinatoire)=
# Dénombrement combinatoire

En Python, il est assez facile de générer tous les types de groupements vus
jusqu'ici. En particulier, le module `itertools` fournit des itérateurs
efficaces permettant de générer en séquence tous les groupements possibles d'un
type donné, sans jamais les charger tous en mémoire simultanément.

```{admonition} Itérateurs et mémoire
:class: tip
Les fonctions d'`itertools` renvoient des _itérateurs_, pas des listes. Les
éléments sont générés un à un, à la demande, sans jamais charger la totalité de
la séquence en mémoire. C'est particulièrement avantageux lorsque $n$ et $k$
sont grands : par exemple, sélectionner toutes les équipes de 5 héros parmi les
50 personnages de l'Univers Cinématographique Marvel produirait
$c_{50,5} = $ <span style="word-spacing: -0.1rem">2 118 760</span> combinaisons. En supposant que décrire une équipe nécessite
de spécifier un identifiant entier pour chaque membre, matérialiser toutes les
équipes possibles dans une liste nécessiterait probablement plusieurs dizaines de
mégaoctets de RAM, alors que l'approche basée sur les itérateurs ne garderait
qu'une seule équipe en mémoire à tout moment — nécessitant environ vingt octets !

Si une application nécessitait de sauvegarder toutes les descriptions en mémoire
— par exemple parce que certains traitements des équipes ne peuvent pas être
effectués séquentiellement — les itérateurs peuvent être explicitement convertis
en listes à l'aide de `list`.
```

## Permutations simples

Les objets de la classe `itertools.permutations` sont des itérateurs qui, lors
de leur parcours, génèrent toutes les permutations simples des éléments contenus
dans l'objet utilisé pour instancier la classe. Par exemple, l'exécution de la
cellule suivante produit une liste des permutations possibles des Quatre
Fantastiques, analogue au {numref}`permutations-quatre-fantastiques-fr` :

```{code-cell} python
import itertools as it

fantastic_4 = ['f', 'i', 't', 'c']
for i, p in enumerate(it.permutations(fantastic_4)):
    print(p, end='\n' if (i+1) % 3 == 0 else '  ')
```

Autrement dit, le code précédent génère toutes les $p_4 = 24$ permutations des
quatre membres de l'équipe.

## Permutations avec répétition

Le module `itertools` n'offre pas la possibilité de générer directement toutes
les permutations avec répétition d'un ensemble d'objets discernables par groupes.
Il est toutefois assez facile d'obtenir ces permutations à partir des permutations
simples en filtrant les doublons[^sympy], par exemple en insérant les permutations
dans un ensemble, de façon à pouvoir ignorer leurs occurrences ultérieures. La
cellule suivante utilise une approche de ce type pour produire une liste similaire
au {numref}`permutations-objets-indiscernables-fr` :

```{code-cell} python

clones = ['k', 'k', 'p', 'p', 'p']
seen = set()
for t in it.permutations(clones):
    if t not in seen:
        print(t, end='\n' if (len(seen)+1) % 3 == 0 else '  ')
        seen.add(t)
```

## Arrangements avec répétition

Il est facile de voir que les arrangements avec répétition des éléments d'un
ensemble $A$ en $k \in \mathbb N$ cases sont exactement les éléments du produit
cartésien

```{math}
A^k = \underbrace{A \times A \times \cdots \times A}_{\text{$k$ fois}} \enspace,
```

et qu'ils peuvent donc être obtenus directement en générant les éléments du
produit cartésien itéré, ce qui se fait facilement à l'aide de l'itérateur
renvoyé par `itertools.product`, qui, appelé avec le paramètre optionnel
`repeat`, calcule le produit d'un ensemble avec lui-même un nombre donné de fois.
La cellule suivante montre comment reproduire ainsi les arrangements avec
répétition du {numref}`tab-fr-arrangements-avec-repetition`.

```{code-cell} python
alpha_flight = ['g', 's', 'n', 'a']
for i, d in enumerate(it.product(alpha_flight, repeat=3)):
    print(d, end='\n' if (i+1) % 4 == 0 else '  ')
    if i == 15:
        break
```

Ce code n'affiche pas les $D_{4, 3} = 64$ arrangements avec répétition en
totalité, car la boucle `for` est forcée de s'arrêter après en avoir considéré
$16$, afin d'éviter une sortie inutilement longue.

## Arrangements simples

Grâce à la relation entre permutations simples et arrangements simples, ces
derniers peuvent être générés à l'aide d'`itertools.permutations`, en spécifiant
un second argument indiquant le nombre de cases. Par exemple, dans la cellule
suivante sont produits tous les $d_{4, 3} = 24$ arrangements simples mis en
évidence en gras dans le {numref}`tab-fr-arrangements-avec-repetition`.

```{code-cell} python

for i, d in enumerate(it.permutations(alpha_flight, 3)):
    print(d, end='\n' if (i+1) % 4 == 0 else '  ')
```

## Combinaisons

Le module `itertools` contient deux classes `combinations` et
`combinations_with_replacement` dont les objets sont des itérateurs sur les
combinaisons — simples et avec répétition, respectivement. Par exemple, la
cellule suivante affiche les combinaisons simples de trois des pouvoirs de Peter
Petrelli (voir {prf:ref}`ex-fr-peter-petrelli`), dans le cas où ceux-ci peuvent
être choisis parmi un groupe de cinq super-pouvoirs.

```{code-cell} python
powers = ['telepathy', 'invisibility', 'psychokinesis',
          'regeneration', 'precognition']
for c in it.combinations(powers, 3):
    print(c)
```

De même, le code ci-dessous génère toutes les combinaisons avec répétition
considérées dans le {numref}`tab-fr-combinaisons-DK-MP`.

```{code-cell} python
for c in it.combinations_with_replacement(['k','p'], 4):
    print(c)
```



[^sympy]: En principe, une approche légèrement plus efficace consiste à itérer
sur `dict.fromkeys(it.permutations(clones))`, un dictionnaire factice créé à la
volée en utilisant les tuples décrivant les permutations comme clés, toutes
associées à `None`. Ainsi, les doublons sont automatiquement exclus, car insérer
une paire clé-valeur pour une clé déjà présente l'écrase simplement. Si
l'implémentation Python utilisée est, disons, écrite en C, créer le dictionnaire
prend moins de temps que créer et utiliser l'ensemble qui collecte les tuples
distincts. En pratique, les deux approches ont une efficacité très faible lorsque
le nombre d'objets est grand mais qu'il y a peu d'objets distincts, car
`it.permutations` génère toujours _toutes_ les permutations simples avant de
filtrer. Pour contourner cet inconvénient, le module `sympy.utilities.iterables`
contient le générateur `multiset_permutations`, qui énumère efficacement
uniquement les permutations distinctes.

## Exercices

````{exercise} •
:label: ex-fr-gen-titans-gardes

Générez et affichez toutes les façons d'attribuer trois gardes de patrouille aux
cinq [Teen Titans](https://dc.fandom.com/wiki/Teen_Titans) (Robin, Starfire,
Raven, Beast Boy, Cyborg), en pouvant assigner plus d'une garde au même
super-héros. Comptez et affichez également le nombre total de plannings possibles.
````
````{solution} ex-fr-gen-titans-gardes
:class: dropdown

Chaque attribution correspond à un arrangement avec répétition des cinq Teen
Titans en trois cases : le même super-héros peut assurer plus d'une garde (d'où
la nécessité de considérer les répétitions), et l'ordre des gardes est important
— être assigné à la première garde est différent d'être assigné à la deuxième ou
à la troisième (d'où l'utilisation des arrangements).

```{code-cell} python
titans = ['Robin', 'Starfire', 'Raven', 'Beast Boy', 'Cyborg']
count = 0
for t in it.product(titans, repeat=3):
    print(t)
    count += 1
print(f'Il y a en tout {count} façons différentes d\'attribuer les gardes.')
```
````

````{exercise} •
:label: ex-fr-gen-titans-compte

Si dans l'exercice précédent la seule exigence avait été de compter le nombre de
plannings différents sans les afficher, y aurait-il eu des façons plus efficaces
de répondre à la question ?
````
````{solution} ex-fr-gen-titans-compte
:class: dropdown

Puisqu'on considère des arrangements avec répétition de cinq objets en trois
cases, on sait qu'il y en a exactement $D_{5, 3} = 5^3 = 125$. Cet argument
permet de répondre à la question en calculant une seule exponentiation.
````

````{exercise} •
:label: ex-fr-gen-watchmen-paires

Générez et affichez toutes les paires possibles formées à partir des six membres
des [Watchmen](https://dc.fandom.com/wiki/Watchmen) (Rorschach, Hibou de Nuit,
Spectre de Soie, Ozymandias, Docteur Manhattan, Comédien).
````
````{solution} ex-fr-gen-watchmen-paires
:class: dropdown

```{code-cell} python
watchmen = ['Rorschach', 'Nite Owl', 'Silk Spectre',
            'Ozymandias', 'Dr Manhattan', 'Comedian']

for c in it.combinations(watchmen, 2):
    print(c)
```
````

````{exercise} •
:label: ex-fr-gen-dk-mp-repetition

Calculez combien de combinaisons avec répétition de Dupli-Kate et Multi-Paul en
quatre cases contiennent au moins un clone de Kate.
````
````{solution} ex-fr-gen-dk-mp-repetition
:class: dropdown

```{code-cell} python
count = 0
for c in it.combinations_with_replacement(['k', 'p'], 4):
    if 'k' in c:
        count += 1
print(f'Exactement {count} combinaisons contiennent au moins un clone de Kate.')
```
````

````{exercise} •
:label: ex-fr-gen-dk-mp-repetition-comp

Reconsidérez l'exercice précédent en le résolvant à l'aide d'une _compréhension
de liste_.
````
````{solution} ex-fr-gen-dk-mp-repetition-comp
:class: dropdown

```{code-cell} python
count = len([1 for c in it.combinations_with_replacement(['k', 'p'], 4)
               if 'k' in c])
print(f'Exactement {count} combinaisons contiennent au moins un clone de Kate.')
```
````

````{exercise} •
:label: ex-fr-gen-iter-vs-liste

Comptez combien d'arrangements avec répétition des $21$ membres réguliers de la
[Légion des Super-Héros](https://dc.fandom.com/wiki/Legion_of_Super-Heroes_(Earth-Prime))
en $3$ cases satisfont la condition que les première et troisième cases soient
occupées par le même héros, sans stocker la liste complète en mémoire.
````
````{solution} ex-fr-gen-iter-vs-liste
:class: dropdown

```{code-cell} python
count = sum(1 for d in it.product(range(21), repeat=3) if d[0] == d[2])
print(f'Dans exactement {count} cas le même héros apparaît en première '
      'et en dernière position.')
```

Le résultat est $21^2 = 441$ : la première case a $21$ choix, la deuxième
également, alors que la troisième est contrainte à correspondre à la première.
````

````{exercise} ••
:label: ex-fr-gen-alpha-flight-sans-guardian

Combien d'arrangements simples des quatre membres d'Alpha Flight (voir
{prf:ref}`ex-fr-arrangements-avec-repetition-1`) en trois cases excluent
Guardian ? Vérifiez la réponse expérimentalement en générant tous les
arrangements et en comptant ceux qui l'excluent.
````
````{solution} ex-fr-gen-alpha-flight-sans-guardian
:class: dropdown

Exclure Guardian revient à ne pas considérer l'un des objets possibles, et donc
à se concentrer sur les arrangements simples de trois objets en trois cases, qui
sont au nombre de $d_{3, 3} = 6$, comme le confirme le code ci-dessous.

```{code-cell} python
alpha_flight = ['g', 's', 'n', 'a']
no_g = [d for d in it.permutations(alpha_flight, 3) if 'g' not in d]
print(f'Le nombre d\'arrangements n\'incluant pas Guardian est {len(no_g)}')
```
````

````{exercise} ••
:label: ex-fr-verifier-formule

Écrivez une fonction `compute_combinatorics(n, k)` qui, à l'aide des itérateurs
d'`itertools`, compte le nombre d'arrangements avec répétition, d'arrangements
simples et de combinaisons simples de `n` objets en `k` cases. La fonction doit
renvoyer un dictionnaire dont les clés sont les chaînes `'D'`, `'d'` et `'c'`,
associées respectivement aux arrangements avec répétition, aux arrangements
simples et aux combinaisons. Vérifiez que la fonction se comporte correctement
lorsque les arguments `n` et `k` valent respectivement $5$ et $3$.
````
````{solution} ex-fr-verifier-formule
:class: dropdown

Bien que les valeurs requises pourraient être calculées directement, le problème
demande explicitement l'utilisation d'itérateurs. Il est donc possible d'utiliser
des générateurs basés sur ceux-ci, produisant la valeur constante $1$ pour chaque
groupement considéré. Sommer les valeurs générées donne les nombres requis.

Le problème ne spécifie pas quels objets considérer, seulement combien. Comme
les indices combinatoires ne dépendent pas de la nature spécifique des objets,
on peut utiliser des entiers de $0$ à la valeur de `n`, produits efficacement
par `range`.

```{code-cell} python
def compute_combinatorics(n, k):
    objects = range(n)
    disp_repeat = sum(1 for _ in it.product(objects, repeat=k))
    disp_simple = sum(1 for _ in it.permutations(objects, k))
    comb = sum(1 for _ in it.combinations(objects, k))
    return {'D': disp_repeat, 'd': disp_simple, 'c': comb}
```

En appliquant les formules correspondantes pour les deux types d'arrangements et
pour les combinaisons, il est facile d'obtenir $D_{5, 3} = 125$,
$d_{5, 3} = 60$ et $c_{5, 3} = 10$, que l'on peut vérifier par de simples
assertions.

```{code-cell} python
result = compute_combinatorics(5, 3)

assert result['D'] == 125
assert result['d'] == 60
assert result['c'] == 10
```
````

````{exercise} ••
:label: ex-fr-gen-dk-clones-anagrammes

Générez toutes les permutations des objets du multiensemble contenant deux clones
de Dupli-Kate et trois clones de Multi-Paul, en insérant toutes les permutations
simples dans un ensemble.
````
````{solution} ex-fr-gen-dk-clones-anagrammes
:class: dropdown

Dans la section sur les permutations avec répétition, les permutations étaient
insérées dans un ensemble _après_ avoir été utilisées, pour éviter de les
reconsidérer ultérieurement. Ici, en revanche, il est demandé d'utiliser
l'ensemble pour agréger les permutations, peut-être pour un usage futur.
L'approche la plus directe consiste à énumérer les permutations simples en les
insérant toutes dans l'ensemble : cette opération gère automatiquement les
doublons, car insérer un élément déjà présent dans un ensemble n'a aucun effet.

```{code-cell} python
clones = ['k', 'k', 'p', 'p', 'p']
distinct = set()
for p in it.permutations(clones):
    distinct.add(p)
print(distinct)
```

En fait, il est possible de réécrire ce code de manière bien plus concise. Les
constructeurs de presque tous les types de données structurées que nous avons
étudiés acceptent des itérateurs comme arguments, qui sont parcourus
automatiquement en insérant progressivement les éléments générés dans la
structure. Dans notre cas, cela permet de réécrire la cellule précédente comme
ci-dessous.

```{code-cell} python
clones = ['k', 'k', 'p', 'p', 'p']
distinct = set(it.permutations(clones))

print(distinct)
```
````

````{exercise} ••
:label: ex-fr-gen-doom-patrol-islice

Lisez la
[documentation](https://docs.python.org/3/library/itertools.html#itertools.islice)
de la classe `itertools.islice` et utilisez-la pour générer et afficher
seulement dix permutations simples des cinq membres du
[Doom Patrol](https://dc.fandom.com/wiki/Doom_Patrol) (Robotman, Negative Man,
Elasti-Girl, Crazy Jane, Flex Mentallo), sans générer ni parcourir les $5! - 10
= 110$ permutations restantes.
````
````{solution} ex-fr-gen-doom-patrol-islice
:class: dropdown

La classe `islice` construit un itérateur à partir d'un autre itérateur, en
extrayant une sous-séquence. Dans sa forme la plus simple, le constructeur prend
l'itérateur source et un entier $n$ : l'itérateur renvoyé ne produira que les
premiers $n$ éléments de l'original.

```{code-cell} python
doom_patrol = ['Robotman', 'Negative Man', 'Elasti-Girl',
               'Crazy Jane', 'Flex Mentallo']
for p in it.islice(it.permutations(doom_patrol), 10):
    print(p)
```
````

````{exercise} ••
:label: ex-fr-gen-peter-pouvoirs-incompatibles

Affichez toutes les combinaisons de trois super-pouvoirs, choisis parmi
télépathie, invisibilité, télékinésie, régénération et précognition, en excluant
celles qui contiennent simultanément télépathie et télékinésie. Combien de telles
combinaisons y a-t-il ?
````
````{solution} ex-fr-gen-peter-pouvoirs-incompatibles
:class: dropdown

```{code-cell} python
powers = ['telepathy', 'invisibility', 'psychokinesis',
          'regeneration', 'precognition']
valid = [c for c in it.combinations(powers, 3)
          if not ('telepathy' in c and 'psychokinesis' in c)]
print(f'Il y a {len(valid)} combinaisons valides.')
```

Le nombre de combinaisons valides peut aussi être obtenu par le raisonnement
suivant : à partir des $c_{5, 3} = 10$ combinaisons totales, soustraire toutes
celles dans lesquelles deux des trois cases sont occupées par télépathie et
télékinésie ; comme la case restante peut contenir l'un des autres super-pouvoirs,
il y a exactement trois combinaisons à retirer. Il y aura donc sept combinaisons
valides.

````

````{exercise} •••
:label: ex-fr-gen-young-avengers-equipes

Écrivez un générateur Python qui, étant donné une liste de héros et un entier
$k$, produit toutes les paires d'équipes disjointes de $k$ héros chacune.
Vérifiez le comportement du générateur en utilisant les neuf
[Young Avengers](https://marvel.fandom.com/wiki/Young_Avengers) (Patriot,
Hulkling, Wiccan, Speed, Stature, Vision, Kate Bishop, Noh-Varr et Jonas) et
$k = 2$, en gardant à l'esprit que le nombre de paires d'équipes — dans ce cas
— doit être égal à $c_{9,2} \cdot c_{7,2} = 36 \cdot 21 = 756$.
````
````{solution} ex-fr-gen-young-avengers-equipes
:class: dropdown

```{code-cell} python
def disjoint_teams(heroes, k):
    for team_1 in it.combinations(heroes, k):
        remaining = [e for e in heroes if e not in team_1]
        for team_2 in it.combinations(remaining, k):
            yield team_1, team_2

young_avengers = ['Patriot', 'Hulkling', 'Wiccan', 'Speed',
                  'Stature', 'Vision', 'Kate Bishop', 'Noh-Varr', 'Jonas']
num_pairs = sum(1 for _ in disjoint_teams(young_avengers, 2))
assert num_pairs == 756
```
````
