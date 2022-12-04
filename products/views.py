from django.shortcuts import render
from rest_framework.views import APIView
from .models import Products, Order
from .serializers import ProductsSerializer, OrderSerializers
from rest_framework import status
from rest_framework.response import Response




class ProductsView(APIView):

    def get(self, request):
        products = Products.objects.all()
        ser_data = ProductsSerializer(instance=products, many = True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)



class OrderongView(APIView):

    def post(selff, request):
        pass


    def get(self, request):
        order = Order.objects.filter(id = request.user_id)
        ser_data = OrderSerializers(instance=order, many=True)
        