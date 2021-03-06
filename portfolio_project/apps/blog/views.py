from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post, Comment
from .forms import CommentForm
from utils.utils import paginator_use


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    posts = paginator_use(request, posts, num=3)
    context = {
        "posts": posts,

    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    filter = Post.objects.filter(pk=pk)
    post = get_object_or_404(filter, pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return redirect('blog_detail', pk)

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog_detail.html", context)
