from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Fun(models.Model):
    Name=models.CharField(max_length=20,default="")
    Email=models.CharField(max_length=50,default="")
    Message=models.CharField(max_length=100,default="")





