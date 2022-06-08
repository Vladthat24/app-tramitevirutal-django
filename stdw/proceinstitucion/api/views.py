from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from proceinstitucion.models import ProceInstitucion
from proceinstitucion.api.serializers import ProceInstitucionSerializer


class ProceInstitucionApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProceInstitucionSerializer
    queryset = ProceInstitucion.objects.all()