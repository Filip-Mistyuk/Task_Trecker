from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('inprogres', 'In Progress'),
        ('done', 'Done'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]


    title = models.CharField(max_length=511)
    description = models.TextField()
    status = models.CharField(max_length=31, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=31, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    content = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    media = models.FileField(upload_to='comments_media/', blank=True, null=True)
