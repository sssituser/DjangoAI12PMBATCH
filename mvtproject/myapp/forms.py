from django import forms
from myapp.models import Product

class ProductForm(forms.ModelForm):
    ProductId = forms.IntegerField()
    ProductName = forms.CharField(max_length=30)
    ProductPrice = forms.DecimalField(max_digits=7,decimal_places=2)
    class Meta:
        model = Product
        fields = '__all__'