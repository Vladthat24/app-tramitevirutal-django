from django.db import models


# Create your models here.
class TipoDocPersonal(models.Model):
    tipdocperccod = models.CharField(db_column='TIpDocPerCCod', primary_key=True, max_length=2)  # Field name made lowercase.
    tipdocpertdescrip = models.CharField(db_column='TIpDocPerTDescrip', max_length=50)  # Field name made lowercase.
    tipdocpernnumcaracter = models.IntegerField(db_column='TIpDocPerNNumCaracter', blank=True, null=True)  # Field name made lowercase.
    tipdocpertestad = models.CharField(db_column='TIpDocPertEstad', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oeimTipDocPersonal'

    def __str__(self):
        return self.tipdocpertdescrip
