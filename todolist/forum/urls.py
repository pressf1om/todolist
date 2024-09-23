from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.forum_index, name='forum_index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),
]
