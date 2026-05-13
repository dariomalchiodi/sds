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

(sec_operaciones-conjuntos)=
# Operaciones entre conjuntos

Además de utilizar las relaciones descritas en la sección anterior, es
posible construir nuevos conjuntos a partir de conjuntos existentes
utilizando las operaciones que se describen a continuación.

- La _unión_ de dos conjuntos $S$ y $T$ es el conjunto $S \cup T$ de todos
  los elementos que pertenecen a al menos uno de ellos. Formalmente,
  $S \cup T = \{x \in \Omega \mid x \in S \vee x \in T \}$.
- La _intersección_ de dos conjuntos $S$ y $T$ es el conjunto $S \cap T$
  de los elementos comunes a ambos:
  $S \cap T = \{ x \in \Omega \mid x \in S \wedge x \in T \}$.
- La _diferencia_ entre un conjunto $S$ y un conjunto $T$ es el conjunto
  $S \setminus T$ de los elementos de $S$ que no pertenecen a $T$:
  $S \setminus T = \{ x \in \Omega \mid x \in S \wedge x \notin T \}$.
- La _diferencia simétrica_ entre dos conjuntos $S$ y $T$ es el conjunto
  $S \ominus T$ de los elementos que pertenecen a exactamente uno de los
  dos conjuntos:
  $S \ominus T = \{ x \in \Omega \mid ( x \in S \wedge x \notin T )
  \vee ( x \notin S \wedge x \in T) \}$.
- El _complemento_ de un conjunto $S$ es el conjunto $\overline S$ de los
  elementos del universo que no pertenecen a $S$:
  $\overline S = \{ x \in \Omega \mid x \notin S \} = \Omega \setminus S$.


```{code-cell} python
:tags:  [hide-input]

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch

MATH_SIZE = 9
TEXT_SIZE = 7
EDGE_COLOR = '#333333'
BG_COLOR   = '#eaf3f5'
FILL_COLOR = '#d6e4f7'
HIGHLIGHT  = '#aac5e8'
DOT_COLOR  = '#2255aa'

O_XY = (5, 3.7); O_W, O_H = 5.5, 4.8
V_XY = (7.8, 4.0); V_W, V_H = 4.5, 3.8

ELEMS_O   = [('Captain\nAmerica', 3.0, 4.5,  1.0,  0.),
             ('Hulk',             3.5, 2.8,  0.65, 0.0)]
ELEMS_OV  = [('Thor',             6.2, 4.2,  0.75, 0.0)]
ELEMS_V   = [('Iron\nMan',        9.3, 4.5,  -0.6,  0.)]
ELEMS_OUT = [('Black\nWidow',     1.2, 7.0,  0, -0.6),
             ('Hawkeye',         10.8, 1.5, -0.85, -0.4)]
ELEMS_COMPLEMENT = [('Ant-Man',      10.5, 6.5, -0.85, -0.4)]

def _setup_ax(ax, s=1, box_fill=None, labels=True):
    ax.set_facecolor(BG_COLOR)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.add_patch(FancyBboxPatch((0.2, 0.2), 11.6, 7.6,
                               boxstyle='square,pad=0',
                               facecolor=box_fill or BG_COLOR, edgecolor=EDGE_COLOR,
                               linewidth=1.1 * s, zorder=0))
    ax.text(11.5, 7.5, r'$\Omega$', fontsize=MATH_SIZE * s, ha='right', va='top')
    if labels:
        ax.text( 3, 6.3, r'$O$', fontsize=MATH_SIZE * s, va='top')
        ax.text(9, 6.2, r'$V$',  fontsize=MATH_SIZE * s, va='top')

def _add_borders(ax, s=1):
    for xy, w, h in [(O_XY, O_W, O_H), (V_XY, V_W, V_H)]:
        ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                             facecolor='none', edgecolor=EDGE_COLOR,
                             linewidth=1.2 * s, zorder=4))

def _add_elements(ax, s=1):
    for name, x, y, xof, yof in ELEMS_O + ELEMS_OV + ELEMS_V + ELEMS_OUT:
        ax.plot(x, y, 'o', markersize=4 * s, color=DOT_COLOR, zorder=5)
        ax.text(x + xof, y + yof, name, ha='center', va='center',
                fontsize=TEXT_SIZE * s, zorder=6)

def _fill_intersection(ax, color):
    clip = Ellipse(xy=V_XY, width=V_W, height=V_H,
                   facecolor='none', edgecolor='none')
    ax.add_patch(clip)
    hl = Ellipse(xy=O_XY, width=O_W, height=O_H,
                 facecolor=color, edgecolor='none', zorder=2)
    ax.add_patch(hl)
    hl.set_clip_path(clip)

def venn_union(ax, s=1):
    _setup_ax(ax, s)
    for xy, w, h in [(O_XY, O_W, O_H), (V_XY, V_W, V_H)]:
        ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                             facecolor=HIGHLIGHT, edgecolor='none', zorder=1))
    _add_borders(ax, s)
    _add_elements(ax, s)

def venn_intersection(ax, s=1):
    _setup_ax(ax, s)
    for xy, w, h in [(O_XY, O_W, O_H), (V_XY, V_W, V_H)]:
        ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                             facecolor=FILL_COLOR, edgecolor='none', zorder=1))
    _fill_intersection(ax, HIGHLIGHT)
    _add_borders(ax, s)
    _add_elements(ax, s)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.8, 4.8), facecolor=BG_COLOR)
venn_union(ax1, s=2)
venn_intersection(ax2, s=2)
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_es-venn-union-interseccion

Diagramas de Venn para la unión $O \cup V$ (izquierda) y la intersección
$O \cap V$ (derecha), donde $O$ es el conjunto de los Avengers con fuerza
sobrehumana y $V$ el de los Avengers que pueden volar. En ambos casos, la
región azul más oscura describe el conjunto de interés y la región más
clara indica las partes de $O$ o $V$ que no pertenecen a él.
````

````{prf:example}
:label: ex-es-operaciones-conjuntos

Consideremos el universo $\Omega$ de todos los Avengers, y definamos en su
interior los conjuntos $O = \{\text{Captain America}, \text{Hulk}, \text{Thor}\}$
y $V = \{\text{Thor}, \text{Iron Man}\}$, que contienen respectivamente
los Avengers con fuerza sobrehumana y los que pueden volar.
La {numref}`fig_es-venn-union-interseccion` muestra los diagramas de Venn de
- $O \cup V = \{\text{Captain America}, \text{Hulk}, \text{Thor},
\text{Iron Man}\}$, que incluye a todos los héroes considerados, y
- $O \cap V = \{\text{Thor}\}$, que contiene al único Avenger con fuerza
  sobrehumana que también puede volar.

De manera análoga, la {numref}`fig_es-venn-diferencia` ilustra la diferencia
$O \setminus V = \{\text{Captain America}, \text{Hulk}\}$ de todos los
héroes con superfuerza que no pueden volar, y la diferencia simétrica
$O \ominus V = \{\text{Captain America}, \text{Hulk}, \text{Iron Man}\}$,
de la que Thor queda excluido porque pertenece a ambos conjuntos. Es
importante destacar que la diferencia entre conjuntos no es simétrica: un
contraejemplo sencillo es el hecho de que
$V \setminus O = \{\text{Iron Man}\} \neq O \setminus V$.

Finalmente, el complemento $\overline O$ corresponde al conjunto de los
Avengers sin fuerza sobrehumana: Iron Man, Black Widow, Hawkeye y Ant-Man,
como se ilustra en la {numref}`fig_es-venn-complemento`.
````

```{code-cell} python
:tags:  [hide-input]

def venn_difference(ax, s=1):
    _setup_ax(ax, s)
    ax.add_patch(Ellipse(xy=O_XY, width=O_W, height=O_H,
                         facecolor=HIGHLIGHT, edgecolor='none', zorder=1))
    ax.add_patch(Ellipse(xy=V_XY, width=V_W, height=V_H,
                         facecolor=FILL_COLOR, edgecolor='none', zorder=2))
    _add_borders(ax, s)
    _add_elements(ax, s)

def venn_symdiff(ax, s=1):
    _setup_ax(ax, s)
    for xy, w, h in [(O_XY, O_W, O_H), (V_XY, V_W, V_H)]:
        ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                             facecolor=HIGHLIGHT, edgecolor='none', zorder=1))
    _fill_intersection(ax, FILL_COLOR)
    _add_borders(ax, s)
    _add_elements(ax, s)

fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.8, 4.8), facecolor=BG_COLOR)
venn_difference(ax1, s=2)
venn_symdiff(ax2, s=2)
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_es-venn-diferencia

Diagramas de Venn para la diferencia $O \setminus V$ (izquierda) y la
diferencia simétrica $O \ominus V$ (derecha). Misma notación que en
la {numref}`fig_es-venn-union-interseccion`.
````



```{code-cell} python
:tags:  [hide-input]

def venn_complement(ax, s=1):
    _setup_ax(ax, s, box_fill=HIGHLIGHT, labels=False)
    ax.text(3.5, 6.7, r'$O$', fontsize=MATH_SIZE * s, va='top')
    ax.add_patch(Ellipse(xy=O_XY, width=O_W, height=O_H,
                         facecolor=FILL_COLOR, edgecolor=EDGE_COLOR,
                         linewidth=1.2 * s, zorder=1))
    for name, x, y, xof, yof in ELEMS_O + ELEMS_OV:
        ax.plot(x, y, 'o', markersize=4 * s, color=DOT_COLOR, zorder=4)
        ax.text(x + xof, y + yof, name, ha='center', va='center',
                fontsize=TEXT_SIZE * s, zorder=5)
    for name, x, y, xof, yof in ELEMS_V + ELEMS_OUT + ELEMS_COMPLEMENT:
        ax.plot(x, y, 'o', markersize=4 * s, color=DOT_COLOR, zorder=4)
        ax.text(x + xof, y + yof, name, ha='center', va='center',
                fontsize=TEXT_SIZE * s, zorder=5)

fig3, ax = plt.subplots(facecolor=BG_COLOR)
venn_complement(ax)
plt.tight_layout()
plt.show()
```
````{customfigure}
:name: fig_es-venn-complemento

Diagrama de Venn para el complemento $\overline O$: la región resaltada
contiene todos los Avengers que no pertenecen a $O$. Misma notación que en
la {numref}`fig_es-venn-union-interseccion`.
````

Es fácil verificar que las operaciones de unión e intersección son

- conmutativas: $S \cup T = T \cup S$ y $S \cap T = T \cap S$ siempre se
  cumplen, por lo que los dos conjuntos pueden intercambiarse sin modificar
  su unión ni su intersección;
- asociativas: $S \cup ( T \cup U ) = (S \cup T ) \cup U$ y
  $S \cap ( T \cap U ) = (S \cap T ) \cap U$, lo que significa que el orden
  en que se realizan dos uniones (o dos intersecciones) es indiferente, por
  lo que se puede escribir por ejemplo $S \cup T \cup U$ sin ambigüedad;
- distributivas entre sí: $S \cup (T \cap U) = (S \cup T) \cap (S \cup U)$
  y $S \cap (T \cup U) = (S \cap T) \cup (S \cap U)$, en analogía con la
  distribución de la multiplicación respecto de la suma en aritmética (donde
  $a \cdot (b + c) = a \cdot b + a \cdot c$), con la diferencia de que aquí
  la propiedad se cumple en ambas direcciones.

````{prf:theorem} Leyes de De Morgan
:label: teo-es-de-morgan

Para todo par de conjuntos $S, T \subseteq \Omega$, se cumplen las _leyes
de De Morgan_:

1. $\overline{\left( S \cup T \right)} = \overline S \cap \overline T$;
2. $\overline{\left( S \cap T \right)} = \overline S \cup \overline T$.
````
````{admonition} _
:class: myproof

Demostramos la primera ley. Fijemos $x \in \overline{\left( S \cup T \right)}$;
por definición de complemento, $x \notin \left( S \cup T \right)$, lo que
implica $x \notin S$ y $x \notin T$. Usando de nuevo la definición de
complemento, obtenemos $x \in \overline S$ y $x \in \overline T$, y por
tanto $x \in \overline S \cap \overline T$. Como no se ha hecho ninguna
hipótesis particular sobre $x$ salvo $x \in \overline{(S \cup T)}$, hemos
demostrado que
$\overline{\left( S \cup T \right)} \subseteq \overline S \cap \overline T$.
Procediendo en sentido inverso (partiendo de
$x \in \overline S \cap \overline T$) se puede demostrar que
$\overline S \cap \overline T \subseteq \overline{\left( S \cup T \right)}$,
obteniendo así la primera ley de De Morgan. La segunda ley se demuestra de
forma análoga.
````

Las leyes de De Morgan nos dicen esencialmente que es posible «transferir»
la operación de complemento desde la unión de dos conjuntos a los dos
conjuntos individualmente, teniendo cuidado de convertir la unión en
intersección (y una operación análoga vale para el complemento de una
intersección).

Las siguientes relaciones también conectan la diferencia simétrica, la
unión, la intersección y la diferencia entre conjuntos.

````{prf:theorem}
:label: teo-es-set-difference

Dados dos conjuntos $S, T \subseteq \Omega$:

1. $S \ominus T = (S \setminus T) \cup (T \setminus S)$,
2. $S \ominus T = (S \cup T) \setminus (S \cap T)$.
````
````{admonition} _
:class: myproof

La primera relación es consecuencia directa de la definición de diferencia
simétrica: en efecto, para todo $x \in \Omega$,

```{math}
x \in S \ominus T \leftrightarrow
(x \in S \wedge x \notin T) \vee (x \notin S \wedge x \in T) \leftrightarrow
(x \in S \setminus T) \vee (x \in T \setminus S) \leftrightarrow
x \in (S \setminus T) \cup (T \setminus S) \enspace.
```

Para la segunda relación, supongamos $x \in (S \cup T) \setminus (S \cap T)$;
entonces $x \in (S \cup T)$ y $x \notin (S \cap T)$, lo que implica
$(x \in S \vee x \in T) \wedge (x \notin S \cap T)$. Distribuyendo la
disyunción sobre la conjunción se obtiene
$(x \in S \wedge x \notin S \cap T) \vee (x \in T \wedge x \notin S \cap T)$.
Por tanto $x \in S \setminus T \vee x \in T \setminus S$, y la primera
relación ya demostrada implica $x \in S \ominus T$. Así
$(S \cup T) \setminus (S \cap T) \subseteq S \ominus T$. Procediendo de
forma análoga se demuestra
$S \ominus T \subseteq (S \cup T) \setminus (S \cap T)$, lo que da la
tesis.
````

Las operaciones de unión e intersección permiten introducir la _partición_
de un conjunto, entendida como una descomposición de este en partes no
solapadas.

````{prf:definition} Partición
:label: def-es-partition

Una _partición_ de un conjunto $S$ es una familia
$\mathcal{P} = \{ P_1, P_2, \ldots, P_k \}$ de subconjuntos no vacíos de
$S$, llamados _bloques_ o _clases_, tal que:

1. $P_i \cap P_j = \varnothing$ para todo $i \neq j$ (los bloques no se
   solapan);
2. $\cup_{i=1}^k P_i = S$ (los bloques cubren $S$).
````

En otras palabras, una partición asigna cada elemento de $S$ a exactamente
una clase: cada elemento pertenece a uno y solo un bloque. Una consecuencia
inmediata de la definición es que dos bloques distintos $P_i$ y $P_j$ no
pueden compartir un elemento.

````{prf:example}
:label: ex-es-particiones

Consideremos el conjunto de los Avengers en su formación original:
$S = \{ \text{Captain America}, \text{Hulk}, \text{Thor},
\text{Iron Man}, \text{Black Widow}, \text{Hawkeye} \}$.

- La familia
  $\mathcal{P}_1 = \bigl\{
  \{\text{Captain America}, \text{Iron Man}\},\,
  \{\text{Hulk}, \text{Thor}\},\,
  \{\text{Black Widow}, \text{Hawkeye}\}
  \bigr\}$
  es una partición de $S$: los tres bloques son disjuntos y juntos cubren
  a todos los héroes.

- En cambio, la familia
  $\mathcal{P}_2 = \bigl\{
  \{\text{Captain America}, \text{Hulk}, \text{Thor}\},\,
  \{\text{Thor}, \text{Iron Man}, \text{Black Widow}, \text{Hawkeye}\}
  \bigr\}$
  no es una partición de $S$, ya que Thor aparece en ambos bloques.

- De manera similar,
  $\mathcal{P}_3 = \bigl\{
  \{\text{Captain America}, \text{Thor}, \text{Iron Man}\},\,
  \{\text{Hulk}, \text{Black Widow}\}
  \bigr\}$
  no es una partición de $S$, porque Hawkeye no pertenece a ningún bloque.
````

Un conjunto $S$ siempre admite dos particiones triviales: la formada por
un único bloque $\{S\}$, y la en que cada bloque es un singleton,
$\bigl\{ \{s\} \mid s \in S \bigr\}$. Finalmente, una partición de $S$ en
dos bloques está estrechamente relacionada con la operación de complemento:
si $A \subseteq S$ es un subconjunto no vacío y distinto de $S$, entonces
$\{A,\, S \setminus A\}$ es una partición de $S$ en dos bloques.


## Ejercicios

````{exercise}
:label: ex-es-conjuntos-base

Sea
```{math}
\Omega = \{ \text{Batman}, \text{Superman}, \text{Thor}, \text{Wolverine},
        \text{Deadpool}, \text{Storm}, \text{Cyborg} \} \enspace.
```
Partiendo de los siguientes conjuntos de superhéroes:

```{math}
\begin{align*}
A &= \{ \text{Batman}, \text{Thor}, \text{Deadpool},
        \text{Cyborg} \} \enspace, \\
B &= \{ \text{Superman}, \text{Thor}, \text{Storm},
        \text{Wolverine} \} \enspace, \\
C &= \{ \text{Deadpool}, \text{Cyborg}, \text{Batman} \} \enspace,
\end{align*}
```

describa extensivamente los siguientes conjuntos:

1. $A \cap B$,
2. $\overline C$,
3. $A \setminus C$,
4. $A \ominus B$,
5. $\overline A \cap (B \cup C)$,
6. $A \cup (B \cap C)$,
7. $(A \cap \overline B) \cup C$,
8. $(A \cap C) \cup (B \cap C)$.
````

````{solution} ex-es-conjuntos-base
:class: dropdown

1. $A \cap B = \{\text{Thor}\}$.
2. $\overline C = B = \{ \text{Superman}, \text{Thor}, \text{Storm},
   \text{Wolverine} \}$.
3. $A \setminus C = \{ \text{Thor} \}$.
4. $A \cup B = \Omega$ y $A \cap B = \{\text{Thor}\}$, por lo que
   $A \ominus B = \Omega \setminus \{ \text{Thor} \} =
   \{ \text{Batman}, \text{Superman}, \text{Wolverine},
   \text{Deadpool}, \text{Storm}, \text{Cyborg} \}$.
5. $\overline A = \{\text{Superman}, \text{Wolverine}, \text{Storm} \}$ y
   $B \cup C = \Omega$, por lo que $\overline A \cap (B \cup C) = \overline A
   = \{ \text{Superman}, \text{Wolverine}, \text{Storm} \}$.
6. $B \cap C = \varnothing$, por lo que $A \cup (B \cap C) = A = \{ \text{Batman},
   \text{Thor}, \text{Deadpool}, \text{Cyborg}\}$.
7. $A \cap \overline B = \{ \text{Batman}, \text{Deadpool}, \text{Cyborg} \}
   = C$, por lo que $(A \cap \overline B) \cup C = C = \{ \text{Batman},
   \text{Deadpool}, \text{Cyborg} \}$.
8. Como $C \subseteq A$, se tiene $A \cap C = C$. Además,
   $B \cap C = \varnothing$, por lo que $(A \cap C) \cup (B \cap C) = C =
   \{ \text{Batman}, \text{Deadpool}, \text{Cyborg} \}$.
````

````{exercise}
:label: ex-es-tres-conjuntos

Sean $E$, $F$ y $G$ tres conjuntos de superhéroes. Escriba las expresiones
algebraicas, en términos de intersecciones, uniones y complementos, que
permiten expresar los siguientes conjuntos.

 1. Solo los superhéroes en $E$.
 2. Los superhéroes en $E$ y $G$, pero no en $F$.
 3. Los superhéroes en al menos uno de los tres conjuntos.
 4. Los superhéroes en al menos dos de los tres conjuntos.
 5. Los superhéroes en los tres conjuntos.
 6. Ningún superhéroe (el conjunto vacío).
 7. Los superhéroes en a lo sumo un conjunto.
 8. Los superhéroes en a lo sumo dos conjuntos.
 9. Los superhéroes en exactamente dos conjuntos.
10. Los superhéroes en a lo sumo tres conjuntos.
````
````{solution} ex-es-tres-conjuntos
:class: dropdown

 1. $E \cap \overline F \cap \overline G$.
 2. $E \cap G \cap \overline F$.
 3. $E \cup F \cup G$.
 4. $(E \cap F) \cup (E \cap G) \cup (F \cap G)$.
 5. $E \cap F \cap G$.
 6. $\emptyset$.
 7. Es el complemento del conjunto del punto 4:

    ```{math}
    \overline{E \cap F} \cap \overline{E \cap G} \cap \overline{F \cap G}.
    ```

 8. El conjunto requerido es el complemento del obtenido en el punto 5:
    $\overline{E \cap F \cap G}$.
 9. Estar en exactamente dos conjuntos equivale a estar en al menos dos,
    pero no en los tres:

    ```{math}
    \bigl( (E \cap F) \cup (E \cap G) \cup (F \cap G) \bigr)
    \cap \overline{E \cap F \cap G}.
    ```

10. Todo superhéroe pertenece por definición a lo sumo a tres conjuntos.
    Por tanto el conjunto requerido es el universo $\Omega$.
````

````{exercise}
:label: ex-es-simplificar

Simplifique, cuando sea posible, las siguientes expresiones.

1. $E \cup \overline E$.
2. $E \cap \overline E$.
3. $(E \cup F) \cap (E \cup \overline F)$.
4. $(E \cup F) \cap (\overline E \cup F) \cap (E \cup \overline F)$.
5. $(E \cup F) \cap (F \cup G)$.
````

````{solution} ex-es-simplificar
:class: dropdown

1. $E \cup \overline E = \Omega$ por el _principio del tercero excluido_:
   una proposición debe ser verdadera o falsa, por lo que para todo
   $\omega \in \Omega$ se cumple $\omega \in E$ o $\omega \notin E$, lo
   que hace que $\omega \in E \cup \overline E$ y da el universo.

2. $E \cap \overline E = \varnothing$ por el _principio de no contradicción_:
   una proposición no puede ser a la vez verdadera y falsa, por lo que para
   todo $\omega \in \Omega$ exactamente una de las proposiciones $\omega \in E$
   y $\omega \notin E$ es verdadera, haciendo falsa su conjunción. Por tanto
   ningún $\omega \in \Omega$ pertenece a $E \cap \overline E$, lo que lo
   caracteriza como el conjunto vacío.

3. Por la distributividad de la unión respecto de la intersección,
   $(E \cup F) \cap (E \cup \overline F) = E \cup (F \cap \overline F) =
   E \cup \varnothing = E$.

4. Por la asociatividad de la intersección,
   $(E \cup F) \cap (\overline E \cup F) \cap (E \cup \overline F) =
   (E \cup F) \cap (E \cup \overline F) \cap (\overline E \cup F)$; por
   el resultado del punto anterior, la primera intersección es igual a $E$,
   por lo que toda la expresión se reduce a $E \cap (\overline E \cup F) =
   (E \cap \overline E) \cup (E \cap F) = \varnothing \cup (E \cap F) =
   E \cap F$.

5. Por la conmutatividad de la intersección,
   $(E \cup F) \cap (F \cup G) = (F \cup E) \cap (F \cup G)$, y aplicando
   la distributividad de la intersección respecto de la unión se obtiene
   $(F \cup E) \cap (F \cup G) = F \cup (E \cap G)$.
````

````{exercise}
:label: ex-es-justice-league-dark

Dados tres conjuntos $M$, $D$, $H$ en un universo $\Omega$, demuestre la
validez de las siguientes relaciones usando diagramas de Venn.

1. $M \cap D \subseteq M \subseteq M \cup D$.
2. Si $H \subseteq \overline M$, entonces $M \subseteq \overline H$.
3. $D = (D \cap M) \cup (D \cap \overline M)$.
4. $M \cup D = M \cup (\overline M \cap D)$.
````

````{solution} ex-es-justice-league-dark
:class: dropdown

1. $M \cap D \subseteq M \subseteq M \cup D$

El diagrama siguiente muestra los tres conjuntos: el rayado diagonal
descendente cubre la unión $M \cup D$; el relleno azul de $M$ se superpone
a este rayado, haciendo visible que $M$ está contenido en $M \cup D$; el
rayado diagonal ascendente marca $M \cap D$, que queda por tanto
completamente contenido en $M$.

```{code-cell} python
:tags: [hide-input]

BG_COLOR = 'white'

def _ex_setup_ax(ax):
    ax.set_facecolor(BG_COLOR)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.add_patch(FancyBboxPatch((0.2, 0.2), 11.6, 7.6,
                                boxstyle='square,pad=0',
                                facecolor=BG_COLOR, edgecolor=EDGE_COLOR,
                                linewidth=1.1, zorder=0))
    ax.text(11.5, 7.5, r'$\Omega$', fontsize=MATH_SIZE, ha='right', va='top')

_M2_XY = (5.0, 3.7); _M2_W, _M2_H = 5.5, 4.8
_D2_XY = (7.8, 4.0); _D2_W, _D2_H = 4.5, 3.8

fig, ax = plt.subplots(figsize=(3.2, 2.4), facecolor=BG_COLOR)
_ex_setup_ax(ax)
ax.text(2.5, 6.3, r'$M$', fontsize=MATH_SIZE, va='top')
ax.text(9.3, 6.1, r'$D$', fontsize=MATH_SIZE, va='top')

ax.add_patch(Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                        facecolor=FILL_COLOR, edgecolor=EDGE_COLOR,
                        hatch='\\\\', linewidth=0, zorder=2))
ax.add_patch(Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                        facecolor=BG_COLOR, edgecolor=EDGE_COLOR,
                        hatch='\\\\', linewidth=0, zorder=1))

ax.add_patch(Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                     facecolor=HIGHLIGHT, alpha=0.5, edgecolor='none', zorder=1))

_clip_D = Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                  facecolor='none', edgecolor='none')
ax.add_patch(_clip_D)
_inter_hatch = Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                       facecolor='none', edgecolor=EDGE_COLOR, hatch='//', zorder=3)
ax.add_patch(_inter_hatch)
_inter_hatch.set_clip_path(_clip_D)

for xy, w, h in [(_M2_XY, _M2_W, _M2_H), (_D2_XY, _D2_W, _D2_H)]:
    ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                          facecolor='none', edgecolor=EDGE_COLOR,
                          linewidth=1.2, zorder=4))
plt.tight_layout()
plt.show()
```

2. Si $H \subseteq \overline{M}$, entonces $M \subseteq \overline{H}$

Como $H \subseteq \overline{M}$, todo elemento de $H$ no es elemento de
$M$, lo que significa que los dos conjuntos deben ser disjuntos, como se
muestra en el diagrama siguiente. En consecuencia, ningún elemento de $M$
puede ser elemento de $H$, lo que significa $M \subseteq \overline{H}$.

```{code-cell} python
:tags: [hide-input]

_H2_XY  = (3.5, 4.0); _H2_W,  _H2_H  = 4.2, 3.8
_M2d_XY = (8.5, 4.0); _M2d_W, _M2d_H = 4.2, 3.8

fig, ax = plt.subplots(figsize=(3.2, 2.4), facecolor=BG_COLOR)
_ex_setup_ax(ax)
ax.text(1.2,  6.2, r'$H$', fontsize=MATH_SIZE, va='top')
ax.text(10.4, 6.2, r'$M$', fontsize=MATH_SIZE, va='top')

ax.add_patch(Ellipse(xy=_H2_XY, width=_H2_W, height=_H2_H,
                          facecolor=FILL_COLOR, edgecolor=EDGE_COLOR,
                          linewidth=1.2, zorder=4))
ax.add_patch(Ellipse(xy=_M2d_XY, width=_M2d_W, height=_M2d_H,
                          facecolor='none', edgecolor=EDGE_COLOR,
                          linewidth=1.2, zorder=4))

plt.tight_layout()
plt.show()
```

3. $D = (D \cap M) \cup (D \cap \overline{M})$

El diagrama siguiente resalta $D \cap M$ (la parte de $D$ que se solapa
con $M$) con un tipo de rayado, y $D \cap \overline{M}$ (la parte de $D$
exterior a $M$) con otro. Juntos, estos dos conjuntos cubren exactamente $D$.

```{code-cell} python
:tags: [hide-input]

_M2_XY = (5.0, 3.7); _M2_W, _M2_H = 5.5, 4.8
_D2_XY = (7.8, 4.0); _D2_W, _D2_H = 4.5, 3.8

fig, ax = plt.subplots(figsize=(3.2, 2.4), facecolor=BG_COLOR)
_ex_setup_ax(ax)
ax.text(2.5, 6.3, r'$M$', fontsize=MATH_SIZE, va='top')
ax.text(9.3, 6.1, r'$D$', fontsize=MATH_SIZE, va='top')

ax.add_patch(Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                     facecolor=FILL_COLOR, edgecolor=EDGE_COLOR,
                     hatch='///', linewidth=0, zorder=1))
ax.add_patch(Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                     facecolor=BG_COLOR, edgecolor='none',
                     linewidth=0, zorder=2))
_clip_D = Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                  facecolor='none', edgecolor='none')
ax.add_patch(_clip_D)
_inter_fill = Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                      facecolor=FILL_COLOR, edgecolor='none', zorder=3)
ax.add_patch(_inter_fill)
_inter_fill.set_clip_path(_clip_D)
_inter_hatch = Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                       facecolor='none', edgecolor=EDGE_COLOR, hatch=3*'\\', zorder=4)
ax.add_patch(_inter_hatch)
_inter_hatch.set_clip_path(_clip_D)

for xy, w, h in [(_M2_XY, _M2_W, _M2_H), (_D2_XY, _D2_W, _D2_H)]:
    ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                          facecolor='none', edgecolor=EDGE_COLOR,
                          linewidth=1.2, zorder=4))
plt.tight_layout()
plt.show()
```

4. $M \cup D = M \cup (\overline{M} \cap D)$

En el diagrama siguiente, un tipo de rayado resalta $\overline{M} \cap D$,
que contiene todos los puntos en $D$ pero no en $M$. Este último se muestra
con un rayado diferente, y considerando todas las áreas que llevan uno u
otro rayado se obtiene exactamente $M \cup D$.

```{code-cell} python
:tags: [hide-input]

_M2_XY = (5.0, 3.7); _M2_W, _M2_H = 5.5, 4.8
_D2_XY = (7.8, 4.0); _D2_W, _D2_H = 4.5, 3.8

fig, ax = plt.subplots(figsize=(3.2, 2.4), facecolor=BG_COLOR)
_ex_setup_ax(ax)
ax.text(2.5, 6.3, r'$M$', fontsize=MATH_SIZE, va='top')
ax.text(9.3, 6.1, r'$D$', fontsize=MATH_SIZE, va='top')

ax.add_patch(Ellipse(xy=_D2_XY, width=_D2_W, height=_D2_H,
                     facecolor=HIGHLIGHT, edgecolor=EDGE_COLOR,
                     hatch=3*'\\', linewidth=0, zorder=1))
ax.add_patch(Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                     facecolor=HIGHLIGHT, edgecolor='none',
                     linewidth=0, zorder=2))
ax.add_patch(Ellipse(xy=_M2_XY, width=_M2_W, height=_M2_H,
                     facecolor='none', edgecolor=EDGE_COLOR,
                     hatch='///', linewidth=0, zorder=3))

for xy, w, h in [(_M2_XY, _M2_W, _M2_H), (_D2_XY, _D2_W, _D2_H)]:
    ax.add_patch(Ellipse(xy=xy, width=w, height=h,
                          facecolor='none', edgecolor=EDGE_COLOR,
                          linewidth=1.2, zorder=4))
plt.tight_layout()
plt.show()
```
````

````{exercise}
:label: ex-es-particion

Considere el universo $\Omega$ y los conjuntos $A$, $B$ y $C$ definidos en
el {ref}`ex-es-conjuntos-base`.

1. Determine si cada una de las siguientes familias es una partición de
   $\Omega$, justificando su respuesta.

   - $\mathcal{F}_1 = \{ A, B, C \}$.
   - $\mathcal{F}_2 = \{ A, \overline A\}$.
   - $\mathcal{F}_3 = \{ A \cap B, A \setminus B, \overline A \}$.
   - $\mathcal{F}_4 = \{ A \cap B, A \ominus B, \overline{A \cup B} \}$.
   - $\mathcal{F}_5 = \{ C, B \setminus C, \overline C \}$.

2. Encuentre una partición de $\Omega$ en cuatro bloques tal que uno de
   los bloques sea $\{\text{Wolverine}, \text{Deadpool}\}$.

3. Determine todas las particiones de $\Omega$ que contienen $A \ominus B$.
````

````{solution} ex-es-particion
:class: dropdown

Recordando los conjuntos del {ref}`ex-es-conjuntos-base`:

```{math}
\begin{align*}
A &= \{\text{Batman}, \text{Thor}, \text{Deadpool}, \text{Cyborg}\},\\
B &= \{\text{Superman}, \text{Thor}, \text{Storm}, \text{Wolverine}\},\\
C &= \{\text{Batman}, \text{Deadpool}, \text{Cyborg}\}.
\end{align*}
```

1. Consideramos los cinco casos por separado.

   - $\mathcal{F}_1 = \{ A, B, C \}$ no es una partición de $\Omega$, ya
     que $A$ y $B$ no son disjuntos (ambos contienen a Thor), ni tampoco
     lo son $A$ y $C$ (que ambos contienen a Batman, Deadpool y Cyborg).
   - $\mathcal{F}_2 = \{ A, \overline A \}$ es una partición de $\Omega$,
     para cualquier $A \subseteq \Omega$ no vacío: $A$ y $\overline A$ son
     disjuntos y su unión es $\Omega$.
   - $\mathcal{F}_3 = \{ A \cap B, A \setminus B, \overline A \}$ es una
     partición de $\Omega$, formada por los tres bloques $\{ \text{Thor} \}$,
     $\{ \text{Batman}, \text{Deadpool}, \text{Cyborg} \}$ y
     $\{ \text{Superman}, \text{Wolverine}, \text{Storm} \}$, que son dos
     a dos disjuntos y cuya unión es $\Omega$. Nótese que esto refleja la
     descomposición $\Omega = (A \cap B) \cup (A \setminus B) \cup \overline A$,
     válida para cualquier par de conjuntos $A, B$.
   - $\mathcal{F}_4 = \{ A \cap B, A \ominus B, \overline{A \cup B} \}$
     no es una partición de $\Omega$: como $A \cup B = \Omega$, se tiene
     $\overline{A \cup B} = \varnothing$, que es un bloque vacío, lo que
     viola la definición de partición.
   - $\mathcal{F}_5 = \{ C, B \setminus C, \overline C \}$ no es una
     partición de $\Omega$, ya que $B \setminus C$ y $\overline C$ no son
     disjuntos (ambos contienen a Thor).

2. Una posible partición en cuatro bloques que contiene
   $\{\text{Wolverine}, \text{Deadpool}\}$ como uno de los bloques es:

```{math}
\bigl\{
\{\text{Wolverine}, \text{Deadpool}\},\;
\{\text{Batman}, \text{Cyborg}\},\;
\{\text{Superman}, \text{Storm}\},\;
\{\text{Thor}\}
\bigr\}.
```

3. $A \ominus B = \{ \text{Batman}, \text{Deadpool}, \text{Cyborg},
   \text{Superman}, \text{Storm}, \text{Wolverine} \} = \Omega \setminus
   \{ \text{Thor} \}$, por lo que la única partición posible es

```{math}
\bigl\{ A \ominus B, \{\text{Thor}\} \bigr\}.
```
````
