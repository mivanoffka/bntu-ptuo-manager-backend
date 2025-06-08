from operator import is_
from django_filters.rest_framework import (
    FilterSet,
    CharFilter,
    ModelChoiceFilter,
    ModelMultipleChoiceFilter,
    BooleanFilter,
)

from ..models.employee_model import EmployeeModel

from ..models.employee_version_model import EmployeeVersionModel
from references.models import (
    GenderModel,
    WorkingGroupModel,
    EducationLevelModel,
    AcademicDegreeModel,
)

from django.db.models import OuterRef, Subquery
from django.db.models import Q, F


from django_filters import rest_framework as filters


class EmployeeFilter(filters.FilterSet):
    birthdate_min = filters.CharFilter(field_name="latest_birthdate", lookup_expr="gte")
    birthdate_max = filters.CharFilter(field_name="latest_birthdate", lookup_expr="lte")
    gender_ids = filters.ModelMultipleChoiceFilter(
        field_name="latest_gender_id",
        queryset=GenderModel.objects.all(),
        to_field_name="id",
    )
    education_level_ids = filters.ModelMultipleChoiceFilter(
        field_name="latest_education_level_id",
        queryset=EducationLevelModel.objects.all(),
        to_field_name="id",
    )
    academic_degree_ids = filters.ModelMultipleChoiceFilter(
        field_name="latest_academic_degree_id",
        queryset=AcademicDegreeModel.objects.all(),
        to_field_name="id",
    )
    working_group_ids = filters.ModelMultipleChoiceFilter(
        field_name="latest_working_group_id",
        queryset=WorkingGroupModel.objects.all(),
        to_field_name="id",
    )
    is_archived = filters.BooleanFilter(field_name="latest_is_archived")
    is_retired = filters.BooleanFilter(field_name="latest_is_retired")

    class Meta:
        model = EmployeeModel
        fields = []
