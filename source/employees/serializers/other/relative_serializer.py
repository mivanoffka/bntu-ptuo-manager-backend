from rest_framework import serializers

from .relative_type_serializer import RelativeTypeSerializer

from ...models import RelativeModel


class RelativeSerializer(serializers.ModelSerializer):
    relative_type = serializers.SerializerMethodField()

    def get_relative_type(self, obj):
        return RelativeTypeSerializer(obj.relative_type).data

    class Meta:
        model = RelativeModel
        fields = ["id", "full_name", "birthdate", "comment", "relative_type"]
