from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ReferencesViewSet

router = DefaultRouter()
router.register(r"", ReferencesViewSet, "")

urlpatterns = [
    path("", include(router.urls)),
]
