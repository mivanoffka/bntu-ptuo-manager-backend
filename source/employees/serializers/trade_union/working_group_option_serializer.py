from rest_framework import serializers

from ...models import WorkingGroupOptionModel


class WorkingGroupOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingGroupOptionModel
        fields = ["id", "label"]
