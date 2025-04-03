from rest_framework import serializers

from ...models import WorkingGroupModel, WorkingGroupOptionModel


class WorkingGroupSerializer(serializers.ModelSerializer):
    working_group_option_id = serializers.PrimaryKeyRelatedField(
        queryset=WorkingGroupOptionModel.objects.all(),
        source="working_group_option",
    )

    class Meta:
        model = WorkingGroupModel
        fields = ["id", "working_group_option_id"]
