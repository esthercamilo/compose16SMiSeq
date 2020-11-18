from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import logging
import os

logging.basicConfig(format='Line:%(lineno)d %(message)s',
                    filename='/code/error.log',
                    filemode='a', level=logging.INFO)

@login_required
def home(request):
   context = {}
   return render(request, 'home.html', context)


class TrimmingView(View):
   def get(self, request, *args, **kwargs):
      context = {'args':self}
      return render(request, "step1/trimming.html", context)
   def post(self, request, *args, **kwargs):
      results = request.POST
      epitope = results.get('epitope')
      mhc = results.get('mhc')
      country = results.get('country')

      context = {'args':self}
      return render(request, "trimming_results.html", context)

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