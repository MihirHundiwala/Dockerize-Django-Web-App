from django.db import models


# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    shortname = models.CharField(max_length=15)
    imagefile = models.CharField(max_length=50)
    aboutgame = models.TextField()
    officialsite = models.TextField()


class GameRequest(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50, primary_key=True)
    gametitle = models.CharField(max_length=50)
    officialsite = models.TextField()
