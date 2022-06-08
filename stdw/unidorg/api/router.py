from django.urls import path
from rest_framework.routers import DefaultRouter
from unidorg.api.views import UnidOrgApiViewSet,ReporteView

router_unidorg=DefaultRouter()

router_unidorg.register(
    prefix='unidorg',basename='unidorg',viewset=UnidOrgApiViewSet
)
urlpatterns=[
    path('reporte/unidorg/<int:pk>/',ReporteView.as_view(),name="reporte_personas_pdf")
]