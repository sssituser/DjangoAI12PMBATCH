from django.shortcuts import render

# Create your views here.
def home(request):
    dict1 ={
        "org":"SSSIT PVT LTD",
        "age":"25 years",
        "type":"Provide Online and Offline Trainings, Internships"
    }
    return render(request,'myapp/home.html',dict1)

def register(request):
    dict2 = {
        "ID":4111,
        "NAME":"Kiran Kumar",
        "COURSE":"Python FullStack",
        "TYPE":"OFFLINE Training"
    }
    return render(request,'myapp/register.html',dict2)