from django.db import models

# Create your models here.
class ProceInstitucion(models.Model):
    procinstccod = models.CharField(db_column='ProcInstCCod', primary_key=True, max_length=2)  # Field name made lowercase.
    procinsttdescrip = models.CharField(db_column='ProcInstTDescrip', max_length=20, blank=True, null=True)  # Field name made lowercase.
    procinsttestad = models.CharField(db_column='ProcInstTestad', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oeimProceInstitucion'

    def __str__(self):
        return self.procinstccod
