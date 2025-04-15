from rest_framework import serializers


from ...models import AddressModel


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = AddressModel
        fields = ["id", "value", "comment"]
