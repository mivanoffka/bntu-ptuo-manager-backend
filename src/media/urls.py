from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ImagesViewSet

images_router = DefaultRouter()
images_router.register(r"images", ImagesViewSet, "images")

urlpatterns = [
    path("", include(images_router.urls)),
]
