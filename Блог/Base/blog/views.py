from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import AddPostForm


# Страница со  всеми постами
def posts(request):
    posts = Post.objects.all()
    return render(request, "blog/posts.html", {"posts": posts})


# Добавление поста
def add_post(request):
    form = AddPostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data)
            post = Post(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
                author_user_name=form.cleaned_data["author_user_name"],
            )
            post.save()
            return render(request, "success.html")
    else:
        return render(request, "blog/add.html", {"form": form})


# Страница отдельного поста
def single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/single_post.html", {"post": post})


# Страница профиля
def profile(request):
    return render(request, "blog/profile.html")


def about(request):
    return render(request, "blog/about.html")


# Страница контактами поддержки
def support(request):
    return render(request, "blog/support.html")
