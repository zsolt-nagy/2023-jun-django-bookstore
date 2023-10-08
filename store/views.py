from django.shortcuts import render
from .models import Book

# Create your views here.


def index(request):
    context = {
        'title': 'Mystery Books Home',
        'menu': 'home',
    }
    return render(request, 'store/index.html', context)


def store(request):
    books = Book.objects.all()
    count = books.count()
    context = {
        'title': 'Mystery Books Store',
        'books': books,
        'count': count,
        'menu': 'store',
    }
    return render(request, 'store/store.html', context)


def book_details(request, book_id):
    context = {
        'menu': 'store',
        'has_error': False,
    }
    try:
        book = Book.objects.get(id=book_id)
        context['title'] = book.title
        context['book'] = book
    except:
        context['title'] = 'The book you are looking for is not available'
        context['has_error'] = True
    return render(request, 'store/book_details.html', context)
