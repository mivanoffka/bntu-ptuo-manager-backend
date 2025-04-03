from rest_framework import serializers


from ...models import PhoneNumberModel, PhoneNumberTypeModel


class PhoneNumberSerializer(serializers.ModelSerializer):
    phone_number_type_id = serializers.PrimaryKeyRelatedField(
        queryset=PhoneNumberTypeModel.objects.all(), source="phone_number_type"
    )

    class Meta:
        model = PhoneNumberModel
        fields = ["id", "value", "phone_number_type_id", "comment"]
