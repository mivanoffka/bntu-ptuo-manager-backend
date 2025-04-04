from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.employees_view_set import EmployeesViewSet

from .views import EmployeeVersionViewSet, GenerateView, EnumerationsView

employees_versions_router = DefaultRouter()
employees_versions_router.register("", EmployeeVersionViewSet, basename="")

employees_router = DefaultRouter()
employees_router.register("", EmployeesViewSet, basename="")


urlpatterns = [
    path("versions/", include(employees_versions_router.urls)),
    path("employees/", include(employees_router.urls)),
    path("generate/", GenerateView.as_view(), name="generate"),
    path("enumerations/", EnumerationsView.as_view(), name="enumerations"),
]
