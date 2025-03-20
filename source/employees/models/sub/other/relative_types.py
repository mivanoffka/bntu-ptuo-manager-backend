from django.db import models


class RelativeType(models.IntegerChoices):
    NATIVE_CHILD = 0
    ADOPTED_CHILD = 1
