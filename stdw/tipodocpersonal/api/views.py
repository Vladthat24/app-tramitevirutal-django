from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from tipodocpersonal.models import TipoDocPersonal

from tipodocpersonal.api.serializers import TipoDocPersonalSerializer

class TipoDocPersonalApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TipoDocPersonalSerializer
    queryset = TipoDocPersonal.objects.all()

    #Filtros
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['tipdocpertdescrip']

