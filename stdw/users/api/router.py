from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from users.api.views import UserApiViewSet, UserView

router_user = DefaultRouter()

# Una vez configurado el sistema de rutas de nuestra api
router_user.register(
    prefix='users', basename='users', viewset=UserApiViewSet
)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/', UserView.as_view())

]
