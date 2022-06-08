from rest_framework.routers import DefaultRouter

#importando nuestro api view
from tipodocpersonal.api.views import TipoDocPersonalApiViewSet

router_tipodocpersonal=DefaultRouter()

router_tipodocpersonal.register(
    prefix='tipodocpersonal',basename='products',viewset=TipoDocPersonalApiViewSet
)