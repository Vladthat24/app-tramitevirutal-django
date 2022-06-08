from rest_framework.serializers import ModelSerializer

from institucion.models import Institucion
from proceinstitucion.api.serializers import ProceInstitucionSerializer

class InstitucionSerializers(ModelSerializer):

    proce_inst_data=ProceInstitucionSerializer(source='instcproced',read_only=True)

    class Meta:
        model=Institucion
        fields=['instccod','insttdescrip','insttsigla',
                'insttsigla','instctipo','instcproced',
                'perccod','insttestad','instncantdias',
                'instffechreg','instffechult','instopera','proce_inst_data']