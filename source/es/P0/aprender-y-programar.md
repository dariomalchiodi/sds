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

(sec_aprender-y-programar)=
# Aprender <span class="ast">\*</span>y<span class="ast">\*</span> programar

Como se describió en el párrafo anterior, introduciré los conceptos
acompañándolos (o precediéndolos) con ejemplos. Cuando sea posible, también
mostraré algunas _implementaciones_ utilizando un lenguaje relativamente
moderno: en particular, haré referencia a Python y al correspondiente _data
science stack_, compuesto por los paquetes que, al momento de escribir esto,
son ampliamente utilizados por la comunidad _open source_ dedicada al análisis
de datos[^librerías]. Por lo tanto, se recomienda encarecidamente tener una
competencia básica en programación de ordenadores.
```{margin}
Este libro representa la evolución de una serie de apuntes pensados para
estudiantes de segundo año de grados en informática, por lo que haré referencia
al nivel de conocimientos de programación que se adquiere en el primer año de
esos mismos grados, o en grados de áreas afines.
```

El {ref}`chap_intro-python` contiene una descripción de nivel medio-alto de las
funcionalidades de Python que se utilizan, y puede servir para ponerse al día a
quienes ya saben programar pero no conocen este lenguaje. De todos modos, se
recomienda la lectura de este capítulo a todo el mundo, para familiarizarse con
las convenciones que utilizo al escribir código.

Este libro está escrito utilizando una tecnología que permite insertar
contenidos generados mediante la ejecución de código Python. Este código se
muestra explícitamente en todos los casos en los que se guía al lector en la
implementación de uno o más conceptos explicados en el texto, mientras que se
oculta cuando sirve, por ejemplo, para generar tablas o gráficos; aunque en
estos casos siempre hay un link «Mostrar código» que permite
visualizarlo[^hidden-code]. Animo a todos a aprovechar esta oportunidad: así
como no es muy útil leer un texto de forma pasiva, tampoco tiene mucho sentido
ejecutar código de forma mecánica; al contrario, es importante analizarlo,
comprenderlo, modificarlo (¡también valen las modificaciones que ayudan a
entender mejor cómo funciona!)&mdash;en resumen, _jugar_ con él con una
mentalidad _hacker_, en el sentido original del término[^hacker]. De hecho,
también es posible jugar con el libro sin necesidad de comprender o ejecutar el
código: como se muestra en el {ref}`sec_uno-sguardo-di-insieme`, una parte de
los contenidos es interactiva, y su manipulación está pensada precisamente para
facilitar la comprensión de los conceptos introducidos.
```{margin}
Las partes interactivas están basadas en PyScript, una tecnología que permite
ejecutar código Python dentro de navegadores web relativamente modernos. No se
requiere ninguna instalación o configuración por parte del usuario, siempre que
se disponga de una conexión a internet activa y un navegador web compatible (se
admiten todas las versiones recientes de navegadores basados en WebAssembly,
como Chrome, Firefox, Edge, Safari y todos los basados en Chromium).
```

Muy a menudo intento guiar al lector en una implementación real de las
herramientas fundamentales, especialmente en la primera parte, dedicada a la
estadística descriptiva. El resultado al que llego no debe considerarse al 
nivel de las bibliotecas profesionales: por un lado, el objetivo es centrarse
en los aspectos fundamentales para facilitar el aprendizaje de uno o más
conceptos. Por otro lado, estas implementaciones no están pensadas para ser
utilizadas en entornos profesionales: del mismo modo que es razonable que un
desarrollador haya aprendido a escribir desde cero los principales algoritmos
de ordenamiento (y, si fuera necesario, sea capaz de hacerlo), pero que luego
recurra a sus implementaciones en una biblioteca, optimizadas y validadas mucho
mejor de lo que una sola persona podría hacer razonablemente por su cuenta. En
esta línea, justo después de las implementaciones «hazlo tú mismo», se orienta
al lector hacia el uso de bibliotecas de última generación.

En principio, incluso quien no sabe programar puede leer este libro,
simplemente saltándose las partes que contienen, describen o discuten código.
Pero en ese caso conviene evaluar bien el riesgo de no asimilar los contenidos
de forma óptima, teniendo en cuenta que buena parte del libro está escrita
alternando texto y código. A este tipo de lectores les recomiendo considerar
textos escritos con un enfoque más tradicional, como por ejemplo:

- Probabilidad y estadística para las ciencias y la ingeniería, de Sheldon Ross
  {cite:p}`ross`,
- Introducción a la estadística, de Marylin K. Pelosi, Theresa M. Sandifer,
  Paola Cerchiello y Paolo Giudici {cite:p}`pelosi`.

También hay que advertir a quien no sabe programar y se siente tentado de leer
este libro para aprender a hacerlo, quizás mientras aprende a analizar datos al
mismo tiempo. Este __no es__ un libro para aprender a programar, sino más bien
un libro para _aprender programando_, usando la capacidad de escribir código
para enriquecer el proceso de aprendizaje de otra materia. Se dice que uno no
ha entendido realmente algo si no es capaz de explicárselo a su
abuela[^cite-granny]: hago mía esta máxima, esperando no distorsionarla
demasiado al decir que uno no ha entendido realmente un concepto técnico si no
es capaz de implementarlo escribiendo un programa. Pero si se quiere seguir
esta filosofía, hay que haber aprendido ya a escribir software, y esa es una
competencia que requiere tiempo, energía y material específico para su
aprendizaje. También en este caso, hay muchos libros que pueden utilizarse con
provecho, por ejemplo:

```{margin}
Me habría gustado añadir también un libro introductorio a la programación
basado en Go, como en las otras versiones de este libro. Sin embargo, no he
conseguido encontrar ningún recurso que me convenciera. Se agradecen propuestas
en ese sentido.
```
- [Think Python](https://github.com/espinoza/ThinkPython2-spanish), de Allen B.
  Downey.
- Introducción a la programación en C, de y Diego Rodriguez-Losada Gozález,
  Javier Muñoz Cano y Cecilia García Cena {cite:p}`rodriguez`.

He incluido deliberadamente en la lista anterior dos volúmenes más o menos
recientes, y sobre todo cada uno dedicado a un lenguaje diferente: el objetivo,
en este caso, es aprender los fundamentos de la programación y no los detalles
de un lenguaje específico. Por último, este párrafo se refiere únicamente a
libros escritos en español, pero siempre hay que considerar la posibilidad de
estudiar en la versión original de un libro cuando esta está escrita en inglés,
o cuando existe una versión en inglés específicamente concebida para
estudiantes cuya lengua materna no es el inglés.

````{margin}
```{figure} ../_static/img/whistle.jpg
---
name: fig-whistle
height: 100px
---
Un silbato Cap’n Crunch Bo’sun (imagen del Heinz Nixdorf MuseumsForum, distribuida bajo licencia CC BY-NC-SA 4.0)
```
````


[^librerías]: El [repositorio](https://github.com/dariomalchiodi/sds) asociado
a este libro contiene un archivo que enumera todas las bibliotecas utilizadas
para generar los contenidos, incluidas las necesarias para ejecutar el código.

[^hidden-code]: Es importante tener en cuenta que el código oculto puede
contener detalles técnicos relacionados con la generación de contenido
destinado a ser incluido en páginas web (como elementos HTML o estilos CSS).
Por lo tanto, no está escrito de la misma manera en que se escribiría código
para el análisis de datos en entornos de trabajo tradicionales: su estructura
responde a necesidades de presentación e interactividad, más que a necesidades
analíticas.

[^hacker]: El término _hacker_ se utiliza hoy en día en el lenguaje común con
una connotación negativa, que lo asocia esencialmente a quienes persiguen fines
maliciosos escribiendo o modificando software, o en general explotando
vulnerabilidades de seguridad para hacer un uso indebido de tecnologías
informáticas existentes. En realidad, el uso moderno de este término en inglés
se remonta aproximadamente a 1960, con una connotación más neutra y no
necesariamente vinculada a la informática: la de describir a una persona con el
talento de comprender en profundidad el funcionamiento de un sistema, y por
tanto capaz de controlarlo hasta el punto de utilizarlo de forma distinta a la
prevista por su diseño original. Por citar un ejemplo, uno de los primeros
_hacks_ famosos&mdash;aunque ilegal&mdash;consistía en usar el «Cap’n Crunch
Bo’sun Whistle» (un silbato que venía de regalo en las cajas de una conocida
marca de cereales, mostrado en {numref}`fig-whistle`) para realizar llamadas de
larga distancia o internacionales gratuitas desde algunos teléfonos públicos en
los Estados Unidos. Uno de los entornos donde comenzó a desarrollarse la
contracultura _hacker_ fue el Massachusetts Institute of Technology (MIT): el
primer rastro escrito del término «hacking» aparece en el acta de una reunión
de 1955 del [Tech Model Railroad Club](http://tmrc.mit.edu/), un club de
estudiantes apasionados por el modelismo ferroviario. Solo más recientemente se
ha producido una identificación directa con el mundo informático.

[^cite-granny]: Es difícil rastrear con certeza el autor de esta máxima: hay
quien la atribuye a Einstein, otros a Feynman y otros a Rutherford (parece
haber consenso, al menos, en el contexto de las ciencias físicas); también
existen variantes en las que la abuela es sustituida por un niño o
incluso&mdah;por algún motivo&mdash;por un camarero.

