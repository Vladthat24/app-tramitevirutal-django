from rest_framework.serializers import ModelSerializer
from proceinstitucion.models import ProceInstitucion


class ProceInstitucionSerializer(ModelSerializer):
    class Meta:
        model=ProceInstitucion
        fields=['procinstccod','procinsttdescrip','procinsttestad']
