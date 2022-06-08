from rest_framework.serializers import ModelSerializer

from estadousuario.models import EstadoUsuario

class EstadoUsuarioSerializers(ModelSerializer):

    class Meta:
        model=EstadoUsuario
        fields=['cestacode','sestadesc']