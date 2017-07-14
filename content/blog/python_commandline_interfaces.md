# Side-by-side comparison of Python command line interfaces (CLIs)

[Article advocating *against* `click`](http://xion.io/post/programming/python-dont-use-click.html)
(2016-05-20)

[Comparison of `argparse`, `docopt`, and `click`](https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/)
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
have always hesitated. For you, my dear reader, I have written out the very
long `argparse` version (Yes I know it doesn't have to be this long but I like
being thorough)


## [argparse](https://docs.python.org/3/library/argparse.html)



<table>
  <tr>
    <th><pre>argparse</pre></th>
    <th><pre>click</pre></th>
    <th><pre>fire</pre></th>
  </tr>
  <tr>
    <td>
<pre style="font-family:Consolas,Inconsolata,Courier,monospace;font-size:1em;line-height:1.3em;margin:1.2em 0;"><code class="python" style="background-color:#f8f8f8;border-radius:3px;border:1px solid #ccc;display:block;font-family:Consolas,Inconsolata,Courier,monospace;font-size:0.9em;margin:0 0.15em;overflow:auto;padding:0.5em 0.7em;white-space:pre;color:#444;">## --- Contents of commandline.py --- ##
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
                            help=&quot;Which letters to search for in the fasta &quot;
                                 &quot;file. Default is '{}'.&quot;.format(
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

        print &gt;&gt; sys.stderr, str
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
</code></pre>
</td>
    <td>Doe</td>
  </tr>
</table>



## [click](http://click.pocoo.org/5/)


### Code

Below are the contents of `commandline.py`

```python
#!/usr/bin/env python
from __future__ import print_function

import click

import kvector

@click.command()
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
              help='Number of threads/processors to use for parallel processing'
                   ' of a multithreaded job. Default is -1, which uses the '
                   'maximum number of threads available, via the "joblib" '
                   'module.')
@click.version_option(version=kvector.__version__)
def cli(bed, fasta, intersect, kmer_lengths, residues, threads):
    """Counts k-mers in the bed intervals and writes a csv to stdout

    \b
    Parameters
    ----------
    bed : str
        Location of a bed file of the genomic intervals whose k-mers you want
        to count
    fasta : str
        Path to the genome fasta file containing all chromosomes. Must be
        indexed (usually has a `.fai` file in the same directory, created
        using `faidx`).
    """

    kmer_lengths = tuple(map(int, kmer_lengths.split(',')))

    kmers = kvector.per_interval_kmers(bed, fasta, intersect=intersect,
                                       kmer_lengths=kmer_lengths,
                                       residues=residues, threads=threads)
    click.echo(kmers.to_csv())


if __name__ == '__main__':
    cli()
```

The `\b` is necessary to prevent rewrapping of the `Parameters` paragraph,
otherwise it would all be forced to flow together.

### Example help output

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

## [fire]() from Google

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
