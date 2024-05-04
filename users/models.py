from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=250)

class Admin(models.Model):
    username = models.CharField(max_length=254)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=250)

class Product(models.Model):
    selleremail = models.EmailField()
    productname = models.CharField(max_length=255)
    productdescription = models.TextField()
    productprice = models.IntegerField()
    deliverycharge = models.IntegerField()
    productImg1 = models.ImageField(upload_to='')
    productImg2 = models.ImageField(upload_to='')
    productImg3 = models.ImageField(upload_to='')
    productImg4 = models.ImageField(upload_to='')


class BookOrders(models.Model):
        useruid = models.CharField(max_length=255,default='0000')
        username = models.CharField(max_length=255)
        useremail = models.EmailField()
        userphone = models.CharField(max_length=10)
        state = models.CharField(max_length=50)
        district = models.CharField(max_length=50)
        taluka = models.CharField(max_length=50)
        city = models.CharField(max_length=50)
        landmark = models.CharField(max_length=255)
        pincode = models.IntegerField()
        sellerid = models.CharField(max_length=255)
        sellername = models.CharField(max_length=255)
        date = models.DateField(auto_now_add=True)
        product = models.CharField(max_length=255)
        productimage = models.ImageField(default='abc.jpg')
        productid = models.CharField(max_length=255)
        price = models.IntegerField()
        deliverycharge = models.IntegerField(default=0)
        totalprice = models.IntegerField()

