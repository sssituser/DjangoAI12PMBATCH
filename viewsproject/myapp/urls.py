from django.urls import path
from myapp import views
urlpatterns=[
    path('home/',views.home),
    path('reigister/',views.register),
    path('login/',views.login),
]