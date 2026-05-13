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

(sec_enumeracion-combinatoria)=
# Enumeración combinatoria

En Python es bastante fácil generar todos los tipos de agrupaciones vistos hasta
ahora. En particular, el módulo `itertools` proporciona iteradores eficientes que
permiten generar en secuencia todas las agrupaciones posibles de un tipo dado,
sin necesidad de cargar todas ellas en memoria simultáneamente.

```{admonition} Iteradores y memoria
:class: tip
Las funciones de `itertools` devuelven _iteradores_, no listas. Los elementos
se generan de uno en uno, solo cuando se solicitan, sin cargar jamás la secuencia
completa en memoria. Esto resulta especialmente ventajoso cuando $n$ y $k$ son
grandes: por ejemplo, seleccionar todos los equipos de 5 héroes entre los 50
personajes del Universo Cinematográfico Marvel produciría
$c_{50,5} = $ <span style="word-spacing: -0.1rem">2 118 760</span> combinaciones. Suponiendo que describir un equipo requiere
especificar un identificador entero para cada miembro, materializar todos los
equipos posibles en una lista requeriría probablemente varias decenas de
megabytes de RAM, mientras que el enfoque basado en iteradores solo mantendría
un único equipo en memoria en cada momento — ¡requiriendo aproximadamente veinte
bytes!

Si una aplicación necesitara guardar todas las descripciones en memoria — por
ejemplo, porque ciertos procesamientos de los equipos no pueden realizarse de
forma secuencial — los iteradores pueden convertirse explícitamente en listas
usando `list`.
```

## Permutaciones simples

Los objetos de la clase `itertools.permutations` son iteradores que, al
recorrerse, generan todas las permutaciones simples de los elementos contenidos
en el objeto utilizado para instanciar la clase. Por ejemplo, la ejecución de
la siguiente celda produce una lista de las permutaciones posibles de los Cuatro
Fantásticos, análoga a la {numref}`permutaciones-cuatro-fantasticos-es`:

```{code-cell} python
import itertools as it

fantastic_4 = ['f', 'i', 't', 'c']
for i, p in enumerate(it.permutations(fantastic_4)):
    print(p, end='\n' if (i+1) % 3 == 0 else '  ')
```

En otras palabras, el código anterior genera las $p_4 = 24$ permutaciones de
los cuatro miembros del equipo.

## Permutaciones con repetición

El módulo `itertools` no ofrece la posibilidad de generar directamente todas las
permutaciones con repetición de un conjunto de objetos distinguibles por grupos.
Sin embargo, es bastante fácil obtener estas permutaciones a partir de las
permutaciones simples filtrando los duplicados[^sympy], por ejemplo insertando
las permutaciones en un conjunto, de modo que puedan ignorarse sus apariciones
posteriores. La siguiente celda emplea un enfoque de este tipo para producir una
lista similar a la {numref}`permutaciones-objetos-indistinguibles-es`:

```{code-cell} python

clones = ['k', 'k', 'p', 'p', 'p']
seen = set()
for t in it.permutations(clones):
    if t not in seen:
        print(t, end='\n' if (len(seen)+1) % 3 == 0 else '  ')
        seen.add(t)
```

## Variaciones con repetición

Es fácil comprobar que las variaciones con repetición de los elementos de un
conjunto $A$ en $k \in \mathbb N$ casillas son exactamente los elementos del
producto cartesiano

```{math}
A^k = \underbrace{A \times A \times \cdots \times A}_{\text{$k$ veces}} \enspace,
```

y que, por tanto, pueden obtenerse directamente generando los elementos del
producto cartesiano iterado, lo cual se realiza fácilmente con el iterador
devuelto por `itertools.product`, que al invocarse con el parámetro opcional
`repeat` calcula el producto de un conjunto consigo mismo un número determinado
de veces. La siguiente celda muestra cómo reproducir de este modo las variaciones
con repetición de la {numref}`tab-es-variaciones-con-repeticion`.

```{code-cell} python
alpha_flight = ['g', 's', 'n', 'a']
for i, d in enumerate(it.product(alpha_flight, repeat=3)):
    print(d, end='\n' if (i+1) % 4 == 0 else '  ')
    if i == 15:
        break
```

Este código no imprime las $D_{4, 3} = 64$ variaciones con repetición en su
totalidad, porque el bucle `for` se ve obligado a detenerse tras considerar $16$
de ellas, para evitar una salida innecesariamente larga.

## Variaciones simples

Gracias a la relación entre permutaciones simples y variaciones simples, estas
últimas pueden generarse con `itertools.permutations`, especificando un segundo
argumento que indica el número de casillas. Por ejemplo, en la siguiente celda se
producen todas las $d_{4, 3} = 24$ variaciones simples destacadas en negrita en
la {numref}`tab-es-variaciones-con-repeticion`.

```{code-cell} python

for i, d in enumerate(it.permutations(alpha_flight, 3)):
    print(d, end='\n' if (i+1) % 4 == 0 else '  ')
```

## Combinaciones

El módulo `itertools` contiene dos clases `combinations` y
`combinations_with_replacement` cuyos objetos son iteradores sobre combinaciones
— simples y con repetición, respectivamente. Por ejemplo, la siguiente celda
imprime las combinaciones simples de tres de los poderes de Peter Petrelli (véase
{prf:ref}`ex-es-peter-petrelli`), en el caso en que estos puedan seleccionarse
entre un grupo de cinco superpoderes.

```{code-cell} python
powers = ['telepathy', 'invisibility', 'psychokinesis',
          'regeneration', 'precognition']
for c in it.combinations(powers, 3):
    print(c)
```

Análogamente, el código siguiente genera todas las combinaciones con repetición
consideradas en la {numref}`tab-es-combinaciones-DK-MP`.

```{code-cell} python
for c in it.combinations_with_replacement(['k','p'], 4):
    print(c)
```



[^sympy]: En principio, un enfoque ligeramente más eficiente consiste en iterar
sobre `dict.fromkeys(it.permutations(clones))`, un diccionario provisional creado
al vuelo usando las tuplas que describen las permutaciones como claves, todas
asociadas a `None`. De este modo, los duplicados se excluyen automáticamente,
porque insertar un par clave-valor para una clave ya presente simplemente lo
sobrescribe. Si la implementación de Python utilizada está escrita, por ejemplo,
en C, crear el diccionario lleva menos tiempo que crear y usar el conjunto que
recopila las tuplas distintas. En la práctica, ambos enfoques tienen una
eficiencia muy baja cuando el número de objetos es grande pero hay pocos objetos
distintos, porque `it.permutations` siempre genera _todas_ las permutaciones
simples antes de filtrar. Para superar este inconveniente, el módulo
`sympy.utilities.iterables` contiene el generador `multiset_permutations`, que
enumera eficientemente solo las permutaciones distintas.

## Ejercicios

````{exercise} •
:label: ex-es-gen-titans-turnos

Genere e imprima todas las maneras de asignar tres turnos de patrulla a los
cinco [Teen Titans](https://dc.fandom.com/wiki/Teen_Titans) (Robin, Starfire,
Raven, Beast Boy, Cyborg), pudiendo asignar más de un turno al mismo superhéroe.
Cuente e imprima también el número total de calendarios posibles.
````
````{solution} ex-es-gen-titans-turnos
:class: dropdown

Cada asignación corresponde a una variación con repetición de los cinco Teen
Titans en tres casillas: el mismo superhéroe puede cubrir más de un turno (de ahí
la necesidad de considerar repeticiones), y el orden de los turnos importa —
ser asignado al primer turno es diferente de ser asignado al segundo o al tercero
(de ahí el uso de variaciones).

```{code-cell} python
titans = ['Robin', 'Starfire', 'Raven', 'Beast Boy', 'Cyborg']
count = 0
for t in it.product(titans, repeat=3):
    print(t)
    count += 1
print(f'En total hay {count} maneras diferentes de asignar los turnos.')
```
````

````{exercise} •
:label: ex-es-gen-titans-cuenta

Si en el ejercicio anterior el único requisito hubiera sido contar el número de
calendarios diferentes sin imprimirlos, ¿habría maneras más eficientes de
responder a la pregunta?
````
````{solution} ex-es-gen-titans-cuenta
:class: dropdown

Como se consideran variaciones con repetición de cinco objetos en tres casillas,
sabemos que hay exactamente $D_{5, 3} = 5^3 = 125$. Este argumento permite
responder a la pregunta calculando una única exponenciación.
````

````{exercise} •
:label: ex-es-gen-watchmen-parejas

Genere e imprima todas las parejas posibles formadas a partir de los seis
miembros de los [Watchmen](https://dc.fandom.com/wiki/Watchmen) (Rorschach,
Búho Nocturno, Espectro de Seda, Ozymandias, Doctor Manhattan, Comediante).
````
````{solution} ex-es-gen-watchmen-parejas
:class: dropdown

```{code-cell} python
watchmen = ['Rorschach', 'Nite Owl', 'Silk Spectre',
            'Ozymandias', 'Dr Manhattan', 'Comedian']

for c in it.combinations(watchmen, 2):
    print(c)
```
````

````{exercise} •
:label: ex-es-gen-dk-mp-repeticion

Calcule cuántas de las combinaciones con repetición de Dupli-Kate y Multi-Paul
en cuatro casillas contienen al menos un clon de Kate.
````
````{solution} ex-es-gen-dk-mp-repeticion
:class: dropdown

```{code-cell} python
count = 0
for c in it.combinations_with_replacement(['k', 'p'], 4):
    if 'k' in c:
        count += 1
print(f'Exactamente {count} combinaciones contienen al menos un clon de Kate.')
```
````

````{exercise} •
:label: ex-es-gen-dk-mp-repeticion-comp

Reconsidere el ejercicio anterior resolviéndolo mediante una _comprensión de
lista_.
````
````{solution} ex-es-gen-dk-mp-repeticion-comp
:class: dropdown

```{code-cell} python
count = len([1 for c in it.combinations_with_replacement(['k', 'p'], 4)
               if 'k' in c])
print(f'Exactamente {count} combinaciones contienen al menos un clon de Kate.')
```
````

````{exercise} •
:label: ex-es-gen-iter-vs-lista

Cuente cuántas variaciones con repetición de los $21$ miembros regulares de la
[Legión de Super-Héroes](https://dc.fandom.com/wiki/Legion_of_Super-Heroes_(Earth-Prime))
en $3$ casillas cumplen la condición de que la primera y la tercera casilla estén
ocupadas por el mismo héroe, sin almacenar la lista completa en memoria.
````
````{solution} ex-es-gen-iter-vs-lista
:class: dropdown

```{code-cell} python
count = sum(1 for d in it.product(range(21), repeat=3) if d[0] == d[2])
print(f'En exactamente {count} casos el mismo héroe aparece en la primera '
      'y en la última posición.')
```

El resultado es $21^2 = 441$: la primera casilla tiene $21$ opciones, la segunda
también, mientras que la tercera está obligada a coincidir con la primera.
````

````{exercise} ••
:label: ex-es-gen-alpha-flight-sin-guardian

¿Cuántas variaciones simples de los cuatro miembros de Alpha Flight (véase
{prf:ref}`ex-es-variaciones-con-repeticion-1`) en tres casillas excluyen a
Guardian? Verifique la respuesta experimentalmente generando todas las variaciones
y contando las que lo excluyen.
````
````{solution} ex-es-gen-alpha-flight-sin-guardian
:class: dropdown

Excluir a Guardian equivale a no considerar uno de los objetos posibles y, por
tanto, a centrarse en las variaciones simples de tres objetos en tres casillas,
que son $d_{3, 3} = 6$, como confirma el código siguiente.

```{code-cell} python
alpha_flight = ['g', 's', 'n', 'a']
no_g = [d for d in it.permutations(alpha_flight, 3) if 'g' not in d]
print(f'El número de variaciones que no incluyen a Guardian es {len(no_g)}')
```
````

````{exercise} ••
:label: ex-es-gen-verificar-formula

Escriba una función `compute_combinatorics(n, k)` que, usando los iteradores de
`itertools`, cuente el número de variaciones con repetición, variaciones simples
y combinaciones simples de `n` objetos en `k` casillas. La función debe devolver
un diccionario cuyas claves sean las cadenas `'D'`, `'d'` y `'c'`, asociadas
respectivamente a las variaciones con repetición, las variaciones simples y las
combinaciones. Verifique que la función se comporta correctamente cuando los
argumentos `n` y `k` valen $5$ y $3$ respectivamente.
````
````{solution} ex-es-gen-verificar-formula
:class: dropdown

Aunque los valores requeridos podrían calcularse directamente, el problema pide
explícitamente el uso de iteradores. Es posible, por tanto, utilizar generadores
basados en estos, produciendo el valor constante $1$ para cada agrupación
considerada. Sumar los valores generados proporciona los recuentos requeridos.

El problema no especifica qué objetos considerar, solo cuántos. Como los índices
combinatorios no dependen de la naturaleza específica de los objetos, podemos
usar enteros de $0$ al valor de `n`, producidos eficientemente por `range`.

```{code-cell} python
def compute_combinatorics(n, k):
    objects = range(n)
    disp_repeat = sum(1 for _ in it.product(objects, repeat=k))
    disp_simple = sum(1 for _ in it.permutations(objects, k))
    comb = sum(1 for _ in it.combinations(objects, k))
    return {'D': disp_repeat, 'd': disp_simple, 'c': comb}
```

Aplicando las fórmulas correspondientes para los dos tipos de variaciones y para
las combinaciones, es fácil obtener $D_{5, 3} = 125$, $d_{5, 3} = 60$ y
$c_{5, 3} = 10$, que podemos verificar mediante simples aserciones.

```{code-cell} python
result = compute_combinatorics(5, 3)

assert result['D'] == 125
assert result['d'] == 60
assert result['c'] == 10
```
````

````{exercise} ••
:label: ex-es-gen-dk-clones-anagramas

Genere todas las permutaciones de los objetos del multiconjunto que contiene dos
clones de Dupli-Kate y tres clones de Multi-Paul, insertando todas las
permutaciones simples en un conjunto.
````
````{solution} ex-es-gen-dk-clones-anagramas
:class: dropdown

En la sección sobre permutaciones con repetición, las permutaciones se insertaban
en un conjunto _después_ de usarse, para evitar reconsiderarlas más adelante.
Aquí, en cambio, se pide usar el conjunto para agregar las permutaciones, quizás
para un uso futuro. El enfoque más directo consiste en enumerar las permutaciones
simples insertándolas todas en el conjunto: esta operación gestiona los duplicados
automáticamente, ya que insertar un elemento que ya está en un conjunto no tiene
ningún efecto.

```{code-cell} python
clones = ['k', 'k', 'p', 'p', 'p']
distinct = set()
for p in it.permutations(clones):
    distinct.add(p)
print(distinct)
```

De hecho, es posible reescribir este código de manera mucho más concisa. Los
constructores de casi todos los tipos de datos estructurados que hemos visto
aceptan iteradores como argumentos, que se recorren automáticamente insertando
progresivamente los elementos generados en la estructura. En nuestro caso, esto
permite reescribir la celda anterior como se muestra a continuación.

```{code-cell} python
clones = ['k', 'k', 'p', 'p', 'p']
distinct = set(it.permutations(clones))

print(distinct)
```
````

````{exercise} ••
:label: ex-es-gen-doom-patrol-islice

Lea la
[documentación](https://docs.python.org/3/library/itertools.html#itertools.islice)
de la clase `itertools.islice` y úsela para generar e imprimir solo diez
permutaciones simples de los cinco miembros del
[Doom Patrol](https://dc.fandom.com/wiki/Doom_Patrol) (Robotman, Negative Man,
Elasti-Girl, Crazy Jane, Flex Mentallo), sin generar ni recorrer las $5! - 10 =
110$ permutaciones restantes.
````
````{solution} ex-es-gen-doom-patrol-islice
:class: dropdown

La clase `islice` construye un iterador a partir de otro iterador, extrayendo
una subsecuencia. En su forma más sencilla, el constructor toma el iterador
fuente y un entero $n$: el iterador devuelto solo producirá los primeros $n$
elementos del original.

```{code-cell} python
doom_patrol = ['Robotman', 'Negative Man', 'Elasti-Girl',
               'Crazy Jane', 'Flex Mentallo']
for p in it.islice(it.permutations(doom_patrol), 10):
    print(p)
```
````

````{exercise} ••
:label: ex-es-gen-peter-poderes-incompatibles

Imprima todas las combinaciones de tres superpoderes, elegidos entre telepatía,
invisibilidad, psicocinesis, regeneración y precognición, excluyendo las que
contengan simultáneamente telepatía y psicocinesis. ¿Cuántas combinaciones de
este tipo hay?
````
````{solution} ex-es-gen-peter-poderes-incompatibles
:class: dropdown

```{code-cell} python
powers = ['telepathy', 'invisibility', 'psychokinesis',
          'regeneration', 'precognition']
valid = [c for c in it.combinations(powers, 3)
          if not ('telepathy' in c and 'psychokinesis' in c)]
print(f'Hay {len(valid)} combinaciones válidas.')
```

El número de combinaciones válidas puede obtenerse también razonando del
siguiente modo: partiendo de las $c_{5, 3} = 10$ combinaciones totales, se
restan todas aquellas en las que dos de las tres casillas están ocupadas por
telepatía y psicocinesis; como la casilla restante puede contener cualquiera de
los otros superpoderes, hay exactamente tres combinaciones a eliminar. Por tanto,
habrá siete combinaciones válidas.

````

````{exercise} •••
:label: ex-es-gen-young-avengers-equipos

Escriba un generador de Python que, dada una lista de héroes y un entero $k$,
produzca todos los pares de equipos disjuntos de $k$ héroes cada uno. Verifique
el comportamiento del generador usando los nueve
[Young Avengers](https://marvel.fandom.com/wiki/Young_Avengers) (Patriot,
Hulkling, Wiccan, Speed, Stature, Vision, Kate Bishop, Noh-Varr y Jonas) y
$k = 2$, teniendo en cuenta que el número de pares de equipos — en este caso —
debe ser igual a $c_{9,2} \cdot c_{7,2} = 36 \cdot 21 = 756$.
````
````{solution} ex-es-gen-young-avengers-equipos
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
