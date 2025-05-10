from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import UserModel
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import UserSerializer


class SignInRequestSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs["username"],
            password=attrs["password"],
        )

        if isinstance(user, UserModel):
            if not user.is_verified:
                raise serializers.ValidationError("User is not verified")
            return user

        raise serializers.ValidationError("Invalid username or password")


class SignInResponseSerializer(serializers.Serializer):
    user = serializers.SerializerMethodField(read_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        user = obj
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def get_user(self, obj):
        user = obj
        return UserSerializer(user).data
