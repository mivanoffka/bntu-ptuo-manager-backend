from typing import TYPE_CHECKING
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from source.employees.models import Employee

if TYPE_CHECKING:
    from django.db.models import Manager
    from source.employees.models.parts.bntu.bntu_position import BntuPosition


class BntuDepartment(MPTTModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    working_positions = models.ForeignKey(
        BntuPosition, on_delete=models.CASCADE, related_name="department"
    )

    parent = TreeForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="children"
    )

    if TYPE_CHECKING:
        children: Manager["BntuDepartment"]
