from rest_framework.routers import DefaultRouter
from .views import EmployeesViewSet

employees_router = DefaultRouter()
employees_router.register(r"", EmployeesViewSet, "")

urlpatterns = employees_router.urls
