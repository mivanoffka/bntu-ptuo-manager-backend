from rest_framework import serializers
from users.models import UserModel


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ("username", "password")

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data.get("username"),
            password=validated_data.get("password"),
        )

        return user
