from django.shortcuts import render
from book.models import Book

def book(request):
    
    books = Book.objects.all()

    context = {'books':books}
    return render(request, 'book/book.html', context)
