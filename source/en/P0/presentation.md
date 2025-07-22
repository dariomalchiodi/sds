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

(par:franklin-law)=
# Presentation

> In this world, nothing can be said to be certain,<br/>
> except death and taxes
>
> -- Benjamin Franklin

The quote that begins this paragraph is translated from a letter written in
1789 by Benjamin Franklin (see {numref}`benjamin-franklin`), one of the
founding fathers of the United States of America. If we accept this saying,
often referred to as the _Franklin’s law_ [^franklin-citation], it is worth
studying uncertainty, because practically everything is uncertain (ironically,
the validity of Franklin’s law itself should not be taken for granted: just
think, for example, of the phenomenon of tax evasion, or the fact that those
who reside in the Principality of Monaco do not pay taxes).

```{figure} https://live.staticflickr.com/2869/9544834557_b844c48e78_b.jpg
:width: 70%
:name: benjamin-franklin

Depiction of Benjamin Franklin on the United States 100-dollar bills
(image by E. Strauhmanis, distributed under
  [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/))
```

In reality, the concept of _uncertainty_ is particularly difficult to define,
because it is highly multifaceted and takes on different nuances depending on
the context. In this book, we will focus on a particular incarnation of this
concept, which we will call _randomness_. In simple terms (and therefore
definitely open to improvement), we can identify randomness as the property
that characterizes any experience that, even if repeated under the same
conditions, does not have a determinable result a priori. In a (for now)
informal way, we call _events_ the statements concerning the outcomes of these
experiences. The truth value of these statements will therefore be uncertain.
A classic example of an event is the outcome of rolling dice when playing
Monopoly. Another equally classic but more modern example concerns the closing
value of a stock index. If we reflect more attentively, many other examples 
to mind: if we look at the sky in the morning and see clouds on the horizon,
will it rain today? How many grandchildren will my neighbor’s sister have? Next
year, will I be able to get through the cold season catching the flu at most
once? Indeed, it is not difficult to convince ourselves that randomness (or, if
you prefer, non-determinism) permeates our existence, to the point of playing a
fundamental role in the description of some fundamental aspects of Nature,
such as the theory of evolution or quantum mechanics.

Despite this, people learn more or less quickly to live quite well with
uncertainty: when leaving home, most of the time we know when it is wise to
take an umbrella with us, and some people even manage to speculate successfully
in the stock market. This happens because we are able to _assess_ the
uncertainty of many events, accepting the _risk_ that our assessment entails
(returning to the example of the cloudy sky, the risk is either carrying an
umbrella unnecessarily or not carrying it and ending up in the rain). Almost
always, we do all this largely subjectively, based on our _experience_.
Mathematics, however, provides us with qualitative and quantitative tools to
address this problem rigorously. In particular, by combining _probability
calculus_ and _statistics_, we can model the uncertainty of events and evaluate
it using the experience we have acquired.

The purpose of this book is precisely to provide the foundations of these two
branches of mathematics, using an interactive approach centered on data
analysis, suitable especially for students who have already developed skills in
computer programming. In particular, the content has been designed for students
enrolled in undergraduate computer science programs, but it is certainly
suitable for all educational contexts that include at least one compulsory
programming course.

The work is organized into four parts:

- The first introduces the Python programming language and the main libraries
  currently used to analyze data (the so-called _Python data science stack_);
- The second addresses the topic of _descriptive statistics_, which we can
  informally relate to the problem of organizing observations of a phenomenon,
  then analyzing them in order to extract _information_ (the basis of the
  experience mentioned above);
- The third introduces the foundations of _probability theory_, understood as a
  discipline that allows quantitative evaluation of the uncertainty of events;
- The fourth finally focuses on the foundations of _inferential statistics_,
  in order to provide tools that allow decision-making under uncertainty,
  using the tools introduced in the previous chapters.

Each of these parts, considered on its own, would fill an entire
textbook—possibly more than one! Therefore, although the material can be used
without resorting to external sources, the book very often allows only the
fundamental concepts of the disciplines considered to be addressed.
Nevertheless, where possible, some advanced tools typical of _machine learning_
are briefly described, which are based on the application of concepts and tools
presented in the book.

[^franklin-citation]: The aphorism is commonly ascribed to a sentence contained
in a letter from B. Franklin to the French physicist Jean-Baptiste Le Roy;
nevertheless, it is important to recognize that
[earlier sources]([wiki:Death_and_taxes_(idiom)](https://en.wikipedia.org/wiki/Death_and_taxes_(idiom)))
exist which could be original origins of the saying, alongside various recorded
variants.
