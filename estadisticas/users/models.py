from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    password_ra = models.CharField(max_length=50,help_text="Password que utiliza en RA")
    user_ra = models.CharField(max_length=15,help_text="Usuario que utiliza en RA")