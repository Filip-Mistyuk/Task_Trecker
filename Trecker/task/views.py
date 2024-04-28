from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from . import models
from . forms import TaskForm

class TaskListView(ListView):
    model = models.Task
    context_object_name = 'tasks'

class TaskDetailViews(DetailView):
    model = models.Task
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = models.Task
    form_class = TaskForm
    success_url = reverse_lazy('task:task-list')