from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic

from models import Question

latest_question_display = 5

class IndexView(generic.ListView):
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:latest_question_display]
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(keyError,Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Please select a valid choice",
        })
	else:
		selected_choice.votes += 1
		selected_choice.save()

    # redirect to results page
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))