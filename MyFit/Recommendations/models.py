from django.db import models

# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=255)
    vegetarian = models.BooleanField()
    ready_mins = models.IntegerField()
    link = models.URLField()

class Exercises(models.Model):
    name = models.CharField(max_length=255)
    primary_muscle = models.CharField(max_length=100)
    instructions = models.TextField()
    level = models.CharField(max_length=100)