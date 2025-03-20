from django.db import models


class PhoneNumberType(models.IntegerChoices):
    MOBILE = 0
    HOME = 1
