from rest_framework import serializers
from django.contrib.auth import authenticate

from services.constants import Errors


class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """

    username = serializers.CharField(
        label="Username",
        write_only=True,
    )

    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True,
    )

    def validate(self, attrs):
        request = self.context.get('request')

        if request.user.is_authenticated:
            raise serializers.ValidationError(msg, code='authorization')

        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        error_message = None

        # Try to authenticate the user using Django auth framework.
        user = authenticate(request=request,
                            username=username, password=password)

        if not user:
            error_message = Errors.INCORRECT_DATA

        # If we have error message, raise a ValidationError
        if error_message:
            raise serializers.ValidationError(error_message, code='authorization')

        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user

        return attrs
