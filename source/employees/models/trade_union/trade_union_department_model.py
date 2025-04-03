from encodings.punycode import T
from django.db import models

from .trade_union_department_option_model import TradeUnionDepartmentOptionModel

from ..employee_model import EmployeeVersionModel
from ..abstract import TimestampedModel


class TradeUnionDepartmentModel(TimestampedModel):
    class Meta(TimestampedModel.Meta):
        db_table = "trade_union_departments"

    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        EmployeeVersionModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    trade_union_department_option = models.ForeignKey(
        TradeUnionDepartmentOptionModel,
        on_delete=models.CASCADE,
        related_name=Meta.db_table,
        null=True,
        blank=True,
    )
