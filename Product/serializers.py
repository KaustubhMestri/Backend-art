from Product.models import AddToCart
from rest_framework import serializers

class AddtoCartSerializers(serializers.ModelSerializer):
    class Meta:
        model= AddToCart
        fields = '__all__'