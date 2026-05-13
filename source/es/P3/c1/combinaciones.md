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

(sec_combinaciones-es)=
# Combinaciones

De manera análoga a las variaciones, las combinaciones también describen tuplas
de longitud fija en las que aparecen objetos elegidos de un conjunto. En este
caso, sin embargo, las tuplas son _no ordenadas_: no son sucesiones sino
_subconjuntos_ del conjunto de partida. Por tanto, en los agrupamientos que
corresponden a combinaciones el orden no es relevante, pero sigue siendo posible
decidir si los objetos pueden repetirse o no. Las dos categorías resultantes de
combinaciones se describen en las secciones siguientes.

## Combinaciones simples

```{margin}
También puede hablarse de construir _conjuntos_ a partir de un _universo_ que
contiene los objetos considerados.
```
Cuando un objeto puede considerarse como máximo una vez, podemos decir
efectivamente que existe una correspondencia entre las combinaciones —llamadas
_simples_— y los subconjuntos del conjunto de partida.

````{prf:definition}
:label: def-es-combinaciones
Dado un conjunto $A = \{ a_1, \ldots, a_n \}$ de $n$ objetos y fijado un
número natural $k \leq n$, una _combinación simple_ (o más brevemente una
_combinación_) de los $n$ objetos en $k$ casillas es una tupla no ordenada
$\{ a_{i_1}, \dots, a_{i_k} \}$ tal que para todo $j = 1, \dots, k$ se tiene
$a_{i_j} \in A$, y $a_{i_j} \neq a_{i_l}$ para todo $j, l = 1, \dots, k$ con
$j \neq l$. Denotamos el número de combinaciones simples posibles de $n$ objetos
en $k$ casillas por $c_{n, k}$.
````

Denotaré las combinaciones usando llaves como delimitadores de las tuplas, para
subrayar que el orden no es relevante; además, esta notación es coherente con el
hecho de que una combinación simple identifica un subconjunto
$\{ a_{i_1}, \dots, a_{i_k} \}\subseteq A$, de modo que las descripciones del
subconjunto —dadas en forma extensional— y de la combinación coinciden.

````{prf:example} Peter Petrelli
:label: ex-es-peter-petrelli
[Peter Petrelli](https://comicvine.gamespot.com/peter-petrelli/4005-47678/) es
uno de los protagonistas de
[Heroes](https://comicvine.gamespot.com/heroes/4050-19509/), dotado de una forma
extraordinaria de _empatía_ que le permite reproducir los poderes de otros
superhéroes en su proximidad. Supongamos que este meta-poder es limitado y que
Peter solo puede replicar tres superpoderes a la vez:
$\{ \text{telequinesis}, \text{telepatía}, \text{invisibilidad} \}$ y
$\{ \text{telepatía}, \text{invisibilidad}, \text{telequinesis} \}$ denotan la
misma tripla no ordenada y, por tanto, el mismo subconjunto y la misma
combinación simple de $k = 3$ superpoderes. En este caso, el conjunto del que
extraemos los objetos es el conjunto de todos los superpoderes, y es poco
relevante determinar su cardinalidad $n$.
````

Para calcular el número $c_{n, k}$ de combinaciones simples posibles de $n$
objetos en $k$ casillas, podemos aprovechar el vínculo entre estas y las
variaciones simples:
- cada combinación simple corresponde a múltiples variaciones: permutando de
  todas las maneras posibles los $k$ objetos que la componen se obtienen $k!$
  variaciones distintas;
- en consecuencia, cada combinación aparece exactamente $k!$ veces en el
  conjunto de las $d_{n, k}$ variaciones simples de $n$ objetos en $k$ casillas,
  de donde $d_{n, k} = c_{n, k} \cdot k!$;
- invirtiendo esta relación se obtiene $c_{n, k} = \frac{d_{n, k}}{k!}$.

Aplicando la fórmula para calcular $d_{n, k}$, obtenemos finalmente

```{math}
c_{n, k} = \frac{d_{n, k}}{k!} = \frac{n!}{(n-k)!k!} =\binom{n}{k} \enspace.
```

````{prf:example} Peter Petrelli
:label: ex-es-peter-petrelli-2

Imaginemos que hay $n = 477$ superpoderes
posibles[^superpoderes], y que Peter Petrelli (véase
{prf:ref}`ex-es-peter-petrelli`) puede reproducirlos todos. Esto significa que,
en cualquier momento dado, será capaz de «recordar»
$c_{477, 3} = \binom{477}{3} = \;$
<span style="word-spacing: -0.1rem">17 974 950</span>
configuraciones diferentes de tres superpoderes.
````

## Combinaciones con repetición

Cuando es posible insertar el mismo objeto más de una vez en una combinación,
decimos que es una _combinación con repetición_. En este caso, la construcción
de una combinación es análoga a la de un _multiconjunto_, una generalización del
concepto de conjunto en cuya descripción extensional los objetos pueden aparecer
más de una vez, de modo que cada elemento del multiconjunto tiene también una
_multiplicidad_, entendida como el número de veces que aparece.

````{prf:definition} Combinación con repetición
:label: def-es-combinacion-con-repeticion

Dado un conjunto $A = \{ a_1, \ldots, a_n \}$ de $n$ objetos y fijado un número
$k \in \mathbb N$, una _combinación con repetición_ de los $n$ objetos en $k$
casillas es una tupla no ordenada $\{ a_{i_1}, \dots, a_{i_k} \}$ tal que para
todo $j = 1, \dots, k$ se tiene $a_{i_j} \in A$. Denotamos el número de todas
las combinaciones con repetición posibles de $n$ objetos en $k$ casillas por
$C_{n, k}$.
````

Describiré las combinaciones con repetición usando la misma notación que las
simples, con la diferencia de que en este caso la tupla entre llaves puede
contener duplicados.

````{prf:example}
:label: ex-es-combinaciones-con-repeticion

Imaginemos un ascensor con capacidad para cuatro personas, lleno de clones de
Dupli-Kate y Multi-Paul (véase {prf:ref}`es-dupli-kate-multi-paul`), sin que
ambos gemelos tengan que estar necesariamente presentes. La
{numref}`tab-es-combinaciones-DK-MP` lista todas las maneras en que cuatro
clones pueden entrar en el ascensor, donde cada configuración corresponde a una
combinación con repetición de los dos objetos $k$ y $p$ (Kate y Paul) en cuatro
casillas.
````

```{table} Combinaciones con repetición posibles de Dupli-Kate y Multi-Paul en cuatro casillas
:name: tab-es-combinaciones-DK-MP
:align: center

|    Combinación     |
| :----------------: |
| $\{ k, k, k, k \}$ |
| $\{ k, k, k, p \}$ |
| $\{ k, k, p, p \}$ |
| $\{ k, p, p, p \}$ |
| $\{ p, p, p, p \}$ |
```


Una posible manera de calcular el número $C_{n, k}$ de combinaciones con
repetición de $n$ objetos de un conjunto $A$ en $k$ casillas consiste en
asociarlas unívocamente con subconjuntos apropiados de $\mathbb N$. Dada una
función biyectiva $r: A \rightarrow \{ 1, \ldots, n \}$, cada combinación con
repetición posible $\{ a_{i_1}, \ldots, a_{i_k} \}$ puede transformarse en el
conjunto numérico $\{r(a_{i_1}), \ldots, r(a_{i_k}) \}$, reemplazando cada
elemento por su representación numérica a través de $r$. Si denotamos por
$\sigma^r$ la sucesión obtenida ordenando este conjunto de forma no decreciente,
se sigue que:

- $\sigma^r$ no depende del orden particular en que se listan los elementos de
  la combinación de partida;
- los $k$ elementos de $\sigma^r$ son enteros entre $1$ y $n$, extremos
  incluidos, y esta sucesión puede contener valores adyacentes iguales.

Finalmente, denotemos por $\sigma^r_i$ el $i$-ésimo elemento de $\sigma^r$ y
construyamos una última sucesión

```{math}
\rho = \{ \sigma^r_1 + 0, \sigma^r_2 + 1, \ldots, \sigma^r_k + k - 1 \}.
```

$\rho$ también contendrá $k$ elementos, pero estarán automáticamente ordenados
de forma estrictamente creciente, porque se obtuvieron incrementando los
elementos de $\sigma^r$ —que es no decreciente— en una cantidad cada vez mayor.
Además, $\rho$ contendrá valores enteros entre $1$ y $n + k - 1$, por lo que
puede ponerse en correspondencia biyectiva con un subconjunto de
$M = \{ 1, \ldots, n + k - 1 \}$ que contenga $k$ elementos. En resumen, cada
combinación con repetición de $n$ objetos en $k$ casillas puede relacionarse con
un subconjunto de $M$ de cardinalidad $k$.

Recíprocamente, un subconjunto genérico de $M$ de cardinalidad $k$ puede
describirse listando sus elementos en orden creciente, obteniendo una sucesión
$\rho$. Si ahora decrementamos los elementos de esta sucesión restando cero al
primer elemento, uno al segundo, dos al tercero, y así sucesivamente, obtenemos
una nueva sucesión $\sigma^r$ ordenada de forma no decreciente, cuyos valores
(que pueden repetirse) se encuentran entre $1$ y $n$ (extremos incluidos).
Considerar entonces las preimágenes de estos valores a través de $r$ proporciona
una combinación con repetición de $k$ objetos de $A$. Así, todo subconjunto de
$M$ de $k$ elementos puede relacionarse con una combinación con repetición de
$n$ objetos en $k$ casillas.

````{prf:example}
:label: es-combinaciones-DK-MP-2
Volviendo a {prf:ref}`ex-es-combinaciones-con-repeticion`, el conjunto de
objetos de partida $A = \{ k, p \}$, donde $k$ y $p$ denotan a Kate y Paul
respectivamente, puede ponerse en correspondencia biyectiva con
$N = \{ 1, 2 \}$, por ejemplo estableciendo $r(k) = 2$ y $r(p) = 1$. La
{numref}`tab-es-combinaciones-DK-MP-2` muestra la correspondencia entre todas
las combinaciones con repetición de los dos objetos de $A$ en cuatro posiciones
y las sucesiones $\sigma^r$ y $\rho$.
````

```{table} Correspondencia entre las combinaciones con repetición de Dupli-Kate y Multi-Paul en cuatro casillas.
:name: tab-es-combinaciones-DK-MP-2
:align: center

|    Combinación     |     $\sigma^r$     |     $\rho$     |
| :----------------: | :----------------: | :----------------: |
| $\{ k, k, k, k \}$ | $\{ 2, 2, 2, 2 \}$ | $\{ 2, 3, 4, 5 \}$ |
| $\{ k, k, k, p \}$ | $\{ 1, 2, 2, 2 \}$ | $\{ 1, 3, 4, 5 \}$ |
| $\{ k, k, p, p \}$ | $\{ 1, 1, 2, 2 \}$ | $\{ 1, 2, 4, 5 \}$ |
| $\{ k, p, p, p \}$ | $\{ 1, 1, 1, 2 \}$ | $\{ 1, 2, 3, 5 \}$ |
| $\{ p, p, p, p \}$ | $\{ 1, 1, 1, 1 \}$ | $\{ 1, 2, 3, 4 \}$ |
```

Por tanto, las combinaciones con repetición de $n$ objetos en $k$ casillas están
en correspondencia biyectiva con los subconjuntos de $M$ de cardinalidad $k$, y
como el número de estos subconjuntos es igual al número de combinaciones simples
de $n + k - 1$ objetos en $k$ casillas, podemos concluir que

```{math}
C_{n, k} = c_{n + k - 1, k} = \binom{n+k-1}{k} \enspace.
```


[^superpoderes]: Tal como se listan, por ejemplo, en
[superherodb](https://www.superherodb.com/powers/).


## Ejercicios

````{exercise} ••
:label: ex-es-conjunto-partes

Dado el conjunto $A = \{ a_1,\dots a_n \}$ y denotando por $\mathcal{P}(A)$ el
conjunto de partes de $A$, calcule la cardinalidad de $\mathcal{P}(A)$.
````
````{solution} ex-es-conjunto-partes
:class: dropdown

Recuérdese que el conjunto de partes $\mathcal{P}(A)$ es el conjunto de todos
los subconjuntos propios e impropios de $A$: contiene el conjunto vacío, todos
los subconjuntos formados por un único elemento de $A$, todos los subconjuntos
formados por exactamente dos elementos de $A$, y así sucesivamente, y contiene
también el propio $A$.

Como el número de subconjuntos formados por $k$ elementos es
$c_{n,k}=\binom{n}{k}$, la cardinalidad de $\mathcal{P}(A)$ es
$|\mathcal{P}(A)| = 1 + \sum_{k=1}^{n} \binom{n}{k}$, donde el primer sumando
corresponde al conjunto vacío. Usando las propiedades del coeficiente binomial,
obtenemos

```{math}
|\mathcal{P}(A)| = \sum_{k=0}^{n} \binom{n}{k}
                 = \sum_{k=0}^{n}\binom{n}{k} 1^k 1^{n-k} = 2^n,
```

donde en el último paso hemos usado la fórmula del binomio de Newton:
$(a+b)^n = \sum_{k=0}^{n}\binom{n}{k}a^k b^{n-k}$, poniendo $a=1$ y $b=1$.

Este ejercicio puede resolverse también como sigue: si representamos cada
subconjunto $S$ de $A$ como una $n$-tupla de elementos binarios, donde la
posición $i$ contiene el símbolo $1$ si el elemento $a_i$ pertenece a $S$ y $0$
si no pertenece, entonces el conjunto de partes $\mathcal{P}(A)$ es el conjunto
de todas las $n$-tuplas que pueden construirse con los dos símbolos $0$ y $1$.
Por tanto,

```{math}
|\mathcal{P}(A)| = D_{n,2}=2^n.
```

````

````{exercise} ••
:label: ex-es-comb-justice-league-equipo

La [Justice League](https://dc.fandom.com/wiki/Justice_League_(Prime_Earth))
debe seleccionar un equipo de respuesta rápida de cuatro miembros, eligiendo
entre diez candidatos. ¿De cuántas maneras distintas puede formarse el equipo?
````
````{solution} ex-es-comb-justice-league-equipo
:class: dropdown

Se trata de elegir cuatro héroes entre diez, sin orden y sin repetición. Puede
hacerse de $c_{10,4} = \binom{10}{4} = 210$ maneras.
````

````{exercise} ••
:label: ex-es-comb-xmen-profesor-x

Los [X-Men](https://marvel.fandom.com/wiki/X-Men) deben formar un equipo de
cinco miembros entre doce disponibles. El Profesor X debe incluirse
necesariamente. ¿Cuántos equipos diferentes son posibles?
````
````{solution} ex-es-comb-xmen-profesor-x
:class: dropdown

Como el Profesor X debe estar incluido, deben elegirse cuatro miembros entre los
once restantes. El número de equipos es, por tanto,
$c_{11,4} = \binom{11}{4} = 330$.
````

````{exercise} •••
:label: ex-es-comb-defenders-no-juntos

Los [Defenders](https://marvel.fandom.com/wiki/Defenders_(Earth-616)) tienen
nueve candidatos para una misión que requiere cuatro miembros. ¿De cuántas
maneras puede formarse el equipo si Daredevil y Jessica Jones no pueden aparecer
juntos?
````
````{solution} ex-es-comb-defenders-no-juntos
:class: dropdown

Sin restricciones, los equipos posibles serían $c_{9, 4} = \binom{9}{4} = 126$.
Por otro lado, los equipos que contienen a Daredevil y Jessica Jones se cuentan
así: con la pareja fijada, deben elegirse dos miembros más entre los siete
restantes, lo que puede hacerse de $c_{7,2} = \binom{7}{2} = 21$ maneras. Los
equipos válidos son, por tanto, $126 - 21 = 105$.
````

````{exercise} ••
:label: ex-es-comb-guardianes-recursos

Los [Guardianes de la
Galaxia](https://marvel.fandom.com/wiki/Guardians_of_the_Galaxy_(Earth-616))
están equipando la
[Milano](https://marvel.fandom.com/wiki/Milano) (su nave espacial) para una
misión. A bordo hay cinco bahías disponibles, cada una de las cuales puede
alojar uno de cuatro tipos de dispositivo: cañones láser, escudos de energía,
sensores de detección y módulos de soporte vital. Calcule el número de maneras
diferentes de configurar la Milano, dado que cada tipo de dispositivo puede
instalarse varias veces y solo importa el recuento de cada tipo (no en qué bahía
específica están instalados).
````
````{solution} ex-es-comb-guardianes-recursos
:class: dropdown

Cada configuración corresponde a una y solo una combinación con repetición de
cuatro objetos (los tipos de dispositivo) en cinco casillas (las bahías), para
un total de $C_{4,5} = \binom{4+5-1}{5} = \binom{8}{5} = 56$ configuraciones
posibles.
````

````{exercise} •
:label: ex-es-comb-avengers-gemas

Los [Vengadores](https://marvel.fandom.com/wiki/Avengers_(Earth-616)) desean
seleccionar cuatro [Gemas del
Infinito](https://marvel.fandom.com/wiki/Infinity_Stones) de las seis
disponibles para estudiar su comportamiento. Sin embargo, las Gemas del Tiempo
y de la Realidad deben estudiarse juntas, porque modificar la secuencia de
eventos sin actualizar el estado de la realidad puede generar inconsistencias
lógicas y paradojas. Por tanto, estas dos gemas deben seleccionarse ambas o
excluirse ambas del grupo. Calcule el número de configuraciones de gemas
diferentes que pueden considerarse.
````
````{solution} ex-es-comb-avengers-gemas
:class: dropdown

Como las Gemas del Tiempo y de la Realidad deben considerarse juntas o
excluirse completamente, podemos considerar los dos casos por separado, calcular
el número de elecciones posibles para cada uno y luego sumar.

- Hay $c_{4, 2} = \binom{4}{2} = 6$ configuraciones que contienen las dos
  gemas, porque una vez fijadas las Gemas del Tiempo y de la Realidad, deben
  seleccionarse dos más de las cuatro gemas restantes.
- Intuitivamente, si esas dos gemas se excluyen, quedan exactamente cuatro y
  todas deben seleccionarse. En efecto, en este caso las combinaciones de estas
  cuatro gemas en cuatro casillas son $c_{4, 4} = 1$.

En conclusión, hay siete maneras posibles de seleccionar las gemas para
estudiar.
````

````{exercise} •••
:label: ex-es-comb-batman-gadgets-restriccion

Batman debe preparar su cinturón utilitario eligiendo cuatro gadgets de una
lista de ocho, pero dos gadgets (la granada de destello y las gafas de visión
nocturna) son incompatibles y no pueden incluirse juntos. ¿De cuántas maneras
puede elegir su equipo?
````
````{solution} ex-es-comb-batman-gadgets-restriccion
:class: dropdown

Sin la restricción de incompatibilidad, los equipamientos posibles se
describirían mediante las combinaciones de ocho gadgets en grupos de cuatro,
para un total de $c_{8, 4} = \binom{8}{4} = 70$ casos. De estos debemos restar
las configuraciones no permitidas. En tales configuraciones dos de las cuatro
casillas ya están ocupadas por la granada de destello y las gafas de visión
nocturna, por lo que su recuento es igual al número de combinaciones de los seis
gadgets restantes en grupos de dos, es decir, $c_{6, 2} = \binom{6}{2} = 15$.
El total válido es, por tanto, $70 - 15 = 55$.
````
