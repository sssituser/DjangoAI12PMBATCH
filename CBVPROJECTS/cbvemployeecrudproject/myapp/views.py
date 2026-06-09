from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from myapp.models import Employee
# Create your views here.

class EmployeeList(ListView):
    model = Employee
    fileds = '__all__'
    
class CreateEmployee(CreateView):
    model = Employee
    fields = '__all__'
class UpdateEmployee(UpdateView):
    model = Employee
    fields = '__all__'
class EmployeeDetails(DetailView):
    model = Employee
    fields = '__all__'

class DeleteEmpoyee(DeleteView):
    model = Employee
    success_url = reverse_lazy('EmployeeList')    