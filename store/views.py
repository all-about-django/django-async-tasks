from django.shortcuts import render

from .models import Book


def download_book(request):
    template_name = 'store/book_list.html'
    books = Book.objects.all()
    return render(request, template_name, {
        'books': books,
    })
