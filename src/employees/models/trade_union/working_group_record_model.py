from typing import TYPE_CHECKING
from django.db import models

from .working_group_option_model import WorkingGroupOptionModel

from ..employee_version_model import EmployeeVersionModel

from ..abstract import TimestampedModel


class WorkingGroupRecordModel(models.Model):
    class Meta(TimestampedModel.Meta):
        db_table = "working_group_records"

    id = models.AutoField(primary_key=True)

    employee_version = models.ForeignKey(
        EmployeeVersionModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    authentic_label = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    working_group_option = models.ForeignKey(
        WorkingGroupOptionModel,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )
