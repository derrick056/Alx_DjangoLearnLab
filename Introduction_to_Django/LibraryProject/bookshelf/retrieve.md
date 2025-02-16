# Retrieving a Book Instance in the Django Shell

**Command:**  
```python
# Import the Book model
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()

# Print the books
print(books)

Expected Output:
<QuerySet [<Book: 1984 by George Orwell (1949)>]>
