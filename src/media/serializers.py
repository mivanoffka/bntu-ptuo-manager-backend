from rest_framework import serializers
from .models import ImageModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ["id", "file", "uploaded_at"]
        read_only_fields = ["uploaded_at", "id"]
