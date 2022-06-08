from rest_framework.routers import DefaultRouter
from personal.api.views import PersonalApiViewSet

router_personal=DefaultRouter()

router_personal.register(
    prefix='personal',basename='personal',viewset=PersonalApiViewSet
)