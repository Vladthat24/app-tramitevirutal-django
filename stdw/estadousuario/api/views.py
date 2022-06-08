from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from estadousuario.models import EstadoUsuario
from estadousuario.api.serializers import EstadoUsuarioSerializers


class EstadoUsuarioApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = EstadoUsuarioSerializers
    queryset = EstadoUsuario.objects.all()

