from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('step1/trimming/', TrimmingView.as_view()),
    path('step1/trimming_results/', views.trimming_results, name='trimming'),
    path('step1/report', views.reports, name='report'),
    path('step1/otu', views.otu, name='otu'),
    path('step1/taxonomy', views.taxonomy, name='taxonomy'),
    path('step1/automation', views.automation, name='automation'),

    path('step2/counting', views.counting, name='counting'),

    path('step3/question1', views.questions, name='question1'),
    path('step3/question2', views.questions, name='question2'),
    path('step3/question3', views.questions, name='question3'),
    path('step3/question4', views.questions, name='question4'),
    path('step3/question5', views.questions, name='question5'),

]
