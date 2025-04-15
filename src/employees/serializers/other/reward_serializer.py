from rest_framework import serializers


from ...models import RewardModel


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardModel
        fields = ["id", "label", "comment", "granted_at"]
