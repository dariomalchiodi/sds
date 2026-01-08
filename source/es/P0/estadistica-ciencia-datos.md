(sec_estadistica-ciencia-datos)=
# Estadística, ciencia de datos y otras etiquetas

En el pasado, los datos eran en su mayoría considerados un subproducto de
procedimientos operativos&mdash;a veces informatizados&mdash;, destinados
principalmente al archivo y rara vez reutilizados en los procesos productivos.
La idea de que representan un recurso crucial en casi todos los ámbitos del
conocimiento humano se ha consolidado solo en las últimas dos décadas,
reconociendo plenamente que, cuando se recopilan, almacenan y procesan
sistemáticamente, los datos se convierten en herramientas fundamentales para
analizar procesos complejos y apoyar decisiones en contextos críticos, como los
de la medicina, la política o las finanzas.

```{margin}
Es importante destacar que, tras la intervención de John Snow, se registró
efectivamente una disminución de los contagios. Sin embargo, esta caída debe
interpretarse en un contexto más amplio, también debido al hecho de que una
parte significativa de la población había abandonado el barrio para ponerse a
salvo. En cualquier caso, los descubrimientos posteriores de la investigación
médica confirmarán la validez de la hipótesis de Snow sobre las formas de
transmisión de la enfermedad.
```

Existen sin embargo algunos casos históricos que muestran cómo el enfoque
_data-driven_ ya estaba presente a finales del siglo XIX. En 1854, frente a una
epidemia de cólera en Londres, el médico John Snow superpuso al mapa del barrio
de Soho la información relativa al número de contagios en cada
casa[^cartografia]. El gráfico obtenido, visible en {numref}`john-snow`,
muestra cómo los casos se concentraban cerca de una bomba de agua situada en
Broad Street. El objetivo de Snow era refutar la creencia de los médicos de la
época según la cual el contagio ocurría por vía aérea (se hablaba de _miasmas_,
o _mal aire_), y al mismo tiempo apoyar la hipótesis de que la verdadera causa
era la contaminación del agua. Como apoyo a esta hipótesis, Snow también
observó que los cerveceros, que bebían más cerveza&mdash;sometida a
pasteurización&mdash;que agua, eran menos afectados por la enfermedad. Gracias
a estas evidencias, convenció a las autoridades para desactivar la bomba,
contribuyendo así a contener el brote.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/2/27/20201116211939%21Snow-cholera-map-1.jpg
:width: 60%
:name: john-snow

Mapa del barrio de Soho, Londres, con indicación del número de contagios en
cada casa (las lineas finas negras) durante la epidemia de cólera de 1854.
Imagen de dominio público. Realizada por John Snow (1854). Fuente:
[Wikimedia Commons](https://en.wikipedia.org/wiki/File:Snow-cholera-map-1.jpg).
```

Curiosamente, el segundo ejemplo también se sitúa en ese mismo año. En 1854,
Florence Nightingale llega en misión a Crimea, donde se está desarrollando una
guerra entre Rusia y el Imperio Otomano, con la implicación de varias potencias
europeas, incluido el Reino Unido. De allí proviene Nightingale, en calidad de
superintendente del Institute for Sick Gentlewoman, junto con otras enfermeras
voluntarias. Al darse cuenta de la desorganización en la atención médica
proporcionada a los soldados, recoge datos que presentará en 1858 en un informe
titulado _Notes on Matters Affecting the Health, Efficiency and Hospital
Administration of the British Army_. En ese documento se incluye un célebre
_diagrama polar_[^polari], reproducido en {numref}`florence-nightingale`,
citado con frecuencia como ejemplo de visualización eficaz de datos. El
diagrama está compuesto por dos áreas circulares, cada una dividida en doce
sectores, uno por cada mes de los periodos abril 1854&ndash;marzo 1855 y abril
1855&ndash;marzo 1856. El área de cada sector representa el número de muertes
mensuales entre los soldados, divididas en tres categorías:

- heridas de guerra (rojo),
- enfermedades curables o prevenibles (azul),
- otras causas (negro).

Sin entrar en detalles técnicos, está claro que la mayoría de las muertes no se
debía a los combates, hecho que Nightingale utilizó para denunciar la
desorganización de los hospitales de campaña, cuyo entorno insalubre propiciaba
la propagación entre los soldados de enfermedades como el cólera, el tifus o la
disentería. También gracias a esta intervención, el sistema sanitario militar
fue posteriormente reformado.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/1/17/20201105141904%21Nightingale-mortality.jpg
:width: 100%
:name: florence-nightingale

Diagramas polares que muestran la serie de muertes de soldados británicos
registradas entre abril de 1854 y marzo de 1856 en el hospital militar donde
orestaba servicio Florence Nightingale. El área de cada sector representa el
número de muertes, mientras que los colores indican la causa: rojo para heridas
de guerra, azul para enfermedades curables y negro para otras causas. Imagen de
dominio público. Realizada por Florence Nightingale (1858). Fuente:
[Wikimedia Commons](https://en.wikipedia.org/wiki/File:Nightingale-mortality.jpg).
```

Los casos de Snow y Nightingale ilustran un enfoque descriptivo del análisis de
datos: una buena recopilación y presentación de la información permite poner en
evidencia aspectos relevantes de un fenómeno (las causas, en este caso, de los
contagios de cólera y de la mayoría de las muertes entre los soldados),
apoyando decisiones informadas. Paralelamente, a partir de finales del siglo
XIX, también se desarrolla la estadística en un sentido más cuantitativo y
teórico. Sin ánimo de ser exhaustivos, vale la pena mencionar las
contribuciones de Ronald A. Fisher, quien tuvo un papel central en el diseño de
los métodos de la estadística moderna, así como en sus aplicaciones en genética
y producción agrícola, y de William Gossett, quien desarrolló técnicas
estadísticas para controlar la calidad de la cerveza Guinness sin comprometer
la producción completa, publicando sus resultados bajo el seudónimo «Student»
para evitar que los competidores de su empresa descubrieran los métodos
innovadores utilizados en la fábrica.

Con la llegada de los ordenadores, utilizados desde los años 40 para
automatizar tareas repetitivas, pronto se comprendió que no solo era posible
mecanizar operaciones, sino también generar y conservar una enorme cantidad de
datos. El aumento de la potencia de cálculo, la reducción del coste del
almacenamiento y la difusión de internet hicieron que estos datos fueran más
accesibles y aumentaron drásticamente su volumen, amplificando su valor.

Entre finales del siglo XX y principios del XXI ha surgido la figura del
_data scientist_, profesional capaz de integrar competencias informáticas y
estadísticas con el conocimiento de un dominio de aplicación específico, para
transformar datos brutos en información útil, a menudo orientada al ámbito
empresarial. Pero, ¿qué distingue a un _data scientist_ de un estadístico o de
un informático?

La respuesta no es sencilla. Hoy, un estadístico debe tener una sólida
familiaridad con herramientas y conceptos propios de la informática, así como
un informático debería dominar algunos aspectos fundamentales de la estadística
y las matemáticas. Sin embargo, las tres figuras no coinciden: un informático
casi nunca es también estadístico, ni matemático, y viceversa. Existen ámbitos
de la informática, como el desarrollo de sistemas operativos o de aplicaciones
para dispositivos móviles, que un matemático puede ignorar completamente; del
mismo modo, muchos informáticos conservan solo vagos recuerdos de conceptos
probabilísticos o estadísticos, y difícilmente se aventurarían en territorios
como la topología o las contrastes de hipótesis.

Cabe señalar que he evitado mencionar, hasta ahora, la inteligencia artificial,
disciplina relativamente reciente pero que está teniendo un gran impacto en la
vida cotidiana. Aunque a menudo se cruza con el análisis de datos, su objetivo
principal es el estudio y la replicación automática de procesos que, cuando son
realizados por seres humanos, requieren alguna forma de inteligencia. En
algunos casos, estos procesos se basan en razonamientos guiados por los datos;
en otros, en cambio, se requieren enfoques completamente distintos. Es
precisamente esta variedad de objetivos y métodos lo que hace que la
inteligencia artificial sea una rama de la informática que merece un
tratamiento aparte respecto a los temas abordados en este libro.

El presente volumen se propone abordar temas que van desde la programación
hasta el análisis de datos, pasando por la probabilidad y la estadística. Una
combinación desafiante, pero coherente con el recorrido formativo&mdash;a
menudo fragmentado&mdash;de quienes estudian informática. Leerlo (y,
_ça va sans dire_, comprender su contenido) no os convertirá en
_data scientist_, ni en estadísticos o matemáticos. Y, para ser precisos,
tampoco en informáticos o expertos en inteligencia artificial. Pero os
proporcionará una base sólida, uno de los pilares fundamentales para
convertirse en un informático competente y preparado&mdash;en resumen, alguien
a quien tomarse en serio. En cualquier caso, me gustaría subrayar que, al
final, lo que cuenta no es la etiqueta profesional que nos asignen, sino lo
que sabemos hacer bien.

[^cartografia]: Aunque el enfoque de Snow es el más conocido, los verdaderos
precursores de la _cartografía estadística_ fueron los franceses André-Michel
Guerry y Charles Dupin, que ya en la primera mitad del siglo XIX usaban
gráficos para mostrar diferencias entre las provincias de la República en
aspectos como la alfabetización o la tasa de criminalidad. Dupin fue el primero
en introducir lo que hoy llamamos
[mapas coropléticos](https://es.wikipedia.org/wiki/Mapa_coropl%C3%A9tico), en
los que las regiones de un mapa geográfico se colorean según el valor de un
indicador específico.

[^polari]: Cabe señalar que los diagramas polares popularizados por Florence
Nightingale ya habían sido introducidos en 1829 por André-Michel Guerry (el
mismo citado en la nota anterior).
