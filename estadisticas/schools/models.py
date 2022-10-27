from django.db import models
from config.settings.base import AUTH_USER_MODEL
# Create your models here.


class ServiceUnit(models.Model):
    school_user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,help_text='ID de usuario escuela que es el CUEANEXO')
    region = models.CharField(max_length= 10)
    oferta = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.school_user.cueanexo} - {self.region} - {self.oferta}'
    