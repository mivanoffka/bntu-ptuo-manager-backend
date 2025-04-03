from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmployeeView, GenerateView, EnumerationsView

employees_router = DefaultRouter()
employees_router.register("", EmployeeView, basename="")

urlpatterns = [
    path("employees", include(employees_router.urls)),
    path("generate/", GenerateView.as_view(), name="generate"),
    path("enumerations/", EnumerationsView.as_view(), name="enumerations"),
]
