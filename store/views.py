from django.shortcuts import render
from .models import Book

# Create your views here.


def index(request):
    context = {
        'title': 'Mystery Books Home',
    }
    return render(request, 'store/index.html', context)


def store(request):
    count = Book.objects.all().count()
    context = {
        'title': 'Mystery Books Store',
        'count': count,
    }
    return render(request, 'store/store.html', context)
