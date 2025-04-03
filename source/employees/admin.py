from django.contrib import admin

from .models import (
    EmployeeVersionModel,
    NameModel,
    BntuDepartmentModel,
    BntuPositionModel,
    AddressModel,
    PhoneNumberModel,
    EmailModel,
    TradeUnionDepartmentModel,
    TradeUnionPositionModel,
    RewardModel,
    RelativeModel,
    EducationalInstitutionModel,
    WorkingGroupModel,
    PhoneNumberTypeModel,
    RelativeTypeModel,
    CommentModel,
    GenderModel,
    AcademicDegreeModel,
    EducationLevelModel,
    TradeUnionDepartmentOptionModel,
    WorkingGroupOptionModel,
)


def register():
    # region Common
    admin.site.register(NameModel),
    admin.site.register(GenderModel)
    # endregion

    # region BNTU
    admin.site.register(BntuPositionModel),
    admin.site.register(BntuDepartmentModel),
    # endregion

    # region Contacts
    admin.site.register(PhoneNumberModel),
    admin.site.register(AddressModel),
    admin.site.register(EmailModel),
    admin.site.register(PhoneNumberTypeModel)
    # endregion

    # region Trade Union
    admin.site.register(TradeUnionPositionModel),
    admin.site.register(TradeUnionDepartmentModel),
    admin.site.register(WorkingGroupModel),
    admin.site.register(TradeUnionDepartmentOptionModel),
    admin.site.register(WorkingGroupOptionModel),
    # endregion

    # region Education

    admin.site.register(EducationalInstitutionModel)
    admin.site.register(EducationLevelModel)
    admin.site.register(AcademicDegreeModel)

    # endregion

    # region Other
    admin.site.register(RewardModel),
    admin.site.register(RelativeModel),
    admin.site.register(RelativeTypeModel),
    admin.site.register(CommentModel)

    # endregion

    admin.site.register(EmployeeVersionModel)


register()
