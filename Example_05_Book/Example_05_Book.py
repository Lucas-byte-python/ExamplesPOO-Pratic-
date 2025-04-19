# Create Library with Books--------------------------------------------------------
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added to Library "{self.name}".')

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f'Book "{book.title}" removed from Library "{self.name}".')
                return
        print(f'Book with ISBN {isbn} not found in Library "{self.name}".')

    def list_books(self):
        if not self.books:
            print(f'The Library "{self.name}" has no books.')
        else:
            print(f'Books in Library "{self.name}":')
            for book in self.books:
                print(f'- {book.title} by {book.author} (ISBN: {book.isbn})')

# Test The Class

# Create some Books
book1 = Book('The Lord of the Rings', 'J.R.R. Tolkien', '1234567890')
book2 = Book('1984', 'George Orwell', '0987654321')
book3 = Book('The Catcher in the Rye', 'J.D. Salinger', '1122334455')

# Create one Library
library = Library('Main Library')

# Add Books Library
library.add_books(book1)
library.add_books(book2)
library.add_books(book3)
print()

# List full Books of Library
library.list_books()
print()

# Remove one Book of Library
library.remove_book('0987654321')
print()

# Listing all Books of Library Before Remove
library.list_books()
print()
