from rest_framework import serializers


from ...models import EducationLevelModel


class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevelModel
        fields = ["id", "label"]
