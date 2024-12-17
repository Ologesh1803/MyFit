from django.db import models

# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=200)
    vegetarian = models.BooleanField()
    ready_mins = models.IntegerField()
    link = models.URLField()