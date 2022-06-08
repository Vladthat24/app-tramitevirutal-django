from rest_framework.routers import DefaultRouter
from acceso.api.views import AccesoApiViewSet

router_acceso=DefaultRouter()

router_acceso.register(
    prefix='acceso',basename='personal',viewset=AccesoApiViewSet
)