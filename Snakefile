# ============================================
# NGS Quality Control Pipeline
# Author: Victoria Djana
# ============================================

configfile: "config.yaml"

SAMPLES = config["samples"]

rule all:
input:
expand("results/fastqc/{sample}_fastqc.html", sample=SAMPLES),
expand("results/trimmed/{sample}_trimmed.fastq.gz", sample=SAMPLES),
"results/multiqc_report.html"

rule fastqc:
input:
"data/raw/{sample}.fastq.gz"
output:
html = "results/fastqc/{sample}_fastqc.html",
zip = "results/fastqc/{sample}_fastqc.zip"
shell:
"fastqc {input} --outdir results/fastqc/"

rule trimmomatic:
input:
"data/raw/{sample}.fastq.gz"
output:
"results/trimmed/{sample}_trimmed.fastq.gz"
params:
adapters = config["adapters"],
minlen = config["min_length"]
shell:
"""
trimmomatic SE {input} {output} \
ILLUMINACLIP:{params.adapters}:2:30:10 \
LEADING:3 TRAILING:3 \
SLIDINGWINDOW:4:15 \
MINLEN:{params.minlen}
"""

rule multiqc:
input:
expand("results/fastqc/{sample}_fastqc.zip", sample=SAMPLES)
output:
"results/multiqc_report.html"
shell:
"multiqc results/fastqc/ -o results/"
