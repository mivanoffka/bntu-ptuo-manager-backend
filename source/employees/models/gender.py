from django.db import models


class Gender(models.IntegerChoices):
    MALE = 0
    FEMALE = 1
