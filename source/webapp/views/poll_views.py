from django.urls import reverse_lazy, reverse

from webapp.forms import PollForm
from webapp.models import Poll
from django.views.generic import ListView, DeleteView,DetailView,CreateView,UpdateView


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class PollView(DetailView):
    template_name = 'poll/poll.html'
    model = Poll
    context_object_name = 'poll'



class PollCreateView(CreateView):
    template_name = 'poll/create.html'
    model = Poll
    form_class = PollForm


    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    form_class = PollForm
    template_name = 'poll/update.html'
    model = Poll
    context_object_name = 'mission'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})

class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'poll/delete.html'
    success_url = reverse_lazy('index')
    context_object_name =  'poll'