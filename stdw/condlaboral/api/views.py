from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from condlaboral.models import CondLaboral
from condlaboral.api.serializers import CondLaboralSerializers

class CondLaboralApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CondLaboralSerializers
    queryset = CondLaboral.objects.all()


