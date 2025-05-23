from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "employees"

    def ready(self):
        from .signals import (
            BntuDepartmentSignals,
            TradeUnionDepartmentSignals,
        )

        BntuDepartmentSignals.connect_signals()
        TradeUnionDepartmentSignals.connect_signals()
