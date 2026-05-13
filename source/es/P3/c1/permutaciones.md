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

(sec_permutaciones-es)=
# Permutaciones

Una _permutación_ de $n$ objetos es, en esencia, una lista ordenada que contiene
cada uno de ellos exactamente una vez. En este contexto, las configuraciones
consideradas dependen estrictamente del orden de los elementos, y no se permite
reutilizar el mismo objeto. Dicho de otro modo, consiste en disponer $n$ objetos
en otras tantas casillas disponibles, lo que equivale a fijar un criterio de
orden y luego listarlos de «menor» a «mayor».

Para calcular el número de permutaciones posibles debemos distinguir dos
situaciones:

- en la primera, todos los objetos son diferentes;
- en la segunda, existen objetos diferentes que son, no obstante,
  indistinguibles entre sí.

Según el caso, hablamos de permutaciones _simples_ o de permutaciones _con
repetición_, que exploraremos a continuación.

## Permutaciones simples

Cuando los objetos a permutar son los elementos de un conjunto, son por
definición todos diferentes, es decir, distinguibles entre sí. En este caso
hablamos de _permutación simple_ (o simplemente _permutación_), tal como
describe la siguiente definición.

````{prf:definition} Permutación simple
:label: def-es-permutacion-simple

Dado un conjunto $A = \{ a_1,\dots a_n \}$ que contiene $n$ objetos, llamamos
_permutación simple_ (_permutación_) de estos objetos a toda sucesión ordenada

```{math}
(a_{i_1}, \dots, a_{i_n}), \quad
1 \leq i_j \leq n \ \forall j \in \{1, \dots, n \}, \quad
i_h \neq i_k \ \forall h \neq k
```

en la que aparecen todos y solo los $n$ elementos de $A$. Denotamos por $p_n$
el número de tales permutaciones simples.
````

En general, describiré una permutación listando sus elementos en el orden
correspondiente, separados por comas y encerrados entre paréntesis. Cabe
destacar que, a partir de una permutación simple, basta con intercambiar dos
elementos cualesquiera para obtener una nueva.

````{prf:example} Los Cuatro Fantásticos
:label: ex-es-fantastic-4
Consideremos el conjunto $Q = \{ f, i, t, c \}$ de los Cuatro Fantásticos:
Mister Fantástico ($f$), la Mujer Invisible ($i$), la Antorcha Humana ($t$) y
la Mole ($c$): las permutaciones simples posibles de sus elementos se listan en
la {numref}`permutaciones-cuatro-fantasticos-es`.
````

```{table} Permutaciones simples posibles de los miembros de los Cuatro Fantásticos
:name: permutaciones-cuatro-fantasticos-es
:align: center

|  Permutación   |  Permutación   |
| :------------: | :------------: |
| $(f, i, t, c)$ | $(t, f, i, c)$ |
| $(f, i, c, t)$ | $(t, f, c, i)$ |
| $(f, t, i, c)$ | $(t, i, f, c)$ |
| $(f, t, c, i)$ | $(t, i, c, f)$ |
| $(f, c, i, t)$ | $(t, c, f, i)$ |
| $(f, c, t, i)$ | $(t, c, i, f)$ |
| $(i, f, t, c)$ | $(c, f, i, t)$ |
| $(i, f, c, t)$ | $(c, f, t, i)$ |
| $(i, t, f, c)$ | $(c, i, f, t)$ |
| $(i, t, c, f)$ | $(c, i, t, f)$ |
| $(i, c, f, t)$ | $(c, t, f, i)$ |
| $(i, c, t, f)$ | $(c, t, i, f)$ |
```

El principio fundamental de la combinatoria nos permite calcular fácilmente el
número $p_n$ de permutaciones diferentes de $n$ objetos:

- el objeto a colocar en la primera posición de la lista puede seleccionarse de
  $n$ maneras distintas, ya que podemos elegir entre todos los objetos
  disponibles;
- la segunda posición puede ser ocupada por $n-1$ objetos distintos, pues el
  usado en el paso anterior no puede considerarse de nuevo, de modo que hay
  $n \cdot (n-1)$ maneras diferentes de elegir los dos primeros elementos de la
  sucesión;
- procediendo análogamente para cada posición siguiente, el número de opciones
  disminuye en uno en cada paso, creando un árbol en el que el nivel $i$ está
  asociado a la $i$-ésima posición; para rellenar esta posición quedan
  $n-(i-1)$ elementos de $A$ entre los que elegir, por lo que hay
  $n\cdot(n-1) \cdot \ldots \cdot(n-(i-1))$ maneras posibles de listar los
  primeros $i$ elementos de la sucesión;
- al llegar a la última posición, el único elemento restante de $A$ debe
  elegirse obligatoriamente.

Puede construirse así un árbol de profundidad $n$ que tiene un número de hojas
igual a $n(n-1)(n-2)\ldots 1=n!$, cada una de las cuales corresponde a una de
las permutaciones simples posibles. En resumen, el número de permutaciones de
$n$ objetos es $p_n = n!$. Mirando la {numref}`permutaciones-cuatro-fantasticos-es`,
por ejemplo, puede verificarse fácilmente que contiene las $4! = 24$
permutaciones posibles de los cuatro elementos del conjunto $Q$ introducido en
{prf:ref}`ex-es-fantastic-4`.


## Permutaciones con repetición

Consideremos ahora el caso en que algunos de los objetos a permutar son
indistinguibles, pero siguen siendo _distinguibles por grupos_. Más precisamente,

- hay $r \in \mathbb N$ versiones posibles para los objetos, que podemos
  denotar $a_1, \ldots, a_r$, y
- para cada $j = 1, \dots, r$, la versión $a_j$ se repite $n_j$ veces (lo que
  implica $\sum_{j=1}^r n_j = n$).

Para cada versión $a_j$ hay, por tanto, un grupo de objetos indistinguibles de
tamaño $n_j$. Estos objetos forman un _multiconjunto_ (una colección no ordenada
en la que cada elemento puede aparecer una o más veces) que contiene $n_1$
ocurrencias de la versión $a_1$, $n_2$ ocurrencias de $a_2$, y así
sucesivamente. En resumen, podemos escribir los elementos de este multiconjunto
uno tras otro, obteniendo la sucesión

```{math}
\underbrace{a_1, \ldots, a_1}_{n_1 \text{ veces}},
\underbrace{a_2, \ldots, a_2}_{n_2 \text{ veces}}, \ldots,
\underbrace{a_r, \ldots, a_r}_{n_r \text{ veces}} \enspace.
```

Cambiar el orden de los elementos no siempre produce una sucesión diferente: si
se intercambian dos objetos indistinguibles, la sucesión permanece igual. En
estas situaciones solo se consideran las permutaciones que producen sucesiones
genuinamente distinguibles, tal como describe la siguiente definición.

````{prf:definition} Permutación con repetición
:label: def-es-permutacion-repeticion

Dado un multiconjunto $A = \{ a_1,\dots a_n \}$ que contiene $n$ objetos
distinguibles por grupos de tamaños $n_1, \ldots, n_r$, una _permutación de
objetos distinguibles por grupos_ (o, más brevemente, _permutación con
repetición_) de estos objetos es toda sucesión ordenada de ellos que sea
distinguible de las demás, y denotamos por $P_{n; n_1, \ldots, n_r}$ el número
de tales configuraciones.
````

Denotaré las permutaciones con repetición usando la misma sintaxis que las
permutaciones simples, separando los elementos con comas y usando paréntesis
como delimitadores.

````{prf:example} Dupli-Kate y Multi-Paul
:label: es-dupli-kate-multi-paul
Consideremos los gemelos
[Kate](https://comicvine.gamespot.com/dupli-kate/4005-41136/) y
[Paul Cha](https://comicvine.gamespot.com/multi-paul/4005-48737/) que aparecen
en [Invincible](https://comicvine.gamespot.com/invincible/4050-150390/).
Ambos están dotados del poder de autorreplicarse a voluntad y son conocidos como
Dupli-Kate y Multi-Paul. En particular, cada versión de Dupli-Kate lleva un
entero progresivo en su traje, de modo que podemos denotar sus clones presentes
en un momento dado como $k_1$, $k_2$, etc. Imaginemos que lo mismo ocurre con
Multi-Paul, cuyas réplicas denotaremos por $p_1, p_2, \ldots$, y que frente a
nosotros hay dos versiones de Kate y tres de Paul, de modo que el quinteto
resultante se describe mediante el multiconjunto $A= \{ k_1, k_2, p_1, p_2, p_3
\}$.

Para calcular de cuántas maneras estas cinco versiones de Kate y Paul pueden
ponerse en fila sin tener en cuenta su número progresivo, hay que encontrar el
número de permutaciones con repetición de $n = 5$ objetos divididos en dos
grupos distintos: uno que comprende las $n_1 = 2$ copias de Kate y otro con
$n_2 = 3$ clones de Paul. En este contexto, $(k_1, k_2, p_1, p_2, p_3)$ y
$(k_2, k_1, p_1, p_2, p_3)$ denotan dos permutaciones simples diferentes, pero
corresponden a la misma permutación con repetición: en las dos primeras
posiciones aparece Kate y en las tres últimas aparece Paul. En cambio,
$(k_1, k_2, p_1, p_2, p_3)$ y $(k_1, p_1, k_2, p_2, p_3)$ denotan
permutaciones con repetición diferentes, porque en el primer caso la segunda
posición la ocupa Kate y la tercera Paul, mientras que en el segundo ocurre lo
contrario.
````

Antes de calcular el número total de permutaciones con repetición de $n$ objetos
distinguibles por grupos de tamaños $n_1, n_2,\dots n_r$, analicemos primero el
caso particular de {prf:ref}`es-dupli-kate-multi-paul`.
```{margin}
Fijar las posiciones de las copias de Kate determina en este caso también las de
las copias de Paul.
```
Centrémonos en una permutación con repetición posible, fijando las posiciones
de Kate y las de Paul. Por ejemplo, supongamos que las posiciones primera y
última se destinan a Kate y las restantes a Paul:

<p style="text-align: center">Kate Paul Paul Paul Kate</p>

Ahora bien, varias permutaciones simples de cinco objetos (las dos copias de
Kate y las tres de Paul) corresponden a esta permutación con repetición.
La {numref}`permutaciones-objetos-indistinguibles-es` lista todas las
permutaciones en las que Kate está en los extremos de la fila, es decir, en la
permutación con repetición que hemos fijado.

```{table} Permutaciones simples posibles de objetos en dos grupos distinguibles que contienen respectivamente dos duplicados $k_1$ y $k_2$ de Kate y tres duplicados $p_1$, $p_2$ y $p_3$ de Paul, de modo que Kate esté en la primera y última posición.
:name: permutaciones-objetos-indistinguibles-es
:align: center

|         Permutación        |
| :-------------------------: |
| $(k_1, p_1, p_2, p_3, k_2)$ |
| $(k_1, p_3, p_1, p_2, k_2)$ |
| $(k_1, p_2, p_3, p_1, k_2)$ |
| $(k_1, p_3, p_2, p_1, k_2)$ |
| $(k_1, p_2, p_1, p_3, k_2)$ |
| $(k_1, p_1, p_3, p_2, k_2)$ |
| $(k_2, p_1, p_2, p_3, k_1)$ |
| $(k_2, p_3, p_1, p_2, k_1)$ |
| $(k_2, p_2, p_3, p_1, k_1)$ |
| $(k_2, p_3, p_2, p_1, k_1)$ |
| $(k_2, p_2, p_1, p_3, k_1)$ |
| $(k_2, p_1, p_3, p_2, k_1)$ |
```

Las filas de la {numref}`permutaciones-objetos-indistinguibles-es` se obtuvieron
permutando las dos copias de Kate en la primera y última posición y las tres
copias de Paul en las posiciones restantes. Si consideramos a Kate, solo hay dos
posibilidades: $k_1$ y $k_2$ en primera y última posición respectivamente, o
viceversa, y estas dos posibilidades corresponden a las $2!$ permutaciones
simples de las dos versiones de Kate. En otras palabras, podríamos haber
considerado todas las permutaciones simples de estas dos versiones y, para cada
una, tomado el primer elemento y colocado en la primera columna de la tabla,
insertando luego el segundo elemento en la última columna. De este modo
habríamos obtenido dos _plantillas_ para las filas de la tabla —
respectivamente para las filas una a seis y siete a doce. En ambos casos, las
filas se completan con un argumento análogo que implica las $3!$ permutaciones
simples posibles de las versiones de Paul. Podemos, por tanto, aplicar el
principio fundamental de la combinatoria: como hay $2!$ maneras de rellenar las
posiciones extremas y $3!$ maneras de rellenar las posiciones centrales, la
única configuración considerada corresponde a $n_1! \cdot n_2! = 2! \cdot 3! =
12$ permutaciones simples de los cinco objetos disponibles.

Este argumento no depende de la permutación con repetición particular analizada:
a cada una de las $P_{5; 2,3}$ permutaciones con repetición corresponden
$2! \cdot 3! = 12$ permutaciones simples, y si las consideramos todas es fácil
ver que conjuntamente identifican la totalidad de las permutaciones simples.
Por tanto debe verificarse la igualdad $P_{5; 2,3} \cdot 2! \cdot 3! = 5!$, lo
que permite derivar

```{math}
P_{5; 2,3} = \frac{5!}{2! \cdot 3!} = 10 \enspace.
```

Nótese que $P_{5; 2,3} = \binom{5}{2}$, y efectivamente el número de
permutaciones con repetición coincide con el número de maneras en que pueden
seleccionarse las dos posiciones para Kate entre las cinco disponibles.

En el caso general, tenemos $n$ objetos divididos en $r$ grupos de tamaños
$n_1, \ldots, n_r$ y, repitiendo el argumento anterior, obtenemos
$n! = P_{n; n_1,\dots, n_r} \cdot n_1! \cdot n_2! \cdot \ldots \cdot n_r!$,
lo que implica

```{math}
:label: eq-es-permutaciones-repeticion

P_{n; n_1, \dots, n_r} = \frac{n!}{n_1!\cdot n_2! \cdot \ldots \cdot n_r!}
\enspace.
```

La cantidad $P_{n; n_1, \dots, n_r}$ también se llama _coeficiente multinomial_
y se denota

```{math}
P_{n; n_1, \dots, n_r} = \frac{n!}{n_1!\cdot n_2! \cdot \ldots \cdot n_r!}
                       \triangleq \binom{n}{n_1, n_2, \ldots, n_r} \enspace,
```

porque representa una generalización del coeficiente binomial: en efecto,
$\binom{n}{k} = \binom{n}{k, n-k}$ indica de cuántas maneras es posible dividir
$n$ objetos en dos grupos que contienen $k$ y $n-k$ elementos respectivamente;
análogamente, $\binom{n}{n_1, \ldots, n_r}$ indica de cuántas maneras es posible
dividir $n$ objetos en $r$ grupos en los que el primero contiene $n_1$ elementos,
el segundo $n_2$, y así sucesivamente.

## Ejercicios

````{exercise} ••
:label: ex-es-perm-xmen-original

Los [X-Men](https://marvel.fandom.com/wiki/X-Men) en su alineación original son
cinco: Cíclope, Marvel Girl, la Bestia, el Ángel y el Hombre de Hielo. ¿De
cuántas maneras pueden ponerse en fila de modo que Cíclope esté siempre al
frente (como líder del equipo)?
````
````{solution} ex-es-perm-xmen-original
:class: dropdown

Si Cíclope debe ocupar la primera posición, los cuatro héroes restantes pueden
ocupar las otras cuatro posiciones de $p_4 = 4! = 24$ maneras.
````

````{exercise} ••
:label: ex-es-perm-thunderbolts

Los [Thunderbolts](https://marvel.fandom.com/wiki/Thunderbolts) originales
estaban formados por Citizen V, un villano que operaba bajo una identidad falsa
y que había convencido a otros cinco criminales de cambiar de identidad y
hacerse pasar por héroes. Jolt se unió más tarde al grupo sin conocer el engaño.
¿De cuántas maneras pueden alinearse todos los miembros del grupo de modo que
los cinco ex-villanos originales ocupen las primeras posiciones?
````
````{solution} ex-es-perm-thunderbolts
:class: dropdown

Los cinco ex-villanos pueden ocupar las primeras posiciones de $p_5 = 5! = 120$
maneras y —para cada uno de estos órdenes— los dos miembros restantes pueden
ocupar las últimas posiciones de $p_2 = 2! = 2$ maneras. Por el principio
fundamental, el número de configuraciones posibles es $120 \cdot 2 = 240$.
````

````{exercise} ••
:label: ex-es-perm-sinister-six

¿De cuántas maneras pueden los [Sinister Six](https://marvel.fandom.com/wiki/Sinister_Six)
(Doctor Octopus, el Buitre, Electro, Misterio, Kraven el Cazador y el Hombre de
Arena) ocupar seis sillas, de modo que Doctor Octopus y Electro nunca estén
sentados uno al lado del otro?
````
````{solution} ex-es-perm-sinister-six
:class: dropdown

Cada asignación de personajes a sillas corresponde a una permutación particular
de los Sinister Six, pero no todas las permutaciones deben considerarse. Para
resolver este problema, conviene razonar por complementariedad, restando de las
$p_6 = 6! = 720$ permutaciones todas aquellas en las que Doctor Octopus y
Electro son adyacentes. El recuento de estas últimas se realiza tratando a los
dos villanos como un único bloque, lo que da cinco objetos (cuatro personajes
más el par) a permutar de $p_5 = 5! = 120$ maneras; sin embargo, debe tenerse
en cuenta que intercambiar los dos elementos del par produce dos permutaciones
diferentes entre las originales, por lo que hay $240$ maneras de colocar a
Doctor Octopus y Electro juntos. En conclusión, hay $720 - 240 = 480$
disposiciones aceptables.
````

````{exercise} ••
:label: ex-es-perm-substitute-legion

La [Legión de Héroes Sustitutos](https://dc.fandom.com/wiki/Legion_of_Substitute_Heroes_(Earth-Prime))
comprende a Polar Boy, Night Girl, Fire Lad, Stone Boy y Chlorophyll Kid. Su
clasificación semanal de poderes se elabora así: Night Girl y Polar Boy siempre
están en las dos primeras posiciones (en cualquier orden), mientras que Stone
Boy siempre es el último. ¿De cuántas maneras distintas puede elaborarse la
clasificación?
````
````{solution} ex-es-perm-substitute-legion
:class: dropdown

Stone Boy debe aparecer siempre en último lugar, por lo que el número de
clasificaciones se obtiene aplicando el principio fundamental de la
combinatoria, multiplicando:

- las $p_2 = 2! = 2$ maneras en que Night Girl y Polar Boy pueden ocupar las
  dos primeras posiciones, y
- las $p_2 = 2$ maneras posibles de distribuir a Fire Lad y Chlorophyll Kid en
  las posiciones centrales restantes.

Es posible, por tanto, elaborar la clasificación de cuatro maneras distintas.
````

````{exercise} ••
:label: ex-es-perm-identidad-publica-secreta

Iron Man, Capitán América y la Mujer Invisible tienen identidades públicamente
conocidas; en cambio, Daredevil, Spider-Man y Ant-Man operan en el anonimato.
Si consideramos indistinguibles entre sí a los superhéroes con identidad pública,
y de igual modo a los de identidad secreta, ¿de cuántas maneras distintas es
posible ordenarlos?
````
````{solution} ex-es-perm-identidad-publica-secreta
:class: dropdown

En este caso debemos considerar las permutaciones de seis objetos organizados en
dos grupos de tres héroes indistinguibles cada uno. Aplicando la fórmula
{eq}`eq-es-permutaciones-repeticion`, obtenemos

```{math}
P_{6;\,3,3} = \frac{6!}{3!\cdot 3!} = \binom{6}{3} = 20 \enspace.
```
````

````{exercise} ••
:label: ex-es-perm-anagramas-superman

¿De cuántas maneras pueden formarse los anagramas de la palabra SUPERMAN,
entendiendo por anagrama cualquier reordenación de las letras de la palabra
original, aunque el resultado no tenga significado?
````
````{solution} ex-es-perm-anagramas-superman
:class: dropdown

SUPERMAN es una palabra que contiene ocho letras, todas diferentes entre sí. El
número de anagramas coincide, por tanto, con el número de permutaciones simples
de $8$ objetos, que es igual a $p_8 = 8! = 40\,320$.
````

````{exercise} ••
:label: ex-es-perm-anagramas-antman

¿De cuántas maneras pueden formarse los anagramas de la palabra ANTMAN, en el
mismo sentido que el ejercicio anterior?
````
````{solution} ex-es-perm-anagramas-antman
:class: dropdown

La palabra ANTMAN contiene seis letras, de las cuales dos aparecen cada una en
dos posiciones diferentes. El número de anagramas distintos es, por tanto, una
permutación con repetición: más precisamente, T y M pertenecen cada una a un
grupo de multiplicidad $1$, mientras que A y N remiten a dos grupos de
multiplicidad $2$. Por tanto, el número de anagramas distintos es

```{math}
P_{6;\,2,2,1,1} = \frac{6!}{2!\cdot 2!\cdot 1!\cdot 1!} = \frac{720}{4} = 180
\enspace.
```
````

````{exercise} •••
:label: ex-es-perm-justice-society

En su alineación original, la [Justice Society of
America](https://dc.fandom.com/wiki/Justice_Society_of_America_(New_Earth))
cuenta con ocho héroes: tres con poderes mágicos o alienígenas (Green Lantern,
Spectre y Doctor Fate), tres que utilizan tecnologías secretas (Atom, Hourman y
Flash) y dos que utilizan tecnologías bien conocidas y fácilmente reconocibles
(Sandman y Hawkman). ¿De cuántas maneras pueden intervenir uno tras otro en la
batalla, manteniendo siempre consecutivos a los héroes de la misma categoría?
````
````{solution} ex-es-perm-justice-society
:class: dropdown

Imaginemos que todos los héroes con poderes mágicos intervienen primero, luego
los que usan tecnologías secretas y finalmente los demás. Como los dos primeros
grupos pueden permutarse de $p_3 = 3!$ maneras y el tercero puede ordenarse de
$p_2 = 2!$ configuraciones, por el principio fundamental de la combinatoria hay
$6 \cdot 6 \cdot 2 = 72$ maneras de intervenir en este orden de grupos. Si
cambiamos el orden de los grupos, el resultado es el mismo. Por tanto, el
resultado final se obtiene multiplicando $72$ por el número de permutaciones de
los grupos, que es $p_3 = 3!$. En conclusión, habrá $432$ maneras diferentes de
desplegar a los miembros de la Justice Society, uno tras otro.
````
