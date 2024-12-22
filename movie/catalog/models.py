from django.db import models

from core.models import AbstractImageModel


class Film(AbstractImageModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2047)
    image = models.ImageField(upload_to="preview/%y/%m/%d")
    year_of_release = models.IntegerField()
    premiere = models.DateField()
    country = models.CharField(max_length=63)
    movie = models.FileField(upload_to="film/%Y/%m/%d/")
    mark = models.FloatField()
    is_eighteen = models.BooleanField()
    director = models.CharField()
    genre = models.ManyToManyField(
        "Genre",
    )


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    film = models.OneToOneField(
        Film,
        on_delete=models.CASCADE,
    )
    comment = models.TextField(max_length=2047)
