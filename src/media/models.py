from django.db import models

from .utils import upload_to_images


class ImageModel(models.Model):
    class Meta:
        db_table = "images"

    file = models.ImageField(upload_to=upload_to_images)
    uploaded_at = models.DateTimeField(auto_now_add=True)
