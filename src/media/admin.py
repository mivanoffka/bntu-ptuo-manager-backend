from django.contrib import admin
from .models import ImageModel


def register():
    admin.site.register(ImageModel)


register()
