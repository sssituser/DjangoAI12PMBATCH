from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

@login_required
def javaex(request):
    return render(request,'myapp/javaexam.html')

@login_required
def pythonex(request):
    return render(request,'myapp/pythonexam.html')

@login_required
def uiex(request):
    return render(request,'myapp/ui.html')
