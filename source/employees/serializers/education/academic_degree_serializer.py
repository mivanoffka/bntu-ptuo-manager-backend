from rest_framework import serializers

from ..abstract.deserializer import Deserializer

from ...models import AcademicDegree


class AcademicDegreeSerializer(Deserializer):
    class Meta(Deserializer.Meta):
        model = AcademicDegree
        fields = ["id", "label"]
