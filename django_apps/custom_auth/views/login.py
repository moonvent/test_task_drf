from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView, status

from django_apps.custom_auth.serializers import LoginSerializer
from services.constants import Success
from services.response_types import success_response


class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, 
             request, 
             format=None):

        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        login(request, user)

        return Response(success_response(description=Success.LOGGED), 
                        status=status.HTTP_202_ACCEPTED)
