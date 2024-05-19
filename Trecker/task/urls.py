from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', views.TaskDetailViews.as_view(), name='task-detail'),
    path('create/', views.TaskCreateView.as_view(), name='task-create'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register_view, name='register')
]