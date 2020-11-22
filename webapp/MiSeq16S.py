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


class OTU(object):
    def __init__(self):
        self.database = os.path.join(WORKDIR, 'data', 'database', 'fasta_file.fasta')
        self.fastq_folder = os.path.join(WORKDIR, 'data','fastq_final')
        self.usearch = os.path.join(WORKDIR, 'apps', 'usearch11.0.667_i86linux32')
        self.indexed_db = self.index_fasta()
        self.outputfolder = os.path.join(WORKDIR, 'data', 'otutab')

    def index_fasta(self):
        index_otu = os.path.join(WORKDIR,'data','database', 'otus.udb')
        comm = [self.usearch, '-makeudb_usearch', self.database, '-output', index_otu  ]
        #subprocess.check_call(comm)
        return index_otu

    def mapotu(self, fastq):
        comm = [self.usearch, '-otutab', fastq, '-otus', self.indexed_db,
                '-otutabout', os.path.join(self.outputfolder,os.path.basename(fastq).replace('.fastq','_map.txt')),
                '-mapout', os.path.join(self.outputfolder,os.path.basename(fastq).replace('.fastq', '_otutab.txt'))]
        subprocess.check_call(comm)

    def summarize_otus(self):
        otus = [x for x in os.listdir(self.outputfolder) if '_otutab.txt' in x]






if __name__ == "__main__":
    WORKDIR = Path(os.getcwd()).parent
    otu = OTU()
    otu.mapotu('/home/gntech/Documents/Projetos/PROSPECTA/compose16SMiSeq/data/fqs/F3D0_S188_L001_R1_001.fastq')