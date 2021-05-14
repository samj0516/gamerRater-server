from django.db import models
from django.db.models.deletion import CASCADE

class GamePics(models.Model):
    pic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    gamer = models.ForeignKey('Gamer', on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
