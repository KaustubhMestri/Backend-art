from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from payment.razorpay.main import RazorpayClient
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from payment.models import History
rz = RazorpayClient()

@csrf_exempt
def create_order(request):
    if request.method=='POST':
        amount = int(float(request.POST.get('amount')))
        currency=request.POST.get('currency')
       
        
        try:
            order_response = rz.create_order(amount=amount,currency=currency)
            return JsonResponse({'orderdata':order_response})
        except Exception as e:
            print(e)
            return JsonResponse({'orderdata':'order failed','status':'400'})
        
@csrf_exempt
def complete_order(request):
    if request.method=='POST':
        order_id = request.POST.get('order_id')
        payment_id =request.POST.get('payment_id')
        signature=request.POST.get('signature')
        amount=int(request.POST.get('amount'))
        userid = request.POST.get('userid')
        # prodid =request.POST.get('productid')
        
        try:
            rz.verify_payment(
                razorpay_order_id=order_id,
                razorpay_payment_id=payment_id,
                razorpay_signature=signature
            )
            history = History(
            order_id=order_id,
            payment_id=payment_id,
            signature=signature,
            amount=amount,
            userid=userid,
        
            )
            history.save()
            return JsonResponse({'status':'200','msg':'order booked succesfully'})

        except Exception as e:
            print(e)
            return JsonResponse({'status':'200','msg':'order booked failed'})