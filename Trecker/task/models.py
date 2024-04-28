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
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
