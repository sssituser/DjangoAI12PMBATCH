from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.getproducts,name='products'),
    path('add/',views.addproduct),
    path('find/<int:id>/',views.getproduct),
    path('edit/<int:id>/',views.editproduct),
    path('delete/<int:id>/',views.delproduct),  
]