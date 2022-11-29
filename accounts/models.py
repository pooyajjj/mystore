from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class User(AbstractUser):
    email = models.EmailField(max_length=225, unique=True)
    username = models.CharField(max_length=225, unique=True)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True)
    is_phone_active = models.BooleanField(default=False)
    is_email_active = models.BooleanField(default=False)

    object = UserManager()

    def __str__(self):
        return self.email