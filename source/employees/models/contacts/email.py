from django.db import models

from ..employee import Employee


class Email(models.Model):
    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="emails"
    )

    value = models.CharField(max_length=128)

    comment = models.TextField(null=True, blank=True, max_length=512)
