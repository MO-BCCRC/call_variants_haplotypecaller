#cvh : call_variant_haplotypecaller : Call SNPs and indels simultaneously via local re-assembly of haplotypes in an active region.


```
Development information

date created : Sep 10 2014
last update  : Sep 10  2014
Developer    : Rad Aniba (raniba@bccrc.ca)
Input        : Sorted alignment, reference genome 
Output       : CVF file
Seed used    : <no_seed>

```


###Usage

The basic operation of the HaplotypeCaller proceeds as follows:


1. Define active regions
The program determines which regions of the genome it needs to operate on, based on the presence of significant evidence for variation.


2. Determine haplotypes by re-assembly of the active region
For each ActiveRegion, the program builds a De Bruijn-like graph to reassemble the ActiveRegion, and identifies what are the possible haplotypes present in the data. The program then realigns each haplotype against the reference haplotype using the Smith-Waterman algorithm in order to identify potentially variant sites.


3. Determine likelihoods of the haplotypes given the read data
For each ActiveRegion, the program performs a pairwise alignment of each read against each haplotype using the PairHMM algorithm. This produces a matrix of likelihoods of haplotypes given the read data. These likelihoods are then marginalized to obtain the likelihoods of alleles for each potentially variant site given the read data.


4. Assign sample genotypes
For each potentially variant site, the program applies Bayes? rule, using the likelihoods of alleles given the read data to calculate the likelihoods of each genotype per sample given the read data observed for that sample. The most likely genotype is then assigned to the sample.

###Dependencies

- GATK
- python



###Example

```
java
     -jar GenomeAnalysisTK.jar
     -T HaplotypeCaller
     -R reference/human_g1k_v37.fasta
     -I sample1.bam \
     --emitRefConfidence GVCF \
     --variant_index_type LINEAR \
     --variant_index_parameter 128000
     [--dbsnp dbSNP.vcf] \
     [-L targets.interval_list] \
     -o output.raw.snps.indels.g.vcf
```

###Known issues

(will update later)

###Last updates

(will update later)

### test data
Reference : /genesis/extscratch/shahlab/raniba/Software/bowtie2/genomes/GRCh37-lite   
seq1 : /extscratch/shahlab/raniba/Tasks/test_data/SA495-Normal_S8_L001_R1_001.fastq 
seq2 : /extscratch/shahlab/raniba/Tasks/test_data/SA495-Normal_S8_L001_R2_001.fastq  
outfile : test.bam   

bowtie2 path : /genesis/extscratch/shahlab/raniba/Software/bowtie2/  
samtools path : /extscratch/shahlab/raniba/pipelines/miseq_pipeline/miseq_analysis_pipeline/miseq-pipeline/software/samtools-0.1.19/samtools 


