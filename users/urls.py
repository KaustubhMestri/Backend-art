
from django.contrib import admin
from django.urls import path,include
from users import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('registerAd/',views.registerAdmin,name='registerAdmin'),
    path('loginAd/',views.loginAdmin,name='loginAdmin'),
    path('addproduct/',views.addProduct,name='Add'),
    path('sellerprod/',views.sellerProduct,name='seller'),
    path('all/',views.addProduct,name='AllProduct'),
    path('serchrandom/',views.searchRandom,name='Random')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
