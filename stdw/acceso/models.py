from django.db import models

# Create your models here.
class Acceso(models.Model):
    usrccod = models.CharField(db_column='UsrCCod', primary_key=True, max_length=6)  # Field name made lowercase.
    usrtlogin = models.CharField(db_column='UsrTLogin', max_length=18, blank=True, null=True)  # Field name made lowercase.
    usrtclave = models.CharField(db_column='UsrTClave', max_length=15, blank=True, null=True)  # Field name made lowercase.
    #usrcindides = models.CharField(db_column='Usrcindides', max_length=1, blank=True, null=True)  # Field name made lowercase.
    #usrcestacnx = models.CharField(db_column='Usrcestacnx', max_length=1, blank=True, null=True)  # Field name made lowercase.
    usrtmail = models.CharField(db_column='UsrTMail', max_length=30, blank=True, null=True)  # Field name made lowercase.
    usrtobser = models.CharField(db_column='UsrTObser', max_length=30, blank=True, null=True)  # Field name made lowercase.

    #usrccodper = models.CharField(db_column='UsrCCodper', max_length=6, blank=True, null=True)  # Field name made lowercase.
    usrccodper= models.ForeignKey('personal.Personal',models.DO_NOTHING,db_column='UsrCCodper',blank=True,null=True)

    #usrtindinue = models.CharField(db_column='UsrTIndinue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    #usrcindiadm = models.CharField(db_column='Usrcindiadm', max_length=1, blank=True, null=True)  # Field name made lowercase.
    #usrvdominio = models.CharField(db_column='UsrvDominio', max_length=80, blank=True, null=True)  # Field name made lowercase.
    usrncodrol = models.SmallIntegerField(db_column='UsrNCodRol', blank=True, null=True)  # Field name made lowercase.
    usrncodpermiso = models.SmallIntegerField(db_column='UsrNCodPermiso', blank=True, null=True)  # Field name made lowercase.
    usrvcamcla = models.CharField(db_column='Usrvcamcla', max_length=51, blank=True, null=True)  # Field name made lowercase.
    usrffechexp = models.DateTimeField(db_column='UsrFFechexp', blank=True, null=True)  # Field name made lowercase.
    usrtindiest = models.CharField(db_column='UsrTIndiest', max_length=1, blank=True, null=True)  # Field name made lowercase.
    usrtesttra = models.CharField(db_column='UsrTEstTra', max_length=1)  # Field name made lowercase.

    #usrtestad = models.CharField(db_column='UsrTEstad', max_length=1, blank=True, null=True)  # Field name made lowercase.
    usrtestad= models.ForeignKey('estadousuario.EstadoUsuario',models.DO_NOTHING,db_column='UsrTEstad',blank=True,null=True)

    usrcentd = models.CharField(db_column='UsrCEntd', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uniorganica = models.CharField(db_column='UniOrganica', max_length=1, blank=True, null=True)  # Field name made lowercase.
    usrteexp = models.CharField(db_column='UsrTEExp', max_length=1, blank=True, null=True)  # Field name made lowercase.
    usrubigeosede = models.CharField(db_column='UsrUbigeoSede', max_length=10, blank=True, null=True)  # Field name made lowercase.

    #usrnivel = models.CharField(db_column='UsrNivel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    usrnivel=models.ForeignKey('usuarionivel.UsuarioNivel', models.DO_NOTHING, db_column='UsrNivel', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SIUsuario'

    def __str__(self):
        return self.usrtlogin