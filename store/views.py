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
        try:
            new_book = Book(
                title=request.POST.get('title'),
                author=request.POST.get('author'),
                description=request.POST.get('description'),
                publish_date=request.POST.get('publish_date'),
                price=request.POST.get('price'),
                stock=request.POST.get('stock'),
            )
            new_book.save()
            context['success_message'] = 'The book has been created'
        except:
            context['book_title'] = request.POST.get('title')
            context['author'] = request.POST.get('author')
            context['description'] = request.POST.get('description')
            context['publish_date'] = request.POST.get('publish_date')
            context['price'] = request.POST.get('price')
            context['stock'] = request.POST.get('stock')
            context['error_message'] = 'Error creating book'
            context['display_form'] = True
    else:
        context['display_form'] = True

    return render(request, 'store/book_form.html', context)
