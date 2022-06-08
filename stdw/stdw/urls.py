"""
stdw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#importar nuestros sistemas de rutas de nuestros aplicativos
from users.api.router import router_user
from proceinstitucion.api.router import router_proceinstitucion
from institucion.api.router import router_institucion
from unidorg.api.router import router_unidorg
from tipodocpersonal.api.router import router_tipodocpersonal
from estadousuario.api.router import router_estadousuario
from usuarionivel.api.router import router_usuarionivel
from personal.api.router import router_personal
from acceso.api.router import router_acceso
from segpersonal.api.router import router_segpersonal
from condlaboral.api.router import router_condlaboral
from anexo.api.router import router_anexo

schema_view = get_schema_view(
    openapi.Info(
        title="stdw - ApiDoc",
        default_version='v1',
        description="Documentación de la api stdw",
        terms_of_service="https://www.dirislimasur.gob.pe/",
        contact=openapi.Contact(email="desarrollo@dirislimasur.gob.pe"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #Sistema de Rutas
    path('api/', include('users.api.router')),
path('api/', include('unidorg.api.router')),
    path('api/',include(router_user.urls)),
    path('api/',include(router_proceinstitucion.urls)),
    path('api/',include(router_institucion.urls)),
    path('api/',include(router_unidorg.urls)),
    path('api/',include(router_tipodocpersonal.urls)),
    path('api/',include(router_estadousuario.urls)),
    path('api/',include(router_usuarionivel.urls)),
    path('api/',include(router_personal.urls)),
    path('api/',include(router_acceso.urls)),
    path('api/',include(router_segpersonal.urls)),
    path('api/',include(router_condlaboral.urls)),
    path('api/',include(router_anexo.urls))
]
