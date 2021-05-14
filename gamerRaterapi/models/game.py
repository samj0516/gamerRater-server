from django.db import models
from django.db.models.fields import IntegerField

class Game(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=100)
    number_of_players = models.IntegerField(null=True)
    age_rec = models.IntegerField(null=True)
    year_released = models.CharField(max_length=5)

    categories = models.ManyToManyField('Category', through = 'GameCategory')
