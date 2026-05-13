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

In the past, much data was regarded as a by-product of operational procedures
&mdash; sometimes computerized &mdash; intended mainly for storage and only
rarely reused. The idea that data are a strategic resource in almost every
area of human knowledge has taken hold only in the last twenty years. Today it
is fully recognized that, if collected, stored, and processed systematically,
data become essential tools for analyzing complex processes, helping us
understand them, and supporting decisions in critical contexts such as
medicine, politics, or finance.

```{margin}
After John Snow's intervention, infections did in fact decrease. That decline,
however, should be interpreted in a broader context: many people had already
left the neighborhood to seek safety. In any case, subsequent medical findings
confirmed Snow's intuition about how the disease was transmitted.
```

And yet, some remarkable examples show that a _data-driven_ approach already
existed in the nineteenth century, long before the term was coined. One of the
most famous dates back to 1854, during a cholera epidemic in London. The
physician John Snow, convinced that the disease was not spread through the air
&mdash; whereas the doctors of his time blamed _miasmas_, or _bad air_ &mdash;
decided to collect evidence in support of a different hypothesis: water
contamination. To do so, he overlaid on a map of the Soho district the number
of infections recorded in each house[^cartography]. The result, shown in
{numref}`john-snow`, highlighted that the cases were clustered near a water
pump located on Broad Street. To strengthen his thesis, Snow also observed
that brewers, who drank more beer than water &mdash; and therefore consumed a
pasteurized product &mdash; were less affected by the disease. Thanks to this
evidence, he convinced the authorities to disable the pump, helping to contain
the epidemic.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/2/27/20201116211939%21Snow-cholera-map-1.jpg
:width: 60%
:name: john-snow

Map of the Soho district drawn by John Snow during the 1854 cholera epidemic:
each black horizontal bar indicates an infection recorded in the adjacent
house. Public-domain image. Created by John Snow (1854). Source:
{extlink}`Wikimedia Commons </sds/short/cholera-map>`.
```

Curiously, the second example also takes place in 1854. That year Florence
Nightingale left for Crimea, where a war between Russia and the Ottoman Empire
was underway, with several European powers involved, including the United
Kingdom. Nightingale came from there, in her role as superintendent of the
Institute for Sick Gentlewomen, together with other volunteer nurses. In order
to document the shortcomings in the management of medical care, she decided to
collect data on the soldiers' health conditions. In 1858 she presented the
results in a report entitled «Notes on Matters Affecting the Health,
Efficiency and Hospital Administration of the British Army». That document
includes a _polar diagram_[^polar], reproduced in
{numref}`florence-nightingale`, which is now considered a classic example of
effective data visualization. The chart consists of two circular areas,
divided into twelve sectors corresponding to the months from April 1854 to
March 1855 (on the left) and from April 1855 to March 1856 (on the right).
The area of each sector represents the number of deaths, divided into three
categories:

- wounds sustained in battle (red),
- curable or preventable diseases (blue),
- other causes (black).

The visual effect is immediate: most of the deaths were not caused by combat.
Nightingale used that fact to denounce the inefficiency of field hospitals,
whose unsanitary conditions led to the spread among soldiers of diseases such
as cholera, typhus, and dysentery. It was also thanks to this intervention
that the military healthcare system was later reformed.

```{figure} https://upload.wikimedia.org/wikipedia/commons/archive/1/17/20201105141904%21Nightingale-mortality.jpg
:width: 100%
:name: florence-nightingale

Polar diagrams showing the deaths of British soldiers from April 1854 to March
1856 in the military hospital where Florence Nightingale served. Each sector
represents one month, with the area proportional to the number of deaths,
while the colors indicate the cause of death: red for battle wounds, blue for
curable diseases, and black for other causes. Public-domain image. Created by
Florence Nightingale (1858). Source: {extlink}`Wikimedia Commons
<https://malchiodi.com/sds/short/nightingale-source>`.
```

The cases of Snow and Nightingale show very clearly a descriptive approach to
data analysis: collecting and presenting information accurately makes it
possible to highlight relevant aspects of a phenomenon &mdash; in these
examples, the causes of cholera contagion and of soldiers' deaths &mdash; and
to provide solid grounds for informed decisions. Starting from the end of the
nineteenth century, however, statistics also began to develop on a more
theoretical and quantitative plane. Without any claim to completeness, let me
mention two fundamental figures: Ronald A. Fisher, who played a central role
in shaping the methods of modern statistics and their applications to genetics
and agricultural production, and William Gossett, who developed techniques for
controlling the quality of Guinness beer without compromising the entire
production process. For reasons of confidentiality, Gossett published his
results under the pseudonym «Student», so that his employer's competitors
would not discover the innovative methods used in the brewery.

With the advent of computers, from the 1940s onward, it soon became clear that
they could be used not only to mechanize operations, but also to generate and
store large quantities of data. As time passed and related technologies
developed, computing power increased, storage costs decreased, and the spread
of the internet made data more accessible. These factors led to a drastic
increase in their volume, amplifying their value.

Around the turn of the twentieth and twenty-first centuries, the role of the
_data scientist_ emerged: a person able to integrate computing and
mathematical/statistical skills with knowledge of a specific domain, thereby
turning raw data into useful information, often for _business_ purposes. But
what really distinguishes someone working as a data scientist from someone
working in statistics, computer science, or mathematics? The answer is not
immediate.

Today, all of them need a more-than-decent familiarity with tools and concepts
belonging to computer science, in addition to knowing at least the basics of
statistics and mathematics. Yet those figures remain distinct: people working
in computer science are almost never the same as those working in statistics
or mathematics, and vice versa. For instance, there are areas of computer
science &mdash; such as operating systems or smartphone and mobile-application
development &mdash; that can be safely ignored in typical settings of
mathematics, statistics, or data science. Likewise, most computer scientists do
not venture into fields such as topology or hypothesis testing.

I also stress that, until now, I have deliberately left artificial
intelligence out of the discussion. It is a relatively recent discipline, but
one that is having a huge impact on everyday life. Although it often intersects
with data analysis, its main goal is the study and automatic replication of
processes that, when carried out by human beings, require some form of
intelligence. In some cases those processes rely on data-driven reasoning; in
others, completely different approaches are needed. It is precisely this
variety of aims and methods that makes artificial intelligence a branch of
computer science deserving separate treatment from the topics addressed in
this book.

This book aims to deal with topics ranging from programming to data analysis,
passing through probability and statistics. It is a demanding combination, but
one that is coherent with the often fragmented educational path of people who
study computer science. Reading it (and, _ça va sans dire_, understanding its
contents) will not turn you into data scientists, nor into experts in
statistics or mathematics. Strictly speaking, not even into experts in
computer science or artificial intelligence. But it will give you a solid
foundation, one of the building blocks needed to become a capable and
well-prepared computer scientist, together with the corresponding professional
autonomy &mdash; in short, to develop the skills that make a person worth
taking seriously. In any case, I want to stress that in the end what matters is
not the professional label assigned to us, but what we know how to do well.

[^cartography]: While Snow’s approach is the most famous, the real pioneers of
_statistical cartography_ were the French scholars André-Michel Guerry and
Charles Dupin, who already in the first half of the nineteenth century used
charts to highlight differences among the provinces of France in terms of
literacy or crime. Dupin was the first to introduce what we now call
{extlink}`choropleth maps <https://en.wikipedia.org/wiki/Choropleth_map>`, in
which the regions of a geographical map are colored according to the value of
a specific indicator.

[^polar]: It is worth noting that the polar diagrams made famous by Florence
Nightingale had already been introduced in 1829 by André-Michel Guerry, the
same person mentioned in the previous footnote.
