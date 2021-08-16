from django.db import models

# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=200)
    order_no = models.CharField(max_length=50, unique=True)
    grand_total = models.FloatField()

class OrderLine(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    tax_rate = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)