from encodings.punycode import T
from django.db import models

from .trade_union_department_option_model import TradeUnionDepartmentOptionModel

from ..employee_version_model import EmployeeVersionModel
from ..abstract import TimestampedModel


class TradeUnionDepartmentRecordModel(models.Model):
    class Meta(TimestampedModel.Meta):
        db_table = "trade_union_department_records"

    id = models.AutoField(primary_key=True)

    employee_version = models.ForeignKey(
        EmployeeVersionModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    authentic_label = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    trade_union_department_option_path = models.CharField(
        max_length=255, null=True, blank=True
    )
