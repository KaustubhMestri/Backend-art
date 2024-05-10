from django.db import models



class History(models.Model):
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    signature = models.CharField(max_length=100)
    amount = models.IntegerField()
    userid = models.CharField(max_length=100)
    # prodid = models.CharField(max_length=100)