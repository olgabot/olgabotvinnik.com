---
title: "CSHL Single Cell Analysis 2017 - Bioinformatics"
date: 2017-07-13T21:38:56-04:00
draft: true
---

# Reflections on teaching math to biologists

# CSHL Single Cell Analysis Course 2017 - Bioinformatics



The Cold Spring Harbor Laboratory (CSHL) Single Cell Analysis Course for 2017
just finished yesterday. I was a co-Instructor and was in charge of the
bioinformatics curriculum. In some ways, teaching at CSHL is a perfect teaching
setting because there are no distractions - the students are there exactly to
just work on the course. However, many of the students had minimal programming
and command line exposure so while they can completely focus on learning, they
also have a lot to catch up on.

This post goes over some lessons learned from this experience


## Expectation vs Reality

Here's what I planned to do in the course

- Students read 4 papers ahead of the course
- We recreate one figure from each of the papers


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
   1. The students have to apply the function in a slightly new way or read
      documentation and add a new parameter

Here's what actually happened

- Students read 4 papers
- We recreated one figure from one paper
- We spent a lot of time talking about Python basics, more than I had
  anticipated

What I would do differently next time:

- Start with simple dataframe manipulation such as with a metadata file
    - show plotting and groupby
- Focus on one paper, and one analysis
  - Take an existing paper and recreate its figures, but also show how to do
    the analysis the "right" way, if it differs from what they did in the paper
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