from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

@login_required
def java(request):
    return render(request,'myapp/javaexam.html')

@login_required
def python(request):
    return render(request,'myapp/pythonexam.html')

@login_required
def ui(request):
    return render(request,'myapp/uiexam.html')
