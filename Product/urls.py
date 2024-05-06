
from django.contrib import admin
from django.urls import path,include
from Product import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('addtocart/',views.addtocart,name='addtocart'),
    path('cartlist/',views.cartlist,name='cartlist'),
    path('category/',views.category_search,name='categorysearch'),
    path('bookorder/',views.bookorder,name='orderbooked')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
