from models import Author, Book, Library, Librarian

author = Author.objects.create(name = "Ernest")
library_name = Library.objects.create(name="Library_name")
All_books = Library.objects.get(name=library_name)
librarian1 = Librarian.objects.create(name = "George")
library1 = librarian1.library


author.books.all()