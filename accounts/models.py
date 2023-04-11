from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *

# Create your models here.

class User(AbstractUser):
    
    is_doctor = models.BooleanField('Is doctor',default=False)
    is_patient = models.BooleanField('Is patient',default=False)

    address = models.CharField(max_length=150)

    profilepic = models.ImageField(upload_to="images")

    objects = UserManager

    