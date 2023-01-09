from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['email']
