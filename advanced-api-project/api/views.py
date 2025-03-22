from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Book Views
class BookListView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of books or create a new one.
    Allows filtering and searching by title, and ordering by title or publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title', 'publication_year']
    search_fields = ['title']

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific book.
    Only authenticated users can modify books, but anyone can view them.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Author Views
class AuthorListView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of authors or create a new one.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete an author.
    Only authenticated users can modify authors, but anyone can view them.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
