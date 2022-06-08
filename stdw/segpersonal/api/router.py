from rest_framework.routers import DefaultRouter
from segpersonal.api.views import SegPersonalApiViewSet

router_segpersonal=DefaultRouter()

router_segpersonal.register(
    prefix='segpersonal',basename='segpersonal',viewset=SegPersonalApiViewSet
)