from typing import TYPE_CHECKING
from django.db import models

from employees.models import Employee
from .bntu_department import BntuDepartment


class BntuPosition(models.Model):
    class Meta:
        db_table = "bntu_positions"

    id = models.AutoField(primary_key=True)

    label = models.CharField(max_length=255)

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    department = models.ForeignKey(
        BntuDepartment,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )

    hired_at = models.DateTimeField(null=True, blank=True)
    is_discharged = models.BooleanField(default=False)
    discharged_at = models.DateTimeField(null=True, blank=True)
    is_discharged_voluntarily = models.BooleanField(null=True, blank=True)
    dischargement_comment = models.TextField(null=True, blank=True, max_length=512)
