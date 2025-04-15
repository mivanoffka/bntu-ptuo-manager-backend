from rest_framework import serializers


from ...models import NameModel


class NameSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = NameModel
        fields = ["id", "first_name", "middle_name", "last_name", "created_at"]
