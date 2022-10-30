from django.db import models
from config.settings.base import AUTH_USER_MODEL

# Create your models here.
class School(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    region= models.CharField(max_length=20)
    oferta= models.CharField(max_length=150)
    cueanexo= models.CharField(max_length=9)


    def __str__(self) -> str:
        return f"{self.cueanexo} {self.region} {self.oferta}"