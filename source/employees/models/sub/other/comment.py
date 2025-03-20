from django.db import models

from source.employees.models import Employee


class Comment(models.Model):
    id = models.AutoField(primary_key=True)

    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="comments"
    )

    comment = models.TextField(null=True, blank=True, max_length=512)
