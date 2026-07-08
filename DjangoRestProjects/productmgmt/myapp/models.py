from django.db import models

# Create your models here
class Product(models.Model):
    ProductId = models.IntegerField(primary_key=True)
    ProductName  = models.CharField(max_length=30)
    Price = models.DecimalField(max_digits=8,decimal_places=2)
    def __str__(self):
        return self.ProductName