# NGS Quality Control Pipeline

Automated NGS pipeline for quality control of sequencing data (FastQ files).
Built with Snakemake and Python — designed for reproducibility and scalability.

## Features
- Automated FastQ quality assessment
- Adapter trimming and low-quality read filtering
- Multi-sample processing in parallel
- HTML quality reports generation
- Snakemake workflow for full reproducibility

## Project Structure
```
ngs-quality-pipeline/
├── README.md
├── Snakefile # Main Snakemake workflow
├── config.yaml # Pipeline configuration
├── scripts/
│ └── parse_fastqc.py # Python script to parse QC results
└── data/
└── samples.tsv # Sample sheet (fictional data)
```

## Stack
- Workflow : Snakemake
- Language : Python 3
- Tools : FastQC, Trimmomatic
- Environment : Linux/Bash

## Context
Developed as part of bioinformatics training in NGS data analysis.
Simulates a real-world quality control workflow for Illumina sequencing data.

## Usage
```bash
# Dry run (check workflow without executing)
snakemake -n

# Run the full pipeline
snakemake --cores 4

# Generate workflow graph
snakemake --dag | dot -Tpdf > dag.pdf
