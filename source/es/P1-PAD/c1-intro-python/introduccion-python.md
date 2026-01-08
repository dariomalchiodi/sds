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

(chap_intro-python)=
# Procesar datos con Python

> Beautiful is better than ugly.<br/>
> Explicit is better than implicit.<br/>
> Simple is better than complex.<br/>
> Complex is better than complicated.<br/>
> Flat is better than nested.<br/>
> Sparse is better than dense.<br/>
> Readability counts.<br/>
> Special cases aren't special enough to break the rules.<br/>
> Although practicality beats purity.<br/>
> Errors should never pass silently.<br/>
> Unless explicitly silenced.<br/>
> In the face of ambiguity, refuse the temptation to guess.<br/>
> There should be one-- and preferably only one --obvious way to do it.<br/>
> Although that way may not be obvious at first unless you're Dutch.<br/>
> Now is better than never.<br/>
> Although never is often better than *right* now.<br/>
> If the implementation is hard to explain, it's a bad idea.<br/>
> If the implementation is easy to explain, it may be a good idea.<br/>
> Namespaces are one honking great idea -- let's do more of those!<br/>
>
> --- El Zen de Python, por Tim Peters[^zen]


En este capítulo vamos a ver de forma resumida las herramientas básicas para
explorar y analizar datos usando [Python](https://www.python.org) como lenguaje
de programación, junto con los
[notebooks](https://en.wikipedia.org/wiki/Notebook_interface) para escribir y
ejecutar código, y las bibliotecas principales del llamado
_Python data science stack_, que irán apareciendo a medida que las vayamos
necesitando.
```{margin}
Los notebooks se pueden usar en varios entornos de desarrollo: en el momento
en que se escribió este libro, los más populares eran
[Jupyter](https://jupyter.org/) y
[Visual Studio Code](https://code.visualstudio.com/), que además son gratuitos,
aunque hay otras opciones.
```

Todas las herramientas que menciono forman parte del
[FLOSS](https://es.wikipedia.org/wiki/Software_de_c%C3%B3digo_abierto_y_libre),
y por lo tanto se distribuyen con licencias que permiten, entre otras cosas,
usarlas libremente.
```{margin}
FLOSS es la sigla de «Free/Libre Open Source Software»
```

El texto está pensado para estudiantes que ya tengan cierta experiencia
programando y, en particular, dominen al menos un lenguaje de programación con
un enfoque imperativo y procedimental. En cambio, sí que introduciré algunos
conceptos básicos de la programación orientada a objetos, necesarios para
trabajar con el _data science stack_ de Python, y que no siempre forman parte
del bagaje de quien empieza a estudiar esta materia.


[^zen]: El «Zen de Python» es el nombre oficial de $19$ pautas para escribir
código Python aprovechando su elegancia y su sintaxis, en vez de traducir al
pie de la letra otros lenguajes: lo que se conoce como «escribir código
pitónico». Estas pautas, de dominio público, fueron escritas en 1999 por Tim
Peters, uno de los principales contribuidores de Python. Además de estar
publicadas en [esta sección](https://peps.python.org/pep-0020/) de los
_Python Enhancement Proposals_, se pueden ver ejecutando la instrucción de
Python `import this`.

