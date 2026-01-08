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

(chap_apprach)=
# Approach

I have always found it easy to learn new concepts by putting them into practice  
in a context that could be easily explored and controlled. When, years ago, I
started teaching, it felt natural to use the same approach, unconsciously
adopting a teaching method that I only later discovered was codified in the
methodology of _learning by doing_   {cite:p}`freire1982`. This book tries to
follow the same philosophy,   introducing topics from the very
beginning&mdash;where possible&mdash;within   an application-oriented context.

```{margin}
The use of science fiction to introduce scientific concepts is not particularly
unusual: two fairly well-known examples are «The Physics of Star Trek»
{cite:p}`krauss` and «The Physics of Superheroes» {cite:p}`kakalios`[^note].
```

To ensure coherence in the discussion, I decided to frame the examples used
alongside the more theoretical parts within a single domain. The scope I chose
is the superhero multiverse. This may seem paradoxical, given the philosophy I
just stated: superheroes are characters in a fictional narrative—highly
_fiction_, indeed. However, the ability to apply a concept to a context does
not depend on the physical realizability of that context: it only requires that
the assumptions describing a given situation be clearly, consistently, and
precisely stated. This allows one to metaphorically immerse oneself in that
situation, to use mathematics to model it and computer science to simulate it,
thus enabling exploration using the scientific method and, hopefully, deriving
insights, making decisions, and so on. Besides being great fun, referring to a
non-existent world has another advantage: it helps learners avoid establishing
a direct link between a problem instance and the solution methods to use,
promoting learning focused on the _critical_ use of methods and tools.

Although I embarked on this endeavor, I am no superhero expert. I therefore
preemptively apologize to those who know more than I do for any imperfections
or errors I might have included, hoping that these won’t make it harder to
understand the concepts and examples presented. While I am somewhat more
experienced in data analysis, probability, and statistics, I can't guarantee
that there are no inaccuracies overall, although in this case I’m confident
there aren’t too many.

The writing work is still _in progress_, and likely will be for quite some
time: please report typos and errors, and more generally any examples or
material you think could enrich what I have written, keeping in mind that
images, data, and so on can only be published if they are compatible with the
_Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International_
license
([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en))
under which this book is distributed. The most practical way to send me these
reports is to submit _issues_ (to report errors or suggest improvements) or
_pull requests_ (to propose content changes) to the
[repository](https://github.com/dariomalchiodi/sds) in which I have organized
the contents of this book. This requires familiarity with
[git](https://www.git-scm.org), the _source control management_ tool I use for
my software projects.

[^note]: I will use margin notes for comments I consider important but that
should not burden the main reading of the corresponding paragraphs. Instead, I
will relegate to endnotes all in-depth discussions that can be skipped on a
first reading.
