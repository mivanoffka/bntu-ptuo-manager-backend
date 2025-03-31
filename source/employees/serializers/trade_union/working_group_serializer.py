from rest_framework import serializers

from .working_group_option_serializer import WorkingGroupOptionSerializer

from ...models import WorkingGroup


class WorkingGroupSerializer(serializers.ModelSerializer):
    working_group_option = serializers.SerializerMethodField()

    def get_working_group_option(self, obj: WorkingGroup):
        return WorkingGroupOptionSerializer(obj.working_group_option).data

    class Meta:
        model = WorkingGroup
        fields = ["id", "working_group_option"]
