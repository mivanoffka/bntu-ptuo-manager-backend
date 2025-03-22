from dataclasses import field
from rest_framework import serializers

from ..utils import Enumerated


class EnumeratedSerializer(serializers.ModelSerializer):
    @staticmethod
    def from_field(obj, field_name: str):
        if obj.__getattribute__(field_name) is None:
            return None
        else:
            return EnumeratedSerializer(obj.__getattribute__(field_name)).data

    class Meta:
        model = Enumerated
        fields = ["id", "label"]
