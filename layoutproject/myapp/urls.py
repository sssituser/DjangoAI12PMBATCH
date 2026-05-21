from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.home,name='xyz'),
    path('register/',views.register,name='pqr'),
    path('login/',views.login,name='lmn'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]