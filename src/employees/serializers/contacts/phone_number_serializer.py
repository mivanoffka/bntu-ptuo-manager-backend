from rest_framework import serializers

from references.models import PhoneNumberTypeModel
from ...models import PhoneNumberModel


class PhoneNumberSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    phone_number_type_id = serializers.PrimaryKeyRelatedField(
        queryset=PhoneNumberTypeModel.objects.all(), source="phone_number_type"
    )

    class Meta:
        model = PhoneNumberModel
        fields = ["id", "value", "phone_number_type_id", "comment"]
