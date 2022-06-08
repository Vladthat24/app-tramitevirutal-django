from rest_framework.routers import DefaultRouter
from usuarionivel.api.views import UsuarioNivelApiViewSet


router_usuarionivel=DefaultRouter()

router_usuarionivel.register(
    prefix='usuarionivel',basename='usuarionivel',viewset=UsuarioNivelApiViewSet
)