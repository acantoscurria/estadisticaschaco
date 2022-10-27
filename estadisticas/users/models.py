from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    cueanexo = models.CharField(max_length=9,unique=True)
    password_ra = models.CharField(max_length=50,help_text="Password que utiliza en RA")
    user_ra = models.CharField(max_length=15,help_text="Password que utiliza en RA")

    def __str__(self) -> str:
        return f'{self.cueanexo}'


# class HelpDeskUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     dni = models.IntegerField(primary_key=True)
#     region = models.CharField(max_length=10)

#     def __str__(self) -> str:
#         return f'{self.user.first_name} - {self.user.last_name}'