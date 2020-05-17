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
# nb we are using generic view for index, detail, results. They (were) very short
# views and can be managed easily using the generic view system. this is why we ad the .as_view()
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# The DetailView generic view expects the primary key value captured from the URL 
# to be called "pk", so we’ve changed question_id to pk for the generic views.
