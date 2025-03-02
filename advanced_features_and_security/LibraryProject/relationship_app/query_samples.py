import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")  # Ensure the correct project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library (Fix applied here)
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # Correct usage
    return librarian

# Sample Data Creation (Only run this once to avoid duplicate records)
if __name__ == "__main__":
    # Creating objects
    author, _ = Author.objects.get_or_create(name="J.K. Rowling")
    book1, _ = Book.objects.get_or_create(title="Harry Potter and the Sorcerer's Stone", author=author)
    book2, _ = Book.objects.get_or_create(title="Harry Potter and the Chamber of Secrets", author=author)

    library, _ = Library.objects.get_or_create(name="Central Library")
    library.books.add(book1, book2)

    librarian, _ = Librarian.objects.get_or_create(name="John Doe", library=library)

    # Running Queries
    print("Books by J.K. Rowling:", list(get_books_by_author("J.K. Rowling")))
    print("Books in Central Library:", list(get_books_in_library("Central Library")))
    print("Librarian of Central Library:", get_librarian_for_library("Central Library"))