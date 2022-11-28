from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, blank = True, null = True)
    is_phone_active = models.BooleanField(default=False)
    is_email_active = models.BooleanField(default=True)



    def __str__(self):
        return self.email