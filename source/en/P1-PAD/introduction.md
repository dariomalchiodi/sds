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

(chap:introduction)=
# Introduction

The first part of this book introduces some basic tools for the automated
analysis of small- to medium-sized datasets[^big-data] using a computer. 
Mastering these tools, together with the ability to apply them effectively 
to various data science scenarios, is now essential for analyzing and 
interpreting the wide variety of available data and using it to support 
decision-making.

Among the essential tools are:

- a programming language that allows writing instructions to automate 
  data processing;
- a library for structured management of datasets.

In this book, I will use Python and Pandas, presented in 
{ref}`chap:intro-python` and {ref}`chap:pandas`, respectively. While there 
are many valid alternatives, these two technologies currently represent 
a central part of the data analysis ecosystem, both in academia and in 
the professional world.

[^big-data]: A dataset is considered small when it can be processed with 
the resources available on a single computer. In the simplest case&mdash;the 
one covered in this book&mdash;the entire dataset can be loaded into a 
computer's main memory. In general, we still speak of «locally manageable» 
data if the dataset can reside on mass storage and be progressively 
processed in main memory, for example by transferring one record at a 
time. When the size of the data greatly exceeds the available mass storage 
capacity (roughly, over one terabyte with currently available hardware), 
we enter the realm of _big data_, which require approaches different from 
those of traditional data analysis.
