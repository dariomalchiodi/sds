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

(chap_overview)=
(sec_overview)=
# Overview

The purpose of this chapter is twofold: on the one hand, it aims to describe
the logic with which I have organized the contents and to introduce the key
concepts in a relatively informal way. On the other hand, it explains how to
use the interactive components of the book. As stated in
{ref}`chap_approach`, throughout the text I will refer to a _dataset_ obtained
by modifying a subset of the {extlink}`Superhero database
<http://www.superherodb.com>`. The examples therefore draw on the world of
superheroes, each of whom is described by the _attributes_ listed in
{numref}`tab_dataset`.

```{table} Description of the dataset used in the examples.
:name: tab_dataset
:align: center
| Attribute          | Meaning                  | Content                                                  |
|--------------------|--------------------------|----------------------------------------------------------|
| `name`             | unique identifier        | string                                                   |
| `full_name`        | full name                | string                                                   |
| `identity`         | secret identity          | string                                                   |
| `alignment`        | moral alignment          | `'Good'`, `'Neutral'`, or `'Bad'`                        |
| `place_of_birth`   | place of birth           | string                                                   |
| `creator`          | publisher/creator        | string                                                   |
| `universe`         | universe                 | string                                                   |
| `first_appearance` | year of first appearance | integer                                                  |
| `eye_color`        | eye color                | string                                                   |
| `hair_color`       | hair color               | string                                                   |
| `height`           | height in cm             | floating-point number                                    |
| `weight`           | weight in kg             | floating-point number                                    |
| `strength`         | strength                 | integer (from `0` to `100`)                              |
| `intelligence`     | intelligence             | `'Low'`, `'Moderate'`, `'Average'`, `'Good'`, or `'High'`|
| `speed`            | speed                    | integer (from `0` to `100`)                              |
| `durability`       | durability               | integer (from `0` to `100`)                              |
| `combat`           | combat skill             | integer (from `0` to `100`)                              |
| `power`            | list of superpowers      | string                                                   |
```

```{margin}
The excerpt from the _dataset_ is generated dynamically, and it may be
necessary to wait a few seconds before it appears, replacing the message
`Please wait, loading PyScript...`. The same behavior occurs everywhere the
browser executes Python code.
```

The dataset is stored in the file `heroes.csv` located in the `data` directory
of the {extlink}`repository <https://github.com/dariomalchiodi/sds>` associated
with the book. In the interactive code, the file is accessible as
`data/heroes.csv`. Its contents are represented using CSV (_comma separated
values_), a standard format commonly used for sharing relatively small datasets:
each row corresponds to a superhero, and in that row the values of the
attributes in {numref}`tab_dataset` are separated by commas. The only
exception is the first row of the file, which contains the names of the
attributes, also separated by commas. {numref}`tab_dataset-excerpt` shows an
excerpt from the _dataset_, displaying the values of some attributes for ten
randomly selected superheroes.


````{customtable}
:name: tab_dataset-excerpt
:class: full-width, left-align


```{interactive-code} python
:height: 300px
:class: toggle-code

import pandas as pd

heroes = pd.read_csv('data/heroes.csv', index_col=0)
    
source = heroes.sample(10).loc[:,'name':'combat']
source.index.name = None
source

```

Excerpt from the reference _dataset_.

````

Later in the book we will see how to load the contents of this file into
memory and analyze them. For now, we will focus on a few preliminary examples.
The one in {numref}`fig_altair-example` is a first example of an interactive
chart. In the upper diagram, some superheroes are represented by circles on a
Cartesian plane: the coordinates of each center indicate weight and height,
while the radius expresses strength. The color varies according to the
publisher, using different shades of blue. Moving the pointer over a circle
reveals the name of the corresponding superhero. The lower diagram instead
shows horizontal bars indicating the number of superheroes for each
publisher/creator. It is possible to select a subset of superheroes by drawing
a rectangle in the upper diagram: the other elements of the _dataset_ are
deactivated and colored gray, and the lower chart is updated to reflect the
distribution of the selected group. The selection can be moved, and clicking
outside it restores the original view.
```{margin}
The chart in {numref}`fig_altair-example` was created with
{extlink}`Altair <https://altair-viz.github.io/>`, a Python library for
creating interactive charts in web pages. A distinctive sign of Altair charts
is the round button with three dots in the top-right corner: it opens a menu
that, among other things, allows the chart to be downloaded.
```

```{code-cell} python
:tags: [remove-cell]

import matplotlib.pyplot as plt
plt.style.use('../_static/sds.mplstyle')
%matplotlib inline
plt.ioff()
```

```{code-cell} python
:height: 600px
:tags: [hide-input]

import altair as alt
import pandas as pd

heroes = pd.read_csv('data/heroes.csv', index_col=0).convert_dtypes()

filter = (heroes['creator'].isin(heroes.creator.value_counts()[:15].index))
filter &= (heroes['weight']<200)
filter &= (heroes['height']<250)
source = heroes[filter].sample(1500)

# Create the selection for brushing
brush = alt.selection_interval()

points = alt.Chart(source).mark_point().encode(
            alt.X('weight', title='Weight'),
            alt.Y('height', title='Height'),
            alt.Size('strength', title='Strength'),
            color=alt.condition(brush, 'creator', alt.value('lightgray')),
            tooltip='name'
        ).add_params(brush)

bars = alt.Chart(source).mark_bar().encode(
            alt.Y('creator', title='Creator'),
            alt.X('count:Q', title='N. of superheroes'),
            alt.Color('creator:N', title='Creator').scale(scheme="blues"),
        ).transform_filter(
            brush
        ).transform_aggregate(
            count='count()',
            groupby=['creator']
        )
# Create the final interactive chart
chart = (points & bars).configure(background='#eaf3f5')
chart
```

````{customfigure}
:name: fig_altair-example
:class: left-align

An example of an interactive chart based on Altair.

````

By interacting with the chart, you can perform an _exploratory analysis_ of
the data, for example in order to answer the following questions.

1. Which publisher/creator has the highest number of superheroes overall?
2. Which publisher has the most superheroes shorter than one meter?
3. Which publisher has the most superheroes weighing between 80 and 100 kg?
4. Who is the tallest superhero of all?

Many aspects can also be analyzed without interacting with the chart, simply by
looking at it in its initial form, as with the two questions below.

5. Is there some kind of trend or relationship linking the weight and height of
   superheroes?
6. Does this relationship change if we focus on superheroes belonging to a
   particular publisher/creator?

```{margin}
If all of this seems complicated, do not worry: the next chapters will explain
these concepts starting from the basics.
```
Questions like these are addressed with the tools of _descriptive statistics_,
introduced in the chapters devoted to that topic. Their goal is to extract
information from a _dataset_ that describes a set of individuals, wholly or in
part. The techniques used can be of two kinds: _qualitative_ or
_quantitative_.

- Qualitative analysis seeks to determine the nature of a certain phenomenon
  (for example, in order to answer questions 5 and 6 in the list above). It
  often relies on graphical tools, whose results must be interpreted and thus
  introduce a certain degree of subjectivity.
- Quantitative analysis, by contrast, produces one or more numerical values,
  which can be compared objectively with other measurements, such as the
  results of other analyses.

For simplicity, let us now focus on the weight of superheroes. The previous
chart is rather crowded: on the one hand it is easy to identify the minimum and
maximum heights, but on the other hand it is not immediately clear whether
«light» superheroes or «heavier» ones are more common. To clarify this point,
we can use a _histogram_, a chart that highlights the frequencies with which
the different weight values appear in the _dataset_.


```{code-cell} python
:height: 400px
:tags: [hide-input]

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
data = heroes.weight[heroes.weight < 200]

ax.hist(data, bins=30, density=True)
fig
```

````{customfigure}
:name: fig_histogram

A histogram of superhero weights.
````

```{margin}
Using a histogram is not always the right choice for exploring data. It is
useful when we have many numerical observations of a continuous attribute; in
other cases, it can be misleading.
```

```{margin}
Looking at the y-axis, we see that the values are not integers, so the height
of the rectangles cannot represent the number of superheroes. In this histogram
it is the area of each rectangle that is proportional to the frequency. That
choice, which has important implications, will be explained in more detail
later in the book.
```
Histograms are explained in detail later in the book, but for now what matters
is how to read one. The chart is made up of many rectangles: the base of each
one corresponds to an interval $I$ of possible weight values, and its height is
related to the fraction of superheroes whose weight falls inside that interval
[^histogram]. Looking at the histogram, we notice two interesting things:

- superheroes who weigh more than $125$ kg are more numerous than those who
  weigh less than $40$ kg;
- if we exclude extreme weights, the distribution is roughly symmetric, with
  the rectangle heights increasing up to around $70$ kg and then decreasing.

This is already a first form of exploratory analysis, even without interactive
charts.

Once enough knowledge about the available data has been gathered, the next step
is to try to _model_ mathematically the process that generated them. To do
that, we need to change perspective: instead of reasoning about the whole
_dataset_, let us imagine that we can observe any one of its elements without
knowing in advance which one it will be (remember [Franklin's
Law](#par_franklin-law)). Let us simply assume that every superhero has the
same chance of being observed as every other. Beginning with
{ref}`chap_combinatorics`, the chapters devoted to _Probability Theory_ provide
rigorous tools for dealing with the uncertainty caused by not knowing which
superhero we will observe each time. We will focus on _events_, that is,
statements about what we might observe. For example, the following are events:

1. we will observe an evil superhero (assuming that moral alignment is fixed,
   defined a priori, and indicated by the `alignment` attribute of the
   dataset);
2. if we observe a Marvel superhero and a DC superhero, the former is faster
   than the latter;
3. if we observe two superheroes who first appeared in the same year, they
   have the same intelligence rating;
4. if we observe ten superheroes, at least one of them belongs to one of the
   _Star Wars_ universes.

We do not know whether these statements are true or false (technically,
whether the corresponding events occur or not): it depends on what we observe.
This is where _probability_ enters the scene. It assigns a number
$p \in [0, 1]$ to quantify that uncertainty. Without going into details for the
moment, uncertainty is greatest when $p$ approaches $\frac{1}{2}$, and it
decreases as $p$ moves toward the extremes. In particular, the closer $p$ is to
zero, the less plausible we should consider the statement, and if $p = 0$ we
know it is false with certainty. Similarly, as $p$ approaches $1$, our
confidence that the statement is true increases, and if $p = 1$ it becomes
certain. We will see that this formalization allows us to compute the
probability of complex events starting from simpler ones. For instance, to
calculate the probability of the last event in the list above, it is enough to
know the probability that a superhero from a _Star Wars_ universe is observed.

Very often, the events we consider refer to one or more numerical quantities
(think, for instance, of a superhero's durability or height: it makes sense to
ask whether it is maximal or whether it falls inside a certain interval). It is
important to stress that the fact that every superhero has the same chance of
being observed does not imply the same for the values those quantities can
take. You can see this easily by looking again at the previous histogram:
weights between $50$ and $100$ kg are much more frequent than weights above one
hundred kilos. It therefore becomes necessary to model these random quantities
too. To that end, we introduce the concept of a _random variable_ and its
mathematical formalization. For now, let us focus on the specific case of
superhero weight, keeping in mind that in general the procedure may be more
complex, or simply different. The idea behind the formalization is to identify
a function $f$, called a _probability density_, whose graph _idealizes_ the
histogram of the observed values, producing a continuous curve that preserves
its main properties. In our example, these properties are symmetry with respect
to a central axis and a _unimodal_ shape (that is, increasing up to a maximum
value and then decreasing). There are infinitely many functions with those two
properties, but for reasons too complex to explain at this stage &mdash; but
which I will clarify later &mdash; I will focus on the one defined by:

```{margin}
In this formula, $\exp(x)$ denotes the constant $\mathrm e$ raised to the
power $x$. I prefer this notation to $\mathrm e^x$ to avoid a fractional
exponent, which would be less readable.
```
```{math}
:label: eq_weight_normal
f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2 \pi}} \;
       \mathrm{exp}\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right) \enspace,
```

```{margin}
The curve we are considering is informally called a _Gaussian bell curve_, and
the resulting model is called a _normal_ model. As we will see, it will play a
fundamental role in the last two parts of the book.
```
where $x$ denotes a generic weight and $f(x; \mu, \sigma)$ returns the
corresponding height in the idealized histogram. It is important to stress that
$f$ has only one argument, denoted by $x$, while $\mu \in \mathbb R$ and
$\sigma \in \mathbb R^+$ are two _parameters_ that must be fixed to define the
function completely. The semicolon serves precisely to distinguish the argument
from the parameters. More precisely, as $\mu$ and $\sigma$ vary,
{eq}`eq_weight_normal` defines a _family_ of functions: each corresponds to a
random variable, and we refer to this family as a _random-variable model_. In
{numref}`fig_normal-model` you can observe how the graph of $f$ changes as its
parameters vary. By moving the two sliders associated with $\mu$ and $\sigma$,
you will immediately see how the graph of $f$ updates in response to the new
settings.


````{customfigure}
:name: fig_normal-model
:class: left-align


```{interactive-code} python
:tags: [toggle-code]

import asyncio
import matplotlib.pyplot as plt
import numpy as np
from js import document
from pyscript import display
from pyscript.web import page, when

mu = float(page['#pdf-mu-slider'][0].value)
sigma = float(page['#pdf-sigma-slider'][0].value)

x = np.linspace(0, 200, 400)
y = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

fig_pdf, ax_pdf = plt.subplots()
curve_pdf, = ax_pdf.plot(x, y, alpha=0.5, color='tab:blue')


ax_pdf.set_xlabel('$x$', fontsize=12, ha='right')
#ax.xaxis.set_label_coords(1.07, 0.03)
ax_pdf.set_ylabel('$f$', fontsize=12, rotation=0)
#ax.yaxis.set_label_coords(0., 1.09)
ax_pdf.set_xlim(0, 200)
ax_pdf.set_ylim(0, 0.02)

@when("input", "#pdf-mu-slider, #pdf-sigma-slider")
def pdf_plot(event):

    mu = float(page['#pdf-mu-slider'][0].value)
    sigma = float(page['#pdf-sigma-slider'][0].value)
    page['#pdf-mu-value'][0].innerHTML = f'{mu:.1f}'
    page['#pdf-sigma-value'][0].innerHTML = f'{sigma:.1f}'

    y = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) /
        sigma) ** 2)
    curve_pdf.set_data(x, y)
    display(fig_pdf, target='graph-%this%', append=False)

display(fig_pdf, target='graph-%this%', append=False)
```

```{raw} html
<div class="plot-container">
    <div class="model-slider-container">
        <label for="pdf-mu-slider">\(\mu\): </label>
        <input type="range" id="pdf-mu-slider"
               min="10" max="200" value="150" step="0.1" />
        <span id="pdf-mu-value">150</span>
    </div>

    <div class="model-slider-container">
        <label for="pdf-sigma-slider">\(\sigma\): </label>
        <input type="range" id="pdf-sigma-slider"
               min="0.1" max="50" value="33" step="0.1" />
        <span id="pdf-sigma-value">33.0</span>
    </div>
</div>
```

Graph of the probability density described by {eq}`eq_weight_normal`.
````

One of the reasons we speak of a «model for a random variable» is that it is
possible to choose the values of its parameters so as to _fit_ the probability
density function, and more generally the corresponding random variable, to data
that have already been observed. In the case we have just seen, this means
choosing suitable values for $\mu$ and $\sigma$ so that the graph of $f$
qualitatively overlaps the histogram initially obtained for weight. The
interactive chart in {numref}`fig_adapt-model` allows you to carry out this
operation manually, by moving the sliders in order to find a qualitative
alignment between the two graphs.

```{interactive-code} python
:height: 0px
:class: no-output

data = heroes['weight'][heroes['weight'] < 200].dropna()
```

````{customfigure}
:name: fig_adapt-model
:class: left-align

```{interactive-code} python
:height: 400px
:class: toggle-code

mu = float(page['#model-mu-slider'][0].value)
sigma = float(page['#model-sigma-slider'][0].value)

x = np.linspace(0, 200, 400)
y = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

fig, ax = plt.subplots()
ax.hist(data, bins=30, density=True, alpha=0.3, color='tab:blue')
curve, = ax.plot(x, y, alpha=0.5, color='tab:blue')

ax.set_xlabel(r'$x$', fontsize=12, ha='right')
ax.xaxis.set_label_coords(1.07, 0.03)
ax.set_ylabel(r'$f$', fontsize=12, rotation=0)
ax.yaxis.set_label_coords(0., 1.09)
ax.set_xlim(0, 200)
ax.set_ylim(0, 0.02)

@when("input", "#model-mu-slider, #model-sigma-slider")
def model_plot(event):

    mu = float(page['#model-mu-slider'][0].value)
    sigma = float(page['#model-sigma-slider'][0].value)
    page['#model-mu-value'][0].innerHTML = f'{mu:.1f}'
    page['#model-sigma-value'][0].innerHTML = f'{sigma:.1f}'

    y = (1 / (sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
    curve.set_data(x, y)
    display(fig, target='graph-%this%', append=False)

display(fig, target='graph-%this%', append=False)
    
```

```{raw} html
<div class="plot-container">
    <div class="model-slider-container">
        <label for="model-mu-slider">\(\mu\): </label>
        <input type="range" id="model-mu-slider"
               min="10" max="200" value="150" step="0.1" />
        <span id="model-mu-value">150</span>
    </div>

    <div class="model-slider-container">
        <label for="model-sigma-slider">\(\sigma\): </label>
        <input type="range" id="model-sigma-slider"
               min="0.1" max="50" value="33" step="0.1" />
        <span id="model-sigma-value">33.0</span>
    </div>
</div>
```

Superposition of the graph of the density described by
{eq}`eq_weight_normal` on the histogram in {numref}`fig_histogram`. By moving
the sliders, it is possible to find parameter values that fit the model to the
histogram.
````

In the final part of the book, we will see that there are several methods for
determining a model's parameters automatically, so as to adapt it to a set of
data. This is one of the aims of _inferential statistics_. The starting point
is always a _dataset_, which in this context represents a _sample_ of
observations taken from a broader _population_. We want to make hypotheses
about that population or draw conclusions regarding it, even though we cannot
observe it in its entirety. In other words, we use the sample to obtain
information about what we do not know about the population. The simplest case
&mdash; and also the one on which we will focus most &mdash; is the one in which
the population is described by a random variable associated with a model that
depends on one or more unknown parameters. The objective is to approximate
those parameters, or other quantities that depend on them. For example,
consider the population of superheroes in our _dataset_ and suppose we are
interested in their average weight $p$. If we have only a sample of one hundred
superheroes at our disposal, common sense suggests using the average of their
weights as an approximation of $p$. In general, we call an _estimator_ the
function applied to the sample to obtain approximations of this kind. In our
example, the estimator is the arithmetic mean of the sample values, called the
_sample mean_. {numref}`fig_statistics-variability` shows how the values of
this estimator vary when ten different samples are drawn.

````{customtable}
:name: fig_statistics-variability
:class: left-align

```{interactive-code} python
:height: 100px
:class: toggle-code

weights = heroes['weight'][heroes['weight']<200].dropna()

def sample_mean(weights, n=100):
    sample = weights.sample(n)
    return sample.mean().round(2)

num_samples = 10
means = [sample_mean(weights) for _ in range(num_samples)]
pd.DataFrame([means],
             columns=[f'#{i}' for i in range(1, num_samples+1)],
             index=['Mean weight'])

```

Value of the sample mean for superhero weight, calculated on ten different
samples drawn from the population.
````

It is natural that the sample means obtained from the ten samples differ from
one another, since every sample is different. Nevertheless, the results do not
vary drastically and tend to cluster around $79$, which is a good
approximation of the correct value for the mean weight of all superheroes (as
you can verify by looking at the previous histogram). But can we be certain
that the sample mean is really the best possible estimator? And, more generally,
how can we assess the quality of an estimator while taking into account the
intrinsic variability we have just highlighted? These questions will find their
answer in the part devoted to inferential statistics. In a certain sense, that
part allows me to finish the book by «closing the circle»: both because it
puts into synergistic practice what we have seen in descriptive statistics and
probability theory, and because it allows us to understand more deeply the
power of some of the concepts and tools already encountered &mdash; perhaps in
a relatively informal way &mdash; in the preceding parts.

Before beginning with descriptive statistics, however, it is important to
review some fundamental concepts of computer programming and, above all, to
become comfortable with the computational tools I will use throughout the book.
That is the purpose of the opening chapters on Python and pandas, with which
the discussion begins.

## Exercises

At the end of almost every paragraph, a few exercises are provided. Their
difficulty is indicated by the number of dots in parentheses.

```{exercise} •
Download the superhero dataset from the book's
{extlink}`repository <https://github.com/dariomalchiodi/sds>` and import it
into any spreadsheet program (all the most common ones can import CSV files),
so that each column contains a different attribute. Focus on, say, the first
thirty rows and consider the columns separately, in order to get an idea of
how the values associated with the individual attributes vary.
```

```{margin}
Being a _data scientist_ means not only combining skills in probability,
statistics, and programming, but also mastering various _scripting_ tools for
converting, adapting, and cleaning data. Those tools are often used via a
terminal and its shell. Depending on the professional setting, data may be
available in forms that are more or less structured, and handling them can
require complex procedures, sometimes involving representations other than CSV
or articulated databases.
```
````{exercise} •••
Reconsider the previous exercise, looking at the contents of each individual
column of the CSV file without using a spreadsheet program, but only a
terminal and shell commands.
````

```{exercise} ••
Based on the idea you have formed of the superhero dataset while solving the
previous exercises, try dividing the attributes into homogeneous groups based
not on the type of data used to represent the corresponding values (as
indicated in the «Content» column of {numref}`tab_dataset`), but on the
_nature_ of the attributes themselves.
```

```{exercise} •
Answer questions 1 to 4 in the list that follows the first interactive chart.
```

```{exercise} ••
Answer questions 5 and 6 in the list following the first interactive chart.
Write down the reasoning you followed.
```

```{exercise} ••
Formulate other questions about the dataset that can be answered using the
first interactive chart. Again, write down the reasoning needed to answer
them.
```

````{exercise} •
Consider the following values

```{math}
\{13, 8, 7, 4, 9, 8, 4, 4, 19, 2, 5, 3, 3, 1, 12 \}
```

and draw the corresponding histogram by hand, calculating the height of each
rectangle as the number of values that fall in the corresponding interval, and
using the following reference intervals: $[0, 5)$, $[5, 10)$, $[10, 15)$,
$[15, 20)$. Compare the shape of the resulting chart with the one shown in the
text, highlighting the main differences.
````

```{exercise} •
Write ten possible events concerning the superhero dataset.
```

```{exercise} ••
Write an event whose probability is zero. Then write one whose probability is
$1$.
```

```{exercise} ••
Set $\mu = \sigma = 1$ and study the function described in
{eq}`eq_weight_normal`, drawing the corresponding graph by hand and verifying
that the shape matches what is shown in the second interactive chart.
```

```{exercise} •
Based on the result of the previous exercise, and taking into account what you
experienced using the second interactive chart, what is the role of parameters
$\mu$ and $\sigma$ in the graph of $f$ defined in {eq}`eq_weight_normal`?
```

```{exercise} •
Using the second interactive chart, determine values for $\mu$ and $\sigma$
that allow the graph of $f$ to reasonably overlap with the histogram of
superhero weights.
```

```{exercise} ••
Write down the reasoning you used to convince yourself that $79$ is
approximately the mean superhero weight.
```

[^histogram]: The bins defining the bases of histogram bars can be chosen with
some flexibility. For simplicity, the histogram in the text was generated using
thirty equal-width intervals covering all possible weight values. Depending on
the context, it may make sense to use a larger number (or a smaller one) of
such intervals, or to use intervals with different widths.