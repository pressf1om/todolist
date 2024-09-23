from django.shortcuts import render, get_object_or_404, redirect
from .models import ForumPost
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required


@login_required
def forum_index(request):
    posts = ForumPost.objects.all()
    comment_form = CommentForm()
    return render(request, 'forum/forum_index.html', {
        'posts': posts,
        'comment_form': comment_form,
    })


@login_required
def post_detail(request, pk):
    post = get_object_or_404(ForumPost, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Убедитесь, что пользователь аутентифицирован
            comment.save()
            return redirect('forum:post_detail', pk=post.pk)  # Перенаправление на ту же страницу
    else:
        form = CommentForm()

    return render(request, 'forum/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': form,
    })


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Устанавливаем автора
            post.save()
            return redirect('forum:forum_index')  # Перенаправляем на главную страницу форума
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'form': form})
