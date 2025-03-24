from django.db import models

from ..employee import Employee
from .phone_number_type import PhoneNumberType


class PhoneNumber(models.Model):
    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="phone_numbers",
        null=True,
        blank=True,
    )

    value = models.CharField(max_length=255)

    phone_number_type = models.ForeignKey(
        PhoneNumberType, on_delete=models.CASCADE, null=True, blank=True
    )

    comment = models.TextField(null=True, blank=True, max_length=512)
