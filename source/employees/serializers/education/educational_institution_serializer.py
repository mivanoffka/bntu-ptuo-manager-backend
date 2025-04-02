from rest_framework import serializers

from ..abstract.deserializer import Deserializer

from ...models import EducationalInstitutionModel


class EducationalInstitutionSerializer(Deserializer):
    class Meta(Deserializer.Meta):
        model = EducationalInstitutionModel
        fields = ["id", "label", "graduated_at", "comment"]
