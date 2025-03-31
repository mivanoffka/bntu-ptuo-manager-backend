from typing import TYPE_CHECKING
from django.db import models

from .working_group_option_model import WorkingGroupOptionModel

from ..employee_model import EmployeeModel

from ..abstract import TimestampedModel


class WorkingGroupModel(TimestampedModel):
    class Meta(TimestampedModel.Meta):
        db_table = "working_groups"

    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        EmployeeModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    working_group_option = models.ForeignKey(
        WorkingGroupOptionModel,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )
