from rest_framework import serializers
from ...models import EnumeratedModel


class EnumeratedSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source="id", read_only=True)

    class Meta:
        model = EnumeratedModel
        fields = ["label", "value"]
