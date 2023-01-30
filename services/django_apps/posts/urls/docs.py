from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import os


docs_view = get_schema_view(
   openapi.Info(
      title=os.environ.get('PROJECT_NAME'),
      default_version=os.environ.get('PROJECT_VERSION'),
      description=os.environ.get('PROJECT_DESCRIPTION'),
      contact=openapi.Contact(email="dummy_mail@test.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
