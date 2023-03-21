from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Task


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todoapp/task.html'


class TaskCreateView(CreateView):
    model = Task
    fields = ('title', 'description', 'is_completed')
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ('title', 'description', 'is_completed')
    success_url = reverse_lazy('task_list')


class TaskListView(ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'todoapp/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(owner=self.request.user)
        search_context = self.request.GET.get('search_field') or ''
        if search_context:
            context['task_list'] = context['task_list'].filter(title__icontains=search_context)
        context['search_context'] = search_context
        return context
