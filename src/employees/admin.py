from django.contrib import admin


from .models import (
    EmployeeVersionModel,
    EmployeeModel,
    BntuPositionModel,
    AddressModel,
    PhoneNumberModel,
    EmailModel,
    TradeUnionPositionModel,
    RewardModel,
    RelativeModel,
    EducationalInstitutionModel,
    CommentModel,
)


def register():
    # region BNTU
    admin.site.register(BntuPositionModel),
    # endregion

    # region Contacts
    admin.site.register(PhoneNumberModel),
    admin.site.register(AddressModel),
    admin.site.register(EmailModel),
    # endregion

    # region Trade Union
    admin.site.register(TradeUnionPositionModel),

    # endregion

    # region Education

    admin.site.register(EducationalInstitutionModel)

    # endregion

    # region Other

    admin.site.register(RewardModel),
    admin.site.register(RelativeModel),

    admin.site.register(CommentModel)

    # endregion

    admin.site.register(EmployeeVersionModel)
    admin.site.register(EmployeeModel)


register()
