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

(sec:overview)=
# An Overview

The aim of this chapter is twofold: on the one hand, it serves to broadly
outline the logical structure behind the organization of the content and to
introduce the key concepts in a relatively informal way; on the other hand,
it explains how to use the interactive components of the book. As mentioned
in {ref}`chap:approach`, throughout the text I will refer to a dataset obtained
by modifying a suitable subset of the
[Superhero database](http://www.superherodb.com). The examples will therefore
refer to the world of superheroes, each of whom is described through the
_attributes_ listed in {numref}`tab:dataset`.

```{table} Description of the dataset used in the examples.
:name: tab:dataset
:align: center
| Attribute           | Meaning                    | Content                                                  |
|---------------------|----------------------------|----------------------------------------------------------|
| `name`              | unique identifier          | string                                                   |
| `full_name`         | full name                  | string                                                   |
| `identity`          | secret identity            | string                                                   |
| `alignment`         | moral alignment            | `'Good'`, `'Neutral'`, or `'Bad'`                        |
| `place_of_birth`    | place of birth             | string                                                   |
| `creator`           | publisher/creator          | string                                                   |
| `universe`          | universe                   | string                                                   |
| `first_appearance`  | year of first appearance   | integer                                                  |
| `eye_color`         | eye color                  | string                                                   |
| `hair_color`        | hair color                 | string                                                   |
| `height`            | height in cm               | floating-point number                                    |
| `weight`            | weight in kg               | floating-point number                                    |
| `strength`          | strength                   | integer (from `0` to `100`)                              |
| `intelligence`      | intelligence               | `'Low'`, `'Moderate'`, `'Average'`, `'Good'`, or `'High'`|
| `speed`             | speed                      | integer (from `0` to `100`)                              |
| `durability`        | durability                 | integer (from `0` to `100`)                              |
| `combat`            | combat skills              | integer (from `0` to `100`)                              |
| `powers`            | list of superpowers        | string                                                   |
```

```{margin}
The dataset excerpt is generated dynamically, and it may take a few seconds for
it to appear, replacing the message `Please wait, loading PyScript...`. The
same applies to all other points where the browser needs to execute Python
code.
```

The dataset is stored in the file `heroes.csv` located in the `data` directory
of the [repository](https://github.com/dariomalchiodi/sds) associated with the
book. In the interactive code, the file can be accessed as `data/heroes.csv`.
This file uses the CSV (comma-separated values) format, a standard format used
for sharing relatively small datasets: each line represents a superhero, and
the values of the attributes listed in {numref}`tab:dataset` are separated by
commas. The only exception is the first line of the file, which contains the
attribute names, also separated by commas, as can be seen when previewing the
start of the file.

Below, you can see a description of some of the attributes for ten superheroes
randomly selected from the dataset.


```{code-block} python
:class: toggle-code
import pandas as pd

heroes = pd.read_csv('data/heroes.csv', index_col=0).convert_dtypes()
    
source = heroes.sample(10).loc[:,'name':'combat']
source.index.name = None
source
```

In {ref}`chap:pandas`, we will see how to load the contents of this file into
memory and, more importantly, how to process them. For now, let’s focus on a
few simple examples that, on the one hand, demonstrate how to use the
interactive parts of the book and, on the other, provide an overview of the
concepts that will be discussed.

What follows is a first example of an interactive chart. In the upper diagram,
several superheroes are represented using circles on a Cartesian plane: the
coordinates of the center indicate weight and height, while the radius
expresses strength. Each circle is shaded in blue according to the publisher,
and hovering over it automatically displays the corresponding superhero’s name.
The lower diagram shows the number of superheroes for each publisher/creator
using horizontal bars. By selecting a rectangular area in the upper diagram,
you can focus on a subset of superheroes (the circles representing excluded
superheroes will be grayed out): the lower diagram is automatically regenerated
to reflect the distribution of the selected group. Once made, the selection can
be moved, and clicking anywhere outside it will restore the original chart.

```{margin}
The chart next to this paragraph was created using
[altair](https://altair-viz.github.io/), a library that allows the use of
Python to render complex charts within web pages in an interactive format that
is automatically activated when the page loads. To recognize whether a chart
was generated with altair, simply check if there’s a round button with three
dots at the top right. This button opens a menu that allows, among other
things, to download the chart.
```


```{code-block} python
:class: toggle-code

import altair as alt

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
            alt.X('count(creator)', title='N. of superheroes'),
            alt.Color('creator', title='Creator').scale(scheme="blues"),
        ).transform_filter(brush)

# Create the final interactive chart
chart = (points & bars).configure(background='#eaf3f5')
chart
```

By interacting with the chart, you can perform an _exploratory analysis_ of
the data, for instance to answer the following questions.

1. Which publisher/creator has the highest number of superheroes overall?
2. Which publisher has the most superheroes shorter than one meter?
3. Which publisher has the most superheroes weighing between 80 and 100 kg?
4. Who is the tallest superhero of all?

```{margin}
In general, only a small portion of the charts we will see are interactive.
```

Of course, many aspects can be analyzed preliminarily just by looking at the
chart as it was generated (i.e., without using the interactive components),
such as the two below.

5. Is there some kind of trend or relationship linking the weight and height of
   superheroes?
6. Does this relationship change if we focus on superheroes belonging to a
   particular publisher/creator?

_Descriptive statistics_, introduced from {ref}`chap:dati-e-informazione` to
{ref}`chap:analizzare-le-relazioni-tra-i-dati`, provides tools to answer
questions like those just listed. In general, the goal is to extract
information from a dataset that describes, either globally or partially, a
group of reference individuals. The techniques used can be either _qualitative_
or _quantitative_ in nature. We refer to qualitative analysis when the goal is
to determine the nature of a certain phenomenon (for example, to answer
questions 5 or 6 above). This often requires the use of tools—like the chart
previously shown&mdash;whose results must be interpreted, introducing a certain
degree of subjectivity. Quantitative analysis, on the other hand, refers to
cases where the outcome is expressed in one or more numerical values, which can
then be objectively compared with other quantities (typically, the results of
other analyses).

```{margin}
If all of this sounds complicated, don’t worry: the concepts will become
clearer in the following chapters.
```

Now suppose we want to focus, for simplicity, on the superheroes’ weight: the
previous chart is quite full of circles, and while it’s relatively easy to get
a sense of the smallest and largest heights, it becomes less clear, for
example, whether there are superheroes who wheigh less or more in kilograms.
To get a better understanding, I present below a specific chart, called a
_histogram_, which highlights the frequencies with which different weight
values appear in the dataset.

```{code-block} python
:class: toggle-code

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
data = heroes.weight[heroes.weight < 200]

ax.hist(data, bins=30, density=True)
fig.show()
```

```{margin}
It doesn’t always make sense to use a histogram to explore values in a
_dataset_, as we’ll see in {ref}`chap:dati-e-informazione`.
```

```{margin}
We will also see that the exploration process doesn’t necessarily (or
exclusively) involve the use of graphical methods&mdash;it can also be based on
quantitative tools (and typically is).
```

Histograms are defined in detail in {ref}`sec:istogrammi`, but for now it’s
enough to understand how to read the result: in each of the shown bars, the
base identifies an interval $I$ (called a _bin_) of possible weight values for
superheroes, and the height is related to the fraction of superheroes whose
weight falls within $I$ [^histogram]. The resulting chart highlights some
interesting aspects: for example, it shows that there are more superheroes
weighing over 125 kg than those weighing less than forty kilos. On the other
hand, if we ignore the very large or very small weights, a rough symmetry
appears around a central axis, along with the fact that the bar heights tend to
increase up to approximately $70$ kg and then decrease. This too is a form of
data exploration, which in this case doesn’t require interactive charts.

```{margin}
If you’ve been paying attention, you’ll have noticed that the height of a bar
can’t be equal to the number of superheroes with a certain weight, because the
values shown on the y-axis are not integers. In this histogram, in fact, the
number of superheroes is tied to the area of the bar. This will soon allow us
to compare the result with another chart. The reason for this choice is
explained in {ref}`sec:istogrammi`.
```

Once enough knowledge about the available data has been gathered, the next
step typically involves _modeling_ the process that generated it. To do this,
we need to radically shift our perspective: instead of reasoning in terms of
the entire dataset, we now pose questions about observing one of its elements,
or a group of elements, under the assumption that we don’t know in advance
what we’ll observe (remember [Franklin's Law](#par:franklin-law)). We also
assume that each superhero has the same chance of being observed as any other.
Starting from {ref}`{chap:calcolo-combinatorio}` through
{ref}`chap:va-e-modelli-continui`, the book discusses _Probability Theory_,
providing formal tools to deal with uncertainty that stems from not knowing
what will be observed.

More specifically, we will focus on _events_, understood as statements
concerning the outcome of observations. Still thinking about superheroes, the
following are examples of events:

1. a superhero is bad (under the assumption that each superhero has a
   predefined moral alignment, as indicated by the `alignment` attribute in our
   dataset);
2. a Marvel superhero is faster than a DC superhero;
3. two superheroes who debuted in the same year have the same intelligence
   rating;
4. at least one superhero in a group of ten belongs to a _Star Wars_ universe.

Clearly, we don’t know in advance whether the statement that constitutes an
event is true or false, because its truth value depends on what is actually
observed. For this reason, we introduce the key concept of _probability_,
understood as a numerical quantification of this uncertainty using a number
$p \in [0, 1]$. Without going into detail for now, the closer this number is to
$\frac{1}{2}$, the higher the uncertainty; conversely, the closer $p$ gets to
the extremes, the lower the uncertainty becomes. As $p$ approaches zero, our
confidence in the truth of the statement decreases until, when $p = 0$, the
statement is definitely false. Similarly, as $p$ approaches one, our confidence
increases, and when $p = 1$, the statement is definitely true. As we’ll see,
the advantage of mathematically formalizing the concept of probability is that
it enables us to develop techniques to compute the probability of complex
events based on the probability of simpler ones. This is the case for item 4
above, where the desired probability can be determined once we know the
probability that a single hero comes from a _Star Wars_ universe.

Very often, the events we consider refer to one or more numerical quantities
(as in examples 2 and 3 above): it makes sense, for instance, to ask whether
the durability of a superhero is at its maximum, or whether the height falls
within a given interval. It’s important to note that the fact that each
superhero has the same chance of being observed as any other does not mean the
same applies to the values those quantities can take. You can easily realize
this by revisiting the earlier histogram: weights between $50$ and $100$ kg are
much more frequent than weights over one hundred kilos. Therefore, it becomes
important to model these random quantities as well. To do that, we introduce
the concept of a _random variable_ and its mathematical formalization. Without
going into details for now, let’s focus on the specific case of superhero
weight, keeping in mind that in general the process might be more complex or
simply different. The underlying idea of the formalization is to identify a
function $f$, called the _probability density function_, whose graph
_idealizes_ the histogram of the observed values while preserving its key
properties. In this case, we can identify those properties as being symmetric
around a central axis and having a _unimodal_ trend (i.e., increasing up to a
maximum and decreasing afterwards). There are infinitely many functions that
display these two properties, but for reasons that are currently too advanced
to justify&mdash;but which should become clear after reading the rest of the
book&mdash;it’s worth focusing on the one defined by:

```{margin}
In this formula, $\exp(x)$ indicates the exponential of the constant
$\mathrm e$ raised to the power $x$: this form is preferred over $\mathrm e^x$
to avoid fractional exponents, which would be harder to read.
```
```{math}
:label: eq:weight_normal
f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2 \pi}} \;
       \mathrm{exp}\left(-\frac{(x - \mu)^2}{2 \sigma^2}\right) \enspace,
```

where $x$ denotes a generic weight and $f(x; \mu, \sigma)$ identifies the
corresponding height value in the idealized histogram. It is important to
highlight that $f$ has a single argument, denoted by $x$, while
$\mu \in \mathbb R$ and $\sigma \in \mathbb R^+$ should be understood as two
_parameters_: the function is fully defined only once their values have been
set. The semicolon in the definition of $f$ is precisely meant to emphasize the
different roles of the argument on one hand and the parameters on the other.
More precisely, {eq}`eq:weight_normal` defines, as $\mu$ and $\sigma$ vary, a
_family_ of functions, each of which is associated with a random variable. The
result is a family of random variables, commonly referred to as a
_random variable model_. In the interactive diagram shown below, you can
observe how the graph of $f$ changes when its two parameters vary. By adjusting
the two sliders, corresponding to $\mu$ and $\sigma$, you can change the values
of the respective parameters and simultaneously see how the graph of $f$ is
affected.

```{code-block} python
:class: toggle-code 
import numpy as np
from js import document
from pyodide.ffi import create_proxy
import pyscript as pys
import io
import base64

def plot_pdf(mu, sigma):
    x = np.linspace(-10, 10, 400)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    fig, ax = plt.subplots()
    ax.fill_between(x, 0, y, alpha=0.5, color='tab:blue')

    # Use plain text label to avoid MathJax processing
    ax.set_xlabel('x', fontsize=12, ha='right')
    ax.xaxis.set_label_coords(1.07, 0.03)
    ax.set_xlim(-10, 10)
    ax.set_ylim(0, 1)
    
    # Manual rendering to avoid MathJax processing
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format='png', bbox_inches='tight', dpi=100)
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    img_buffer.close()
    
    # Display in protected div
    img_html = '<div class="no-mathjax"><img src="data:image/png;base64,' + img_base64 + '" style="max-width: 100%; height: auto;" /></div>'
    Element("pdf-output").write(img_html)
    
    plt.close(fig)

def update_plot(event=None):
    mu = float(document.getElementById("mean-slider").value)
    sigma = float(document.getElementById("std-slider").value)
    document.getElementById("mean-value").innerText = f"{mu:.1f}"
    document.getElementById("std-value").innerText = f"{sigma:.1f}"
    plot_pdf(mu, sigma)


mean_slider = document.getElementById("mean-slider")
std_slider = document.getElementById("std-slider")

mean_slider.addEventListener("input", create_proxy(update_plot))
std_slider.addEventListener("input", create_proxy(update_plot))

# Initial plot
plot_pdf(0, 1)
```
```{raw} html

<div id="plot-container" style="visibility: none;">
    <div class="slider-container" style="float: left;">
        <label for="mean-slider">$\mu$: </label>
        <input type="range" id="mean-slider"
               min="-5" max="5" value="0" step="0.1" />
        <span id="mean-value">0</span>
    </div>

    <div class="slider-container" style="float: right;">
        <label for="std-slider">$\sigma$: </label>
        <input type="range" id="std-slider"
               min="0.1" max="5" value="1" step="0.1" />
        <span id="std-value">1.0</span>
    </div>

    <div id="pdf-output" class="no-mathjax"
            style="clear: both; display: flex; justify-content: center; margin-bottom: 2em;">
        <div class="splash"></div>
    </div>
</div>
```

One of the reasons why we refer to a «random variable model» is that it’s
possible to choose the values of its parameters in order to _fit_ the graph of
$f$, and more generally the corresponding random variable, to previously
observed data. In the case we just saw, this means selecting appropriate values
for $\mu$ and $\sigma$, so that the graph of $f$ qualitatively overlaps with
that of the histogram initially obtained for weight. The interactive diagram
below allows you to perform this operation manually: you can use the sliders to
achieve a good overlap between the histogram and the probability density
function.

```{code-block} python
:class:  toggle-code

import base64
import io

def model_plot_pdf(mu, sigma):
    x = np.linspace(0, 200, 400)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, density=True, alpha=0.3, color='tab:blue')
    ax.fill_between(x, 0, y, alpha=0.5, color='tab:blue')

    # Use plain text for axis labels to avoid MathJax interference
    ax.set_xlabel('x', fontsize=12, ha='right')
    ax.xaxis.set_label_coords(1.07, 0.03)
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 0.02)
    
    # Convert plot to base64 string for display
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', dpi=100)
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode()
    plt.close(fig)
    
    # Display in no-mathjax container
    output_html = f'''
    <div class="no-mathjax" style="display: flex; justify-content: center; margin-bottom: 2em;">
        <img src="data:image/png;base64,{img_base64}" alt="Model Plot" style="max-width: 100%; height: auto;">
    </div>
    '''
    
    target_element = document.getElementById("model-output")
    if target_element:
        target_element.innerHTML = output_html
    else:
        print("Target element 'model-output' not found")

def model_update_plot(event=None):
    try:
        mu = float(document.getElementById("model-mean-slider").value)
        sigma = float(document.getElementById("model-std-slider").value)
        document.getElementById("model-mean-value").innerText = f"{mu:.1f}"
        document.getElementById("model-std-value").innerText = f"{sigma:.1f}"
        model_plot_pdf(mu, sigma)
    except Exception as e:
        print(f"Error updating plot: {e}")

# Wait for DOM to be ready
def setup_model_sliders():
    try:
        model_mean_slider = document.getElementById("model-mean-slider")
        model_std_slider = document.getElementById("model-std-slider")
        
        if model_mean_slider and model_std_slider:
            model_mean_slider.addEventListener("input", create_proxy(model_update_plot))
            model_std_slider.addEventListener("input", create_proxy(model_update_plot))
            
            # Initial plot
            model_plot_pdf(150, 33)
            print("Model sliders setup complete")
        else:
            print("Model slider elements not found, retrying in 100ms...")
            import asyncio
            asyncio.get_event_loop().call_later(0.1, setup_model_sliders)
    except Exception as e:
        print(f"Error setting up model sliders: {e}")

# Setup sliders when DOM is ready
setup_model_sliders()
```
```{raw} html

<div id="plot-container" style="visibility: none;">
    <div class="model-slider-container" style="float: left;">
        <label for="model-mean-slider">Mean ($\mu$): </label>
        <input type="range" id="model-mean-slider"
               min="10" max="200" value="150" step="0.1" />
        <span id="model-mean-value">150</span>
    </div>

    <div class="model-slider-container" style="float: right;">
        <label for="model-std-slider">Standard Deviation ($\sigma$): </label>
        <input type="range" id="model-std-slider"
               min="0.1" max="50" value="33" step="0.1" />
        <span id="model-std-value">33.0</span>
    </div>

    <div id="model-output" style="clear: both; display: flex; justify-content: center; margin-bottom: 2em;">
        <div class="splash"></div>
    </div>
</div>
```

In the final part of the book, we’ll explore several methods that allow us to
automatically determine the parameters of a model, so that it fits a given
dataset. This is one of the goals of _inferential statistics_, which we’ll
cover from {ref}`chap:inferential_statistics` through to
{ref}`chap:statistica-non-parametrica`. The starting point is always a dataset,
which in this context represents a _sample_ of observations taken from a larger
_population_. Our aim is to formulate hypotheses or draw conclusions about
this population&mdash;even if we can’t observe it directly in full. In other
words, we’ll use the sample to learn something about what we don’t know about
the population.

The simplest case&mdash;and the one we’ll focus on the most&mdash;is when the
population can be described by a random variable, associated with a model that
depends on one or more unknown parameters. The goal is to estimate these
parameters, or other quantities that depend on them. For instance, let’s
imagine that the population consists of all the superheroes in our dataset, and
the quantity we care about is their average weight $w$. If we only have a
sample of one hundred superheroes, it makes sense to use the average of their
weight as an approximation of $w$. In general, we use the term _estimator_ to
refer to the function that is applied to the sample in order to compute
approximations of this kind. In our example, the estimator is simply the
arithmetic mean of the sample values&mdash;what we call the _sample mean_. The
table below shows how the values of this estimator change across ten different
random samples.

```{code-block} python
:class:  toggle-code

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

As you can see, the sample means vary from one sample to the next, which is
expected&mdash;after all, each sample is different. Still, the results aren’t
all over the place: they tend to cluster around 79, which is a pretty good
estimate of the true average strength of all superheroes (as you can check by
looking at the earlier histogram). But can we be sure that the sample mean is
really the best estimator available? And more generally, how do we evaluate how
«good» an estimator is, especially considering the kind of variability we just
observed?

We’ll tackle these kinds of questions in the section on inferential statistics.
In a way, this part lets me wrap up the book and «close the loop»: not only
does it bring together what we’ve seen in descriptive statistics and
probability theory, but it also helps us better appreciate the full power of
some of the concepts and tools we encountered&mdash;perhaps in a more informal
way&mdash;earlier in the book.

But before diving into descriptive statistics, it’s important to review some
key concepts from computer programming, and above all to get comfortable with
the computational tools I’ll be using throughout the book. That’s the purpose
of {ref}`chap:intro-python` and {ref}`chap:pandas`, which open the
discussion.

## Exercises

At the end of each paragraph, a few exercises are proposed, with their
difficulty indicated by the number of dots in parentheses.

```{exercise} •
Download the superheroes dataset from the book's
[repository](https://github.com/dariomalchiodi/sds) and import it into any
spreadsheet application (all major ones support importing CSV files), so that
each column contains a different attribute. Focus on, say, the first thirty
rows and examine the individual columns separately to get a sense of how the
values associated with each attribute vary.
```

```{margin}
Being a _data scientist_ means not only combining skills in probability,
statistics, and programming, but also mastering various scripting tools that
allow you to convert, adapt, and clean data: quite often, these tools are
operated via a terminal and its corresponding shell.
```

```{exercise} •••
Revisit the previous exercise, inspecting the contents of each individual
column of the CSV file without using a spreadsheet application, but only a
terminal and shell commands.
```

```{exercise} ••
Based on the impression you’ve formed of the superhero dataset while solving
the previous exercises, try grouping the attributes into homogeneous sets, not
based on the type of data used to represent the corresponding values (as
indicated in the «Content» column of {numref}`tab:dataset`), but rather on the
_nature_ of the attributes themselves.
```

```{exercise} •
Answer questions 1 to 4 in the list that follows the first interactive chart.
```

```{exercise} ••
Answer questions 5 and 6 in the list following the first interactive chart.
Write down your reasoning.
```

```{exercise} ••
Think of other questions about the dataset that could be answered using the
first interactive chart. Again, write down the reasoning needed to answer them.
```

```{exercise} •
Consider the following values

$$ \\{13, 8, 7, 4, 9, 8, 4, 4, 19, 2, 5, 3, 3, 1, 12 \\} $$

and manually draw the corresponding histogram, calculating the height of each
bar as the number of values that fall within the corresponding interval, using
the following bins: $[0, 5)$, $[5, 10)$, $[10, 15)$, $[15, 20)$. Compare the
shape of your graph to what’s shown in the text, highlighting the main
differences.
```

```{exercise} •
Write ten possible events concerning the superheroes dataset.
```

```{exercise} ••
Write an event whose probability is zero. Then write one whose probability is
$1$.
```

```{exercise} ••
Set $\mu = \sigma = 1$ and study the function described in
{eq}`eq:weight_normal`, drawing the corresponding graph by hand and verifying
that the shape matches what is shown in the second interactive chart.
```

```{exercise} •
Based on the result of the previous exercise, and taking into account what you
experienced using the second interactive chart, what is the role of parameters
$\mu$ and $\sigma$ in the graph of $f$ defined in {eq}`eq:weight_normal`?
```

```{exercise} •
Using the second interactive chart, determine values for $\mu$ and $\sigma$
that allow the graph of $f$ to reasonably overlap with the histogram of
superhero weights.
```

```{exercise} ••
Write down the reasoning you used to convince yourself that $79$ is
approximately the average superhero weights.
```


[^histogram]: The bins defining the bases of histogram bars can be chosen with
some flexibility. For simplicity, the histogram in the text was generated using
twenty-five equal-width intervals that cover all possible weight values, but
depending on the context, it may make sense to use more (or fewer) such
intervals, or even intervals of different widths.
