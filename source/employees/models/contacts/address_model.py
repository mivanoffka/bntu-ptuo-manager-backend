from django.db import models

from ..employee_version_model import EmployeeVersionModel


class AddressModel(models.Model):
    class Meta:
        db_table = "addresses"

    id = models.AutoField(primary_key=True)

    employee_version = models.ForeignKey(
        EmployeeVersionModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    value = models.CharField(max_length=256)

    comment = models.TextField(null=True, blank=True, max_length=512)
