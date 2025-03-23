from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book, Author  # ✅ Fixed import

class BookAPITestCase(TestCase):
    """Test cases for CRUD operations on the Book API"""

    def setUp(self):
        """Set up test client, users, and sample data"""
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password")
        
        # ✅ Use login instead of force_authenticate
        self.client.login(username="testuser", password="password")  # ✅ Added

        # Create a sample author
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create a sample book
        self.book = Book.objects.create(title="Harry Potter", author=self.author, publication_year=1997)

        # API endpoints
        self.list_create_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"

    def test_create_book(self):
        """Test creating a new book"""
        data = {
            "title": "The Hobbit",
            "author": self.author.id,
            "publication_year": 1937
        }
        response = self.client.post(self.list_create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "The Hobbit")

    def test_get_book_list(self):
        """Test retrieving book list"""
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  # At least one book exists

    def test_get_book_detail(self):
        """Test retrieving a specific book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harry Potter")

    def test_update_book(self):
        """Test updating a book"""
        data = {"title": "Harry Potter and the Sorcerer’s Stone"}
        response = self.client.patch(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harry Potter and the Sorcerer’s Stone")

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())


class BookFilteringTestCase(TestCase):
    """Test filtering, searching, and ordering features"""

    def setUp(self):
        """Set up test client and sample data"""
        self.client = APIClient()

        # ✅ Log in the test user
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")  # ✅ Added

        # Create authors
        self.author1 = Author.objects.create(name="J.K. Rowling")
        self.author2 = Author.objects.create(name="Tolkien")

        # Create books
        Book.objects.create(title="Harry Potter", author=self.author1, publication_year=1997)
        Book.objects.create(title="The Hobbit", author=self.author2, publication_year=1937)

    def test_filter_by_author(self):
        """Test filtering books by author"""
        response = self.client.get("/api/books/?author=1")  # Adjust author ID accordingly
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_by_title(self):
        """Test searching books by title"""
        response = self.client.get("/api/books/?search=Harry")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_ordering_by_publication_year(self):
        """Test ordering books by publication year"""
        response = self.client.get("/api/books/?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
