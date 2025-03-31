from rest_framework import serializers

from ...models import WorkingGroupOption


class WorkingGroupOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingGroupOption
        fields = ["id", "label"]
