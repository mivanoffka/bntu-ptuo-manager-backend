from typing import TYPE_CHECKING
from django.db import models


from ..employee_version_model import EmployeeVersionModel


class EducationalInstitutionModel(models.Model):
    class Meta:
        db_table = "educational_institutions"

    id = models.AutoField(primary_key=True)

    label = models.CharField(max_length=255)

    graduated_at = models.DateTimeField(null=True, blank=True)

    comment = models.TextField(null=True, blank=True, max_length=512)

    employee_version = models.ForeignKey(
        EmployeeVersionModel, on_delete=models.CASCADE, related_name=Meta.db_table
    )
