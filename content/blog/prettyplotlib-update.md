---
title: "Prettyplotlib update!"
date: 2013-12-23T18:06:00-07:00
draft: false
tags: [python, dataviz, prettyplotlib, pydata]
categories: [text]
---


Check it out: http://nbviewer.ipython.org/github/olgabot/prettyplotlib/blob/master/ipython_notebooks/Examples%20of%20everything%20pretty%20and%20plotted!.ipynb?create=1

Major changes:

* Don't have to supply `ax` object to everything
* All functions return an `ax` object (let me know if this is not true!)
* Added `fill_between` and `fill_betweenx`
* `pcolormesh` accepts `center_value` keyword argument ('kwarg') to re-center diverging colormaps
* Don't change `rcParams` upon import, do everything programmatically
* Major refactoring - every function is now in its own file, java-style (we'll see how that goes..)
