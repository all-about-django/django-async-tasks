from django.shortcuts import render

from .models import Book


def download_book(request):
    template_name = 'store/book_list.html'
    books = Book.objects.all()
    if request.method == 'GET':
        is_download = request.GET.get('is_download', None)
        if is_download == '1':
            print ('Request for csv processing')
    return render(request, template_name, {
        'books': books,
    })
