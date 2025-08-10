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

(sec:data-types)=
# Data Types

In the context of computer programming, the term _type_ is commonly used to
identify the category to which a particular _data_ element
belongs&mdash;whether it is associated with a variable, an expression, a
parameter, a function's return value, and so on. Associating each data element
with a type is important because it determines which operations can be
performed on it: for example, exponentiation makes sense when the exponent is a
number, but not, say, a string. Python also associates every piece of data with
a type, but it does so in a way that's quite different from the languages you
usually encounter when first learning to program. We'll soon see how this
mechanism works, by introducing some broad type categories that we'll explore
in more detail in the following sections. This will also give me a chance to
briefly introduce some concepts of _object-oriented programming_ that will be
needed to use certain libraries I'll reference, since this topic is not always
familiar to those starting to learn the fundamentals of _data science_.
```{margin}
In {ref}`sec:attributes` we'll see that it's important not to confuse the
_type of an attribute_ within a _dataset_ with the _data type_ used to store
that attribute's values.
```

(sec:dynamic-typing)=
## Dynamic Typing

In most of the languages studied when learning to program computers (such as C,
Java, or Go), a data element must be explicitly associated with its
corresponding type through a _declaration_, which determines what can be done
with that data. This makes it possible to detect invalid operations&mdash;like
the exponentiation of a letter mentioned earlier&mdash;by performing a
preliminary lexical analysis of the program's contents, and then translating it
into executable code only if the analysis succeeds. This approach is known as
_static type checking_, or _static typing_, referring to the fact that type
consistency is checked «at rest,» by reading the code before it runs, and
fixing each data type once and for all.

Python, however, takes a different approach: it removes the requirement for
explicit declarations and relies on _dynamic type checking_, which is carried
out during program execution. Without going into too much detail, before
performing any single operation Python checks whether it's possible given the
values of the operands involved. If inconsistencies are detected, an exception
is raised; otherwise, execution proceeds.
```{margin}
It's worth noting that Python is _strongly typed_, meaning it never performs
implicit conversions (such as promotions) between fundamentally different
operand types, like strings and integers.
```

Dynamic type checking greatly simplifies the language's structure: variables
and function parameters are simply assigned _names_ without specifying the
types involved. Specifically:

- a variable is automatically created the first time it's assigned a value, and
  its type is that of the value assigned;
- the formal parameters of methods and functions take on the types of the
  actual arguments passed during each call;
- the return type of a function is that of the expression returned at the end
  of its execution.

This means that, technically, it no longer makes sense to talk about the type
of a variable, parameter, or function return value as something immutable. A
function could, for example, return different types depending on the arguments
provided during its call; likewise, a variable can be assigned a value whose
type is completely different from what it previously held. In short, the
concept of type in Python is relative: what you can do with a variable or
parameter depends on the value it holds at that moment. To complicate things,
starting from Python 3.5 it's possible to add a kind of declaration using a
formalism called _type hinting_, which allows you to indicate in the code the
type of certain elements (such as a function's parameters or its return value).
It's important to stress that typing remains dynamic, but this way you can use
external tools to perform _type checking_ statically (that is, based on the
written code) to ensure that variables are used correctly. Editors and IDEs can
take advantage of type hinting to suggest code completions or flag warnings.
Finally, type hinting also serves as a way to lighten the software's
documentation, so I'll tend to use it whenever it makes the code easier to
read, while avoiding it when it would unnecessarily clutter things up.

(sec:types-classes-objects)=
## Types, Classes, and Objects

Python fully supports the object-oriented programming paradigm, which uses the
concepts of _class_ and _object_ to represent and manipulate data. Put simply,
a class represents an _abstraction_ for all data of a certain type. A class is,
in practice, the set of all data of a certain type. A single element of that
set is called an _object_, or an _instance_. More specifically, a class defines
not only what needs to be stored for a piece of data to exist (the information
contained in its _instance variables_), but also the operations that can be
performed on the corresponding object (its _methods_). For instance, a
hypothetical `Superhero` class might include:

- two instance variables `name` and `secret_identity`, containing two strings
  that represent a superhero's name and secret identity;
- two methods `fly` and `run` that implement the actions of flying and running,
  respectively.
```{margin}
In some object-oriented languages, methods completely replace functions.
As we'll see later, in Python the two concepts coexist.
```

If all we care about is referring to a superhero's name and secret identity,
and making them fly or run, the `Superhero` class contains everything we need.
When we want to think in terms of a specific superhero&mdash;say,
Superman&mdash;we can create the corresponding object by calling a special
method called the class's _constructor_, passing the necessary information to
initialize the object (often, but not always, values for all or some of the
instance variables). The constructor returns a _reference_ to the created
object, which is usually stored in a variable. In Python, the constructor is
invoked using the class's name itself, so creating the Superman object and
storing its reference could hypothetically be done as shown below.

```{code}
# This code is just to illustrate the concepts of class, constructor,
# reference, and object. Don't run it, because it won't work!

# Also note that any text following a hash sign (#) is ignored during execution
# and thus represents a comment.

hero = Superhero('Superman', 'Clark Kent')
``` 

```{margin}
As we'll see in {numfre}`sec:strings`, Python offers several string delimiters,
one of which is the single quote.
```
Here,

- `Superhero` is the class, and thus also the constructor;
- `'Superman'` and `'Clark Kent'` are the strings used to initialize the two
  instance variables;
- `hero` is the name of the variable that will store the reference to the
  `Superhero` object representing Superman.

Storing the reference returned by the constructor in a variable is necessary
because, in most cases, interaction with the object happens through a specific
syntax called _dot notation_: you write the variable name, then a dot, then
the name of an instance variable or method. In the first case, the expression
evaluates to the content of that instance variable; in the second, the result
can be used to call the method, passing any required parameters.
```{margin}
In theory, dot notation can be applied directly to the reference returned by
the constructor, or even to class _literals_[^literals], although in practice,
developers seldom need to use dot notation this way.
```

Returning to our example, `hero.name` has `'Superman'` as value, and you can
call `hero.fly()` (if the method requires no parameters). Here too, the
language is based on dynamic type checking: regardless of the class, when a
dot notation is analyzed at runtime, if the reference points to an object that
has the specified instance variable or method, execution proceeds smoothly;
otherwise, an `AttributeError` is raised. This means that, regardless of its
class, if an object lets you access the instance variables `name` and
`secret_identity` and call the methods `fly` and `run`, it iss effectively
equivalent to a `Superhero` object and can be used in any context designed for
that class[^duck-typing].

(adm:style-rules)=
```{admonition} Focus: identifiers and style rules
The term _identifier_ refers to the name chosen to uniquely reference specific
entities in a program, such as variables, instance variables, classes,
functions, methods, parameters, and so on. I will use the terms «name» and
«identifier» interchangeably, although the former can also be used in different
contexts (think, for example, of a file name).

From a syntactic perspective, to form an identifier in Python you can use
uppercase and lowercase alphabetic characters (keeping in mind that the
language is case sensitive: `superman` and `Superman` represent two different
identifiers), digits, and the underscore character (`_`), as long as the first
character is not a digit.

Respecting the syntax is mandatory, but it is also good practice to follow
_style rules_ as consistently as possible, which, among other things, include
specific conventions on how identifiers should be formed. There is no single
standard, however: I will refer to the
[Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/), which
also contains a section on
[Naming conventions](https://peps.python.org/pep-0008/#naming-conventions).
For (instance and regular) variables, functions, and methods, these style rules
prescribe the so-called _snake case_: use only lowercase letters and
underscores, employing the latter only as a separator in an identifier composed
of multiple words (as in `secret_identity` in the previous example). The use of
one or more underscores at the beginning or end of a name should be avoided, as
it can give a special meaning to the code that emerges only in particular
situations. I will not cover such cases in this book, but it is best to be
aware of this aspect early on when learning the basics of the language. There
are, however, exceptions to consider, and only two are relevant for our
purposes:

- when it is particularly meaningful to use a language keyword as an identifier
  (for instance `lambda`, which we will use in {ref}`sec:anonymous-functions`,
  might be used for expressing a mathematical or physical concept), it is
  acceptable to append an underscore to it (yielding, in the previous case,
  the identifier `lambda_`);
- if you need to explicitly refer to a variable that is used in a very limited
  portion of code, or not used at all, instead of inventing a meaningful name
  you can use a single underscore as the identifier.

Class identifiers, on the other hand, should follow the so-called
_upper camel case_, which requires using only alphabetic characters and
capitalizing the first letter of each word (as in `Superhero`). Finally,
although Python does not have the concept of a _constant_, you can use the
variant of _snake case_ that employs only uppercase letters (the
_screaming snake case_) to suggest that the content of a variable will not
change after its first (and only) assignment.

Even while following syntax and style rules, there is still a wide degree of
freedom in choosing an identifier: in the previous example, instead of `hero`
you could use `clark_kent`, `superman`, `s`, `s1`, or more or less intelligible
jumbles of characters. However, to improve code readability, it is highly
recommended to choose a name that reflects the meaning of the identifier itself.
```

It should also be emphasized that the only way to refer to a data type in
Python is through the use of classes: unlike Java, there are no «primitive
types» that store integers, floats, and so on as mere sequences of bytes.
Instead, the integer and floating-point types correspond to the `int`[^maxint]
and `float` classes, each characterized by its own methods.
```{margin}
Many of the classes that implement types introduced in the earliest versions of
Python, such as `int` and `float`, are an exception to the style rule mentioned
earlier: for various reasons, including backward compatibility, their names do
not start with an uppercase letter.
```

To recap, when talking about a variable in Python code, rather than saying that
a variable contains a value of a given type, it would be more accurate to speak
of a _name_ (or identifier) associated with a _reference_ that in turn uniquely
identifies the object of a class: the latter (temporarily, due to dynamic
typing) determines the type of the particular data corresponding to the
variable. In programming jargon, the verb _to bind_ is used to more strongly
indicate this association between the name and the object. A similar discussion
applies, for example, to the formal parameters of a function or method.
Admittedly, this terminology can be cumbersome, and indeed in everyday speech
it is common to refer to a variable (or parameter) and the object&mdash;or even
the value&mdash;it contains.

```{admonition} Warning
Object-oriented programming is a very complex topic, and in this section I have
only scratched the surface. I have limited myself to introducing what you need
to know in order to understand the code I will present later, and to learn how
to write programs that automate the data analysis techniques I will introduce
in the following chapters. I have not described how to create classes for
custom data types, nor have I covered specific topics such as inheritance and
polymorphism, because knowing these aspects of the language is not necessary
to profitably follow the rest of what I will write. Mastering these concepts,
however, is definitely an expected skill for a computer scientist, and also
desirable for a data scientist, but all of this is well beyond the scope of
this book. To explore these topics in more depth, you can refer to the
[relevant section](https://docs.python.org/3/tutorial/classes.html) of the
official Python documentation or to Part IV in {cite:p}`ramalho`.
```

(sec:simple-and-structured-types)=
## Simple and structured types

To simplify the discussion a bit, we can divide the data types we will use into
two broad categories:

- _simple_ data types, which define an atomic piece of information that makes
  little sense to break down further, such as an integer or floating-point
  number;
- _structured_ data types, which are used to aggregate multiple data types
  (whether simple or structured), such as arrays or sets.

The next two sections will describe, respectively, the simple and structured
data types I will use in this book. Even just considering the core language,
Python includes several data types (the official documentation provides a
[list](https://docs.python.org/3/library/datatypes.html)), to which we must add
those implemented by third-party libraries. The treatment I will provide is
certainly not exhaustive, and even if it were, it would be far from perfect. On
one hand, it is incomplete because there are classes that implement types that
do not naturally fall into either of the two categories introduced (such as
those that describe functions, iterators, or complex concepts that do not
correspond to any data type in the classic sense); on the other hand, it is
debatable to associate certain types with one category or the other: for
example, strings can be thought of as a simple type, but they can also be
considered structured, since they consist of a sequence of characters.  

To decide whether a data type is simple or structured, I will use the following
criterion: a piece of data is considered structured if Python natively allows
you to _iterate_ over its elements using the `for` idiom (see
{ref}`sec:iterate`); in all other cases, I will treat the data type as simple.

## Exercises

```{exercise} •
With reference to the characteristics of dynamic type checking, state which
of the following statements are true and which are false:

- at different moments during a program's execution, the same variable can hold
  values of different types;
- the name of a variable can change during execution;
- it is possible to assign a value to a variable before it is defined;
- a function might or might not return a value, depending on the situation.
```

```{exercise} •
Consider the hypothetical `Superhero` class defined in
{ref}`sec:types-classes-objects`, and suggest additional instance variables
and methods that would make sense for its objects.
```

```{exercise} ••
Identify which of the following statements about constructors in Python are
true and which are false:

- to create an object of a class, it may be necessary to call the
  corresponding constructor more than once;
- calling a constructor never requires specifying values for any parameters;
- every instance variable in a class corresponds to a parameter in the
  constructor;
- calling a constructor is the only way to create an object;
- the name of a class is also the identifier used to call its corresponding
  constructor.
```

```{exercise} ••
The `type` function returns the class of the value provided as its argument.
Use this function to find out the type of the following expressions:

- `42`;
- `42.`;  
- `'foo'`;
- `None`;
- `int`.
```

```{exercise} ••
Consider the following character sequences, and for each figure out whether it
represents a valid identifier in Python or not. For each valid identifier,
decide whether it follows the conventions introduced in the text.

- `speed`;
- `Speed`;
- `sp&emarc;&emarc;d`;
- `CarSpeed`;
- `CArSPeED`;
- `Car_Speed`
- `SPEED`
- `CAR_SPEED`
- `_speed`;
- `speed_`;
- `__speed`;
- `speed__`;
- `__speed__`;
- `__init__`;
- `set_level`;
- `set__level`;
- `set__level__`;
- `int`;
- `int_`;
- `i`;
- `i1`;
- `1i`;
- `_`;
- `black&white`;
- `jfellfsef`.
```

```{exercise} ••
Consider the data types you are already familiar with (for example, those you
have studied in programming courses), and for each one specify whether it falls
into the category of simple types or structured types, explaining your choice.
```

[^literals]: If you don't know (or don't remember) what a literal is, you'll
find out in the next paragraph.

[^duck-typing]: The term _duck typing_ is often used to describe this aspect of
dynamic typing, referring to a phrase attributed to the American poet James
Whitcomb Riley: «when I see a bird that walks like a duck and swims like a duck
and quacks like a duck, I call that bird a duck».

[^maxint]: It is also worth noting that the implementation of the `int` class
uses an arbitrary-precision arithmetic approach: the number of bits required to
store an integer value is not fixed, but allocated dynamically depending on the
values assigned from time to time. This means there is no «largest» or
«smallest» storable integer, as in other languages.
