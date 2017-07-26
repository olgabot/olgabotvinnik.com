---
title: "CSHL Single Cell Analysis 2017 - Bioinformatics"
date: 2017-07-13T21:38:56-04:00
draft: false
---

# Reflections on teaching math to biologists

[TOC]: # "Table of Contents"

# Table of Contents
- [Expectation vs Reality](#expectation-vs-reality)
    - [What I planned to do in the course](#what-i-planned-to-do-in-the-course)
    - [What actually happened](#what-actually-happened)
- [Bugs I ran into](#bugs-i-ran-into)
- [Lessons learned: What I would do differently next time](#lessons-learned-what-i-would-do-differently-next-time)



The Cold Spring Harbor Laboratory (CSHL)
[Single Cell Analysis Course](https://meetings.cshl.edu/courses.aspx?course=C-SINGLE&year=17)
(not to be confused with the "Single Cell *Analyses*" Meeting) for 2017 just
finished a few weeks ago. I was a co-Instructor and was in charge of the
bioinformatics curriculum. In some ways, teaching at CSHL is a perfect teaching
setting because there are no distractions - the students are there exactly to
just work on the course. However, many of the students had minimal programming
and command line exposure so while they can completely focus on learning, they
also have a lot to catch up on.

This post goes over some lessons learned from this experience. If you want all
the teaching materials, I made a
[github repo](http://github.com/olgabot/cshl-singlecell-2017) containing all of
the notebooks we used in the course.


## Expectation vs Reality

As always, what you planned isn't what actually happened.

### What I planned to do in the course




To help prepare students for any possible single cell question they run into, I
wanted to expose them to several papers' different methods of analysis. I
wanted paoers covering four common questions in single cells

1. Dissociate a tissue --> ??? --> Celltypes!
2. Treatment vs control, in a singlecell context
3. Molecular transformations over time ("pseudotime")
4. Perturbations + single-cell RNA-seq

Therefore in an ideal setting, we would have done:
- Students read 4 papers ahead of the course
- We recreate one figure from each of the papers
- We'd cover all possible questions that could be answered using single-cell RNA-seq


### What actually happened

- Students read 4 papers
- We recreated *one* figure from *one* paper
- We spent a lot of time talking about Python basics, much more than I had
  anticipated
- We didn't get to answering every possible single-cell question
- We spent far less time on the "interesting" part of bioinformatics -
  interpretation of results

I often let "perfect be the enemy of good" and would not fully reuse a lesson
from last year because it was from last year's papers, even if the concepts or
programming commands were the same.

The way I designed the notebooks was there were two notebooks for each concept:
1. Explain a mathematical concept using images, animations, and
   interactive Jupyter widgets.
   1. Assessment: Class discussion, calling on `random_student()` to explain
      the question
2. Show how the plot from the previous figure was created with complete
   step-by-step breakdowns of each function and parameter
   1. Assessment: the students have to apply the function in a slightly new way
      or read documentation and add a new parameter


## Bugs I ran into

- [Jake VDP's Scikit-learn](https://github.com/jakevdp/sklearn_tutorial)
  tutorial, while excellent, has not been updated to the most recent version of
  Jupyter/IPython widgets. Specifically, the syntax for specifying

## Lessons learned: What I would do differently next time

- Start with simple dataframe manipulation such as with a metadata file
    - show plotting and groupby
- Focus on *one paper*, and *one analysis*
  - Take an existing paper and recreate its figures, but also show how to do
    the analysis the "right" way, if it differs from what they did in the paper
  - Start from the end - what commands and concepts do they need to know by the
    end of the analysis? How can we build towards that?
- Using a single dataset and analyzing it all the way through would help the
  students get deeper into a single problem, rather than exposing them to a lot
  of random stuff
- Don't expect that people have any experience when we start. Start out the
  course with an overview of Python and programming

One of the hardest things about designing a curriculum like this is finding a
good dataset to showcase all of these analyses on. It's hard to find a single
paper that covers all possible questions, but maybe that's alright. I always
have to remind myself that "good enough" but shipped is still better than
perfect and unrelease.

The good thing is that these mistakes made me write out my
[learning goals](https://github.com/olgabot/cshl-singlecell-2017/blob/master/learning-goals.md)
for the different sections of the course. I remember now from Software
Carpentry teacher training (
[Lessons and Objectives](https://swcarpentry.github.io/instructor-training/19-lessons/))
that I should have done this in the beginning, but hey, you live and you learn.