from django.urls import path
from .views import list_books, LibraryDetailView
from .views import user_login, user_logout, user_register, list_books, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="list_books"),  # Function-based view for listing books
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Class-based view for library details
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),

]