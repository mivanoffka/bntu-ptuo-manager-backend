from rest_framework import serializers


from ...models import GenderModel


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderModel
        fields = ["id", "label"]
