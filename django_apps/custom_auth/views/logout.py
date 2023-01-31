from django.contrib.auth import login, logout
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView, status

from django_apps.custom_auth.serializers import LoginSerializer
from services.constants import Errors, Success
from services.response_types import error_response, success_response


class LogoutView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def get(self, 
            request, 
            format=None):

        if request.user.is_authenticated:
            # if in system - logout
            logout(request)
            response = Response(success_response(description=Success.LOGOUT), 
                        status=status.HTTP_202_ACCEPTED)

        else:
            # if not in system drop the error
            response = Response(error_response(description=Errors.NOT_LOGGED), 
                        status=status.HTTP_400_BAD_REQUEST)

        return response

