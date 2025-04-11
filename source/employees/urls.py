from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.tree_view_set import BntuDepartmentOptionViewSet

from .views import EmployeesViewSet

employees_router = DefaultRouter()

bntu_departments_router = DefaultRouter()

employees_router.register("employees", EmployeesViewSet, basename="employees")
bntu_departments_router.register(
    "bntu-departments", BntuDepartmentOptionViewSet, basename="bntu-departments"
)

urlpatterns = [
    path("", include(employees_router.urls)),
    path("", include(bntu_departments_router.urls)),
]
