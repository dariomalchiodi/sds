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

(par:franklin-law)=
# Introducción

> En este mundo, nada puede darse por cierto,<br/>
> excepto la muerte y los impuestos
>
> -- Benjamin Franklin

La cita que inicia este párrafo está traducida de una carta escrita en 1789 por
Benjamin Franklin (ver {numref}`benjamin-franklin`), uno de los padres
fundadores de los Estados Unidos de América. Si aceptamos este dicho, a menudo
referido como la _ley de Franklin_ [^cita-franklin], vale la pena estudiar la
incertidumbre, porque prácticamente todo es incierto (irónicamente, la validez
de la propia ley de Franklin no debe darse por sentada: basta pensar, por
ejemplo, en el fenómeno de la evasión fiscal, o en el hecho de que quienes
residen en el Principado de Mónaco no pagan impuestos).

```{figure} https://live.staticflickr.com/2869/9544834557_b844c48e78_b.jpg
:width: 70%
:name: benjamin-franklin

Representación de Benjamin Franklin en los billetes de 100 dólares
estadounidenses (imagen de E. Strauhmanis, distribuida bajo
[CC BY 2.0](https://creativecommons.org/licenses/by/2.0/))
```

En realidad, el concepto de _incertidumbre_ es particularmente difícil de
definir, porque es muy multifacético y adopta diferentes matices según el
contexto. En este libro, nos centraremos en una encarnación particular de este
concepto, a la que llamaremos _aleatoriedad_. En términos simples (y por tanto,
definitivamente mejorables), podemos identificar la aleatoriedad como la
propiedad que caracteriza a cualquier experiencia que, incluso si se repite
bajo las mismas condiciones, no tiene un resultado determinable a priori. De
manera (por ahora) informal, llamamos _eventos_ a las afirmaciones que se
refieren a los resultados de estas experiencias. Por lo tanto, el valor de
verdad de estas afirmaciones será incierto. Un ejemplo clásico de evento es el
resultado de lanzar dados cuando se juega al Monopoly. Otro ejemplo igualmente
clásico, pero más moderno, se refiere al valor de cierre de un índice bursátil.
Si reflexionamos más atentamente, nos vienen a la mente muchos otros ejemplos:
si miramos al cielo por la mañana y vemos nubes en el horizonte, ¿lloverá hoy?
¿Cuántos nietos tendrá la hermana de mi vecino? ¿El próximo año podré pasar la
temporada fría contagiándome la gripe como máximo una vez? De hecho, no es
difícil convencernos de que la aleatoriedad (o, si prefieres, el no
determinismo) impregna nuestra existencia, hasta el punto de jugar un papel
fundamental en la descripción de algunos aspectos fundamentales de la
Naturaleza, como la teoría de la evolución o la mecánica cuántica.

A pesar de ello, las personas aprenden más o menos rápido a convivir bastante
bien con la incertidumbre: al salir de casa, la mayoría de las veces sabemos
cuándo es prudente llevar un paraguas con nosotros, y algunas personas incluso
logran especular con éxito en el mercado bursátil. Esto sucede porque somos
capaces de _evaluar_ la incertidumbre de muchos eventos, aceptando el _riesgo_
que conlleva nuestra evaluación (volviendo al ejemplo del cielo nublado, el
riesgo es llevar un paraguas innecesariamente o no llevarlo y terminar bajo la
lluvia). Casi siempre, hacemos todo esto de manera mayormente subjetiva,
basándonos en nuestra _experiencia_. Sin embargo, las matemáticas nos
proporcionan herramientas cualitativas y cuantitativas para abordar este
problema rigurosamente. En particular, combinando el _cálculo de
probabilidades_ y la _estadística_, podemos modelar la incertidumbre de los
eventos y evaluarla usando la experiencia que hemos adquirido.

El propósito de este libro es precisamente proporcionar las bases de estas dos
ramas de las matemáticas, usando un enfoque interactivo centrado en el análisis
de datos, adecuado especialmente para estudiantes que ya hayan desarrollado
habilidades en programación informática. En particular, el contenido ha sido
diseñado para estudiantes matriculados en programas de grado en informática,
pero sin duda es adecuado para todos los contextos educativos que incluyen al
menos un curso obligatorio de programación.

El trabajo está organizado en cuatro partes:

- La primera introduce el lenguaje de programación Python y las principales
  bibliotecas actualmente utilizadas para analizar datos (el llamado _Python
  data science stack_);
- La segunda aborda el tema de la _estadística descriptiva_, que podemos
  relacionar informalmente con el problema de organizar observaciones de un
  fenómeno y luego analizarlas para extraer _información_ (la base de la
  experiencia mencionada anteriormente);
- La tercera introduce los fundamentos de la _teoría de la probabilidad_,
  entendida como una disciplina que permite la evaluación cuantitativa de la
  incertidumbre de los eventos;
- La cuarta finalmente se centra en los fundamentos de la _estadística
  inferencial_, con el fin de proporcionar herramientas que permitan la toma de
  decisiones bajo incertidumbre, utilizando las herramientas introducidas en
  los capítulos anteriores.

Cada una de estas partes, considerada por sí sola, llenaría un libro de texto
completo—¡posiblemente más de uno! Por lo tanto, aunque el material puede
usarse sin recurrir a fuentes externas, el libro a menudo solo permite abordar
los conceptos fundamentales de las disciplinas consideradas. No obstante, donde
es posible, se describen brevemente algunas herramientas avanzadas típicas del
_aprendizaje automático_, que se basan en la aplicación de conceptos y
herramientas presentados en el libro.

[^cita-franklin]: En la fuente original (una carta de B. Franklin al
físico francés Jean-Baptiste Le Roy), esta afirmación aparece en realidad como
parte final de la frase: «... in this world nothing can be said to be certain,
except death and taxes». No obstante, cabe destacar que, aunque la autoría de
este dicho suele atribuirse a Benjamin Franklin, existen
[fuentes anteriores](https://es.wikipedia.org/wiki/Death_and_taxes) que recogen
algunas variantes.
