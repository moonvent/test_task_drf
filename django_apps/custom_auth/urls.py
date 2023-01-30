from django.urls import path
from django_apps.custom_auth.views.login import LoginView
from django_apps.custom_auth.views.logout import LogoutView


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]

