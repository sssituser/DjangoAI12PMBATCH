from django.shortcuts import render
from myapp.models import Student
from django.http import HttpResponse
# Create your views here.

def home(request):
    students = Student.objects.all()
    for stu in students:
        print(f'{stu.StudentId}\t{stu.StudentName}\t{stu.StudentMarks}')
    return render(request,'myapp/home.html',{"studentlist":students})
