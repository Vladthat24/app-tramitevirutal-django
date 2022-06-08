from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from personal.models import Personal
from personal.api.serializers import PersonalSerializers

class PersonalApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PersonalSerializers
    queryset = Personal.objects.all().order_by('perccod')

    #filtros
    #filter_backends = [DjangoFilterBackend]
    #filter_fields=['percnumdoc']

    filter_backends = [filters.SearchFilter]
    search_fields = ['percnumdoc', 'pertnombre','pertapepat','pertapemat']

