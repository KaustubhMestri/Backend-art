from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=250)

class Admin(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=250)

class Product(models.Model):
    uniqueid = models.IntegerField(max_length=10)
    productname = models.CharField(max_length=255)
    productdescription = models.CharField(max_length=255)
    productprice = models.IntegerField(max_length=20)
    deliverycharge = models.IntegerField(max_length=20)
    dealerId = models.IntegerField(max_length=10)
    dealerName = models.CharField(max_length=20)
    productImg1 = models.ImageField()
    productImg2 = models.ImageField()
    productImg3 = models.ImageField()
    productImg4 = models.ImageField()