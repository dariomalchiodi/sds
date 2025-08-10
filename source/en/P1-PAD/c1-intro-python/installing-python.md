---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
nb_execution: false
---

(sec:installation)=
# Installation, configuration, and first steps

This section explains how to install Python and the libraries I'll refer to
throughout the book, while also introducing a set of good practices that are
worth adopting from the very beginning of any data analysis software
project&mdash;such as the use of virtual environments and package managers. If
you are already familiar with Python and have a working installation, you can
likely skip to the next section. However, I still recommend a quick read to
align with the terminology I'll be using and to ensure there are no
compatibility issues with your installed version and that all required
libraries are available.

(sec:languages-versions-implementations)=
## Languages, versions, and implementations

Programming languages evolve over time, as their specifications get updated.
These changes result in a sequence of _versions_ of the language. Today, the
widely adopted way of identifying a specific version of a programming language
(but also of a library or any software product) is the so-called
[semantic versioning](https://semver.org/) scheme, which, in its simplest form,
describes a version using the format `X.Y.Z`, a sequence of three integers
initially set to zero and incremented upon updates:

- `X` indicates a _major release_ and is increased when breaking changes are
      introduced,
- `Y` is the _minor release_, increased when new backward-compatible features
      are added,
- `Z` represents the _patch number_, related to small changes and fixes.

In general, unless an unusually precise specification is needed, it's enough to
refer to a specific version of Python using only the major and minor releases.
For example, even though the code in this book was written using Python version
3.11.11, I will simply refer to version 3.11, since the code is executable
regardless of the specific patch number. Moreover, using newer minor releases
should not cause any issues, while using significantly older ones is
discouraged.

It might seem that knowing the exact version of a programming language is
enough to determine all of its features, but that's not quite true. Defining a
language involves specifying its _syntax_ and _semantics_, but building the
tools to run the corresponding programs&mdash;interpreters and
compilers[^compilers]&mdash;is a different matter. These tools may be built by
different people, at different times, and using different technologies. As a
result, there are multiple _implementations_ of a language that might differ
even when they comply with the same version, as the specifications may not
fully dictate _how_ certain features should be implemented. For example, string
encoding formats might vary between implementations. In Python's case, there
are [several implementations](https://www.toptal.com/python/why-are-there-so-many-pythons),
each using a different underlying technology: one relies on the Java virtual
machine, another on a C-based runtime, another runs in web browsers, and so on.
The most common implementation, usually installed by default, is called
_CPython_, and, as the name suggests, is written in C.

(sec:download-book)=
## Downloading the book contents

This book is designed to be used through a web server. The benefit is that the
interactive components can be accessed without needing to install or configure
any libraries, but this requires a continuous internet connection.
Alternatively, you can download the book contents and generate its chapters as
web pages served from a local web server, but that involves first installing
all necessary software for this generation process. Note that running
interactive components still requires an internet connection.

```{margin}
To clone the book's repository, you need to have a git _client_ installed, a
GitHub account, and a public SSH key associated with it. Alternatively, cloning
via HTTPS is also possible, which simplifies some steps (like the SSH key) but
complicates others.
```

The recommended way to download the book is via [git](https://git-scm.com), a
source control management system used to manage source code in software
projects. To do this, open a terminal, navigate to a desired location in your
file system, and execute the following command to clone the book's
[repository](https://github.com/dariomalchiodi/sds) locally into a new `sds`
directory:

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      In all the examples below, the symbol ``$`` indicates the shell prompt.
      Depending on your system configuration, your prompt might look different.
      In the example below, ``my_parent_dir`` is a placeholder for the path
      where you wish to save the book's directory.

      .. code-block:: bash

         $ cd my_parent_dir
         $ git clone git@github.com:dariomalchiodi/sds.git
         $ cd sds

      I'll assume throughout the rest of this section that the same shell
      session is being used.

   .. group-tab:: Windows

      In the following examples, ``C:>`` represents the PowerShell prompt. Your
      prompt may vary depending on your system. ``my_parent_dir`` is a
      placeholder for the folder path where you wish to save the book's
      directory.

      .. code-block:: powershell

         C:> cd my_parent_dir
         C:> git clone git@github.com:dariomalchiodi/sds.git
         C:> cd sds

      I'll assume this PowerShell session remains open throughout the rest of
      this section.

```

```{margin}
An active internet connection is required to perform this operation.
```

Alternatively, a ZIP archive can be downloaded. However, using git makes it
easy to keep the book up-to-date simply by running the command:

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         $ git pull

   .. group-tab:: Windows

      .. code-block:: powershell

         C:> git pull

```

from a terminal after navigating into the `sds` directory (or any of its
subdirectories). Additionally, git is the tool used to report issues or propose
changes, by submitting _issues_ or _pull requests_ as explained in
{ref}`chap:approccio`. Finally, learning git is something I recommend to anyone
studying not only computer science, but any discipline within the field of data
science. In fact, git is used in the vast majority of software projects, so
it's worth learning from the start.

## Installing Python

Python installation heavily depends on your operating system. Recent
distributions of Linux and Mac OS include Python by default, while on Windows
it needs to be installed manually. Still, your current computer might already
have Python installed. To check, open a terminal and run:

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         $ python --version

   .. group-tab:: Windows

      .. code-block:: powershell

         C:> python --version

```

Three outcomes are possible:

1. The output is `Python 3.Y.Z`, meaning Python 3 is installed, where `Y` and
   `Z` are the minor release and patch numbers respectively, and `Y` is greater
   than or equal to $5$;
2. The output shows a version starting with `1` or `2`, or `3` but with a minor
   release lower than $5$, meaning Python is present but too old to run this
   book's code. I will be referring to version 3.11, which is widely adopted at
   the time of writing;
```{margin}
If the major release is `4` or higher, then you're reading this book long after
it was written, and some Python-related content may be outdated. Check for
newer editions or updated documentation.
``` 
3. You get an error stating that `python` is not a recognized command, likely
   meaning Python isn't installed.

In the first case, your current Python installation will likely suffice to run
the book's code. Still, it's worth checking that the version is as close as
possible to the one I used. A significantly different version might cause
compatibility issues, in which case you should install the version I refer to,
without removing the existing one.
```{margin}
Technically, replacing the system Python is possible, but it risks breaking
other software. This is generally not recommended.
```

In the second case, a compatible version might still exist, but the `python`
command points to a different one. To check, you can type `python` in the
terminal and then press {kbd}`TAB` without a space: if multiple versions are
installed, their commands will be listed. In the third case, Python might be
installed but not configured properly for terminal use&mdash;though this is
rare.
```{margin}
Usually, for each installed version, there's a corresponding command like
`pythonX.Y`, where `X` and `Y` are the major and minor release numbers. The
command `python` is an alias pointing to one of these, typically the version
most used by the system.
```

If Python needs to be installed, refer to the official documentation, which
includes guides for
[Unix (like Linux)](https://docs.python.org/3/using/unix.html),
[Mac OS](https://docs.python.org/3/using/mac.html), and
[Windows](https://docs.python.org/3/using/windows.html).

## Creating a virtual execution environment

Python is commonly used with many libraries, and I strongly advise against a
_monolithic_ installation approach, where libraries are added one at a time as
needed. Over time, this increases the risk of incompatibilities between your
environment and newly added libraries. Similar issues arise when updating
libraries. To avoid such problems, it's best to isolate library installations
by running Python inside a dedicated space containing only the libraries needed
for a specific project. These spaces, called _virtual environments_, are
activated when starting to work on a specific project and deactivated when
switching to another.

There are various ways to create virtual environments in Linux; this book uses
_venv_[^environment], which is included with recent Python versions. To create
a virtual environment, use the same shell session as before, navigate to the
`sds` directory, and run:

```{margin}
Naming the directory `.venv` is a common practice recognized by many IDEs. You
can technically choose any name, but do so only if you have a specific reason.
The `--prompt sds` option is optional and sets the prompt label; otherwise, the
directory name is used.
```

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         $ python3.11 -m venv .venv --prompt sds

   .. group-tab:: Windows

      .. code-block:: powershell

         C:> python3 -m venv .venv --prompt sds

```

Make sure `python3.11` (on Linux/Mac OS) or `python3` (on Windows) points to
the intended version and that it's properly installed. This creates a `.venv`
directory (hidden on Linux and Mac OS) with executables and future libraries
for this environment. To activate it, run:

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         $ source .venv/bin/activate

   .. group-tab:: Windows

      .. code-block:: powershell

         C:> .venv\Scripts\activate

```

You must run this from within the `sds` directory (or use a relative/absolute
path to the `activate` script). Activation also changes the prompt, adding
`(sds)` to signal that a virtual environment is in use. The next section
explains how to install libraries after activation. To deactivate the
environment, run:

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         (sds) $ deactivate

   .. group-tab:: Windows

      .. code-block:: powershell

         (sds) C:> deactivate

```

This returns the system prompt to its original state.

(sec:lib-install)=
## Managing libraries

In theory, a library can be installed manually by downloading its executable or
building it from publicly available source code. But this can be tricky: most
libraries depend on other libraries, which themselves may depend on others, and
so on, and so forth. Manually installing a library often becomes a
time-consuming and frustrating experience. The more dependencies required, the
higher the chance of errors that stall or break the process. To avoid this
issue, it's best to use a _package manager_&mdash;a tool that automatically
detects and handle dependencies. This is considered best practice in Python and
software development in general. Like with virtual environments, Python has
several
[package managers](https://packaging.python.org/en/latest/tutorials/installing-packages/#alternative-packaging-tools)[^package-manager].
I will refer to [pip](https://pip.pypa.io), which is included with recent
Python versions.

Library installation, usually done in an active virtual environment, is done
with the `pip` command in a shell, specifying the library name&mdash;optionally
followed by `==version` for installing a specific release. For example, to
install altair, the library used in {ref}`sec:overview` for interactive plots,
you'd run:

```{margin}
Soon we'll see how to install all required libraries at once, so you don't need
to run this command now.
```

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         (sds) $ pip install altair

   .. group-tab:: Windows

      .. code-block:: powershell

         (sds) C:> pip install altair

```

This checks for altair's dependencies, installs them if missing, or updates
them if versions are incompatible, and does the same recursively for further
dependencies.

Using package managers also provides another benefit: you can share a software
project along with a text file listing required libraries, and install them all
at once. With pip, this list typically goes into a `requirements.txt` file. To
install everything listed there, run:

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         (sds) $ pip install -r requirements.txt

   .. group-tab:: Windows

      .. code-block:: powershell

         (sds) C:> pip install -r requirements.txt

```

The [repository](https://github.com/dariomalchiodi/sds) for this book includes
a `requirements.txt` file listing all libraries needed to run the code
throughout the chapters.

(sec:notebook)=
## Installing a notebook manager

As mentioned at the beginning of this chapter, I will present Python code in a
way that allows it to be easily executed inside files called _notebooks_. The
content of these files is organized into _cells_, which can be of three
different types:
- code cells, consisting of one or more lines of executable code[^nb-lang],
- output cells, each of which is associated with a specific code cell and
  contains the output produced by the execution of the latter,
- other cells, which can contain formatted text, charts, or videos, possibly
  generated as side effects of the code executed in the notebook, or manually
  added by its author.

```{margin}
When the name of a Python-based technology includes the syllable «py,» it is
typically pronounced like the English word «pie,» that is,
[ˈpī](https://www.merriam-webster.com/dictionary/pie?pronunciation&lang=en_us&dir=p&file=pie00001).
Jupyter is an exception, as declared by its creators[^pronunce-jupyter], and is
pronounced
[ˈjü-pə-tər](https://www.merriam-webster.com/dictionary/Jupiter?pronunciation&lang=en_us&dir=gg&file=ggjupi01),
like the English name for the planet Jupiter.
```

The _de facto_ standard for notebooks is the one introduced by the
[Jupyter](https://jupyter.org) project. There are
[many applications](https://mljourney.com/jupyter-notebook-alternatives-in-2025/)
that allow you to write, read, and especially execute notebooks. Among them,
the most commonly used are the one distributed directly by the Jupyter project
and Microsoft's main IDE, [Visual Studio Code](https://code.visualstudio.com).

If you have installed the libraries using the `requirements.txt` file following
the instructions in the previous sections, then Jupyter is already available
within the virtual environment you created. To launch it, simply run the
following command from the terminal:

```{margin}
A little further on you'll also find instructions on how to view and run a
notebook using Visual Studio Code.
```

```{eval-rst}
.. tabs::

   .. group-tab:: Linux / Mac OS

      .. code-block:: bash

         (sds) $ jupyter notebook

   .. group-tab:: Windows

      .. code-block:: powershell

         (sds) C:> jupyter notebook

```

```{margin}
The `.ipynb` extension identify python notebooks.
```
This will automatically open a browser connected to a local address, where a
web server has been launched to listen for requests. The loaded page will show
the files contained in the directory from which Jupyter was launched. For
example, {numref}`jupyter-home` shows what this page looks like when starting
from the root directory of this book’s repository. By clicking on the
_playground_ directory and selecting the only file available,
_first-notebook.ipynb_, a simple notebook example is displayed. This notebook
contains a single code cell, in which the expression `1 + 1` is already
present. If you place the cursor inside the cell and press
{kbd}`Shift` + {kbd}`⤶`, an output cell will automatically be added to the
notebook, showing the result of the expression. To create a new _notebook_, you
can either select the menu item _File > New > Notebook_, or return to the file
listing view, click on the «New» button, and choose «Python 3 (ipykernel)».
A new page will appear, containing a single empty code cell. The advantage of
using a notebook lies in the high interactivity during code execution, since
the results of a cell's execution remain in memory for as long as the notebook
stays open: this allows you to reuse them in subsequent cells.

```{figure} ../../../_static/img/jupyter-home.png
:width: 100%
:name: jupyter-home

The Jupyter home screen, showing the list of files present in the directory
corresponding to the book's repository.
```

Using a notebook with recent versions of Visual Studio Code is even easier,
provided the corresponding extension is installed: you just need to open the
file from the IDE, and its cells will be displayed in a tab. In this case too,
you can add code and execute it just as you would in Jupyter. The only
difference is that the first time you run a cell, you might need to select an
environment from a context menu.

```{admonition} Warning
There is considerable flexibility in how you can evaluate the code cells within
a notebook: you just need to place the cursor on a cell and press
{kbd}`Shift` + {kbd}`⤶`, which allows them to be executed in any
order&mdash;from first to last, last to first, seven times the first then the
third, or in any order that might come to mind. This has both pros and cons. On
the one hand, this flexibility can be used to analyze data in a highly
interactive way, running small parts of code and evaluating the results before
deciding on the next step. On the other hand, the inability to constrain
execution to a fixed, predefined order introduces some level of indeterminacy
in the result, thus limiting the reproducibility of outcomes. Additionally,
although notebooks are essentially text files, they include a lot of metadata
that makes them harder to manage via git[^jupytext]. It's also worth noting
that notebooks are just one of many tools you can use to run Python code. Among
the most common alternatives, two are particularly widespread. The first is the
use of the so-called REPL (Read, Evaluate, Print, Loop), a purely text-based
environment run in a shell that, in some ways, follows the same philosophy as
notebooks: you enter an instruction and execute it, observe the result, then
run a second instruction, and so on&mdash;but in this case, to re-run a
previous instruction, you have to type it again. The second is using a Python
interpreter to run a program, much like you would with other languages such as
Go or Java.
```

## Getting Started with Python

As discussed in {ref}`sec:learning-and-programming`, I assume you are already
familiar with at least one programming language. In this section, however,
we'll take a quick look at some basic programming operations to see how they
are performed in Python. This will allow me to immediately introduce code
examples in Python alongside the concepts I'll be explaining.

### Assignments
Assigning a value to a variable uses the same notation as in most other
programming languages, following the syntax `variable = value`. In
{ref}`sec:dynamic-tipig`, we'll see that Python doesn't require type
declarations: variables are automatically created the first time a value is
assigned to them, and that value implicitly determines their type. For example:

```python
age = 42
```

is an assignment that involves an integer type.

### Printing a value
We've already seen how evaluating a cell in a notebook can produce output.
However, this method has limitations (for example, it only prints the result of
the last expression evaluated in the input cell), and it doesn't work at all
outside notebooks. More generally, you can print a value or the contents of a
variable by passing them as arguments to the `print` function:

```python
print(age)
print(3.14)
```

### Conditional execution
When it comes to conditional execution, Python uses syntax that is probably
quite similar to what you already know, though not exactly the same. Consider
the following cell:

```python
if age >= 18:
  print('They are of age, they are', age, 'years old.')
else:
  print('They are not of age.')
```

```{margin}
Indentation can be done using any number of spaces or tabs, as long as you
don't mix the two and keep the same choice throughout the entire block. There
are arguments both for and against spaces or tabs, and this remains a deeply
divisive topic among developers&mdash;a real war of preferences. Personally,
I don't intend to take sides: it often comes down to personal taste, unless the
decision is imposed by your work environment. I'll just point out that whatever
option you choose, consistency in your code is essential.
```

Selection is done using the `if` statement, which must be followed by a
condition ending in a colon (`:`). The block of statements executed when the
condition is true must have consistent indentation. The `else` keyword
specifies an alternative block if the condition is false, using the same
syntax[^one-liner]. Note that the example above highlights that:

- there is no need to surround the condition in parentheses,
- the `print` function allows you to print messages in the form of strings,
  enclosed in single quotes,
- you can pass a variable number of arguments to `print`, which will be printed
  separated by spaces.

### Defining functions
The next cell shows how to define a function that takes one argument
(interpreted as a person's age) and returns a boolean indicating whether the
person is of legal age, after printing a message similar to the one introduced
earlier:

```{margin}
"Note how the execution generates two cells, each serving a very different
purpose: the first cell contains printed message from the `print` function,
while the second is the output cell that holds the value returned by
`check_age`. It's worth underlying that mixing standard output and return
values in this way is __not__ considered good programming
practice[^bad-practice], but in this case it helps me introduce several
important concepts in a single, concise example.
```

```python
def check_age(age):
  if age >= 18:
    print('They are of age, they are', age, 'years old.')
    return True
  else:
    print('They are not of age.')
    return False

check_age(age)
```

This example also allows us to observe that:

- a function definition starts with the `def` keyword, followed by the function
  name, a pair of parentheses containing its parameters, and a colon;
- argument types are not declared, due to the language's dynamic typing;
- the function body is indented, and the blocks corresponding to `if` and
  `else` are further indented;
- the `return` statement marks the end of execution for the function and
  specifies the return value;
- the constants `True` and `False` refer to the two possible boolean values.

The main advantage of defining a function is, of course, being able to reuse it
with different arguments, as shown below:

```python
check_age(13)
```

### Importing modules
In Python, complex software projects and code reuse are based on the concept of
_modules_. A module is essentially a file that defines one or more variables,
functions, or classes. You can import an entire module or just one (or some) of
its components. Modules are especially useful for working with standard or
third-party libraries. Consider the `math` module, which is distributed with
Python and defines, among other things, the variable `pi` (an approximation of
$\pi$) and the function `factorial` (factorial of an integer). These two
elements can be _imported_ so they can be used in your code just like if you
had defined them yourself, using the syntax `from <module> import <name>`:

```{margin}
Note that it is possible to use `import` to bring in multiple elements from a
module in a single statement.
```

```python
from math import factorial, pi

print(pi)
print(factorial(10))
```

```{margin}
You can also define _aliases_ using the form
`from <module> import <element> as <alias>`.
```

When working with complex code, it's possible that elements from different
modules have the same name. A common way to avoid such name clashes is to use
so-called _namespaces_: you import the entire module using `import <module>`,
and then access its individual elements using a variant of dot notation,
writing the module name followed by a dot and the element name.

```python
import math

print(math.pi)
print(math.factorial(10))
```

In cases like this, should two modules `m1` and `m2` both contain an element
named `e`, there can be no naming conflict, because you'd refer to them as
`m1.e` and `m2.e`. However, using the module name to access its elements makes
your code longer, and potentially less readable. That's why you can import a
module using a shorter alternative name, or _alias_, with the syntax
`import <module> as <alias>`. I'll use this approach for the libraries I use
most ofthen in the book: [numpy](http://www.numpy.org),
[pandas](http://pandas.pydata.org), and [matplotlib](http://matplotlib.org),
which allow us to work with arrays, datasets, and graphical visualizations. I
will always import them like this:

```{margin}
As you can see in the third line of this cell, some modules (like matplotlib)
are organized in hierarchical structures called _packages_, much like in Java.
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

```{admonition} Naming conventions
:class: naming
This way of importing numpy, pandas, and the `pyplot` module from matplotlib
using the aliases `np`, `pd`, and `plt` is a universally accepted convention
among developers. It's highly recommended to follow this convention, so readers
can immediately understand which module is being referenced.
```

### Errors and exceptions
Python handles error situations by raising _exceptions_, similarly to how it's
done in Java. The example below shows how a `NameError` exception is raised
when referencing a variable that has never been initialized:

```{margin}
The output indicating an error condition, typically called the _stack trace_,
is detailed: it shows the portion of code involved, possibly listing the
sequence of function or method calls, and specifies both the type of exception
and an associated message.
```

```python
print(uninitialized_variable)
```

A key aspect of exceptions is that their occurrence normally stops the
program's execution (or the evaluation of a cell in a notebook), but the
programmer can write code that is automatically executed when a specific
exception occurs within a certain block. I won't go into the details of this
feature here. To learn more, you can consult the
[official documentation](https://docs.python.org/3/tutorial/errors.html).

There are also error situations that cannot be handled through exceptions: a
classic example is syntax errors, which occur when the source code parser fails
to recognize a line of code.

## Exercises

[^compilers]: A common question is whether Python is an interpreted or compiled
language. The answer depends on the specific implementation being used, though
in most cases the most accurate answer is: «neither.» Python typically uses an
intermediate compilation to _bytecode_, similar to Java. This bytecode is
equivalent to binary code but for a _virtual machine_. A specific piece of
software then executes the bytecode by translating it into the machine code of
the computer being used. When using CPython&mdash;the Python implementation
this book refers to&mdash;compilation happens automatically and transparently
when modules are imported (see {ref}`sec:importing-modules`): the result of
compilation is a set of `.pyc` files saved in a `__pycache__` directory,
generated only if they don't exist or are older than the source file; in other
cases, the bytecode already existing is executed directly.
[^environment]: There are some alternatives for creating and managing virtual
environments. At the time of writing,
[Anaconda](https://docs.anaconda.com/anaconda/) and
[Miniconda](https://docs.anaconda.com/miniconda/) are among the most commonly
used along with `venv`.
[^package-manager]: Anaconda and Miniconda, mentioned in the previous note,
also provide their own package managers, which can be used instead of pip.
[^nb-lang]: Notebooks are not tied to a specific programming language. Notebook
managers are typically modular and allow the installation of one or more
_kernels_, each dedicated to a specific programming language. I will mostly
work with Python code, but we'll occasionally see how to run shell commands
without opening a dedicated terminal.
[^pronunce-jupyter]: Fernando Perez, one of the creators of the Jupyter
project, pronounces it this way in his
[talk](https://www.youtube.com/watch?v=cc2hHjARNTY) at the PLOTCON 2016
conference.
[^jupytext]: Including notebooks directly in a git repository is discouraged.
Instead, you can use tools like [jupytext](https://jupytext.readthedocs.io/),
which automatically sync notebooks with equivalent Python code and version that
instead.
[^one-liner]: It's actually possible to write a one-liner `if` expression, but
I advise against it because it tends to reduce code readability.
[^bad-practice]: In principle, a function should not print output to the
screen unless it is for warnings or errors. Even in such cases, it's usually
better to use dedicated language features like logging or exceptions rather
than relying on `print`. This helps avoid confusing readers of the program's
output, makes a clear distinction between messages and returned values, and
simplifies software testing.
