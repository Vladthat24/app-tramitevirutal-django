from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from usuarionivel.models import UsuarioNivel

class UsuarioNivelApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UsuarioNivel
    queryset = UsuarioNivel.objects.all()
