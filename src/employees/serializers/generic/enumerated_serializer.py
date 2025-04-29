from rest_framework import serializers


class EnumeratedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "label"]
        abstract = True
