from rest_framework import serializers

from ..enumerated_serializer import EnumeratedSerializer

from ...models import PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):
    phone_number_type = serializers.SerializerMethodField()

    def get_phone_number_type(self, obj):
        return EnumeratedSerializer.from_field(obj, "phone_number_type")

    class Meta:
        model = PhoneNumber
        fields = ["value", "phone_number_type", "comment"]
