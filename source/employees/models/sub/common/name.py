from django.db import models

from source.employees.models import Employee


class Name(models.Model):
    id = models.AutoField(primary_key=True)

    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="names"
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)

    createdAt = models.DateTimeField(auto_now_add=True)
