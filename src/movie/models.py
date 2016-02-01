from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class Genre(models.Model):
    genre = models.CharField(max_length=30)

    def __unicode__(self):
        return self.genre

class Movie(models.Model):
    name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    release = models.DateField(editable=True)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    owner = models.ForeignKey(User, related_name='movies')


    def __unicode__(self):
        return self.name
