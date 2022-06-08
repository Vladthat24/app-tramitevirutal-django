from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters

from anexo.models import Anexo
from anexo.api.serializers import AnexoSerializers


class AnexoApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AnexoSerializers
    queryset = Anexo.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ['num_anexo'
                     'direc_ip'
                     'marctelf'
                     'model'
                     'estado'
                     'observ']
