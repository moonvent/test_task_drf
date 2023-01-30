from django.contrib import admin
from django.urls import include, path

from django_apps.posts.apps import APP_NAME as POST_APP_NAME

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(f'{POST_APP_NAME}.urls')),
]

