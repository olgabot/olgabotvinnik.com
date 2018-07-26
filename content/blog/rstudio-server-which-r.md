---
title: "Rstudio Server Which R"
date: 2018-05-23T10:55:49-07:00
draft: true
tags: []
categories: []
---

Today I ran into the problem of getting my RStudio Server on our remote machine to actually listen to me and use the right version of R. The `.libPaths()` variable showed versions of R that I *didn't* want:

```R
> .libPaths()
[1] "/home/olga/R/x86_64-pc-linux-gnu-library/3.2"
[2] "/usr/local/lib/R/site-library"               
[3] "/usr/lib/R/site-library"                     
[4] "/usr/lib/R/library"                          
```

These [RStudio Desktop ](https://support.rstudio.com/hc/en-us/articles/200486138-Changing-R-versions-for-RStudio-desktop) instructions didn't work for me, but really I was using [RStudio Server configuration instructions](https://support.rstudio.com/hc/en-us/articles/200552316-Configuring-the-Server) and what I had to do was edit the `/etc/rstudio/rserver.conf` file

```bash
$ sudo emacs /etc/rstudio/rserver.conf
```

Here are the contents of `/etc/rstudio/rserver.conf`:


```conf
# Server Configuration File                                                                                                                                            
rsession-which-r=/home/olga/miniconda3/envs/tabula-muris-env-aaron/bin/R
```

And now this points to the right R!

```R
> .libPaths()
[1] "/home/olga/miniconda3/envs/tabula-muris-env-aaron/lib/R/library"
> packageVersion("Seurat")
[1] ‘2.2.1’
```

But upon importing Seurat I got this error:

```R
> source(here("00_data_ingest", "02_tissue_analysis_rmd", "boilerplate.R"))
Loading required package: ggplot2
Loading required package: cowplot

Attaching package: ‘cowplot’

The following object is masked from ‘package:ggplot2’:

    ggsave

Loading required package: Matrix
Error: package or namespace load failed for ‘Seurat’ in dyn.load(file, DLLpath = DLLpath, ...):
 unable to load shared object '/home/olga/miniconda3/envs/tabula-muris-env-aaron/lib/R/library/ranger/libs/ranger.so':
  /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.22' not found (required by /home/olga/miniconda3/envs/tabula-muris-env-aaron/lib/R/library/ranger/libs/ranger.so)
```




```bash
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/
```