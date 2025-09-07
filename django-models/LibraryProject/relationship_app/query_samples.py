from models import Author, Book, Library, Librarian

author_name = Author.objects.create(name="author_name")
author = Author.objects.get(name=author_name)
Author.objects.filter(author=author)
library_name = Library.objects.create(name="Library_name")
All_books = Library.objects.get(name=library_name)
librarian1 = Librarian.objects.get(library="Science Library")
library1 = librarian1.library


author.books.all()