from django.db import models

# Create your models here.
class Product(models.Model):
    ProductId =   models.IntegerField()
    ProductName = models.CharField(max_length=30)
    ProductPrice = models.DecimalField(max_digits=7,decimal_places=2)
