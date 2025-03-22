from typing import TYPE_CHECKING
from django.db import models

from employees.models import Employee
from .bntu_position_name import BntuPositionName

if TYPE_CHECKING:
    from .bntu_department import BntuDepartment


class BntuPosition(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.ForeignKey(
        BntuPositionName, on_delete=models.CASCADE, related_name="entrances"
    )

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="bntu_positions"
    )

    if TYPE_CHECKING:
        department: BntuDepartment

    hired_at = models.DateTimeField(null=True, blank=True)
    is_discharged = models.BooleanField(default=False)
    discharged_at = models.DateTimeField(null=True, blank=True)
    is_discharged_voluntarily = models.BooleanField(null=True, blank=True)
    dischargement_comment = models.TextField(null=True, blank=True, max_length=512)
