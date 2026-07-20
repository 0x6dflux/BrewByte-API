from django.db import models

from config.base_model import BaseModel


class Ingredient(BaseModel):
    name = models.CharField(max_length=100)
    weight = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.name
