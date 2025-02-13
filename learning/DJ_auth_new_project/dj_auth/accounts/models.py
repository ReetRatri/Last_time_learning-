from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=12 , unique=True)
    profile_image = models.ImageField(upload_to='profile' , blank=True , null=True)
    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = []


    objects = UserManager()