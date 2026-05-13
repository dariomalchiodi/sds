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

(sec_variaciones-es)=
# Variaciones

Una variación de $n$ objetos distintos en $k$ casillas es cualquier sucesión de
$k$ símbolos, cada uno de los cuales representa uno de los objetos. Por tanto,
el tipo de agrupación que corresponde a las variaciones depende del orden
utilizado, y los objetos deben ser mutuamente distinguibles. Hablamos de
variaciones _con repetición_ cuando un símbolo puede aparecer más de una vez en
la sucesión, y de _variaciones simples_ en caso contrario.

## Variaciones con repetición

En las variaciones con repetición, el mismo objeto puede usarse más de una vez,
tal como especifica la siguiente definición.

```{margin}
En este caso el significado de _repetición_ difiere del visto para las
permutaciones, en las que era necesario insertar cada objeto exactamente tantas
veces como aparece en el multiconjunto de partida; en las variaciones, en
cambio, podemos repetir el mismo objeto tantas veces como queramos u omitirlo
completamente.
```
```{prf:definition} Variación con repetición
:label: def-es-variaciones-con-repeticion
Dado un conjunto de $n$ objetos $A = \{ a_1,\dots a_n \}$ y un número
$k \in \mathbb N$, una _variación con repetición_ es una sucesión
$(a_{i_1}, \dots, a_{i_k})$, donde para todo $j = 1, \dots, k$ se tiene
$i_j \in \{1, \dots, n\}$ y $a_{i_j} \in A$. Denotamos por $D_{n, k}$ el
número de variaciones con repetición posibles de $n$ objetos en $k$ casillas.
```


```{prf:example} Un ejemplo de variación con repetición
:label: ex-es-variaciones-con-repeticion-1

El [Departamento H](https://marvel.fandom.com/wiki/Department_H_(Earth-616))
debe planificar una secuencia de tres misiones diarias — mañana, tarde y noche.
Para cada misión, puede enviarse cualquiera de los cuatro miembros de
[Alpha Flight](https://marvel.fandom.com/wiki/Alpha_Flight_(Earth-616)):
Guardian, Sasquatch, Northstar y Aurora, denotados por sus iniciales $G$, $S$,
$N$ y $A$ respectivamente. Si cada miembro puede ser desplegado en más de una
misión durante el mismo día, cada programación corresponde a una variación con
repetición de los $n = 4$ objetos del conjunto $\{G, S, N, A\}$ (los miembros
del equipo) en $k = 3$ casillas (los turnos diarios). Por ejemplo, las tres
situaciones siguientes describen programaciones diferentes (y variaciones
diferentes):
- $(G, S, N)$ indica que Guardian, Sasquatch y Northstar llevan a cabo los
  turnos de mañana, tarde y noche respectivamente;
- $(S, N, G)$ intercambia los turnos de mañana y tarde respecto al punto
  anterior;
- $(A, G, G)$ implica a Aurora por la mañana y a Guardian en los dos turnos
  siguientes.
```

Calcular el número $D_{n, k}$ de variaciones con repetición posibles es bastante
sencillo considerando el número de elecciones posibles para cada una de las $k$
casillas:
- el objeto a colocar en la primera casilla puede elegirse de $n$ maneras
  diferentes;
- el número de elecciones sigue siendo $n$ para la segunda casilla también, ya
  que es posible reutilizar el objeto seleccionado para la primera posición;
- claramente, habrá $n$ elecciones posibles para todas las casillas restantes.

Aplicando el principio fundamental de la combinatoria, obtenemos

$$
D_{n, k} = \underbrace{n \cdot n \dots \cdot n}_{k \text{ veces}} = n^k \enspace.
$$

El mismo resultado se obtiene notando que el conjunto de todas las variaciones es
el producto cartesiano $A^k$ de $A$ consigo mismo, calculado $k$ veces, y
recordando que $|A^k| = |A|^k = n^k$.

```{prf:example} Un ejemplo de variación con repetición
:label: ex-es-variaciones-con-repeticion-2

Volviendo a {prf:ref}`ex-es-variaciones-con-repeticion-1`, el número total de
programaciones diarias distintas es igual a $D_{4,3} = 4^3 = 64$, tal como se
muestra en la {numref}`tab-es-variaciones-con-repeticion`, donde las columnas M,
T y N se refieren a los turnos de mañana, tarde y noche respectivamente.
```

````{table} Las variaciones con repetición posibles de $4$ objetos en $3$ casillas, describiendo los turnos de Alpha Flight; las variaciones simples correspondientes se destacan en negrita.
:name: tab-es-variaciones-con-repeticion
:align: center

|  # | M   | T   | N   |  # | M   | T   | N   |  # | M   | T   | N   |
|----|-----|-----|-----|----|-----|-----|-----|----|-----|-----|-----|
|  1 | $G$ | $G$ | $G$ |  2 | $G$ | $G$ | $S$ |  3 | $G$ | $G$ | $N$ |
|  4 | $G$ | $G$ | $A$ |  5 | $G$ | $S$ | $G$ |  6 | $G$ | $S$ | $S$ |
| **7** | $\boldsymbol{G}$ | $\boldsymbol{S}$ | $\boldsymbol{N}$ | **8** | $\boldsymbol{G}$ | $\boldsymbol{S}$ | $\boldsymbol{A}$ |  9 | $G$ | $N$ | $G$ |
| **10** | $\boldsymbol{G}$ | $\boldsymbol{N}$ | $\boldsymbol{S}$ | 11 | $G$ | $N$ | $N$ | **12** | $\boldsymbol{G}$ | $\boldsymbol{N}$ | $\boldsymbol{A}$ |
| 13 | $G$ | $A$ | $G$ | **14** | $\boldsymbol{G}$ | $\boldsymbol{A}$ | $\boldsymbol{S}$ | **15** | $\boldsymbol{G}$ | $\boldsymbol{A}$ | $\boldsymbol{N}$ |
| 16 | $G$ | $A$ | $A$ | 17 | $S$ | $G$ | $G$ | 18 | $S$ | $G$ | $S$ |
| **19** | $\boldsymbol{S}$ | $\boldsymbol{G}$ | $\boldsymbol{N}$ | **20** | $\boldsymbol{S}$ | $\boldsymbol{G}$ | $\boldsymbol{A}$ | 21 | $S$ | $S$ | $G$ |
| 22 | $S$ | $S$ | $S$ | 23 | $S$ | $S$ | $N$ | 24 | $S$ | $S$ | $A$ |
| **25** | $\boldsymbol{S}$ | $\boldsymbol{N}$ | $\boldsymbol{G}$ | 26 | $S$ | $N$ | $S$ | 27 | $S$ | $N$ | $N$ |
| **28** | $\boldsymbol{S}$ | $\boldsymbol{N}$ | $\boldsymbol{A}$ | **29** | $\boldsymbol{S}$ | $\boldsymbol{A}$ | $\boldsymbol{G}$ | 30 | $S$ | $A$ | $S$ |
| **31** | $\boldsymbol{S}$ | $\boldsymbol{A}$ | $\boldsymbol{N}$ | 32 | $S$ | $A$ | $A$ | 33 | $N$ | $G$ | $G$ |
| **34** | $\boldsymbol{N}$ | $\boldsymbol{G}$ | $\boldsymbol{S}$ | 35 | $N$ | $G$ | $N$ | **36** | $\boldsymbol{N}$ | $\boldsymbol{G}$ | $\boldsymbol{A}$ |
| **37** | $\boldsymbol{N}$ | $\boldsymbol{S}$ | $\boldsymbol{G}$ | 38 | $N$ | $S$ | $S$ | 39 | $N$ | $S$ | $N$ |
| **40** | $\boldsymbol{N}$ | $\boldsymbol{S}$ | $\boldsymbol{A}$ | 41 | $N$ | $N$ | $G$ | 42 | $N$ | $N$ | $S$ |
| 43 | $N$ | $N$ | $N$ | 44 | $N$ | $N$ | $A$ | **45** | $\boldsymbol{N}$ | $\boldsymbol{A}$ | $\boldsymbol{G}$ |
| **46** | $\boldsymbol{N}$ | $\boldsymbol{A}$ | $\boldsymbol{S}$ | 47 | $N$ | $A$ | $N$ | 48 | $N$ | $A$ | $A$ |
| 49 | $A$ | $G$ | $G$ | **50** | $\boldsymbol{A}$ | $\boldsymbol{G}$ | $\boldsymbol{S}$ | **51** | $\boldsymbol{A}$ | $\boldsymbol{G}$ | $\boldsymbol{N}$ |
| 52 | $A$ | $G$ | $A$ | **53** | $\boldsymbol{A}$ | $\boldsymbol{S}$ | $\boldsymbol{G}$ | 54 | $A$ | $S$ | $S$ |
| **55** | $\boldsymbol{A}$ | $\boldsymbol{S}$ | $\boldsymbol{N}$ | 56 | $A$ | $S$ | $A$ | **57** | $\boldsymbol{A}$ | $\boldsymbol{N}$ | $\boldsymbol{G}$ |
| **58** | $\boldsymbol{A}$ | $\boldsymbol{N}$ | $\boldsymbol{S}$ | 59 | $A$ | $N$ | $N$ | 60 | $A$ | $N$ | $A$ |
| 61 | $A$ | $A$ | $G$ | 62 | $A$ | $A$ | $S$ | 63 | $A$ | $A$ | $N$ |
| 64 | $A$ | $A$ | $A$ |    |     |     |     |    |     |     |     |

````

## Variaciones simples

En las variaciones con repetición, cada objeto puede aparecer más de una vez en
la sucesión. Cuando, en cambio, cada objeto solo puede colocarse en una
posición, hablamos de _variaciones simples_, o _variaciones sin repetición_. En
este caso debemos imponer $k \leq n$, porque una vez que todos los $n$ objetos
han sido colocados en una sucesión no quedan más para elegir.

```{prf:definition} Variación simple
:label: def-es-variaciones-simples

Dado un conjunto de $n$ objetos $A = \{ a_1,\dots a_n \}$ y un número
$k \in \mathbb N$ con $k \leq n$, una _variación simple_ es una sucesión
$(a_{i_1}, \dots, a_{i_k})$, donde para todo $j = 1, \dots, k$ se tiene
$i_j \in \{1, \dots, n\}$ y $a_{i_j} \in A$, y para todo
$j, l = 1, \dots, k$ con $j \neq l$ se tiene $a_{i_j} \neq a_{i_l}$.
Denotamos por $d_{n, k}$ el número de variaciones simples posibles de $n$
objetos en $k$ casillas.
```

````{prf:example}
:label: ex-es-variaciones-simples-1

Si en {prf:ref}`ex-es-variaciones-con-repeticion-1` no fuera posible asignar
más de un turno diario a la misma persona, sucesiones como $(A, G, G)$ dejarían
de ser admisibles y cada programación correspondería a una y solo una variación
simple de cuatro objetos en tres casillas.
````

Para calcular el número $d_{n, k}$ de variaciones simples de $n$ objetos en $k$
casillas, podemos seguir un argumento análogo al de las permutaciones simples:

- el objeto a colocar en la primera casilla puede elegirse de $n$ maneras
  diferentes;
- la segunda casilla puede rellenarse de $n - 1$ maneras posibles, ya que el
  objeto seleccionado para la primera posición no puede reutilizarse;
- la tercera elección puede hacerse de $n - 2$ maneras, y así sucesivamente
  hasta la última casilla, que puede rellenarse eligiendo entre $n - k + 1$
  objetos.

Aplicando el principio fundamental de la combinatoria, obtenemos

```{math}
d_{n, k} = n (n-1) \ldots (n-k+1) =
n (n-1) \ldots (n-k+1) \cdot \frac{(n-k)!}{(n-k)!} =
\frac{n!}{(n-k)!} \enspace.
```

````{prf:example}
:label: ex-es-variaciones-simples-2

La {numref}`tab-es-variaciones-con-repeticion` destaca en negrita las
programaciones de {prf:ref}`ex-es-variaciones-simples-1`, cuyo número es igual a
$d_{4, 3} = 4 \cdot 3 \cdot 2 = 24$.
````

Cuando $k=n$, formar una variación requiere usar todos los elementos de $A$, de
modo que las permutaciones simples son un caso particular de las variaciones
simples. De manera coherente, $d_{n, n} = n!/0! = n! = p_n$.

## Ejercicios

```{exercise} •
:label: ex-es-var-shield-codigos

El sistema informático del [S.H.I.E.L.D.](https://marvel.fandom.com/wiki/S.H.I.E.L.D.)
genera códigos de acceso compuestos de cinco caracteres, cada uno elegido entre
ocho símbolos especiales, con repetición permitida. ¿Cuántos códigos distintos
pueden generarse?
```
```{solution} ex-es-var-shield-codigos
:class: dropdown

Cada código es una variación con repetición de $8$ símbolos en $5$ casillas,
por lo que el número de códigos distintos es $D_{8,5} = 8^5 = 32\,768$.
```

````{exercise} ••
:label: ex-es-var-wakanda-patrullas

La Guardia Real del [Wakanda](https://marvel.fandom.com/wiki/Wakanda) debe
planificar patrullas para los próximos tres días, seleccionando un guerrero
diferente cada día entre seis disponibles. ¿De cuántas maneras puede organizarse
el calendario?
````
````{solution} ex-es-var-wakanda-patrullas
:class: dropdown

Cada calendario es una variación simple de los seis guerreros en los tres días,
por lo que el calendario puede organizarse de $d_{6,3} = 6 \cdot 5 \cdot 4 =
120$ maneras diferentes.
````

````{exercise} ••
:label: ex-es-var-defenders-turnos

Los [Defenders](https://marvel.fandom.com/wiki/Defenders_(Earth-616)) deben
cubrir cuatro turnos distintos en un día (madrugada, mañana, tarde, noche),
eligiendo cada vez un miembro diferente entre nueve candidatos. ¿De cuántas
maneras puede elaborarse el turno?
````
````{solution} ex-es-var-defenders-turnos
:class: dropdown

Se trata de variaciones simples de $9$ objetos en $4$ casillas:

```{math}
d_{9,4} = 9 \cdot 8 \cdot 7 \cdot 6 = 3024.
```
````

````{exercise} ••
:label: ex-es-var-portavoz

Los miembros de los [Guardianes de la
Galaxia](https://marvel.fandom.com/wiki/Guardians_of_the_Galaxy_(Earth-616))
&mdash; Star-Lord, Gamora, Drax, Rocket y Groot &mdash; deben asignar tres
roles distintos: portavoz, portavoz adjunto y archivista. ¿Cuántas asignaciones
son posibles, dado que Groot no puede ser portavoz, ya que su lenguaje se limita
a la expresión «Yo soy Groot»?
````
````{solution} ex-es-var-portavoz
:class: dropdown

Sin restricciones, cada asignación correspondería a una de las
$d_{5, 3} = 5 \cdot 4 \cdot 3 = 60$ variaciones simples de héroes respecto a
los roles. Como fijar uno de los roles reduce el número de configuraciones
diferentes a $d_{4, 2} = 4 \cdot 3 = 12$ &mdash; ya que quedan dos roles y
cuatro personas &mdash; las asignaciones en las que Groot no es portavoz serán
$60 - 12 = 48$.
````

````{exercise} ••
:label: ex-es-var-young-avengers-restriccion

Para una misión de los [Young Avengers](https://marvel.fandom.com/wiki/Young_Avengers_(Earth-616)),
deben asignarse tres roles distintos (mando, reconocimiento, apoyo) a siete
héroes. ¿De cuántas maneras pueden asignarse los roles si Patriot y Wiccan no
pueden ser seleccionados juntos?
````
````{solution} ex-es-var-young-avengers-restriccion
:class: dropdown

Sin restricciones, habría $d_{7, 3} = 7 \cdot 6 \cdot 5 = 210$ maneras posibles
de proceder. A partir de este número, podemos restar los casos no permitidos, en
los que aparecen tanto Patriot como Wiccan. Como los tres roles son distintos,
los dos héroes pueden ocupar dos de ellos de $3 \cdot 2 = 6$ maneras diferentes
(son las variaciones $d_{3, 2}$ de tres roles en dos héroes; alternativamente,
elegir primero el rol de Patriot y luego el de Wiccan). El tercer rol puede
asignarse a uno de los $5$ héroes restantes. Los casos a excluir son, por tanto,
$6 \cdot 5 = 30$, y el número de configuraciones válidas es $210 - 30 = 180$.
````

````{exercise} •••
:label: ex-es-var-avengers-primero-ultimo

Los [Vengadores](https://marvel.fandom.com/wiki/Avengers) deben planificar una
secuencia de cuatro misiones consecutivas, eligiendo cada vez un miembro
diferente entre Iron Man, Thor, Capitán América, Viuda Negra y Ojo de Halcón.
Iron Man debe participar en la primera o en la última misión. ¿Cuántas
programaciones son posibles?
````
````{solution} ex-es-var-avengers-primero-ultimo
:class: dropdown

Contemos por separado los casos en que Iron Man es asignado a la primera o
última misión. Los dos conjuntos son disjuntos, porque cada héroe participa en
como máximo una misión y, por tanto, no puede ocupar ambas posiciones.

- Cuando Iron Man participa en la primera misión, las tres restantes pueden
  asignarse a los cuatro Vengadores restantes de
  $d_{4,3} = 4 \cdot 3 \cdot 2 = 24$ maneras diferentes.
- El argumento del punto anterior no cambia cuando Iron Man es asignado a la
  última misión.

Las programaciones válidas suman, por tanto, $24 + 24 = 48$.
````
