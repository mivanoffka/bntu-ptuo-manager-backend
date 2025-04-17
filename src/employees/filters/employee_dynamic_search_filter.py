from typing import Collection
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError

_PREFIX = "employee_versions"
_ALLOWED_FIELDS = ("first_name", "last_name", "middle_name", "birthplace")
_DEFAULT_FIELDS = ("first_name", "last_name", "middle_name")


class EmployeeDynamicSearchFilter(SearchFilter):
    def __convert_fields(self, values: Collection[str]):
        return (f"{_PREFIX}__{value}" for value in values)

    def get_search_fields(self, view, request):
        search_fields_param = request.query_params.get("search_fields", None)

        fields = _DEFAULT_FIELDS

        if search_fields_param:
            requested_fields = search_fields_param.split(",")
            valid_fields = [
                field for field in requested_fields if field in _ALLOWED_FIELDS
            ]
            if not valid_fields:
                raise ValidationError(
                    f"Invalid search fields. Allowed fields: {', '.join(_ALLOWED_FIELDS)}"
                )

            fields = valid_fields

        return self.__convert_fields(fields)
