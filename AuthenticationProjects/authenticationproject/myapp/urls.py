from django.urls import path
from myapp import views

urlpatterns =[
    path('',views.home),
    path('java/',views.javaex),
    path('python/',views.pythonex),
    path('ui/',views.uiex),
    
]