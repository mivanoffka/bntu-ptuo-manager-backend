from django.db import models

from ..employee_version_model import EmployeeVersionModel


class CommentModel(models.Model):
    class Meta:
        db_table = "comments"

    id = models.AutoField(primary_key=True)

    employee_version = models.ForeignKey(
        EmployeeVersionModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )

    value = models.TextField(max_length=512)
