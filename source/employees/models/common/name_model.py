from django.db import models

from ..employee_model import EmployeeModel
from ..abstract import TimestampedModel


class NameModel(TimestampedModel):
    class Meta(TimestampedModel.Meta):
        db_table = "names"

    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        EmployeeModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)

    createdAt = models.DateTimeField(auto_now_add=True)
