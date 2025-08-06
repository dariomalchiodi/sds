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

# Introducción

La primera parte de este libro presenta algunas herramientas básicas para el
análisis automatizado de conjuntos de datos de tamaño pequeño o
medio[^big-data], utilizando un ordenador. Dominar estas herramientas
&mdash;junto con la capacidad de aplicarlas de manera eficaz en distintos
escenarios de data science&mdash; es hoy fundamental para analizar e
interpretar la gran variedad de datos disponibles y utilizarlos como apoyo en
la toma de decisiones.

Entre las herramientas clave se encuentran:

- un lenguaje de programación, que nos permita escribir instrucciones para
  automatizar el procesamiento de datos;
- una biblioteca para la gestión estructurada de los datasets.

En este libro utilizaremos Python y Pandas para estos fines, presentados
respectivamente en los capítulos {ref}`chap:intro-python` y {ref}`chap:pandas`.
Si bien existen muchas alternativas válidas, estas dos tecnologías constituyen
actualmente una parte central del ecosistema de análisis de datos, tanto en
contextos académicos como en el ámbito profesional.

[^big-data]: Un dataset se considera de tamaño reducido cuando puede procesarse
con los recursos disponibles en un solo ordenador. En el caso más simple
&mdash;que es el que se trata en este libro&mdash; el conjunto completo de
datos cabe en la memoria principal del equipo. De forma más general, los datos
aún se consideran «gestionables localmente» si pueden almacenarse en disco y
cargarse progresivamente en la memoria RAM, por ejemplo, un registro a la vez.
Cuando el tamaño de los datos supera significativamente la capacidad de
almacenamiento disponible (aproximadamente, más de un terabyte con el hardware
actual), entramos en el ámbito del _big data_, que requiere enfoques
computacionales distintos a los del análisis clásico de datos.
