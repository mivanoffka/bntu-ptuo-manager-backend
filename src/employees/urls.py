from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import EmployeesViewSet, EmployeeVersionsViewSet

employees_router = DefaultRouter()
employees_router.register(r"", EmployeesViewSet, "")

employee_versions_detail = EmployeeVersionsViewSet.as_view(
    {"get": "retrieve", "delete": "destroy"}
)
employee_versions_restore = EmployeeVersionsViewSet.as_view({"patch": "restore"})

urlpatterns = [
    path(
        "<int:id>/versions/<str:created_at>/",
        employee_versions_detail,
    ),
    path("<int:id>/versions/<str:created_at>/restore/", employee_versions_restore),
    *employees_router.urls,
]
