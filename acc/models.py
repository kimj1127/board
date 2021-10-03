from django.db import models
from django.contrib.auth.models import AbstractUser #한군대만 가능
# Create your models here.

class User(AbstractUser):
    comment = models.TextField(blank=True)
    age = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    pic = models.ImageField(upload_to='acc/%y/%m', blank=True) #y = 년도, m = 월