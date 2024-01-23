from django.db import models

class Processors(models.Model):
    caption = models.TextField()
    price = models.IntegerField()
    path_img = models.TextField()

class VideoCards(models.Model):
    caption = models.TextField()
    price = models.IntegerField()
    path_img = models.TextField()

class RAM(models.Model):
    caption = models.TextField()
    price = models.IntegerField()
    path_img = models.TextField()
