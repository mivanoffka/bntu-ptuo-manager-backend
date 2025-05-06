from django.db import models


class ImageModel(models.Model):
    class Meta:
        db_table = "images"

    file = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
