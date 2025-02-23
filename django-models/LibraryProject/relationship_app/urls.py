from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from .views import user_login, user_logout, user_register, list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, list_books, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
]