# Deleting a Book Instance in the Django Shell

**Command:**
```python
# Import the Book model
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm the deletion by checking all books
print(Book.objects.all())

Expected Output:

(1, {'bookshelf.Book': 1})  # Indicates that one record was deleted

<QuerySet []>  # Empty QuerySet confirms deletion