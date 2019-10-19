from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse

from webapp.forms import PollForm,ChoiceForm,PollChoiceForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = self.object
        context['form'] = PollChoiceForm()
        choices = poll.choice_poll.all()
        self.paginate_choices_to_context(choices, context)
        return context

    def paginate_choices_to_context(self, choices, context):
        paginator = Paginator(choices, 5, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['choices'] = page.object_list
        context['is_paginated'] = page.has_other_pages()



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