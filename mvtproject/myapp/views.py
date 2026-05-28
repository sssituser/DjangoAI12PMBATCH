from django.shortcuts import render,redirect
from myapp.forms import ProductForm
from myapp.models import Product
# Create your views here.
def addproduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("products")
    return render(request,'myapp/addproduct.html',{"form":form})

def products(request):
    prods=Product.objects.all()
    return render(request,'myapp/showproducts.html',{"products":prods})
    