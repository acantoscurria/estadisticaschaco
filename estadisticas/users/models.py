from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django import forms
from django.contrib.auth.models import User
# Create your models here.


class User(AbstractUser):
    password_entered = models.BooleanField(default=False)
    failed_login_attempts = models.IntegerField(default=0)

    REQUIRED_FIELDS = ["password"]

    def __str__(self):
        return f"Cue: {self.username}"

