from encodings.punycode import T
from django.db import models

from .trade_union_department_option import TradeUnionDepartmentOption

from ..employee import Employee
from ...utils.timestamp import Timestamped


class TradeUnionDepartment(Timestamped):
    class Meta(Timestamped.Meta):
        db_table = "trade_union_departments"

    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    trade_union_department_option = models.ForeignKey(
        TradeUnionDepartmentOption,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )
