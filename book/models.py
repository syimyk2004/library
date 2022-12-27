from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=100)


class Picture(models.Model):
    image = models.ImageField(upload_to='books')
    book =  models.ForeignKey('Book', related_name='books_pictures', on_delete=models.SET_NULL, null=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    year = models.PositiveSmallIntegerField()
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title