from rest_framework import serializers

from ..abstract.deserializer import Deserializer

from ...models import EducationLevelModel


class EducationLevelSerializer(Deserializer):
    class Meta(Deserializer.Meta):
        model = EducationLevelModel
        fields = ["id", "label"]
