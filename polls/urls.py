# NB YOU NEED TO CREATE THIS FILE

# need to import path module
from django.urls import path 

# need to import the views from this app
from . import views
# add the path, (home page), the view (the index method) and the name


# add namespaces to your URLconf so that the url names
# can be used in other apps
# the url in templates is like so: 
# <a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a>

app_name = 'polls'
urlpatterns = [
     # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

