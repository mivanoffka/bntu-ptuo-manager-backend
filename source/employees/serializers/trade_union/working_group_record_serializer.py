from rest_framework import serializers

from ...models import WorkingGroupRecordModel, WorkingGroupOptionModel


class WorkingGroupRecordSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    working_group_option_id = serializers.PrimaryKeyRelatedField(
        queryset=WorkingGroupOptionModel.objects.all(),
        source="working_group_option",
    )

    def create(self, validated_data):
        validated_data.pop("authentic_label")

        working_group_option_id = validated_data["working_group_option_id"]
        authentic_label = WorkingGroupOptionModel.objects.get(
            id=working_group_option_id
        ).label

        instance = WorkingGroupRecordModel.objects.create(
            **validated_data, authentic_label=authentic_label
        )

        return instance

    class Meta:
        model = WorkingGroupRecordModel
        fields = ["id", "working_group_option_id", "created_at", "authentic_label"]
