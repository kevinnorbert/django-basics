from django.db import models

# Create your models here.
class Products:
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    unit_price = models.DecimalField()

