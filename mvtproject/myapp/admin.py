from django.contrib import admin
from myapp.models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=["ProductId","ProductName","ProductPrice"]
admin.site.register(Product,ProductAdmin)
