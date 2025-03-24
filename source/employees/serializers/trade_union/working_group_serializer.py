from rest_framework import serializers

from ...models import WorkingGroup


class WorkingGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingGroup
        fields = ["id", "label"]
