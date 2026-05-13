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

(chap_introduction)=
(par_franklin-law)=
# Introduction

> In this world, nothing can be said to be certain,<br/>
> except death and taxes
>
> -- Benjamin Franklin

The quotation that opens this section comes from a letter written in 1789 by
Benjamin Franklin (see {numref}`benjamin-franklin`), one of the Founding
Fathers of the United States of America. If we accept this principle, often
called _Franklin's law_ [^franklin-citation], then studying uncertainty is
worth the effort, because practically everything is uncertain. Ironically, even
Franklin's law itself is not entirely beyond doubt: just think, for instance,
of tax evasion, or of the fact that residents of the Principality of Monaco do
not pay income tax.

```{figure} https://live.staticflickr.com/2869/9544834557_b844c48e78_b.jpg
:width: 70%
:name: benjamin-franklin

Depiction of Benjamin Franklin on United States 100-dollar bills
(image by E. Strauhmanis, distributed under
{extlink}`CC BY 2.0 <https://creativecommons.org/licenses/by/2.0/>`)
```

In reality, the concept of _uncertainty_ is hard to define, because it has
many facets and takes on different meanings depending on the context. In this
book I will focus on one specific sense of the term, often denoted by the word
_randomness_. In simple terms &mdash; and therefore terms that are bound to be
imperfect &mdash; we can identify randomness as the property that
characterizes an experience which, even if repeated under the same conditions,
produces a result that cannot be predicted a priori. In a way that is, for the
moment, informal, we call _events_ statements about the outcomes of those
experiences. Their truth value is therefore uncertain. A classic example of an
event is the outcome of rolling a die during a game of Monopoly. Another,
equally classic but more modern, example concerns the closing value of a stock
market index. But we could add many others: will it rain today, if when we
look at the sky in the morning we see clouds on the horizon? How many
grandchildren will my next-door neighbor's sister have? Next year, will I
manage to get through flu season by falling ill at most once? In fact, it is
not hard to realize that randomness &mdash; or, if you prefer,
non-determinism &mdash; permeates everyday life. It also plays an essential
role in the description of some fundamental aspects of Nature, such as the
theory of evolution or quantum mechanics.

Despite this, we soon learn to live fairly well with uncertainty: when leaving
home, we almost always know whether it is worth taking an umbrella with us,
and some people even manage to speculate successfully on the stock market.
This happens because we are able to _assess_ the uncertainty of many events,
accepting the _risk_ that our assessment involves. Returning to the example of
the cloudy sky, the risk is either carrying an umbrella for no reason or ending
up in the rain without one. Usually, the decisions we make are based on widely
subjective criteria grounded in our _experience_. Mathematics, however,
provides tools for tackling this problem rigorously. In particular, by
combining _probability theory_ and _statistics_ we can model the uncertainty of
events and evaluate it using the experience we have acquired.

The purpose of this book is precisely to provide the foundations of these two
branches of mathematics, adopting an interactive approach centered on data
analysis and aimed at students who have already developed skills in computer
programming. The material has been designed for students in computer-science
degree programs, but it is certainly suitable for any course of study that
includes at least one compulsory programming class.

The work is organized into four parts:

- the first introduces the Python programming language and its _data science
  stack_, that is, the main libraries used for data analysis;
- the second deals with _descriptive statistics_, which provides tools for
  organizing and analyzing observations of a phenomenon in order to extract
  _information_ (the basis of the experience mentioned above);
- the third describes the foundations of _probability theory_, understood as a
  discipline that allows us to quantify the uncertainty of events;
- the fourth and final part focuses on the foundations of _inferential
  statistics_, providing tools that support decision-making under uncertainty
  by exploiting the methods introduced in the previous parts.

Each of these parts, taken on its own, would fill an entire textbook &mdash;
more than one, in fact. For this reason, I will limit myself to the
fundamental concepts of the disciplines considered, while still trying to make
the book usable without having to rely on external sources. Whenever possible,
I will also present some more advanced aspects, typical of _machine learning_,
based on the concepts and tools described in the preceding chapters.

[^franklin-citation]: The aphorism is commonly ascribed to a sentence contained
in a letter from B. Franklin to the French physicist Jean-Baptiste Le Roy. It
is worth stressing, however, that even though the saying is attributed to
Benjamin Franklin, there are {extlink}`earlier sources
<https://en.wikipedia.org/wiki/Death_and_taxes_(idiom)>` that report several
variants of it.
