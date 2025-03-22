from typing import TYPE_CHECKING
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from ..employee import Employee

from .bntu_position import BntuPosition

if TYPE_CHECKING:
    from django.db.models import Manager


class BntuDepartment(MPTTModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    bntu_positions = models.ForeignKey(
        BntuPosition, on_delete=models.CASCADE, related_name="department"
    )

    parent = TreeForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="children"
    )

    if TYPE_CHECKING:
        children: Manager["BntuDepartment"]
