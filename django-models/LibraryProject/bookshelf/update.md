**Command:**
```python
# Import the Book model
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"

# Save the changes
book.save()

# Confirm the update
print(Book.objects.get(id=book.id))

Expected Output:
<Book: Nineteen Eighty-Four by George Orwell (1949)>