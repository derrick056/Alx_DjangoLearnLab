from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView
)

urlpatterns = [
    # Book URLs
    path('books/', BookListView.as_view(), name='book-list'),  # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve a single book
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a book
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),  # Update a book
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book

    # Author URLs
    path('authors/', AuthorListView.as_view(), name='author-list'),  # List all authors
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),  # Retrieve a single author
    path('authors/create/', AuthorCreateView.as_view(), name='author-create'),  # Create an author
    path('authors/update/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),  # Update an author
    path('authors/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author-delete'),  # Delete an author
]
