from rest_framework import serializers

from ...models import EducationalInstitution


class EducationalInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalInstitution
        fields = ["id", "label"]
