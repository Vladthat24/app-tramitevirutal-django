from django.db import models

# Create your models here.
class Anexo(models.Model):
    idanexo = models.AutoField(primary_key=True)
    num_anexo = models.CharField(unique=True, max_length=45)
    direc_ip = models.CharField(unique=True, max_length=45, blank=True, null=True)
    marctelf = models.CharField(max_length=45, blank=True, null=True)
    model = models.CharField(max_length=45, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    fechinstal = models.DateTimeField()
    fechcambio = models.DateTimeField()
    observ = models.CharField(max_length=255, blank=True, null=True)
    fechreg = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'anexo'
