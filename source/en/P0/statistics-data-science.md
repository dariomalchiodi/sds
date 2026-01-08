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

(sec_statistics-data-science)=
# Statistics, data science, and other labels

In the past, data were mostly considered a byproduct of operational
procedures&mdash;sometimes executed automatically&mdash;meant primarily for
archiving and rarely reused in production processes. The idea that data are a
crucial resource in almost every area of human knowledge has only gained
widespread acceptance in the last twenty years, fully recognizing that when
systematically collected, stored, and processed, data become essential tools
for analyzing complex processes and supporting decision-making in critical
domains like medicine, politics, or finance.

```{margin}
It’s worth noting that after John Snow’s intervention, there was indeed a drop
in infections. However, this decline should be seen in a broader context, also
due to the fact that a significant portion of the population had left the
neighborhood to seek safety. In any case, later findings in medical research
would confirm the validity of Snow’s hypothesis about how the disease was
transmitted.
```

There are, however, some historical examples that show how the data-driven
approach was already present in the late 19th century. In 1854, during a
cholera outbreak in London, the physician John Snow overlaid a map of the Soho
district with information about the number of infections in individual
houses[^cartography]. The resulting diagram, shown in {numref}`john-snow`,
highlights how the cases were concentrated around a water pump located on Broad
Street. Snow's goal was to disprove the medical consensus of the time, which
held that infection spread through the air (a theory that referred to
_miasmas_, or _bad air_), and instead support the hypothesis that the real
cause was water contamination. Supporting this idea, Snow also observed that
brewers&mdash;who drank more beer (pasteurized) than water&mdash;were less
affected by the disease. Thanks to this evidence, he convinced the authorities
to shut down the pump, helping to contain the epidemic.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/2/27/20201116211939%21Snow-cholera-map-1.jpg
:width: 60%
:name: john-snow

Map of Soho, London, showing the number of infections in individual houses
(black horizontal bars) during the 1854 cholera outbreak. Public domain image.
Created by John Snow (1854). Source:
[Wikimedia Commons](https://en.wikipedia.org/wiki/File:Snow-cholera-map-1.jpg).
```

Interestingly, the second example also dates to the same year. In 1854,
Florence Nightingale went on a mission to Crimea, where a war was taking place
between Russia and the Ottoman Empire, involving several European powers,
including the United Kingdom. Nightingale, who was superintendent at the
Institute for Sick Gentlewoman, came from there with a group of volunteer
nurses. Realizing how disorganized the medical care provided to soldiers was,
she collected data that she later presented in 1858 in a report titled _Notes
on Matters Affecting the Health, Efficiency and Hospital Administration of the
British Army_. The document included a famous _polar diagram_[^polar],
reproduced in {numref}`florence-nightingale` and often cited as an example of
effective data visualization. The diagram consists of two circular areas, each
divided into twelve sectors, one for each month in the periods from April 1854
to March 1855 and April 1855 to March 1856. The area of each sector represents
the monthly number of deaths among soldiers, split into three categories:

- wounds sustained in battle (red),
- preventable or treatable diseases (blue),
- other causes (black).

Without going into technical details, it’s clear that most of the deaths
weren’t due to combat. Nightingale used this fact to expose how disorganized
the field hospitals were&mdash;their unsanitary conditions contributing to the
spread of diseases like cholera, typhus, or dysentery among soldiers. This
intervention was instrumental in bringing about reforms to the military
healthcare system.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/1/17/20201105141904%21Nightingale-mortality.jpg
:width: 100%
:name: florence-nightingale

Polar diagrams showing the death toll among British soldiers between April 1854
and March 1856 at the military hospital where Florence Nightingale served. The
area of each sector represents the number of deaths, and the colors indicate
the cause: red for battle wounds, blue for preventable diseases, and black for
other causes. Public domain image. Created by Florence Nightingale (1858).
Source: [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Nightingale-mortality.jpg).
```

The cases of Snow and Nightingale illustrate a descriptive approach to data
analysis: solid data collection and presentation help highlight important
aspects of a phenomenon (in this case, the causes of cholera outbreaks and most
soldier deaths), enabling informed decisions. At the same time, starting from
the late 19th century, statistics began to develop in a more quantitative and
theoretical direction. Without any claim to completeness, it’s worth mentioning
the contributions of Ronald A. Fisher, who played a central role in shaping
modern statistical methods and applying them in fields like genetics and
agricultural production, and William Gossett, who developed statistical
techniques to control the quality of Guinness beer without wasting entire
batches. He published his work under the pseudonym «Student» to keep
competitors from learning the innovative methods being used at the brewery.

With the advent of computers, used from the 1940s to automate repetitive tasks,
it soon became clear that not only could operations be mechanized, but huge
amounts of data could also be generated and stored. Increasing computing power,
lower storage costs, and the spread of the internet made these data more
accessible and greatly increased their volume&mdash;amplifying their value.

Around the turn of the 21st century, the role of the _data scientist_ emerged:
an individual able to combine computing and statistical skills with domain
knowledge in a specific field, to transform raw data into useful
information&mdash;often business-oriented. But what really sets a data
scientist apart from a statistician or a computer scientist?

There’s no simple answer. Today, a statistician needs to be familiar with
computer science tools and concepts, just as a computer scientist should
understand key ideas in statistics and math. Still, the three roles aren’t the
same: a computer scientist is almost never also a statistician or
mathematician, and vice versa. There are areas of computer science, like
operating systems or mobile app development, that a mathematician may
completely ignore; likewise, many computer scientists retain only vague
memories of probability or statistics and wouldn’t venture into topics like
topology or hypothesis testing.

I’ve deliberately avoided bringing artificial intelligence (AI) into the
picture until now&mdash;a relatively recent field that’s having a major impact
on daily life. While it often overlaps with data analysis, its main goal is to
study and replicate processes that, when performed by humans, require some form
of intelligence. In some cases, these processes rely on data-driven reasoning;
in others, completely different approaches are needed. It’s exactly this
diversity of goals and methods that makes AI a distinct area of computer
science&mdash;deserving its own space, separate from the topics covered in this
book.

In this volume, topics range from programming to data analysis, including
probability and statistics. It’s a challenging combination, but one that fits
the often fragmented educational path of computer science students. Reading it
(and, _ça va sans dire_, understanding it) won’t make you a data
scientist&mdash;or a statistician or mathematician, for that matter. And to be
fair, not even a fully-fledged computer scientist or AI expert. But it will
give you a solid foundation, one of the key building blocks for becoming a
capable, well-prepared computer scientist&mdash;in short, someone to take
seriously. In the end, what really matters isn’t the label we’re given, but
what we know how to do well.

[^cartography]: While Snow’s approach is the most famous, the real pioneers of
_statistical cartography_ were French scholars André-Michel Guerry and Charles
Dupin. Already in the first half of the 19th century, they were using charts to
highlight differences among the provinces of France in areas like literacy or
crime rates. Dupin was the first to introduce what we now call
[choropleth maps](https://en.wikipedia.org/wiki/Choropleth_map), in which
geographical regions are colored based on the value of a specific indicator.

[^polar]: It's worth noting that the polar diagrams made famous by Florence
Nightingale were actually first introduced in 1829 by André-Michel Guerry (the
same person mentioned in the previous footnote).
