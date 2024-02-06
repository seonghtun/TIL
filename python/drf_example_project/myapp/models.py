from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # author = models.CharField(max_length=100)
    publication_date = models.DateField(auto_now_add=True)
    # publication_date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.title