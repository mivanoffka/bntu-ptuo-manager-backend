from rest_framework import serializers

from references.models import RelativeTypeModel
from ...models import RelativeModel


class RelativeSerializer(serializers.ModelSerializer):
    relative_type_id = serializers.PrimaryKeyRelatedField(
        queryset=RelativeTypeModel.objects.all(), source="relative_type"
    )

    class Meta:
        model = RelativeModel
        fields = ["id", "full_name", "birthdate", "comment", "relative_type_id"]
