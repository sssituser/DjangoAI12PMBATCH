from django.shortcuts import render

# Create your views here.
def home(request):
    dict1 ={
        "org":"SSSIT",
        "age":"25 Years"

    }
    return render(request,'myapp/home.html',dict1)

def register(request):
    dict2 ={
        "name":"kirankumar",
        "id":"41110",
        "type":"OFFLINE"
    }
    return render(request,'myapp/register.html',dict2)

def login(request):
    return render(request,'myapp/login.html')

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')