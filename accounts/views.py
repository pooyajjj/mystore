from django.shortcuts import render
from django.views import View
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics




class UserRegister(APIView):

    def post(self, request):
        ser_data = RegisterSerializer(data = request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

