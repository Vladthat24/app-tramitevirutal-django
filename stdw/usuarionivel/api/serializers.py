from rest_framework.serializers import ModelSerializer

from usuarionivel.models import UsuarioNivel

class UsuarioNivelSerializers(ModelSerializer):

    class Meta:
        model=UsuarioNivel
        fields=['cnivelcode','sniveldesc']