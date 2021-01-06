from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=150, blank=True)
    address = models.TextField(max_length=500, blank=True)
    # 1은 관리자, 2는 구매자, 3은 판매자
    user_type = models.IntegerField(default=2, blank=True)