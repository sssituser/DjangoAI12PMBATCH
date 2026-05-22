from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1 style='text-align:center'>Hi this is my first project</h1>")

def login(request):
    return HttpResponse("<h1 style='text-align:center'>Hi this is Login</h1>")

def register(request):
    return HttpResponse("<h1 style='text-align:center'>Hi this is Register Page</h1>")

