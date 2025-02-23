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
