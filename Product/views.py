from django.shortcuts import render
from Product.models import AddToCart
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Product.serializers import AddtoCartSerializers
# Create your views here.

@csrf_exempt  
def addtocart(request):
    if request.method=='POST':
        useruid = request.POST.get('useruid')
        username = request.POST.get('username')
        product = request.POST.get('product')
     
        productid = request.POST.get('productid')
       
        prod = AddToCart(username=username,useruid=useruid,product=product,productid=productid)
        prod.save()
        return JsonResponse({'status':'200'})
    return JsonResponse({'status':'500'})

@csrf_exempt
def cartlist(request):
     if request.method=='POST':
         email = request.POST.get('email')
         add = AddToCart.objects.filter(useruid=email)
         addserial = AddtoCartSerializers(add,many=True)
         tot=0
         return JsonResponse({'addtocart':addserial.data})

