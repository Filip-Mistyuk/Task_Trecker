from django import forms
from task.models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title','description', 'status', 'priority', 'due_date', 'creator'
        ]

class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'All'),
        ('todo', 'To Do'),
        ('inprogres', 'In Progress'),
        ('done', 'Done'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label='status')

    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        self.fields["status"].widget.attrs.update({"class": "form-control"})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'media']
        widgets = {
            'media': forms.FileInput()
        }

