from django.shortcuts import render,redirect,get_object_or_404
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
     
def getstudent(request,id):
    student = get_object_or_404(Student,StudentId=id)
    return render(request,'myapp/find.html',{'stud':student})

def editstudent(request,id):
    student = get_object_or_404(Student,StudentId=id)
    sform = StudentForm(instance=student)
    if request.method=='POST':
        sform = StudentForm(request.POST,instance=student)
        if sform.is_valid():
            sform.save()
            return redirect('/')
    return render(request,'myapp/edit.html',{'form':sform})

def deletestudent(request,id):
    student = get_object_or_404(Student,StudentId=id)
    if request.method =="POST":
        student.delete()
        return redirect('/')
    return render(request,'myapp/delete.html',{'stud':student})