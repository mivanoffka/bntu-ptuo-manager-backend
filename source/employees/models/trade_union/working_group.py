from typing import TYPE_CHECKING
from django.db import models

from .working_group_option import WorkingGroupOption

from ..employee import Employee

from ...utils.timestamp import Timestamped


class WorkingGroup(Timestamped):
    class Meta(Timestamped.Meta):
        db_table = "working_groups"

    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    working_group_option = models.ForeignKey(
        WorkingGroupOption,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )
