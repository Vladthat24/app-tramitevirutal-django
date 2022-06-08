from rest_framework.serializers import ModelSerializer

from personal.models import Personal
from tipodocpersonal.api.serializers import TipoDocPersonalSerializer
from unidorg.api.serializers import UnidOrgSerializer
from estadousuario.api.serializers import EstadoUsuarioSerializers
from usuarionivel.api.serializers import UsuarioNivelSerializers
from condlaboral.api.serializers import CondLaboralSerializers

class PersonalSerializers(ModelSerializer):

    data_tipodoc=TipoDocPersonalSerializer(source='perccoddoc',read_only=True)
    data_unidorg=UnidOrgSerializer(source='perccoduorg',read_only=True)
    data_estadousuario=EstadoUsuarioSerializers(source='pertestad',read_only=True)
    data_usuarionivel=UsuarioNivelSerializers(source='pernord',read_only=True)
    data_condlaboral=CondLaboralSerializers(source='perttipo',read_only=True)


    class Meta:
        model = Personal

        #Informacion que retornara en la consulta docs del api
        fields = ['perccod',
                  'pertdescrip',
                  'pertnombre',
                  'pertapepat',
                  'pertapemat',
                  'pertdireccion',
                  'pertnumtlf',
                  'perttipo',
                  'pertsexo',
                  'pertestaciv',
                  'perffechnac',
                  'perffeching',
                  'perccoddoc',
                  'percnumdoc',
                  'percnumeruc',
                  'perccodiplz',
                  'perccodcar',
                  'perccoduorg',
                  'perccodban',
                  'percnumcta',
                  'pertlugproc',
                  'pertasig',
                  'perffechreg',
                  'perffechult',
                  'pertestad',
                  'pertflag',
                  'pernord',
                  'peroper',
                  'pertcorreo',
                  'data_tipodoc',
                  'data_unidorg',
                  'data_estadousuario',
                  'data_usuarionivel',
                  'data_condlaboral']
