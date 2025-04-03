from django.db import models

from ..employee_model import EmployeeVersionModel
from .relative_type_model import RelativeTypeModel


class RelativeModel(models.Model):
    class Meta:
        db_table = "relatives"

    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        EmployeeVersionModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    full_name = models.CharField(max_length=128)

    birthdate = models.DateTimeField(null=True)

    comment = models.TextField(null=True, blank=True, max_length=512)

    relative_type = models.ForeignKey(
        RelativeTypeModel, on_delete=models.CASCADE, null=True, blank=True
    )
