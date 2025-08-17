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

(chap:presentacion)=
# Presentación

La primera parte de este libro presenta algunas herramientas básicas para el
análisis automatizado de conjuntos de datos pequeños o medianos[^big-data]
mediante el uso de un ordenador. Dominar estas herramientas, junto con la
capacidad deaplicarlas de forma eficaz en distintos escenarios de
_data science_, es hoy fundamental para analizar e interpretar la amplia
variedad de datos disponibles y aprovecharlos como apoyo en la toma de
decisiones.

Entre las herramientas esenciales se encuentran:

- un lenguaje de programación que permita escribir instrucciones para
  automatizar el procesamiento de datos;
- una biblioteca para la gestión estructurada de conjuntos de datos.

En este libro utilizaré Python y Pandas, presentados en
{ref}`chap:intro-python` y {ref}`chap:pandas`, respectivamente. Aunque
existen muchas alternativas válidas, estas dos tecnologías representan hoy
una parte central del ecosistema de análisis de datos, tanto en el ámbito
académico como en el profesional.

[^big-data]: Un conjunto de datos se considera pequeño cuando puede procesarse
con los recursos disponibles en un único ordenador. En el caso más
sencillo&mdash;el tratado en este libro&mdash;todo el conjunto de datos puede
cargarse en la memoria principal de un ordenador. En general, todavía hablamos
de datos «manejables localmente» si el conjunto de datos puede residir en el
almacenamiento masivo y procesarse progresivamente en la memoria principal, por
ejemplo, transfiriendo un registro cada vez. Cuando el tamaño de los datos
supera con creces la capacidad de almacenamiento masivo disponible
(aproximadamente, más de un terabyte con el hardware actualmente disponible),
entramos en el ámbito de los _big data_, que requieren enfoques diferentes de
los del análisis de datos tradicional.
