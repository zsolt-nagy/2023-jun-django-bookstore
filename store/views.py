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


def new_book(request):
    context = {
        'title': 'New Book',
        'menu': 'new_book',
        'display_form': False,
    }
    if request.method == 'POST':
        print(request.POST.get('title'))
        print(request.POST.get('author'))
        print(request.POST.get('description'))
        print(request.POST.get('publish_date'))
        print(request.POST.get('price'))
        print(request.POST.get('stock'))
        context['success_message'] = 'The book has been created'
    else:
        context['display_form'] = True

    return render(request, 'store/book_form.html', context)
