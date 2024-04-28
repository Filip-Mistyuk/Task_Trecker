from django.urls import path
from task import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', views.TaskDetailViews.as_view(), name='task-detail'),
    path('<task_create>/', views.TaskCreateView.as_view(), name='task-create'),
]

app_name = 'task'
