from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django import forms
from django.contrib.auth.models import User
# Create your models here.


class User(AbstractUser):
    password_entered = models.BooleanField(
        default=False,
        verbose_name='Password cambiado',
        help_text='Indica si la escuela eligió su password. El campo no debe estar marcado si desea permitirle que pueda elegir una nueva contraseña.'
        )
    failed_login_attempts = models.IntegerField(
        default=0,
        verbose_name='Cantidad de intentos fallidos',
        help_text='Debe ser menor a 6 para que el usuario no sea bloqueado.'
        )

    REQUIRED_FIELDS = ["password"]

    def __str__(self):
        return f"Cue: {self.username}"

