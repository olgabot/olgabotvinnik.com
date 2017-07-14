# Ode to first year of grad school

Aka things I wish I knew about when I started grad school

This is half things I didn't know about before grad school, half things that once I started using them, grad school became MUCH better (though that also coincided with the end of third year of the PhD which everyone knows is the worst year so... possibly confounding variable.)

This is relative to when I started my master's at UCSC.

## It's okay to not know anything

As a perfectionist, I hate not knowing things. And it's especially hard to transition from undergrad where you're given a checklist of things to know and you diligently check them off, to graduate school where your research project is a question with no answer.

The way I started feeling better was by aggregating my growing knowledge in a [cheatsheet](https://github.com/olgabot/cheatsheets). I've had multiple cheatsheets over the years and I found that folder of text files was the easiest way to organize the new information. The flipside of this was that I could always look up the useful thing I found during some StackOverflow'ing and save it there for myself so it was always in the same place. Some people use Evernote or other note-taking software for this.

## What you're trying to do is *new* and therefore all the tools don't exist

What I found *very* frustrating at the beginning of graduate school was that what felt like everything I wanted to do was an unexplored edge case of the currently available toolset. Slowly I realized that since nobody's done this stuff before, I have to make everything up. That's what led me to write piles and piles of code.

Related to this: I use [`cookiecutter-python`](https://github.com/audreyr/cookiecutter) as a template for my Python packages. This is very useful as even the boilerplate for making a Python package can be quite cumbersome and confusing. Here's [my fork](https://github.com/olgabot/cookiecutter-pypackage) which uses Anaconda in Travis-CI, but may not be updated to the latest versions of everything.

## Sometimes, tools that do *kind of* what you want *do* exist

The list of tools I wish I could have known about in graduate school is so vast that it deserves its own post.

## Time is citations: How I plan my days

In business, time is money. But in academia, the currency is not published units but citations of your publications. For someone to not only read your paper but understand and cite it, you need to produce high-quality, readable papers. And that requires deep work.

I'm an avid reader of [Cal Newport's blog](http://calnewport.com/blog/) where he writes about managing your attention and energy to output high-quality work. I strongly believe that a person's work output is directly dependent on the hours they spend in deep work. "Deep work" is when you are fully "in the zone" - you have notifications turned off on your phone, you aren't checking your email or social media, and you are fully engaged in your complex activity. For me those activities could be writing or editing a paper, adding new features to my code, carefully curating a well-designed test dataset, tweaking an explanatory figure to make it more clear, working on an upcoming presentation with a new audience, or doing a new analysis of the data.

To help keep track of your deep work, Cal Newport suggests [planning every minute of your day](http://calnewport.com/blog/2013/12/21/deep-habits-the-importance-of-planning-every-minute-of-your-work-day/). It may sound crazy and obsessive-compulsive, but it really works. What he does is plan his day out on paper and adjust the schedule as things happen. I don't like that because then my day looks really messy and I want my "on-paper" plan to be an exact record of what actually happened. Instead, I plan my day out on [Google Calendar](https://calendar.google.com) the day before (during the "shutdown" time) and record what actually happened in a Moleskine daily planner notebook. Additionally, I keep a `self` private GitHub repository containing markdown files for every week, and summarize what I was able to do that day.

Here's the step-by-step of my planning rituals, with pointers to the columns of the figure below.

1. At the beginning of the week, I create a new markdown file and start filling it in with notes from last week and plans for this week. Sometimes my notes start with a big ole rant about some problem I've been running into, or have a big rolling todo list that I keep updated for the week. **The most important thing about each week's file is that each day is separate.** This way, you can keep track of the incremental progress you made that day, and what you hope to accomplish that day. (First column - files for each week)
1. Before each day starts, e.g. during "shutdown" time the day before (or sometimes on Fridays for the next Monday), I plan out what I want to do on Google Calendar. (Second column - plan for each day)
  - I find this works quite well because at the beginning of the day, I'm bursting with energy and want to do *all of the things!* But by the end of the day I've realized that I can only do so much, and I'm much better at prioritizing what's important, while at the beginning of the day I'm much better at *doing* things. So planning at the end of the day works for me.
  - I make sure to schedule 30m for "shutdown" at the end of the day. If I don't do this, the system breaks because I stop planning, and I am at the mercy of my morning impulses, rather than being in control of what I'm trying to do.
1. Throughout the day, I "stopwatch" my time by writing down in my planner the exact minute that I start and stop each activity. (Third column)
1. At the end of the day, during "shutdown," I briefly write down what I was able to do in my markdown document (third column)

When you first start doing it, you may get frustrated that you're not getting much done -- that's okay. Don't get frustrated, just keep tracking. Just like any other goal such as losing weight, results don't come right away.

I work in an "open office" environment which makes doing deep work quite difficult as there is constant movement and potential for interruptions around me. Our lab is quite collaborative so there *are* times when your input or insight is needed for someone's project to go through. I made the mistake of taking this to an extreme and getting very frustrated when people would interrupt me while I was "in the zone" and tried to set boundaries but this closed me off from others. As Richard Hamming says in his fabulous talk, [You and Your Research](http://www.cs.virginia.edu/~robins/YouAndYourResearch.html) about people who closed themselves off:

> I noticed the following facts about people who work with the door open or the door closed. I notice that if you have the door to your office closed, you get more work done today and tomorrow, and you are more productive than most. But 10 years later somehow you don't know quite know what problems are worth working on; all the hard work you do is sort of tangential in importance. He who works with the door open gets all kinds of interruptions, but he also occasionally gets clues as to what the world is and what might be important. Now I cannot prove the cause and effect sequence because you might say, "The closed door is symbolic of a closed mind." I don't know. But I can say there is a pretty good correlation between those who work with the doors open and those who ultimately do important things, although people who work with doors closed often work harder. Somehow they seem to work on slightly the wrong thing - not much, but enough that they miss fame.

So I had to learn to temper this desire to get solid work done and strike a balance between being available and performing intense work. Now, I take lunch off to socialize and chat with the group (rather than working through it), take my headphones off when I am available to work, and when I really need to get work done, I run away and go hide in a place that nobody can find me.


## Rest and hobbies are just as important as deep work

I define hobbies somewhat militantly - they are active activities, not mindless escapes. Hobbies are things that engage your mind in a novel way that doesn't happen during work times. It's something that you're **striving to be better** at in every session, not something you passively consume. For example:

- Any exercise - dancing, climbing, running, gymnastics
- Any art - painting, music, sculpture, novel writing
- Games and Puzzles - crosswords, video games, tabletop puzzles

I list video games because you *can* approach them as something you're trying to improve, rather than a mindless escape.

No, Netflix is not a hobby. Studying French New Wave films or motifs in character development in modern TV series are hobbies. But passively scrolling through Netflix looking for entertainment is not a hobby.


# Sometimes, tools that do *kind of* what you want *do* exist

These are tools I wish I knew about to use when I first started grad school, because they would have greatly relieved

## [Explain SAM flags](https://broadinstitute.github.io/picard/explain-flags.html).

Don't know what a sam flag of `49` means? No worries! Enter the flags


## [`bedtools`](bedtools.readthedocs.io).

What self-respecting bioinformatician could live without `bedtools`?


## [`gffutils`](http://daler.github.io/gffutils/)


## Python's [`itertools`](https://docs.python.org/library/itertools.html)

## Generators in Python - [`yield`](https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/) et al



## [`screen`](https://kb.iu.edu/d/acuy)


But Control-`A` conflicts with the `emacs` shortcut Control-`A` to jump to the beginning of the line, so I remapped it to Control-`J`. Which makes sense in my mind as "Control-Jump"

```
hardstatus on
term xterm-256color
hardstatus alwayslastline
hardstatus string '%{= kG}[ %{G}%H %{g}][%= %{= kw}%?%-Lw%?%{r}(%{W}%n*%f%t%?(%u)%?%{r})%{w}%?%+Lw%?%?%= %{g}][%{B} %m-%d %{W}%c %{g}]'
escape ^jj

# enable scrolling
termcapinfo xterm* ti@:te@
```

## [PyCharm](https://www.jetbrains.com/pycharm/)

This is really about the whole [JetBrains](https://www.jetbrains.com/) suite because they make such fantastic products, but for when your code complexity exceeds Jupyter Notebooks, I highly highly highly recommend using a JetBrains Integrated Development Environment (IDE) for your programming. Any time I have something that's too long for a  notebook (say 20+ lines in a cell), I move it to a Python package, and I use PyCharm to manage my package.

Running tests, renaming things seamlessly, telling you about unused variables and incompliance with PEP8 standards.


## Command-line debugging with `pdb`

Instead of:

```
outrigger index \
    --sj-out-tab outrigger/test_data/tasic2016/unprocessed/sj_out_tab/* \
    --gtf outrigger/test_data/tasic2016/unprocessed/gtf/gencode.vM10.annotation.snap25.myl6.gtf
```

```
python -m pdb outrigger/commandline.py index \
    --sj-out-tab outrigger/test_data/tasic2016/unprocessed/sj_out_tab/* \
    --gtf outrigger/test_data/tasic2016/unprocessed/gtf/gencode.vM10.annotation.snap25.myl6.gtf
```

## `pandas`

specifically, tidy data, `groupby`, and `join`

## `seaborn`

# Document every step of the way, in order that you did it

When I first started, I was optimistic that all the analyses of a single project would fit into a single [Jupyter Notebook](http://jupyter.org/). Hah! That is far, far from the case. Each project will have multiple little annoying steps, and you'll probably not use all of them for the final manuscript. As a result of cramming everything into a single notebook, I completely underestimated how important it is to explicitly document every step that you did, and when you did each step.

Now I have developed the following rules for notebooks:

1. Every notebook does one thing and one thing only
2. Every notebook is named `###_something_descriptive`


## 1. Every notebook does one thing and one thing only

I have made the mistake of enormous notebooks consisting of 100s of cells that need to be run in a specific order. I would include notes like `## Restart Here` so that I knew where to start again, but I've realized that it's much simpler to have separate notebooks for every step. Why? Here are the reasons:

- Much faster loading
  - When a notebook has a lot of stuff in it (especially images), it takes a long time to load so you'll waste time sitting around waiting for your page to load.
- More manageable, Less scrolling
  - With a huge notebook, you'll have to scroll back and forth in a huge document to get to where you need to go. Smaller documents are much easier to use because they exactly can only do a few things
- Less runtime
  -
- Easier on your brain
  - When you have a big document, it can be especially bad if you have to run the cells in a certain order, and that order isn't exactly the order of the cells. For example, if you have to run the last cell first, and then the second cell, you will become easily confused. Separating the cells into separate notebooks, no matter how small they are, separates the pages in your brain so you don't have to.

## 2. Every notebook is named `###_something_descriptive`

This avoids creating notebooks that are impossible to navigate and  tiny-tiny-tiny scroll bars
