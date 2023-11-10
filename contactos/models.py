from django.db import models

# Create your models here.
class Contactos(models.Model):
    nombre = models.CharField(max_length=80)
    ap_pat = models.CharField(max_length=80)
    ap_mat = models.CharField(max_length=80)
    status = models.SmallIntegerField()