from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
from .models import Book
from .models import Library


from django.shortcuts import render
from .models import Book

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