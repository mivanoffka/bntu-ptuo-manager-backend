from rest_framework import serializers

from ...models import PhoneNumberTypeModel


class PhoneNumberTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneNumberTypeModel
        fields = ["id", "label"]
