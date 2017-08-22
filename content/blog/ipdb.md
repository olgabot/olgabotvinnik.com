---
title: "How to use the (Interactive) Python Debugger (ipdb/pdb)"
date: 2017-08-21T16:58:17-07:00
draft: true
tags = ['python', 'debugging']
categories = ['software', 'python']
---

When I can, I prefer to use the interactive Python debugger (`ipdb`) over the
built-in `pdb`, which adds tab completion and better object printing and inspection.
This is especially helpful as `ipdb` understands `pandas` tables much better.
Compare this dataframe printed by `pdb` and `ipdb`.

### Pandas `DataFrame` printed with `pdb`



### Pandas `DataFrame` printed with `ipdb`



## How to use the Python debugger within Python code


```
import ipdb ; ipdb.set_trace()
```


## How to use the Python debugger for command line apps

For example,
when debugging
[dobby](https://github.com/czbiohub/dobby) instead of running `python -m pdb
dobby/cli.py`, I'll run `python -m ipdb dobby.cli.py`.


## Helpful aliases in

To make `pdb` especially
useful, I really like using these aliases which are super helpful to navigate
the stack trace and print the variables you have around.

```bash
# Ned's .pdbrc from https://stackoverflow.com/questions/1623039/python-debugging-tips

# Print a dictionary, sorted. %1 is the dict, %2 is the prefix for the names.
alias p_ for k in sorted(%1.keys()): print "%s%-15s= %-80.80s" % ("%2",k,repr(%1[k]))

# Print the instance variables of a thing.
alias pi p_ %1.__dict__ %1.

# Print the instance variables of self.
alias ps pi self

# Print the locals.
alias pl p_ locals() local:

# Next and list, and step and list.
alias nl n;;l
alias sl s;;l

# Short cuts for walking up and down the stack
alias uu u;;u
alias uuu u;;u;;u
alias uuuu u;;u;;u;;u
alias uuuuu u;;u;;u;;u;;u
alias dd d;;d
alias ddd d;;d;;d
alias dddd d;;d;;d;;d
alias ddddd d;;d;;d;;d;;d
```

Copy the above text into the clipboard and paste it into your `~/.pdbrc` file
with one command:

```
pbpaste > ~/.pdbrc
```

`pbpaste` stands for "Pasteboard" paste, which takes the contents of your
clipboard so you can use it on the command line. There's also `pbcopy` which
you can pipe `stdout` into the clipboard, e.g. to paste your `~/.pdbrc` file:


```
cat ~/.pdbrc | pbcopy
```