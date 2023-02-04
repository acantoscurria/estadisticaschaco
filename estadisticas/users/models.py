from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.


class User(AbstractUser):
    random_pass = models.CharField(max_length=50,help_text="Password que utiliza en RA")
    failed_login_attempts = models.IntegerField(default=0)

    REQUIRED_FIELDS = ["password"]