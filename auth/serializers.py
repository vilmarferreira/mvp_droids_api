from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True,max_length=100)
    password = serializers.CharField(required=True, write_only=True)
    password_confirm = serializers.CharField(required=True, write_only=True)

    def create(self, validated_data):
        """
        Args:
            validated_data:
        """
        del validated_data["password_confirm"]
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        """
        Args:
            attrs:
        """
        if User.objects.filter(username=attrs['username']).exists():
            raise ValidationError({'error': {
                'message': "Email already exists."
            }}
            )
        if attrs["password"] != attrs["password_confirm"]:
            raise ValidationError({'error': {'message': "The two password fields didn't match.",

                                             }}
                                  )
        return attrs
