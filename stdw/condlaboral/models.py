from django.db import models

# Create your models here.

class CondLaboral(models.Model):
    tipperccod = models.CharField(db_column='TipPerCCod', primary_key=True, max_length=1)  # Field name made lowercase.
    tippertdescrip = models.CharField(db_column='TipPerTDescrip', max_length=50)  # Field name made lowercase.
    tippertestad = models.CharField(db_column='TipPerTEstad', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oeimTipPersonal'

    def __str__(self):
        return self.tippertdescrip