---
title: "How to use the (Interactive) Python Debugger (ipdb/pdb)"
date: 2017-08-21T16:58:17-07:00
draft: true
tags: ['python', 'debugging']
categories: ['software', 'python']
---

When I can, I prefer to use the interactive Python debugger (`ipdb`) over the
built-in `pdb`, which adds tab completion and better object printing and inspection.
This is especially helpful as `ipdb` understands `pandas` tables much better.
Compare this dataframe printed by `pdb` and `ipdb`.

### Pandas `DataFrame` printed with `pdb`



### Pandas `DataFrame` printed with `ipdb`

```
ipdb> fluorescence.head()
        1        2        3        4        5        6        7        8   \
A  1607623   870255  1473596   822329  2606790   915395   743408   839900   
B  1526862  1549455   736932  1381884   724205   739192  2506348  2984756   
C   802298   717058  2193970  1339812  2431480   707961   893018  1330707   
D   923225  1641454  1607814  1831640   828121  1363558  1084257   947216   
E  1765777  1698291   722003  1755268  1005841  1896726   648793   643921   

        9        10   ...          15       16       17       18       19  \
A  1680346  2601054   ...     1559793   668853   742214   773718   758931   
B   761838   788951   ...     1185720   727802  1655809   726753   732393   
C  2380715   742939   ...     1537176   784172  1649059   720813  1239116   
D   729707  2822514   ...     1407914   640962  1171847  4051558  3224590   
E  1214801  1159885   ...     3214236  4515606  1725177  1594698  1216301   

        20       21       22      23       24  
A   659945  1482332   687784  698864  6942884  
B  1628888   602365  1679494  680780  6505976  
C  1916442   760324  1206095  678499  5812210  
D   710349   753823  1173053  743266  5981866  
E  1285544  1661882   694574  693239  4044818  

[5 rows x 24 columns]
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


## How to use the Python debugger within Python code


```python
import pdb; pdb.set_trace()
means = fluorescence[standards_col].groupby(standards).mean()
regressed = linregress(means.index, means)
```

Here we

```
-> means = fluorescence[standards_col].groupby(standards).mean()
(Pdb) means
*** NameError: name 'means' is not defined
(Pdb) nl
KeyError: 8.0
> /Users/olgabot/code/dobby/dobby/convert.py(27)_fluorescence_to_concentration()
-> means = fluorescence[standards_col].groupby(standards).mean()
 22  	    """
 23  	    if isinstance(standards, str):
 24  	        standards = [float(x) for x in standards.split(',')]
 25  	
 26  	    import pdb; pdb.set_trace()
 27  ->	    means = fluorescence[standards_col].groupby(standards).mean()
 28  	    regressed = linregress(means.index, means)
 29  	
 30  	    if regressed.rvalue < r_minimum:
 31  	        raise ValueError(
 32  	            f'{platename} Regression failed test: '
```