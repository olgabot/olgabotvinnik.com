---
title: "Side-by-side comparison of Python command line interfaces (CLIs)"
date: 2017-08-28T18:57:02-07:00
draft: true
---


-
[Article advocating *against* `click`](http://xion.io/post/programming/python-dont-use-click.html)
(2016-05-20)
- [Comparison of `argparse`, `docopt`, and `click`](https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/)
  (2015-09-06)

If you're like me, you wake up in the middle of the night while dreaming about
your packages in terror, "But I have to write a command line interface!!?!?" In
Python, the accepted command line interface (CLI) that lets you do a lot of
help documentation is called `argparse`. But, it can be quite clunky to d this.

For example, I have a small package called
[`kvector`](https://github.com/olgabot/kvector/) which can be used to count
*k*-mers (DNA words) in specified places in the genome, so you can compare for
enrichment between conditions. So far, I've only worked with it within Python
and have meant to turn this into a command line interface for some time, but
have always hesitated. But for you, my dear reader, I have taken the plunge.


[TOC]: # "Table of Contents"

# Table of Contents
- [Anatomy of a CLI in Python](#anatomy-of-a-cli-in-python)
    - [What is `__main__`?](#what-is---main--)
    - [What is `#!/usr/bin/env python`?](#what-is-usrbinenv-python)
    - [Simple CLI with a contrived example](#simple-cli-with-a-contrived-example)
- [`argparse` from the Python standard library](#argparse-from-the-python-standard-library)
    - [Example help output with `argparse`](#example-help-output-with-argparse)
- [[click](http://click.pocoo.org/5/)](#click)
    - [Code](#code)
    - [Example command with no arguments in `click`](#example-command-with-no-arguments-in-click)
    - [Example help output with `click`](#example-help-output-with-click)
- [`fire` from Google](#fire-from-google)
    - [Example output](#example-output)
- [Conclusions](#conclusions)

## Anatomy of a CLI in Python

### What is `__main__`?

In writing a command line interface in Python, you must always have the
following line:

```python
if __name__ == "__main__":
```

What does this line do? If the special variable `__name__` for the file is set
to `__main__`, that means that it was run from the command line.

### What is `#!/usr/bin/env python`?

If you want to run your command always with `python cli.py`, then you don't
need this "crunch bang" ("`#`" for crunch and "`!`" for "bang") line. However,
if you'd like to make your life a little simpler and run the file with
`/.cli.py`, then you need to do some extra work. The `#!/usr/bin/env python`
tells the operating system to use Python to interpret the text of the file into
a compiled program. Then you can set the mode of the file as an executable
using `chmod +x cli.py`. This may not be necessary with all CLIs but it is good
practice as it unambiguously sets the language of the program you are creating.f

### Simple CLI with a contrived example

```python
#!/usr/bin/env python

if __name__ == "__main__":
    # run cli
```



## `argparse` from the Python standard library

[argparse](https://docs.python.org/3/library/argparse.html) is the currently
accepted method of writing CLIs.

I have written out the very long `argparse` version. I know it doesn't have to
be this long but I like being thorough. The skeleton for this parser came from
David Deamer at UCSC from the "Bioinformatics Algorithms" course.


```python
#!/usr/bin/env python

import argparse

import kvector


class CommandLine(object):
    def __init__(self, inOpts=None):
        self.parser = parser = argparse.ArgumentParser(
            description='Counts k-mers in the bed intervals and writes a csv '
                        'to stdout', version=kvector.__version__)
        parser.add_argument('bed', required=True, type=str, action='store',
                            help='Location of a bed file of the genomic '
                                 'intervals whose k-mers you want to count')
        parser.add_argument('fasta', required=True, type=str, action='store',
                            help='Fasta files of the genome from which the '
                                 'intervals are derived. Must be indexed '
                                 '(usually has a `.fai` file in the same '
                                 'directory, created by `samtools faidx`)')
        parser.add_argument('--intersect', required=False, type=str,
                            action='store',
                            help='Bed file of other regions, e.g. conserved '
                                 'elements, that you want to intersect when '
                                 'searching for k-mers.')
        parser.add_argument('--kmer-lengths', default='4,5,6',
                            action='store', type=str,
                            help='How long of DNA words to search for (aka '
                                 'values of k).')
        parser.add_argument('--residues', default=kvector.kmer.DNA,
                            action='store', type=str,
                            help="Which letters to search for in the fasta "
                                 "file. Default is '{}'".format(
                                 kvector.kmer.DNA))
        parser.add_argument('--threads', default=-1,
                            action='store', type=str,
                            help='Number of threads/processors to use for '
                                 'parallel processing of a multithreaded job. '
                                 'Default is -1, which uses the maximum '
                                 'number of threads available, via the '
                                 '&quot;joblib&quot; module.')
        if inOpts is None:
            self.args = vars(self.parser.parse_args())
        else:
            self.args = vars(self.parser.parse_args(inOpts))

    def do_usage_and_die(self, str):
        '''
        If a critical error is encountered, where it is suspected that the
        program is not being called with consistent parameters or data, this
        method will write out an error string (str), then terminate execution
        of the program.
        '''
        import sys

        sys.stderr.write(str)
        self.parser.print_usage()
        return 2


class Usage(Exception):
    '''
    Used to signal a Usage error, evoking a usage statement and eventual
    exit when raised
    '''

    def __init__(self, msg):
        self.msg = msg



if __name__ == '__main__':
    try:
        cl = CommandLine()

        kmer_lengths = tuple(map(int, cl.kmer_lengths.split(',')))

        kmers = kvector.per_interval_kmers(cl.bed, cl.fasta,
                                           intersect=cl.intersect,
                                           kmer_lengths=kmer_lengths,
                                           residues=cl.residues,
                                           threads=cl.threads)
        print(kmers.to_csv())

    except Usage, err:
        cl.do_usage_and_die()
```

### Example help output with `argparse`



## [click](http://click.pocoo.org/5/)


### Code

Below are the contents of `commandline.py` for `kvector` written in `click.

```python
#!/usr/bin/env python
from __future__ import print_function

import click

import kvector

settings = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=settings)
@click.argument('bed', type=click.Path(dir_okay=False))
@click.argument('fasta', type=click.Path(dir_okay=False))
@click.option('--intersect',
              help='Bed file of other regions, e.g. conserved elements, that '
                   'you want to intersect when searching for k-mers.')
@click.option('--kmer-lengths', default='4,5,6',
              help='How long of DNA words to search for (aka values of k). '
                   'Default is "4,5,6".')
@click.option('--residues', default=kvector.kmer.DNA,
              help="Which letters to search for in the fasta file. Default is "
                   "'{}'.".format(kvector.kmer.DNA))
@click.option('--threads', default=-1,
              help='Number of threads/processors to use for parallel '
                   'processing of a multithreaded job. Default is -1, which '
                   'uses the maximum number of threads available, via the '
                   '"joblib" module.')
@click.version_option(version=kvector.__version__)
def cli(bed, fasta, intersect=None, kmer_lengths='4,5,6',
        residues=kvector.kmer.DNA, threads=-1):
    """Counts k-mers in the bed intervals and writes a csv to stdout

    \b
    Parameters
    ----------
    bed : str
        Location of a bed file of the genomic intervals whose k-mers you want
        to count
    fasta : str
        Path to the genome fasta file containing all chromosomes. Must be
        indexed (usually has a `.fai` file in the same directory, usually
        created using `samtools faidx`).
    """

    kmer_lengths = tuple(map(int, kmer_lengths.split(',')))

    kmers = kvector.per_interval_kmers(bed, fasta, intersect=intersect,
                                       kmer_lengths=kmer_lengths,
                                       residues=residues, threads=threads)
    click.echo(kmers.to_csv())


if __name__ == '__main__':
    cli()
```

Notice that in `click`, there is a strong distinction between `arguments`,
which are positional and `options` which use flags. Below are some more
distinctions that `click` makes with regards to arguments vs options.

**Arguments**
- Positional
- Required
- Documented in the docstring, cannot take `help` as an argument in `click.argument()`
  - Note: The `\b` is necessary in the docstring to prevent rewrapping of the
    `Parameters` paragraph, otherwise it would all be forced to flow together.

**Options**
- Not positional
- Use flags
- Documented as the `help` argument in the `click.option()` initialization


Other "gotchas" in click:

- `--help` is the default help flag, if you want `-h` to also indicate help
  then you need to pass `dict(help_option_names=['-h', '--help'])` to `click.command()`
-

This is
a very "opinionated" view of command line interfaces and if you don't mind
using this style of inputs, then `click` is much easier to use than `argparse`.


### Example command with no arguments in `click`

```
$ kvector
Usage: kvector [OPTIONS] BED FASTA

Error: Missing argument "bed".
```


### Example help output with `click`

```
$ kvector --help  
Usage: kvector [OPTIONS] BED FASTA

  Counts k-mers in the bed intervals and writes a csv to stdout

  Parameters
  ----------
  bed : str
      Location of a bed file of the genomic intervals whose kmers you want
      to count
  fasta : str
      Path to the genome fasta file containing all chromosomes. Must be
      indexed (usually has a `.fai` file in the same directory, created
      using `faidx`).

Options:
  --intersect TEXT     Bed file of other regions, e.g. conserved elements,
                       that you want to intersect when searching for k-mers.
  --kmer-lengths TEXT  How long of DNA words to search for (aka values of k).
                       Default is "4,5,6".
  --residues TEXT      Which letters to search for in the fasta file. Default
                       is 'ACGT'.
  --threads INTEGER    Number of threads/processors to use for paralell
                       processing of a multithreaded job. Default is -1, which
                       uses the maximum number of threads available, via the
                       "joblib" module.
  --version            Show the version and exit.
  --help               Show this message and exit.
```

## `fire` from Google

[fire]()

### Example output

I couldn't figure out how to add `--help` documentation or anything

Bare command:

```
$ python kvector/kmer.py
print_function:     _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 65536)
itertools:          <module 'itertools' (built-in)>
SeqIO:              <module 'Bio.SeqIO' from '/Users/olgabot/anaconda3/envs/kvector-fire/lib/python3.6/site-packages/Bio/SeqIO/__init__.py'>
joblib:             <module 'joblib' from '/Users/olgabot/anaconda3/envs/kvector-fire/lib/python3.6/site-packages/joblib/__init__.py'>
np:                 <module 'numpy' from '/Users/olgabot/anaconda3/envs/kvector-fire/lib/python3.6/site-packages/numpy/__init__.py'>
pd:                 <module 'pandas' from '/Users/olgabot/anaconda3/envs/kvector-fire/lib/python3.6/site-packages/pandas/__init__.py'>
pybedtools:         <module 'pybedtools' from '/Users/olgabot/anaconda3/envs/kvector-fire/lib/python3.6/site-packages/pybedtools/__init__.py'>
fire:               <module 'fire' from '/Users/olgabot/anaconda3/envs/kvector-fire/lib/python3.6/site-packages/fire/__init__.py'>
DIRECTIONS:         ["upstream", "downstream"]
RNA:                ACGU
DNA:                ACGT
score_kmers:        <function score_kmers at 0x10f7ecea0>
count_kmers:        <function count_kmers at 0x117e7cae8>
make_kmers:         <function make_kmers at 0x117e91e18>
per_interval_kmers: <function per_interval_kmers at 0x117e91f28>

```


#### Subcommand `count_kmers`

```
$ python kvector/kmer.py count_kmers
Fire trace:
1. Initial component
2. Accessed property "count_kmers"
3. ('The function received no value for the required argument:', 'filename')

Type:        function
String form: <function count_kmers at 0x10a5fe8c8>
File:        ~/code/kvector/kvector/kmer.py
Line:        55
Docstring:   Observe the number of substrings of specific lengths in sequence file

A k-mer is a DNA (or RNA!) "word" of a specific length "k".

Parameters
----------
filename : str
    Name of a sequence file
kmer_lengths : list of ints
    Lengths of the kmers to count. 8 or more (4^8 sequences) is generally
    not storable in memeory
format : str, optional
    Format of the sequence file. Default is "fasta"
residues : str, optional
    The residues to count, default is "ACGT" (DNA)

Returns
-------
kmer_matrix : pandas.DataFrame
    A (kmers, sequences) dataframe of the kmers observed

Usage:       kmer.py count_kmers FILENAME [KMER_LENGTHS] [FORMAT] [RESIDUES]
             kmer.py count_kmers --filename FILENAME [--kmer-lengths KMER_LENGTHS] [--format FORMAT] [--residues RESIDUES]
(kvector-fire) ➜  kvector git:(cli-fire) ✗ 
```


## Conclusions

As always, it depends on your needs :)

- If you are in the early stages of software development and need a quick and
  dirty CLI to debug your code or run someone else's code, then `fire` is
  superb. It's dead simple to set up and beautifully turns your pile of code
  into a command line interface.
- If you are in the later stages of software development and need something
  user-friendly and want to have nice, helpful documentation, want to control
  the names of the inputs and the are okay with an opinionated CLI builder,
  then `click` is the way to go.
- If you want to control everything about your argument parsing, use `argparse`
