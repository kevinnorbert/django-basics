from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self) -> str:
        return self.code

