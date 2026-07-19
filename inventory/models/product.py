from django.db import models


class Product(models.Model):
    category = models.ForeignKey("inventory.Category", models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    average_score = models.FloatField(default=0.0)
    inventory_stock = models.IntegerField(default=0)
    sale_stock = models.IntegerField(default=0)
    # validator: sale_stock <= inventory_stock
    ingredients = models.ForeignKey("inventory.Ingredient", models.CASCADE)
