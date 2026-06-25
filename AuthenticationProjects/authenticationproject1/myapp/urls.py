from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home),
    path('register/',views.register),
    path('javaex/',views.java),
    path('pythonex/',views.python),
    path('uiex/',views.ui),
    # path('logout/',views.logout_view)
    
]