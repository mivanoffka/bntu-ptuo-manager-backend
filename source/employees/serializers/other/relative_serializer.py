from rest_framework import serializers


from .relative_type_serializer import RelativeTypeSerializer

from ...models import RelativeModel


class RelativeSerializer(serializers.ModelSerializer):
    relative_type = RelativeTypeSerializer()

    class Meta:
        model = RelativeModel
        fields = ["id", "full_name", "birthdate", "comment", "relative_type"]
