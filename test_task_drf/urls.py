from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

from django_apps.posts.apps import APP_NAME as POST_APP_NAME
from django_apps.custom_auth.apps import APP_NAME as AUTH_APP_NAME

from services.django_apps.posts.urls.docs import docs_view
# from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('', lambda request: redirect('docs'), name='main_url'),
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),                              # for showing login button in browsable api

    path('api/', include(f'{POST_APP_NAME}.urls')),
    path('api/auth/', include(f'{AUTH_APP_NAME}.urls')),

    path('docs/', docs_view.with_ui('swagger', cache_timeout=0), name='docs')
    # path('docs', include_docs_urls(title='test'), name='docs')
]

