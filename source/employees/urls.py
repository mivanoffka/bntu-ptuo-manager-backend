from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmployeesViewSet

employees_router = DefaultRouter()
employees_router.register("", EmployeesViewSet, basename="")


urlpatterns = [
    path("", include(employees_router.urls)),
]
