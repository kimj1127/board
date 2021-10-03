from django.db import models
from acc.models import User
# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=30)
    writer_pic = models.ImageField()
    comment = models.TextField(blank=True)
    voter = models.ManyToManyField(User, blank=True)

    def summary(self):
        if len(self.comment) > 30:
            return self.comment[:30] + "..."
        return self.comment

class Choice(models.Model):
    title = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="vote", blank=True)
    choicer = models.ManyToManyField(User, blank=True)