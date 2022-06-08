from rest_framework.serializers import ModelSerializer

from tipodocpersonal.models import TipoDocPersonal



class TipoDocPersonalSerializer(ModelSerializer):

    class Meta:
        model = TipoDocPersonal
        fields=['tipdocperccod','tipdocpertdescrip','tipdocpernnumcaracter','tipdocpertestad']