from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice, Location


class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'latest_location_list'

    def get_queryset(self):
        """
        Return the all locations alphabetically
        """
        return Location.objects.order_by('location_name')


class DetailView(generic.DetailView):
    model = Location
    template_name = 'pages/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Location.objects


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'pages/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'pages/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pages:results', args=(question.id,)))
