from django.db import models


class EnumeratedModel(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=64)

    class Meta:
        abstract = True
