from django.db import models

# Create your models here.
class UsuarioNivel(models.Model):
    cnivelcode = models.IntegerField(db_column='cNivelCode', primary_key=True)  # Field name made lowercase.
    sniveldesc = models.CharField(db_column='sNivelDesc', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nivel'

    def __str__(self):
        return self.sniveldesc