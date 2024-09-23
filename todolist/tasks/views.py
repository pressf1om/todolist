from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task
from django.contrib import messages

def index(request):
    context = {
    }
    return render(request, 'tasks/index.html', context)

def profile(request):
    context = {
    }
    return render(request, 'tasks/profile.html', context)

def about(request):
    context = {
    }
    return render(request, 'tasks/about.html', context)

def guide(request):
    context = {
    }
    return render(request, 'tasks/guide.html', context)


@login_required()
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:mytasks')  # Перенаправление на страницу со списком задач
    else:
        form = TaskForm()

    context = {
        'form': form,
    }
    return render(request, 'tasks/create_task.html', context)

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if task.user != request.user:
        return redirect('tasks:mytasks')  # Перенаправляем, если пользователь не владелец

    if request.method == 'POST':
        if 'undone' in request.POST:
            task.status = False
            task.save()
            form = TaskForm(request.POST, instance=task) # Перезагружаем форму, чтобы данные не сбрасывались

            if form.is_valid():
                form.save()  # Сохраняем данные формы
            return redirect('tasks:mytasks')

        if 'delete' in request.POST:
            task.delete()
            return redirect('tasks:mytasks')

        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:mytasks')
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task,
    }

    return render(request, 'tasks/edit_task.html', context)


def mytasks(request):
    tasks = Task.objects.filter(user=request.user)  # Получаем задачи текущего пользователя
    context = {
        'tasks': tasks
               }
    return render(request, 'tasks/mytasks.html', context)


def completed_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if not task.status:  # Если задача еще не выполнена
        task.status = True
        task.save()
    return redirect('tasks:mytasks')

