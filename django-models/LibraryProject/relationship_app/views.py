from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from .models import Book
from django.contrib.auth.decorators import permission_required
from .forms import BookForm


# Create your views here.
from .models import Book
from .models import Library


from django.shortcuts import render
from .models import Book

def home(request):
    return render(request, 'home.html')

def list_books(request):
    books = Book.objects.all()  
    return render(request, "relationship_app/list_books.html", {"books": books}) 

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# User Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")  # Redirect to books list after login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# User Registration View
def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")  # Redirect to books list after registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Class-Based User Registration View
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "relationship_app/register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")  # Redirect to login page after successful registration
        return render(request, "relationship_app/register.html", {"form": form})

def check_role(role):
    def has_role(user):
        return user.is_authenticated and user.userprofile.role == role
    return user_passes_test(has_role)

@check_role('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@check_role('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@check_role('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

def register(request):
    return render(request, "relationship_app/register.html")

def is_admin(user):
    return user.is_superuser  # Or any custom check

@user_passes_test(is_admin, login_url="/login/")
def add_book(request):
    # Add book logic here
    return render(request, "relationship_app/add_book.html")

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Redirect to book list after adding
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Redirect after edit
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')  # Redirect after delete
    return render(request, 'relationship_app/confirm_delete.html', {'book': book})