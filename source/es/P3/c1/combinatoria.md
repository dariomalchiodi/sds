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

(chap_combinatoria)=
# Combinatoria

La _combinatoria_ es la rama de las matemáticas que estudia el número de formas
en que los elementos de un conjunto finito pueden agruparse u ordenarse. Como
cabe intuir, este número no depende de la naturaleza de los objetos considerados:
ya se trate de elementos tangibles (como frutas o bicicletas) o de entidades
abstractas (como los poderes de un superhéroe o los colores de las paredes de
una oficina), la lógica necesaria para contar sus configuraciones permanece
invariante.

Para abordar correctamente un problema de recuento, es importante responder a
tres preguntas fundamentales:

- ¿Puede elegirse el mismo elemento más de una vez?
- ¿Son todos los elementos de partida distintos, o algunos son
  _indistinguibles_ entre sí?
- ¿Importa el orden en que se seleccionan los elementos, o no?

Una vez aclarados estos aspectos, el número de configuraciones posibles depende
en general de solo dos parámetros: el tamaño $n$ del conjunto de partida y el
número $k$ de elementos que se pretende seleccionar.

Una metáfora especialmente útil es la siguiente: imaginemos asignar $n$
_objetos_ (tangibles o no) a $k$ _casillas_ disponibles. En las secciones que
siguen, analizaré los principales modos de agrupación y ordenación y, para cada
uno de ellos, mostraré cómo derivar la fórmula para calcular el número de casos
posibles.
