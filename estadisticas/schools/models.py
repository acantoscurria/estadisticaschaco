from django.db import models
from users.models import SchoolUser
# Create your models here.


class ServiceUnit(models.Model):
    school_user = models.ForeignKey(SchoolUser,on_delete=models.CASCADE,help_text='ID de usuario escuela que es el CUEANEXO')
    region = models.CharField(max_length= 10)
    oferta = models.CharField(max_length=50)