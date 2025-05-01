from django.db import models

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager
    from employees.models import PhoneNumberModel, EmployeeVersionModel, RelativeModel


class EnumeratedModel(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=64)

    class Meta:
        abstract = True


class PhoneNumberTypeModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "phone_number_types"

    if TYPE_CHECKING:
        phone_numbers = RelatedManager[PhoneNumberModel]


class EducationLevelModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "education_levels"

    if TYPE_CHECKING:
        employees: RelatedManager[EmployeeVersionModel]


class GenderModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "genders"

    if TYPE_CHECKING:
        employees: RelatedManager[EmployeeVersionModel]


class AcademicDegreeModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "academic_degrees"

    if TYPE_CHECKING:
        employee_versions: RelatedManager[EmployeeVersionModel]


class RelativeTypeModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "relative_types"

    if TYPE_CHECKING:
        relatives = RelatedManager[RelativeModel]


class WorkingGroupModel(EnumeratedModel):
    class Meta(EnumeratedModel.Meta):
        db_table = "working_groups"

    if TYPE_CHECKING:
        employee_versions: RelatedManager[EmployeeVersionModel]
