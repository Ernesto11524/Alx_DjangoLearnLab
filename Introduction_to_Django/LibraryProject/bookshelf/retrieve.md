from bookshelf.models import Book

book = Book.objects.get(title = "1984")
print(f"{book.title} by {book.author} in {book.publication_year}")

<!-- Expected output: 1984 by George Orwell in 1949 -->