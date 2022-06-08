from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from segpersonal.models import SegPersonal
from segpersonal.api.serializers import SegPersonalSerializers

class SegPersonalApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SegPersonalSerializers
    queryset = SegPersonal.objects.all().order_by('perccod')

    #filtros
    #filter_backends = [DjangoFilterBackend]
    #filter_fields=['percnumdoc']

    filter_backends = [filters.SearchFilter]
    search_fields = ['percnumdoc', 'pertnombre','pertapepat','pertapemat']