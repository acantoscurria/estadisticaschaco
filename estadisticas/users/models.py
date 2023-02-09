from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.


class User(AbstractUser):
    set_password = models.BooleanField(default=False)
    failed_login_attempts = models.IntegerField(default=0)

    REQUIRED_FIELDS = ["password"]

    def __str__(self):
        return f"Cue: {self.username}"