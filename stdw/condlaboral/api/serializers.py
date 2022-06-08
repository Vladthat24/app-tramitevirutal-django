from rest_framework.serializers import ModelSerializer

from condlaboral.models import CondLaboral

class CondLaboralSerializers(ModelSerializer):

    class Meta:
        model= CondLaboral
        fields=['tipperccod','tippertdescrip','tippertestad']