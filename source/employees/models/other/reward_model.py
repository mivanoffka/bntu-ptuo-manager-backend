from django.db import models

from ..employee_version_model import EmployeeVersionModel


class RewardModel(models.Model):
    class Meta:
        db_table = "rewards"

    id = models.AutoField(primary_key=True)

    employee_version = models.ForeignKey(
        EmployeeVersionModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    label = models.CharField(max_length=128)

    granted_at = models.DateTimeField(null=True, blank=True)

    comment = models.TextField(null=True, blank=True, max_length=512)
