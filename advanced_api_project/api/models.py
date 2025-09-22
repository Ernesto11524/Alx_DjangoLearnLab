from django.db import models

# Create your models here.


# This model is used to create instances of the author of a book.
# It saves the data of the author by taking the author's name.
class Author(models.Model):
    name = models.CharField(max_length=100)

# This model is reposible for saving the data a book.
# It receives the book's title, publication year and the author of the book.
# Therefore, it is connected to the author model in order to save the details of the author.

class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')