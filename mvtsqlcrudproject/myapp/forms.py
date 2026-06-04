from django import forms
from myapp.models import Product

class ProductForm(forms.ModelForm):
    ProductId = forms.IntegerField()
    ProdutName = forms.CharField(max_length=50)
    ProductPrice =forms.DecimalField(max_digits=8,decimal_places=2)
    class Meta:
        model = Product
        fields ='__all__'  