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

(sec_convenciones)=
# Convenciones y notación

Como se mencionó en el párrafo anterior, a menudo intercalaré el texto con
código, no tanto con el objetivo de ejecutarlo, sino más bien con fines
ilustrativos (por ejemplo, para indicar los literales `true` y `false` como los
únicos valores posibles para el tipo de dato `bool`). En este caso, utilizaré
una fuente monoespaciada con un color distinto al del texto principal. En
cambio, cuando sea necesario mostrar una o más líneas de código pensadas para
ser ejecutadas por quien lee, presentaré dichas líneas dentro de un recuadro
que recuerda a la típica _celda de código_ de un _notebook_. También en este
caso usaré una fuente monoespaciada, pero la coloración del texto destacará
ciertos elementos del código (como variables, literales, palabras clave, etc.,
de forma similar a lo que hacen los IDE modernos). Además, el código aparecerá
separado del texto principal. Por último, el posible resultado de la ejecución
aparecerá dentro de una _celda de salida_ dedicada, colocada justo después de
la celda de código, como se muestra a continuación, de modo que la conexión
entre instrucciones y resultados sea clara.

```{margin}
Es práctica común utilizar una fuente monoespaciada (en la que todos los glifos
usados para representar una letra tienen el mismo ancho) para visualizar
código, entradas y salidas, por una serie de razones que optimizan la
legibilidad del propio código, como la mayor facilidad para indentar
instrucciones o el menor riesgo de confundir caracteres similares como 1 y l.
```

```{code-cell}
age = 24
print(age <= 42)
```

Por último, utilizaré un estilo específico para resaltar en el texto ciertos
elementos particulares, como se ejemplifica a continuación.

```{admonition} _
:class: naming
Este tipo de área contiene notas relativas a la nomenclatura utilizada
en un ámbito particular, o a la descripción de términos alternativos respecto
a los introducidos.
```

```{prf:definition}
:label: segnaposto-definicion
:class: no-number
En esta área se definen formalmente uno o más conceptos.
```
```{margin}
Definiciones, ejemplos, etc., estarán normalmente numerados, y a menudo
acompañados por un nombre específico entre paréntesis.
```

```{prf:example}
:label: segnaposto-ejemplo
:class: no-number
Esta área contiene un ejemplo.
```

````{prf:theorem}
:label: segnaposto-teorema
:class: no-number
Esta área contiene el enunciado de un teorema.
````

```{prf:corollary}
:label: segnaposto-corolario
:class: no-number
Esta área contiene el enunciado de un corolario.
```

```{prf:lemma}
:class: no-number
:label: segnaposto-lemma
Esta área contiene el enunciado de un lema.
```

```{admonition} _
:class: myproof
En esta área se incluye la demostración de un teorema, corolario o lema. En
algunos casos omitiré las demostraciones, limitándome a escribir el enunciado.
Esto ocurrirá cuando sea importante introducir un resultado teórico relevante,
aunque su demostración requiera conocimientos matemáticos avanzados.
```

```{note}
Este tipo de área recoge algunos aspectos secundarios que prefiero destacar en
el texto, en lugar de describirlos en notas al pie.
```

(sec_notacion)=
Finalmente, la {numref}`tab-notacion` recoge las principales notaciones que
utilizaré en las fórmulas matemáticas.

```{table} Notación utilizada en el texto para las fórmulas matemáticas.
:name: tab-notacion
:align: center
:class: [full-width]

| Símbolo                   | Significado                                                                     |
|:--------------------------|:--------------------------------------------------------------------------------|
| $\mathbb N$               | conjunto de los números naturales                                               |
| $\mathbb Z$               | conjunto de los números enteros                                                 |
| $[a..b]$                  | intervalo discreto de números enteros entre $a$ y $b$ (extremos incluidos)      |
| $\mathbb R$               | conjunto de los números reales                                                  |
| $[a, b]$                  | intervalo cerrado de números reales entre $a$ y $b$                             |
| $(a, b)$                  | intervalo abierto de números reales entre $a$ y $b$                             |
| $[a, b)$, $(a, b]$        | intervalos semiabiertos de números reales entre $a$ y $b$                       |
| $A = \\{ a_1, \dots a_n \\}$| conjunto/suceso compuesto por los elementos/resultados $a_1, \dots, a_n$        |
| $a \in A$                 | elemento $a$ del conjunto $A$                                                   |
| $(a_1, \dots, a_n)$       | disposición o permutación compuesta por los elementos $a_1, \dots, a_n$         |
| $n!$                      | factorial del número entero $n$                                                 |
| $\binom{n}{k}$            | coeficiente binomial («$n$ sobre $k$») de $n$ objetos en $k$ posiciones         |
| $p_n$                     | número de permutaciones simples de $n$ elementos                                |
| $P_{n; n_1, \dots, n_k}$  | número de permutaciones con repetición de $n$ elementos distinguibles en grupos de $n_1, \dots, n_k$ objetos |
| $\\{ a_1, \dots, a_n \\}$   | combinación compuesta por los elementos $a_1, \dots, a_n$                        |
| $D_{n, k}$                | disposiciones con repetición de $n$ objetos en $k$ posiciones                   |
| $d_{n, k}$                | disposiciones sin repetición de $n$ objetos en $k$ posiciones                   |
| $c_{n, k}$                | combinaciones simples de $n$ objetos en $k$ posiciones                          |
| $C_{n, k}$                | combinaciones con repetición de $n$ objetos en $k$ posiciones                   |
| $S \subseteq T$           | subconjunto/subsuceso $S$ de un conjunto/suceso $T$                             |
| $\Omega$                  | conjunto universo / espacio muestral / suceso seguro                            |
| $\varnothing$             | conjunto vacío / suceso imposible                                               |
| $A \rightarrow B$         | suceso/proposición $A$ implica suceso/proposición $B$                           |
| $A \leftrightarrow B$     | suceso/proposición $A$ coimplica suceso/proposición $B$                         |
| $S \cup T$                | unión de los conjuntos/sucesos $S$ y $T$                                        |
| $S \cap T$                | intersección de los conjuntos/sucesos $S$ y $T$                                 |
| $S \backslash T$          | diferencia entre el conjunto/suceso $S$ y el conjunto/suceso $T$                |
| $S \Delta T$              | diferencia simétrica entre los conjuntos/sucesos $S$ y $T$                      |
| $A \vee B$                | disyunción lógica entre las proposiciones $A$ y $B$                             |
| $A \wedge B$              | conjunción lógica entre las proposiciones $A$ y $B$                             |
| $\mathscr E$              | experimento aleatorio                                                           |
| $\omega \in \Omega$       | resultado de un experimento aleatorio                                           |
| $\\{ \omega \\}$            | suceso elemental                                                                |
| $\mathsf A$               | álgebra de sucesos                                                              |
| $2^A$                     | conjunto potencia del conjunto $A$                                              |
| $\mathcal P$              | partición de un conjunto                                                        |
| $\mathbb P$               | función de probabilidad                                                         |
| $\mathbb P(E)$            | probabilidad del suceso $E$                                                     |
| $\mathbb P(E\|F)$         | probabilidad condicional del suceso $E$ dado el suceso $F$                      |
| $\mathbb E(X)$            | valor esperado de la variable aleatoria $X$                                     |
| $\mathbb E(g(X))$         | valor esperado de la función $g$ de la variable aleatoria $X$                   |
| $\mathbb E(g(X, Y))$      | valor esperado de la función $g$ de las variables aleatorias $X$ y $Y$          |
| $a \triangleq b$          | $a$ se define como igual a $b$                                                  |
```
