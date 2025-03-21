from django.db import models


class AcademicDegree(models.IntegerChoices):
    NONE = 0
    A = 1
    B = 2
