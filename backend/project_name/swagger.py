from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication


schema_view = get_schema_view(
   openapi.Info(
      title="STM API",
      default_version= f"v{settings.VERSION}",
      description="The STM API is a RESTful API that provides web services for the STM project.",
      terms_of_service="https://stm.fiust.ir",
      contact=openapi.Contact(email="amirali.dst.lll@gmail.com"),
      license=openapi.License(name="BSD License"),
      x={
         'security': [{'Bearer': []}],
      },
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=(JWTAuthentication,),
)