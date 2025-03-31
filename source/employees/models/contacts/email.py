from django.db import models

from ..employee import Employee


class Email(models.Model):
    class Meta:
        db_table = "emails"

    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    value = models.CharField(max_length=128)

    comment = models.TextField(null=True, blank=True, max_length=512)
