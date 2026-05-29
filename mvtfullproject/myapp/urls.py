from django.urls import path
from myapp import views


urlpatterns=[
   path('',views.showemployees,name='emps'),
   path('addemployee/',views.add,name="addemp"),
]