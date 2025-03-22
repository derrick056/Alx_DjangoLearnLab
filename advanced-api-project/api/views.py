from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Explicit Create View for Books
class Book CreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Explicit Update View for Books
class Book UpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Explicit Delete View for Books
class Book DeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Explicit Create View for Authors
class Author CreateView(generics.CreateAPIView):
    """
    API view to create a new author.
    Only authenticated users can create authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

# Explicit Update View for Authors
class Author UpdateView(generics.UpdateAPIView):
    """
    API view to update an existing author.
    Only authenticated users can update authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

# Explicit Delete View for Authors
class Author DeleteView(generics.DestroyAPIView):
    """
    API view to delete an author.
    Only authenticated users can delete authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
