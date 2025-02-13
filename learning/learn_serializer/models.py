from django.db import models

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=200)
    author =  models.CharField(max_length=200)
    published_date = models.DateField()
    author_dob = models.DateField()
    

class Author(models.Model):
    author =  models.CharField(max_length=200)
    number_of_books = models.IntegerField()

