from django.db import models

from ..employee import Employee


class EducationalInstitution(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    employees = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="educational_institutions",
        null=True,
        blank=True,
    )
