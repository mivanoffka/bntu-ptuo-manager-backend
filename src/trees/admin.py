from django.contrib import admin

from .models import BntuDepartmentModel, TradeUnionDepartmentModel


def register():
    admin.site.register(BntuDepartmentModel)
    admin.site.register(TradeUnionDepartmentModel)


register()
