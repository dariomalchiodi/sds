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

(sec_principio-fundamental-combinatoria)=
# Principio fundamental

```{figure} https://static.wikia.nocookie.net/marvel_dc/images/8/8c/Detective_Comics_241.jpg/revision/latest?cb=20081218152007
---
figclass: margin
name: fig_dc-241-es
width: 200px
align: left
---
Portada de _Detective Comics_ número 241 (marzo de 1957). Marcas registradas y
Copyright © 1935–2026 DC Comics, Inc. Fuente: [DC Database, Fandom](https://dc.fandom.com/wiki/Detective_Comics_Vol_1_241).
```
Puede parecer extraño, pero en algunas historias Batman ha llevado trajes mucho
más coloridos que el clásico gris de los cómics originales o el negro de las
películas más recientes. El número 241 de _Detective Comics_ presenta una
historia titulada «The Rainbow Batman». En esta versión, el Caballero Oscuro
alterna atuendos naranja, verde y rosa, con el objetivo de atraer la atención
sobre sí mismo en lugar de sobre una herida en el brazo de Robin que podría
haber levantado sospechas al parecerse a la de Dick Grayson {cite}`robb`.
Modifiquemos ligeramente el escenario: imaginemos que Batman tiene en su armario
cuatro capas (rosa, verde, roja y marrón) y tres trajes (amarillo, azul celeste
y negro). ¿De cuántas maneras diferentes puede combinar una capa con un traje?
La {numref}`fig_principio-fundamental-es` muestra la respuesta: para cada una
de las cuatro capas hay tres trajes posibles, de modo que el total de
combinaciones es $4 \times 3 = 12$.

```{figure} ../../../_static/img/superhero-grid.png
:width: 50%
:name: fig_principio-fundamental-es

Una ilustración sencilla del principio fundamental de la combinatoria: con
cuatro opciones posibles para una primera elección y tres opciones para una
segunda, hay doce elecciones combinadas en total (imagen creada desde cero por
el autor con IA (ChatGPT) y postproducción gráfica).
```

Generalizando, obtenemos el llamado _principio fundamental de la combinatoria_:
al realizar $t$ elecciones, si la primera puede hacerse de $s_1$ maneras, la
segunda de $s_2$, la tercera de $s_3$, y así sucesivamente, entonces el número
total de secuencias de elecciones es

```{math}
s_1 \cdot \ldots \cdot s_t = \prod_{i=1}^t s_i \enspace.
```

El mismo resultado puede obtenerse construyendo un árbol de decisión: el número
de maneras posibles de realizar las $t$ elecciones es igual al número de hojas
de un árbol de profundidad $t$ en el que el primer nivel tiene $s_1$ nodos, cada
uno con $s_2$ hijos, donde cada hijo tiene a su vez $s_3$ hijos, y así
sucesivamente, tal como se ilustra en la {numref}`fig_arbol-es`.

```{figure} ../../../_static/img/superhero-tree.png
:width: 100%
:name: fig_arbol-es

El árbol correspondiente a las elecciones posibles en
{numref}`fig_principio-fundamental-es` (imagen creada desde cero por el autor
con IA (ChatGPT) y postproducción gráfica).
```

Como subrayé al principio del capítulo, la aplicación del principio fundamental
de la combinatoria no depende de la naturaleza de los objetos considerados, ya
sean capas, trajes, verduras o instrumentos financieros. Si en el ejemplo
anterior hubiéramos combinado tres colores con cuatro modelos de Batmóvil,
habríamos obtenido el mismo resultado numérico. Esto es válido en general: los
resultados de la combinatoria dependen del tamaño de los objetos y, cuando
proceda, del número de casillas consideradas. Por ello se habla, por ejemplo, de
las _permutaciones_ de $n$ objetos o de las _combinaciones_ de $n$ objetos en
$k$ casillas, usando los términos «objeto» y «casilla» en sentido abstracto. En
las secciones siguientes haré referencia con frecuencia a objetos específicos
para ilustrar los conceptos presentados.


## Ejercicios

````{exercise} •••
:label: ex-es-disp-justice-society-categorias

La [Justice Society of
America](https://dc.fandom.com/wiki/Justice_Society_of_America_(New_Earth))
envía tres miembros en misión en secuencia (el primero inicia las hostilidades,
el segundo interviene en plena batalla, el tercero cubre la retirada), eligiendo
entre cuatro superhéroes con poderes sobrenaturales (Green Lantern, Flash,
Doctor Fate y Hourman) y tres vigilantes sin superpoderes (Sandman, Wildcat y
Starman). ¿Cuántas secuencias son posibles si la primera posición debe ser
ocupada por un superhéroe y la última por un vigilante?
````
````{solution} ex-es-disp-justice-society-categorias
:class: dropdown

Las tres casillas deben rellenarse respetando las restricciones de categoría:

- la primera casilla corresponde a uno de los cuatro superhéroes con poderes
  sobrenaturales;
- la última casilla corresponde a uno de los tres vigilantes;
- la posición central puede estar ocupada por cualquiera de los cinco héroes
  restantes.

Por el principio fundamental de la combinatoria, el número de secuencias válidas
es $4 \cdot 5 \cdot 3 = 60$.
````

````{exercise} ••
:label: ex-es-fpc-xmen-amenaza

Para clasificar una misión de los X-Men, Cerebro asigna:

- un nivel de amenaza de entre $6$ valores posibles;
- una prioridad de entre $4$ valores posibles;
- un sector operativo de entre $5$ valores posibles.

¿Cuántos códigos de misión distintos puede producir?
````
````{solution} ex-es-fpc-xmen-amenaza
:class: dropdown

Cada código se obtiene eligiendo sucesivamente un valor para cada una de las
tres categorías. Por el principio fundamental de la combinatoria, los códigos
posibles son $6 \cdot 4 \cdot 5 = 120$.
````

````{exercise} ••
:label: ex-es-fpc-avengers-turnos

Los Vengadores deben cubrir tres turnos (mañana, tarde, noche), eligiendo
siempre un miembro diferente entre ocho disponibles. ¿De cuántas maneras puede
elaborarse el turno diario?
````
````{solution} ex-es-fpc-avengers-turnos
:class: dropdown

Para el turno de mañana hay ocho opciones, para el de tarde siete (porque el
miembro elegido por la mañana no puede reutilizarse) y para el de noche seis
(por un argumento análogo). Por el principio fundamental de la combinatoria,
las maneras posibles de asignar los turnos son $8 \cdot 7 \cdot 6 = 336$.
````

````{exercise} •••
:label: ex-es-fpc-defenders-restriccion-lider

Los [Defenders](https://marvel.fandom.com/wiki/Defenders_(Earth-616)) deben
asignar tres roles distintos: líder del equipo, analista táctico y apoyo
operativo, entre siete candidatos. Jessica Jones, si es seleccionada, solo puede
ocupar el rol de líder del equipo. ¿Cuántas asignaciones son posibles?
````
````{solution} ex-es-fpc-defenders-restriccion-lider
:class: dropdown

Consideremos por separado los casos en que Jessica Jones es seleccionada o no.
En el primer caso, el rol de líder queda fijado, y los dos roles restantes
pueden asignarse a los seis candidatos restantes de $d_{6, 2}$ maneras. En el
segundo caso, solo hay seis candidatos para los tres roles, por lo que hay
$d_{6, 3}$ maneras de proceder. Sumando los dos resultados, las asignaciones
posibles son $d_{6, 2} + d_{6, 3} = 6 \cdot 5 + 6 \cdot 5 \cdot 4 = 30 + 120
= 150$.
````
