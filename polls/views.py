from django.shortcuts import render, get_object_or_404
# from django.http import Http404
# from django.shortcuts import , render
# Create your views here.
# for more info on urls 

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# get object or 404 means you don't need to do try except 
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

"""
IMPORTANT NOTES ON THE ABOVE METHOD FOR VOTE
request.POST is a dictionary-like object that lets you access submitted data by 
key name. request.POST['choice'] returns the ID of the selected choice.

request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data. 
The above code checks for KeyError and redisplays the question form with an 
error message if choice isn’t given.

the code returns an HttpResponseRedirect . HttpResponseRedirect takes a single 
argument: the URL to which the user will be redirected.

We are using the reverse() function in the HttpResponseRedirect constructor in 
this example. This function helps avoid having to hardcode a URL in the view 
function. It is given the name of the view that we want to pass control to and 
the variable portion of the URL pattern that points to that view. In this case, 
using the URLconf we set up in Tutorial 3, this reverse() call will return a 
string like '/polls/3/results/'. where the 3 is the value of question.id. 
This redirected URL will then call the 'results' view to display the final page.
"""