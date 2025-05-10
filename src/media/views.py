from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ImageModel
from .serializers import ImageSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@permission_classes([IsAuthenticated])
class ImagesViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]
