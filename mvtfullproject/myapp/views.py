from django.shortcuts import render,redirect
from myapp.forms import EmployeeForm
from myapp.models import Employee
# Create your views here.
def add(request):
    empform = EmployeeForm()
    if request.method == 'POST':
        empform = EmployeeForm(request.POST)
        if empform.is_valid():
            empform.save(commit=True)
            return redirect('emps')
    return render(request,'myapp/addemployee.html',{"form":empform})

def showemployees(request):
    emplist = Employee.objects.all()
    return render(request,'myapp/employees.html',{'employees':emplist})


    