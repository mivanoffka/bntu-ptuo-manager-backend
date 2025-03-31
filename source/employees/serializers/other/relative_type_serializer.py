from rest_framework import serializers

from ...models import RelativeTypeModel


class RelativeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelativeTypeModel
        fields = ["id", "label"]
