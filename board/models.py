from django.db import models
from acc.models import User
# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=30)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    likey = models.IntegerField(default=0)
    up = models.ManyToManyField(User, blank=True)