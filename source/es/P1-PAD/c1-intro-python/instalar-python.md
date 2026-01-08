---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
nb_execution: false
---

(sec_instalacion)=
# Instalación, configuración y primeros pasos

Esta sección explica cómo instalar Python y las bibliotecas a las que haré
referencia a lo largo del libro, y presenta también algunas buenas prácticas
que vale la pena adoptar desde el inicio de cualquier proyecto de software para
el análisis de datos&mdash;como el uso de entornos virtuales y gestores de
bibliotecas. Si ya estás familiarizado con Python y cuentas con una instalación
funcional, probablemente puedas saltar a la siguiente sección. Sin embargo, te
recomiendo una lectura rápida para alinearte con la terminología que usaré y
para asegurarte de que no haya problemas de compatibilidad con la versión que
tienes instalada y de que todas las bibliotecas necesarias estén disponibles.

(sec_lenguajes-versiones-implementaciones)=
## Lenguajes, versiones e implementaciones

Los lenguajes de programación evolucionan con el tiempo, a medida que se
actualizan sus especificaciones. Estos cambios dan lugar a una secuencia de
_versiones_ del lenguaje. Hoy en día, la forma más difundida de identificar una
versión específica de un lenguaje de programación (pero también de una
biblioteca o de cualquier producto software) es el esquema llamado
[versionado semántico](https://semver.org/lang/es), que, en su forma más
simple, describe una versión usando el formato `X.Y.Z`, una secuencia de tres
enteros que se inicializan en cero y se incrementan con cada actualización:

- `X` indica una _versión mayor_ y se incrementa cuando se introducen cambios
  incompatibles,
- `Y` es la _versión menor_, que se incrementa cuando se agregan
  características compatibles hacia atrás,
- `Z` representa el _número de parche_, asociado a correcciones y pequeños
   cambios.

En general, a menos que se necesite una especificación inusualmente precisa,
basta con referirse a una versión específica de Python usando solo el número
mayor y menor. Por ejemplo, aunque el código de este libro fue escrito usando
la versión 3.11.11 de Python, me referiré simplemente a la versión 3.11, ya que
el código se puede ejecutar independientemente del número de parche específico.
Además, usar versiones menores más recientes no debería causar problemas,
mientras que usar versiones mucho más antiguas no es recomendable.

Podría parecer que conocer la versión exacta de un lenguaje de programación sea
suficiente para determinar todas sus características, pero no es del todo así.
Definir un lenguaje implica especificar su _sintaxis_ y su _semántica_, pero
construir las herramientas para ejecutar los programas
correspondientes&mdash;intérpretes y compiladores[^compilers]&mdash;es otro
asunto. Estas herramientas pueden ser desarrolladas por personas distintas, en
momentos distintos y con tecnologías diferentes. Como resultado, existen
distintas _implementaciones_ de un lenguaje que pueden diferir entre sí incluso
si cumplen con la misma versión, ya que las especificaciones no dictan
completamente _cómo_ se deben implementar ciertas características. Por ejemplo,
los formatos de codificación de cadenas pueden variar entre implementaciones.
En el caso de Python, existen
[varias implementaciones](https://www.toptal.com/python/why-are-there-so-many-pythons),
cada una con una tecnología subyacente distinta: una se basa en la máquina
virtual Java, otra en un entorno en C, otra se ejecuta en navegadores web, etc.
La implementación más común, que suele instalarse por defecto, se llama
_CPython_ y, como su nombre indica, está escrita en C.

(sec_download-book)=
## Descargar el contenido del libro

Este libro está diseñado para ser usado a través de un servidor web. La ventaja
es que se puede acceder a los componentes interactivos sin necesidad de
instalar ni configurar bibliotecas, pero esto requiere una conexión a internet
continua. Alternativamente, se puede descargar el contenido del libro y generar
sus capítulos como páginas web servidas desde un servidor local, pero esto
implica instalar previamente todo el software necesario para este proceso.
Ten en cuenta que ejecutar componentes interactivos aún requiere conexión a
internet.

```{margin}
Para clonar el repositorio del libro necesitas tener instalado un _cliente_ de
git, una cuenta de GitHub y una clave SSH pública asociada. Alternativamente,
también es posible clonar vía HTTPS, lo cual simplifica algunos pasos (como la
clave SSH) pero complica otros.
```

La forma recomendada de descargar el libro es mediante
[git](https://git-scm.com), un sistema de control de versiones usado para
gestionar código fuente en proyectos de software. Para ello, abre una terminal,
navega hasta una ubicación deseada en tu sistema de archivos y ejecuta el
siguiente comando para clonar localmente el
[repositorio](https://github.com/dariomalchiodi/sds) del libro en un nuevo
directorio llamado `sds`:

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      En todos los ejemplos siguientes, el símbolo ``$`` indica el prompt del
      intérprete de comandos. Dependiendo de la configuración de tu sistema, el
      prompt puede verse diferente. En el ejemplo, ``my_parent_dir`` es un
      marcador de posición para la ruta donde deseas guardar el directorio del
      libro.

      .. code-block:: bash

         $ cd my_parent_dir
         $ git clone git@github.com:dariomalchiodi/sds.git
         $ cd sds

      Asumiré que esta sesión de shell permanece abierta durante el resto
      de esta sección.

   .. group-tab_: Windows

      En los ejemplos siguientes, ``C:>`` representa el prompt de PowerShell.
      Dependiendo de la configuración de tu sistema, el prompt puede verse
      diferente. ``my_parent_dir`` es un marcador de posición para la ruta
      donde deseas guardar el directorio del libro.

      .. code-block:: powershell

         C:> cd my_parent_dir
         C:> git clone git@github.com:dariomalchiodi/sds.git
         C:> cd sds

      Asumiré que esta sesión de PowerShell permanece abierta durante el resto
      de esta sección.

```

```{margin}
Se necesita una conexión a internet activa para realizar esta operación.
```

También es posible descargar un archivo ZIP. Sin embargo, usar git permite
mantener el libro actualizado fácilmente, simplemente ejecutando el siguiente
comando:

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         $ git pull

   .. group-tab_: Windows

      .. code-block:: powershell

         C:> git pull

```

desde una terminal, luego de haber navegado al directorio `sds` (o a
cualquiera de sus subdirectorios). Además, git es la herramienta usada para
reportar errores o proponer cambios, mediante el envío de _issues_ o
_pull requests_, como se explica en {ref}`chap_approccio`. Finalmente, aprender
git es algo que recomiendo a cualquiera que estudie no solo informática, sino
cualquier disciplina dentro de la ciencia de datos. De hecho, git se usa en la
gran mayoría de los proyectos de software, así que vale la pena aprenderlo
desde el inicio.

## Instalación de Python

La instalación de Python depende mucho del sistema operativo. Las
distribuciones recientes de Linux y Mac OS ya lo incluyen por defecto, mientras
que en Windows debe instalarse manualmente. Aun así, es posible que tu
computadora ya tenga Python instalado. Para verificarlo, abre una terminal y
ejecuta:

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         $ python --version

   .. group-tab_: Windows

      .. code-block:: powershell

         C:> python --version

```

Pueden darse tres situaciones:

1. El resultado es `Python 3.Y.Z`, lo que indica que tienes instalada la
   versión 3 de Python, donde `Y` y `Z` son el número menor y de parche,
   respectivamente, y `Y` es mayor o igual a $5$;
2. El resultado muestra una versión que comienza con `1` o `2`, o `3` pero con
   un número menor inferior a $5$, lo que significa que Python está presente
   pero es demasiado antiguo para ejecutar el código de este libro. Me
   referiré a la versión 3.11, que está ampliamente difundida al momento de
   escribir estas líneas;
```{margin}
Si el número mayor es `4` o superior, entonces estás leyendo este libro mucho
después de que fue escrito y puede que parte del contenido relacionado con
Python esté desactualizado. Consulta ediciones más recientes o documentación
actualizada.
``` 
3. Obtienes un error indicando que `python` no es un comando reconocido, lo que
   probablemente significa que Python no está instalado.

En el primer caso, probablemente tu instalación actual de Python sea suficiente
para ejecutar el código del libro. Aun así, conviene verificar que la versión
sea lo más cercana posible a la utilizada aquí. Una versión significativamente
diferente podría causar problemas de compatibilidad, en cuyo caso deberías
instalar la versión que se menciona, sin eliminar la existente.
```{margin}
Técnicamente, se puede reemplazar la versión de Python del sistema, pero eso
puede romper otros programas. En general, no recomiendo hacerlo.
```

En el segundo caso, podría existir una versión compatible, pero el comando
`python` apunta a otra. Para comprobarlo, puedes escribir `python` en la
terminal y luego presionar {kbd}`TAB` sin espacio: si hay múltiples versiones
instaladas, se listarán sus comandos. En el tercer caso, Python podría estar
instalado pero no configurado correctamente para usarse desde la
terminal&mdash;aunque esto es poco común.
```{margin}
Normalmente, por cada versión instalada existe un comando correspondiente como
`pythonX.Y`, donde `X` e `Y` son los números mayor y menor de la versión. El
comando `python` es un alias que apunta a una de estas, típicamente la que más
se utiliza en el sistema.
```

Si es necesario instalar Python, consulta la documentación oficial, que incluye
guías para [Unix (como Linux)](https://docs.python.org/3/using/unix.html),
[Mac OS](https://docs.python.org/3/using/mac.html), y
[Windows](https://docs.python.org/3/using/windows.html).

## Creación de un entorno virtual de ejecución

Python se utiliza frecuentemente junto con muchas bibliotecas, y desaconsejo
fuertemente una instalación _monolítica_, donde se agregan bibliotecas una por
una según se van necesitando. Con el tiempo, esto aumenta el riesgo de
incompatibilidades entre tu entorno y las bibliotecas nuevas. También pueden
surgir problemas similares al actualizar bibliotecas. Para evitar estos
inconvenientes, lo mejor es aislar las instalaciones ejecutando Python dentro
de un espacio dedicado que contenga solo las bibliotecas necesarias para un
proyecto específico. Estos espacios, llamados _entornos virtuales_, se activan
al comenzar a trabajar en un proyecto y se desactivan al cambiar a otro.

Existen varias formas de crear entornos virtuales en Linux; este libro utiliza
_venv_[^environment], que viene incluido con versiones recientes de Python.
Para crear un entorno virtual, utiliza la misma sesión de shell de antes,
navega al directorio `sds` y ejecuta:

```{margin}
Nombrar el directorio como `.venv` es una práctica común reconocida por muchos
IDEs. Técnicamente puedes usar cualquier nombre, pero solo hazlo si tienes una
razón específica. La opción `--prompt sds` es opcional y sirve para definir la
etiqueta del prompt; de lo contrario, se usa el nombre del directorio.
```

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         $ python3.11 -m venv .venv --prompt sds

   .. group-tab_: Windows

      .. code-block:: powershell

         C:> python3 -m venv .venv --prompt sds

```

Asegúrate de que `python3.11` (en Linux/Mac OS) o `python3` (en Windows)
apunten a la versión deseada y estén correctamente instalados. Esto creará un
directorio `.venv` (oculto en Linux y Mac OS) con ejecutables y futuras
bibliotecas para este entorno. Para activarlo, ejecuta:

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         $ source .venv/bin/activate

   .. group-tab_: Windows

      .. code-block:: powershell

         C:> .venv\Scripts\activate

```

Este comando debe ejecutarse dentro del directorio `sds` (o usando una ruta
relativa/absoluta al script `activate`). La activación también modifica el
prompt, agregando `(sds)` para señalar que se está usando un entorno virtual.
La siguiente sección explica cómo instalar bibliotecas después de activar el
entorno. Para desactivarlo, ejecuta:

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         (sds) $ deactivate

   .. group-tab_: Windows

      .. code-block:: powershell

         (sds) C:> deactivate

```

Esto restaura el prompt del sistema a su estado original.

(sec_lib-install)=
## Gestión de bibliotecas

En teoría, se puede instalar una biblioteca manualmente descargando su
ejecutable o construyéndola desde el código fuente público. Pero esto puede ser
complicado: la mayoría de las bibliotecas dependen de otras, que a su vez
pueden depender de otras, y así sucesivamente. La instalación manual suele
convertirse en una experiencia larga y frustrante. Cuantas más dependencias se
requieran, mayor es la probabilidad de errores que interrumpan o bloqueen el
proceso. Para evitar esto, lo mejor es usar un _gestor de paquetes_&mdash;una
herramienta que detecta y gestiona automáticamente las dependencias. Esto se
considera una buena práctica en Python y en el desarrollo de software en
general. Al igual que con los entornos virtuales, existen varios
[gestores de paquetes](https://packaging.python.org/en/latest/tutorials/installing-packages/#alternative-packaging-tools)[^package-manager]
para Python. Yo haré referencia a [pip](https://pip.pypa.io), que está incluido
con versiones recientes de Python.

La instalación de bibliotecas, que normalmente se hace dentro de un entorno
virtual activo, se realiza con el comando `pip` desde la terminal, indicando el
nombre del paquete&mdash;opcionalmente seguido de `==versión` para instalar una
versión específica. Por ejemplo, para instalar altair, la biblioteca utilizada
en {ref}`sec_vista-de-conjunto` para generar gráficos interactivos, puedes
ejecutar:

```{margin}
Pronto veremos cómo instalar todas las bibliotecas necesarias de una sola vez,
así que no es necesario ejecutar este comando ahora.
```

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         (sds) $ pip install altair

   .. group-tab_: Windows

      .. code-block:: powershell

         (sds) C:> pip install altair

```

Este comando verifica las dependencias de altair, las instala si no están
presentes, o las actualiza si las versiones no son compatibles, y hace lo mismo
recursivamente con sus dependencias.

Usar gestores de paquetes ofrece otra ventaja: puedes compartir un proyecto
junto con un archivo de texto que liste las bibliotecas necesarias e
instalarlas todas de una vez. Con pip, esta lista normalmente se guarda en un
archivo `requirements.txt`. Para instalar todo lo que allí aparece, ejecuta:

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         (sds) $ pip install -r requirements.txt

   .. group-tab_: Windows

      .. code-block:: powershell

         (sds) C:> pip install -r requirements.txt

```

El [repositorio](https://github.com/dariomalchiodi/sds) de este libro incluye
un archivo `requirements.txt` que enumera todas las bibliotecas necesarias para
ejecutar el código en los distintos capítulos.


(sec_notebook)=
## Instalación de un gestor de notebooks

Como se mencionó al inicio de este capítulo, presentaré código Python de manera
que pueda ejecutarse fácilmente dentro de archivos llamados _notebooks_ (o
_cuadernos computacionales_). El contenido de estos archivos está organizado en
_celdas_, que pueden ser de tres tipos distintos:

- celdas de código, compuestas por una o más líneas de código
  ejecutable[^nb-lang],
- celdas de salida, cada una asociada a una celda de código específica y que
  contiene el resultado producido al ejecutar dicha celda,
- otras celdas, que pueden contener texto con formato, gráficos o videos,
  posiblemente generados como efecto secundario del código ejecutado en el
  notebook, o añadidos manualmente por su autor.

```{margin}
Cuando el nombre de una tecnología basada en Python incluye la sílaba «py»,
normalmente se pronuncia como la palabra inglesa «pie», es decir, 
[ˈpī](https://www.merriam-webster.com/dictionary/pie?pronunciation&lang=en_us&dir=p&file=pie00001).
Jupyter es una excepción, como lo declararon sus creadores[^pronunce-jupyter],
y se pronuncia
[ˈjü-pə-tər](https://www.merriam-webster.com/dictionary/Jupiter?pronunciation&lang=en_us&dir=gg&file=ggjupi01),
igual que el nombre inglés del planeta Júpiter.
```

El estándar _de facto_ para notebooks es el introducido por el proyecto
[Jupyter](https://jupyter.org). Existen 
[muchas aplicaciones](https://mljourney.com/jupyter-notebook-alternatives-in-2025/)
que permiten escribir, leer y sobre todo ejecutar notebooks. Entre ellas, las
más usadas son la distribuida directamente por el proyecto Jupyter y el IDE
principal de Microsoft, [Visual Studio Code](https://code.visualstudio.com).

Si has instalado las bibliotecas usando el archivo `requirements.txt` siguiendo
las instrucciones de las secciones anteriores, entonces Jupyter ya está
disponible dentro del entorno virtual que creaste. Para lanzarlo, simplemente
ejecuta el siguiente comando desde la terminal:

```{margin}
Más adelante también encontrarás instrucciones sobre cómo visualizar y ejecutar un notebook usando Visual Studio Code.
```

```{eval-rst}
.. tabs::

   .. group-tab_: Linux / Mac OS

      .. code-block:: bash

         (sds) $ jupyter notebook

   .. group-tab_: Windows

      .. code-block:: powershell

         (sds) C:> jupyter notebook

```

```{margin}
La extensión .ipynb identifica los notebooks de Python.
```
Esto abrirá automáticamente un navegador conectado a una dirección local, donde
se ha lanzado un servidor web que escucha peticiones. La página cargada
mostrará los archivos contenidos en el directorio desde el cual se lanzó
Jupyter. Por ejemplo, {numref}`jupyter-home` muestra cómo se ve esta página al
iniciar desde el directorio raíz del repositorio de este libro. Al hacer clic
en el directorio _playground_ y seleccionar el único archivo disponible,
_first-notebook.ipynb_, se mostrará un ejemplo simple de notebook. Este
notebook contiene una sola celda de código, en la que ya está presente la
expresión `1 + 1`. Si colocas el cursor dentro de la celda y presionas
{kbd}`Shift` + {kbd}`⤶`, se añadirá automáticamente una celda de salida al
notebook, mostrando el resultado de la expresión. Para crear un nuevo notebook,
puedes seleccionar el ítem de menú _File > New > Notebook_, o volver a la vista
de listado de archivos, hacer clic en el botón «New» y elegir «Python 3
(ipykernel)». Aparecerá una nueva página, con una sola celda de código vacía.
La ventaja de usar un notebook radica en la gran interactividad durante la
ejecución del código, ya que los resultados de una celda permanecen en memoria
mientras el notebook siga abierto: esto te permite reutilizarlos en celdas
posteriores.

```{figure} ../../../_static/img/jupyter-home.png
:width: 100%
:name: jupyter-home

La pantalla de inicio de Jupyter, mostrando la lista de archivos presentes en
el directorio correspondiente al repositorio del libro.
```

Usar un notebook con versiones recientes de Visual Studio Code es aún más
sencillo, siempre que tengas instalada la extensión correspondiente: solo
necesitas abrir el archivo desde el IDE, y sus celdas se mostrarán en una
pestaña. También en este caso, puedes añadir código y ejecutarlo tal como
harías en Jupyter. La única diferencia es que la primera vez que ejecutes una
celda, puede que tengas que seleccionar un entorno desde un menú contextual.

```{admonition} Advertencia
Existe una flexibilidad considerable en cómo puedes evaluar las celdas de
código dentro de un notebook: basta con colocar el cursor en una celda y
presionar {kbd}`Shift` + {kbd}`⤶`, lo que permite ejecutarlas en cualquier
orden&mdash;de la primera a la última, de la última a la primera, siete veces
la primera y luego la tercera, o en el orden que se te ocurra. Esto tiene
ventajas y desventajas. Por un lado, esta flexibilidad puede usarse para
analizar datos de forma muy interactiva, ejecutando pequeñas partes del código
y evaluando los resultados antes de decidir el siguiente paso. Por otro lado,
la imposibilidad de restringir la ejecución a un orden fijo y predefinido
introduce cierto grado de indeterminación en el resultado, lo que limita la
reproducibilidad. Además, aunque los notebooks son esencialmente archivos de
texto, incluyen muchos metadatos que dificultan su gestión mediante
git[^jupytext]. También conviene recordar que los notebooks son solo una de las
muchas herramientas que puedes usar para ejecutar código Python. Entre las
alternativas más comunes, hay dos que están particularmente extendidas. La
primera es el uso del llamado REPL (Read, Evaluate, Print, Loop), un entorno
puramente textual que se ejecuta en una terminal y que, en cierto modo, sigue
la misma filosofía que los notebooks: introduces una instrucción, la ejecutas,
observas el resultado, luego ejecutas una segunda instrucción, y así 
ucesivamente&mdash;pero en este caso, para volver a ejecutar una instrucción
anterior, tienes que escribirla de nuevo. La segunda consiste en usar un
intérprete de Python para ejecutar un programa, de forma similar a como lo
harías con otros lenguajes como Go o Java.
```

## Primeros pasos con Python

Como se discute en {ref}`sec_aprender-y-programar`, supongo que ya estás
familiarizado con al menos un lenguaje de programación. Sin embargo, en esta
sección daré un vistazo rápido a algunas operaciones básicas de programación
para ver cómo se realizan en Python. Esto me permitirá introducir de inmediato
ejemplos de código en Python junto a los conceptos que voy explicando.

### Asignaciones
Asignar un valor a una variable utiliza la misma notación que en la mayoría de
los lenguajes de programación, siguiendo la sintaxis `variable = valor`. En
{ref}`sec_dynamic-tipig`, veremos que Python no requiere declaraciones de tipo:
las variables se crean automáticamente la primera vez que se les asigna un
valor, y ese valor determina implícitamente su tipo. Por ejemplo:

```python
age = 42
```

es una asignación que implica un tipo entero.

### Imprimir un valor
Ya vimos cómo la evaluación de una celda en un notebook puede producir una
salida. Sin embargo, este método tiene limitaciones (por ejemplo, solo imprime
el resultado de la última expresión evaluada en la celda de entrada), y no
funciona en absoluto fuera de notebooks. Más generalmente, puedes imprimir un
valor o el contenido de una variable pasándolos como argumentos a la función
`print`:

```python
print(age)
print(3.14)
```

### Ejecución condicional
En cuanto a la ejecución condicional, Python usa una sintaxis que probablemente
te resulte similar, aunque no idéntica a lo que ya conoces. Considera la
siguiente celda:

```python
if age >= 18:
  print('They are of age, they are', age, 'years old.')
else:
  print('They are not of age.')
```

```{margin}
La indentación puede hacerse con cualquier número de espacios o tabulaciones,
siempre que no mezcles ambos y mantengas la misma elección a lo largo de todo
el bloque. Hay argumentos tanto a favor como en contra de usar espacios o
tabulaciones, y sigue siendo un tema profundamente divisivo entre
desarrolladores&mdash;una verdadera guerra de preferencias. Personalmente, no
tengo intención de tomar partido: usa la que prefieras (cuando puedas
permitírtelo; a veces la elección está determinada por el entorno de trabajo),
pero sé coherente.
```

La selección se hace con la sentencia `if`, que debe ir seguida de una
condición que termina con dos puntos (`:`). El bloque de instrucciones que se
ejecuta cuando la condición es verdadera debe tener una indentación
consistente. La palabra clave `else` especifica un bloque alternativo si la
condición es falsa, usando la misma sintaxis[^one-liner]. Observa que el
ejemplo anterior muestra que:

- no hace falta encerrar la condición entre paréntesis,
- la función `print` permite imprimir mensajes en forma de cadenas de texto,
  encerradas entre comillas simples,
- puedes pasar un número variable de argumentos a `print`, que serán impresos
  separados por espacios.

### Definir funciones
La siguiente celda muestra cómo definir una función que toma un argumento
(interpretado como la edad de una persona) y devuelve un valor booleano
indicando si es mayor de edad, tras imprimir un mensaje similar al visto antes:

```{margin}
Observa cómo la ejecución genera dos celdas, cada una con un propósito muy
distinto: la primera contiene el mensaje impreso por la función `print`,
mientras que la segunda es la celda de salida que contiene el valor devuelto
por `check_age`. Vale la pena señalar que mezclar salida estándar y valores de
retorno de esta manera __no__ se considera una buena práctica de
programación[^bad-practice], pero en este caso me permite introducir varios
conceptos importantes en un solo ejemplo conciso.
```

```python
def check_age(age):
  if age >= 18:
    print('They are of age, they are', age, 'years old.')
    return True
  else:
    print('They are not of age.')
    return False

check_age(age)
```

Este ejemplo también nos permite observar que:

- la definición de una función empieza con la palabra clave `def`, seguida por
  el nombre de la función, un par de paréntesis que contienen sus parámetros y
  dos puntos;
- no se declaran los tipos de los argumentos, debido al tipado dinámico del
  lenguaje;
- el cuerpo de la función está indentado, y los bloques correspondientes a `if`
  y `else` están indentados adicionalmente;
- la instrucción `return` marca el final de la ejecución de la función y
  especifica el valor que devuelve la función;
- las constantes `True` y `False` se refieren a los dos posibles valores
  booleanos.

La principal ventaja de definir una función es, por supuesto, poder
reutilizarla con distintos argumentos, como se muestra a continuación:

```python
check_age(13)
```

### Importar módulos
En Python, los proyectos de software complejos y la reutilización de código se
basan en el concepto de _módulos_. Un módulo es, esencialmente, un archivo que
define una o más variables, funciones o clases. Puedes importar un módulo
completo o solo uno (o varios) de sus componentes. Los módulos son
especialmente útiles para trabajar con bibliotecas estándar o de terceros.
Considera el módulo `math`, que se distribuye con Python y define, entre otras
cosas, la variable `pi` (una aproximación de $\pi$) y la función `factorial`
(factorial de un entero). Estos dos elementos pueden ser _importados_ para que
se puedan usar en tu código como si los hubieras definido tú mismo, usando la
sintaxis `from <módulo> import <nombre>`:

```{margin}
Observa que es posible usar `import` para traer varios elementos de un módulo
en una sola instrucción.
```

```python
from math import factorial, pi

print(pi)
print(factorial(10))
```

```{margin}
También puedes definir _alias_ usando la forma
`from <módulo> import <elemento> as <alias>`.
```

Al trabajar con código complejo, es posible que elementos de distintos módulos
tengan el mismo nombre. Una manera común de evitar estos conflictos es usar
los llamados _namespaces_: importas el módulo completo usando
`import <módulo>`, y luego accedes a sus elementos individuales con notación de
punto, escribiendo el nombre del módulo seguido de un punto y el nombre del
elemento.

```python
import math

print(math.pi)
print(math.factorial(10))
```

En casos como este, si dos módulos `m1` y `m2` contienen un elemento llamado
`e`, no hay conflicto de nombres, porque te referirías a ellos como `m1.e` y
`m2.e`. Sin embargo, usar el nombre del módulo para acceder a sus elementos
hace que el código sea más largo y potencialmente menos legible. Por eso,
puedes importar un módulo usando un nombre alternativo más corto, o _alias_,
con la sintaxis `import <módulo> as <alias>`. Usaré este enfoque para las
paquetes que uso más frecuentemente en el libro: [numpy](http://www.numpy.org),
[pandas](http://pandas.pydata.org) y [matplotlib](http://matplotlib.org), que
nos permiten trabajar con arreglos, conjuntos de datos y visualizaciones
gráficas. Siempre las importo así:

```{margin}
Como puedes ver en la tercera línea de esta celda, algunos paquetes
están organizados en estructuras jerárquicas, similares a los de Java, y
comprenden varios _paquetes_: en este caso, `pyplot`.
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

```{admonition} Convenciones de nombres
:class: naming
Esta forma de importar numpy, pandas y el módulo `pyplot` de matplotlib usando
los alias `np`, `pd` y `plt` es una convención universalmente aceptada entre
los desarrolladores. Es altamente recomendable seguir esta convención, para que
quienes leen el código puedan identificar rápidamente el módulo al que se hace
referencia.
```

### Errores y excepciones
Python maneja situaciones de error lanzando _excepciones_, de manera similar a
como se hace en Java. El ejemplo siguiente muestra cómo se lanza una excepción
de tipo `NameError` al hacer referencia a una variable que nunca ha sido
inicializada:

```{margin}
La salida que indica una condición de error, típicamente llamada _stack trace_,
es detallada: muestra la porción de código involucrada, posiblemente listando
la secuencia de llamadas a funciones o métodos, y especifica tanto el tipo de
excepción como un mensaje asociado.
```

```python
print(uninitialized_variable)
```

Un aspecto clave de las excepciones es que su ocurrencia normalmente detiene la
ejecución del programa (o de la celda en un notebook), pero el programador
puede escribir código que se ejecuta automáticamente cuando ocurre una
excepción específica dentro de un cierto bloque. No entraré en detalles sobre
esta funcionalidad aquí. Para saber más, puedes consultar la
[documentación oficial](https://docs.python.org/3/tutorial/errors.html).

También hay situaciones de error que no pueden manejarse mediante excepciones:
un ejemplo clásico son los errores de sintaxis, que ocurren cuando el
analizador del código fuente no puede interpretar correctamente una línea.



## Ejercicios

[^compilers]: Una pregunta común es si Python es un lenguaje interpretado o
compilado. La respuesta depende de la implementación específica que se utilice,
aunque en la mayoría de los casos la respuesta más precisa es: «ninguno de los
dos». Python suele usar una compilación intermedia a _bytecode_, similar a
Java. Este bytecode es equivalente al código binario pero para una
_máquina virtual_. Un software específico se encarga luego de ejecutar el
bytecode traduciéndolo al código máquina del ordenador que se esté usando.
Cuando se utiliza CPython&mdash;la implementación de Python a la que se
refiere este libro&mdash;la compilación ocurre de forma automática y
transparente al importar módulos (véase {ref}`sec_importar-modulos`): el
resultado de la compilación es un conjunto de archivos `.pyc` guardados en un
directorio `__pycache__`, generados solo si no existen o son más antiguos que
el archivo fuente; en otros casos, el bytecode ya existente se ejecuta
directamente.

[^environment]: Existen algunas alternativas para crear y gestionar entornos
virtuales. En el momento de escribir estas líneas,
[Anaconda](https://docs.anaconda.com/anaconda/) y
[Miniconda](https://docs.anaconda.com/miniconda/) están entre las más
utilizadas junto con `venv`.

[^package-manager]: Anaconda y Miniconda, mencionadas en la nota anterior,
también proporcionan sus propios gestores de paquetes, que pueden usarse en
lugar de pip.

[^nb-lang]: Los notebooks no están vinculados a un lenguaje de programación
específico. Los gestores de notebooks suelen ser modulares y permiten la
instalación de uno o más _kernels_, cada uno dedicado a un lenguaje de
programación concreto. Principalmente trabajaré con código Python, pero
ocasionalmente veremos cómo ejecutar comandos de shell sin abrir una terminal
dedicada.

[^pronunce-jupyter]: Fernando Perez, uno de los creadores del proyecto Jupyter,
lo pronuncia así en su [charla](https://www.youtube.com/watch?v=cc2hHjARNTY) en
la conferencia PLOTCON 2016.

[^jupytext]: Incluir notebooks directamente en un repositorio git no es
recomendable. En su lugar, se pueden usar herramientas como
[jupytext](https://jupytext.readthedocs.io/), que sincronizan automáticamente
los notebooks con el código Python equivalente y versionan este último.

[^one-liner]: De hecho, es posible escribir una expresión `if` en una sola
línea, pero desaconsejo hacerlo porque tiende a reducir la legibilidad del
código.

[^bad-practice]: En principio, una función no debería imprimir salida en
pantalla salvo que sea para advertencias o errores. Incluso en esos casos,
normalmente es mejor usar características específicas del lenguaje como
_logging_ o excepciones en lugar de recurrir a `print`. Esto ayuda a evitar
confundir a quien lea la salida del programa, marca claramente la diferencia
entre mensajes y valores devueltos, y simplifica las pruebas del software.

