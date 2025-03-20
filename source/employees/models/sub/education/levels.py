from django.db import models


class EducationLevels(models.IntegerChoices):
    PRIMARY = 0
    MIDDLE = 1
    HIGH = 2
