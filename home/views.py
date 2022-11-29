from django.shortcuts import render
from rest_framework.views import APIView
from accounts.models import User
from .serializers import UserDetailSerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class Home(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        user = User.objects.all()
        ser_data = UserDetailSerializers(instance=user, many = True)
        return Response(data=ser_data.data)
