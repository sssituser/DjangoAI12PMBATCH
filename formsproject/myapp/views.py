from django.shortcuts import render
from myapp.forms import EmployeeForm
# Create your views here.

def home(request):
    empform = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Employee Added...")  
    return render(request,"myapp/home.html",{"form":empform})