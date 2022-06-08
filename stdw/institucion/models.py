from django.db import models

# Create your models here.
class Institucion(models.Model):
    instccod = models.CharField(db_column='InstCCod', primary_key=True, max_length=8)  # Field name made lowercase.
    insttdescrip = models.CharField(db_column='InstTDescrip', max_length=100, blank=True, null=True)  # Field name made lowercase.
    insttsigla = models.CharField(db_column='InstTSigla', max_length=16, blank=True, null=True)  # Field name made lowercase.
    instctipo = models.CharField(db_column='InstCTipo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    instcproced = models.ForeignKey('proceinstitucion.ProceInstitucion', models.DO_NOTHING, db_column='InstCProced', blank=True, null=True)  # Field name made lowercase.
    perccod = models.CharField(db_column='PerCCod', max_length=6, blank=True, null=True)  # Field name made lowercase.
    insttestad = models.CharField(db_column='InstTEstad', max_length=1, blank=True, null=True)  # Field name made lowercase.
    instncantdias = models.SmallIntegerField(db_column='InstNcantdias', blank=True, null=True)  # Field name made lowercase.
    instffechreg = models.DateTimeField(db_column='InstFFechreg', blank=True, null=True)  # Field name made lowercase.
    instffechult = models.DateTimeField(db_column='InstFFechult', blank=True, null=True)  # Field name made lowercase.
    instopera = models.CharField(db_column='InstOpera', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oeimInstitucion'

    def __str__(self):
        return self.insttdescrip