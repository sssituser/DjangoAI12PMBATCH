from django.urls import path
from myapp import views

urlpatterns =[
    path('',views.getstudents,name='students'),
    path('add/',views.addstudent,name='add'),
]