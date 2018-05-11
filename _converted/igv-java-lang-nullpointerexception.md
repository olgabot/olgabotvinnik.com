---
title: "Fixing issues with Integrated Genomics Viewer (IGV): Null pointer exceptions, invalid GZIP header, invalid BZIP header"
date: 2015-05-06T17:25:59-04:00
draft: false
tags: [bioinformatics, samtools, igv, java]
categories: [bioinformatics]
---


If you've run into a `java.lang.NullPointerException` or "Invalid Gzip Header" or some complaint about bzip while using the Integrative Genomics Viewer, then you've run into the same problem as me. Turns out I had too many index (`*.bai`) files that had similar naming to my `*.bam` files, and IGV assigned the wrong ones as the index, so whenever I tried to view reads from those samples, the index pointed to the wrong location in the bam, and one of those many errors would happen. So the solution is simple (and relatively fast): use `samtools index` on your bam files!