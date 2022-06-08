from rest_framework.routers import DefaultRouter
from proceinstitucion.api.views import ProceInstitucionApiViewSet


router_proceinstitucion=DefaultRouter()

router_proceinstitucion.register(
    prefix='proceinstitucion',basename='proceinstitucion',viewset=ProceInstitucionApiViewSet
)