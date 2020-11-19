from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import logging
import os
from pathlib import Path
from webapp.MiSeq16S import QualityNGS
from itertools import groupby
from operator import itemgetter

WORKDIR = Path(os.getcwd())

logging.basicConfig(format='Line:%(lineno)d %(message)s',
                    filename='error.log',
                    filemode='a', level=logging.INFO)


def groupfiles():
   allfiles = os.listdir(os.path.join(WORKDIR, 'data', 'fqs'))
   listfiles = [x for x in allfiles if '_trimmed_' in x]
   g = [tuple(x.split('_trimmed_')) for x in listfiles]
   groups = [list(group) for key, group in groupby(g, itemgetter(1))]
   result = {}
   for i in groups:
      for j in i:
         key = j[1].split('.')[0]
         if key not in result.keys():
            result[key] = []
         result[key].append(j[0])
   return result


@login_required
def home(request):
   context = {}
   return render(request, 'home.html', context)

def trimming_results(request):
   files = os.listdir(os.path.join(WORKDIR, 'data', 'fqs'))
   original = [x for x in files if '_trimmed_' not in x]
   context = {'files': groupfiles(), 'original': original}
   return render(request, "step1/trimming_results.html", context)

def getplot(idplot):
   return idplot

def reports(request):
   # data1, data2 = getplot(id=1) #somente para 1 por enquanto
   # context = {
   #    'before': data1, 'after':data2
   # }
   return render(request, 'step1/modal.html', {})

def otu(request):
   # make_otu_table()
   with open(os.path.join(WORKDIR, 'data', 'tables', 'otu_table_tax_amostras.tsv'), 'r') as f: #mudar para tabela final
      header = f.readline().split('\t')
      lines = [x.rstrip().split('\t') for x in f.readlines()]
   return render(request, 'step1/otu.html', {'header':header, 'lines':lines})

def taxonomy(request):
   # make_otu_table()
   with open(os.path.join(WORKDIR, 'data', 'tables', 'tax_table_amostras.tsv'), 'r') as f: #mudar para tabela final
      header = f.readline().split('\t')
      lines = [x.rstrip().split('\t') for x in f.readlines()]
   return render(request, 'step1/taxonomy.html', {'header2':header, 'lines2':lines})

def automation(request):
   return render(request, 'step1/automation.html', {})


def data_plot(header,lines):
   pass

def counting(request):
   with open(os.path.join(WORKDIR, 'data', 'tables', 'tax_table_amostras.tsv'), 'r') as f: #mudar para tabela final
      header = f.readline().split('\t')
      lines = [x.rstrip().split('\t') for x in f.readlines()]
   data_plot(header, lines)
   return render(request, 'step2/bacterial_counting.html', {'header2':header, 'lines2':lines})



def questions(request):
   question = request.path_info.split('/')[2]
   context = {'question':question}
   return render(request, f'step3/{question}.html', context)


class TrimmingView(View):

   def get(self, request, *args, **kwargs):
      files = [x for x in os.listdir(os.path.join(WORKDIR, 'data', 'fqs')) if '_trimmed_' not in x]
      context = {'files':files}
      return render(request, "step1/trimming.html", context)

   def post(self, request, *args, **kwargs):
      files = os.listdir(os.path.join(WORKDIR, 'data', 'fqs'))
      original = [x for x in files if '_trimmed_' not in x]
      results = request.POST
      trim_threshold = results.get('trim_threshold') # todo implementar validacao
      qualObj = QualityNGS(trim_threshold)
      qualObj.trimming()
      context = {'files':groupfiles(), 'original':original}
      return render(request, "step1/trimming_results.html", context)

# class Args:
#    def __init__(self):
#       pass
#       # self.filename = '/home/gntech/2020/PycharmProjects/local_immuno/immuno/iedb/population_coverage/test/mhcii_alleles.txt'
#       # self.mhc_class = [['I']]
#       # self.path = '/home/gntech/Downloads/'
#       # self.population = []
#       # self.list = False


#
# class CoverageInHouse(View):
#    def get(self, request, *args, **kwargs):
#       context = {'value':self.args}
#       return render(request, "coverage_inhouse.html", context)
#
# class Introduction(TemplateView):
#    template_name = "introduction.html"
#
# class References(TemplateView):
#     template_name = "references.html"