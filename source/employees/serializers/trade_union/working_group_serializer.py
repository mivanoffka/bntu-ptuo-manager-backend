from rest_framework import serializers

from .working_group_option_serializer import WorkingGroupOptionSerializer

from ...models import WorkingGroupModel


class WorkingGroupSerializer(serializers.ModelSerializer):
    working_group_option = serializers.SerializerMethodField()

    def get_working_group_option(self, obj: WorkingGroupModel):
        return WorkingGroupOptionSerializer(obj.working_group_option).data

    class Meta:
        model = WorkingGroupModel
        fields = ["id", "working_group_option"]
