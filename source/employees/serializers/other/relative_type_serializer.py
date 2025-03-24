from rest_framework import serializers

from ...models import RelativeType


class RelativeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelativeType
        fields = ["id", "label"]
