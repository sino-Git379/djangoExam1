from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('authors/', authors_list, name='authors'),
    path('add_author/', add_author, name='add_author'),
    path('books/', books_list, name='books'),
    path('add_books/', add_book, name='add_book'),
    path('books_detail/<int:pk>/', books_list, name='books_detail'),
    path('update/<int:pk>/', book_update, name='update')
]