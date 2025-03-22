from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# ---- BOOK VIEWS ----

# List View - Retrieve a list of books
class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books.
    Allows filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title', 'publication_year']
    search_fields = ['title']

# Detail View - Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create View - Add a new book
class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Update View - Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete View - Remove a book
class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# ---- AUTHOR VIEWS ----

# List View - Retrieve a list of authors
class AuthorListView(generics.ListAPIView):
    """
    API view to retrieve a list of authors.
    Supports searching.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

# Detail View - Retrieve a single author
class AuthorDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

# Create View - Add a new author
class AuthorCreateView(generics.CreateAPIView):
    """
    API view to create a new author.
    Only authenticated users can create authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

# Update View - Modify an existing author
class AuthorUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing author.
    Only authenticated users can update authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete View - Remove an author
class AuthorDeleteView(generics.DestroyAPIView):
    """
    API view to delete an author.
    Only authenticated users can delete authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
