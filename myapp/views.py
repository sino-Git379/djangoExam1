from django.shortcuts import render, redirect
from .models import Author, Book
# Create your views here.
def main(request):
    return render(request, 'main.html')

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors':authors})


def add_author(request):
    if request.method == 'POST':
        Author.objects.create(
        first_name = request.POST.get('first_name'),
        last_name = request.POST.get('last_name'),
        b_date = request.POST.get('b_date')
        )
        return redirect('authors')
    return render(request, 'add_authors.html')

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def books_detail(request, pk):
    books = Book.objects.get(pk=pk)
    return render(request, 'books_detail.html', {'object':books})

def add_book(request):
    authors = Author.objects.all()
    if request.method == 'POST':
        Book.objects.create(
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            pages = request.POST.get('pages'),
            price = request.POST.get('price'),
            description = request.POST.get('description')
        )
        return redirect('books')
    return render(request, 'add_books.html', {'authors':authors})

def book_update(request, pk):
    authors = Author.objects.all()
    books = Book.objects.get(pk=pk)
    
    if request.method == 'POST':
        books.title = request.POST.get('title')
        books.author = request.POST.get('author')
        books.pages = request.POST.get('pages')
        books.price = request.POST.get('price')
        books.description = request.POST.get('description')
        books.save() 
        
        return redirect('books')
        
    return render(request, 'add_books.html', {'authors': authors, 'book': books})

def book_delete(request, pk):
    books = Book.objects.get(pk=pk)
    books.delete()
    return redirect('books')
    




