"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.debug import default_urlconf
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi, generators
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view as get_schema_views
from .views import file_downloading, Homepage, StatusCelery, SetCookie, GetCookie
from django.conf.urls.i18n import i18n_patterns
from graphene_django.views import GraphQLView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

class BothHttpAndHttpsSchemaGenerator(generators.OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["https", "http"]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
        validators=['ssv', 'flex'],
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # url="https://localhost"
    generator_class=BothHttpAndHttpsSchemaGenerator,
)


# v1_schema_view = get_schema_view(
#     openapi.Info(
#         title="Snippets API",
#         default_version="v1.1",
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="BSD License"),
#         validators=['ssv', 'flex'],

#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
#     # url="",
#     patterns=[
#         path('api/', include(v1_urlpatterns)),
#     ],
# )
urlpatterns = [
    path("", default_urlconf),
    path("api/graphql/", GraphQLView.as_view(graphiql=True)),
    # path('', Homepage),
    path('auth/', include('rest_framework.urls')),
    path('status/', StatusCelery),
    path('setcookie/', SetCookie),
    path('getcookie/', GetCookie),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    # path('docs/v1/', v1_schema_view.with_ui('swagger',
    #      cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    # path('api-auth/', include('rest_framework.urls'))
    path('api/', include('api.urls')),
    path('download/<uuid:sid>/', file_downloading),

    path('tinymce/', include('tinymce.urls')),

    path('openapi', get_schema_views(
        title="Your Project",
        description="API for all things …",
        version="1.0.0",
        permission_classes=(permissions.AllowAny,)

    ), name='openapi-schema'),

    path('api/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # For URL media / files
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += i18n_patterns(
#     path('admin/', admin.site.urls),
# )
