from django import forms
from task.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title','description', 'status', 'priority', 'due_date', 'creator'
        ]