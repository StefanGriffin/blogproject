from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'StefGriffin',
        'title': 'Blogpost1',
        'content': 'First post content',
        'date_posted': 'July 11, 2020',

    },
    {
        'author': 'StephanG',
        'title': 'Blogpost2',
        'content': 'Second post content',
        'date_posted': 'July 12, 2020',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


    