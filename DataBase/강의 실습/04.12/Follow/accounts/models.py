from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    #symmetrical이 True면 내가 상대방을 follow하면 상대방도 나를 follow하게 됨
    followings=models.ManyToManyField('self', symmetrical=False, related_name='followers')