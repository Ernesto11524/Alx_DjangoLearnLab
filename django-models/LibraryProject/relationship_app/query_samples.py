from models import Author, Book, Library, Librarian

author = Author.objects.create(name = "Ernest")
All_books = Book.objects.all()
librarian1 = Librarian.objects.create(name = "George")
library1 = librarian1.library


author.books.all()