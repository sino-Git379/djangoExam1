from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    b_date = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    title = models.CharField( max_length=50)
    author = models.CharField( max_length=50)
    pages = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField( max_length=100)
    models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    