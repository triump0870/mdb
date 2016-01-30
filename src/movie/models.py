from django.db import models

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=30)

    def __unicode__(self):
        return self.genre

class Movie(models.Model):
#    _string_validator
    name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    # owner = models.ForeignKey('auth.User')


    def __unicode__(self):
        return self.name
