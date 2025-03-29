from rest_framework import serializers
from ..utils.enumeration import Enumerated


class EnumeratedSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Enumerated
        fields = ['label', 'value']
