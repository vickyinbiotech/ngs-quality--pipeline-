# ============================================
# FastQC Results Parser
# Author: Victoria Djana
# Description: Parse FastQC zip outputs and
# generate a summary CSV report
# ============================================

import zipfile
import os
import csv
import sys

def parse_fastqc_zip(zip_path):
"""Extract key QC metrics from a FastQC zip file."""
metrics = {}

with zipfile.ZipFile(zip_path, 'r') as zf:
# Find the summary file
summary_file = [f for f in zf.namelist() if f.endswith('summary.txt')]

if not summary_file:
print(f"No summary found in {zip_path}")
return None

with zf.open(summary_file[0]) as f:
for line in f.read().decode('utf-8').splitlines():
parts = line.strip().split('\t')
if len(parts) == 3:
status, metric, sample = parts
metrics[metric] = status

return metrics

def generate_report(fastqc_dir, output_csv):
"""Parse all FastQC zip files and write summary report."""
zip_files = [
os.path.join(fastqc_dir, f)
for f in os.listdir(fastqc_dir)
if f.endswith('_fastqc.zip')
]

if not zip_files:
print("No FastQC zip files found.")
sys.exit(1)

all_metrics = []
for zf in zip_files:
sample_name = os.path.basename(zf).replace('_fastqc.zip', '')
metrics = parse_fastqc_zip(zf)
if metrics:
metrics['Sample'] = sample_name
all_metrics.append(metrics)

# Write CSV report
if all_metrics:
fieldnames = ['Sample'] + [k for k in all_metrics[0] if k != 'Sample']
with open(output_csv, 'w', newline='') as csvfile:
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()
writer.writerows(all_metrics)
print(f"Report saved: {output_csv}")

if __name__ == "__main__":
fastqc_dir = sys.argv[1] if len(sys.argv) > 1 else "results/fastqc"
output_csv = sys.argv[2] if len(sys.argv) > 2 else "results/qc_summary.csv"
generate_report(fastqc_dir, output_csv)
