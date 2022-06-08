from rest_framework.routers import DefaultRouter
from institucion.api.views import InstitucionApiViewSet

router_institucion=DefaultRouter()

router_institucion.register(
    prefix='institucion',basename='institucion',viewset=InstitucionApiViewSet
)