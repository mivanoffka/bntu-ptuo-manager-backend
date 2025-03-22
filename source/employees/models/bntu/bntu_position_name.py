from typing import TYPE_CHECKING
from django.db import models


if TYPE_CHECKING:
    from django.db.models import Manager
    from .bntu_position import BntuPosition


class BntuPositionName(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=64)

    if TYPE_CHECKING:
        entrances = Manager[BntuPosition]
