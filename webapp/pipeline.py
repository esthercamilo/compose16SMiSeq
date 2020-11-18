import os
import argparse
from webapp.MiSeq16S import QualityNGS

parser = argparse.ArgumentParser(description='16s NGS Metagenomics pipeline (single paired reads).')
parser.add_argument('folder', type=str, help='Path to the folder containing fastq folder.')
args = parser.parse_args()

if __name__ == '__main__':
    # 1.1. Trimming by quality (using default: 30)
    miseq = QualityNGS(args.folder)
    miseq.trimming()
    # 1.2. Report Phred Scores (before and after trimming)
    miseq.report()

