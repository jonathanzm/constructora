from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    cedula_identidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)


    def __str__(self):
		return " %s -%s -%s"% (self.direccion, self.cedula_identidad, self.telefono)