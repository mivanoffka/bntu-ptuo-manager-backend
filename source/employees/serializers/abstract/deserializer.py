from django.forms import ValidationError
from rest_framework import serializers
from django.db import transaction


class Deserializer(serializers.ModelSerializer):
    def _validate_id(self, validated_data, is_update=False):
        id_value = validated_data.get("id")

        if is_update:
            if id_value is None or id_value < 0:
                raise ValidationError(
                    {
                        "id": "Update operation requires a positive ID for an existing object."
                    }
                )
        else:
            if id_value is not None and id_value > 0:
                raise ValidationError(
                    {
                        "id": "Create operation does not allow a positive ID; use update instead."
                    }
                )
            if id_value is not None and id_value < 0:
                validated_data.pop("id")

        return validated_data

    def create(self, validated_data):
        validated_data = self._validate_id(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = self._validate_id(validated_data)
        return super().update(instance, validated_data)

    class Meta:
        abstract = True
