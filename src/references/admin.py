from django.contrib import admin

from .models import (
    ExemptionModel,
    PhoneNumberTypeModel,
    RelativeTypeModel,
    GenderModel,
    AcademicDegreeModel,
    EducationLevelModel,
    WorkingGroupModel,
)


def register():
    admin.site.register(GenderModel)
    admin.site.register(PhoneNumberTypeModel)
    admin.site.register(WorkingGroupModel),
    admin.site.register(EducationLevelModel)
    admin.site.register(AcademicDegreeModel)
    admin.site.register(RelativeTypeModel),
    admin.site.register(ExemptionModel)


register()
