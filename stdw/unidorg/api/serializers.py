from rest_framework.serializers import ModelSerializer

from unidorg.models import UnidOrg
from institucion.api.serializers import InstitucionSerializers

class UnidOrgSerializer(ModelSerializer):

    inst_data=InstitucionSerializers(source='uorgccodinst',read_only=True)

    class Meta:
        model=UnidOrg
        fields=['uorgccod','uorgccodinst','uorgtdescrip','uorgtsigla',
                'uorgctipo','perccod','uorgccodpat','uorgccodsup',
                'uorgffechreg','uorgffechult','uorgtestad','uorgnord',
                'uorgflagst','uorgflagconst','inst_data']