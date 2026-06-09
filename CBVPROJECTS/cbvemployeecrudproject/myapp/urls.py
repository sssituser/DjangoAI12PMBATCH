from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.EmployeeList.as_view(),name="EmployeeList"),
    path('<int:pk>/',views.EmployeeDetails.as_view()),
    path('edit/<int:pk>/',views.UpdateEmployee.as_view()),
    path('delete/<int:pk>/',views.DeleteEmpoyee.as_view()),
    path('create/',views.CreateEmployee.as_view()),
]