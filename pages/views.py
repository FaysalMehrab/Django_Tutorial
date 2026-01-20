from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def home(request):
    all_posts = Post.objects.all()
    context = {
        'year' : 2026,
        'day' : 1,
        'posts': all_posts,
    }

    return render(request, 'home.html', context )

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)

    context = {'post': post}

    return render(request, 'post_detail.html', context)


