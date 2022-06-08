from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend
from institucion.models import Institucion
from institucion.api.serializers import InstitucionSerializers


class InstitucionApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = InstitucionSerializers
    queryset = Institucion.objects.all().order_by('instccod')

    #filtros
    #filter_backends = [DjangoFilterBackend]
    #filter_fields=['insttdescrip']