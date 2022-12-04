from rest_framework import serializers
from .models import Products, Order


class ProductsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Products
        fields = '__all__'


class OrderSerializers(serializers.Serializer):
    class Meta():
        model = Order
        fields = '__all__'