from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden, HttpResponse
from .models import Book
from .forms import BookForm  # ✅ Import BookForm for validation
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ Use Django's form to prevent SQL injection
            return redirect("book_list")
    else:
        form = BookForm()
    
    return render(request, 'bookshelf/book_form.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)  # ✅ Use form for validation
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(request, 'bookshelf/book_form.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

def search_books(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        books = Book.objects.filter(title__icontains=query)  # ✅ Prevents SQL injection
    else:
        books = Book.objects.all()

    return render(request, "bookshelf/book_list.html", {"books": books})

def my_view(request):
    response = HttpResponse("Hello, secure world!")
    
    # ✅ Secure Content Security Policy (CSP)
    response["Content-Security-Policy"] = "default-src 'self'; script-src 'self'; style-src 'self'"
    
    return response
