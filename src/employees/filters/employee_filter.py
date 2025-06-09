from ..models.employee_model import EmployeeModel

from references.models import (
    ExemptionModel,
    GenderModel,
    WorkingGroupModel,
    EducationLevelModel,
    AcademicDegreeModel,
)

from django.db.models import Q


from django_filters import rest_framework as filters


class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


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
    exemption_ids = filters.ModelMultipleChoiceFilter(
        field_name="latest_exemptions",
        queryset=ExemptionModel.objects.all(),
        to_field_name="id",
    )
    is_archived = filters.BooleanFilter(field_name="latest_is_archived")
    is_retired = filters.BooleanFilter(field_name="latest_is_retired")

    trade_union_department_paths = CharInFilter(
        field_name="trade_union_department_paths",
        method="filter_trade_union_department_paths",
        lookup_expr="startswith",
    )

    def filter_trade_union_department_paths(self, queryset, name, value):
        values = self.request.query_params.getlist(name)

        if not values:
            return queryset

        query = Q()
        for val in values:
            query |= Q(latest_trade_union_department_path__startswith=val)

        return queryset.filter(query)

    bntu_department_paths = CharInFilter(
        field_name="bntu_department_paths",
        method="filter_bntu_department_paths",
        lookup_expr="startswith",
    )

    def filter_bntu_department_paths(self, queryset, name, value):
        values = self.request.query_params.getlist(name)
        if not values:
            return queryset

        query = Q()
        for val in values:
            query |= Q(
                employee_versions__bntu_positions__bntu_department_path__startswith=val
            )

        return queryset.filter(query).distinct()

    class Meta:
        model = EmployeeModel
        fields = []

    bntu_position_labels = CharInFilter(
        field_name="bntu_position_labels", method="filter_bntu_position_labels"
    )

    def filter_bntu_position_labels(self, queryset, name, value):
        values = self.request.query_params.getlist(name)

        if not values:
            return queryset

        query = Q()
        for val in values:
            query |= Q(employee_versions__bntu_positions__label__iregex=rf"\m{val}")

        return queryset.filter(query).distinct()
