from rest_framework.routers import DefaultRouter
from condlaboral.api.views import CondLaboralApiViewSet


router_condlaboral=DefaultRouter()

router_condlaboral.register(
    prefix='condlaboral',basename='condlaboral',viewset=CondLaboralApiViewSet
)