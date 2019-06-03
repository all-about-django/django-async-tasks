import os
import subprocess

from os.path import join

from django.shortcuts import render
from django.utils.crypto import get_random_string

from .models import Book


def download_book(request):
    template_name = 'store/book_list.html'
    books = Book.objects.all()
    if request.method == 'GET':
        is_download = request.GET.get('is_download', None)
        if is_download == '1':
            file_id = get_random_string(10)
            print ('Request for csv processing', file_id)
            # we will generate log for `generatecsv.py` in `csvlogs`
            # directory, in the directory where `manage.py` is present
            # change accordingly
            log_dir = join(os.getcwd(), 'csvlogs')
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)
            log_file = open(join(log_dir, 'gcsv.log'), 'a+')
            error_log_file = open(join(log_dir, 'gcsverror.log'), 'a+')
            manage_py_location = join(os.getcwd(), 'manage.py')
            # in my case, name of virutal env is 'pyenv'
            python_path = join(os.getcwd(), 'pyenv', 'bin', 'python')
            command_run_args = [python_path, manage_py_location, 'generatecsv']
            args = [file_id, ]
            subprocess.Popen(command_run_args + args,
                             env=os.environ.copy(),
                             stdout=log_file,
                             stderr=error_log_file,
                             )
    return render(request, template_name, {
        'books': books,
    })
