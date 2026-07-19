from django.db import models

from config.base_model import BaseModel


class Picture(BaseModel):
    product = models.ForeignKey("inventory.Product", models.CASCADE)
    file_path = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.product}-pic"
