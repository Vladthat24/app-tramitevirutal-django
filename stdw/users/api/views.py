from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
# importaciones propias
from users.models import User
from users.api.serializers import UserSerializer


class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer  # como queremos que nos devuelvan los datos
    queryset = User.objects.all()  # Aque modelo queremos atacar

    # encrytando contraseña
    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    # Actualizar usuario y desifrar la contraseña
    def partial_update(self, request, *args, **kwargs):
        passsword = request.data['password']
        if passsword:
            request.data['password'] = make_password(passsword)
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)

#Clase para visualizar usuarios autenticados en el sistema
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        serializer=UserSerializer(request.user)
        return Response(serializer.data)