from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [   
    # ex: /polls/5/results/
    url('(\d)/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    url('(\d)/vote/', views.vote, name='vote'),    
      # ex: /polls/5/
    url('(\d)/', views.detail, name='detail'),
     # ex: /polls/
    url('', views.index, name='index'),
]