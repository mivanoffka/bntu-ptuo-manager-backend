from rest_framework import serializers

from ..utils.history import History
from ..models import Employee, Name


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ["first_name", "middle_name", "last_name"]


class EmployeeSerializer(serializers.ModelSerializer):
    names = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ["id", "names", "birthdate", "birthplace"]

    def get_names(self, obj):
        return History[Name].from_timestamped(obj.names, NameSerializer)


# class EmployeeDeserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ["id", "names"]  # Предположим, names — это поле для записи
#         read_only_fields = ["id"]

#     def create(self, validated_data):
#         names_data = validated_data.pop("names")
#         employee = Employee.objects.create(**validated_data)
#         # Логика для создания связанных объектов Name
#         return employee
