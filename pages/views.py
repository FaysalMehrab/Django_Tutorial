from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    all_data = Post.objects.all()
    context = {
        'year' : 2026,
        'day' : 1,
        'posts': all_data,
    }

    return render(request, 'home.html', context )


