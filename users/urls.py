
from django.contrib import admin
from django.urls import path,include
from users import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('registerAd/',views.registerAdmin,name='registerAdmin'),
    path('loginAd/',views.loginAdmin,name='loginAdmin')
]
