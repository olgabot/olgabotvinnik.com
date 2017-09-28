---
title: "Python packaging is hard"
date: 2017-09-19T15:41:00-07:00
draft: true
tags: ['python']
categories: ['software', 'open source']
---

The dream of open source is that anyone, anywhere in the world, can share their
code and anyone else can improve it. A key aspect of this is *sharing*, which
is easiset to do when your package is installable using the simplest possible
interface for the language. In the case of Python, that means posting your
package to the Python Package Index (PyPI). Unfortunately, end-to-end
publishing of code is not that easy.

I wrote a Python command line interface
[`abi2fastq`](https://github.com/olgabot/abi2fastq), a super simple command
line interface for converting the rather antiquated format of sequencing files
(Sanger `.ab1`/Applied Biosystem files) to the more commonly used FASTQ format
for input to assembly programs. Even though I already had a working example, I
already knew what testing framedwork and command line interface wrapper I was
going to use, and had already used Travis-CI, CodeCov, PyPI, Bioconda, GitHub,
getting the code up and ready to share with the world was much harder than I
thought it would be. I don't consider myself a super-expert Python programmer
but I've been in the ecosystem for a while so if it's this non-straightfoward
to me then it is a total nightmare for beginners.

## Creating a fresh GitHub repository


## Boilerplate code using `pim`


## Tests using `pytest`


## Setting up continuous integration using Travis-CI


## Measuring coverage using `coverage`


## Measuring Python style guide adherence using `flake8`


## Pushing coverage to the CodeCov.io service


## Use `bumpversion` to increment version numbers

## Why is this so hard?


## Enter `cookiecutter`!
Enter
[`cookiecutter`](https://github.com/audreyr/cookiecutter), a package templater.
Cookiecutter is a nice way that you can set up folder structures and
boilerplate files. For example, I used `cookiecutter` and forked the
[`cookiecutter-reproducible-science`](https://github.com/mkrapp/cookiecutter-reproducible-science)
to set up a simple folder structure for the singlecell-batches project I'm
working on with
[singlecell-batches/cookiecutter-reproducible-science](https://github.com/singlecell-batches/cookiecutter-reproducible-science)


    .
    ├── 00_data
    ├── 01_notebooks
    ├── 02_scripts
    ├── 03_workflows
    ├── 04_figures
    ├── AUTHORS.md
    ├── LICENSE
    ├── README.md
    └── environment.yml

