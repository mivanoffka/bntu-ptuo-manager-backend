from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from .models import ImageModel
from .serializers import ImageSerializer


class ImageViewSet(ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
