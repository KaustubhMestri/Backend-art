from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=255)