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

(chap_teoria-conjuntos)=
# Teoría de conjuntos

En 1895, Georg Cantor propuso una definición capaz de capturar con notable
precisión la idea intuitiva de conjunto: «por multiplicidad o conjunto
entiendo todo _múltiple_ que puede pensarse como _uno_» [^cita-cantor].
Según esta concepción, un conjunto es una agrupación de objetos distintos
que comparten alguna propiedad común. Poco después, el propio Cantor
refinó su definición: «por "conjunto" entendemos cualquier colección $M$
de objetos $m$ definidos y distintos de nuestra intuición o de nuestro
pensamiento — llamados "elementos" de $M$» {cite}`cantor-1895`.

Pocos años después, la comunidad matemática descubrió que este enfoque,
hoy conocido como _teoría ingenua de conjuntos_, escondía trampas lógicas
y paradojas; para evitarlas, fue necesario refundar la materia sobre un
sistema axiomático mucho más riguroso {cite}`suppes`. A pesar de ello, en
este libro he optado por adoptar la perspectiva ingenua: aunque menos
formal, me permite mantener la exposición simple y centrada en los
objetivos pedagógicos de esta obra, sin sobrecargar el discurso. Por lo
demás, como observa Rudy Rucker, es significativo que la palabra _set_
(conjunto) tenga la entrada más larga entre todos los términos del
_Oxford English Dictionary_ {cite}`rucker`.

[^cita-cantor]: Traducido del original: "Unter einer 'Mannigfaltigkeit'
oder 'Menge' verstehe ich nämlich allgemein jedes Viele, welches sich als
Eines denken lässt" {cite}`cantor-1883`. La cursiva en la traducción
española ha sido añadida por el autor para subrayar el contraste conceptual
entre pluralidad y unidad.
