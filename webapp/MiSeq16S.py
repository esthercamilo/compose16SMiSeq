# -*- coding: utf-8 -*-16SMiSeq
import os
import logging
import subprocess
from pathlib import Path
WORKDIR = Path(os.getcwd())
logging.basicConfig(filename=os.path.join(WORKDIR, 'error.log'), filemode='a', level=logging.DEBUG)

class QualityNGS(object):
    def __init__(self, threshold, fastq_folder = os.path.join(WORKDIR, 'data', 'fqs')):
        self.istrimmed = False
        self.threshold = threshold
        self.fastq_folder = fastq_folder

    def trimming(self):
        self.istrimmed = True
        trimmomatic = os.path.join(WORKDIR, 'apps', 'Trimmomatic-0.39', 'trimmomatic-0.39.jar')
        adapter = os.path.join(WORKDIR, 'apps','Trimmomatic-0.39','adapters','TruSeq3-SE.fa')
        comm = ['java', '-jar', trimmomatic, 'SE', '-phred33']

        fastq_files = [x for x in os.listdir(self.fastq_folder) if '_trimmed_' not in x]
        for f in fastq_files:
            fastq = os.path.join(self.fastq_folder, f)
            output = os.path.join(self.fastq_folder, f.replace('.fastq', f'_trimmed_{self.threshold}.fastq'))
            final_comm = comm + [fastq, output, f'ILLUMINACLIP:{adapter}:2:30:10']
            try:
                subprocess.check_call(final_comm)
            except subprocess.CalledProcessError as e:
                logging(e.output)


    def report(self): # ver relatório antes e depois trimming
        if not self.istrimmed:
            msg = 'Reads not trimmed, only original will be reported'
        pass


