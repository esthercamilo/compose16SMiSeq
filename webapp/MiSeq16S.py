# -*- coding: utf-8 -*-16SMiSeq
import os
import logging
import subprocess
from pathlib import Path
WORKDIR = Path(os.getcwd()).parent
logging.basicConfig(filename=os.path.join(WORKDIR, 'error.log'), filemode='a', level=logging.DEBUG)

class QualityNGS(object):
    def __init__(self, fastq_folder):
        self.istrimmed = False
        self.threshold = 30
        self.fastq_folder = fastq_folder

    def trimming(self, threshold=None):
        self.istrimmed = True
        self.threshold = threshold or self.threshold
        trimmomatic = os.path.join(WORKDIR, 'apps', 'Trimmomatic-0.39', 'trimmomatic-0.39.jar')
        comm = ['java', '-jar', trimmomatic, 'SE', f'-phred{str(threshold)}']
        fastq_files = ''
        try:
            fastq_files = os.listdir(os.path.join(self.fastq_folder,'fqs'))
        except FileNotFoundError:
            msg = 'The folder containing the fastq files must be necessarily be named \"fqs\".' \
                  'The path in the argument must point to one level up.'
            logging.error(msg)
        if not bool(fastq_files):
            msg = "The folder is empty"
            logging.error(msg)
        for f in fastq_files:
            fastq = os.path.join(self.fastq_folder, f)
            comm = comm + [fastq]
            try:
                subprocess.check_call(comm)
            except subprocess.CalledProcessError as e:
                logging(e.output)


    def report(self): # ver relatório antes e depois trimming
        if not self.istrimmed:
            msg = 'Reads not trimmed, only original will be reported'
        pass


