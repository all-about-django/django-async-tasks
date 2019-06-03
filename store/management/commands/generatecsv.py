import csv
import os

from os.path import join

from django.core.management.base import BaseCommand, CommandError

from store.models import Book


class Command(BaseCommand):
    '''
        To run, use

        python manage.py generatecsv

        Creates a csv file for all objects of `store.Book` model
    '''

    help_text = 'Creates a csv file for all objects of `store.Book` model'
    can_import_settings = True

    def _fetch_data(self):
        return Book.objects.all()

    def _get_csv_dir(self):
        '''
        We will generate all csv files in a folder named `csvfile`
        '''
        csv_dir = join(os.getcwd(), 'csvfile')
        if not os.path.exists(csv_dir):
            os.mkdir(csv_dir)
        return csv_dir

    def generate_csv(self, file_id):
        books = self._fetch_data()
        csv_dir = self._get_csv_dir()
        csv_file = '{}.csv'.format(file_id)
        csv_file_path = join(csv_dir, csv_file)
        with open(csv_file_path, 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Book Name', 'ISBN Number'])
            for book in books:
                writer.writerow([book.name, book.isbn_number])

    def add_arguments(self, parser):
        parser.add_argument('file_id', nargs='?', help='Specify File Id here')

    def handle(self, *args, **options):
        if not options['file_id']:
            raise CommandError("Option `--file_id...` must be specified.")

        file_id = options.get('file_id')
        print ('Starting csv file generation')
        self.generate_csv(file_id)
        print ('Successfully generated csv file {}'.format(file_id))
