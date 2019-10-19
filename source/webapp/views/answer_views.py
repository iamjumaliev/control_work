from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View, TemplateView

from webapp.models import Answer, Poll, Choice


class AnswerView(TemplateView):


    template_name = 'answer/answer.html'
    context_object_name = 'answers'
    model = Answer
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poll'] = get_object_or_404(Poll, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=kwargs['pk'])
        choice = Choice.objects.get(pk=request.POST.get('box'))
        Answer.objects.create(poll=poll, choice=choice)
        context = {
            'poll':poll
        }
        return render(request, 'poll/index.html', context=context)



