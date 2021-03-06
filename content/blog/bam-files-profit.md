---
title: ".bam files --> ??? ---> profit!"
date: 2012-08-24T13:22:00-07:00
draft: false
tags: []
categories: [text]
---

<div class="posterous_autopost">
<p>
<img src="http://media.tumblr.com/tumblr_mde7hsADmq1rw6gvj.png" alt="The vision for this software" />
</p>
<h1>
RNA-Sequencing results in one step!
</h1>
<p>
A departure from the usual productivity theme, I pleased to announce the release of my RNA-Sequencing differential expression (RSDE for short) package, <a href="https://github.com/olgabot/rna-seq-diff-exprn">available on Github</a>. I have worked on this package for the past 4 months and have put a lot of effort into making it as easy to use as possible, so please let me know if you run into any issues.
</p>
<p>
My vision of how easy it should be to use is outlined in the headline photo and title:
</p>
<blockquote>
<p>
<code>.bam</code> files —-&gt; ??? —&gt; Results!
</p>
</blockquote>
<p>
Structural variant detection is grey because it is not yet available.
</p>
<p>
The example included in the code looks at the differential expression of two prostate cancer cell lines, LNCaP and PrEC. It only includes reads from chromosome 9, an arbitrary choice to reduce the time of running the example. Currently, the example takes 20 minutes to run on my laptop (MacBook Pro, Late 2008 model, 2.4G Hz Intel Core Duo, 4 GB RAM), and this is really supposed to be run on a server that holds all your gigantic (10gb+) <code>.bam</code> files. If you do choose to run it on your own personal computer, I would recommend leaving your computer alone while it runs, or else your entire machine may crash. Mine has.
</p>
<h1>
The inputs
</h1>
<p>
Basically, the inputs are (they will be more thoroughly described below):
</p>
<ol>
<li>
Output directory
</li>
<li>
Metadata file with the <code>.bam</code> file locations, sample IDs, and experiment descriptions
</li>
<li>
Gene transfer format file (GTF file, a subset of the General Feature Format, GFF filetypes) of genes for your species
</li>
<li>
GTF file processed with DEXSeq, a differential exon usage program.
</li>
<li>
Browser-extensible data (BED) file of genes for your species. Both the BED and GTF files are needed for the different transcript-counting programs (<code>bedtools Coverage</code> and <code>htseq-count</code>)
</li>
<li>
Transcript ID – Symbol file (explained below)
</li>
<li>
“Genome” file. This is available in your BEDTools distribution for mouse and human (mm8, mm9, hg18 and hg19), and I’ll show you an example of one so you can create one for other species, too.
</li>
<li>
“Karyotype” file for <a href="http://circos.ca/">Circos</a> plotting. This is available in your Circos distribution for mouse and human (mm8, mm9, hg18 and hg19), and again, I’ll show you an example so you can create your own.
</li>
<li>
Gene density file, for <a href="http://circos.ca/">Circos</a> plotting. I have created one for humans (hg19) and will give instructions and a script for how to create one on your own.
</li>
<li>
GC content file, for <a href="http://circos.ca/">Circos</a> plotting. I have one for humans, chromosome 9 (it takes a long time to plot if it is very dense, so I chose a subset of the genome), and will show you how to create your own
</li>
<li>
Number of “bunches” you’d like to create (more on this later)
</li>
</ol>
<h1>
The outputs
</h1>
<p>
And after submitting all those files and waiting ~20 min for the example to finish, you get:
</p>
<ol>
<li>
Quality-control plots of the <code>.bam</code> files, via <a href="http://code.google.com/p/rseqc/">RSeQC</a>. Most of the commands listed in the <a href="http://code.google.com/p/rseqc/wiki/Manual">manual</a> are performed. In alphabetical order, they are (with documentation copy/pasted from the RSeQC manual):
<ol>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#clipping_profile.py"><code>clipping_profile.py</code></a>: This program is used estimate clipping profile of RNA-seq reads from BAM or SAM file. Note that to use this function, CIGAR strings within SAM/BAM file should have <code>S</code> operation (This means your reads mapper should support clipped mapping).
</li>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#geneBody_coverage.py"><code>geneBody_coverage.py</code></a>: Read coverage over gene body. This module is used to check if reads coverage is uniform and if there is any 5’/3’ bias. This module scales all transcripts to 100 nt and calculates the number of reads covering each nucleotide position. Finally, it generates a plot illustrating the coverage profile along the gene body. NOTE: this module requires lots of memory for large BAM files, because it load the entire BAM file into memory.
<ol>
<li>
This is a VERY useful function to look at how fully covered the transcripts are in your experiment. I highly recommend taking a look at the gene body coverage before interpreting differential expression.
</li>
</ol>
</li>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#geneBody_coverage.py"><code>infer_experiment.py</code></a>: This program is used to speculate how RNA-seq sequencing were configured, especially how reads were stranded for strand-specific RNA-seq data, through comparing reads' mapping information to the underneath gene model.
<ol>
<li>
Note: currently, RPKM_count.py does not take in the infer_experiment data but will in the future.
</li>
</ol>
</li>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#inner_distance.py"><code>inner_distance.py</code></a>: This module is used to calculate the inner distance (or insert size) between two paired RNA reads. The distance is the mRNA length between two paired fragments.
</li>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#junction_annotation.py"><code>junction_annotation.py</code></a>: For a given alignment file (<code>-i</code>) in BAM or SAM format and a reference gene model (<code>-r</code>) in BED format, this program will compare detected splice junction to reference gene model.
</li>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#junction_saturation.py"><code>junction_saturation.py</code></a>: It’s very important to check if current sequencing depth is deep enough to perform alternative splicing analyses. For a well annotated organism, the number of expressed genes in particular tissue is almost fixed so the number of splice junctions is also fixed,　all splice junctions can be predetermined according to reference gene model. All (annotated) splice junctions should be rediscovered from a saturated RNA-seq data, otherwise, downstream alternative splicing analysis is problematic because low abundance splice junctions are missing. This module checks for saturation by resampling 5%, 10%, 15%, …, 95% of total alignments from BAM or SAM file, and then detects splice junctions from each subset and compares them to reference gene model.
</li>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#read_distribution.py"><code>read_distribution.py</code></a>: Provided a BAM/SAM file and reference gene model, this module will calculate how mapped reads were distributed over genome feature (like CDS exon, 5'UTR exon, 3' UTR exon, Intron, Intergenic regions). When genome features are overlapped (e.g. a region could be annotated as both exon and intron by two different transcripts) , they are prioritize as: CDS exons &gt; UTR exons &gt; Introns &gt; Intergenic regions, for example,if a read was mapped to both CDS exon and intron, it will be assigned to CDS exons.
</li>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#read_duplication.py"><code>read_duplication.py</code></a>: Two strategies were used to determine reads duplication rate:
<ol>
<li>
Sequence based: reads with exactly the same sequence content are regarded as duplicated reads.
</li>
<li>
Mapping based: reads mapped to the same genomic location are regarded as duplicated reads. For splice reads, reads mapped to the same starting position and splice the same way are regarded as duplicated reads.
</li>
</ol>
</li>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#read_GC.py"><code>read_GC.py</code></a>
<ol>
<li>
Finds the GC content of your reads and outputs a histogram plot.
</li>
</ol>
</li>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#read_NVC.py"><code>read_NVC.py</code></a>: This module is used to check the nucleotide composition bias. Due to random priming, certain patterns are over represented at the beginning (5'end) of reads. This bias could be easily examined by NVC (Nucleotide versus cycle) plot. NVC plot is generated by overlaying all reads together, then calculating nucleotide composition for each position of read (or each sequencing cycle). In ideal condition (genome is random and RNA-seq reads is randomly sampled from genome), we expect A%=C%=G%=T%=25% at each position of reads.
<ol>
<li>
I also highly recommend looking at this plot and possibly trimming the first 6-9bp of your reads.
</li>
</ol>
</li>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#read_quality.py"><code>read_quality.py</code></a>: According to SAM specification, if Q is the character to represent “base calling quality” in SAM file, then Phred Quality Score = <code>ord(Q) - 33</code>. Here <code>ord()</code> is python function that returns an integer representing the Unicode code point of the character when the argument is a unicode object, for example, <code>ord('a')</code> returns 97. Phred quality score is widely used to measure “reliability” of base-calling, for example, phred quality score of 20 means there is 1/100 chance that the base-calling is wrong, phred quality score of 30 means there is 1/1000 chance that the base-calling is wrong. In general: Phred quality score = <code>-10*log10P</code>, here <code>P</code> is probability that base-calling is wrong.
</li>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#RPKM_count.py"><code>RPKM_count.py</code></a>: Given a BAM file and reference gene model, this program will calculate the raw count and RPKM values for transcript at exon, intron and mRNA level. For strand specific RNA-seq data, program will assign read to its parental gene according to strand rule, if you don’t know the strand rule, run <code>infer_experiment.py</code>. Please note that chromosome ID, genome cooridinates should be concordant between BAM and BED files.
</li>
<li>
<a href="http://code.google.com/p/rseqc/wiki/Manual#RPKM_saturation.py"><code>RPKM_saturation.py</code></a>: The precision of any sample statitics (RPKM) is affected by sample size (sequencing depth); “resampling” or “jackknifing” is a method to estimate the precision of sample statistics by using subsets of available data. This module will resample a series of subsets from total RNA reads and then calculate RPKM value using each subset. By doing this we are able to check if the current sequencing depth was saturated or not (or if the RPKM values were stable or not) in terms of genes' expression estimation. If sequencing depth was saturated, the estimated RPKM value will be stationary or reproducible. By default, this module will calculate 20 RPKM values (using 5%, 10%, … , 95%,100% of total reads) for each transcripts. Although people can use KPSS test to determine if the estimated RPKM level is in stationary or not. Visual inspection is more accurate.
</li>
</ol>
</li>
<li>
Genome-wide coverage of all samples, visualized by a <a href="http://circos.ca">Circos</a> plot. The example only includes reads mapped to chromosome 9, so the example plot only shows coverage from chromosome 9.
</li>
<li>
Transcript counts, counted by two methods:
<ol>
<li>
BEDTools, via <code>bedtools coverage</code>
</li>
<li>
HTSeq, via <code>htseq-count</code>
</li>
</ol>
</li>
<li>
Differential Expression analysis, by <code>DESeq</code> (in the <code>R</code> programming language). This include gene lists and heat maps.
<ol>
<li>
Other differential expression methods (NOISeq, DEXSeq) are in the works
</li>
</ol>
</li>
<li>
(Not yet: Structural Variant detection, e.g. of fusion genes via SVDetect)
</li>
</ol>
<h1>
Input files: A thorough description
</h1>
<h2>
Output directory
</h2>
<p>
This is where all the results files will be. Folders that will be created are:
</p>
<p>
The basic directories are:
</p>
<div class="CodeRay">
<div class="code">
<pre>expression/ rseqc/ circos/</pre>
</div>
</div>
<p>
Quality control files go in:
</p>
<div class="CodeRay">
<div class="code">
<pre>rseqc/[all your sample ids]</pre>
</div>
</div>
<p>
Circos files go in:
</p>
<div class="CodeRay">
<div class="code">
<pre>circos/[all your sample ids]</pre>
</div>
</div>
<p>
The counts files will go in:
</p>
<div class="CodeRay">
<div class="code">
<pre>expression/bedtools/[all your sample ids] expression/htseq/[all your sample ids]</pre>
</div>
</div>
<p>
Heatmaps will go:
</p>
<div class="CodeRay">
<div class="code">
<pre>expression/bedtools/figures/ expression/hsteq/figures/</pre>
</div>
</div>
<h2>
Metadata file
</h2>
<ul>
<li>
What: Description of the input data files, where they are, sample IDs, a “group” such as a treatment type, and details of the RNA-Seq experiment
</li>
<li>
Used by: Entire pipeline
</li>
<li>
Example file: <code>test-data/conditions_chr9.tab</code>
</li>
</ul>
<p>
Text of example file:
</p>
<div class="CodeRay">
<div class="code">
<pre># These data are a subset of http://0-www.ncbi.nlm.nih.gov.elis.tmu.edu.tw/geo/query/acc.cgi?acc=GSE27619 from GEO, specifically:
# GSM721116, GSM721117, GSM721118, GSM721119, GSM721123, GSM721124 
## LNCaP and PrEC are the names of prostate cancer cell lines used in this GEO dataset 
## As you may have noticed, any lines starting with a hash (`#') are ignored 
## This file is based on the columns, so if you add extraneous columns, they will not be read into the program (ie you can add comments) 
#### 
# This is a tab-delimited file, with the following columns: 
# bam_prefix     id     group     gender     read_type     strandedness 
## bam_prefix = the filename, without the .bam 
## id = (user-defined, could be anything) 
## group = (user-defined, could be anything) 
## gender = male --or-- female 
## read_type = single_read --or-- paired_end 
## strandedness = whether the cDNA library preparation was strand-specific or not. values = &quot;strand_specific&quot; --or-- &quot;not_strand_specific&quot; 
test-data/GSM721117_mctp_20F0GAAXX_1_chr9_withheader     LNCaP_1     LNCaP     male     single_read     not_strand_specific # (This is a comment) Illumina
test-data/GSM721119_mctp_20F0GAAXX_2_chr9_withheader     LNCaP_2     LNCaP     male     single_read     not_strand_specific     # Illumina 
test-data/GSM721118_mctp_20F0GAAXX_3_chr9_withheader     LNCaP_3     LNCaP     male     single_read     not_strand_specific 
test-data/GSM721116_mctp_20F0GAAXX_4_chr9_withheader     LNCaP_4     LNCaP     male     single_read     not_strand_specific 
test-data/GSM721123_mctp_30CYNAAXX_5_chr9_withheader     PrEC_1     PrEC     male     single_read     not_strand_specific 
test-data/GSM721124_mctp_209ENAAXX_8_chr9_withheader     PrEC_2     PrEC     male     single_read     not_strand_specific</pre>
</div>
</div>
<p>
A tab-delimited file of the conditions of each sample, including:
</p>
<ol>
<li>
<code>.bam</code> file location (without the final <code>.bam</code>, this makes the processing much easier)
<ol>
<li>
Note: your <code>.bam</code> files MUST be indexed (have a accompanying <code>.bai</code> files) for RSeQC
</li>
</ol>
</li>
<li>
sample ID that you can assign to whatever you want
</li>
<li>
The group or treatment type. In the example, it is the identification of two cell lines, but you may have “untreated” and “treated,” for example.
</li>
<li>
Gender of the sample. This is important for Circos plotting, and whether we need to include or omit the Y chromosome.
</li>
<li>
Read type, whether the sequencing was single-read or paired-end
</li>
<li>
Strandedness, whether the cDNA library preparation was strand-specific or not.
</li>
</ol>
<h2>
Gene Transfer Format (GTF) file for estimating gene counts
</h2>
<ul>
<li>
What: GTF (Gene Transfer Format) files that you want to use to estimate gene counts.
</li>
<li>
Used by: <code>HTSeq</code> and <code>DEXSeq</code> (differential exon usage)
</li>
<li>
Example file: <code>test-data/hg19_ucsc_genes.gtf</code>
</li>
</ul>
<p>
First few lines of example file:
</p>
<div class="CodeRay">
<div class="code">
<pre>
chr1     hg19_knownGene     exon     11874     12227     0.000000     +     .     gene_id &quot;uc001aaa.3&quot;; transcript_id &quot;uc001aaa.3&quot;; 
chr1     hg19_knownGene     exon     12613     12721     0.000000     +     .     gene_id &quot;uc001aaa.3&quot;; transcript_id &quot;uc001aaa.3&quot;; 
chr1     hg19_knownGene     exon     13221     14409     0.000000     +     .     gene_id &quot;uc001aaa.3&quot;; transcript_id &quot;uc001aaa.3&quot;; 
chr1     hg19_knownGene     exon     11874     12227     0.000000     +     .     gene_id &quot;uc010nxr.1&quot;; transcript_id &quot;uc010nxr.1&quot;; 
chr1     hg19_knownGene     exon     12646     12697     0.000000     +     .     gene_id &quot;uc010nxr.1&quot;; transcript_id &quot;uc010nxr.1&quot;; 
chr1     hg19_knownGene     exon     13221     14409     0.000000     +     .     gene_id &quot;uc010nxr.1&quot;; transcript_id &quot;uc010nxr.1&quot;; 
chr1     hg19_knownGene     start_codon     12190     12192     0.000000     +     .     gene_id &quot;uc010nxq.1&quot;; transcript_id &quot;uc010nxq.1&quot;; 
chr1     hg19_knownGene     CDS     12190     12227     0.000000     +     0     gene_id &quot;uc010nxq.1&quot;; transcript_id &quot;uc010nxq.1&quot;; 
chr1     hg19_knownGene     exon     11874     12227     0.000000     +     .     gene_id &quot;uc010nxq.1&quot;; transcript_id &quot;uc010nxq.1&quot;; 
chr1     hg19_knownGene     CDS     12595     12721     0.000000     +     1     gene_id &quot;uc010nxq.1&quot;; transcript_id &quot;uc010nxq.1&quot;;</pre>
</div>
</div>
<p>
GTF files are a subset of GFF (General Feature Format) files. To get one of these files, follow the following steps: (there is probably a similar method to use the ENSEMBL website, but I am not familiar with it so I am giving these instructions that I myself have followed many times)
</p>
<ol>
<li>
Go to <a href="http://genome.ucsc.edu/cgi-bin/hgTables">http://genome.ucsc.edu/cgi-bin/hgTables</a>
</li>
<li>
Choose your clade and organism of interest
</li>
<li>
Choose these settings:
<ol>
<li>
group: “Genes and Gene Prediction Tracks”
</li>
<li>
track: (whatever you want, but these instructions are built on using “UCSC Genes.” You can use Ensembl or other transcript IDs but then you will need to choose different columns from the kgXref file for the TranscriptID-Symbol file, so I recommend sticking with UCSC IDs for now)
</li>
<li>
table: “knownGene”
</li>
<li>
region: “genome”
</li>
<li>
output format: “GTF – gene transfer format”
</li>
</ol>
</li>
<li>
output file: (whatever you want, but I suggest something informative like <code>hg19_ucsc_genes.gtf</code>)
<ol>
<li>
Make sure to include the file extension (<code>.gtf</code>) in the filename
</li>
</ol>
</li>
<li>
Press “get output”
<ol>
<li>
A file will be downloaded to your “Downloads” folder that you will need to move to somewhere more permanent, such as where you keep your other gene information files.
</li>
</ol>
</li>
</ol>
<h2>
GTF file processed with DEXSeq
</h2>
<ul>
<li>
What: GTF (Gene Transfer Format) file specially formatted for use with DEXSeq, which measures differential exon usage.
</li>
<li>
Used by: DEXSeq
<ul>
<li>
[not yet fully running, but you need to specify this so the order of files doesn’t get altered from what the program expects]
</li>
</ul>
</li>
<li>
Example file: <code>test-data/hg19_ucsc_genes_chr9_dexseq.gtf</code>
</li>
</ul>
<p>
First few lines of example file:
</p>
<div class="CodeRay">
<div class="code">
<pre>
chr9     hg19_ucsc_genes_chr9.gtf     aggregate_gene     11987     14525     .     +     .     gene_id &quot;uc011llp.1&quot; 
chr9     hg19_ucsc_genes_chr9.gtf     exonic_part     11987     12340     .     +     .     transcripts &quot;uc011llp.1&quot;; exonic_part_number &quot;001&quot;; gene_id &quot;uc011llp.1&quot; 
chr9     hg19_ucsc_genes_chr9.gtf     exonic_part     12726     12834     .     +     .     transcripts &quot;uc011llp.1&quot;; exonic_part_number &quot;002&quot;; gene_id &quot;uc011llp.1&quot; 
chr9     hg19_ucsc_genes_chr9.gtf     exonic_part     13334     14525     .     +     .     transcripts &quot;uc011llp.1&quot;; exonic_part_number &quot;003&quot;; gene_id &quot;uc011llp.1&quot; 
chr9     hg19_ucsc_genes_chr9.gtf     aggregate_gene     14511     29739     .     -     .     gene_id &quot;uc010mgp.1+uc010mgm.1+uc022bcs.1+uc011llq.1+uc003zfu.1&quot; 
chr9     hg19_ucsc_genes_chr9.gtf     exonic_part     14511     14940     .     -     .     transcripts &quot;uc010mgm.1&quot;; exonic_part_number &quot;001&quot;; gene_id &quot;uc010mgp.1+uc010mgm.1+uc022bcs.1+uc011llq.1+uc003zfu.1&quot; 
chr9     hg19_ucsc_genes_chr9.gtf     exonic_part     15081     15149     .     -     .     transcripts &quot;uc010mgm.1+uc022bcs.1&quot;; exonic_part_number &quot;002&quot;; gene_id &quot;uc010mgp.1+uc010mgm.1+uc022bcs.1+uc011llq.1+uc003zfu.1&quot; 
chr9     hg19_ucsc_genes_chr9.gtf     exonic_part     15909     16061     .     -     .     transcripts &quot;uc010mgm.1+uc022bcs.1&quot;; exonic_part_number &quot;003&quot;; gene_id &quot;uc010mgp.1+uc010mgm.1+uc022bcs.1+uc011llq.1+uc003zfu.1&quot; 
chr9     hg19_ucsc_genes_chr9.gtf     exonic_part     16188     16421     .     -     .     transcripts &quot;uc011llq.1&quot;; exonic_part_number &quot;004&quot;; gene_id &quot;uc010mgp.1+uc010mgm.1+uc022bcs.1+uc011llq.1+uc003zfu.1&quot; 
chr9     hg19_ucsc_genes_chr9.gtf     exonic_part     16718     16876     .     -     .     transcripts &quot;uc010mgm.1+uc022bcs.1+uc011llq.1&quot;; exonic_part_number &quot;005&quot;; gene_id &quot;uc010mgp.1+uc010mgm.1+uc022bcs.1+uc011llq.1+uc003zfu.1&quot;</pre>
</div>
</div>
<p>
To create this file, You need a GTF file (which can be obtained as described in the GTF section), and then use the script included in <code>rna-seq-diff-exprn/scripts/external/dexseq_prepare_annotation.py</code>:
</p>
<div class="CodeRay">
<div class="code">
<pre>$ python2.7 scripts/external/dexseq_prepare_annotation.py test-data/hg19_ucsc_genes.gtf test-data/hg19_ucsc_genes_dexseq.gtf</pre>
</div>
</div>
<p>
The dollar sign <code>$</code> indicates a bash shell and shows that we are using a command-line interface, as opposed to a command embedded in source code such as this document.
</p>
<h2>
Browser extensible data (BED) files, again for estimating gene counts
</h2>
<ul>
<li>
What: BED (Browser Extensible Data) files that you want to use to estimate gene counts.
</li>
<li>
Used by: <code>bedtools coverage</code>
</li>
<li>
Example file: <code>test-data/hg19_ucsc_genes.bed</code>
</li>
</ul>
<p>
First few lines of example file:
</p>
<div class="CodeRay">
<div class="code">
<pre>track name=&quot;tb_knownGene&quot; description=&quot;table browser query on knownGene&quot; visibility=3 url= 
chr1     11873     14409     uc001aaa.3     0     +     11873     11873     0     3     354,109,1189,     0,739,1347, 
chr1     11873     14409     uc010nxr.1     0     +     11873     11873     0     3     354,52,1189,     0,772,1347, 
chr1     11873     14409     uc010nxq.1     0     +     12189     13639     0     3     354,127,1007,     0,721,1529, 
chr1     14361     16765     uc009vis.3     0     -     14361     14361     0     4     468,69,147,159,     0,608,1434,2245, 
chr1     16857     17751     uc009vjc.1     0     -     16857     16857     0     2     198,519,     0,375, 
chr1     15795     18061     uc009vjd.2     0     -     15795     15795     0     5     152,159,198,136,456,     0,811,1062,1437,1810, 
chr1     14361     19759     uc009vit.3     0     -     14361     14361     0     9     468,69,152,159,198,510,147,99,847,     0,608,1434,2245,2496,2871,3553,3906,4551, 
chr1     14361     19759     uc009viu.3     0     -     14361     14361     0     10     468,69,152,159,198,510,147,102,54,847,     0,608,1434,2245,2496,2871,3553,3906,4139,4551, 
chr1     14361     19759     uc001aae.4     0     -     14361     14361     0     10     468,69,152,159,198,136,137,147,99,847,     0,608,1434,2245,2496,2871,3244,3553,3906,4551,</pre>
</div>
</div>
<p>
To get one of these files, do the following steps: (there is probably a similar method to use the ENSEMBL website, but I am not familiar with it so I am giving these instructions that I myself have followed many times and can help you out with if you are stuck)
</p>
<ol>
<li>
Go to <a href="http://genome.ucsc.edu/cgi-bin/hgTables">http://genome.ucsc.edu/cgi-bin/hgTables</a>
</li>
<li>
Choose your clade and organism of interest
</li>
<li>
Choose these settings:
<ol>
<li>
group: “Genes and Gene Prediction Tracks”
</li>
<li>
track: (whatever you want, but these instructions are built on using “UCSC Genes.” You can use Ensembl or other transcript IDs but then you will need to choose different columns from the kgXref file for the <code>TranscriptID-Symbol</code> file, so I recommend sticking with UCSC IDs for now)
</li>
<li>
table: “knownGene”
</li>
<li>
region: “genome”
</li>
<li>
output format: “BED – browser extensible data”
</li>
</ol>
</li>
<li>
output file: (whatever you want, but I suggest something informative like <code>hg19_ucsc_genes.bed</code>)
<ol>
<li>
Make sure to include the file extension (<code>.bed</code>) in the filename
</li>
</ol>
</li>
<li>
Press “get output”
<ol>
<li>
A file will be downloaded to your “Downloads” folder that you will need to move to somewhere more permanent, such as where you keep your other gene information files.
</li>
</ol>
</li>
</ol>
<p>
If you have an existing BED file, make sure the first line has <code>track name=….</code> or else RSeQC gets mad.
</p>
<h2>
TranscriptID-Symbol file
</h2>
<ul>
<li>
What: Tab-delimited file with the transcript ID in column 1 and the gene symbols you’d like to use in column 2, without a header line.
</li>
<li>
Used by: the pipeline to create a table of gene counts
</li>
<li>
Example file: <code>test-data/hg19_id_symbol.txt</code>
</li>
</ul>
<p>
First few lines of example file:
</p>
<div class="CodeRay">
<div class="code">
<pre>
uc001aaa.3     DDX11L1 
uc010nxr.1     DDX11L1 
uc010nxq.1     DDX11L9 
uc001aal.1     OR4F5 
uc001aaq.2     DQ597235 
uc001aar.2     DQ599768 
uc001aau.3     LOC100132287 
uc021oeh.1     LOC100133331 
uc009vjk.2     LOC100133331 
uc021oei.1     LOC388312</pre>
</div>
</div>
<p>
You can get one of these files by:
</p>
<ol>
<li>
Go to <a href="http://genome.ucsc.edu/cgi-bin/hgTables">http://genome.ucsc.edu/cgi-bin/hgTables</a>
</li>
<li>
Choose your clade and organism of interest
</li>
<li>
Choose these settings:
<ol>
<li>
group: “Genes and Gene Prediction Tracks”
</li>
<li>
track: (whatever you want, but these instructions are built on using “UCSC Genes.” You can use Ensembl or other transcript IDs but then you will need to choose different columns from the kgXref file for the <code>TrascriptID-Symbol</code> file, so I recommend sticking with UCSC IDs for now)
</li>
<li>
table: “kgXref”
</li>
<li>
region: “genome”
</li>
<li>
output format: “GTF – gene transfer format”
</li>
</ol>
</li>
<li>
output file: (whatever you want, but I suggest something informative like <code>hg19_kgXref.txt</code>)
<ol>
<li>
Make sure to include the file extension (<code>.txt</code>, for example) in the filename
</li>
</ol>
</li>
<li>
Press “get output”
</li>
<li>
Now you need to take an extra step to get just the UCSC IDs, e.g. <code>uc002gig.1</code> (column 1 in the kgXref file) and the gene symbols, e.g. <code>TP53</code> (column 5 in the kgXref file), a known tumor suppressor gene.
</li>
</ol>
<p>
<strong>But wait! You’re not done yet!</strong>
</p>
<p>
You need to remove the first line, the header of the file that explains what is in which column.
</p>
<p>
You could do this in Microsoft Excel, but the human file (for example) has 80,923 lines in it and will crash Excel. For organisms with fewer documented genes, using Excel to push columns around may be just fine.
</p>
<p>
The Linux/UNIX (lovingly called “*NIX”) commands to take columns is called “cut” (there is also “paste” to put together columns from different files but that’s out of the scope of what we’re doing here) We want columns 1 and 5 (the UCSC ID and the gene symbol – take a peek at the file by typing <code>head hg19_kgXref.txt</code> on the command line in the directory – this will show the first 10 lines of the file), so we’ll say <code>cut -f 1,5</code> where the <code>-f</code> indicates the “fields” we want to <code>cut</code>. Then we use <code>sed 1d</code> to skip the first line (skipping more than one line has a slighly different command, check out <a href="http://www.grymoire.com/Unix/Sed.html">my favorite Sed tutorial</a> if you’re interested in learning more). And the <code>&lt;</code> indicates the input file, the <code>|</code> indicates that the output of the previous command is treated as input to the next command, and the <code>&gt;</code> indicates the output file. Note that we created a <em>new</em> file and did not overwrite the old one. In general, it is best practices to create a new file rather than overwrite the old one. Also, if you try to make your input and output files the same, the commands may get confused and you could lose your original data. :(
</p>
<div class="CodeRay">
<div class="code">
<pre>$ cut -f 1,5 &lt; hg19_kgXref.txt | sed 1d &gt; hg19_id_symbol.txt</pre>
</div>
</div>
<p>
Or, if you want to create a chromosome-specific file like I did, use your <code>.bed</code> file to search through your kgXref file:
</p>
<div class="CodeRay">
<div class="code">
<pre>$ cut -f 4 hg19_ucsc_genes_chr9.bed | grep --fixed-strings - hg19_kgXref.txt &gt;hg19_kgXref_chr9.txt</pre>
</div>
</div>
<p>
Then do the same as above, but with your chr9 file:
</p>
<div class="CodeRay">
<div class="code">
<pre>$ cut -f 1,5 &lt; hg19_kgXref_chr9.txt | sed 1d &gt; hg19_id_symbol_chr9.txt</pre>
</div>
</div>
<h2>
Genome file
</h2>
<ul>
<li>
What: This &quot;Genome&quot; file really just says how long each chromosome is.
</li>
<li>
Used by: <code>genomeCoverageBed</code>
</li>
<li>
Example file: <code>test-data/human.hg19.genome</code>
</li>
</ul

<p>
First few lines of example file:
</p>
<div class="CodeRay">
<div class="code">
<pre>
chr1     249250621 
chr2     243199373 
chr3     198022430 
chr4     191154276 
chr5     180915260 
chr6     171115067 
chr7     159138663 
chrX     155270560 
chr8     146364022 
chr9     141213431</pre>
</div>
</div>
<p>
Besides the example files, you can also use ones shipped with BEDTools. On my machine, these files are located in <code>~/packages/BEDTools/genomes</code>:
</p>
<div class="CodeRay">
<div class="code">
<pre>$ ls ~/packages/BEDTools-Version-2.16.2/genomes/ human.hg18.genome human.hg19.genome mouse.mm8.genome  mouse.mm9.genome</pre>
</div>
</div>
<p>
As to how to create these files for non-mouse or human organisms, my suggestion (while rather unwieldy) is to:
</p>
<ol>
<li>
Go to <a href="http://genome.ucsc.edu/cgi-bin/hgTables">http://genome.ucsc.edu/cgi-bin/hgTables</a>
</li>
<li>
Choose your clade and organism of interest
</li>
<li>
Choose these settings:
<ol>
<li>
group: “All Tables”
</li>
<li>
table: “chromInfo”
</li>
<li>
output format: “all fields from selected table”
</li>
<li>
output file: (anything you want, but preferably something informative like platypus.ornAna1.genome)
</li>
</ol>
</li>
<li>
Press “get output”
</li>
<li>
Remove the first line and the third column of the file, which you could do in Microsoft Excel (since this file will be comparatively small), or by using this shell command: <code>$ cut -f 1,2 &lt; platypus.ornAna1.genome | sed 1d &gt; platypus.ornAna1.genome.fixed</code>
</li>
</ol>
<h2>
Karyotype file
</h2>
<ul>
<li>
What: Another “this is how long all the chromosomes are” file, but formatted so Circos can use it
</li>
<li>
Used by: Circos
</li>
<li>
Example file: <code>test-data/karyotype/karyotype.human.hg19.txt</code>
</li>
</ul>
<p>
This file looks like:
</p>
<div class="CodeRay">
<div class="code">
<pre>
chr - chr1 chr1 0 249250621 chr1 
chr - chr2 chr2 0 243199373 chr2 
chr - chr3 chr3 0 198022430 chr3 
chr - chr4 chr4 0 191154276 chr4 
chr - chr5 chr5 0 180915260 chr5 
chr - chr6 chr6 0 171115067 chr6 
chr - chr7 chr7 0 159138663 chr7 
chr - chr8 chr8 0 146364022 chr8 
chr - chr9 chr9 0 141213431 chr9</pre>
</div>
</div>
<p>
Karyotype file used by Circos, which specifies the chromosome lengths. The third column, the chromosome name, MUST use <code>chr1</code>-type notation, and not the typical <code>hs1</code> notation for Homo sapiens chromosome 1. This is because <code>bedtools</code> and friends use <code>chr1</code> notation, but I didn’t want to require the organism name and then lookup the conversion. Presumably, you would have samples from all the same organism since you are comparing gene expression and coverage across different treatments, so I felt this was a safe assumption. I also didn’t want to lock you into ONLY using human data, because there are plenty of interesting organisms out there.
</p>
<h2>
GC Content file
</h2>
<ul>
<li>
What: Percentage of Guanine and Cytosine (GC) bases per some distance (I recommend at least 1000 bases, or else it will take a VERY long time to plot). This is an important quantity because the GC base pairing has three hydrogen bonds instead of two like AT, is known to be a stronger bond, and genes are also known to be GC-rich.
</li>
<li>
Used by: Circos
</li>
<li>
Example file: <code>test-data/hg19_gc_content_circos_chr9.txt</code>
</li>
</ul>
<p>
First few lines of example file:
</p>
<div class="CodeRay">
<div class="code">
<pre>
chr9     10000     10999     58 
chr9     11000     11999     58 
chr9     12000     12999     57.9 
chr9     13000     13999     57.9 
chr9     14000     14999     58 
chr9     15000     15999     60.7 
chr9     16000     16999     56.9 
chr9     17000     17999     61.3 
chr9     18000     18999     60.7 
chr9     19000     19999     57.7</pre>
</div>
</div>
<p>
This GC content file can be created by converting a <code>.wig</code> (wiggle) format file that’s used for a genome browser into a circus format using:
</p>
<div class="CodeRay">
<div class="code">
<pre>../scripts/wig_to_circos.R hg19_gc1000Base.txt hg19_gc_content.circos</pre>
</div>
</div>
<h2>
Number of bunches
</h2>
<ul>
<li>
What: Merges samples of the same group, e.g. <em>untreated</em> into “bunches,” or mergings of several samples.
<ul>
<li>
For example, in the example data provided, there are four samples of the LNCaP prostate cancer cell line, and two of the PrEC prostate cancer cell line.
</li>
<li>
In the provided example, two bunches are specified. This means that in addition to calculating the gene counts for <code>LNCaP_1</code>, <code>LNCaP_2</code>, <code>LNCaP_3</code>, <code>LNCaP_4</code>, <code>PrEC_1</code>, <code>PrEC_2</code>, the pipeline will also create
<ul>
<li>
<code>LNCaP_bunch1of2</code>, containing <code>LNCaP_1</code> and <code>LNCaP_2</code>
</li>
<li>
<code>LNCaP_bunch2of2</code>, containing <code>LNCaP_3</code> and <code>LNCaP_4</code>
</li>
<li>
<code>PrEC_bunch1of2</code>, containing <code>PrEC_1</code>
</li>
<li>
<code>PrEC_bunch2of2</code>, containing <code>PrEC_2</code>
</li>
</ul>
</li>
<li>
<strong>Why this is useful:</strong> Originally, this pipeline was written for single-cell RNA-Seq analysis and we found that while it is very interesting to look at the genes expressed in a single cell, we saw significantly more signal by merging treatment groups into bunches, and performing differential expression analysis on these bunches.
</li>
</ul>
</li>
<li>
Used by: Entire pipeline
</li>
<li>
Example: 2
</li>
</ul>
<p>
To change the ordering of samples, change the conditions file, as that is the basis of the bunching order.
</p>
<p>
If you don’t want <strong>any</strong> bunches, omit this variable from the command line.
</p>
<h1>
Dependencies
</h1>
<p>
These are programs you must have installed before attempting to run the code. Note: This may seem like a lot, but if you are in biomedical research, it is likely that the servers at your institution already have most of these installed.
</p>
<ol>
<li>
<a href="http://www.python.org/getit/releases/2.7/">Python 2.7</a> – for RSeQC and HTSeq, #2 and #3
<ol>
<li>
<a href="http://www.cython.org/#download">Cython</a> – required for pybedtools below
</li>
<li>
<a href="http://packages.python.org/pybedtools/">pybedtools</a> – required for HTSeq
</li>
<li>
<a href="http://www-huber.embl.de/users/anders/HTSeq/doc/overview.html">HTSeq</a> – Another method of calculating gene expression counts, in addition to BEDTools Coverage. Installed via python2.7, i.e. instead of typing <code>python setup.py install</code> Say: <code>python2.7 setup.py install</code>
</li>
</ol>
</li>
<li>
<a href="http://code.google.com/p/rseqc/downloads/list">RSeQC, Version 2.3 or later</a>, RNA-Sequencing Quality Control software
</li>
<li>
<a href="http://code.google.com/p/bedtools/downloads/list">BEDTools</a>, version 2.16.2 or greater
</li>
<li>
Perl 5.8.x or newer (for Circos, #6) Linux and Mac users: <a href="http://www.perl.org/get.html">http://www.perl.org/get.html</a> Windows users: <a href="http://strawberryperl.com/">http://strawberryperl.com/</a>
</li>
<li>
<a href="http://circos.ca">Circos</a>, version 0.60 or later (for plotting genome coverage data) Note: Circos has a number of Perl package dependencies that take some time to make sure they are all properly installed on your system. <code>http://circos.ca/software/download/circos</code> Aliased such that <code>circos</code> will run the program On my machine, this is accomplished by adding this line to the file in <code>/Users/olgabotvinnik/.bashrc</code>, or my <code>~/.bashrc</code> file: <code>PATH=<span class="math inline"><em>P</em><em>A</em><em>T</em><em>H</em> : /<em>u</em><em>s</em><em>r</em>/<em>b</em><em>i</em><em>n</em>/<em>c</em><em>i</em><em>r</em><em>c</em><em>o</em><em>s</em>/<em>b</em><em>i</em><em>n</em>; <em>e</em><em>x</em><em>p</em><em>o</em><em>r</em><em>t</em><em>P</em><em>A</em><em>T</em><em>H</em> &lt; /<em>c</em><em>o</em><em>d</em><em>e</em> &gt; <em>W</em><em>h</em><em>i</em><em>c</em><em>h</em><em>m</em><em>e</em><em>a</em><em>n</em><em>s</em><em>t</em><em>h</em><em>a</em><em>t</em><em>w</em><em>h</em><em>e</em><em>n</em><em>y</em><em>o</em><em>u</em><em>r</em><em>u</em><em>n</em><em>c</em><em>o</em><em>m</em><em>m</em><em>a</em><em>n</em><em>d</em><em>s</em>, <em>t</em><em>h</em><em>e</em><em>c</em><em>o</em><em>m</em><em>p</em><em>u</em><em>t</em><em>e</em><em>r</em><em>w</em><em>i</em><em>l</em><em>l</em><em>k</em><em>n</em><em>o</em><em>w</em><em>t</em><em>o</em><em>l</em><em>o</em><em>o</em><em>k</em><em>i</em><em>n</em> &lt; <em>c</em><em>o</em><em>d</em><em>e</em> &gt; /<em>u</em><em>s</em><em>r</em>/<em>b</em><em>i</em><em>n</em>/<em>c</em><em>i</em><em>r</em><em>c</em><em>o</em><em>s</em>/<em>b</em><em>i</em><em>n</em> &lt; /<em>c</em><em>o</em><em>d</em><em>e</em> &gt; <em>f</em><em>o</em><em>r</em><em>p</em><em>o</em><em>t</em><em>e</em><em>n</em><em>t</em><em>i</em><em>a</em><em>l</em><em>e</em><em>x</em><em>e</em><em>c</em><em>u</em><em>t</em><em>a</em><em>b</em><em>l</em><em>e</em><em>f</em><em>i</em><em>l</em><em>e</em><em>s</em>./<em>u</em><em>s</em><em>r</em>/<em>b</em><em>i</em><em>n</em>/<em>c</em><em>i</em><em>r</em><em>c</em><em>o</em><em>s</em><em>I</em><em>s</em><em>w</em><em>h</em><em>e</em><em>r</em><em>e</em><em>I</em><em>p</em><em>e</em><em>r</em><em>s</em><em>o</em><em>n</em><em>a</em><em>l</em><em>l</em><em>y</em><em>i</em><em>n</em><em>s</em><em>t</em><em>a</em><em>l</em><em>l</em><em>e</em><em>d</em><em>C</em><em>i</em><em>r</em><em>c</em><em>o</em><em>s</em>.<em>O</em><em>n</em><em>t</em><em>h</em><em>e</em><em>s</em><em>e</em><em>r</em><em>v</em><em>e</em><em>r</em><em>t</em><em>h</em><em>a</em><em>t</em><em>I</em><em>u</em><em>s</em><em>e</em>, <em>f</em><em>o</em><em>r</em><em>e</em><em>x</em><em>a</em><em>m</em><em>p</em><em>l</em><em>e</em>, <em>i</em><em>t</em><em>i</em><em>s</em><em>i</em><em>n</em><em>s</em><em>t</em><em>a</em><em>l</em><em>l</em><em>e</em><em>d</em><em>i</em><em>n</em> : &lt;<em>c</em><em>o</em><em>d</em><em>e</em> &gt; /<em>s</em><em>h</em><em>a</em><em>r</em><em>e</em>/<em>a</em><em>p</em><em>p</em><em>s</em>/<em>c</em><em>i</em><em>r</em><em>c</em><em>o</em><em>s</em> − 0.60/<em>b</em><em>i</em><em>n</em> &lt; /<em>c</em><em>o</em><em>d</em><em>e</em> &gt; <em>S</em><em>o</em><em>t</em><em>h</em><em>e</em><em>n</em><em>m</em><em>y</em> &lt; <em>c</em><em>o</em><em>d</em><em>e</em> &gt;  /.<em>b</em><em>a</em><em>s</em><em>h</em><em>r</em><em>c</em> &lt; /<em>c</em><em>o</em><em>d</em><em>e</em> &gt; <em>f</em><em>i</em><em>l</em><em>e</em><em>o</em><em>n</em><em>t</em><em>h</em><em>e</em><em>s</em><em>e</em><em>r</em><em>v</em><em>e</em><em>r</em><em>l</em><em>o</em><em>o</em><em>k</em><em>s</em><em>l</em><em>i</em><em>k</em><em>e</em> : &lt;<em>c</em><em>o</em><em>d</em><em>e</em> &gt; <em>P</em><em>A</em><em>T</em><em>H</em>=</span>PATH:/share/apps/circos-0.60/bin ; export PATH</code>
</li>
<li>
<a href="http://www.r-project.org/">R, 2.14.2 or later</a>
<ol>
<li>
<a href="http://www-huber.embl.de/users/anders/DESeq/">DESeq</a>. For differential expression analysis.
</li>
<li>
<a href="http://bioinfo.cipf.es/noiseq/doku.php?id=downloads">NOISeq</a>. Another type of differential expression analysis software. You don’t need to download this as it is included in this software, but I figured I should mention it.
</li>
<li>
<a href="http://bioconductor.org/packages/release/bioc/html/DEXSeq.html">DEXSeq</a>. Differential exon usage analysis
</li>
</ol>
</li>
</ol>
<h1>
How to run the example code
</h1>
<h2>
Before running, make sure you have everything in place
</h2>
<p>
Before running, make sure you add these to your path: <code>python2.7</code>, <code>BEDTools</code>, <code>SAMTools</code>, <code>RSeQC</code> in <code>python2.7</code>.
</p>
<p>
For example, for me, these are the locations of these packages on my computer. Add these lines, modified to the locations on your computer, below to your <code>~/.bashrc</code> file and then “source” it: <code>source ~/.bashrc</code>. FYI: the colon character, “:” is the delimiter between places to look for binary executables files.
</p>
<div class="CodeRay">
<div class="code">
<pre>export PATH=/usr/local/bin/python2.7:$PATH export PATH=$PATH:/share/apps/samtools-0.1.18:/share/apps/BEDTools-Version-2.15.0/ export PYTHONPATH=/share/apps/RSeQC/usr/local/lib/python2.7/site-packages:$PYTHONPATH export PATH=/share/apps/RSeQC/usr/local/bin:$PATH</pre>
</div>
</div>
<h2>
The example run
</h2>
<p>
An example run looks like this (yes it is a very long command):
</p>
<div class="CodeRay">
<div class="code">
<pre>scripts/pipeline.sh test-results test-data/conditions_chr9.tab test-data/hg19_ucsc_genes.gtf test-data/hg19_ucsc_genes_chr9_dexseq.gtf test-data/hg19_ucsc_genes.bed test-data/hg19_id_symbol.txt test-data/human.hg19.genome test-data/karyotype/karyotype.human.hg19.txt test-data/hg19_gene_density_1e5bins.txt test-data/hg19_gc_content_circos_chr9.txt 2</pre>
</div>
</div>
<p>
Or, using the keywords we’ve discussed:<img src="http://media.tumblr.com/tumblr_mde7gmsVr81rw6gvj.png" />
</p>
<div class="CodeRay">
<div class="code">
<pre>scripts/pipeline.sh [output directory] [metadata] [.gtf] [dexseq-processed .gtf] [.bed] [transcriptID-symbol] [genome] [karyotype] [gene density] [gc content] [number of bunches]</pre>
</div>
</div>
</div>
