from django.db import models
from schools.models import School

# Create your models here.


class Student(models.Model):
    service_unit = models.ForeignKey(School,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=100)
    current_cueanexo = models.CharField(max_length=100)
    dni = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name} {self.last_name} - {self.dni}'