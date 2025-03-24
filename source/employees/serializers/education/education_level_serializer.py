from rest_framework import serializers

from ...models import EducationLevel


class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = ["id", "label"]
