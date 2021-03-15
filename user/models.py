from django.db import models
from django.contrib.auth.models import User


class Advisor(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=200)

class BookingTime(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    advisor = models.OneToOneField(Advisor, on_delete=models.CASCADE)