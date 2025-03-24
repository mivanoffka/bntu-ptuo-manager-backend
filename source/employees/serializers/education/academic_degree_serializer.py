from rest_framework import serializers

from ...models import AcademicDegree


class AcademicDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDegree
        fields = ["id", "label"]
