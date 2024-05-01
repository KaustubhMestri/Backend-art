from django.shortcuts import render
from users.models import Users
from hashlib import sha256
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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