from rest_framework import serializers


from ...models import EmailModel


class EmailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = EmailModel
        fields = ["id", "value", "comment"]
