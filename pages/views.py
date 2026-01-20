from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

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

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = PostForm()

    return render(request, 'create_post.html', {'form':form})




