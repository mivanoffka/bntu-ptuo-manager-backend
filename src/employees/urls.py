from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    EmployeesViewSet,
    BntuDepartmentViewSet,
    TradeUnionDepartmentViewSet,
    EnumerationsViewSet,
)

employees_router = DefaultRouter()
bntu_departments_router = DefaultRouter()
trade_union_departments_router = DefaultRouter()
enumerations_router = DefaultRouter()

employees_router.register("employees", EmployeesViewSet, basename="employees")

bntu_departments_router.register(
    "bntu-departments", BntuDepartmentViewSet, basename="bntu-departments"
)

trade_union_departments_router.register(
    "trade-union-departments",
    TradeUnionDepartmentViewSet,
    basename="trade-union-departments",
)

enumerations_router.register(
    "enumerations", EnumerationsViewSet, basename="enumerations"
)

urlpatterns = [
    path("", include(employees_router.urls)),
    path("", include(bntu_departments_router.urls)),
    path("", include(trade_union_departments_router.urls)),
    path("", include(enumerations_router.urls)),
]
