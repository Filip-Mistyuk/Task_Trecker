from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . forms import TaskForm, TaskFilterForm
from task.mixins import UserIsOwnerMixin

class TaskListView(ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'task/task_list.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status', '')
        if status:
            queryset = queryset.filter(status=status)
        queryset = queryset.filter(creator=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskFilterForm(self.request.GET)
        return context


class TaskDetailViews(DetailView):
    model = models.Task
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = models.Task
    form_class = TaskForm
    success_url = reverse_lazy('task:task-list')

class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = models.Task
    form_class = TaskForm
    success_url = reverse_lazy('task:task-list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Task
    success_url = reverse_lazy('task:task-list')

