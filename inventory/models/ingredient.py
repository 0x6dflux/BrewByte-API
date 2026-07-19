from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField(default=0.0)
