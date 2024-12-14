from django.db import models


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=127)


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.TextField(max_length=2047)


class Film(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2047)
    preview = models.ImageField(upload_to="preview/%y/%m/%d")
    year_of_release = models.IntegerField()
    premiere = models.DateField()
    country = models.CharField(max_length=63)
    movie = models.FileField(upload_to="music/%Y/%m/%d/")
    mark = models.FloatField()
    is_eighteen = models.BooleanField()
    director = models.CharField(127)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
    )
