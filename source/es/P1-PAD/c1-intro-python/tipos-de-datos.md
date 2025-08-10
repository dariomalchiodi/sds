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

(sec:tipos-de-datos)=
# Tipos de datos

En el contexto de la programación, el término _tipo_ se usa comúnmente para
identificar la categoría a la que pertenece un determinado elemento de
_dato_&mdash;ya esté asociado a una variable, una expresión, un parámetro, al
valor devuelto por una función, y así sucesivamente. Asociar cada elemento de
dato con un tipo es importante porque determina qué operaciones se pueden
realizar sobre él: por ejemplo, la potenciación tiene sentido cuando el
exponente es un número, pero no, digamos, una cadena. Python también asocia
cada dato con un tipo, pero lo hace de un modo bastante distinto al de los
lenguajes que normalmente se encuentran al comenzar a aprender a programar.
Pronto veremos cómo funciona este mecanismo, introduciendo algunas categorías
amplias de tipos que exploraremos con más detalle en las siguientes secciones.
Esto también me dará la oportunidad de presentar brevemente algunos conceptos
de _programación orientada a objetos_ que serán necesarios para usar ciertas
bibliotecas a las que haré referencia, ya que este tema no siempre es familiar
para quienes empiezan a aprender los fundamentos de la ciencia de
datos.
```{margin}
En {ref}`sec:attributos` veremos que es importante no confundir el _tipo de un
atributo_ dentro de un _conjunto de datos_ con el _tipo de dato_ usado para
almacenar los valores de ese atributo.
```

(sec:tipado-dinamico)=
## Tipado dinámico

En la mayoría de los lenguajes que se estudian al aprender a programar
computadoras (como C, Java o Go), un elemento de dato debe asociarse
explícitamente con su tipo correspondiente mediante una _declaración_, que
determina lo que se puede hacer con ese dato. Esto permite detectar operaciones
no válidas&mdash;como la potenciación de una cadena mencionada antes&mdash;
mediante un análisis léxico preliminar del contenido del programa, y traducirlo
a código ejecutable solo si dicho análisis tiene éxito. Este enfoque se
conoce como _comprobación de tipos estática_, o _tipado estático_, en referencia
al hecho de que la coherencia de tipos se comprueba leyendo el código antes d
que se ejecute y fijando cada tipo de dato de una vez por todas.

Python, en cambio, adopta un enfoque diferente: elimina el requisito de
declaraciones explícitas y se basa en la _comprobación de tipos dinámica_, que
se realiza durante la ejecución del programa. Sin entrar en demasiados
detalles, antes de ejecutar cualquier operación Python comprueba si esta es
posible dados los valores de los operandos implicados. Si se detectan
inconsistencias, se lanza una excepción; de lo contrario, la ejecución
continúa.
```{margin}
Cabe señalar que Python es _fuertemente tipado_, lo que significa que nunca
realiza conversiones implícitas (como promociones) entre tipos de operandos
fundamentalmente distintos, como cadenas e enteros.
```

La comprobación de tipos dinámica simplifica mucho la estructura del lenguaje:
las variables y los parámetros de las funciones se definen simplemente
asignándoles _nombres_, sin especificar los tipos implicados. En concreto:

- una variable se crea automáticamente la primera vez que se le asigna un
  valor, y su tipo es el del valor asignado;
- los parámetros formales de métodos y funciones toman el tipo de los
  argumentos reales pasados en cada llamada;
- el tipo de valor que devuelve una función es el de la expresión devuelta al
  final de su ejecución.

Esto significa que, técnicamente, ya no tiene sentido hablar del tipo de una
variable, un parámetro o un valor de retorno de función como algo inmutable.
Una función podría, por ejemplo, devolver distintos tipos según los argumentos
proporcionados en su llamada; del mismo modo, una variable puede recibir un
valor cuyo tipo sea completamente diferente al que tenía antes. En resumen, el
concepto de tipo en Python es relativo: lo que puedes hacer con una variable o
un parámetro depende del valor que contenga en ese momento. Para complicar las
cosas, a partir de Python 3.5 es posible añadir una especie de declaración
mediante un formalismo llamado _type hinting_, que permite indicar en el código
el tipo de ciertos elementos (como los parámetros de una función o su valor de
retorno). Es importante recalcar que el tipado sigue siendo dinámico, pero así
puedes usar herramientas externas para realizar comprobación de tipos de
forma estática (es decir, basándose en el código escrito) y garantizar que las
variables se usan correctamente. Los editores e IDEs pueden aprovechar el
_type hinting_ para sugerir autocompletado o marcar advertencias. Por último,
el _type hinting_ también sirve para aligerar la documentación del software, de
modo que tenderé a usarlo cuando facilite la lectura del código, y evitarlo
cuando solo lo recargue innecesariamente.


(sec:typos-clases-objetos)=
## Tipos, clases y objetos

Python admite plenamente el paradigma de programación orientada a objetos, que
utiliza los conceptos de _clase_ y _objeto_ para representar y manipular datos.
Dicho de forma sencilla, una clase representa una _abstracción_ de todos los
datos de un cierto tipo. En la práctica, una clase es el conjunto de todos los
datos de un tipo determinado. Un solo elemento de ese conjunto se denomina
_objeto_ o _instancia_. Más específicamente, una clase define no solo qué
necesita almacenarse para que exista un dato (la información contenida en sus
_variables de instancia_), sino también las operaciones que pueden realizarse
sobre el objeto correspondiente (sus _métodos_). Por ejemplo, una hipotética
clase `Superhero` podría incluir:

- dos variables de instancia `name` y `secret_identity`, que contengan dos
  cadenas que representen el nombre y la identidad secreta de un superhéroe;
- dos métodos `fly` y `run` que implementen las acciones de volar y correr,
  respectivamente.
```{margin}
En algunos lenguajes orientados a objetos, los métodos sustituyen por completo
a las funciones. Como veremos más adelante, en Python ambos conceptos
coexisten.
```

Si lo único que nos interesa es referirnos al nombre e identidad secreta de un
superhéroe, y hacerlo volar o correr, la clase `Superhero` contiene todo lo que
necesitamos. Cuando queremos pensar en un superhéroe específico&mdash;digamos,
Superman&mdash;podemos crear el objeto correspondiente llamando a un método
especial llamado _constructor_ de la clase, pasando la información necesaria
para inicializar el objeto (a menudo, aunque no siempre, valores para todas o
algunas de las variables de instancia). El constructor devuelve una
_referencia_ al objeto creado, que normalmente se almacena en una variable. En
Python, el constructor se invoca usando el propio nombre de la clase, por lo
que crear el objeto Superman y almacenar su referencia podría, hipotéticamente,
hacerse así:

```{code}
# Este código es solo para ilustrar los conceptos de clase, constructor,
# referencia y objeto. No lo ejecutes, porque no funcionará.

# Además, observa que cualquier texto que siga a una almohadilla (#) se ignora
# durante la ejecución y, por tanto, representa un comentario.

hero = Superhero('Superman', 'Clark Kent')
``` 

```{margin}
Como veremos en {numfre}`sec:cadenas`, Python ofrece varios delimitadores de
cadenas, uno de los cuales es la comilla simple.
```
Aquí:

- `Superhero` es la clase y, por lo tanto, también el constructor;
- `'Superman'` y `'Clark Kent'` son las cadenas usadas para inicializar las dos
  variables de instancia;
- `hero` es el nombre de la variable que almacenará la referencia al objeto
  `Superhero` que representa a Superman.

Guardar en una variable la referencia devuelta por el constructor es necesario
porque, en la mayoría de los casos, la interacción con el objeto se realiza
mediante una sintaxis específica llamada _notación de punto_: se escribe el
nombre de la variable, luego un punto, y después el nombre de una variable de
instancia o método. En el primer caso, la expresión se evalúa al contenido de
esa variable de instancia; en el segundo, el resultado puede usarse para llamar
al método, pasando los parámetros necesarios.
```{margin}
En teoría, la notación de punto puede aplicarse directamente a la referencia
devuelta por el constructor, o incluso a _literales_ de clase[^literales],
aunque en la práctica los desarrolladores rara vez la usan así.
```

Volviendo a nuestro ejemplo, `hero.name` tiene como valor `'Superman'`, y se
puede llamar a `hero.fly()` (si el método no requiere parámetros). También aquí
el lenguaje se basa en la comprobación dinámica de tipos: independientemente de
la clase, cuando se analiza una notación de punto en tiempo de ejecución, si la
referencia apunta a un objeto que tiene la variable de instancia o el método
especificado, la ejecución continúa sin problemas; de lo contrario, se lanza un
`AttributeError`. Esto significa que, independientemente de su clase, si un
objeto permite acceder a las variables de instancia `name` y `secret_identity`
y llamar a los métodos `fly` y `run`, es en efecto equivalente a un objeto
`Superhero` y puede usarse en cualquier contexto diseñado para esa
clase[^duck-typing].

(adm:style-rules)=
```{admonition} Enfoque: identificadores y reglas de estilo
El término _identificador_ se refiere al nombre elegido para referirse de forma
única a entidades específicas en un programa, como variables, variables de
instancia, clases, funciones, métodos, parámetros, etc. Usaré los términos
«nombre» e «identificador» indistintamente, aunque el primero también puede
emplearse en otros contextos (piensa, por ejemplo, en el nombre de un archivo).

Desde un punto de vista sintáctico, para formar un identificador en Python se
pueden usar caracteres alfabéticos en mayúsculas y minúsculas (teniendo en
cuenta que el lenguaje distingue entre mayúsculas y minúsculas: `superman` y
`Superman` son dos identificadores distintos), dígitos y el carácter de guion
bajo (`_`), siempre que el primer carácter no sea un dígito.

Respetar la sintaxis es obligatorio, pero también es buena práctica seguir
_reglas de estilo_ de la manera más coherente posible, las cuales, entre otras
cosas, incluyen convenciones específicas sobre cómo formar identificadores. No
existe un único estándar; me referiré a la
[Guía de estilo para código Python](https://www.python.org/dev/peps/pep-0008/),
que también contiene una sección sobre
[Convenciones de nomenclatura](https://peps.python.org/pep-0008/#naming-conventions).
Para variables (de instancia y regulares), funciones y métodos, estas reglas
prescriben el llamado _snake case_: usar solo letras minúsculas y guiones bajos,
empleando estos últimos únicamente como separador en un identificador formado
por varias palabras (como `secret_identity` en el ejemplo anterior). El uso de
uno o más guiones bajos al principio o final de un nombre debe evitarse, pues
puede conferir un significado especial al código que solo emerge en situaciones
particulares. No trataré estos casos en este libro, pero conviene conocer este
aspecto desde el principio al aprender los fundamentos del lenguaje. Hay,
sin embargo, excepciones, y solo dos son relevantes para nuestros fines:

- cuando sea especialmente significativo usar una palabra clave del lenguaje
  como identificador (por ejemplo, `lambda`, que usaremos en
  {ref}`sec:anonymous-functions`, podría emplearse para expresar un concepto
  matemático o físico), es aceptable añadirle un guion bajo (dando, en este
  caso, el identificador `lambda_`);
- si se necesita referirse explícitamente a una variable utilizada en una parte
  muy limitada del código, o que no se usa en absoluto, en lugar de inventar un
  nombre significativo se puede usar un solo guion bajo como identificador.

Por otro lado, los identificadores de clase deben seguir el llamado
_upper camel case_, que requiere usar solo caracteres alfabéticos y poner en
mayúscula la primera letra de cada palabra (como en `Superhero`). Finalmente,
aunque Python no tiene el concepto de _constante_, puede emplearse la variante
de _snake case_ que usa únicamente letras mayúsculas (_screaming snake case_)
para sugerir que el contenido de una variable no cambiará después de su primera
(y única) asignación.

Aun siguiendo la sintaxis y las reglas de estilo, hay un amplio margen para
elegir un identificador: en el ejemplo anterior, en lugar de `hero` se podría
usar `clark_kent`, `superman`, `s`, `s1` o combinaciones de caracteres más o
menos inteligibles. No obstante, para mejorar la legibilidad del código, es muy
recomendable elegir un nombre que refleje el significado del identificador.
```


También conviene subrayar que la única manera de referirse a un tipo de dato en
Python es mediante el uso de clases: a diferencia de Java, no existen «tipos
primitivos» que almacenen enteros, números en coma flotante, etc., como meras
secuencias de bytes. En su lugar, los tipos enteros y de coma flotante
corresponden a las clases `int`[^maxint] y `float`, cada una caracterizada por
sus propios métodos.
```{margin}
Muchas de las clases que implementan tipos introducidos en las primeras
versiones de Python, como `int` y `float`, son una excepción a la regla de
estilo mencionada antes: por diversas razones, incluida la compatibilidad hacia
atrás, sus nombres no comienzan con mayúscula.
```

En resumen, cuando hablamos de una variable en código Python, más que decir que
una variable contiene un valor de un cierto tipo, sería más preciso hablar de
un _nombre_ (o identificador) asociado a una _referencia_ que, a su vez,
identifica de forma única al objeto de una clase: este último (temporalmente,
debido a la tipificación dinámica) determina el tipo del dato particular
correspondiente a la variable. En la jerga de programación, se usa el verbo
_asociar_ (o _enlazar_, _to bind_ en inglés) para indicar con más fuerza esta
relación entre el nombre y el objeto. Una discusión similar se aplica, por
ejemplo, a los parámetros formales de una función o método. Es cierto que esta
terminología puede resultar pesada y, de hecho, en el habla cotidiana es común
referirse a una variable (o parámetro) y al objeto&mdash;o incluso al
valor&mdash;que contiene.

```{admonition} Advertencia
La programación orientada a objetos es un tema muy complejo, y en esta sección
solo he arañado la superficie. Me he limitado a introducir lo que necesitas
saber para entender el código que presentaré más adelante, y para aprender a
escribir programas que automaticen las técnicas de análisis de datos que
presentaré en los capítulos siguientes. No he descrito cómo crear clases para
tipos de datos personalizados, ni he tratado temas específicos como la herencia
y el polimorfismo, porque conocer estos aspectos del lenguaje no es necesario
para seguir de forma provechosa el resto de lo que escribiré. Dominar estos
conceptos, sin embargo, es sin duda una habilidad esperada en un informátiques,
y también deseable para un científico de datos, pero todo esto queda bien fuera
del alcance de este libro. Para profundizar en estos temas, puedes consultar la
[sección correspondiente](https://docs.python.org/3/tutorial/classes.html) de
la documentación oficial de Python o la Parte IV en {cite:p}`ramalho`.
```

(sec:tipos-simples-y-estructurados)=
## Tipos simples y estructurados

Para simplificar un poco la discusión, podemos dividir los tipos de datos que
usaremos en dos grandes categorías:

- tipos de datos _simples_, que definen una pieza de información atómica que
  tiene poco sentido descomponer más, como un número entero o en coma flotante;
- tipos de datos _estructurados_, que se usan para agrupar múltiples tipos de
  datos (ya sean simples o estructurados), como arreglos o conjuntos.

Las dos siguientes secciones describirán, respectivamente, los tipos de datos
simples y estructurados que usaré en este libro. Incluso considerando solo el
núcleo del lenguaje, Python incluye varios tipos de datos (la documentación
oficial proporciona una
[lista](https://docs.python.org/3/library/datatypes.html)), a los que debemos
añadir los implementados por bibliotecas de terceros. El tratamiento que daré
aquí no es exhaustivo, y aunque lo fuera, estaría lejos de ser perfecto. Por un
lado, es incompleto porque existen clases que implementan tipos que no encajan
de forma natural en ninguna de las dos categorías introducidas (como las que
describen funciones, iteradores o conceptos complejos que no corresponden a
ningún tipo de dato en el sentido clásico); por otro lado, es discutible
asociar ciertos tipos a una u otra categoría: por ejemplo, las cadenas pueden
considerarse un tipo simple, pero también estructurado, ya que consisten en una
secuencia de caracteres.  

Para decidir si un tipo de dato es simple o estructurado, usaré el siguiente
criterio: un dato se considera estructurado si Python permite _iterar_ de forma
nativa sobre sus elementos usando la _forma idiomática_ `for`
(véase {ref}`sec:iterar`); en todos los demás casos, trataré el tipo de dato
como simple.

## Ejercicios

```{exercise} •
En relación con las características de la comprobación dinámica de tipos,
indica cuáles de las siguientes afirmaciones son verdaderas y cuáles falsas:

- en distintos momentos durante la ejecución de un programa, la misma variable
  puede contener valores de diferentes tipos;
- el nombre de una variable puede cambiar durante la ejecución;
- es posible asignar un valor a una variable antes de que esté definida;
- una función puede o no devolver un valor, dependiendo de la situación.
```

```{exercise} •
Considera la hipotética clase `Superhero` definida en
{ref}`sec:tipos-clases-objetos`, y sugiere variables de instancia y métodos
adicionales que tendrían sentido para sus objetos.
```

```{exercise} ••
Identifica cuáles de las siguientes afirmaciones sobre constructores en Python
son verdaderas y cuáles falsas:

- para crear un objeto de una clase, puede ser necesario llamar a su
  constructor correspondiente más de una vez;
- llamar a un constructor nunca requiere especificar valores para parámetros;
- cada variable de instancia de una clase corresponde a un parámetro en el
  constructor;
- llamar a un constructor es la única forma de crear un objeto;
- el nombre de una clase es también el identificador usado para llamar a su
  constructor correspondiente.
```

```{exercise} ••
La función `type` devuelve la clase del valor proporcionado como argumento.
Usa esta función para averiguar el tipo de las siguientes expresiones:

- `42`;
- `42.`;  
- `'foo'`;
- `None`;
- `int`.
```

```{exercise} ••
Considera las siguientes secuencias de caracteres e indica, para cada una, si
representa o no un identificador válido en Python. Para cada identificador
válido, decide si sigue las convenciones introducidas en el texto.

- `velocidad`;
- `velóz`;
- `speed`;
- `Speed`;
- `sp&emarc;&emarc;d`;
- `CarSpeed`;
- `CArSPeED`;
- `Car_Speed`
- `SPEED`
- `CAR_SPEED`
- `_speed`;
- `speed_`;
- `__speed`;
- `speed__`;
- `__speed__`;
- `__init__`;
- `set_level`;
- `set__level`;
- `set__level__`;
- `int`;
- `int_`;
- `i`;
- `i1`;
- `1i`;
- `_`;
- `black&white`;
- `jfellfsef`.
```

```{exercise} ••
Considera los tipos de datos que ya conoces (por ejemplo, los que hayas
estudiado en cursos de programación) y, para cada uno, especifica si entra en
la categoría de tipos simples o estructurados, explicando tu elección.
```

[^literales]: Si no sabes (o no recuerdas) qué es un literal, lo descubrirás en
el siguiente párrafo.

[^duck-typing]: El término _duck typing_ se usa a menudo para describir este
aspecto de la tipificación dinámica, y hace referencia a una frase atribuida al
poeta estadounidense James Whitcomb Riley: «when I see a bird that walks like a
duck and swims like a duck and quacks like a duck, I call that bird a duck».

[^maxint]: También vale la pena señalar que la implementación de la clase `int`
usa un enfoque de aritmética de precisión arbitraria: el número de bits
necesario para almacenar un entero no es fijo, sino que se asigna
dinámicamente, según los valores asignados en cada momento. Esto significa que
no existe un entero «más grande» o «más pequeño» almacenable, como ocurre en
otros lenguajes.
