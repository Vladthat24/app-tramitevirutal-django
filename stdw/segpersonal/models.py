from django.db import models

# Create your models here.
class SegPersonal(models.Model):
    perccod = models.CharField(db_column='PerCCod', primary_key=True, max_length=6)  # Field name made lowercase.
    pertdescrip = models.CharField(db_column='PerTDescrip', max_length=60, blank=True,
                                   null=True)  # Field name made lowercase.
    pertnombre = models.CharField(db_column='PerTNombre', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    pertapepat = models.CharField(db_column='PerTApePat', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    pertapemat = models.CharField(db_column='PerTApemat', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    pertdireccion = models.CharField(db_column='PerTDireccion', max_length=100, blank=True,
                                     null=True)  # Field name made lowercase.
    pertnumtlf = models.CharField(db_column='PerTNumtlf', max_length=10, blank=True,
                                  null=True)  # Field name made lowercase.
    #perttipo = models.CharField(db_column='PerTTipo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    perttipo= models.ForeignKey('condlaboral.CondLaboral',models.DO_NOTHING,db_column='PerTTipo',blank=True,null=True)

    pertsexo = models.CharField(db_column='PerTSexo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pertestaciv = models.CharField(db_column='PerTEstaciv', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    perffechnac = models.DateTimeField(db_column='PerFFechnac', blank=True, null=True)  # Field name made lowercase.
    perffeching = models.DateTimeField(db_column='PerFFeching', blank=True, null=True)  # Field name made lowercase.
    #perccoddoc = models.CharField(db_column='PerCCoddoc', max_length=2, blank=True,null=True)  # Field name made lowercase.

    perccoddoc = models.ForeignKey('tipodocpersonal.TipoDocPersonal', models.DO_NOTHING, db_column='PerCCoddoc',
                                   blank=True, null=True)

    percnumdoc = models.CharField(db_column='PerCNumdoc', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
    percnumeruc = models.CharField(db_column='PerCNumeruc', max_length=11, blank=True,
                                   null=True)  # Field name made lowercase.
    perccodiplz = models.CharField(db_column='PerCCodiplz', max_length=6, blank=True,
                                   null=True)  # Field name made lowercase.
    perccodcar = models.CharField(db_column='PerCCodcar', max_length=6, blank=True,
                                  null=True)  # Field name made lowercase.
    #perccoduorg = models.CharField(db_column='PerCCoduorg', max_length=5, blank=True,null=True)  # Field name made lowercase.

    perccoduorg=models.ForeignKey('unidorg.UnidOrg',models.DO_NOTHING,db_column='PerCCoduorg',blank=True,null=True)

    perccodban = models.CharField(db_column='PerCCodban', max_length=2, blank=True,
                                  null=True)  # Field name made lowercase.
    percnumcta = models.CharField(db_column='PerCNumcta', max_length=12, blank=True,
                                  null=True)  # Field name made lowercase.
    pertlugproc = models.CharField(db_column='PerTLugProc', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    pertasig = models.CharField(db_column='PerTAsig', max_length=1, blank=True, null=True)  # Field name made lowercase.
    perffechreg = models.DateTimeField(db_column='PerFFechreg', blank=True, null=True)  # Field name made lowercase.
    perffechult = models.DateTimeField(db_column='PerFFechult', blank=True, null=True)  # Field name made lowercase.
    #pertestad = models.CharField(db_column='PerTestad', max_length=1, blank=True,null=True)  # Field name made lowercase.

    pertestad=models.ForeignKey('estadousuario.EstadoUsuario',models.DO_NOTHING,db_column='PerTestad',blank=True,null=True)

    pertflag = models.CharField(db_column='PerTflag', max_length=1, blank=True, null=True)  # Field name made lowercase.

    #pernord = models.SmallIntegerField(db_column='PerNOrd', blank=True, null=True)  # Field name made lowercase.
    pernord=models.ForeignKey('usuarionivel.UsuarioNivel',models.DO_NOTHING,db_column='PerNOrd',blank=True,null=True)

    peroper = models.CharField(db_column='PerOper', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pertcorreo = models.CharField(db_column='PerTCorreo', max_length=200, blank=True,
                                  null=True)  # Field name made lowercase.

    #TABLAS DE INFORMACION DEL PERSONAL LOCADOR DE SERVICIO
    pertdescriplocador = models.CharField(db_column='PerTDescripLocador', max_length=60, blank=True, null=True)  # Field name made lowercase.
    pertnombrelocador = models.CharField(db_column='PerTNombreLocador', max_length=60, blank=True, null=True)  # Field name made lowercase.
    pertapepatlocador = models.CharField(db_column='PerTApePatLocador', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pertapematlocador = models.CharField(db_column='PerTApematLocador', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Seguimiento_Personal'

    def __str__(self):
        return self.pertdescrip