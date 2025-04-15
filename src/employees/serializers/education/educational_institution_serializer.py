from rest_framework import serializers


from ...models import EducationalInstitutionModel


class EducationalInstitutionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = EducationalInstitutionModel
        fields = ["id", "label", "graduated_at", "comment"]
