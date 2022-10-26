from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SchoolUser(models.Model):
    cueanexo = models.CharField(max_length=9,primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password_ra = models.CharField(max_length=50,help_text="Password que utiliza en RA")
    user_ra = models.CharField(max_length=15,help_text="Password que utiliza en RA")

    def __str__(self) -> str:
        return f'{self.cueanexo} - {self.user.first_name} {self.user.last_name}'


class HelpDeskUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.IntegerField(primary_key=True)
    region = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f'{self.user.first_name} - {self.user.last_name}'