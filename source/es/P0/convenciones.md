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

```{raw} html

<script type="module" src="https://pyscript.net/releases/2025.5.1/core.js"></script>
```

(sec:convenciones)=
# Convenciones

Como se mencionó en el párrafo anterior, a menudo intercalaré el texto con
código, no tanto con el objetivo de ejecutarlo, sino más bien con fines
ilustrativos (por ejemplo, para indicar los literales `true` y `false` como los
únicos valores posibles para el tipo de dato `bool`). En este caso, utilizaré
una fuente monoespaciada con un color distinto al del texto principal. En
cambio, cuando sea necesario mostrar una o más líneas de código pensadas para
ser ejecutadas por quien lee, presentaré dichas líneas dentro de un recuadro
que recuerda a la típica _celda de código_ de un _notebook_ (si no sabes qué es
un _notebook_, no te preocupes: hablaré de ello en la {ref}`sec:notebook`).
También en este caso usaré una fuente monoespaciada, pero la coloración del
texto destacará ciertos elementos del código (como variables, literales,
palabras clave, etc., de forma similar a lo que hacen los IDE modernos).
Además, el código aparecerá separado del texto principal, como en el siguiente
ejemplo.
```{margin}
Es práctica común utilizar una fuente monoespaciada (en la que todos los glifos
usados para representar una letra tienen el mismo ancho) para visualizar
código, entradas y salidas, por una serie de razones que optimizan la
legibilidad del propio código, como la mayor facilidad para indentar
instrucciones o el menor riesgo de confundir caracteres similares como 1 y l.
```

```python
age = 24
print(age &lt;= 42)
```

Normalmente, mostraré la posible salida de la ejecución dentro de una
_celda de salida_ específica, colocada justo después de la celda de código,
como se muestra a continuación.

```python
print(age &lt;= 42)
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

