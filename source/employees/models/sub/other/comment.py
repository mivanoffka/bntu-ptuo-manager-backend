from django.db import models

from ...employee import Employee


class Comment(models.Model):
    id = models.AutoField(primary_key=True)

    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="comments"
    )

    comment = models.TextField(max_length=512)
