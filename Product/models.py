from django.db import models

# Create your models here.

class AddToCart(models.Model):
    useruid = models.CharField(max_length=255,default='0000')
    username = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    productimage = models.ImageField(default='abc.jpg')
    productid = models.CharField(max_length=255)

class WishList(models.Model):
    useruid = models.CharField(max_length=255,default='0000')
    username = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    productimage = models.ImageField(default='abc.jpg')
    productid = models.CharField(max_length=255)