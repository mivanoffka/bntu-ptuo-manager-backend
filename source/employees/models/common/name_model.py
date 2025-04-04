from django.db import models

from ..employee_version_model import EmployeeVersionModel


class NameModel(models.Model):
    class Meta:
        db_table = "names"

    id = models.AutoField(primary_key=True)

    employee_version = models.ForeignKey(
        EmployeeVersionModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)
