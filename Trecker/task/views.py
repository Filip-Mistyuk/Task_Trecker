from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from . import models
from . forms import TaskForm, TaskFilterForm, CommentForm
from task.mixins import UserIsOwnerMixin
from django.contrib.auth.decorators import login_required

class TaskListView(LoginRequiredMixin, ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'task/task_list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = models.Task.objects.filter(user=user)
        status = self.request.GET.get('status', '')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskFilterForm(self.request.GET)
        return context


class TaskDetailViews(DetailView):
    model = models.Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comment_form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.task = self.get_object()
            comment.save()
            return redirect('task:task-detail', pk=comment.task.pk)

class TaskCreateView(CreateView):
    model = models.Task
    form_class = TaskForm
    success_url = reverse_lazy('task:task-list')
    template_name = 'task/task_create.html'

class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = models.Task
    form_class = TaskForm
    success_url = reverse_lazy('task:task-list')
    template_name = 'task/task_update.html'

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Task
    success_url = reverse_lazy('task:task-list')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task:task-list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'task/login.html')

def custom_logout(request):
    logout(request)
    return redirect('task:task-list') 

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task:task-list') 
    else:
        form = UserCreationForm()
    return render(request, 'task/register.html', {'form': form})


