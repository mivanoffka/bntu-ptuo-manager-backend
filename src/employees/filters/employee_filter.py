from django_filters.rest_framework import (
    FilterSet,
    CharFilter,
    ModelChoiceFilter,
    ModelMultipleChoiceFilter,
)

from ..models import (
    GenderModel,
    WorkingGroupModel,
    EducationLevelModel,
    AcademicDegreeModel,
)


class EmployeeFilter(FilterSet):
    birthdate_min = CharFilter(
        field_name="employee_versions__birthdate", lookup_expr="gte"
    )
    birthdate_max = CharFilter(
        field_name="employee_versions__birthdate", lookup_expr="lte"
    )
    gender_ids = ModelMultipleChoiceFilter(
        queryset=GenderModel.objects.all(),
        field_name="employee_versions__gender",
        to_field_name="id",
        blank=True,
        conjoined=False,
    )
    academic_degree_ids = ModelMultipleChoiceFilter(
        queryset=AcademicDegreeModel.objects.all(),
        field_name="employee_versions__academic_degree",
        to_field_name="id",
        blank=True,
        conjoined=False,
    )
    education_level_ids = ModelMultipleChoiceFilter(
        queryset=EducationLevelModel.objects.all(),
        field_name="employee_versions__education_level",
        to_field_name="id",
        blank=True,
        conjoined=False,
    )
    working_group_ids = ModelMultipleChoiceFilter(
        queryset=WorkingGroupModel.objects.all(),
        field_name="employee_versions__working_group",
        to_field_name="id",
        blank=True,
        conjoined=False,
    )
