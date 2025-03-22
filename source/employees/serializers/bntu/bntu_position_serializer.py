from rest_framework import serializers

from ...models import BntuPosition
from ..enumerated_serializer import EnumeratedSerializer


class BntuPositionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name.value

    def get_department(self, obj):
        return EnumeratedSerializer.from_field(obj, "department")

    class Meta:
        model = BntuPosition
        fields = [
            "name",
            "hired_at",
            "is_discharged",
            "discharged_at",
            "department",
            "is_discharged_voluntarily",
            "dischargement_comment",
        ]
