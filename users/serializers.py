from users.models import Product,BookOrders
from rest_framework import serializers

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__'

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=BookOrders
        fields = '__all__'