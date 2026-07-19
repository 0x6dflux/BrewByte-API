from django.db import models


class Picture(models.Model):
    product = models.ForeignKey("inventory.Product", models.CASCADE)
    file_path = models.CharField(max_length=250)
