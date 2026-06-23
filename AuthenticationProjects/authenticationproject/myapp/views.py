from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login
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
from myapp.forms import RegistrationForm
def singup(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login/')
    return render(request,'myapp/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

