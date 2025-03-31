from django.db import models

from ..employee import Employee
from ...utils.timestamp import Timestamped


class Name(Timestamped):
    class Meta(Timestamped.Meta):
        db_table = "names"

    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)

    createdAt = models.DateTimeField(auto_now_add=True)
