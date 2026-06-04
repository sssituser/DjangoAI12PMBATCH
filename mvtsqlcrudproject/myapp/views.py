from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import Product
from myapp.forms import ProductForm
# Create your views here.

def addproduct(request):
    pform = ProductForm()
    if request.method=='POST':
        pform=ProductForm(request.POST)
        if pform.is_valid():
            pform.save(commit=True)
            return redirect("/")
    return render(request,'myapp/add.html',{'form':pform})

def getproducts(request):
    products = Product.objects.all()
    return render(request,'myapp/products.html',{'pros':products})

def getproduct(request,id):
    prod = get_object_or_404(Product,ProductId=id)
    return render(request,'myapp/find.html',{'product':prod})

def delproduct(request,id):
    prod = get_object_or_404(Product,ProductId=id)
    if request.method=='POST':
        prod.delete()
        return redirect('/')
    return render(request,'myapp/delete.html',{'product':prod})


def editproduct(request,id):
    prod = get_object_or_404(Product,ProductId=id)
    pform =ProductForm(instance=prod)
    if request.method=='POST':
        pform = ProductForm(request.POST,instance=prod)
        pform.save()
        return redirect("/")
    return render(request,'myapp/edit.html',{'form':pform})
        
    