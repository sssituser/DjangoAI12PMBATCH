from django.shortcuts import render,redirect
from myapp.models import Student
from myapp.forms import StudentForm
# Create your views here.

def addstudent(request):
    sform = StudentForm()
    if request.method == 'POST':
        sform = StudentForm(request.POST)
        if sform.is_valid():
            sform.save(commit=True)
            return redirect('/')
    return render(request,'myapp/add.html',{'form':sform}) 
   
def getstudents(request):
    students = Student.objects.all()
    return render(request,'myapp/students.html',{'StuList':students})        