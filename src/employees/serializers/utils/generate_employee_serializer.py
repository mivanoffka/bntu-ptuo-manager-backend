from rest_framework import serializers


class GenerateEmployeesSerializer(serializers.Serializer):
    count = serializers.IntegerField(default=1, min_value=1)
