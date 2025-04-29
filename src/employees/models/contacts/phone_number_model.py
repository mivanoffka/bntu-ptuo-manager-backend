from django.db import models

from ..employee_version_model import EmployeeVersionModel
from references.models import PhoneNumberTypeModel


class PhoneNumberModel(models.Model):
    class Meta:
        db_table = "phone_numbers"

    id = models.AutoField(primary_key=True)

    employee_version = models.ForeignKey(
        EmployeeVersionModel,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )

    value = models.CharField(max_length=255)

    phone_number_type = models.ForeignKey(
        PhoneNumberTypeModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name=Meta.db_table,
    )

    comment = models.TextField(null=True, blank=True, max_length=512)
