from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'deadline']
        labels = {
            'title': 'Название задачи',
            'description': 'Описание',
            'status': 'Статус (выполнено/не выполнено)',
            'deadline': 'Срок выполнения',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
