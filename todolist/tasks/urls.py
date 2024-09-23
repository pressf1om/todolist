from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('guide/', views.guide, name='guide'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('mytasks/', views.mytasks, name='mytasks'),
    path('mytasks/complete/<int:task_id>/', views.completed_task, name='completed_task'),
]
