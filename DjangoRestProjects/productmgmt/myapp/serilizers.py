from myapp.models import Product
from rest_framework import serializers


class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'