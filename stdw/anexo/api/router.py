from rest_framework.routers import DefaultRouter
from anexo.api.views import AnexoApiViewSet


router_anexo=DefaultRouter()

router_anexo.register(
    prefix='anexo',basename='anexo',viewset=AnexoApiViewSet
)