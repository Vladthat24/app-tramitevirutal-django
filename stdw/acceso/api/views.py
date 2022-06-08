from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from acceso.models import Acceso
from acceso.api.serializers import AccesoSerializers


class AccesoApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AccesoSerializers
    queryset = Acceso.objects.all().order_by('usrccod')

    filter_backends = [filters.SearchFilter]
    search_fields=['usrtlogin']