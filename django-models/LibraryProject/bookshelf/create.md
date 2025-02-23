# Creating a Book Instance in the Django Shell

**Command:**  
```python
# Import the Book model
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verify that the book was created
print(book)

Expected Output:

<Book: 1984 by George Orwell (1949)>