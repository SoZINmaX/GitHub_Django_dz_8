from django.contrib.postgres.fields import ArrayField
from django.db import models


class Movie(models.Model):
    class TitleType(models.TextChoices):
        SHORT = "short", "Short"
        MOVIE = "movie", "Movie"

    imdb_id = models.CharField("tconst", max_length=255, null=True)
    title_type = models.CharField("titleType", max_length=255, choices=TitleType.choices)
    name = models.CharField("primaryTitle", max_length=255)
    is_adult = models.BooleanField("isAdult", default=False)
    date = models.DateField("startYear", auto_now=False, auto_now_add=False, null=True)
    genres = ArrayField(models.CharField(max_length=255), verbose_name="genres", null=True)

    def __str__(self):
        return f"M: {self.name}"


class Person(models.Model):
    imdb_id = models.CharField("nconst", max_length=255, null=True)
    name = models.CharField("primaryName", max_length=255)
    birth_date = models.DateField("birthYear", null=True)
    death_date = models.DateField("deathYear", null=True)

    def __str__(self):
        return f"P: {self.name}"


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    order = models.IntegerField("ordering", null=True)
    category = models.CharField("category", max_length=255)
    job = models.CharField("job", max_length=255, null=True)
    characters = ArrayField(models.CharField(max_length=255), verbose_name="characters", null=True)
