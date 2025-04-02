from rest_framework import serializers


from ...models import EmailModel


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailModel
        fields = ["id", "value", "comment"]
