from typing import TYPE_CHECKING
from django.db import models

from employees.models import Employee

if TYPE_CHECKING:
    from employees.models.sub.bntu.bntu_department import BntuDepartment


class BntuPosition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="bntu_positions"
    )

    if TYPE_CHECKING:
        department: BntuDepartment

    hiredAt = models.DateTimeField(null=True, blank=True)
    isDischarged = models.BooleanField(default=False)
    dischargedAt = models.DateTimeField(null=True, blank=True)
    isDischargedVoluntarily = models.BooleanField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True, max_length=512)
