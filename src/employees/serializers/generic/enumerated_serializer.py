from rest_framework import serializers

from ...models import EnumeratedModel


class EnumeratedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField()
