from typing import List
from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
