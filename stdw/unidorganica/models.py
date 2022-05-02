from django.db import models

# Create your models here.
class UnidOrganica(models.Model):
    uorgccod = models.CharField(db_column='UorgCCod', primary_key=True, max_length=5)  # Field name made lowercase.
    uorgccodinst = models.ForeignKey(Oeiminstitucion, models.DO_NOTHING, db_column='UorgCCodInst', blank=True, null=True)  # Field name made lowercase.
    uorgtdescrip = models.CharField(db_column='UorgTDescrip', max_length=100, blank=True, null=True)  # Field name made lowercase.
    uorgtsigla = models.CharField(db_column='UorgTSigla', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uorgctipo = models.CharField(db_column='UorgCTipo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    perccod = models.CharField(db_column='PerCCod', max_length=6, blank=True, null=True)  # Field name made lowercase.
    uorgccodpat = models.CharField(db_column='UorgCCodPat', max_length=5, blank=True, null=True)  # Field name made lowercase.
    uorgccodsup = models.CharField(db_column='UorgCCodSup', max_length=5, blank=True, null=True)  # Field name made lowercase.
    uorgffechreg = models.DateTimeField(db_column='UorgFFechreg', blank=True, null=True)  # Field name made lowercase.
    uorgffechult = models.DateTimeField(db_column='UorgFFechult', blank=True, null=True)  # Field name made lowercase.
    uorgtestad = models.CharField(db_column='UorgTEstad', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uorgnord = models.SmallIntegerField(db_column='UOrgNOrd', blank=True, null=True)  # Field name made lowercase.
    uorgflagst = models.CharField(db_column='UorgFlagST', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uorgflagconst = models.CharField(db_column='UorgFlagConST', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oeimUnidOrg'