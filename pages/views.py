from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'year' : 2026,
        'day' : 1,
    }

    return render(request, 'home.html', context )

# Create your views here.
