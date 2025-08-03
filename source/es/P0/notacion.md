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

(sec:notacion)=
# Notación

La {numref}`tab-notacion` recoge las principales notaciones que utilizaré en
las fórmulas matemáticas.

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
| $\Omega$                  | conjunto universo / espacio muestral                                            |
| $A \rightarrow B$         | suceso/proposición $A$ implica suceso/proposición $B$                           |
| $A \leftrightarrow B$     | suceso/proposición $A$ coimplica suceso/proposición $B$                         |
| $S \cup T$                | unión de los conjuntos/sucesos $S$ y $T$                                        |
| $S \cap T$                | intersección de los conjuntos/sucesos $S$ y $T$                                 |
| $S \backslash T$          | diferencia entre el conjunto/suceso $S$ y el conjunto/suceso $T$                |
| $S \ominus T$             | diferencia simétrica entre los conjuntos/sucesos $S$ y $T$                      |
| $A \vee B$                | disyunción lógica entre las proposiciones $A$ y $B$                             |
| $A \wedge B$              | conjunción lógica entre las proposiciones $A$ y $B$                             |
| $\mathscr E$              | experimento aleatorio                                                           |
| $\omega \in \Omega$       | resultado de un experimento aleatorio                                           |
| $\\{ \omega \\}$            | suceso elemental                                                                |
| $\mathsf A$               | álgebra de sucesos                                                              |
| $2^A$                     | conjunto potencia del conjunto $A$                                         |
| $\mathbb P$               | función de probabilidad                                                         |
| $\mathbb P(E)$            | probabilidad del suceso $E$                                                     |
| $\mathbb P(E\|F)$         | probabilidad condicional del suceso $E$ dado el suceso $F$                      |
| $\mathbb E(X)$            | valor esperado de la variable aleatoria $X$                                     |
| $\mathbb E(g(X))$         | valor esperado de la función $g$ de la variable aleatoria $X$                   |
| $\mathbb E(g(X, Y))$      | valor esperado de la función $g$ de las variables aleatorias $X$ y $Y$          |
| $a \triangleq b$          | $a$ se define como igual a $b$                                                  |
```

