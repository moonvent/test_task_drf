from django.urls import path
from django_apps.custom_auth.views.login import LoginView
from django_apps.custom_auth.views.logout import LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(), name='custom_login'),
    path('logout/', LogoutView.as_view(), name='custom_logout'),
]

