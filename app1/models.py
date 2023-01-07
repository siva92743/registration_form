from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Login(AbstractUser):
    is_user = models.BooleanField(default=False)
    name = models.CharField(max_length=25, null=True)
    contact_no = models.IntegerField(null=True)
    photo = models.ImageField(upload_to='profile', null=True)

