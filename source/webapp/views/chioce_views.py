from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView,UpdateView, DeleteView

from webapp.forms import PollChoiceForm,ChoiceForm
from webapp.models import Choice, Poll


class ChoiceForPollCreateView(CreateView):
    model = Choice
    template_name = 'choice/create.html'
    form_class = PollChoiceForm

    def dispatch(self, request, *args, **kwargs):
        self.poll = self.get_poll()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.poll.choice_poll.create(**form.cleaned_data)
        return redirect('poll_view', pk=self.poll.pk)

    def get_poll(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)





class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/update.html'
    form_class = ChoiceForm
    context_object_name = 'choice'


    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice/delete.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})