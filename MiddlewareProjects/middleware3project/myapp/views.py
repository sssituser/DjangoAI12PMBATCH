from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse(f'<h1 style="text-align:center;color:green">Hi Iam In Home Page , In Calculations,  res is : {10/0}</h1>')
    