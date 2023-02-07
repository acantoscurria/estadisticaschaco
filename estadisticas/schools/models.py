from django.db import models
from users.models import User

# Create your models here.

class Offer(models.Model):
    cue = models.ForeignKey(User,on_delete=models.DO_NOTHING,help_text="Cue asociado a la oferta",
                            db_column='cue',to_field="username")
    cueanexo = models.CharField(max_length=250,null=True,blank=True)
    anexo = models.CharField(max_length=250,null=True,blank=True)
    oferta = models.CharField(max_length=250,null=True,blank=True)
    nom_est = models.CharField(max_length=250,null=True,blank=True)


class DechDesempenio(models.Model):
    id = models.AutoField(primary_key=True)
    cueanexo = models.TextField(max_length=100)
    desempenio = models.BigIntegerField(default=0)
    punto = models.BigIntegerField(default=0)
    promedio = models.BigIntegerField(default=0)

    class Meta:
        managed= False