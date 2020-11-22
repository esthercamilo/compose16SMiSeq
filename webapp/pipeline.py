import os
import argparse
from webapp.MiSeq16S import QualityNGS






if __name__ == '__main__':
    # 1.1. Trimming by quality (using default: 30)
    miseq = QualityNGS(args.folder)
    miseq.trimming()
    # 1.2. Report Phred Scores (before and after trimming)
    miseq.report()

