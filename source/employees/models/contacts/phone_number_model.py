from django.db import models

from ..employee_model import EmployeeModel
from .phone_number_type_model import PhoneNumberTypeModel


class PhoneNumberModel(models.Model):
    class Meta:
        db_table = "phone_numbers"

    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        EmployeeModel,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )

    value = models.CharField(max_length=255)

    phone_number_type = models.ForeignKey(
        PhoneNumberTypeModel, on_delete=models.CASCADE, null=True, blank=True
    )

    comment = models.TextField(null=True, blank=True, max_length=512)
