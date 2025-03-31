from django.db import models

from ..employee import Employee


class Comment(models.Model):
    class Meta:
        db_table = "comments"

    id = models.AutoField(primary_key=True)

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    value = models.TextField(max_length=512)
