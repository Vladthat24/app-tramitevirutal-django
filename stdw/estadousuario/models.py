from django.db import models

# Create your models here.
class EstadoUsuario(models.Model):
    cestacode = models.CharField(db_column='cEstaCode', primary_key=True, max_length=1)  # Field name made lowercase.
    sestadesc = models.CharField(db_column='sEstaDesc', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estado_Usuario'

    def __str__(self):
        return self.sestadesc