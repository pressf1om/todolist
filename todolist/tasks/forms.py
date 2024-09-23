from django import forms
from .models import Task
from django.core.exceptions import ValidationError
from django.utils import timezone

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']
        labels = {
            'title': 'Название задачи',
            'description': 'Описание',
            'deadline': 'Срок выполнения',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
