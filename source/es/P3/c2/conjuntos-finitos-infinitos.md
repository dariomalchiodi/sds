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

(sec_conjuntos-finitos-infinitos)=
# Conjuntos finitos e infinitos

No es difícil pensar en conjuntos que contienen un número finito de
elementos, como el conjunto de los miembros de la Justice League, el
conjunto de los días de la semana o el conjunto de los números primos
menores que $100$. Decimos que tales conjuntos son _finitos_. Sin embargo,
también existen conjuntos que no contienen un número finito de elementos,
como el conjunto de todas las fracciones o el conjunto de los puntos del
plano. Para estos conjuntos _infinitos_ se distinguen dos casos:

```{margin}
En matemáticas, se dice simplemente que un conjunto es _numerable_ si sus
elementos pueden listarse en una sucesión finita o infinita; los conjuntos
finitos son por tanto también numerables.
```
- se dice que un conjunto es _infinito numerable_ cuando es posible
  construir una sucesión (infinita) $x_1, x_2, \dots$ que contiene cada
  uno de sus elementos en alguna posición: el conjunto $D$ de los números
  impares, que introduciré en breve, es un ejemplo de conjunto infinito
  numerable;
- en todos los demás casos se dice que el conjunto es _infinito no
  numerable_: el conjunto de los puntos de una recta y el conjunto de los
  números reales son ambos infinitos y no numerables.

La descripción extensiva no es, en sentido estricto, aplicable a los
conjuntos infinitos, ya que por definición es imposible listar todos sus
elementos. Sin embargo, cuando un conjunto infinito numerable puede
asociarse a una sucesión que se puede intuir continuando después de ver
solo algunos de sus términos iniciales, resulta aceptable extender la
descripción extensiva listando solo esos elementos, añadiendo luego puntos
suspensivos para enfatizar el carácter infinito del conjunto. Por ejemplo,
aunque la descripción intensiva

```{math}
D = \{ 2n+1 \mid n \in \mathbb N \}
```

es la más precisa para designar el conjunto de los números impares, en
muchos contextos también se usa la formulación extensiva
$D = \{1, 3, 5, 7, 9, \dots \}$. Sin embargo, hay que tener en cuenta que
una sucesión parcial no puede identificar un conjunto de forma unívoca: en
el caso anterior, los primeros términos $1, 3, 5, 7, 9$ podrían en
principio referirse también al conjunto de los números impares menores que
$100$, o a cualquier otra sucesión que coincide con la de los impares en
los primeros elementos pero luego diverge. Los puntos suspensivos sugieren
cuáles son los elementos restantes, pero no los definen de manera rigurosa,
por lo que la descripción intensiva sigue siendo la formalmente correcta.
Con mayor razón, las descripciones extensivas no logran capturar la
complejidad de los conjuntos infinitos no numerables, para los cuales
generalmente solo son utilizables descripciones intensivas.

## Ejercicios

````{exercise}
:label: ex-es-suicide-squad

El [Suicide Squad](https://dc.fandom.com/wiki/Suicide_Squad_(Prime_Earth))
está compuesto por seis miembros: Emerald Empress, Doctor Polaris, Johnny
Sorrow, Lobo, Rustam y Cyclotron, cada uno de los cuales puede estar
operativo o fuera de combate. El estado del grupo se describe mediante un
vector $(x_1, x_2, x_3, x_4, x_5, x_6)$, donde para cada $i = 1, \dots 6$,
$x_i$ es igual a $1$ si el $i$-ésimo miembro (en el orden anterior) está
operativo, y $0$ en caso contrario. Responda las siguientes preguntas.

1. ¿Cuántos elementos contiene el conjunto de todos los estados posibles
   del grupo?
2. Sea $A$ el conjunto de los estados en que al menos uno de los miembros
   $1$ y $2$ está operativo, y al menos uno de los miembros $3$ y $4$ está
   operativo. Escriba código Python que liste todos los elementos de $A$.
3. Sea $B$ el conjunto de los estados en que los miembros $1$ y $3$ están
   ambos fuera de combate. ¿Cuántos elementos contiene $B$?
````
````{solution} ex-es-suicide-squad
:class: dropdown

1. Independientemente de $i$, cada componente $x_i$ puede tomar dos
   valores distintos, por lo que el principio fundamental de la
   combinatoria nos dice que el conjunto de todos los estados tiene
   $2^6 = 64$ elementos.

2. Las condiciones requeridas son $(x_1=1 \vee x_2=1)$ y
   $(x_3=1 \vee x_4=1)$. Los pares $(x_1, x_2)$ que satisfacen la
   primera condición son tres: $(1,0),(0,1),(1,1)$. Análogamente, existen
   tres configuraciones para $(x_3, x_4)$. En cambio, $(x_5, x_6)$ puede
   tomar las cuatro configuraciones posibles. Por el principio fundamental
   de la combinatoria, tenemos $|A| = 3 \times 3 \times 4 = 36$, y los
   elementos de $A$ son exactamente los vectores con
   $(x_1, x_2) \neq (0,0)$ y $(x_3, x_4) \neq (0,0)$, como confirma la
   salida del siguiente código.

```{code-cell} python
import itertools as it

v = (0, 1)
teams = [t for t in it.product(v, repeat=6)
           if (t[0] or t[1]) and (t[2] or t[3])]
for t in teams:
    print(t)
```

3. Con $x_1=0$ y $x_3=0$ fijos, las componentes restantes $x_2$, $x_4$,
   $x_5$ y $x_6$ son libres, por lo que $|B| = 2^4 = 16$.
````

````{exercise}
:label: ex-es-new-warriors

Los [New Warriors](https://marvel.fandom.com/wiki/New_Warriors_(Earth-616))
son un grupo de superhéroes de Marvel que, en una de sus formaciones, está
compuesto por seis miembros: Night Thrasher, Firestar, Justice, Namorita,
Speedball y Nova. Para cada uno de los siguientes conjuntos, determine si
es finito, infinito numerable o infinito no numerable, justificando su
respuesta.

1. El conjunto $W$ de los seis miembros de los New Warriors.
2. El conjunto $M$ de los posibles números de misión asignados
   progresivamente al grupo a partir de $1$, es decir,
   $M = \{1, 2, 3, 4, \dots\}$.
3. El conjunto $C$ de todos los pares $(i, n)$ donde
   $i \in [1 .. 6]$ identifica a uno de los seis miembros y
   $n \in \mathbb{N}$ es el número de la misión que dirige.
4. El conjunto $V$ de todos los posibles valores reales (en km/h) de la
   velocidad a la que Nova puede volar, sabiendo que su velocidad está en
   el intervalo $[0, 10^6]$.
````
````{solution} ex-es-new-warriors
:class: dropdown

1. $W$ es finito: contiene exactamente $6$ elementos, uno por cada miembro
   listado.
2. $M$ es infinito numerable: como el número total de misiones que los New
   Warriors emprenderán no se conoce de antemano, todo número natural es
   un posible número de misión. Por tanto $M = \mathbb{N}$, que es por
   definición numerable.
3. $C$ es infinito numerable. Para cada $i$ fijo existen infinitos valores
   de $n$, por lo que $C$ es infinito. Para demostrar la numerabilidad, se
   construye la sucesión $(1,1), (1,2), (1,3), \dots, (2,1), (2,2), \dots$
   que, una vez agotados los elementos con $i = j$, pasa a $i = j+1$.
   Como se concatenan seis sucesiones numerables, el resultado sigue siendo
   una sucesión numerable que lista todos los elementos de $C$.
4. $V$ es infinito no numerable: los posibles valores reales de velocidad
   pertenecen al intervalo $[0, 10^6]$, que es un subconjunto de
   $\mathbb{R}$, y todo intervalo de números reales es no numerable.
````

````{exercise}
:label: ex-es-great-lakes-avengers

Los [Great Lakes
Avengers](https://marvel.fandom.com/wiki/Great_Lakes_Avengers_(Earth-616))
son un excéntrico grupo de Marvel compuesto por seis miembros: Big Bertha,
Doorman, Flatman, Mr. Immortal, Dinah Soar y Grasshopper. Antes de cada
misión, el grupo asigna tres roles distintos — líder, táctico y explorador
— a tres miembros distintos. El orden de los roles es significativo (ser
líder es diferente de ser táctico). Sea $R$ el conjunto de todas las
posibles asignaciones de roles.

1. ¿Cuántos elementos contiene $R$?
2. Sea $D$ el conjunto de las asignaciones en que Doorman desempeña uno
   de los tres roles. ¿Cuántos elementos contiene $D$?
3. Escriba código Python que liste todos los elementos de $R$ y verifique
   los resultados de los puntos 1 y 2.
````
````{solution} ex-es-great-lakes-avengers
:class: dropdown

1. Debemos elegir, en orden, tres miembros distintos de entre seis, por lo
   que estamos contando las variaciones simples de seis objetos (los héroes)
   en tres lugares (los roles). Por tanto
   $|R| = d_{6, 3} = 6 \times 5 \times 4 = 120$.

2. Doorman puede desempeñar cualquiera de los tres roles. Una vez elegido
   el rol de Doorman, los dos roles restantes se asignan seleccionando dos
   miembros distintos de los cinco restantes, lo que puede hacerse de
   $d_{5, 2} = 5 \times 4 = 20$ formas. Por tanto
   $|D| = 3 \times d_{5, 2} = 60$.

3. En la celda siguiente, por brevedad, los superhéroes se denotan BB
   (Big Bertha), DM (Doorman), FM (Flatman), MI (Mr. Immortal), DS (Dinah
   Soar) y GH (Grasshopper). Usando `it.permutations` se pueden generar
   todas las variaciones que corresponden a los elementos de $R$,
   seleccionar las que pertenecen a $D$, imprimirlas y contarlas.

```{code-cell} python
import itertools as it

members = ['BB', 'DM', 'FM', 'MI', 'DS', 'GH']
roles = ['lider', 'tactico', 'explorador']

R = it.permutations(members, 3)

D = [t for t in R if 'DM' in t]

print('Elementos de D:')
for i, a in enumerate(D):
    print('-'.join(a), end=', ' if (i+1) % 6 else '\n')

print(f"\n|D| = {len(D)}")
```
````

````{exercise}
:label: ex-es-doom-patrol

La [Doom Patrol](https://dc.fandom.com/wiki/Doom_Patrol_(New_Earth)) es
un equipo de superhéroes marginados, entre los que se encuentran Robotman,
Negative Man, Elasti-Girl y Crazy Jane. Su archivo histórico etiqueta cada
enfrentamiento con un par de números naturales positivos $(v, s)$, donde
$v$ es el número de un cómic y $s$ el número del enfrentamiento dentro de
ese cómic. Sea $A = \{ (v, s) : v, s \in \mathbb{N} \}$ el conjunto de
todas las posibles etiquetas de enfrentamiento.

1. Demuestre que $A$ es infinito.
2. Demuestre que $A$ es numerable construyendo explícitamente una sucesión
   $a_1, a_2, a_3, \dots$ que lista cada elemento de $A$ en alguna
   posición, y deduzca la fórmula para la posición de un elemento genérico
   $(v, s)$.
3. ¿En qué posición se encuentra $(3, 2)$ en la sucesión del punto
   anterior?
````
````{solution} ex-es-doom-patrol
:class: dropdown

1. No existe un «último» número de cómic en principio, por lo que $A$
   contiene todos los pares $(v, i)$ para $v \in \mathbb N$ y es por tanto
   un conjunto infinito.

2. Se adopta la clásica _enumeración diagonal_: se considera la
   descomposición $A = \cup_{k=2}^{+\infty} D_k$, donde
   $D_k = \{ (v,s) \in A : v + s = k \}$ denota una _diagonal_ que
   contiene exactamente $k-1$ pares, ordenados como
   $(1, k-1), (2, k-2), \dots, (k-1, 1)$. Cada par $(v, s)$ pertenece a
   una y solo una diagonal, por lo que considerando todas las diagonales
   en orden y enumerando sus elementos, tras un número finito de pasos se
   debe alcanzar $(v, s)$. Por tanto $A$ es numerable.

3. Para $(3, 2)$ se tiene $k = 3 + 2 = 5$, por lo que el par pertenece a
   $D_5$. Generando los elementos de la sucesión correspondientes a las
   cuatro primeras diagonales se verifica que $(3, 2)$ aparece en la
   novena posición:

   ```{math}
   \underbrace{(1,1)}_{D_2},
   \underbrace{(1,2), (2,1)}_{D_3},
   \underbrace{(1,3), (2,2), (3,1)}_{D_4},
   \underbrace{(1,4), (2,3), (3,2), (4, 1)}_{D_5} \enspace.
   ```

````

````{exercise}
:label: ex-es-extensiva-intensiva

Para cada uno de los siguientes conjuntos, expresados en forma intensiva,
escriba — cuando sea posible — la descripción extensiva correspondiente, e
indique si es exacta o solo parcial.

1. $A = \{ n \in \mathbb{N} \mid n^2 \leq 25 \}$.
2. $B = \{ n \in \mathbb{Z} \mid -3 \leq n \leq 3 \}$.
3. $C = \{ n \in \mathbb{N} \mid n \text{ es múltiplo de } 3 \}$.
4. $D = \{ x \in \mathbb{R} \mid 1 \leq x \leq 2 \}$.
````
````{solution} ex-es-extensiva-intensiva
:class: dropdown

1. $A = \{ 1, 2, 3, 4, 5 \}$. El conjunto es finito, por lo que la
   descripción extensiva es exacta: lista precisamente todos y solo los
   elementos de $A$.

2. $B = \{ -3, -2, -1, 0, 1, 2, 3 \}$. También en este caso el conjunto
   es finito y la descripción extensiva es exacta.

3. Una posible descripción extensiva es $C = \{0, 3, 6, 9, \dots\}$. $C$
   es infinito numerable, por lo que la descripción extensiva es solo
   parcial: los puntos suspensivos sugieren el patrón pero no lo definen
   rigurosamente. En este caso, por ejemplo, los cuatro valores indicados
   también marcan el comienzo de la sucesión de los números cuyas cifras
   pertenecen todas a $\{ 0, 3, 6, 9 \}$, que continuaría con
   $30, 33, 36, 39, 60$, etc.

4. $D$ es un intervalo de números reales y por tanto es infinito no
   numerable; una descripción extensiva no es aplicable. No es posible
   elaborar una lista parcial de sus elementos que sea significativa.
````

````{exercise}
:label: ex-es-intensiva-extensiva

Para cada uno de los siguientes conjuntos, expresados en forma extensiva,
escriba una descripción intensiva equivalente.

1. $A = \{ \text{Thor}, \text{Iron Man}, \text{Captain America},
   \text{Hulk}, \text{Black Widow}, \text{Hawkeye} \}$.
2. $B = \{ 2, 4, 6, 8, \dots \}$.
3. $C = \{ 1, 4, 9, 16, 25, \dots \}$.
4. $D = \{ 0, 1 \}$.
````
````{solution} ex-es-intensiva-extensiva
:class: dropdown

1. Una posible descripción intensiva es
   $A = \{ x \mid x \text{ es un Avenger de la formación original} \}$.

2. La sucesión indicada sugiere que el conjunto contiene los números pares.
   En ese caso, dos posibles descripciones intensivas son
   $B = \{ n \in \mathbb N \mid n \text{ es par} \}$ y
   $B = \{ 2k \mid k \in \mathbb N \}$ (aunque la misma sucesión podría
   continuar de formas distintas, por ejemplo listando todos los números
   pares con cifras todas iguales).

3. La interpretación más sencilla sugiere que en la descripción extensiva
   se listan los primeros cuadrados perfectos (aunque también son posibles
   otras interpretaciones). En ese caso, se puede usar la formulación
   intensiva $C = \{ n^2 \mid n \in \mathbb N \}$, o equivalentemente
   $C = \{ n \in \mathbb N \mid \sqrt{n} \in \mathbb{N} \}$.

4. $D = \{ n \in \mathbb Z \mid 0 \leq n \leq 1 \}$, o bien
   $D = \{ x \in \mathbb R \mid x^2 = x \}$, o más simplemente
   $D = \{ x \in \mathbb R \mid x = 0 \vee x = 1 \}$.
````
