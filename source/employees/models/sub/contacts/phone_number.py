from django.db import models

from ...employee import Employee
from .phone_number_type import PhoneNumberType


class PhoneNumber(models.Model):
    id = models.AutoField(primary_key=True)

    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="phone_numbers"
    )

    type = models.IntegerField(
        choices=PhoneNumberType.choices,
        default=None,
        null=True,
        blank=True,
    )
