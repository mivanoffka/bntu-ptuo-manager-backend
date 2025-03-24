from rest_framework import serializers

from ...models import PhoneNumberType


class PhoneNumberTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneNumberType
        fields = ["id", "label"]
