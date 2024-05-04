from django.shortcuts import render
from users.models import Users,Product
from hashlib import sha256
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users.serializers import ProductSerializers

@csrf_exempt
def register(request):
    if request.method=='POST':
        name =request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('passw')
        print(mobile)
     
        try:
            user_obj = Users.objects.filter(email=email)
            if len(user_obj)==0:
                users = Users(username=name,email=email,phone=str(mobile),password=sha256(password.encode('utf-8')).hexdigest())
                users.save()
                return JsonResponse({'status':'200','message':'Users account created successful!'})
            else:
                return JsonResponse({'status':'409','message':'Users already exists'})
        except Exception as e:
            print(e)
            return JsonResponse({'status':'500','message':'Internal Server Error!'})


@csrf_exempt    
def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('passw')
        print(username,sha256(password.encode('utf-8')).hexdigest())
        try:
            user = Users.objects.filter(email=username,password=sha256(password.encode('utf-8')).hexdigest())
            if len(user)==1:
                return JsonResponse({'status':'200','message':'Login Successfully'})
            elif len(user)>1:
                return JsonResponse({'status':'403','message':'Bad request'})
            else:
                return JsonResponse({'status':'404','message':'User not found'})
        except Exception as e:
            print(e)
            return JsonResponse({'status':'500','message':'Internal Server Error!'})
        

@csrf_exempt
def registerAdmin(request):
    if request.method=='POST':
        nameAd =request.POST.get('nameAd')
        emailAd = request.POST.get('emailAd')
        mobileAd = request.POST.get('mobileAd')
        passwordAd = request.POST.get('passwAd')
        print(mobileAd)
     
        try:
            user_obj = Users.objects.filter(email=emailAd)
            if len(user_obj)==0:
                users = Users(username=nameAd,email=emailAd,phone=str(mobileAd),password=sha256(passwordAd.encode('utf-8')).hexdigest())
                users.save()
                return JsonResponse({'status':'200','message':'Users account created successful!'})
            else:
                return JsonResponse({'status':'409','message':'Users already exists'})
        except Exception as e:
            print(e)
            return JsonResponse({'status':'500','message':'Internal Server Error!'})
        
@csrf_exempt    
def loginAdmin(request):
    if request.method=='POST':
        usernameAd = request.POST.get('username')
        passwordAd = request.POST.get('passw')
        print(usernameAd,sha256(passwordAd.encode('utf-8')).hexdigest())
        try:
            user = Users.objects.filter(email=usernameAd,password=sha256(passwordAd.encode('utf-8')).hexdigest())
            if len(user)==1:
                return JsonResponse({'status':'200','message':'Login Successfully'})
            elif len(user)>1:
                return JsonResponse({'status':'403','message':'Bad request'})
            else:
                return JsonResponse({'status':'404','message':'User not found'})
        except Exception as e:
            print(e)
            return JsonResponse({'status':'500','message':'Internal Server Error!'})
        
        
@csrf_exempt
def addProduct(request):
    if request.method=='POST':
        name = request.POST.get('name')
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        image3 = request.FILES['image3']
        image4 = request.FILES['image4']
        price = request.POST.get('price')
        description = request.POST.get('description')
        delivery = request.POST.get('delivery')
        selleremail = request.POST.get('selleremail')
        print(name,price,description,delivery)
        try:
            prod = Product(selleremail=selleremail,productname=name,productdescription=description,productprice=price,deliverycharge=delivery,productImg1=image1,productImg2=image2,productImg3=image3,productImg4=image4)
            prod.save()
            return JsonResponse({'status':'200'})
        except Exception as e:
            print(e)
            return JsonResponse({'status':'500'})
        
@csrf_exempt   
def sellerProduct(request):
    if request.method == 'POST':
        selleremail = request.POST.get('email')
        try:
            prod = Product.objects.filter(selleremail=selleremail)
            prod_ser = ProductSerializers(prod,many=True)
            return JsonResponse(prod_ser.data,safe=False)
        except Exception as e:
            return JsonResponse({'status':'500'})

@csrf_exempt   
def allProduct(request):
    if request.method == 'POST':
   
        try:
            prod = Product.objects.all()
            prod_ser = ProductSerializers(prod,many=True)
            return JsonResponse(prod_ser.data,safe=False)
        except Exception as e:
            return JsonResponse({'status':'500'})
        
@csrf_exempt   
def searchRandom (request):
    try : 
        prod = Product.objects.all().order_by('?')[:1]
        print(len(prod))
        prod_ser = ProductSerializers(prod,many=True)
        return JsonResponse(prod_ser.data,safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'status':'500'})
    
