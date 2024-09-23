from django.db import models
from django.contrib.auth.models import User

class ForumPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Поле для содержания поста
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(ForumPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username}'  # Вывод имени пользователя для удобства
