from django.shortcuts import render
from Product.models import AddToCart
from users.models import Product,Users,Admin,BookOrders
from users.serializers import ProductSerializers
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
         for x in add:
            temp = 0
            y = Product.objects.get(id=x.productid)
            temp+=int(y.productprice)
            temp+=int(y.deliverycharge)
            tot +=temp
            temp=0
         return JsonResponse({'addtocart':addserial.data,'total_price':tot})
@csrf_exempt 
def category_search(request):
    if request.method=='POST':
        category = request.POST.get('category')
        cat_prod = Product.objects.filter(productname__icontains=category)
        cat_serial = ProductSerializers(cat_prod,many=True)
        return JsonResponse({'products':cat_serial.data})

@csrf_exempt
def bookorder(request):
    if request.method=='POST':
        useremail = request.POST.get('useruid') #customer email from cookie

        cust = Users.objects.get(email=useremail)

        username = cust.username
        userphone=request.POST.get('userphone')#input
        state = request.POST.get('state')#input
        district = request.POST.get('district')#input
        taluka = request.POST.get('taluka')#input
        city = request.POST.get('city')#input
        landmark = request.POST.get('landmark')
        pincode = request.POST.get('pincode')#input

        productid=request.POST.get('productid') #input each model has invisible id column return that

        prod = Product.objects.get(id =productid)  

        sellerid = prod.selleremail

        selid = Admin.objects.get(email=sellerid)
        sellername = selid.username
        product = request.POST.get('product')
    

        try:
            bookorder = BookOrders(useremail=useremail,username=username,userphone=userphone,state=state,district=district,taluka=taluka,city=city,landmark=landmark,pincode=pincode,sellerid=sellerid,sellername=sellername,product=product,productid=productid,price=prod.price,deliverycharge=prod.deliverycharge)
            bookorder.save()

            add =AddToCart.objects.get(useruid=useremail)
            add.delete()
            return JsonResponse({'status':'200','message':'Order Booked Successful'})
        except Exception as e:
            print(e)


  

      



