from rest_framework.routers import DefaultRouter
from .views import TreesViewSet

router = DefaultRouter()
router.register(r"", TreesViewSet, "")

urlpatterns = router.urls
