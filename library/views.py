from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Library
from django.contrib import messages
from django.db.models import Q

# Add a book to the library
def add_book(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        book_id = request.POST['book_id']
        author_name = request.POST['author_name']
        book_status = request.POST['book_status']
        card_id = request.POST.get('card_id', None)

        if not book_name or not book_id or not author_name:
            messages.error(request, "All fields are required.")
            return redirect('add_book')

        # Check if the book already exists
        if Library.objects.filter(book_id=book_id).exists():
            messages.error(request, "Book ID already exists.")
            return redirect('add_book')

        Library.objects.create(book_name=book_name, book_id=book_id, author_name=author_name,
                               book_status=book_status, card_id=card_id)
        messages.success(request, "Book added successfully.")
        return redirect('home')

    return render(request, 'library/add_book.html')


# Display all books
def home(request):
    books = Library.objects.all()
    return render(request, 'library/home.html', {'books': books})


# Remove a book
def remove_book(request, book_id):
    book = Library.objects.get(book_id=book_id)
    book.delete()
    messages.success(request, "Book deleted successfully.")
    return redirect('home')


# Update a book
def update_book(request, book_id):
    book = Library.objects.get(book_id=book_id)
    if request.method == 'POST':
        book.book_name = request.POST['book_name']
        book.author_name = request.POST['author_name']
        book.book_status = request.POST['book_status']
        book.card_id = request.POST.get('card_id', None)
        book.save()
        messages.success(request, "Book updated successfully.")
        return redirect('home')

    return render(request, 'library/update_book.html', {'book': book})


# Search books
def search_books(request):
    query = request.GET.get('q')
    books = Library.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query))
    return render(request, 'library/home.html', {'books': books})
