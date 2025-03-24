from django.db import models

from ..employee import Employee
from .relative_types import RelativeType


class Relative(models.Model):
    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="relatives"
    )

    full_name = models.CharField(max_length=128)

    birthdate = models.DateTimeField(null=True)

    comment = models.TextField(null=True, blank=True, max_length=512)

    relative_type = models.ForeignKey(
        RelativeType, on_delete=models.CASCADE, null=True, blank=True
    )
