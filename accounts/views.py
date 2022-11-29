from django.shortcuts import render
from django.views import View
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
# class UserRegister(APIView):

#     def post(self, request):
#         ser_data = RegisterSerializer(data = request.POST)
#         if ser_data.is_valid():
#             ser_data.create(ser_data.validated_data)
#             return Response(ser_data.data, status=status.HTTP_201_CREATED)
        
#         return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegister(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })