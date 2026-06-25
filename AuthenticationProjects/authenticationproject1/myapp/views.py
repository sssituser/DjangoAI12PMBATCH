from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from myapp.forms import SingupForm
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

def register(request):
    form = SingupForm()
    if request.method =="POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('login')
    return render(request,'myapp/register.html',{'form':form})

# def logout_view(request):
#     logout(request)
#     return redirect('login')

