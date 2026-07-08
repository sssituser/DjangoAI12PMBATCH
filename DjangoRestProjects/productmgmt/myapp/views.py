from django.shortcuts import render
from rest_framework  import viewsets
from myapp.models import Product
from myapp.serilizers import ProductSerilizer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer
