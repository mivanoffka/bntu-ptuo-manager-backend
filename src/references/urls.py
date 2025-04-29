from rest_framework.routers import DefaultRouter
from .views import ReferencesViewSet

router = DefaultRouter()
router.register(r"", ReferencesViewSet, "")

urlpatterns = router.urls
