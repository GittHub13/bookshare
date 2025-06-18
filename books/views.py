from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm

def home(request):
    """Home page view showing featured books"""
    featured_books = Book.objects.filter(status='available')[:4]
    return render(request, 'home.html', {'featured_books': featured_books})

def book_list(request):
    """List all available books"""
    books = Book.objects.filter(status='available')
    return render(request, 'books/list.html', {'books': books})

def book_detail(request, pk):
    """Show details of a specific book"""
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/detail.html', {'book': book})

@login_required
def book_create(request):
    """Create a new book listing"""
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'books/form.html', {'form': form})

@login_required
def book_update(request, pk):
    """Update an existing book listing"""
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/form.html', {'form': form})

@login_required
def book_delete(request, pk):
    """Delete a book listing"""
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'books/confirm_delete.html', {'book': book})