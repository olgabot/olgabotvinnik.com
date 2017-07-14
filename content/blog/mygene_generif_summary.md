---
title: "Beyond Gene Ontology: Getting publication information from gene ids"
date: 2017-07-13T21:38:56-04:00
draft: true
---

## Getting publication information from gene ids

Let's say you have some interesting genes from running a classifier or differential expression or something. But then you do GO analysis and ... NOTHING comes up. Or, the dreaded "`protein_binding`" category, which really just means "hey you found a gene that maybe does stuff."

Well, now you can use `mygene`, a great service from the [Su Lab]() at UCSD which can programmatically look up information about genes from [PubMed]() (aka Google for life scientists). In particular, I've found this incredibly useful for looking up the ["Gene Reference Into Function" (GeneRIF)]() database, which curates snippets from papers that summarize the specific findings, e.g.

> The helical domain of GBP-1 mediates the inhibition of endothelial cell proliferation by inflammatory cytokines.

This `mygene` function is incredibly useful for curating information about many (100s) of genes at a time so that you can read through a single document, rather than spending hours poring over papers to find the few tidbits of information that are actually useful for your project.

First, we'll import `mygene` and initialize the interface.

```
import mygene

# Initialize the "mygene.info" (http://mygene.info/) interface
mg = mygene.MyGeneInfo()
```

We'll use a list of genes I obtained from [GenePattern]()'s [MSigDB]() (Molecular Signatures Database), specifically the genes that ..... In my research, I use [ENSEMBL]() gene IDs (because they're portable from one genome version to the next) and so we'll say that the `scope` we are searching is `'ensembl.gene'`.

- `scope='ensembl.gene'`: What kind of data we're *giving* the service
- `fields=('generif', 'symbol', 'summary')`: What we want to *receive* from the service. I ask for the Gene ReferenceIntoFunction (GeneRIF) information, the gene symbol (i.e. the common name like BRCA1) and the gene summary, which is exactly the summary you get when you read [EntrezGene](https://www.ncbi.nlm.nih.gov/gene).
- `species='human'`: The species of the human we're querying! Don't want to query the mouse database when we have human samples :)


```
mygene_output = mg.querymany([],
                         scopes='ensembl.gene', fields=('generif', 'symbol', 'summary'), species='human')
```

The `mygene_output` is a list of dictionaries

```                         
dfs = []

for line in mygene_output:
    try:
        df = pd.DataFrame(line['generif'])
    except KeyError:
        df = pd.DataFrame()
    df['ensembl_id'] = line['query']
    try:
        df['symbol'] = line['symbol']
    except KeyError:
        continue
    try:
        df['summary'] = line['summary']
    except KeyError:
        continue
    dfs.append(df)


metadata = pd.concat(dfs)
print('metadata.shape', metadata.shape)
metadata.to_csv('mygene_generif_summary.csv'.format(subset_folder), index=False)
```


All together, the code looks like this:
