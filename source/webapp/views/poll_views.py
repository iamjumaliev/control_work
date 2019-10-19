from webapp.models import Poll
from django.views.generic import ListView



class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1


