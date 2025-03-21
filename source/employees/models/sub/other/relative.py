from django.db import models

from ...employee import Employee
from .relative_types import RelativeType


class Relative(models.Model):
    id = models.AutoField(primary_key=True)

    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="relatives"
    )

    full_name = models.CharField(max_length=128)

    birthdate = models.DateField(null=True)

    comment = models.TextField(null=True, blank=True, max_length=512)

    type = models.IntegerField(
        choices=RelativeType.choices,
    )
