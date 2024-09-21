from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CreationForm
from django.urls import reverse_lazy
class SignUp(CreateView):
    form_class = CreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('tasks:index')