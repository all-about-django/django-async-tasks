from django.urls import path

from . import views


urlpatterns = [
    path('book', views.download_book,
         name='book-list'),
]
