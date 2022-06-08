from rest_framework.serializers import ModelSerializer

from acceso.models import Acceso
from personal.api.serializers import PersonalSerializers
from estadousuario.api.serializers import EstadoUsuarioSerializers
from usuarionivel.api.serializers import UsuarioNivelSerializers

class AccesoSerializers(ModelSerializer):
    data_personal = PersonalSerializers(source='usrccodper', read_only=True)
    data_estadousuario = EstadoUsuarioSerializers(source='usrtestad', read_only=True)
    data_usuarionivel = UsuarioNivelSerializers(source='pernord', read_only=True)


    class Meta:
        model = Acceso

        # Informacion que retorna en la consulta docs del api
        fields = ['usrccod',
                  'usrtlogin',
                  'usrtclave',
                  'usrcindides',
                  'usrcestacnx',
                  'usrtmail',
                  'usrtobser',
                  'usrccodper',
                  'usrtindinue',
                  'usrcindiadm',
                  'usrvdominio',
                  'usrncodrol',
                  'usrncodpermiso',
                  'usrvcamcla',
                  'usrffechexp',
                  'usrtindiest',
                  'usrtesttra',
                  'usrtestad',
                  'usrcentd',
                  'uniorganica',
                  'usrteexp',
                  'usrubigeosede',
                  'usrnivel',
                  'data_personal', 'data_estadousuario','data_usuarionivel']
