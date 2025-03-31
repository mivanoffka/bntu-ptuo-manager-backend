from rest_framework import serializers
from ...models import NameModel


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameModel
        fields = ["first_name", "middle_name", "last_name"]
