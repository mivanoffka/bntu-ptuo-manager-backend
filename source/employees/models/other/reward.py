from django.db import models

from ..employee import Employee


class Reward(models.Model):
    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="rewards"
    )

    label = models.CharField(max_length=128)

    granted_at = models.DateTimeField(null=True, blank=True)

    comment = models.TextField(null=True, blank=True, max_length=512)
