from rest_framework.routers import DefaultRouter
from estadousuario.api.views import EstadoUsuarioApiViewSet

router_estadousuario=DefaultRouter()

router_estadousuario.register(
    prefix='estadousuario',basename='estadousuario',viewset=EstadoUsuarioApiViewSet
)