from django.urls import path
from myapp import views

urlpatterns =[
    path('',views.addproduct),
    path('products/',views.products,name="products"),
]